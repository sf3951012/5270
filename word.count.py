from mrjob.job import MRJob 
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCount(MRJob):
	def mapper(self, _, line):
		for word in WORD_RE.findall(line):
			yield (word.lower(),1)
			# yield is a list of returned items
	def reducer(self, word, count):
		# count is a list
		yield (word, sum(count))

MRWordCount.run()
