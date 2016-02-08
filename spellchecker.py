#Algorithim for checking and spelling words correctly

import re, collections

def words(text): return re.findall('[a-z]',text.lower())

def train(features):
    model = collection.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('big.text').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edist1(word):
    splits = [(word[:i],word[i:]) for i in range (len(words)+1)]
    deletes = [a+b[1:] for a, b in splits if b]
    transposes = [a +b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces = [a + c +b[1:] for a, b in splits for c in alpahabet if b]
    inserts = [a +c +b for a,b in splits for c in alphabet]
    return set (deletes + transposes + replaces + inserts)



