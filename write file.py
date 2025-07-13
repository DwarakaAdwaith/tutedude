
user_input = input("Enter some data to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")


additional_input = input("Enter additional data to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")


print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
