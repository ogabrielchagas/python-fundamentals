import stack_api

stack = stack_api.init_stack()

# Teste 1: Pilha vazia
print(stack_api.stack_is_empty(stack))  # Esperado: True

# Teste 2: Adicionar elementos
print(stack_api.push(stack, 10))  # Esperado: Elemento adicionado: 10
print(stack_api.push(stack, 20))  # Esperado: Elemento adicionado: 20
print(stack_api.push(stack, 30))  # Esperado: Elemento adicionado: 30
stack_api.print_stack(stack)  # Esperado: [10, 20, 30]

# Teste 3: Ver o elemento no topo
print(stack_api.peek(stack))  # Esperado: 30

# Teste 4: Remover elementos
print(stack_api.pop(stack))  # Esperado: Elemento removido: 30
print(stack_api.pop(stack))  # Esperado: Elemento removido: 20
stack_api.print_stack(stack)  # Esperado: [10]

# Teste 5: Verificar se está vazia após remover tudo
print(stack_api.pop(stack))  # Esperado: Elemento removido: 10
print(stack_api.pop(stack))  # Esperado: Stack is empty
print(stack_api.stack_is_empty(stack))  # Esperado: True