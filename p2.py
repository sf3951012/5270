from mrjob.job import MRJob 
import re
from mrjob.step import MRStep
import math
import numpy as np
import sys

n_re = re.compile(r"^[0-9]+$")

class MRCalPi(MRJob):
	def steps(self):
		return [ MRStep(mapper = self.mapper_generateRandomSample,
						reducer = self.reducer_group_samples),
				 MRStep(reducer = self.reducer_report_pi)
				]

	def mapper_generateRandomSample(self, _, N):
		#num = int(n)
		for i in range(int(N)):
			yield (np.random.uniform(-1,1), np.random.uniform(-1,1)), int(N)
			# yield is a list of returned items

	def reducer_group_samples(self,pairs,n):
		if math.sqrt((pairs[0])**2 + pairs[1]**2) <= 1.0 :
			yield (True, sum(n)),1

		
	def reducer_report_pi(self, pair,count):
		yield pair[0],(sum(count)/pair[1] ) * 4

MRCalPi.run()
# python3 word_max.py 
