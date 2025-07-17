# Aula 35 If / Elif.../Else

Condicao_1 = False
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False


# Após a condição deve usar : “o que  vem a seguir, indentado, é o bloco que será executado se a condição for verdadeira”.
# A partir do momento que o bloco executa algo verdadeiro ele sai do bloco, não continua para as outras
if Condicao_1: # O Python entende, pois se a variável está vazia é False, senão é True OBS:' 'é True
    print('Código da condição 1') # Deve identar com 4 espaços ou um tab
elif condicao2: 
    print('Código da condicao 2')
elif condicao3:
    print('Código da condicao 3')
elif condicao4:
    print('Código da condicao 4')
else:
    print('Nenhuma condição foi satisfeita')

print('Fora do if')

if False == False: #O if pode estar sozinho
    print('Outro if')

print('Fora de novo')

#O pass é uma instrução vazia que serve como placeholder. É muito usado quando você ainda não quer implementar algo, 
# mas precisa de um corpo de função, classe ou bloco if.
# Parecido com ... (elipse) faz o programa ignorar erros