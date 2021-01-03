from data import Morse
from art import logo

morse = Morse()

print(logo)

while input('Do you wanna do this ? (y or n) :') == 'y':
    morse.ops()
    option = input('Which operation do you wish to perform ? :')
    if option =='a':
        morse.print_key()

    elif option =='b':
        plaintext = input('Enter some text please : ').upper()
        answer = morse.encode_process(plaintext)
        print(answer)        

    elif option == 'c':
        encoded = input('Enter some text please : ').upper().split(' ')    
        answer = morse.decode_process(encoded)
        print(answer)

    else:
        print('Illegal Option')

print('Thank you come again')