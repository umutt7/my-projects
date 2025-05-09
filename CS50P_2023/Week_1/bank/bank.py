response = input("Greeting: ")

if response.lower().strip().startswith("hello"):
    print("$0")
elif response.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")