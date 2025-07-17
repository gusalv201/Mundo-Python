# Aula 32 Função/Método Format
# Tudo em python é um objeto
# Um objeto pode fazer ações
# Chamamos de métodos para essas ações


a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a,b,c) #Eu coloquei de argumentos a,b e c. Por padrão ele coloca na string pela ordem
# Deve usar as chaves na string para puxar
#Pode usar o :.2f na variável
# Pode usar índices para mudar a ordem {0} {0} {1}
# Erro Out of range é por chamar algo que já acabou. Ex.COlocar quatro chaves com 3 argumentos

# Pode-se nomear os argumentos (parametros nomeados)
# Deve-se colocar <nome do parametro> = <argumento> ex. .format(idade=a, peso=b, imc=c)
# Se nomear o primeiro tem que nomear todos. Se nomear o segundo é dali pra frente que tem que nomear
# Se nomear o último pode ser só ele
# EX. .format(nome=a, b, c) Código com erro
# ex. .format(a,b, nome=c) Código certo
# Após nomear pode chamar nas chaves os nomes atribuídos
# string = '{peso}, {altura}, {imc}'.format(peso=a, altura=b, imc=c)

print (formato)

# A distribuição dos argumentos não precisa estar na mesma linha, ex...
nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))