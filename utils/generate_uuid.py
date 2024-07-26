import random
import string

def custom_id(length):
    random_segment = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    return random_segment

def generate_uuid():
    return f"VOGEO-3010-{custom_id(5)}-8246{custom_id(3)}-{custom_id(10)}-{custom_id(5)}"