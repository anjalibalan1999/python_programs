import random

# Step 1: User Registration
users = {
    "john_doe": "password123",
    "jane_doe": "password456"
}

def register_user(username, password):
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        print(f"User {username} registered successfully!")

# Step 2: OTP Generation
def generate_otp():
    return random.randint(1000, 9999)

# Step 3: Login Logic with OTP Verification
def login_user(username, password):
    if username in users and users[username] == password:
        print("Password verified.")
        otp = generate_otp()
        print(f"Your OTP is: {otp}")  # Simulating OTP being sent to the user
        entered_otp = int(input("Enter the OTP: "))
        if entered_otp == otp:
            print("Login successful!")
        else:
            print("Incorrect OTP. Login failed.")
    else:
        print("Invalid username or password.")

# Testing the system
while True:
    choice = input("enter login or register or exit :")
    if choice.lower() == "register":
        register_user(input("enter username:"), input("enter password:"))
    elif choice.lower() == "login":
        login_user(input("enter your username for login:"), input("enter your password for login"))
    elif choice.lower() == "exit":
        break


 