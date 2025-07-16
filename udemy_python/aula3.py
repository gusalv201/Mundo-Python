# Aula 19
"""Python é uma linguagem de programação 
Tipo de tipagem = Dinâmica(Já sabe o tipo da informação).ex print(1234)--Já sabe que é um número inteiro e 
Tipo de tipagem =Forte (o Python não permite operações entre tipos incompatíveis sem conversão explícita. 
Por exemplo, não é possível somar uma string e um inteiro diretamente sem antes 
converter a string para um inteiro ou o inteiro para uma string.)"""
# str = string = texto
# Strings são textos que estão dentro de aspas

# Aspas simples
print('Gustavo Alves')


# Aspas duplas
print("Gustavo")

#Não tem diferença entre as aspas, mas é melhor usar a simples

# Caracter de escape(Pula o próximo caracter)
print("Gustavo \"Alves") # O interpretador ignora a aspa e não dá erro

# r (usa o r para fazer aparecer o caracter de escape)
print(r"Gustavo \"Alves")
# Retorno de carro volta o cursor ao início da linha e vai sobrescrevendo
print("ABC\r123")
# No fim é melhor usar aspas simples e as aspas duplas dentro do texto ou o contrário
print('Gustavo "Alves"')