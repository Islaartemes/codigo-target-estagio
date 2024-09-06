def is_fibonacci_number(n):
    # Função para verificar se um número pertence à sequência de Fibonacci
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Solicitando o número do usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci_number(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")