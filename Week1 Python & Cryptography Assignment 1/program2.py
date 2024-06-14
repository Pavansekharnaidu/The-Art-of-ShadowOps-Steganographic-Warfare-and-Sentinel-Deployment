def func(choice,file_name,shift):
    ans = ""

    with open(file_name, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into words
            words = line.split()
            
            # Iterate through the words in the line
            for word in words:
                if choice == 1:
                    for c in word:
                        if(c.isupper()):
                            ans += chr((ord(c)+shift-65)%26 + 65)
                        else:
                            ans += chr((ord(c)+shift-97)%26 + 97)
    
                if choice == 2:
                    for c in word:
                        if(c.isupper()):
                            ans += chr((ord(c)-shift-65)%26 + 65)
                        else:
                            ans += chr((ord(c)-shift-97)%26 + 97)
                ans += " "
            ans += "\n"
            
    return ans
                           
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
    file_name = input("provide the filename : ")
    key = int(input("provide the key : "))
    crypted_text = func(choice,file_name,key)
    
    outputfile_name = "output.txt"
    with open(outputfile_name,'w') as output_file:
        output_file.write(crypted_text)
    
    print(f"Output saved to {outputfile_name}")
    
