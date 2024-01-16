import sys

def int_to_binary(num):
    return bin(num).replace("0b", "")

def binary_to_decimal(binary_str):
    if '.' in binary_str:
        int_part, frac_part = binary_str.split('.')
        int_value = int(int_part, 2)
        frac_value = sum(int(bit) * 2**(-i-1) for i, bit in enumerate(frac_part))
        return int_value + frac_value
    else:
        return int(binary_str, 2)

def main():
    if len(sys.argv) == 3:
        option = sys.argv[1].lower()
        value = sys.argv[2]

        try:
            if option == "-int":
                result = int_to_binary(int(value))
                print(f"Binary representation: {result}")
            elif option == "-bin":
                result = binary_to_decimal(value)
                print(f"Decimal representation: {result}")
            else:
                print("Invalid option. Use '-int' to convert to binary or '-bin' to convert to decimal.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Usage: python main.py [-int <integer>] [-bin <binary>]")

if __name__ == "__main__":
    main()
