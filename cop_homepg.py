
def Coperative_homepage():
    print("Welcome to Online Cooperative portal !!!")
    print("""
    Enter 1 as member
    Enter 2 as non_memeber""")
    User = input(">>> ")
    if User == "1":
        from cop_main import member_desk
        member_desk()
    elif User == "2":
        from cop_main import non_member_desk
        non_member_desk()
    else:
        print("Wrong commmand")
        Coperative_homepage()

Coperative_homepage()
