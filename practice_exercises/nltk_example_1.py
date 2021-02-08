from nltk.corpus import wordnet as wn

poses = {'n': 'noun', 'v': 'verb',
         'a': 'adjective', 'r': 'adverb', 's': 'adj (s)'}

syn_word = 'good'
print(f"Get all synonymns for {syn_word}")

# _sysnet = synonymn sets
for synset in wn.synsets(syn_word):

    pose = poses[synset.pos()]
    lemmas = ', '.join([l.name() for l in synset.lemmas()])

    print(f'{pose}: {lemmas}')


hypernym_word = 'dog.n.01'
print(f"Get all hypernyms for {hypernym_word}")

# _hypernym = hypernym words

dog_synset = wn.synset(hypernym_word)
hyper = lambda s:s.hypernyms()
print(list(dog_synset.closure(hyper)))