def count_file(filename):
    characters = 0
    words = 0
    lines = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                lines += 1
                characters += len(line)
                words += len(line.split())

        print("Number of characters:", characters)
        print("Number of words:", words)
        print("Number of lines:", lines)

    except FileNotFoundError:
        print("File not found.")


filename = input("Enter the filename: ")
count_file(filename)
