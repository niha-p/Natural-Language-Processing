Recursive Neural Networks with Dependency Parsing (Implementation of Deep Learning for Question Answering System)

- Implemented multi-class logistic regression using Theano
- Implemented a dependency parse recursive neural network 
- Experimented with hyperparameter settings and different features and evaluated the results

NAME:Niharika Purbey ; UNI:np2544

1) Logistic Regression:
Implemented


2) Input handling:
Implemented sort_datum() function


3) Activation Function:
Implemented normalized_tanh function


4) Recurrence relation and cost function:
Implemented recurrence function

--------OUTPUT---------
number of training sentences: 6780
number of validation sentences: 472
number of dependency relations: 46
number of elements in vocabulary: 19752
number of unique answers: 409
batch_size 271

Epoch 0
-------------------
epoch: 0 batch: 0 cost: 99.6541766281 time: 30.5672109127
epoch: 0 batch: 1 cost: 95.0307514344 time: 28.9593770504
epoch: 0 batch: 2 cost: 90.2739917794 time: 29.9620368481
epoch: 0 batch: 3 cost: 90.163151574 time: 28.3596618176
epoch: 0 batch: 4 cost: 109.718442111 time: 27.4043290615
epoch: 0 batch: 5 cost: 117.631604543 time: 29.5116670132
epoch: 0 batch: 6 cost: 98.6964961817 time: 30.5848491192
epoch: 0 batch: 7 cost: 89.0748442406 time: 26.8062369823
epoch: 0 batch: 8 cost: 88.5862918139 time: 29.9417581558
epoch: 0 batch: 9 cost: 79.174998434 time: 29.9169847965
epoch: 0 batch: 10 cost: 93.7740070639 time: 30.1510541439
.
.
done with epoch 0, epoch cost = 2488.46854222
(6780, 100)
(472, 100)
train acc = 0.35, val acc = 0.108050847458
-------------------

Epoch 10
-------------------
epoch: 10 batch: 0 cost: 30.1295968733 time: 27.2790651321
epoch: 10 batch: 1 cost: 24.5783342512 time: 28.1658630371
epoch: 10 batch: 2 cost: 27.3518617244 time: 29.6299381256
epoch: 10 batch: 3 cost: 28.9386973203 time: 30.2296879292
epoch: 10 batch: 4 cost: 39.9472675208 time: 28.9267199039
epoch: 10 batch: 5 cost: 41.054576509 time: 31.6296770573
epoch: 10 batch: 6 cost: 33.5795096168 time: 32.4772601128
epoch: 10 batch: 7 cost: 33.5233078221 time: 28.9269988537
epoch: 10 batch: 8 cost: 42.0777886606 time: 31.3246700764
epoch: 10 batch: 9 cost: 37.836592212 time: 30.6507351398
epoch: 10 batch: 10 cost: 34.5279305054 time: 31.5163631439
.
.
done with epoch 10, epoch cost = 893.494565298
(6780, 100)
(472, 100)
train acc = 0.981120943953, val acc = 0.358050847458
-------------------

Epoch 20
-------------------
train acc = 0.996460176991, val acc = 0.411016949153
-------------------

Epoch 25
-------------------
epoch: 25 batch: 0 cost: 21.8361153852 time: 26.5161190033
epoch: 25 batch: 1 cost: 18.8418107151 time: 28.1502890587
epoch: 25 batch: 2 cost: 21.7459250329 time: 29.4652609825
epoch: 25 batch: 3 cost: 19.8134404957 time: 28.3105351925
epoch: 25 batch: 4 cost: 25.5016090863 time: 27.8343179226
epoch: 25 batch: 5 cost: 26.9913014889 time: 29.2751979828
epoch: 25 batch: 6 cost: 22.0016507028 time: 29.4973230362
epoch: 25 batch: 7 cost: 23.5570495811 time: 25.9192428589
epoch: 25 batch: 8 cost: 28.1613620188 time: 29.132848978
epoch: 25 batch: 9 cost: 26.8074039063 time: 28.6685400009
epoch: 25 batch: 10 cost: 24.6215469574 time: 28.9630348682
-------------------

