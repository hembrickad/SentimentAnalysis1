'''
Adrienne Hembrick
April 8, 2021

Problem: Find the accuracy for prediction based programs

Description: the scorer will take in two files, a test file and a key file,the
code will then take the files and make the answers a list

Instructions: In the terminal after compiling the file place the test file along with a
'>' character and the file you want the information to be moved to.

Example:

    python scorer.py sentiment-test.txt sentiment-key.txt > sentiment-report.txt

    74.3%

             Negative	Positive
    Negative	5	 3
    Positive	3	 5
    
Results:

Baseline:

             Negative	Positive
    Negative	5	 3
    Positive	3	 5
    
 

'''
## IMPORTS ##
import sys
import re
import random
from collections import defaultdict

##### GLOBAL VARIABLES #####
TPH = 0
TPR = 0
FPH = 0
FPR = 0

### METHODS ###

#Inputs Test Files
def input(arg2):
    sent = ""
    g = open(arg2, 'r')
    sent += g.read() #groups lines into a file
    sent = sent.upper() #ensures all words are lowercase for sorting
    return sent

#splits the lists
def split(strs):
    new = re.split("\n",strs)
    for x in range(len(new)):
        new[x] = new[x].strip()
    while '' in new:
       new.remove('')
    return new
    


# Calculates the accuracy
def scoreCal(l1,l2):
    i = 0.0
    y = 0.0
    
    global TPH
    global TPR
    global FPH
    global FPR
    
    for x in range(len(l1)):
        if l1[x] == l2[x]:
            i += 1
            
            if bool(re.search("PHONE", l2[x])):
                    TPH += 1
            else:
                    TPR += 1
        else:
            if bool(re.search("PHONE", l2[x])):
                    FPH += 1
            else:
                    FPR += 1
        y += 1
    rawScore = i/y*100
    print("Score:" + format(rawScore,'^-.2f') + "%")

# Makes a confusion Matrix
def confusionM ():
    print("\tNegative\tPositive\t")
    print("Negtaive\t" + "{}".format(TPH) + "\t" + "{}".format(FPR))
    print("Positive\t" + "{}".format(FPH) + "\t" + "{}".format(TPR))
    


### MAIN METHOD ###

tester = sys.argv[1]    
scorer = sys.argv[2]

t = split(input(tester))
s = split(input(scorer))

scoreCal(t, s)
    
confusionM()
      
