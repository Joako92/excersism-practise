import random
import string

password = ''.join(random.choice(string.digits) for i in range(8))
print("Random password is:", password)
