Challenge 2 - Did you mean...?
=============

ou work in a company that's main product is a search engine. You have noticed
that users make a lot of mistakes while typing :) And that the most common
mistake is that they type a very similar word instead of the one they are
looking for. So what you have decided is to make suggestions to the users
while they are typing. You want to suggest valid words from the dictionary
that contain the same letters (and the same number of each letter) but in
different orders.

For example, a user types "act", you might want to suggest "cat". In the same
way, if user types "elvis", your suggestion should be "lives".

Your goal is to find all possible suggestions for a set of words and a given
dictionary. Assume that all the words in the dictionary are correct.

Input:

The input consists of comments (lines starting with '#'), name of the dictionary file to use, number of words that require suggestions and the list of words that require suggestions. Comments describe and separate each part of the intput:

    #Dictionary file
    name of the file containting the dictionary
    #Suggestion numbers
    Integer N, representing the number of words provided, one per line, that require suggestions
    #Find the suggestions
    List of words for which you need to find the suggestions, each one in a different line 

The dictionary file is nothing else than a list of words.

Output:

The output must be a list of

    word -> suggestion1 suggestion2 ... 

each one on a different line. The suggestions for each word, if more than one,
need to be in alphabetical order.

If no suggestion for a word can be found, then output

    word -> 

for that word.

Sample input:

    #Dictionary file
    dictionary
    #Suggestion numbers
    3
    #Find the suggestions
    elvis
    lactoprotein
    nosuggestion

Sample output:

    elvis -> lives velis
    lactoprotein -> protectional
    nosuggestion ->

Sample dictionary:

    gainly
    laying
    protectional
    lactoprotein
    elvis
    lives
    velis
    nosuggestion

The dictionaries can be found [here](https://mega.co.nz/#!ugAhEJRQ!X1Q77AV9goX_NstmCPXyTBFwdadx9iHa6577ICoQO6U) and you will need to unzip it in the folder
where you run your program.
