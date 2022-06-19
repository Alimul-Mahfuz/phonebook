import json
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


def PrintJson():
    with open('./pythonProject/PhoneBook/data.json','w') as fobj:
        json.dump(PhoneBook[0].details,fobj,indent=4)


def SearchContact():
    found=False
    index=0
    phone=input("Enter Phone number to search")
    for x in PhoneBook:
        index=index+1
        if phone in x.details['phonelist']:
            print("Number found")
            found=True
            print("Details of the Person")
            print("Name: {}".format(x.details['name']))
            print("Address: {}".format(x.details['address']))
            print("Email: {}".format(x.details['email']))
            ch=input("Want to update the persons's details y/n: ")
            if(ch=='y' or ch=='Y'):
                UpdateDetails(index)
            if(ch=='n' or ch=='N'):
                print('Okay Thanks you')
            pass
    if(found==False):
        print("Number doesn't exists")


def DeleteContact():
    sl=int(input("Enter the sl to delete: "))
    sl=sl-1
    if(int(sl) not in range(0,COUNTENTITY)):
        print("SL not exist")
        pass
    del(PhoneBook[sl])
    print("Contact Deleted Successfully")


def Print():
    fname="./pythonProject/PhoneBook/data.txt"
    with open(fname,'w') as file_obj:
        for i in range(len(PhoneBook)):
            file_obj.write('\n')
            file_obj.writelines('\n#SL{}----------------------'.format(i+1))
            file_obj.writelines("\nName: {}".format(PhoneBook[i].details['name']))
            file_obj.writelines("\nAddress: {}".format(PhoneBook[i].details['address']))
            file_obj.writelines("\nEmail: {}".format(PhoneBook[i].details['email']))
            file_obj.writelines("\nPhone numbers: {}".format(PhoneBook[i].details['phonelist']))
    
        


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
        # if(int(ch) in range(1,1000)):
        #     UpdateDetails(int(ch))
        if(ch=='q'):
            a=PrintPromt()
        else:
            UpdateDetails(int(ch))
            a=PrintPromt()
    elif int(a)==4:
        SearchContact()
        a=PrintPromt()

    elif int(a)==5:
        DeleteContact()
        a=PrintPromt()
    elif int(a)==6:
        Print()
        a=PrintPromt()








        






