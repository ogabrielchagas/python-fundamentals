def init_stack():
    stack = []
    return stack

def stack_size(stack):
    return len(stack)

def push(stack, elem):
    stack += [elem]
    return f'Elemento adicionado: {elem}'

def pop(stack):
    if stack_is_empty(stack) == False:
        last_elem = stack[stack_size(stack) - 1]
        del stack[stack_size(stack) - 1]
        return f'Elemento removido: {last_elem}'
    else:
        return 'Stack is empty'

def peek(stack):
    if stack_is_empty(stack) == False:
        print(stack[stack_size(stack) - 1])
        return stack[stack_size(stack) - 1]
    else:
        return 'Stack is empty'
    
def print_stack(stack):
    if stack_is_empty(stack) == False:
        print(stack)
    else:
        return 'Stack is empty'

def stack_is_empty(stack):
    if stack_size(stack) == 0:
        return True
    else:
        return False




