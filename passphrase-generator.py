import string
import random

def passphrase_generator(size = 12, alphabet = string.ascii_letters + string.digits):
    while True:
        password = ''.join(random.choice(alphabet) for _ in range(size))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password)>= 3):
            break
    return password

print(passphrase_generator())