from collections import defaultdict
import re
import string


def count_words(sentence):
    new_dict = defaultdict(int)
    clean = ""
    words = []

    for char in '_-.,\n:!&@$%^&':
        sentence = sentence.replace(char, ' ')

##    cleaner = re.findall(r'\w+', sentence.lower())
##
##    cleanest = [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in sentence.split()]
##    for i in cleanest:
##        new_dict[i] += 1        
                
    # for word in sentence.lower(): ##Creates new clean string replacing characters that are not alphanumeric
    #     if word.isalnum() == False and word != "'":
    #         word = " "
    #         clean += word
    #     clean += word
    # clean = clean.split() ##Erases all spaces

    # for i in clean:
    #     if i.startswith("'") and i.endswith("'"):
    #         i = i.strip("'")
    #     new_dict[i] += 1

    # return dict(new_dict)
    print(sentence)
    return sentence

count_words("Joe can't tell between 'large' and large.")
