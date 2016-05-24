from __future__  import division
import nltk
import A
import time
from collections import defaultdict
from nltk.align  import AlignedSent
from nltk.corpus import comtrans
from nltk.align.ibm1 import IBMModel1

class BerkeleyAligner():

    def __init__(self, align_sents, num_iter):
        #self.t, self.q = self.train(align_sents, num_iter)
	self.probabilities, self.alignments = self.train(align_sents, num_iter)


    # TODO: Computes the alignments for align_sent, using this model's parameters. Return
    #       an AlignedSent object, with the sentence pair and the alignments computed.
    def align(self, align_sent):
        if self.probabilities is None or self.alignments is None:
            raise ValueError("The model does not train.")

        alignment = []

	l_e = len(align_sent.words)
        l_f = len(align_sent.mots)

        for j, en_word in enumerate(align_sent.words):
            # Initialize the maximum probability with Null token
            max_align_prob = (self.probabilities[en_word][None] * self.alignments[0][j + 1][l_e][l_f], None)
            for i, de_word in enumerate(align_sent.mots):
                # Find out the maximum probability
                max_align_prob = max(max_align_prob, (
                self.probabilities[en_word][de_word] * self.alignments[i + 1][j + 1][l_e][l_f], i))

            # If the maximum probability is not Null token,
            # then append it to the alignment.
            if max_align_prob[1] is not None:
                alignment.append((j, max_align_prob[1]))

        return AlignedSent(align_sent.words, align_sent.mots, alignment)

    
    # TODO: Implement the EM algorithm. num_iters is the number of iterations. Returns the 
    # translation and distortion parameters as a tuple.
    def train(self, aligned_sents, num_iters):
        #t = {}
        #q = {}

	############
	# Get initial translation probability distribution
	# from a few iterations of Model 1 training.
        ibm1= IBMModel1(aligned_sents, 10)
        t_ef = ibm1.probabilities
	
	reverse_aligned_sents = []
        for alignSent in aligned_sents:
            reverse_aligned_sents.append(alignSent.invert())
	    #reverse_aligned_sents.append(alignSent)

        ibm11= IBMModel1(reverse_aligned_sents,10)
        t_fe = ibm11.probabilities

        # Vocabulary of each language
        de_vocab = set()
        en_vocab = set()
        for alignSent in aligned_sents:
            en_vocab.update(alignSent.words)
            de_vocab.update(alignSent.mots)
        de_vocab.add(None)
        en_vocab.add(None)
       
        align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0))))
        reverse_align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0))))

        # Initialize the distribution of alignment probability,
        # a(i|j,l_e, l_f) = 1/(l_f + 1)
        for alignSent in aligned_sents:
            en_set = [None] + alignSent.words
            de_set = [None] + alignSent.mots
            l_f = len(de_set) - 1
            l_e = len(en_set) - 1
            initial_value = 1 / (l_f + 1)
            for i in range(0, l_f + 1):
                for j in range(1, l_e + 1):
                    align[i][j][l_e][l_f] = initial_value
            reverse_initial_value = 1 / (l_e + 1)
            for i in range(0, l_e + 1):
                for j in range(1, l_f + 1):
                    reverse_align[i][j][l_f][l_e] = reverse_initial_value

       
        for k in range(0,num_iters):
            count_ef = defaultdict(lambda: defaultdict(lambda: 0.0))
            count_fe = defaultdict(lambda: defaultdict(lambda: 0.0))
            total_f = defaultdict(lambda: 0.0)
            count_align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0))))
            total_align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0)))
            reverse_count_align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0))))
            reverse_total_align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0)))
            total_e = defaultdict(lambda: 0.0)
            denominator = defaultdict(lambda: 0.0)
            reverse_denominator = defaultdict(lambda: 0.0)

            for alignSent in aligned_sents:
                en_set = [None] + alignSent.words
                de_set = [None] + alignSent.mots
                l_f = len(de_set) - 1
                l_e = len(en_set) - 1

                # compute normalization
                for j in range(1, l_e + 1):
                    en_word = en_set[j]
                    denominator[en_word] = 0
                    for i in range(0, l_f + 1):
                        denominator[en_word] += t_ef[en_word][de_set[i]] * align[i][j][l_e][l_f]

                for j in range(1, l_f + 1):
                    de_word = de_set[j]
                    reverse_denominator[de_word] = 0
                    for i in range(0, l_e + 1):
                        reverse_denominator[de_word] += t_fe[de_word][en_set[i]] * reverse_align[i][j][l_f][l_e]

                # collect counts
                for j in range(1, l_e + 1):
                    en_word = en_set[j]
                    for i in range(0,l_f + 1):
                        de_word = de_set[i]
                        c = t_ef[en_word][de_word] * align[i][j][l_e][l_f] / denominator[en_word]
                        count_ef[en_word][de_word] += c
                        total_f[de_word] += c
                        count_align[i][j][l_e][l_f] += c
                        total_align[j][l_e][l_f] += c

                for j in range(1, l_f + 1):
                    de_word = de_set[j]
                    for i in range(l_e + 1):
                        en_word = en_set[i]
                        c = t_fe[de_word][en_word] * reverse_align[i][j][l_f][l_e] / reverse_denominator[de_word]
                        count_fe[de_word][en_word] += c
                        total_e[en_word] += c
                        reverse_count_align[i][j][l_f][l_e] += c
                        reverse_total_align[j][l_f][l_e] += c

	    #Averaging	
            for eng in count_ef:
                for de in count_ef[eng]:
                    count_ef[eng][de] = (count_ef[eng][de] + count_fe[de][eng]) *0.5
                    #if count_ef[eng][de]>count_fe[de][eng]:
			#count_ef[eng][de]=count_ef[eng][de]*0.4+count_fe[de][eng]*0.6
		    count_fe[de][eng] = count_ef[eng][de]

            for alignSent in aligned_sents:
                source_set = [None] + alignSent.words
                target_set = [None] + alignSent.mots
                source_l = len(source_set) - 1
                target_l = len(target_set) - 1
                for j in range(1, source_l + 1):
                    for i in range(0,target_l + 1):
                        count_align[i][j][source_l][target_l] = (count_align[i][j][source_l][target_l] + reverse_count_align[j][i][target_l][source_l]) / 2
                        reverse_count_align[j][i][target_l][source_l] = count_align[i][j][source_l][target_l]

            # estimate probabilities
            t_ef = defaultdict(lambda: defaultdict(lambda: 0.0))
            align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0))))
            t_fe = defaultdict(lambda: defaultdict(lambda: 0.0))
            reverse_align = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0))))


	    '''
 	    # Smoothing the counts for alignments
            for alignSent in aligned_sents:
                en_set = alignSent.words
                de_set = [None] + alignSent.mots
                l_f = len(fr_set) - 1
                l_e = len(en_set) - 1

                laplace = 1.0
                for i in range(0, l_f+1):
                    for j in range(1, l_e+1):
                        value = count_align[i][j][l_e][l_f]
                        if 0 < value < laplace:
                            laplace = value

                laplace *= 0.5 
                for i in range(0, l_f+1):
                    for j in range(1, l_e+1):
                        count_align[i][j][l_e][l_f] += laplace

                initial_value = laplace * l_e
                for j in range(1, l_e+1):
                    total_align[j][l_e][l_f] += initial_value

	    '''

            # Estimate the new lexical translation probabilities
            for f in de_vocab:
                for e in en_vocab:
                    t_ef[e][f] = count_ef[e][f] / total_f[f]

            for e in en_vocab:
                for f in de_vocab:
                    t_fe[f][e] = count_fe[f][e] / total_e[e]

            # Estimate the new alignment probabilities
            for alignSent in aligned_sents:
                en_set = [None] + alignSent.words
                de_set = [None] + alignSent.mots
                l_f = len(de_set) - 1
                l_e = len(en_set) - 1
                for i in range(0, l_f + 1):
                    for j in range(1, l_e + 1):
                        align[i][j][l_e][l_f] = count_align[i][j][l_e][l_f] / total_align[j][l_e][l_f]
                for i in range(0, l_e + 1):
                    for j in range(1, l_f + 1):
                        reverse_align[i][j][l_f][l_e] = reverse_count_align[i][j][l_f][l_e] / reverse_total_align[j][l_f][l_e]

        return t_ef, align
	############

        #return (t,q)

def main(aligned_sents):
    #time.clock()
    ba = BerkeleyAligner(aligned_sents, 10)
    A.save_model_output(aligned_sents, ba, "ba.txt")
    avg_aer = A.compute_avg_aer(aligned_sents, ba, 50)

    print ('Berkeley Aligner')
    print ('---------------------------')
    print('Average AER: {0:.3f}\n'.format(avg_aer))
    #print ('Total time taken for Part B: '+str(time.clock())+' seconds')

