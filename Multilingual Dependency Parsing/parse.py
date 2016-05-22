import providedcode
from providedcode.transitionparser import TransitionParser
from providedcode.dependencygraph import DependencyGraph
from providedcode.evaluate import DependencyEvaluator
import sys

tp = TransitionParser.load('english.model')

for line in sys.stdin:
    sentence = DependencyGraph.from_sentence(line)
    parsed = tp.parse([sentence])
    print parsed[0].to_conll(10).encode('utf-8')






















