import validators

# Check if the input is a valid email address
response = validators.email(input("What's your email address? "))

# Print the result
if response == True:
    print("Valid")
else:
    print("Invalid")