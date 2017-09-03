#!/usr/bin/env python3
#
# Dallas Foglia
# 2017/8/23
#
# Editor: tabstops = 2, cols = 80
#
# Trie implimentation using list as nodes.
# Alice in Wonderland test will acts as input data.
#
# Written for Python3

import re

#Takes text file, returns list of all words present minus duplicates.
def getWords(file_in):
	words = []
	with open(file_in) as F:
		for line in F:
			words.extend([re.sub("[^A-Za-z]", "", i).lower() for i in line.split(" ")])
	return list(set(words)) #remove dupes with set

#There's always a dictionary.
#There's always a reference.
#There's always a headache.
def makeTrie(words):
	trie_dict = {}
	for word in words:
		new_dict = trie_dict
		for character in word:
			#assign a dict to each character
			new_dict = new_dict.setdefault(character, {})

			#This was the original method, but .setdefault is more accurate.
			#if character not in new_dict:
			#	new_dict[character] = {}
			#else:
			#	new_dict = new_dict[character]

		#'*' represents the end of the word.
		new_dict['*'] = '*'
	return trie_dict

#Thousands of words... accessed recursively.
def countTrie(trie):
	counter = 0
	for i in trie:
		#recursive call if end of word not found at dict entry
		if trie[i] is not '*':
			counter = counter + countTrie(trie[i])
		else:
			counter = counter + 1
	return(counter)

words = getWords('Alice.txt')
print("# of unique words: {}".format(len(words)))
my_trie = makeTrie(words)
print("# of trie branches: {}".format(countTrie(my_trie)))
