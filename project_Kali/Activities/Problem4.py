Sample_text = input("Enter a string: ")
suffix = input("Enter a suffix to check: ")

if Sample_text.endswith(suffix):
    print("The string ends with",suffix)
else:
    print("The string doesn't ends with", suffix)