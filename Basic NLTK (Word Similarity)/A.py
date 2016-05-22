import nltk
import sys

greeting=sys.stdin.read()
print greeting

token_list = nltk.word_tokenize(greeting)
print "The tokens in the greeting are"
for token in token_list:
    print token
squirrel=0
girl=0

for token in token_list:
	str=token.lower()
	if (str=='squirrel'):
		squirrel+=1
	if (str=='girl'):
		girl+=1
	
print "There were %d instances of the word 'squirrel' and %d instances of the word 'girl.'"% (squirrel, girl)


