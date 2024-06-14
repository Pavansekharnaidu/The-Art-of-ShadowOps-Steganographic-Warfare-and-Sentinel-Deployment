def func(choice,text,shift):
    ans = ""
    
    if choice == 1:
        for c in text:
            if(c.isupper()):
                ans += chr((ord(c)+shift-65)%26 + 65)
            else:
                ans += chr((ord(c)+shift-97)%26 + 97)
    
    if choice == 2:
        for c in text:
            if(c.isupper()):
                ans += chr((ord(c)-shift-65)%26 + 65)
            else:
                ans += chr((ord(c)-shift-97)%26 + 97)
    
    print(ans)
                
if __name__ == "__main__":
    number = input("Choose between encryption and decryption: \nIf you want to choose encryption, press 1, else press 2: ")
    if number == '1':
        print("Hello, you chose encryption!")
    elif number == '2':
        print("Hello, you chose decryption!")
    else:
        print("Invalid choice. Run again")
        exit(0)

    choice = int(number)
    text = input("provide the text : ")
    key = int(input("provide the key : "))
    func(choice,text,key)
    
