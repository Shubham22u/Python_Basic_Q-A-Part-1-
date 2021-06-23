import string

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True

#string = 'the quick brown fox jumps over the lazy dog'
string = input("Enter String : " + str())
if (ispangram(string) == True):
    print("Yes it is Pangram")
else:
    print("No")

#######################################################################################################
print("********Alternative Method**********")
######################################################################################################
import string

alphabet = set(string.ascii_lowercase)
def ispangram(string):
    return set(string.lower()) >= alphabet

string = "The quick brown fox jumps over the lazy dog"
if (ispangram(string) == True):
    print("Yes")
else:
    print("No")
