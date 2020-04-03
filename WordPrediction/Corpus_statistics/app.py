import argparse
import json
import time


def inputCorpus(word):   # use python fct Counter() to update ==> delete the fct
    if word in corpus:
        corpus[word] += 1
    else:
        corpus[word] = 1


def split(listwords):
    result = []
    for elem in listwords:
        x = elem.split(" ")
        for string in x:
            w = string.translate({ord(i): None for i in '\n.,?!:;'})  # delete the ponctuations
            result.append(w)  # add each word in file to a list

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='corpus text file to analyse')
    parser.add_argument('-o', '--out', metavar='PATH',
                        help='path to the file where to output the result of the analysis')
    args = parser.parse_args()

    corpus = {}

    print('Analysing', args.file)

    book = open(args.file, "r")
    sentences = book.readlines()  # list of all sentences in file
    words = split(sentences)  # list of all words in file
    for mot in words:
        inputCorpus(mot)  # put each word in the corpus

    with open('corpus.json', 'w') as json_file:  # result as json file
        json.dump(corpus, json_file)

    print("Waiting...")
    time.sleep(2)
    print("Your Json is created")

    if args.out:  # if optional argument --out
        time.sleep(0.5)
        print('Writing output to', args.out)

        with open(args.out + '.txt', 'w') as txt_file:  # result as text file
            for key, value in corpus.items():
                txt_file.write(key + ":" + str(value) + "\n")

        txt_file.close()
    else:  # default option
        print('Writing output to stdout')
        for key, value in corpus.items():
            print(key + ":" + str(value))

    json_file.close()
    book.close()
