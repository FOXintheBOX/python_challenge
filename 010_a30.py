a = [1, 11, 21, 1211, 111221,]

list = ['1']

for i in range(1,31):
    chars = list[-1]
    next_str = ""
    index = 0
    eof = False
    while eof == False:
        same_digit = True
        counter = 0
        while same_digit == True:
            char = chars[index]
            if index == len(chars) - 1:
                counter += 1
                same_digit = False
                eof = True
            else:
                if chars[index + 1] != chars[index]: same_digit = False
                index += 1
                counter += 1
        next_str += str(counter) + char
    list.append(next_str)

print len(list[30])
