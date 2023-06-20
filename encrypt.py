#this program uses a recursive function to encrypt a message by converting all lowercase characters to the next character
#Busisiwe Michelle Ndlovu
#24/4/2023

def encrypt(message):
    """ function that encrypts a message by converting all lowercase characters to the next character"""
    #base case for paramter of no length
    if len(message) == 0:
        return ""
    else:
        #accomodates for special case where z becomes a
        if message[0] == "z":
            return("a"+encrypt(message[1:])) 
        #encrypts lower case alphabetical values
        elif not ord(message[0]) < ord("a") and not ord(message[0]) > ord("y"):
                return chr(ord(message[0])+1) + encrypt(message[1:])  
        else:
            #continues itertaing throughout the text if values aernt lower case and alphabetical through recursion
            return message[0] + encrypt(message[1:])
    
    
def main():
    #main function to take user input
    message = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(message))
    
if __name__ == "__main__":
    main()