import nltk

corpus = 'Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The result is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.'

documents = nltk.sent_tokenize(corpus)
print(documents)

word_tokens = [nltk.word_tokenize(doc) for doc in documents] 
print(word_tokens)
