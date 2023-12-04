alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sentence = input("Insert pangram here: ")

def is_pangram(sentence):

    sentence2 = list(sentence.lower())
    for x in alphabet:
        if not x in sentence2:
            return False
    return True

is_pangram(sentence)

if is_pangram(sentence) == True:
    print("Your sentence is a pangram")
else:
    print("Your sentence is not a pangram")