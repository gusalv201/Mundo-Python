# Aula 18 A função Print


print(12, 34) # Recebe argumento, caso mais de 1 usar vírgula
# Por padrão ela coloca espaço entre vírgulas
# Para duplicar uma linha usar CTRL+C E CTRL +V
print(12, 34) # Argumentos não nomeados
print(12,34,sep="João") #sep define o separador

# Por padrão o print possui o end=\n e sempre quebra linha
#Cada sistema tem um tipo de quebra de linha , no Windows é o CRLF 
#CRLF significa "Carriage Return/Line Feed", e refere-se aos caracteres de controle 
# usados para indicar o final de uma linha em arquivos de texto, 
# especialmente em sistemas operacionais como o Windows
print(12, 10, end='\n') # Quebra a linha ou pode colocar quebra e outro caracter
print(12,10, end="\n##")


# O python diferencia letras maiúsculas e minúsculas(Case Sensitive)
# Print(12,10) está errado

