letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Caeser Cipher!")
playAgain = "yes"

while(playAgain == 'yes' and playAgain != 'no'):
    print("Type \'encode\' to encrypt the message, and \'decode\' to decrypt.")
    status = input()
    while(status != 'encode' and status != 'decode'):
        print("Input invalid. Type \'encode\' to encrypt the message, and \'decode\' to decrypt.")
    print("Type your message: ")
    message = input()
    print("Type the shift number: ")
    shift = int(input())
    translated = ''
    if(status == 'encode'):
        for i in message:
            count = 0
            for x in range(len(letters)):
                count+=1
                if(i == letters[x]):
                    translated += letters[(x+shift)%26]
                    count -= 1
                    break
            if(count == 26):
                translated += i
        print("Here's the encoded message: " + translated)
    else:
        for i in message:
            count = 0
            for x in range(len(letters)):
                count += 1
                if(i == letters[x]):
                    count -= 1
                    translated += letters[(x + 26 - shift)%26]
                    break
            if(count == 26):
                translated += i
        print("Here's the decoded message: " + translated)
    
    translated = ''
    playAgain = input("Type \'yes\' to play again, \'no\' to exit: ")
    while(playAgain != 'yes' and playAgain != 'no'):
        print("Input invalid. Type \'yes\' if you want to play again. Otherwise type \'no\'.")
