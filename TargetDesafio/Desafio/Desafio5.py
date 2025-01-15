# String previamente definida
string_original = "Teste de qualquer string so pra ver"

# Função para inverter os caracteres da string
def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Chama a função e imprime a string invertida
string_invertida = inverter_string(string_original)
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
