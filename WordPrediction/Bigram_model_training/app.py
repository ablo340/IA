from nltk import bigrams, ConditionalFreqDist, FreqDist
from nltk.lm.preprocessing import flatten, pad_both_ends
from nltk.util import everygrams
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

text = 'i love chinese food. chinese people love food.'

model = MLE(2)


def preprocessText(txt):  # preprocess the sentences text
    sentences = txt.split('.')
    if '' in sentences:
        sentences.remove('')
    sentences = [sentence.strip(' ') for sentence in sentences]

    return [sentence.split(' ') for sentence in sentences]


'''def preprocess(sentence_list):  # preprocess the bigram model
    preprocessed = [pad_both_ends(s, n=2) for s in sentence_list]
    tokens = list(flatten(preprocessed))
    model = bigrams(tokens)
    return model
    
b_t = preprocess(preprocessText(text))
v = flatten(preprocessText(text))
training(b_t, v)
'''


# preprocess the bigram model (method 2 more direct, to avoid re-creating the text in memory)
def preprocess(sentence_list):
    b_train, vocabu = padded_everygram_pipeline(4, sentence_list)  # 2 for bigram
    return b_train, vocabu  # return the bigram model


def training(t, v):
    model.fit(t, v)


if __name__ == '__main__':
    b_training, vocabulary = preprocess(preprocessText(text))  # get bigram training and its vocabulary
    training(b_training, vocabulary)  # fit/adjust/improve the model
    """
    p(chinese/love) = c(love chinese)/c(love) = 1 / 2 = 0.5
    p(chinese/i love) = c(i love chinese) / c(i love) = 1 / 1 = 1
    p(food/i love chinese) = c(i love chinese food) / c(i love chinese) = 1 / 1 = 1
    """
    print(model.score('chinese', ['love']))  # get the likelihood of 'love chinese' (bigram model)
    print(model.score('chinese', ['i', 'love']))  # get the likelihood of 'i love chinese' (trigram model)
    print(model.score('food', ['i', 'love', 'chinese']))  # get the likelihood of 'i love chinese food' (4-gram model)


