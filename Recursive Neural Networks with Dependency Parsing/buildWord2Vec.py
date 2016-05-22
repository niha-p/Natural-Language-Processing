import json
from pprint import pprint
import gensim
import numpy as np

#Reading JSON file
with open('hist_split.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
#Populating sentences
sentences=[]
words=[]

for i in range(0,len(data["train"])):
    words=[]
    for j in range(0,len(data["train"][i][0])):
	if data["train"][i][0][j][0] is None:
	    words.append('DUMMY_WORD')
        else:
	    words.append(data["train"][i][0][j][0])
    sentences.append(words)

#print(sentences)

#word2vec method

model = gensim.models.Word2Vec(size=100, window=5, min_count=1) 
model.build_vocab(sentences)  
alpha, min_alpha, passes = (0.025, 0.001, 20)  
alpha_delta = (alpha - min_alpha) / passes

for epoch in range(passes):              
    model.alpha, model.min_alpha = alpha, alpha              
    model.train(sentences)             
    print('completed pass %i at alpha %f' % (epoch + 1, alpha))             
    alpha -= alpha_delta             
    np.random.shuffle(sentences)

model.save('word2vec_file')


