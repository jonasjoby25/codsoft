import random

print("Password Generator")

length = int(input("Enter password length: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password:", password)