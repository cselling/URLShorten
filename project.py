import webbrowser
import json
import random
import string
path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" #to open chrome with webbrowser
with open('data.json', 'r') as inFile: #dictionary is saved between sessions
    data = json.load(inFile)           # loading the dictionary
while(True):
    print("Input: ", end = '') 
    x = input().split() # get user input broken up into words
    match x[0].upper(): # first word is a command # second word is content
        case 'EXIT':
            break  # breaks loop and exits program successfully
        case 'STORE':  # store website
            key = ''  # key generation 'AA##'
            key += ''.join(random.choices(string.ascii_uppercase, k = 2))
            key += ''.join(random.choices(string.digits, k = 2)) 
            data[key] = x[1] # append new pair to the dictionary
            print("%s: %s" % (key, x[1])) # display new entry for saving
            with open('data.json', 'w') as outFile: # write to file
                json.dump(data, outFile)
        case 'KEY': # key key # opens up website by key
            webbrowser.get(path).open_new(data[x[1]])
        case 'KEYS': # displays all key: value pairs
            for x in data:
                print('%s: %s' % (x, data[x]))
        case 'BROWSE': # browse url # just opens up browser at website
            webbrowser.get(path).open_new(x[1])
        case default:
            print("Incorrect command: 'EXIT', 'STORE', 'KEY', 'KEYS', 'BROWSE'")


