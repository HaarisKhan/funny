import sys

def setup():
    if len(sys.argv) > 1:
        f = sys.argv[1]
    else:
        print("No file passed. Using path-to-dict.txt...")
        f = "path-to-dict.txt"
    return f

def divideIntoWords(f):
    s = dictionary.read()
    return s.split()

def solve(anagrams, s):
    lst = []
    for word in anagrams:
        for element in s:
            if (checkWord(word, element)):
                lst.append(element)
    return lst

def checkWord(s1, s2):
    if (len(s1) != len(s2)):
        return False
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 != c2 and c1 != c2.upper() and c1.upper != c2 and c1.upper != c2.upper():
            return False
    return True

def getInput():
    userInput = input("Enter a string: ")
    if userInput == "":
        print("Error: No input found")
        print("Exiting... ")
        sys.exit(0)
    return userInput

def dictMe(string):
    dictionary = {}
    for letter in string:
        if letter.lower() in dictionary:
            dictionary[letter.lower()] += 1
        else:
            dictionary[letter.lower()] = 1
    return dictionary

# Calling the functions

f = setup()
dictionary = open(f, "r")
words = divideIntoWords(dictionary)
s = set(words)

user = getInput()

permutations = dictMe(user)

toSort = []

for element in s:
    if dictMe(element) == permutations:
        toSort.append(element)

if toSort != None and toSort != []:
    toSort = set(toSort) # Remove Duplicates
    toSort = list(toSort) # Change to list to sort
    toSort.sort() # Sort
    for element in toSort:
        print(element, end = " ")
    print()
else:
    print("-")
