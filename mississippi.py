def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def format_output(char_count):
    formatted_output = ""
    for char, count in char_count.items():
        formatted_output += f"{char}={count:02d}, "
    formatted_output = formatted_output[:-2]  # Remove the trailing comma and space
    return formatted_output

input_string = input("Please enter a string: ")
char_count = count_characters(input_string)
output = format_output(char_count)

print(output)
