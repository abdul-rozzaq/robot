

def set_token(name):    
    with open(f'tokens/{name}.txt', 'w') as file:
        file.write(input('Token >> ').strip())

