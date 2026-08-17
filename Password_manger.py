import pyperclip
import os

FILE_NAME="passwords.txt"

def save_password():
    website=input("enter the website:")
    password=input("enter the password:")
    with open (FILE_NAME,"a") as f:
        f.write (f"{website}:{password}\n")

def get_password():
    website=input("enter the website:")
    with open (FILE_NAME,"r") as f:
        for line in f:
            if website in line:
                password=line.strip().split(":")[1]
                pyperclip.copy(password)
                print("password copied to cliboard")
                break
            else:
                print("website not found")
            
def main():
    while True:
        print("1.save password")
        print("2.get password")
        print("3.exit")
        choice=input("enter your choice:")

        if choice=="1":
            save_password()
        elif choice=="2":
            get_password()
        elif choice=="3":
            print("exiting...")
            break
        else:
            print("invalid choice,plase try again")
            
        
            

main()

# python .\Password_manger.py