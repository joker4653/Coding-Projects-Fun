# check if password is in common list of passwords...
# check if password matches OWSAP standards for passwords
# can be updated with multi threading to increase speed


def check_known(pw):
    with open("password_list/rockyou.txt", "rt") as pass_lists:
        while line := pass_lists.readline() != None:
            line.rstrip("\n")
            if line == pw:
                return 0


def check_standards(pw):
    pass



if __name__ == "__main__":
    name = input("Enter a Password:")

    if check_known(str(name)) == 0:
        print("Password is a known compromised password. Do not Use.")
        quit()

    check_standards(str(name))