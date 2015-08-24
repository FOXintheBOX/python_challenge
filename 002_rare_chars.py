with open('002_rare_chars.txt', 'r') as input:
    data = input.read()

char_count = {}
string_out = ""

for char in data:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        string_out += char

print char_count
print string_out
