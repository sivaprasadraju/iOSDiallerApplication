class Main:

    AlphabetDict = {0: [' '], 1: [''], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
	
	ContactNames = ['Keanu Reeves', 'Brad Pitt', 'Trisha', 'Vijay Sethupathy']
    ContactNumbers = [9685768789, 9687783421, 9743274880, 9949083597]
	
	Data = {}

    Data = dict(zip(ContactNames, ContactNumbers))
