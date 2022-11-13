import random
import string

def get_random_password() -> str:
    N = 8
    password_ = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, N)
    password_final = "".join(password_)
    return password_final

print(get_random_password())