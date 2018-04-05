import re
import pickle
import argparse


def AddNewWord(currentword, nextword):
    if currentword not in words:
        words[currentword] = {}

    i_dict = words[currentword]
    if nextword in i_dict:
        i_dict[nextword] += 1
    else:
        i_dict[nextword] = 1


def lastword_dict(lastword, words, nextword):
    if lastword in words:
        special_dict = words[lastword]  # отдельно рассматриваем последнее
        # слово в строке и его словарь
        if nextword in special_dict:
            special_dict[nextword] += 1
        else:
            special_dict[nextword] = 1
    else:
        words[lastword] = {}
        special_dict = words[lastword]
        special_dict[nextword] = 1


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", nargs='?')
parser.add_argument("--model")
args = parser.parse_args()

words = {}
lastword = ''

if args.input_dir is not None:
    with open(args.input_dir) as f:
        for line in f:
            result = re.findall(r'\w+', line)
            linesize = len(result)
            if linesize == 0:
                break

            for i in range(linesize - 1):
                AddNewWord(result[i], result[i + 1])

            lastword_dict(lastword, words, result[0])

            lastword = result[linesize - 1]

else:
    f = input()
    for line in f:
        result = re.findall(r'\w+', line)
        linesize = len(result)
        if linesize == 0:
            break

        for i in range(linesize - 1):
            AddNewWord(result[i], result[i + 1])

        lastword_dict(lastword, words, result[0])

        lastword = result[linesize - 1]

with open(args.model, "wb") as f:
    pickle.dump(words, f)
