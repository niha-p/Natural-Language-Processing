from nltk.compat import python_2_unicode_compatible

printed = False

@python_2_unicode_compatible
class FeatureExtractor(object):
    @staticmethod
    def _check_informative(feat, underscore_is_informative=False):
        """
        Check whether a feature is informative
        """

        if feat is None:
            return False

        if feat == '':
            return False

        if not underscore_is_informative and feat == '_':
            return False

        return True

    @staticmethod
    def find_left_right_dependencies(idx, arcs):
        left_most = 1000000
        right_most = -1
        dep_left_most = ''
        dep_right_most = ''
        for (wi, r, wj) in arcs:
            if wi == idx:
                if (wj > wi) and (wj > right_most):
                    right_most = wj
                    dep_right_most = r
                if (wj < wi) and (wj < left_most):
                    left_most = wj
                    dep_left_most = r
        return dep_left_most, dep_right_most

    @staticmethod
    def extract_features(tokens, buffer, stack, arcs):
        """
        This function returns a list of string features for the classifier

        :param tokens: nodes in the dependency graph
        :param stack: partially processed words
        :param buffer: remaining input words
        :param arcs: partially built dependency tree

        :return: list(str)
        """

        """
        Think of some of your own features here! Some standard features are
        described in Table 3.2 on page 31 of Dependency Parsing by Kubler,
        McDonald, and Nivre

        [http://books.google.com/books/about/Dependency_Parsing.html?id=k3iiup7HB9UC]
        """

        result = []


        global printed
        if not printed:
            #print("This is not a very good feature extractor!")
            printed = True
	
		
	#MY Feature 2 - Distance between BUF[0] and STK[0]
	if stack and buffer:
	    stack_idx0=stack[-1]
	    buffer_idx0=buffer[0]
	    
	    result.append('STK_0_BUF_0_DISTANCE_'+str(abs(stack_idx0 - buffer_idx0)))			
	
        # an example set of features:
        if stack:
            stack_idx0 = stack[-1]
            token = tokens[stack_idx0]
            if FeatureExtractor._check_informative(token['word'], True):
                result.append('STK_0_FORM_' + token['word'])

            if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                feats = token['feats'].split("|")
                for feat in feats:
                    result.append('STK_0_FEATS_' + feat)
	    """	      
	    if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
                tags = token['lemma'].split("|")
                for tag in tags:
                    result.append('STK_0_LEMMA_' + tag)	   
	    """
	    
	    #MY Feature 1 - POS of STK[0]	    
	    if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
		tags=token['tag'].split("|")
		for tag in tags:
		    result.append('STK_0_TAG'+tag)

	    # POS of STK[1]
	    if len(stack) > 1:
                stack_idx1 = stack[-2]
                token = tokens[stack_idx1]
                if 'tag'in token and FeatureExtractor._check_informative(token['tag']):
                    result.append('STK_1_TAG_' + token['tag'])
	
	    
            # Left most, right most dependency of stack[0]
            dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(stack_idx0, arcs)

            if FeatureExtractor._check_informative(dep_left_most):
                result.append('STK_0_LDEP_' + dep_left_most)
            if FeatureExtractor._check_informative(dep_right_most):
                result.append('STK_0_RDEP_' + dep_right_most)

	    
	    #MY Feature 3 - No. of children of STK[0]
	    l_children=0
	    r_children=0
	    stack_idx0=stack[-1]
	   
	    for arc in arcs:
		if tokens[arc[0]]==stack_idx0:
		    if tokens[arc[2]['address']]<=stack_idx0['address']:
			l_children=l_children+1
		    else:
		        r_children=r_children+1
	    result.append('STK_0_L_CHILD_'+str(l_children))
	    result.append('STK_0_R_CHILD_'+str(r_children))
	    
	   
        if buffer:
            buffer_idx0 = buffer[0]
            token = tokens[buffer_idx0]
            if FeatureExtractor._check_informative(token['word'], True):
                result.append('BUF_0_FORM_' + token['word'])

            if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                feats = token['feats'].split("|")
                for feat in feats:
                    result.append('BUF_0_FEATS_' + feat)
	    """	
	    if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
                tags = token['lemma'].split("|")
                for tag in tags:
                    result.append('BUF_0_LEMMA_' + tag)	    
	    
	    """
	    
	    #MY Feature 1 - POS of BUF[0] 
	    if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                tags = token['tag'].split("|")
                for tag in tags:
                    result.append('BUF_0_TAG_' + tag)
	   
	    # POS of BUF[1]	   
	    if len(buffer) > 1:
                buffer_idx1 = buffer[1]
                token = tokens[buffer_idx1]
                if 'tag'in token and FeatureExtractor._check_informative(token['tag']):
                    result.append('BUF_1_TAG_' + token['tag'])
 	   
	    
	    #MY Feature 3 - No. of children of STK[0]
            l_children=0
	    r_children=0
            buffer_idx0=buffer[0]

	    for arc in arcs:
                if tokens[arc[0]]==buffer_idx0:
                    if tokens[arc[2]['address']]<=buffer_idx0['address']:
                        l_children=l_children+1
                    else:
                        r_children=r_children+1
            result.append('BUF_0_L_CHILD_'+str(l_children))
            result.append('BUF_0_R_CHILD_'+str(r_children))
	
  	    
            dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(buffer_idx0, arcs)

            if FeatureExtractor._check_informative(dep_left_most):
                result.append('BUF_0_LDEP_' + dep_left_most)
            if FeatureExtractor._check_informative(dep_right_most):
                result.append('BUF_0_RDEP_' + dep_right_most)

        return result
