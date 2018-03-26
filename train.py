import re
import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", nargs='?')
parser.add_argument("--model")
args = parser.parse_args()
if args.input_dir is not None:
    f = open(args.input_dir)
else:
    f = input()
d = {}
lastword = ''
for line in f:
    result = re.findall(r'\w+', line)
    n = len(result)
    if n == 0:
        break
    lend = len(d)
    for i in range(n - 1):
        if result[i] in d:
            r = d[result[i]]
        else:
            d[result[i]] = {}

        t = d[result[i]]
        if result[i + 1] in t:
            t[result[i + 1]] += 1
        else:
            t[result[i + 1]] = 1
    if lastword in d:
        t = d[lastword]
        if result[0] in t:
            t[result[0]] += 1
        else:
            t[result[0]] = 1
    else:
        d[lastword] = {}
        t = d[lastword]
        t[result[0]] = 1

    lastword = result[n - 1]

f = open(args.model, 'wb')
pickle.dump(d, f)
f.close()