Epoch 29
-------------------
done with epoch 29, epoch cost = 616.513856292
(6780, 100)
(472, 100)
train acc = 0.998820058997, val acc = 0.404661016949
-------------------
Please note: val acc did reach 41% at Epoch 20.


5) Embeddings:
Implemented buildWord2Vec.py to train model which is saved as 'word2vec_file'

a) With We

--------OUTPUT---------
number of training sentences: 6780
number of validation sentences: 472
number of dependency relations: 46
number of elements in vocabulary: 19752
number of unique answers: 409
batch_size 271

Epoch 0
-------------------
epoch: 0 batch: 0 cost: 103.23161522 time: 26.3988499641
epoch: 0 batch: 1 cost: 89.0886039234 time: 28.2807519436
epoch: 0 batch: 2 cost: 85.8504783634 time: 29.1874699593
epoch: 0 batch: 3 cost: 80.7962131798 time: 28.1705710888
epoch: 0 batch: 4 cost: 122.362757584 time: 26.7961919308
epoch: 0 batch: 5 cost: 118.58630375 time: 28.4562120438
epoch: 0 batch: 6 cost: 106.14018195 time: 29.4525468349
epoch: 0 batch: 7 cost: 99.4281501249 time: 25.940625906
epoch: 0 batch: 8 cost: 108.443602457 time: 28.8339428902
epoch: 0 batch: 9 cost: 94.3814814111 time: 28.2653779984
epoch: 0 batch: 10 cost: 89.2578987759 time: 29.5816040039
.
.
done with epoch 0, epoch cost = 2414.46160557
(6780, 100)
(472, 100)
train acc = 0.326548672566, val acc = 0.137711864407
-------------------

Epoch 10
-------------------
epoch: 10 batch: 0 cost: 39.5447266763 time: 26.1803309917
epoch: 10 batch: 1 cost: 35.2691400869 time: 27.9458050728
epoch: 10 batch: 2 cost: 35.5885637849 time: 29.0187489986
epoch: 10 batch: 3 cost: 31.3993343805 time: 28.1265699863
epoch: 10 batch: 4 cost: 49.8847210931 time: 26.7193739414
epoch: 10 batch: 5 cost: 49.0134558056 time: 29.9906520844
epoch: 10 batch: 6 cost: 40.6808009701 time: 29.7659809589
epoch: 10 batch: 7 cost: 41.7179676049 time: 26.1853249073
epoch: 10 batch: 8 cost: 50.9587424541 time: 28.692898035
epoch: 10 batch: 9 cost: 48.6354543873 time: 28.059196949
epoch: 10 batch: 10 cost: 41.9612276587 time: 29.2973439693
done with epoch 10, epoch cost = 1100.36413879
(6780, 100)
(472, 100)
train acc = 0.757522123894, val acc = 0.290254237288
-------------------

Epoch 20
-------------------
train acc = 0.915044247788, val acc = 0.319915254237
-------------------

Epoch 25
-------------------
epoch: 25 batch: 0 cost: 26.0633262578 time: 26.7382581234
epoch: 25 batch: 1 cost: 25.1582789927 time: 28.344878912
epoch: 25 batch: 2 cost: 27.5886530285 time: 28.8755040169
epoch: 25 batch: 3 cost: 24.1054304333 time: 27.5894939899
epoch: 25 batch: 4 cost: 31.9532961847 time: 26.1681480408
epoch: 25 batch: 5 cost: 34.814795811 time: 29.1523730755
epoch: 25 batch: 6 cost: 30.3146544884 time: 30.4539659023
epoch: 25 batch: 7 cost: 32.0769307771 time: 25.4713690281
epoch: 25 batch: 8 cost: 39.2809543535 time: 28.3057069778
epoch: 25 batch: 9 cost: 38.2131628585 time: 27.776045084
epoch: 25 batch: 10 cost: 31.6264668526 time: 28.5278251171
-------------------

