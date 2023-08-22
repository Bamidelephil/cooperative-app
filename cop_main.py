import time
import random
import mysql.connector as connection
conn = connection.connect(host = '127.0.0.1', user = 'root', passwd ='Bam1234del##', database = 'cooperatives')
cursor = conn.cursor()

def member_desk():
    print("Welcome to the member's desk")
    time.sleep(1)
    doo= input("Are you a registered member? ")
    if doo =="yes":
        member_login()
    elif doo=="no":
        member_register()
    else:
      print("Invalid command")
      exit()

def member_register():
    print("Register to be a member of online cooperative")
    val=[]
    copp_info = ("firstname", "lastname", "gender", "Username", "Age", "membership_id", "Loan", "Refund", "Contribution", "Interest", "email", "passwd", "loan_interest")
    querry = "INSERT INTO cooperatives.member_coopertive (first_name, last_name, gender,Username, Age, membership_id, Loan, Refund, Contribution, Interest, email, passwd, loan_interest) VALUES (%s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s)"
    for holder in range(13):
        if copp_info[holder]== "membership_id":
             user = random.randint(45000001, 45900009)
        elif copp_info[holder]== "Loan":
             user = 0   
        elif copp_info[holder]== "Refund":
             user = 0
        elif copp_info[holder]== "Interest":
             user = 0
        elif copp_info[holder]== "Contribution":
             user = 0
        elif copp_info[holder]== "loan_interest":
             user = 0
        else:
             user = input(f"Enter your {copp_info[holder]}: ")
        val.append(user)
    cursor.execute(querry, val)
    conn.commit()
    print("You have successfully registered as a member")
    time.sleep(1)
    print(f"Dear {val[0]} {val[1]} you have succesfully registered and your membership_id is {val[5]} ")
    member_login()

def member_login():
    time.sleep(2)
    print("Kindly login your details")
    email = input("Enter your gmail account: ")
    passwd = input("Enter your password ")
    val = (email, passwd)
    querry = "select * from cooperatives.member_coopertive where email=%s and passwd=%s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        print("You have successfully logged in as a memeber")
        time.sleep(1)
        member_decide()
    else:
        print("Invalid username or password")
        time.sleep(1)
        print("You have to register")
        time.sleep(1)
        member_register()

def member_decide():
    print("Kindly select from the following")
    time.sleep(1)
    print(""" what will you like to do?
    1)Loan
    2)Contribution
    3)Repay loan
    4)Eligibility
    5)Logout
    """)
    user = input(">>> ")
    if user =="1":
        member_loan()
    elif user =="2":
        member_CONTD()
    elif user == "3":
        Repayloan()
    elif user == "4":
        member_eligible()
    elif user == "5":
        exit()
    else:
        print("Invalid Command")
        time.sleep(1)
        member_decide()

def member_loan():
    print("Welcome to loan section")
    time.sleep(1)
    member_Id = input("Enter your membership_ID number:")
    val = (member_Id, )
    querry = "SELECT * from cooperatives.member_coopertive where membership_id = %s "
    cursor.execute(querry,val)
    global take
    take = cursor.fetchone()
    if take:
        print(f"Dear {take[1]} {take[2]} you are about to request for a loan")
        time.sleep(2)
        if take[8]==0:
            if take[9] > 0:
                user =int(input("How much do you want borrow? "))
                val = (user, member_Id) 
                querry= "UPDATE cooperatives.member_coopertive SET Loan = %s where membership_id = %s "
                cursor.execute(querry,val)
                conn.commit()
                interest = (2 / 100) * user
                val4 = (interest, member_Id)
                query3 = "UPDATE cooperatives.member_coopertive SET loan_interest = %s where membership_id = %s "
                cursor.execute(query3, val4)
                conn.commit()
                query = "SELECT * from cop_treasure where ID = %s"
                val2 = (1, )
                cursor.execute(query, val2)
                res = cursor.fetchone()
                newAm = user + res[2]
                query2 = "UPDATE cop_treasure SET Total_expenditure = %s where ID =%s"
                val3 = (newAm, 1)
                cursor.execute(query2, val3)
                conn.commit()
                print(f"Dear esteemed customer you have successfully borrowed: #{user} and your interest is {interest}")
                time.sleep(2)
                print("Do you want to perform another operation")
                takk =input(">>> ")
                if takk =="yes":
                    member_decide()
                elif takk=="no":
                    exit()
                else:
                    print("Invaild Command.")
                    time.sleep(1)
                    exit()
            elif take[9] == 0:
                user =int(input("How much do you want borrow? "))
                val = (user, member_Id) 
                querry= "UPDATE cooperatives.member_coopertive SET Loan = %s where membership_id = %s "
                cursor.execute(querry,val)
                conn.commit()
                interest = (5 / 100) * user
                val4 = (interest, member_Id)
                query3 = "UPDATE cooperatives.member_coopertive SET loan_interest = %s where membership_id = %s "
                cursor.execute(query3, val4)
                conn.commit()
                query = "SELECT * from cop_treasure where ID = %s"
                val2 = (1, )
                cursor.execute(query, val2)
                res = cursor.fetchone()
                newAm = user + res[2]
                query2 = "UPDATE cop_treasure SET Total_expenditure = %s where ID =%s"
                val3 = (newAm, 1)
                cursor.execute(query2, val3)
                conn.commit()
                print(f"Dear esteemed customer you have successfully borrowed: #{user} and your interest is {interest}")
                time.sleep(2)
                print("Do you want to perform another operation")
                takk =input(">>> ")
                if takk =="yes":
                    member_decide()
                elif takk=="no":
                    exit()
                else:
                    print("Invaild Command.")
                    time.sleep(1)
                    exit()
        else:
            print("Sorry!!! You've taken a loan already pay up to access another loan ")
            time.sleep(2)
            member_decide()

