# Aula 22
# conversão de tipo, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print('a' + 'b')

# Uma vez criado um tipo não consegue alterar ele (imutáveis)

# A class int converte um tipo
print(int('1'), type(int('1'))) # Convertido para int
print(float('1') + 1) # COnvertido para float
print(bool('')) # string vazia é False
print(bool(' ')) # string com espaço é True
print(str(11) + 'b') # Coerção de duas strings

      