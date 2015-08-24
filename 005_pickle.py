import pickle

with open('banner.p', 'r') as input:
    data = pickle.load(input)

for line in data:
    output = ""
    for datum in line:
        output += datum[0]*datum[1]
    print output