Epoch 29
-------------------
done with epoch 29, epoch cost = 740.391318801
(6780, 100)
(472, 100)
train acc = 0.958702064897, val acc = 0.33686440678
-------------------


b) Without We

--------OUTPUT---------
number of training sentences: 6780
number of validation sentences: 472
number of dependency relations: 46
number of elements in vocabulary: 19752
number of unique answers: 409
batch_size 271

Epoch 0
-------------------
epoch: 0 batch: 0 cost: 103.278288006 time: 24.4497230053
epoch: 0 batch: 1 cost: 90.4209202407 time: 26.0829269886
epoch: 0 batch: 2 cost: 88.9402173772 time: 27.5198280811
epoch: 0 batch: 3 cost: 89.7946980174 time: 26.0975430012
epoch: 0 batch: 4 cost: 108.339861298 time: 24.6432218552
epoch: 0 batch: 5 cost: 103.479248127 time: 26.8426558971
epoch: 0 batch: 6 cost: 103.582008542 time: 27.8655509949
epoch: 0 batch: 7 cost: 100.426648017 time: 24.3108448982
epoch: 0 batch: 8 cost: 101.367923905 time: 26.7592039108
epoch: 0 batch: 9 cost: 99.0652256385 time: 26.2673830986
epoch: 0 batch: 10 cost: 94.2425970204 time: 27.1699590683

done with epoch 0, epoch cost = 2489.15329242
(6780, 100)
(472, 100)
train acc = 0.306784660767, val acc = 0.131355932203
-------------------

Epoch 10
-------------------
epoch: 10 batch: 0 cost: 80.1128098804 time: 20.2753629684
epoch: 10 batch: 1 cost: 82.2252961161 time: 21.8309121132
epoch: 10 batch: 2 cost: 80.3722017438 time: 22.7816579342
epoch: 10 batch: 3 cost: 79.5654099652 time: 21.7493848801
epoch: 10 batch: 4 cost: 89.1526830284 time: 20.5540549755
epoch: 10 batch: 5 cost: 86.0753560722 time: 22.4213020802
epoch: 10 batch: 6 cost: 83.3848459386 time: 23.1534841061
epoch: 10 batch: 7 cost: 84.4659195052 time: 20.0315878391
epoch: 10 batch: 8 cost: 88.4712603297 time: 22.381152153
epoch: 10 batch: 9 cost: 88.2119468874 time: 21.9041290283
epoch: 10 batch: 10 cost: 84.5061913098 time: 22.4598259926
.
.
done with epoch 10, epoch cost = 2128.58740414
(6780, 100)
(472, 100)
train acc = 0.377876106195, val acc = 0.14406779661
-------------------

Epoch 20
-------------------
train acc = 0.427728613569, val acc = 0.14406779661
-------------------

Epoch 25
-------------------
epoch: 25 batch: 0 cost: 75.1257221252 time: 20.2947471142
epoch: 25 batch: 1 cost: 79.8783187618 time: 21.8497200012
epoch: 25 batch: 2 cost: 77.4841083758 time: 22.7824270725
epoch: 25 batch: 3 cost: 77.0408626496 time: 21.7960050106
epoch: 25 batch: 4 cost: 84.4359449477 time: 20.5826661587
epoch: 25 batch: 5 cost: 82.3351053006 time: 22.4754889011
epoch: 25 batch: 6 cost: 79.2162982156 time: 23.197988987
epoch: 25 batch: 7 cost: 79.5609957737 time: 20.1198511124
epoch: 25 batch: 8 cost: 84.4058793511 time: 22.4344730377
epoch: 25 batch: 9 cost: 83.6889128637 time: 21.9741430283
epoch: 25 batch: 10 cost: 81.3506775535 time: 22.521889925
-------------------

Epoch 29
-------------------
done with epoch 29, epoch cost = 1981.02687123
(6780, 100)
(472, 100)
train acc = 0.454572271386, val acc = 0.16313559322
-------------------


6) TSNE visualization
Created visualizations for the answers in random_init.npz
Check tsne_visualization.png

