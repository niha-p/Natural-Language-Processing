Machine Translation (German-English corpus)

- Implemented IBM Models 1 and 2
- Implemented Berkeley Aligner (Using EM algorithm)

NAME: Niharika Purbey ; UNI: np2544

PART A
--------------------------
Total time taken for Part A: 136.79 seconds

IBM Model 1
Average AER: 0.665

IBM Model 2
Average AER: 0.650

3)
The sentence pair (5th sentence):
[u'Ich', u'bitte', u'Sie', u',', u'sich', u'zu', u'einer', u'Schweigeminute', u'zu', u'erheben', u'.']
[u'Please', u'rise', u',', u'then', u',', u'for', u'this', u'minute', u"'", u's', u'silence', u'.']

IBMModel1 AER: 0.75
0-1 1-1 2-1 3-4 4-10 5-10 6-10 7-10 8-10 9-1

IBMModel2 AER: 0.6666666666666667
0-0 1-1 2-0 3-2 4-10 5-10 6-10 7-7 8-10 9-0 

In the above example, we can see that IBM model2 performs better than IBM model 1 because it has a lower error rate. Model 2 takes into account the alignment paramenter of different word pairs, while model 1 simply sets this value to a default value. Hence, model 2 gives us a higher accuracy than model 1.

4)
Given below is a table with the AER values for different number of iterations for both IBM model 1 and IBM model 2:

Iterations    IBMmodel1       IBMmodel2
2		0.684		0.644
4		0.630		0.642
6		0.626		0.647
8		0.631		0.649
10		0.665		0.650
15		0.665		0.650
20		0.661		0.648
25		0.660		0.649
30		0.660		0.649
40		0.657		0.650
50 		0.658		0.654
60		0.658		0.657
80		0.662		0.657
100 		0.661		0.659

IBM model 1:
As we can see from the table, the AER value decreases uptil 6 iterations and then starts increasing after. After 25 iterations, we observe that the AER value almost stabilizes. The lowest AER was obtained at iteration 6.  

IBM model 2:
As we can see from the table, the AER value decreases uptil 4 iterations and then starts increasing after. After around 60-80 iterations, we observe that the AER value almost stabilizes. The lowest AER was obtained at iteration 4.                  


PART B
--------------------------
Referred to the nltk documentation: http://pydoc.net/Python/nltk/3.0.1/nltk.align.ibm2/

Total time taken for Part B: 316.901288 seconds

Berkeley Aligner
Average AER: 0.548

4)
We can see that the average AER value of the Berkeley Aligner was less than both IBM model 1 and IBM model 2 which means that the Berkeley Aligner performed better than both the IBM models.

5)
Using the same example sentence pair as before (5th sentence):
[u'Ich', u'bitte', u'Sie', u',', u'sich', u'zu', u'einer', u'Schweigeminute', u'zu', u'erheben', u'.']
[u'Please', u'rise', u',', u'then', u',', u'for', u'this', u'minute', u"'", u's', u'silence', u'.']

IBMModel1 AER: 0.75
0-1 1-1 2-1 3-4 4-10 5-10 6-10 7-10 8-10 9-1

IBMModel2 AER: 0.6666666666666667
0-0 1-1 2-0 3-2 4-10 5-10 6-10 7-7 8-10 9-0

Berkeley Aligner: 0.6
0-0 1-1 2-0 3-2 4-6 5-10 6-10 7-7 8-10 9-0 10-11

We can see that the Berkeley Aligner performed better than both IBM model 1 and IBM model 2 as it had a lower AER for this sentence. 
Berkeley Aligner considers information from both the directions i.e. from English to German and from German to English while the IBM models follow only one direction. 
Hence, this gives Berkeley Aligner an edge over the IBM models generating more accurate results. 

6)
Better Berkeley Aligner Not Implemented
