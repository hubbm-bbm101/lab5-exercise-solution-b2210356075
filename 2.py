def isValid_eMail(str1):
    check1 = False
    check2 = False

    for i in str1:
        if i == "@":
            check1 = True
        elif i == ".":
            check2 = True

    if check1 and check2:
        return True
    else:
        return False


email = input("Please enter your email: ")

if isValid_eMail(email):
    print("It's a valid email!")
else:
    print("It's not a valid email!")
