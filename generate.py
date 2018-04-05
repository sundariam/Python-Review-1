import random
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model")
parser.add_argument("--length", type=int)
args = parser.parse_args()

with open(args.model, "rb") as f:
    words = pickle.load(f)
allwords = list(words.keys())
firstword = random.choice(allwords)
ourtext = []
ourtext.append(firstword)
for i in range(args.length - 1):
    array_frequence = []  # временный массив, учитывая частоты
    possible_words = words[ourtext[i]]  # словарь возможных слов после List[i]
    for j in possible_words:
        for k in range(possible_words[j]):
            array_frequence.append(j)
    ourtext.append(random.choice(array_frequence))

print(' '.join(ourtext))
