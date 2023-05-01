### single alphabet change (4->1)
alphabet = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

reverse_alphabet = {v: k for k, v in alphabet.items()}

def change_alp(alp):
    if alp == " ":
        return ' '
    elif int(alphabet.get(alp))-3>0:
        revise_value = int(alphabet.get(alp))-3 # D -> 4 -> 1
        revise_alp = reverse_alphabet.get(revise_value) # 1 -> A
    elif int(alphabet.get(alp))==1:
        revise_alp = "X"
    elif int(alphabet.get(alp))==2:
        revise_alp = "Y"
    elif int(alphabet.get(alp))==3:
        revise_alp = "Z"
    return revise_alp

content = input('write your content : ')

char_list = list(content)
new_list = []
for i in char_list:
    new_content = change_alp(i)
    new_list.append(new_content)

for i in new_list:
    print(i, end = "")

