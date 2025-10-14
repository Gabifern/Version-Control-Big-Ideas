currentYear = 2025
# It takes a name input
name = input("Enter your name: ")
while(True):    
    # It takes some other input
    age = input("Enter your age: ")

    # Attempts to take age input and convert to int
    try:
      age = int(age)
      print(name, "was born in", currentYear - age);
      break
    except:
      print("\"", age, "\" is not an integer!")
