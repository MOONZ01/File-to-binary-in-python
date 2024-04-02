


import colorama





print("""
\033[1;31m\033[1;37m
██╗░░░██╗░█████╗░██████╗░░██████╗░██╗
╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝░██║
░╚████╔╝░███████║██████╔╝██║░░██╗░██║
░░╚██╔╝░░██╔══██║██╔══██╗██║░░╚██╗██║
░░░██║░░░██║░░██║██║░░██║╚██████╔╝██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝
\033[1;31m                                    Binary code♛ \033[1;31m\033[1;37m""")

def file_to_binary(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        binary_data = ''.join(format(ord(char), '08b') for char in text)
        return binary_data
    except FileNotFoundError:
        print(f"The '{file_path}' was not found")
    except Exception as e:
        print(f"Error: {e}")
file_path = input("Enter the path to the text file: ")
binary_data = file_to_binary(file_path)
if binary_data:
    print("Binary code:")
    print(binary_data)
