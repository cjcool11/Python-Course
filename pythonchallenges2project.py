import random
def generate_random_password(length): 
    lower_case = "abcdefghijklmnopqrstuvwxyz" 
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    digits = "0123456789" 

    all_characters = lower_case + upper_case + digits 
    password = ''.join(random.choice(all_characters)
                        
    for _ in range(length)) 
    return password 

password_length = 12 
random_password = generate_random_password(password_length) 
print("Generated password:", random_password)