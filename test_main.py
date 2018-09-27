from unittest import TestCase

class TestMain(TestCase):
    def TestCaseForAlphabetDictDictionary(self):
        self.assertEqual(Main().AlphabetDict[2], ['a', 'b', 'c'])
	
	def TestCaseForDataDictionary(self):
        self.assertEqual(Main().Data['Trisha'], 9743274880)
	
	def TestCaseForAddFunction(self):
        self.assertEqual(AddContact('siva',9542199855,Data={'prasad':9182961266, 'raju':9490738146}),3)
		
	def TestCaseForFirstName(self):
        self.assertEqual(Search(7482, Data={'siva raju': 9542199855, 'prasad bairaju': 9490738146}, AlphabetDict={2: ['a', 'b', 'c'], 4: ['g', 'h', 'i'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v']}), 'siva raju')

