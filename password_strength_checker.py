import stdiomask

inp = stdiomask.getpass()

common_passwords = open("common_passwords.txt", 'r')
for passwords in common_passwords:
    passwords = common_passwords.read()

length = len(inp)
nums = ['1','2','3','4','5','6','7','8','9','0']
extra = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]

weak = False
medium = False
strong = False

if inp in passwords:
    print("Password Strength: Very Weak")

elif inp not in passwords:
    if length >= 8:
        weak = True
        for i in nums:
            if i in inp:
                weak = False
                medium = True
                for j in extra:
                    if j in inp:
                        medium = False
                        strong = True

if weak == True:
    print("Password Strength: Weak")

elif medium == True:
    print("Password Strength: Medium")

elif strong == True:
    print("Password Strength: Strong")
