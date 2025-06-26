
def mirror_pattern(N, special_char):
    # Generating the pattern
    pattern = []
    for i in range(N):
        row = special_char * (i + 1)
        pattern.append(row)
    
    # Generating mirror reflection
    mirror = [' ' * (N - i - 1) + row[::-1] for i, row in enumerate(pattern)]
    
    # Creating the horizontal surface line
    horizontal_line = "-" * (2 * N + 1)
    
    # Combining pattern, horizontal line, and mirror reflection
    combined = [p + "\n" + horizontal_line + "\n" + m for p, m in zip(pattern, mirror)]
    
    # Joining all rows into a single string
    result = "\n".join(combined)
    return result

# Taking input for the number of rows and the special character
N = int(input("Enter the number of rows: "))
special_char = input("Enter the special character: ")

# Generating and printing the mirror pattern
print(mirror_pattern(N, special_char))
