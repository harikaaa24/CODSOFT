import random
import string

# Function to generate password
def generate_password(length):
    
    # Combine all character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# User input
length = int(input("Enter the desired password length: "))

# Generate and display password
password = generate_password(length)

print("\nGenerated Password:")
print(password)
