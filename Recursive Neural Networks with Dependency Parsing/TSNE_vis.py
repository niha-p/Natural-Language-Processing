import numpy as np
from sklearn.manifold import TSNE
from dependencyRNN import DependencyRNN
import matplotlib.pyplot as plt

#You can load the answer embeddings by calling DependencyRNN.load(filename) and then the answermethod will produce a dictionary of answers to their embeddings, which you will need to convert to a matrix.  Then run TSNE on the answer matrix.

#Loading answer embeddings
d=DependencyRNN.load("random_init.npz")
X=d.answers.values()
words=d.answers.keys()
n=len(words)

#print n
#print words

#running TSNE on answer matrix
tsne = TSNE(n_components=2, perplexity=30.0) 
X_reduced = tsne.fit_transform(X)
x=[]
y=[]

#Plot the results  with each point represented on the graph as its word
for i in range(0,n):
    x.append(X_reduced[i][0])
    y.append(X_reduced[i][1])

plt.scatter(x,y)
for i in range(0,n):
    plt.annotate(words[i],xy=(x[i],y[i]),bbox=dict(fc='white'))

plt.show()
