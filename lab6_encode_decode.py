# George

def encode(password):
    '''
    Encodes a numerical password by shifting each digit by 3.
    '''
    encoded_password = ""
    
    for digit in password:
        encoded_password = encoded_password + str(int(digit) + 3)[-1]
    
    print("Your password has been encoded and stored!")
    
    return encoded_password
    
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")  
        print("3. Quit")
        
        input_option = input("\nPlease enter an option: ")
        
        if input_option == "1": # Encode
            password = encode(input("Please enter your password to encode: "))
        elif input_option == "2": # Decode
            pass
        elif input_option == "3": # Quit
            break
        else: # Invalid option
            print("Invalid option.")
            continue
        
        print()
        
if __name__ == '__main__':
    main()