Multilingual Dependency Parsing (English, Danish, Korean, Swedish)

- Generated visualizations for dependency graphs
- Implemented Nivre dependency parser
- Improved performance of the parser by adding new features



NAME:Niharika Purbey ; UNI:np2544

1)
a.
Created 4 files:
figure_en.png
figure_da.png
figure_ko.png
figure_sw.png

b.
A dependency graph that does not have any of it's arcs crossing is projective.Hence, if we do not see any of the lines overlapping in the dependency graph diagram, then it is projective. 
In the code providedcode/transitionparser.py,if there is an arc from a child to parent, it is checked whether there is a direct link or with multiple hops, this indicates that the graph is projective.

c.
Projective: "I went to Paris to see the Eiffel Tower."
Non-Projective: "I bought a cake yesterday which was stale."
The above sentence is non-projective because there will be an arc between 'bought' and 'yesterday' and between 'cake' and 'was'.
----------------------------------------------------------------------------

2)
a.
Completed implementation of the operations left_arc, right_arc, shift and reduce in transition.py and ran test.py

b.
Using badfeatures.model on Swedish data, I got the following output:

$ python test.py
This is not a very good feature extractor!
 Number of training examples : 500
 Number of valid (projective) examples : 437
Training support vector machine...
done!
UAS: 0.279305354559 
LAS: 0.178726483357

Using badfeatures.model, both the unlabeled attachment score and more importantly even the labeled attachment score are very low which indicates a bad performance. It seems that the features that are being used seem to be very generic and do not account for ambiguity. 
----------------------------------------------------------------------------

3)
a.
I added the following 3 features to featureextractor.py which I found on pg 32 of the book [Dependence Parsing by Kuebler, McDonald, and Nivre]: 

1. POSTAG for word on top of the stack and one below it (STK[0] and STK[1]) and for first and second word in the buffer (BUF[0] and BUF[1]).

Using this feature, the attachment scores changed from 
UAS: 0.267481662592 
LAS: 0.218092909535

to
UAS: 0.764303178484 
LAS: 0.732029339853
where the first scores represent the scores before adding any of my features and the latter represents scores after the first feature was added. 

The part of speech feature gave a significant increase in the accuracy which makes sense because it provides more context and eliminates ambiguity – for example, the word “round” can be an adjective or noun depending on the context. Hence, such ambiguity was avoided by adding this feature.

I initially tried POSTAG for only STK[0] and BUF[0], but I also added POSTAG for STK[1] and BUF[0] later which increased the accuracy further. These words are generally used to decide the transitions. 

The complexity for this operation would be constant, since I am only retrieving the POSTAG for 4 fields.
 

2. Distance between the words: top of the stack and first word in the input buffer

Using this feature and the previous feature, the attachment scores change to

UAS: 0.777017114914 
LAS: 0.741320293399

This feature increased the accuracy by a small amount, but not as much as the POSTAG. The reason I used this feature was because, words which are far away from each other have less probability to be related to each other. 

Again, the complexity for this operation would be constant O(1), since I am retrieving the address of 2 words and subtracting them.


3. Number of left and right children for top of the stack and first word in buffer

Using all the 3 features, the attachment scores changed to
	
UAS: 0.80293398533 
LAS: 0.773105134474

Again, by adding this feature, there was a slight increase in the accuracy, however the increase was more significant than the second feature. 

The reason I used this feature was because, a word that has dependents is more probable to be higher up in the dependency tree. Hence, a word that is higher in the dependency tree will has more dependents.  

To find the number of dependents, I looked through all the arcs to check whether the word (top of stack or first word in buffer) exists and incremented the count, every time there was a match. Depending on the address, the number of right children or the number of left children was incremented accordingly. Hence, the complexity would be O(n)

All these scores were obtained for English data.

I also tried the feature “LEMMA”, however I did not see significant changes in the attachment score, so decided not to use it. 


b.
Generated the 3 models:
English.model
Swedish.model
Danish.model

c.
English.model

Number of training examples : 200
Number of valid (projective) examples : 200
Training support vector machine...
done!
UAS: 0.804400977995 
LAS: 0.774572127139

-------
Swedish.model

Number of training examples : 500
Number of valid (projective) examples : 437
Training support vector machine...
done!
UAS: 0.805354558611 
LAS: 0.719247467438

--------
Danish.model

Number of training examples : 200
Number of valid (projective) examples : 165
Training support vector machine...
done!
UAS: 0.790463398254 
LAS: 0.701813297515


d.
The accuracy of the arc-eager parser depends heavily on the training data and the features. 
In this case, we used SVM hence the complexity depends heavily on the SVM algorithm implementation.
Since the parser parses sentences in a single pass on the input, it has a linear time complexity. 

One of the disadvantages of this parser is that, it will not work for sentences which have a non-projective dependency graph. This parser is only suitable for sentences which have a projective dependency graph.

However, a benefit of using this parser is that we can use any classification technique (i.e instead of SVM), where the implementation of the parser would remain the same, except for a few minor changes maybe.
----------------------------------------------------------------------------

4)
parse.py created.
englishfile.conll created.
