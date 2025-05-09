name = input("File name: ")
name = name.strip().lower()

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg") | name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")