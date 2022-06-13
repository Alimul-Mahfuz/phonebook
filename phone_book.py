
COUNTENTITY=0
a=0
PhoneBook=[]

#Person template
class Person:
    def __init__(self,name,address,email,phone):
        self.details={}
        self.details['name']=name
        self.details['address']=address
        self.details['email']=email
        #Phone is an set that's reference is recorded on details dictonary
        self.details['phonelist']=phone

#Gives instruction what the user need to at the beginig of the program
def PrintPromt():
    print('\n')
    print("==============WELCOME TO PYPHONEBOOK==============")
    print("1. View phone numbers")
    print("2. Add a new number")
    print("3. Update exixting contact number")
    print("4. Search")
    print("5. Delete contact")
    print("6. Print your contact book")
    a=input("Enter your choice or press q to exit:  ")
    return a

def AddNewContact():
    global COUNTENTITY
    Name=input('Enter contact name: ')    
    Address=input('Enter address: ')    
    Email=input('Email: ') 
    #Set is used to avoid duplicate phone number entries
    Number=set()
    Number.add(input('Contact number: ')) 
    #Asking for multiple phone number save
    mulnum=input("Do you want to save more than one number 'y/n': ") 
    while (mulnum=='y' or mulnum =='Y'):
        Number.add(input("Enter other contact number:"))
        mulnum=input("Do you want to save more number 'y/n': ")
        if mulnum=='n' or mulnum=='N':
            break
    myObj=Person(Name,Address,Email,Number)
    PhoneBook.append(myObj)
    COUNTENTITY=COUNTENTITY+1


#The following function will update the existing value 
def UpdateDetails(sl):
    sl=sl-1
    if(int(sl) not in range(0,COUNTENTITY)):
        print("SL not exist")
        pass
    else:
        print("1. Update Name: ")
        print("2. Update Address: ")
        print("3. Update Email: ")
        print("4. Update Phone number: ")
        print("5. q to exit ")
        exit=input("Enter choice: ")
        if(exit=='q'):
            pass
        elif(int(exit)==1):
            PhoneBook[sl].details['name']=input("Enter new Name: ")
            pass
        elif(int(exit)==2):
            PhoneBook[sl].details['address']=input("Enter new Address: ")
            pass
        elif(int(exit)==3):
            PhoneBook[sl].details['email']=input("Enter new Email: ")
            pass
        elif(int(exit)==4):
            #View the existing phone number before modifying it
            print("Available Phone number")
            for x in PhoneBook[sl].details['phonelist']:
                print(x)
            print("1. Delete a number")
            print("2. Add a new number")
            ch=input("Enter choice: ")
            if(int(ch)==1):
                num=print("Type the full number to delete:")
                PhoneBook[sl].details['phonelist'].discard(num)
            elif(int(ch)==2):
                PhoneBook[sl].details['phonelist'].add(input("Enter new number:"))
                


#Display the available list of contact form PhoneBook Dictionary
def PrintDetails():
    for i in range(len(PhoneBook)):
        print('\n')
        print('#SL{}----------------------'.format(i+1))
        print("Name: {}".format(PhoneBook[i].details['name']))
        print("Address: {}".format(PhoneBook[i].details['address']))
        print("Email: {}".format(PhoneBook[i].details['email']))
        print("Phone numbers: {}".format(PhoneBook[i].details['phonelist']))

a=PrintPromt()

while(a!='q'):
        
#View all the saved contacts
    if int(a)==1:
        if(len(PhoneBook)==0):
            print("Contact List is empty")
        else:
            PrintDetails()       
        a=PrintPromt()

    #Adding a new contact
    elif int(a)==2:
        AddNewContact()
        a=PrintPromt()
    #Update existing contact details
    elif int(a)==3:
        ch=input("Enter sl to update or q to quit: ")
        if(int(ch) in range(1,1000)):
            UpdateDetails(int(ch))
        elif(ch=='q'):
            a=PrintPromt()
        else:
            a=PrintPromt()


        






