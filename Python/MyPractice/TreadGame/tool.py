def save_code(code):
    with open('code.txt','w') as file:
        file.write(code)

def clear_code():
    with open('code.txt','w') as file:
        pass

def read_code():
    with open('code.txt') as file:
        return file.read()