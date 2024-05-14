import random, string

def create_random_password(password_length):
    available_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(available_characters) for _ in range(password_length))
    return generated_password

def run_password_generator():
    try:
        desired_length = int(input("Enter the desired length of the password: "))
        if desired_length < 1:
            raise ValueError("Password length must be at least 1")
        new_password = create_random_password(desired_length)
        print("System Generated Password:", new_password)
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    run_password_generator()
