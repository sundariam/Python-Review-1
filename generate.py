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
    possible_words = words[ourtext[i]]  # словарь возможных слов после ourtext[i]
    population = []
    weights = []
    for j in possible_words:
        population.append(j)
        weights.append(possible_words[j])
    new_word = random.choices(population, weights, k=1)  # получаем список из 1 нового слова
    ourtext.append(new_word[0])

print(' '.join(ourtext))
