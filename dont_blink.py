"""
I highly recommend to use the terminal to see the magic.

"""
import time

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C',
         'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7',
         '8', '9']


def magic():
    name = input('Type your name : ')
    new_name = ''

    for i in name:
        # if the character not in alpha list then we simply print it.
        if i not in alpha:
            new_name += i
        for j in alpha:
            if name == new_name:
                print(new_name)
                break
            else:
                print(new_name + j, end='\r')  # '\r' makes it in one line
                time.sleep(0.01)  # play with time
                if i == j:
                    new_name += i


if __name__ == '__main__':
    magic()
    input('press any key to continue! ->')
   