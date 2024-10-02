import random

class CREATE_AC_AND_CHECK:
    Acount = [('RAFI014', 'Rafi014'), ('hasan014', 'Rafi014')]
    Amount = [120145, 1201400]  

    def displayInfo(self, indexn):
        print(f"YOUR ACCOUNT NUMBER: {self.Acount[indexn][0]}")
        print(f"YOUR PASSWORD: {self.Acount[indexn][1]}")
        print(f"YOUR AMOUNT: {self.Amount[indexn]}")
        ForText=f"Your ACOUNT NUMBER IS: {self.Acount[indexn][0]}.\nYour Amount is: {self.Amount[indexn]}.\n"
        with open("Your info", "w") as text:
          text.write(ForText)
        
    def Create_AC(self):
        print("Enter your full name:")
        name = input()
        print("Enter your Password:")
        pas = input()
        print("Enter your NID Number:")
        NID = input()
        Ac_Number = random.randint(12450, 7841253)
        self.Acount.append((str(Ac_Number), pas))  
        print("ACCOUNT CREATED SUCCESSFULLY!")
        indexnumber = len(self.Acount) - 1
        print(f"YOUR ACCOUNT NUMBER IS {self.Acount[indexnumber][0]}")
        print(f"YOUR PASSWORD IS: {self.Acount[indexnumber][1]}")
        print("FOR THE NEW ACCOUNT, YOU HAVE TO ADD '500' TAKA FIRST. OTHERWISE, YOUR ACCOUNT WILL NOT BE ACTIVE.\nDO YOU WANT TO ADD MONEY? ('yes' or 'no')")
        
        add_money = input().lower()
        if add_money == 'yes':
            add = int(input("Enter your amount: "))  
            if add >= 500:
                self.Amount.append(add)
                print("MONEY ADDED SUCCESSFULLY!")
                print("DO YOU WANT TO SEE YOUR INFO? (yes or no)")
                if input().lower() == 'yes':
                    print("Enter your AC number:")
                    ForAC = input()
                    print("Enter your password:")
                    ForPASS = input()
                    self.cheakingData(ForAC, ForPASS)
            else:
                print("You need to add at least 500 Taka to activate the account.")
                self.Amount.append(0)  
        elif add_money == 'no':
            self.Amount.append(0)  
            self.logout()

    def logout(self):
        print("LOGGED OUT")

    def Transection(self, ACIN):
        print("What do you want?\n1) Deposit.\n2) Withdrow.\n3) Logout.")
        actions=input("please respons by number.")
        if actions == '1':
            print("How much?")
            money=int(input())
            self.Amount[ACIN]=self.Amount[ACIN]+money
            print("DEPOSIT SUCCESFULL!\n here your ammount")
            print(f"your AC number: {self.Acount[ACIN][0]}\nYour Amount: {self.Amount[ACIN]}")
            UpdateData= f"After Deposit.\n Your AC number:{self.Acount[ACIN][0]}\nYour Amount:{self.Amount[ACIN]}\n"
            with open("Your info", "a") as AfterUpdate:
                AfterUpdate.write(UpdateData)

            return
        if actions=="2":
            print("How much?")
            withdrowMoney=int(input())
            if withdrowMoney > self.Amount[ACIN]:
                print(f"Your do not have sufficient balance.\nYour balance is {self.Amount[ACIN]}")
                self.logout()
                return
            elif withdrowMoney <= self.Amount[ACIN]:

                self.Amount[ACIN]= self.Amount[ACIN]- withdrowMoney 
                print("withdrow succesfull!")
                print(f"your AC number: {self.Acount[ACIN][0]}\nYour Amount: {self.Amount[ACIN]}")
                UpdateDataW= f"After Withdrow.\n Your AC number:{self.Acount[ACIN][0]}\nYour Amount:{self.Amount[ACIN]} "
                with open("Your info", "a") as AfterUpdateW:
                  AfterUpdateW.write(UpdateDataW)
                return
        if actions=='3':
            self.logout()
            return

    def cheakingData(self, A, P):
        for For_index, line in enumerate(self.Acount):
            if line[0] == A and line[1] == P:  
                print("ACCOUNT FOUND!")
                print("HERE IS YOUR INFO:")
                self.displayInfo(For_index)
                print("what do you want?\n1) logout\n2) Transection")
                userinput= input("please respons by number.")
                if userinput=='1':
                    self.logout()
                    return
                if userinput=='2':
                    self.Transection(For_index)
                return
        print("ACCOUNT NUMBER AND PASSWORD DO NOT MATCH.")
        print("1)Please Enter valid pass and ac number.\n2)DO YOU WANT TO CREATE AN ACCOUNT?")
        USER=input("please respons '1' or '2':\n")
        if USER=='1':
            AA=input("Enter your AC number:")
            pp=input("Enter your password:")
            self.cheakingData(AA,pp)
        elif USER == '2':
            self.Create_AC()
        else:
            self.logout()


Bank = CREATE_AC_AND_CHECK()
print("\n\n       WELCOME TO RAFI PLC!\n\n")
print("DO YOU HAVE ANY BANK ACCOUNT IN THIS BANK? ('yes' or 'no')")
d = input().lower()

if d == 'yes':
    print("Enter your AC number:")
    A = input()
    print("Enter your password:")
    P = input()
    Bank.cheakingData(A, P)
elif d == 'no':
    print("DO YOU WANT TO CREATE AN ACCOUNT? ('yes' or 'no')")
    if input().lower() == 'yes':
        Bank.Create_AC()
    elif input().lower() == 'no':
        Bank.logout()