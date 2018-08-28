# Data Analysis Programming
This is the repo of MSBA summer 2018 Data Analysis Course.<br>
It includes 3 homework and 1 project, and all the assignments are written by Python and submitted as Jupyter Notebook.<br>
<br>
**Homework 1**<br>
1. We designed a robot that plays rock, paper, scissors through the interaction with human. The computer will predict the next hand of human through the calculation of type of hands human played before. Unless the human choose to quit, the game will continue. Once the human quit, the game results will return who wins, how many games played.<br>
2. Read in the data of FloridaVoters.html which contains a Web Table of republican and democratic voters in various counties in Florida. Write code that reads in the file as a standard text and prints out the counties, along with the number of republican and democratic voters in those counties, sorted by the number of democratic voters.<br>
3. Read in the data of quotes.txt and play with the format including build the postings-list dictionary, build the reverse postings-list dictionary, write a TF-IDF function and build a search engine for the quotes in the data.<br>
<br>

**Homework 2**<br>
In this assignment, I analyzed restaurant inspections in New York City, starting November 1, 2014 and ending January 31, 2015. The data   is in the NYC Restaurants.csv. I used Pandas series, dataframe and by reshaping, merge and pivot-table, I generated insights according to each questions.<br>
<br>

**Homework 3**<br>
***Introduction of the data***
Suppose we have a bunch of URLs and we want to know their adult-rating (i.e., is the url P, or G, or X, or R). This task is difficult for computers, but easy for humans, and this has led to the growth of crowdsourcing: geta bunch of humans to give ratings to urls, but use automated techniques to figure out how much to trust each person's ratings. We are going to use the data from a paper by Ipeirotis et al. available here. This details an experiment run on Amazon's Mechanical Turk crowd-sourcing system. They ask a bunch of raters (called "turks") to rate several urls, but they already know the answers (the true categories) for a few urls, called the "gold set". The ratings of the turks on the gold set thus allows us to judge their accuracy.<br>
In this assignment, we have to read in two dataset: gold.txt and labels.txt, and by merging, reshaping them, we then generate some insights according to the questions.
