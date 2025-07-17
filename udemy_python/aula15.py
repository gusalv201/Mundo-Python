# Aula 33 Função Input para coletar dados do usuário

# input('Qual o seu nome? ') # No caso não da erro, mas também não finaliza o programa, tem que apertar enter
# O input SEMPRE armazena com STRING, tem que fazer a coerção se quiser algum outro tipo
# Se passar o nome na variável ele já mostra a STR
# nome = input('Qual o seu nome? ')
# print()


#numero_1 = input('Digite um número: ')
#numero_2 = input('Digite outro número: ')

#print(f'A soma dos números é: {numero_1}+{numero_2}') # No caso vai concatenar, pois não tipei a STR
#A maneira certa
numero_1 = int(input('Digite um número: ')) #Embora possa colocar como converte no início não permite ao
#desenvolvedor ver o que foi digitado
numero_2 = int(input('Digite outro número: ')) # Não é a melhor maneira, pois já 'quebra' o programa
# int_numero_1 = int(numero_1) # A melhor maneira, pois continua o programa em caso de erro
# int_numero_2 = int(numero_2)
print(f'A soma dos números é:{numero_1 + numero_2}') 
# 