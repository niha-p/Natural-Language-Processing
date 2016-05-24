import nltk
from nltk.align import IBMModel1
from nltk.align import IBMModel2
import time

# TODO: Initialize IBM Model 1 and return the model.
def create_ibm1(aligned_sents):
    return IBMModel1(aligned_sents, 10)#Change to 10

# TODO: Initialize IBM Model 2 and return the model.
def create_ibm2(aligned_sents):
    return IBMModel2(aligned_sents, 10)#Change to 10 

# TODO: Compute the average AER for the first n sentences
#       in aligned_sents using model. Return the average AER.
def compute_avg_aer(aligned_sents, model, n):
    sum_aer=0.0
    #aer=[]
    for sentence in aligned_sents[:n]:
	sum_aer=sum_aer+sentence.alignment_error_rate(model.align(sentence))
	#aer.append(sentence.alignment_error_rate(model.align(sentence)))
    #print aer
    return sum_aer/n

# TODO: Computes the alignments for the first 20 sentences in
#       aligned_sents and saves the sentences and their alignments
#       to file_name. Use the format specified in the assignment.
def save_model_output(aligned_sents, model, file_name):
    op_file=open(file_name,'w')
    for sentence in aligned_sents[:20]:
	res=model.align(sentence)
	op_file.write(str(res.words)+'\n')
        op_file.write(str(res.mots)+'\n')
        op_file.write(str(res.alignment)+'\n')
	op_file.write('\n')
	
    op_file.close()

def main(aligned_sents):
    #time.clock()
    ibm1 = create_ibm1(aligned_sents)
    save_model_output(aligned_sents, ibm1, "ibm1.txt")
    avg_aer = compute_avg_aer(aligned_sents, ibm1, 50)

    print ('IBM Model 1')
    print ('---------------------------')
    print('Average AER: {0:.3f}\n'.format(avg_aer))

    ibm2 = create_ibm2(aligned_sents)
    save_model_output(aligned_sents, ibm2, "ibm2.txt")
    avg_aer = compute_avg_aer(aligned_sents, ibm2, 50)
    
    print ('IBM Model 2')
    print ('---------------------------')
    print('Average AER: {0:.3f}\n'.format(avg_aer))
    #print ('Total time taken for Part A: '+str(time.clock())+' seconds')
