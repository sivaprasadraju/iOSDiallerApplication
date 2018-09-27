def Search(Input, Data, AlphabetDict):

    combinations = []
    SearchList = []
    NameOutput = None
    NumberOutput = None

    def combine(terms, accum):
        last = (len(terms) == 1)
        n = len(terms[0])
        for i in range(n):
            item = accum + terms[0][i]
            if last:
                combinations.append(item)
            else:
                combine(terms[1:], item)



    UserInput = list(str(Input))

    UserInputString = str(Input)

    for i in range(len(UserInput)):
        for key, value in AlphabetDict.items():
            if UserInput[i] == str(key):
                SearchList.append(value)

    combine(SearchList, '')

    for key1, value1 in Data.items():
        for j in range(len(combinations)):
            if combinations[j] in key1.lower():
                NameOutput = key1

    for key, value in Data.items():
        if UserInputString in str(value):
            NumberOutput = key

    if NameOutput != None:
        print(NameOutput)
    elif NumberOutput != None:
        print(NumberOutput)
    else:
        print('No Contact')