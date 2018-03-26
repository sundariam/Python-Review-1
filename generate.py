import random
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model")
parser.add_argument("--length", type=int)
args = parser.parse_args()

f = open(args.model, 'rb')
d = pickle.load(f)
f.close()
k = list(d.keys())
firstword = random.choice(k)
List = []
List.append(firstword)
for i in range(args.length - 1):
    x = []  # временный массив, учитывая частоты
    t = d[List[i]]  # словарь возможных слов после List[i]
    for j in t:
        for k in range(t[j]):
            x.append(j)
    List.append(random.choice(x))

for i in range(len(List)):
    print(List[i], end=' ')
