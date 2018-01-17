# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary. 
# Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary.
from collections import OrderedDict


glossary = OrderedDict()
#glossary = {}
glossary['loop'] = 'iterations of files'
glossary['variables'] = 'Box containing a value'

for k,v in glossary.items():
    print("Word: " + k +" "+ " Definitinion: " + v)