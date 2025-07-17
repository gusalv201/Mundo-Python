# Aula 31 F-strings Formatação de strings

nome = 'Gustavo Alves'
altura = 1.77
peso = 95
imc = peso / altura ** 2

linha_1 = f'Nome tem {altura:.2f} de altura' # Colocar o f permite usar variáveis dentro do texto com chaves
# Se colocar depois da variável :.2f limita a duas casas decimais a variável
linha_2 = f'Pesa {peso} quilos e seu imc é {imc:.2f}'
print(linha_1, linha_2)