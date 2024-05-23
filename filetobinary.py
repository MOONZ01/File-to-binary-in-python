
print("""
\033[1;31m\033[1;37m


                                                                            
`8.`8888.      ,8'    .8.          8 888888888o.      ,o888888o.     8 8888 
 `8.`8888.    ,8'    .888.         8 8888    `88.    8888     `88.   8 8888 
  `8.`8888.  ,8'    :88888.        8 8888     `88 ,8 8888       `8.  8 8888 
   `8.`8888.,8'    . `88888.       8 8888     ,88 88 8888            8 8888 
    `8.`88888'    .8. `88888.      8 8888.   ,88' 88 8888            8 8888 
     `8. 8888    .8`8. `88888.     8 888888888P'  88 8888            8 8888 
      `8 8888   .8' `8. `88888.    8 8888`8b      88 8888   8888888  8 8888 
       8 8888  .8'   `8. `88888.   8 8888 `8b.    `8 8888       .8'  8 8888 
       8 8888 .888888888. `88888.  8 8888   `8b.     8888     ,88'   8 8888 
       8 8888.8'       `8. `88888. 8 8888     `88.    `8888888P'     8 8888 
       
\033[1;31m                                  Text file to Binary code by YARGI♛ 🐍 \033[1;31m\033[1;37m""")

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
