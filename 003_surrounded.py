import string

with open('003_surrounded.txt', 'r') as input:
    data = input.read()

out_string = ""

for i in range(len(data)-8):
    if data[i] not in string.uppercase:
        if data[i+1] in string.uppercase:
            if data[i+2] in string.uppercase:
                if data[i+3] in string.uppercase:
                    if data[i+4] in string.lowercase:
                        if data[i+5] in string.uppercase:
                            if data[i+6] in string.uppercase:
                                if data[i+7] in string.uppercase:
                                    if data[i+8] not in string.uppercase:
                                        out_string += data[i+4]

print out_string
