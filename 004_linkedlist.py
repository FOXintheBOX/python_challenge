import urllib
import string

link = "8022"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

for i in range(400):
    x = urllib.urlopen(url+link)
    data = x.read()
    print data
    words = data.split()
    for word in words:
        invalid = False
        for char in word:
            if char not in string.digits:
                invalid = True
        if invalid == False:
            output_str = word

    print word
    print "*******"
    link = str(int(word)/1.0)