def member_contribution():
    print("Welcome to contribution section")
    time.sleep(1)
    user = input("Enter the amount you want to contribute")
    passwd = input("Enter your password ")
    query= "SELECT * from member_coopertive where passwd = %s"
    vall = (passwd, )
    cursor.execute(query, vall)
    result = cursor.fetchone()
    if result:
        new_amount = int(user) + result[9]
        val =(new_amount, passwd )
        querry = " UPDATE cooperatives.member_coopertive SET contribution = %s where passwd = %s"
        cursor.execute(querry, val)
        conn.commit()
        time.sleep(2)
        print("You have succesfully contributed in your pulse")
        intrest = 0.15 * new_amount
        querry3 = "UPDATE cooperatives.member_coopertive SET Interest = %s where passwd = %s"
        val3 =(intrest, passwd )
        cursor.execute(querry3, val3)
        conn.commit()
        time.sleep(2)
        print("Do you want to perform another operation")
        takk =input(">>> ")
        if takk =="yes":
            member_decide()
        elif takk=="no":
            exit()
        else:
            print("Invaild Command.")
            time.sleep(1)
            exit()
    else:
        print("Wrong Password. Try again")
        member_contribution()
def member_CONTD():
    print("""
    1)Add Contribution
    2)Exit
    """)
   
    user = (input(">>> "))  
    if user =="1":
        print("Redirecting to contribution section......")
        time.sleep(2)
        member_contribution()    
    elif user =="2":
        print("Thank you!!! Bye")
        exit
    else:
        print("Invalid Command")
        time.sleep(1)
        exit()

def Repayloan():
    print("Redirecting to refund section...")
    time.sleep(2)
    print("Input the amount to repay")
    user = input(">>> ")
    passwd =input ("Enter your Password: ")
    query = "SELECT * from member_coopertive where passwd = %s"
    vall = (passwd, )
    cursor.execute(query, vall)
    result = cursor.fetchone()
    if result:
        new_amount = int(user) + result[8]
        val = (new_amount, passwd)
        querry = "UPDATE cooperatives.member_coopertive SET Refund = %s where passwd = %s "
        cursor.execute(querry,val)
        conn.commit()
        print(f"You have successfully send #{user} has your refund loan")
        time.sleep(2)
        print("Do you want to perform another operation")
        takk =input(">>> ")
        if takk =="yes":
            member_decide()
        elif takk=="no":
            exit()
        else: 
            print("Invaild Command.")
            time.sleep(1)
            exit()        
    else:
        print("Invalid password")  
        Repayloan()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        
