# Função para inverter uma string
def inverter_string(s):
    resultado = ''
    for char in s:
        resultado = char + resultado
    return resultado

# Entrada da string
entrada = input("Digite uma string para inverter: ")

# Inverte a string
string_invertida = inverter_string(entrada)

# Exibe o resultado
print("String invertida:", string_invertida)
