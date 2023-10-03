# Python Task Level 2 :

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

'''
#1-A
upperNames = []
for name in Names:
    upperNames.append(name.upper())

print(upperNames)

'''
'''
#1-B
print([n.upper() for n in Names])
'''

'''
#1-C
def myUper(n):
    return n.upper()

newUper = map(myUper,Names)

print('using functional programming')
print(type(newUper))
print(list(newUper))

'''
'''
#2-A
containsA = []
for n in Names:
    if 'a' in n:
        containsA.append(n)

print(containsA)

'''

'''
#2-B
print([n for n in Names if 'a' in n])
'''

'''
#2-C
def filterForA(n):
    temp = [n for n in Names if 'a'  in n]
    return temp

new = filter(filterForA,Names)
print(type(new))
print(list(new))

'''
'''
#3-A
startwithT = []
for n in Names:
    if n.startswith('t'):
        startwithT.append(n)
print(startwithT)
'''

'''
#3-B
print([n for n in Names if n.startswith('t')])

'''
'''
#3-C
def startWithT(n):
    if n.startswith('t'):
        return n

new = filter(startWithT,Names)
print(list(new))
'''

'''
#4-A
mort = []
for n in Names:
    if n.count('a') >= 2:
        mort.append(n)
print(mort)

'''
'''
#4-B
print([n for n in Names if n.count('a') >=2])
'''

""" #4-c
def morthantwoAchar(n):
    if n.count('a') >=2:
        return(n)
new = filter(morthantwoAchar,Names)
print(list(new))
 """
""" #5-A
lenOfEachItem = []
for n in Names:
    lenOfEachItem.append(len(n))
print(lenOfEachItem)

#5-B
print([len(x) for x in Names])
 """

""" #5-C
def lenOfItemsInList(n):
    return len(n)

new = map(lenOfItemsInList,Names)
print(list(new)) """



#6-A

a,*b = Names
print(f'{Names.index(a)}   {b}')

#6-B
a , *_ , b = Names
print (f'{a}   {b}')

#6-C
a , b , *_ = Names
print (f'{a}   {b}')

""" for i , n in enumerate(Names):
    print(f'{i}    {n}') """