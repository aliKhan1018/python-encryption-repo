import sys
import string

def build_rot13_dict_v3():
    shift_dict = {}
    shift = 13
    alpha = string.ascii_lowercase

    for i in range(13):
        shifted_char = chr(ord(alpha[i]) + shift)
        shift_dict[alpha[i]] = shifted_char
    
    for i in range(13, 26):
        shifted_char = chr(ord(alpha[i]) - shift)
        shift_dict[alpha[i]] = shifted_char
    
    return shift_dict 


def build_rot13_dict_v2():
    shift_dict = {}
    shift = 13
    alpha_fhalf = []
    alpha_lhalf = []
    alpha = string.ascii_lowercase
    
    for i in range(13):
        alpha_fhalf.append(alpha[i])
    
    for i in range(13, 26):
        alpha_lhalf.append(alpha[i])
    
    for char in alpha_fhalf:
        shifted_char = chr(ord(char) + shift)
        shift_dict[char] = shifted_char
    
    for char in alpha_lhalf:
        shifted_char = chr(ord(char) - shift)
        shift_dict[char] = shifted_char

    # print(alpha_fhalf, alpha_lhalf)
    return shift_dict 
    

def build_rot13_dict_v1():
    shift_dict = {}
    shift = 13
    alpha_fhalf = ['a', 'b','c','d','e','f','g','h','i','j','k','l', 'm']
    alpha_lhalf = ['n', 'o','p','q','r','s','t','u','v','w','x','y', 'z']

    for char in alpha_fhalf:
        shifted_char = chr(ord(char) + shift)
        shift_dict[char] = shifted_char
    
    for char in alpha_lhalf:
        shifted_char = chr(ord(char) - shift)
        shift_dict[char] = shifted_char

    return shift_dict


def apply_rot13(text):
    '''
    Returns the rot13 ver. of the orignal text.
    '''
    d = build_rot13_dict_v3()
    encrypted_text = ''

    #loop over char
    for char in text: 
        #check if lowercase is in dict
        if char.lower() in d:
            #if char is upper
            if char.isupper():
                #lower it
                char = char.lower()
                #now append the rotated ver. of char
                encrypted_text += d[char].upper()
            #if char is lower
            elif char.islower():
                #just append
                encrypted_text += d[char]
        else:
            encrypted_text += char

    return encrypted_text


def main():

    args = sys.argv[1:]

    if args:
        i = args.index('-f') + 1
        file = args[i]
        with open(file, 'r') as f:
            text = f.read()
            name = f.name
        # print(args)

        # if the output file is given
        if '-o' in args:
            i = args.index('-o') + 1
            name = args[i]
            with open(name, 'w') as out:
                encrypted_text = apply_rot13(text)
                out.write(encrypted_text)
        # otherwise create a file with a same name + '_encrypted.txt'
        elif len(args) == 1:
            name = name.replace('.txt', '')
            with open(name + '_encrypted.txt', 'w') as out:
                encrypted_text = apply_rot13(text)
                out.write(encrypted_text) 
    else:
        print('file not provided or not supported')

    # Test for upper case
    # text = 'Once there'
    # e_text = apply_rot13(text)
    # print(e_text)


if __name__ == "__main__":
    main()



