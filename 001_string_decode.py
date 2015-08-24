import string

text_in = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text_out = ""

map = string.maketrans(string.lowercase,string.lowercase[2:] + "ab" )
print text_in.translate(map)

"""
for char in text_in:
    if char == 'y': char_out = 'a'
    elif char == 'z': char_out = 'b'
    else:
        if char in string.lowercase:
            char_out = chr(ord(char) + 2)
        else: char_out = char
    text_out += char_out
print text_out

"""
