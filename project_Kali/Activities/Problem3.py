Sample_text = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")

if Sample_text.startswith(prefix):
    print("The string starts with", prefix)
else:
    print("The string does not start with", prefix)
