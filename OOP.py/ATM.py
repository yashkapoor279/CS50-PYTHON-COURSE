 # __init__ is a constructor jinke andr ka code automatically call hoga asa class call hogi


class Atm:

    #static variable
    counter = 1



    def __init__(self):  # special function in which all the attributes will be written
        # print("Hello")
        #creating data members
        self.__pin = ""  # variable creation
        self.__balance = 0
        #this creates a variable named _Atm__pin inside compiler

        self.sno=Atm.counter #accessing static variable
        Atm.counter=Atm.counter+1

        print(id(self))
        
        


        self.__menu()
 # __init__ is a constructor jinke andr ka code automatically call hoga asa class call hogi
     


     #getter and setter
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("Pin changed")

# sbi=Atm()  #object made -> constructor called -> output printed
    

    #menu function
    def __menu(self):
            user_input = input(
                """
            Hello! How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
                       
                       """
            )

            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.checkbal()
            else:
                print("bye")
    def create_pin(self):
         self.__pin = input("Enter your pin")
         print("Pin created successfully")
    def deposit(self):
         temp = input("enter your pin")
         if(temp==self.__pin):
           amount=int(input("Enter your deposit amount"))
           self.__balance=self.__balance+amount
           print("Deposit successful")
         else:
             print("Invalid pin")
    def withdraw(self):
        temp = input("enter your pin")
        if(temp==self.__pin):
            amount=int(input("Enter the withdrawal amount"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Operation successful")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
    def checkbal(self):
        temp = input("enter your balance pin")
        if(temp==self.__pin):
            print(self.__balance)
        else:
            print("invalid pin")


    
sbi = Atm()  #object of a class called 
# print(id(sbi))
# hdfc = Atm()
# print(id(hdfc))

# sbi._Atm__balance="djs"  This will not run
sbi.get_pin()
sbi.set_pin("1234") #now even if you create your own pin , 1234 will be the new pin
sbi.deposit()
sbi.withdraw()
sbi.checkbal()
sbi.__balance="afdfa" #this will still run
#nothing in python is truly private




#self -> jis object k sath aap currently kaam kr rhe ho toh vhi self hoga 
#ex : if working with sbi or hdfc or any other obhect
#id(self=id(sbi)




 






