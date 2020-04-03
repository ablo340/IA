from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

model = MLE(2)


def preparecorpus(file):
    book = open(file, "r")
    txt = book.readlines()
    list_sentences = list([a.translate({ord(i): None for i in '\n,?!:;'}) for a in txt])  # delete ponctuations
    list_sentences = [elem.split('.') for elem in list_sentences]
    for elem in list_sentences:
        if '' in elem:
            elem.remove('')

    txt = [sentence.strip(' ') for sentences in list_sentences for sentence in sentences]
    txt = map(str.lower, txt)
    return [s.split(' ') for s in txt]


def preprocess(sentence_list):
    b_train, vocabu = padded_everygram_pipeline(2, sentence_list)  # 2 for bigram
    return b_train, vocabu  # return the bigram model train and vocabulary


def training(t, v):
    model.fit(t, v)


if __name__ == '__main__':
    b_training, vocabulary = preprocess(preparecorpus('corpus'))  # get bigram training and its vocabulary

    training(b_training, vocabulary)  # fit/adjust/improve the model

    sentence = []
    print("Appuyez 'enter' apres avoir ecrit chaque mot et 'space' lorsque vous avez terminé votre phrase\n"
          "Veuillez ecrire svp")
    while True:
        word = input(' '.join(sentence) + ' ')

        if word == ' ':
            break

        sentence.append(word)
        next_word = model.generate(3, text_seed=[word], random_seed=2)  # list of 3 next word guessed
        if '<s>' in next_word:
            next_word.remove('<s>')

        if '</s>' in next_word:
            next_word.remove('</s>')

        print(next_word)  # next word


    print("votre phrase est : " + " ".join(sentence))










