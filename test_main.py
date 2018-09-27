from unittest import TestCase

class TestMain(TestCase):
    def TestCaseForAlphabetDictDictionary(self):
        self.assertEqual(Main().AlphabetDict[2], ['a', 'b', 'c'])
	
	def TestCaseForDataDictionary(self):
        self.assertEqual(Main().Data['Trisha'], 9743274880)
