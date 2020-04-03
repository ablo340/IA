import random

from nltk import bigrams, ConditionalFreqDist, FreqDist
from nltk.lm.preprocessing import flatten, pad_both_ends
import json
import time


def sentences(file):
    res = []
    book = open(file, "r")
    txt = book.readlines()
    list_sentences = list([a.translate({ord(i): None for i in '\n,?!:;'}) for a in txt])  # delete ponctuations

    for s in list_sentences:
        for elem in s.split('.'):
            if elem != '':
                res.append(elem.lower())

    return res


def jsoncorpus(dic):
    with open('corpus.json', 'w') as json_file:  # result as json file
        json.dump(dic, json_file, indent=2)
        print("Waiting...")
        time.sleep(2)
        print("Your Json is created")
    json_file.close()


def traincorpus():
    for ug, o_u in fd.items():  # parcours l'unigramme
        for bg, o_b in cfd[ug].items():  # parcours le bigramme
            # print(ug, bg, o_b / o_u)
            corpus[ug + " " + bg] = o_b / o_u

    jsoncorpus(corpus)  # make a json file of training of the bigram model from the corpus file (book)


def takeSecond(elem):
    return elem[1]


if __name__ == '__main__':
    # liste contenant des sous liste de chaque mot avec les pads <s> et </s> pour le debut et la fin de phrase
    preprocessed = [pad_both_ends(s.strip(' ').split(' '), n=2) for s in sentences('book')]

    # avec flatten() element dans sous liste de preprocessed extrait pour faire une liste
    tokens = list(flatten(preprocessed))

    fd = FreqDist(tokens)  # unigramme (dict avec chaque mot et sa frequence

    model = bigrams(tokens)  # model du bigramme
    cfd = ConditionalFreqDist(model)  # bigramme (dict avec sous dict: clés = next mots et valeur = leur frequence)

    corpus = {}  # dict of corpus

    traincorpus()  # make a json file of training of the bigram model from the corpus file (book)
    # [print(s, o) for s, o in fd.items()]

    nex = '<s>'
    sentence = []
    while nex != '</s>':
        words = []  # liste de choix des mots suivant
        nm = 0  # pour choix du mot (pour plus tard)
        for word, frq in cfd[nex].items():
            words.append((word, frq))  # mettre les choix et leur frq dans un tuple

        words.sort(key=takeSecond, reverse=True)  # sort choice du plus probable au moins

        while True:
            nex = words[nm][0]
            if nex not in sentence:  # si le mot n'est pas dans la liste alors on l'ajoute
                if nex != '</s>':
                    sentence.append(nex)
                break
            elif nm+1 < len(words):  # si il a a un autre choix pour le mot suivant
                nm += 1
            else:  # si n'il n'y a plus de choix pour le mot suivant
                if nex != '</s>':
                    sentence.append(nex)
                break

    print("La phrase la plus probable est : " + " ".join(sentence))
