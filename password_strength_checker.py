import stdiomask

inp = stdiomask.getpass()

common_passwords = open("common_passwords.txt", "r")
for passwords in common_passwords:
    passwords = common_passwords.read()

length = len(inp)
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
alp_cap = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

weak = False
medium = False
strong = False
very_strong = False

if inp in passwords:
    print("Password Strength: Very Weak")

elif inp not in passwords:
    if length >= 8:
        weak = True
        for i in nums:
            if i in inp:
                weak = False
                medium = True
                for j in alp_cap:
                    if j in inp:
                        medium = False
                        strong = True
                        for m in symbols:
                            if m in inp:
                                strong = False
                                very_strong = True
    else:
        print("Password Strength: Very Weak")


if weak == True:
    print("Password Strength: Weak")

elif medium == True:
    print("Password Strength: Medium")

elif strong == True:
    print("Password Strength: Strong")

elif very_strong == True:
    print("Password Strength: Very Strong")
