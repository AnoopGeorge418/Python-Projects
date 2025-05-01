import string

ALPHABETS = string.ascii_letters

def Encrypt_data():
    try:
        message = input("Type your message to encrypt: ").lower()
        shift = int(input("Enter the shift number: "))
        
        cipher_text = ""
        for letter in message:
            shifted_position = ALPHABETS.index(letter) + shift
            
            shifted_position %= len(ALPHABETS)
            cipher_text += ALPHABETS[shifted_position]
        
        print(f"Your encoded result is '{cipher_text}'")
            
    
    except Exception as e:
        print(f"Please make sure proper data: {e}")
