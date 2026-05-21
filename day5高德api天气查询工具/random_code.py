import string
import random
def random_code():
    c=string.digits+string.ascii_uppercase
    return ''.join([random.choice(c) for i in range(6)])