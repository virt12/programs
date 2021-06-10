import nltk

nltk.download('punkt')

sentence = """NLTP related with making machines to understand humang language and reply with appropriate
responses"""

tokens = nltk.word_tokenize(sentence)

print(tokens)