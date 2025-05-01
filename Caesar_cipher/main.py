from encryption import Encrypt_data
from decryption import Decrypt_data

def main():
    print("Welcome to Caesar Cipher!!")
    while True:
        try:
            user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt or ctrl+c to exit: ").lower()
            if user_choice == "encode":
                
                Encrypt_data()
            elif user_choice == "decode":
                Decrypt_data()
            else:
                print('Please choose "Encode" or "Decode" to Encrypt and Decrypt the data.')         
                
        except (Exception, ValueError) as e:
            print(f"An error occurred: {e}")
        except (KeyboardInterrupt):
            print("Exiting from Caesar Cipher")
            break

     
if __name__ == "__main__":
    main()
