Database=[]
print()
print("welcome to COVID help provider \nAn ULTIMATE helper for people suffering form covid issues")
 


while True:
    
    print()
    print("How can we help \nChoose 1 if you want to donate \nChoose 2 if u Need Help")
    choose = int(input('Enter no. : '))

    

    def Donar():
        
        temp = []
        name = input("Enter your Name : ")
        print()
        address = input("Enter your complete and precise location : ")
        print()
        city = input("Enter your city : ")
        print()
        contact = int(input("Enter your contact : "))
        print()
        print("What u want to donate \nEnter 1 for food \nEnter 2 for madical accessories \nEnter 3 for oxygen")
        print()
        thing = int(input("Enter a no. : "))

        temp.append(name.upper())
        temp.append(address.upper())
        temp.append(city.upper())
        temp.append(contact)


        if thing == 1 :
            temp.append("Food")
        elif thing == 2:
            temp.append("Medical accessories")
        elif thing == 3:
            temp.append("oxygen")

        Database.append(temp)
        #print(Database)
        print()
        return print("Data added succesfully")
        
        
                    

    def reciver():
        print("How can we help u \nEnter 1 for food \nEnter 2 for madical accessories \nEnter 3 for oxygen")
        print()
        no = int(input("Enter a no. : "))
        print()
        print("We Need your City name for more service") 
        c = input("Enter your city name : ")
        city = c.upper()
        
        if no == 1 :
            t = "Food"
        elif no == 2:
            t = "Medical accessories"
        elif no == 3:
            t = "oxygen"

        if len(Database) == 0:
            print("we Do not have any donner yet \n sorry for this " )
        else:
            i=0
            
            #print(city)
            
            while i < len(Database):
                d = Database[i]
                if d[2] == city:
                    if d[4] == t:
                        print()
                        print("This might help you ")
                        print()
                        print("Format : { Name , Adddress , City , Contact no. , item for donstion } Of Donar")
                        i+=1
                        break
                    else:
                        print()
                        print("Sorry no donor available for your requirement")
                        i+=1
                        break

                else:
                    print()
                    print("Sorry no donor available for your Location")
                    i+=1
                    break
                
                    
    if choose == 1:
        print()
        print("we need some of the details \nPlease enter everything in capital")
        Donar()
        print()
        print("Enter 1 to continue \nEnter 2 to exit")
        exit = int(input("Enter a no. : "))
        if exit == 1:
            continue
        else:
            break
    else:
        print()
        reciver()
        print()
        print("If u want we can check for near by cities or other Help \nEnter 1 for Yes \nEnter 2 for No")
        changeC = int(input())
        if changeC == 1:
            reciver()
        else:
            break
print()

print("Thanks for using our app")