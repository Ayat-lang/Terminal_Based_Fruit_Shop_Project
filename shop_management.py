
import pyfiglet
from termcolor import colored
import csv

product = { }
csv_header = ["iteam" , "Price"]

def csv_file_read():
    csv_list = []
    with open ('admin_fruits.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file , delimiter='\t')
        
        next(csv_reader)
        for line in csv_reader:
            csv_list.append(line)


        for line in csv_list:
            vajal = str(line[0])
            xx = vajal.split(',')
            product[xx[0]] = xx[1]

        #blankline taken that is pop from the product
        csv_file.close()
               
def cse_file_write():  
    with open('admin_fruits.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        
        writer.writerow(csv_header)
        for row in product.items():
            writer.writerow(row)
    
    csvfile.close()

def csv_file_customer_write( name, email , total_cost ):
    with open('customer_write.csv', "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, str(total_cost)])
    csvfile.close()

def admin_menu():
    print(colored("Iteam adding in the list select 1: ","green").rjust(100))
    print(colored("Iteam delete in the list select 2: ","green").rjust(100))
    print(colored("Iteam Update price the list select 3: ","green").rjust(100))

def admin( usrname, password):
    if( usrname == "Fruit" and password == "123456789"):
        print()
        print(colored("Administrative Option : ","red").rjust(100))
        admin_menu()
        
        while(True):
            admin_input = input(colored("Select your choose : ","red").rjust(100)) 
            match admin_input:
                 case '1':
                    iteam_name =  input(colored("Enter new Iteam name : ","red").rjust(100)) 
                    iteam_price = input(colored("Enter new iteam price : ","red").rjust(100)) 
                    product[iteam_name] = int(iteam_price)
                 case '2':
                    iteam_name = input(colored("Enter delete Iteam name: ","red").rjust(100))
                    product.pop(iteam_name)
                 case '3':
                    iteam_name = input(colored("Enter Iteam name which price change : ","red").rjust(100))
                    iteam_price = input(colored("Enter update price : ","red").rjust(100))
                    if iteam_name in product:
                        product[iteam_name] = int(iteam_price)
                    else:
                        print(colored("Change is not possible","red").rjust(100))
            
            option = input(colored("Do you exit from the admin panel : \"Yes\" or \"No\" : ","red").rjust(100))
            if option == "Yes" or option == "yes":
                break
            else:
                continue  

        print(colored("New product list :","red").rjust(100))     
        display_menu()  
        cse_file_write()
        return True
    else:
        print(colored("You are not unauthorize to access this folder","red").rjust(100))
        return False

def display_menu():
    keys = product.keys()
    i = 1
    for xx in keys:
        print( colored(f"{i}.{xx} price is : {product[xx]}".rjust(90), "green") )
        i = i+1

def banner():
    banner_grabing = colored(pyfiglet.figlet_format("Fruit Shop Management"),'blue').center(500)
    print(banner_grabing)

#customer part is start from here

def customer(name, email):
    keys = product.keys()
    key_len = len(keys)
    total_cost = 0

    product_number = {}

    i = 1
    for xx in keys:
        product_number[str(i)] = xx
        i = i+1

    customer_input = input(colored("Customer choice givern number : ","red").rjust(100)).split(" ")
    quantity =  input(colored("Customer givern quantity number : ","red").rjust(100)).split(" ")
    print()
    i = 0
    print(colored(f"----------------------Customer Order Menu----------------","yellow").rjust(100))
    for kk in customer_input:
        key = product_number[kk]
        total_cost = total_cost + (int(quantity[i])*int(product[key]))
        print(colored(f"{key} Iteam quantity is {quantity[i]} and total price = {int(quantity[i])*int(product[key])}","blue").rjust(100))
        i = i +1 

    print(colored(f"Total payment order = {total_cost}","yellow").rjust(100))
    

    csv_file_customer_write( name, email, total_cost)
    return True
    


#start Programme here 
banner()
csv_file_read()

print(colored("1...Administrator Login".rjust(100),"yellow").rjust(100))
print(colored("2..*******User*********".rjust(100),"yellow").rjust(100))

option = input(colored("selection to continue : ","red").rjust(100))

if( option == "1"):
    print(colored("product List : ".rjust(90),"blue"))
    display_menu()
    print()
    while(True):
        Admin_user = input(colored("User name     : ","blue").rjust(100))
        Admin_pass = input(colored("User password : ","blue").rjust(100))
        tk = admin(Admin_user , Admin_pass)
      
        if tk == True:
            break
        else:
            option = input(colored("Again Try yes or no","red").rjust(100))
            if option == "no":
                break
            else :
                continue


elif( option == "2"):
    print(colored("product List : ".rjust(100),"yellow"))
    display_menu()
    print()
    while(True):
        customer_name  =  input(colored("Customer name  : ","blue").rjust(100))
        customer_email =  input(colored("Customer email : ","blue").rjust(100))
        
        customer_up = customer(customer_name,customer_email)
       
        if customer_up == True:
            break











