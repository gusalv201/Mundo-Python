# Aula 34 Condicionais if(se) / elif(se não se)..../else(se não)

# Quando faz uma pergunta retorna um dado booleano 
# Para fazer pergunta usa operador lógico

entrada = input('Você quer entrar ou sair?')

#if True: # Tem que ter um valor lógico
if entrada == 'entrar':
    print('Você entrou no sistema!') #Só vai executar se for True
elif entrada == 'sair': # Depende do IF
    print('Você saiu do sistema!') # Posso usar quantos quiser,subsidiário
else: # Depende do IF
    print('Você deveria ter digitado conforme orientado.') # Só executa se não atender todas as outras.

print('Aqui está fora dos blocos e vai executar independente das condições')






