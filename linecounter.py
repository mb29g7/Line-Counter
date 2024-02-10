# Read input directly within the program
user_input = """hello
world
thats
crazy

drums"""

# Function to count lines in an input string
def count_lines(input_string):
    lines = input_string.split("\n")
    return len(lines)

# Call the function to count lines
line_count = count_lines(user_input)

# Print the result
print(f"This input contains {line_count} lines.")


# Read all lines from a file and count them
with open("C:/Users/splas/Downloads/(name goes here).txt", 'r') as fp:      #this is the path, needs user edit based on file
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

