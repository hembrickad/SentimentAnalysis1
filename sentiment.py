'''
Adrienne Hembrick
April 27, 2021

Problem:Through the use of a training file the code tries to use context to find whether
a tweets sentiment is either positive or negative.

Description:The sentiment code first takes in both files that the user gives through the terminal and capitolizes the words
The listTrain() splits the training list text between a negative list and a positive list depending on whether the answer
tag says "negative" or "postive". concat() and sep() splits the list and forms a better seperated
list. tot() forms default dictionaries. listTest() starts to prepare the answers by locating the id of all of the test data and places the words
assoicated into a test-list. associate() predicts whether or not a word is associated with "negative" or "postive" based on
the popularity of words before and after line for each association. format() finishes formatting the answer by
placing the associationg and combo() makes the list into a string.




Instructions: In the terminal after compiling the file place the test file along with a
'>' character and the file you want the information to be moved to.

    python3 sentiment.py sentiment-train.txt sentiment-test.txt my-model.txt > my-sentiment-answers.txt

    Input:

        <corpus lang="en">
        <lexelt item="sentiment">
        <instance id="620979391984566272">
        <context>
        On another note, it seems Greek PM Tsipras married Angela Merkel to Francois Hollande on Sunday #happilyeverafter http://t.co/gTKDxivf79
        </context>
        </instance>

    Output:

        <answer instance="620821002390339585" sentiment="negative"/>

Results:

Score:68.97%
	Negative	Positive	
Negtaive	0	 0
Positive	72	 160

'''

###### IMPORTS ######
import sys
import re
import random
from collections import defaultdict
import math
###### GLOBAL VARIABLES ######

pList = list()
nList = list()

pBag = defaultdict(int)
nBag = defaultdict(int)

wordTest = list()

answTest = list()

###### METHODS ######
# Input for training data
def inputTrain(args):
    sent = " "
    g = open(args, 'r')
    sent += g.read()
    sent = sent.upper()
    return sent

#Make input file a list of words
def listTrain(values):
    global nList,pList
    new = re.split("\n",values)
    for x in range(len(new)):
        if re.search('<ANSWER INSTANCE=',new[x]):
            if bool(re.search("NEGATIVE", new[x])):
                nList.append(new[x+2])
            else:
                pList.append(new[x+2])
                
#seperates words for the files
#also seperates some puncutation that usually repeats
def sep(sent):
    sent = sent.replace("?", " ?")
    sent = sent.replace("!", " !")
    sent = sent.replace(".", "")
    sent = sent.replace("(", "( ")
    sent = sent.replace(")", " )")
    sent = sent.replace("\"", "")
    l = sent.split(" ")
    while '' in l:
       l.remove('')
    return l
        
#Divides the training data into seperate lists
def concat(l):
    n = " "
    return sep(n.join(l))

#Creates Default Dictionaries 
def tot(l):
    tol = defaultdict(int)
    for x in l:
        tol[x] += 1
    return tol 

# Input for testing data a prepares answer list for solutions
def listTest(values):
    #values = values.replace("\n", " <<end>> \n")
    new = re.split("\n", values)
    words = list()
    global answTest, wordTest

    for x in range(len(new)):
        if bool(re.search('<INSTANCE ID',new[x])):
            new[x] = new[x].replace('<INSTANCE ID','')
            new[x] = new[x].replace('>','')
            new[x] = new[x].lower()
            words.append(new[x+2])
            answTest.append('<answer instance' + new[x] + " sentiment=" )
    wordTest = (words)



#Finds the most likely word association point for the test document  
def associate():
    pCounter = 0
    nCounter = 0
    num = 0

    for x in wordTest:
        for k in x:
            p = pBag.get(k, 0) 
            n = nBag.get(k, 0)
            if(p > n):
                pCounter += 1
            elif(p < n):
                nCounter += 1
            #print(nCounter , " " , pCounter, " ",)
        if(pCounter > nCounter):
            format(num, "\"positive\"")
            num += 1
        elif(pCounter < nCounter):
            format(num, "\"negative\"")
            num += 1
        elif (pCounter == nCounter and pCounter <= 2):
            format(num, "\"negative\"")
            num += 1
            print(num)
        else:
            format(num, "\"positive\"")

            num += 1

        pCounter = 0
        nCounter = 0
            

#completes answers in the answer list for output           
def format(pl, answ):
    answTest[pl] += answ + '/>\n'

#combines the words into text
def combo():
    global answTest
    comb = ' '
    return (comb.join(answTest))


##### MAIN PROCESS #####
train = sys.argv[1]
test = sys.argv[2]

listTrain(inputTrain(train))
listTest(inputTrain(test))


pBag = tot(concat(pList))
nBag = tot(concat(nList))

associate()

f = combo()
print(f)