def payment_status():
    print("Dear customer you are about to check payment status")
    time.sleep(1)
    email = input("Kindly input your email")
    time.sleep(1)
    user_Id = input("Kindly enter your user_ID ")
    val = (email, user_Id)
    querry = "SELECT * from cooperative where email = %s and user_Id=%s"
    cursor.execute(querry,val)
    pay = cursor.fetchone()
    if pay:
        print("Accessing User data page....")
        time.sleep(2) 
        if pay[10]==0:
            time.sleep(3)
            print("Paid")

def member_eligible():
    print("Welcome to loan eligibility section")
    time.sleep(2)
    print("""Will you like to check your eligibility status? 
    1)Check eligibility
    2)Proceed to loan
    3)Exit
      """)
    user = (input(">>> "))
    if user =="1":
        time.sleep(2)
        print("""The following are the requirement to check if you are eligible for the load.
        1)You must be a registered member or user of this noble loan cooperative
        2)You must provide some important document before you can access the loan.
          such as: BVN,NIN,Date of Birth, Occupation and your Statement of Account.
        3)A registered member garantor
        4)Your ID is very importand in accessing the loan.
        5)To get more info in accessing the loan visit... www.online_loanApp.com
        """)
        time.sleep(10)
        print("Do you wish to access the loan? ")
        time.sleep(1)
        print("""
        1)Press 1 to access loan
        2)Press 2 to eligibity menu
        3)Press 3 to move to main-menu
        """)
        user = input(">>>: ")
        if user =="1":
            member_loan()
        elif user =="2":
            member_eligible()
        elif user =="3":
            print("Redirecting to main- menu.......")
            time.sleep(2)
            member_decide()
        else:
            print("Invalid Command")
            time.sleep(1)
            exit()
    elif user =="2":
        member_loan()
    elif user =="3":
        exit()
    else:
        print("Invaild Command")
        time.sleep(2)
        member_eligible()



# --------------- users section --------------



def non_member_desk():
    print("Welcome to the non-member(users) desk")
    time.sleep(2)
    doo= input("Are you a registered NM-users? ")
    if doo =="yes":
        non_member_login()
    elif doo=="no":
        non_member_register()
    else:
      print("Invalid command")
      exit()

def non_member_register():
    print("Register to be a user member of online cooperative")
    val=[]
    copp_info = ("firstname", "lastname", "gender", "Age", "user_id", "Balance", "Refund", "Loan_amount","Interest", "email", "passwd","loan_interest")
    querry = "INSERT INTO non_membercop (first_name, last_name, gender, Age, user_id, Balance, Refund, Loan_amount, Interest, email, passwd,loan_interest) VALUES ( %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s)"
    for holder in range(12):
        if copp_info[holder]== "user_id":
             user = random.randint(23000001, 25900000)
        elif copp_info[holder]== "Balance":
             user = 0
        elif copp_info[holder]== "Refund":
             user = 0
        elif copp_info[holder]== "Interest":
             user = 0
        elif copp_info[holder]== "Loan_amount":
             user = 0
        elif copp_info[holder]== "loan_interest":
             user = 0
        else:
             user = input(f"Enter your {copp_info[holder]}: ")
        val.append(user)
    cursor.execute(querry, val)
    conn.commit()
    print("You have successfully registered as a member")
    print(f"Dear {val[0]} {val[1]} you have succesfully registered as a NON-MEMBER of online cooperative and your user-id is {val[4]}")
    non_member_login()

def non_member_login():
    email = input("Enter your gmail account: ")
    passwd = input("Enter your password ")
    val = (email, passwd)
    querry = "select * from non_membercop where email=%s and passwd=%s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        print("You have successfully logged in as a memeber")
        time.sleep(1)
        non_member_decide()
    else:
        print("Invalid username or password")
        time.sleep(1)
        print("You have to register")
        time.sleep(1)
        non_member_register()

def non_member_decide():
    print("Kindly select from the following")
    time.sleep(2)
    print(""" what will you like to do?
    1)Obtain Loan
    2)Payment Status
    3)Eligibility
    4)Repay loan    
    5)Exit
    """)
    user = input(">>> ")
    if user =="1":
        non_member_loan()
    elif user =="2":
        non_member_loan()
    elif user == "3":
       non_member_eligible()
    elif user == "4":
        nonRepay_loan()
    elif user == "5":
        exit()
    else:
        print("Invalid Command")
        time.sleep(1)
        non_member_decide()

