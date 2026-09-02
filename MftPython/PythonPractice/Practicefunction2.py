# This is another function practice 

'''def is_valid_port(port):
    if 1 <= port <= 65535:
        return True
    else:
        return False
# we need to call the function now with below input

print(is_valid_port(8000))
print(is_valid_port(70000))'''

def is_valid_port(port):
    return 1 <= port <= 65535

print(is_valid_port(8000))
print(is_valid_port(70000))