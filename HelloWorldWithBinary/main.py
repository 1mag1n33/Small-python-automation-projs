import sys

def letters_to_binary(message):
    binary_result = ' '.join(f'{char}:{format(ord(char), "08b")}' for char in message)
    return binary_result

def binary_to_letters(binary_string):
    binary_pairs = binary_string.split(' ')
    text_result = ' '.join(pair.split(':')[0] for pair in binary_pairs)
    return text_result

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py [-let <message>] [-bin <binary>]")
        return

    operation = sys.argv[1]
    message = sys.argv[2]

    if operation == '-bin':
        binary_representation = letters_to_binary(message)
        print("Binary representation:", binary_representation)
    elif operation == '-let':
        text_representation = binary_to_letters(message)
        print("Text representation:", text_representation)
    else:
        print("Invalid operation. Use -bin or -let.")

if __name__ == "__main__":
    main()
