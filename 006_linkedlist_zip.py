import zipfile

address = "90052"
linked_list = {}
end_of_list = False

while not end_of_list:

    with open("./channel/" + address + '.txt', 'r') as input:
        data = input.read()
    input.close()

    pointer = data.split()[-1]
    if pointer.isdigit():
        linked_list[address] = [pointer]
        address = pointer
    else:
        end_of_list = True

file = zipfile.ZipFile('channel.zip','r')
infos = file.infolist()

for info in infos:
    key = info.filename[:-4]
    if key in linked_list:
        value = linked_list[key]
        value.append(info.comment)
        linked_list[key] = value

end_of_list = False
address = "90052"
out_str = ""
while not end_of_list:
    if address in linked_list:
        out_str += linked_list[address][1]
        address = linked_list[address][0]
    else: end_of_list = True

print out_str
