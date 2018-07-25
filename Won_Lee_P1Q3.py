# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:00:03 2018

@author: Study Won

THIS VERSION DOES NOT STRIP OUT THE AUTHOR'S NAME
"""


allquotes = [] #list of all quotes

#reads the file and gives us a list of full quotes
def main():
    
    with open('quotes.txt') as file:
        lines = file.readlines() #list of all lines in the file
        for x in range (0, len(lines), 2):
            allquotes.append("\"" + lines[x].rstrip() + " -" + lines[x+1].rstrip() + "\"") # Solves A
    """        
    print (wordsFromFullQuote(allquotes[1])) # Solves B
    print (dictionaryFromAllQuotes()) # Solves C
    print (reverseDictionaryFromAllQuotes()) # Solves D
    """
    print (getTfIdf("roads", allquotes[1])) # Solves E
    """
    print (searchByWord("days")) # Solves F
    print (searchByWordList(["days", "world", "i"])) # Solves G
    """
    
    return

"""
    with open('quotes.txt') as file:
        i = 0
        lines = file.readlines()
        while i < len(lines)-1:
            line = str(lines[i]+ " - " +lines[i+1])
            line = line.replace('\r\n','')
            line=line.replace('\n','')
            allquotes.append(line)
            i += 2
    print allquotes
"""

#splits a quote into words
def splitQuote(fullquote):
    import re
    return re.split('\W+', fullquote)

#generates a word list from a single quote
def wordsFromFullQuote(fullquote):
    wordlist = []
    for w in splitQuote(fullquote): #split the quote into words
        if w: #ignore empty words
            wordlist.append(w.lower()) #lowercase the words and add them to the list
    return wordlist

#generates a postings-list dictionary
def dictionaryFromAllQuotes():
    pldict = {}
    plsingledict = {}
    for fullquote in allquotes: #for each quote in our list
        wordlist = wordsFromFullQuote(fullquote) #split the quote into words
        for word in wordlist: #for each word in the quote
            if word in plsingledict: #if the word has already occured
                plsingledict[word] = plsingledict[word] + 1 #add 1 to that word's count
            else: #if that word hasn't occured yet
                plsingledict[word] = 1 #set that word's count to 1
        pldict[fullquote] = plsingledict #add our word counts to the full dictionary
        plsingledict = {} #reset the word counts
    return pldict #return the full dictionary

#generates a reverse postings-list dictionary
def reverseDictionaryFromAllQuotes():
    rpldict = {}

    fullwordlist = [] #a list of every single word in every single quote
    for fullquote in allquotes: #for each quote in the full quote list
        wordlist = splitQuote(fullquote) #split the quote into words
        for word in wordlist: #for every single word
            if word not in fullwordlist: #if we haven't seen this word yet
                if word: #if the word is not null
                    fullwordlist.append(word) #add the word to the list
    #at this point, fullwordlist has 1 copy of every word in the file

    rplsingledict = {} #a single dict consists of a full quote as key, and the number of word occurences as a value
    for word in fullwordlist: #for each word in the full word list, we're going to search for matches
        for fullquote in allquotes: #for each quote in the file
            if word in fullquote: #if the word occurs in the quote
                rplsingledict[fullquote] = fullquote.count(word) #store the word count in the single dict
        rpldict[word] = rplsingledict #store the single dict in the full dict
        rplsingledict = {} #reset the single dict

    return rpldict

#gets the TF of a word/quote pair
def getTf(word, quote):
    quote = splitQuote(quote) #split the quote into words
    while '' in quote: #remove empty words
        quote.remove('')
        
    #get the count of the most commonly occuring word
    wordcount = []
    for word in quote:
        wordcount.append(quote.count(word))
    return quote.count(word) / float(max(wordcount)) #term frequency = occurences of this word / occurences of most common word


#gets the IDF of a word
def getIdf(word):
    import math
    #count the number of quotes containing word
    x = 1
    for quote in allquotes:
        if word in splitQuote(quote):
            x += 1
    return math.log((len(allquotes) / x), 10) #IDF = log(number of quotes / number of quotes containing this word)

#gets the TF-IDF of a word/quote pair
def getTfIdf(word, quote):
    return getTf(word, quote) * getIdf(word)

#search quotes using a single word
def searchByWord(word):
    results = {}
    for quote in allquotes:
        if word in splitQuote(quote):
            results[quote] = getTfIdf(word, quote)
    return results


#search quotes using a list of words
def searchByWordList(wordlist):
    results = {}
    for quote in allquotes:
        for word in wordlist:
            if word in splitQuote(quote):
                if quote in results:
                    results[quote] = results[quote] + getTfIdf(quote, word)
                else:
                    results[quote] = getTfIdf(quote, word)
    return results


#run the main function automatically
if __name__ == "__main__":
    main()
    