def non_member_loan():
    print("Welcome to user loan section")
    time.sleep(1)
    User_ID = input("Enter your User_ID number:")
    val = (User_ID, )
    querry = "SELECT * from non_membercop where user_id = %s "
    cursor.execute(querry,val)
    global take
    take = cursor.fetchone()
    if take:
        print(f"Dear {take[1]} {take[2]} you are about to request for a loan")
        time.sleep(2)
        if take[6]==0:
            user =int(input("How much do you want borrow? "))
            val = (user, User_ID) 
            querry= "UPDATE non_membercop SET Loan_amount = %s where user_id = %s "
            cursor.execute(querry,val)
            conn.commit()
            interest = (10 / 100) * user
            val4 = (interest, User_ID)
            query3 = "UPDATE non_membercop SET loan_interest = %s where user_id = %s "
            cursor.execute(query3, val4)
            conn.commit()
            query = "SELECT * from cop_treasure where ID = %s"
            val2 = (1, )
            cursor.execute(query, val2)
            res = cursor.fetchone()
            newAm = user + res[2]
            query2 = "UPDATE cop_treasure SET Total_expenditure = %s where ID =%s"
            val3 = (newAm, 1)
            cursor.execute(query2, val3)
            conn.commit()
            print(f"Dear esteemed customer you have successfully borrowed: #{user} and your interest is {interest}")
            time.sleep(2)
            print("Do you want to perform another operation")
            takk =input(">>> ")
            if takk =="yes":
                non_member_decide()
            elif takk=="no":
                exit()
            else:
                print("Invaild Command.")
                time.sleep(1)
                exit()
        else:
            print("You've taken a loan already pay up to access another loan ")
            time.sleep(2)
            non_member_decide()



def non_member_eligible():
    print("Welcome to loan eligibility section")
    time.sleep(2)
    print("""Will you like to check your eligibility status? 
    1)Check eligibility
    2)Proceed to loan
    3)Exit
      """)
    user = (input(">>> "))
    if user =="1":
        time.sleep(2)
        print("""The following are the requirement to check if you are eligible for the load.
        1)You must be a registered member or user of this noble loan cooperative
        2)You must provide some important document before you can access the loan.
          such as: BVN,NIN,Date of Birth, Occupation and your Statement of Account.
        3)A registered member garantor
        4)Your ID is very importand in accessing the loan.
        5)To get more info in accessing the loan visit... www.online_loanApp.com
        """)
        time.sleep(10)
        print("Do you wish to access the loan? ")
        time.sleep(1)
        print("""
        1)Press 1 to access loan
        2)Press 2 to eligibity menu
        3)Press 3 to move to main-menu
        """)
        user = input(">>>: ")
        if user =="1":
            non_member_loan()
        elif user =="2":
           non_member_eligible()
        elif user =="3":
            print("Redirecting to main- menu.......")
            time.sleep(2)
            non_member_decide()
        else:
            print("Invalid Command")
            time.sleep(1)
            exit()
    elif user =="2":
       non_member_loan()
    elif user =="3":
        exit()
    else:
        print("Invaild Command")
        time.sleep(2)
        non_member_eligible()



def nonRepay_loan():
    print("Redirecting to refund section...")
    time.sleep(2)
    print("Input the amount to repay")
    user = input(">>> ")
    passwd =input ("Enter your Password: ")
    query = "SELECT * from non_membercop where passwd = %s"
    vall = (passwd, )
    cursor.execute(query, vall)
    result = cursor.fetchone()
    if result:
        print("Correct Password")
        new_amount = int(user) + result[7]
        val = (new_amount, passwd)
        querry = "UPDATE non_membercop SET Refund = %s where passwd = %s "
        cursor.execute(querry,val)
        conn.commit()
        print(f"You have successfully send #{user} has your refund loan")
        time.sleep(2)
        print("Do you want to perform another operation")
        takk =input(">>> ")
        if takk =="yes":
            member_decide()
        elif takk=="no":
            exit()
        else: 
            print("Invaild Command.")
            time.sleep(1)
            exit()        
    else:
        print("Invalid password")  
        nonRepay_loan()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         






# Treasure Table
def totalIncome():
    query = "SELECT sum(Contribution) from member_coopertive"
    cursor.execute(query)
    result = cursor.fetchone()
    query2 = "UPDATE cop_treasure SET Total_income = %s where ID = %s"
    val = (result[0], 1)
    cursor.execute(query2, val)
    conn.commit()
