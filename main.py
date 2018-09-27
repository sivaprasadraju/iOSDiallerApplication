from add import AddContact
from search import Search


class Main:

    AlphabetDict = {0: [' '], 1: [''], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
	
	ContactNames = ['Keanu Reeves', 'Brad Pitt', 'Trisha', 'Vijay Sethupathy']
    ContactNumbers = [9685768789, 9687783421, 9743274880, 9949083597]
	
	Data = {}

    Data = dict(zip(ContactNames, ContactNumbers))
	
	print('1.Adding contact, 2. Search contact')

    preference = input('Enter your preference : ')

    if(preference == 1):
        name = raw_input('Enter name of the new contact : ')
        number = input('Enter number of the new Number : ')
        AddContact(name, number, Data)
        NewPreference = input('Enter your New preference : ')
        if(NewPreference == 1):
            name1 = raw_input('Enter name of the new contact : ')
            number1 = input('Enter number of the new Number : ')
            AddContact(name1, number1, Data)
        elif(NewPreference == 2):
            Input = input('Enter number : ')
            Search(Input, Data, AlphabetDict)

    elif(preference == 2):
        Input = input('Enter number : ')
        Search(Input, Data, AlphabetDict)
