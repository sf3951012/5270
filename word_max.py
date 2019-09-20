from mrjob.job import MRJob 
import re
from mrjob.step import MRStep


WORD_RE = re.compile(r"[\w']+")

class MRWordMax(MRJob):
	def steps(self):
		return [ MRStep(mapper = self.mapper_get_words,
						reducer = self.reducer_count_words),
				 MRStep(reducer = self.reducer_find_max)
				]

	def mapper_get_words(self, _, line):
		for word in WORD_RE.findall(line):
			yield (word.lower(),1)
			# yield is a list of returned items

	def reducer_count_words(self, word, count):
		# count is a list
		yield None, (sum(count), word)

	def reducer_find_max(self, _, pairs):
		yield max(pairs)
	

MRWordMax.run()
# python3 word_max.py solution.txt