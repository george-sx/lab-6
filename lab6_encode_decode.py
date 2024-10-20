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

def decode(password):
    '''
    Decodes the encoded password by shifting each digit back by 3.
    '''
    decoded_password = ""
    for digit in password:
        decoded_password = decoded_password + str((int(digit) - 3) % 10)
    return decoded_password
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
            try:
                decoded_password = decode(password)
                print(f"The encoded password is {password}, and the original password is {decoded_password}.")
            except:
                print("No password has been encoded yet.")
        elif input_option == "3": # Quit
            break
        else: # Invalid option
            print("Invalid option.")
            continue
        
        print()
        
if __name__ == '__main__':
    main()