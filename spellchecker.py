#Algorithim for checking and spelling words correctly

import re, collections

def words(text): return re.findall('[a-z]',text.lower())

def train(features):
    model = collection.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
