

# Python Task Level 1 :

def oddAndEvenInList(x,y):
    '''
    This function takes 2 numbers and print 2 lists
    containing the odd and even Numbers in the two numbers
    range
    '''
    oddList = []
    evenList = []
    for num in range(x,y):
        if num % 2 == 0:
            evenList.append(num)
        elif num % 2 != 0:
           oddList.append(num)
    print(f'Odd Numbers between {x} and {y} is : {oddList}')
    print(f' Even Numbers Between {x} and {y} is : {evenList}')
    
print('================================================================')           
oddAndEvenInList(2,50)
print('================================================================')     
def CanDividedBy(x,y):
    result = []
    for num in range(1,101):
        if num % x == 0 and num % y == 0:
            result.append(num)
    print(f'The numbers between 1 and 100 that can divided between two given Numbers is {result}')

CanDividedBy(4,6)
print('================================================================')     
def multiplicationTable(x,y):
    '''
    function print multiplication table in range between two given numbers
    '''
    for n1 in range(x,y +1):
        for n2 in range(1,y +1):
            print(f'{n1} X {n2} = {n1*n2}' )
print('================================================================')     
multiplicationTable(2,10)

def sentenceWithoutDuplicate(sent):
    result = []
    words = sent.split()
    for w in words:
        if w not in result:
            result.append(w)
    print(' '.join(result))
   
print('================================================================')      
    
sentenceWithoutDuplicate('ali qais age is ali qais 38 ')

def countWordsWithoutSpaces(sent):
    words = sent.split()
    numOfWords = 0
    for w in words:
        numOfWords+=1
    print(numOfWords)
print('================================================================')   
countWordsWithoutSpaces('ali qais age is ali qais 38')


def removSpicificWordFromSentence(sent,word):
    print(sent.replace(word,''))


print('================================================================')  
removSpicificWordFromSentence('ali qais age is ali qais 38','ali')


def countWordOccurInSentence(sent,word):
    temp = sent.split()
    num = 0
    for w in temp:
        if w == word:
            num+=1

    print(num)


print('================================================================')  
countWordOccurInSentence('ali qais age is ali ali qais 38','ali')

print('================================================================')



def dividedBySecondVarfromFirstTo100(x,y):
    result = []
    for num in range(x,101):
        if num % y == 0:
            result.append(num)
    print(result)
dividedBySecondVarfromFirstTo100(5,7)


