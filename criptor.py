# The MIT License (MIT)
# Copyright (c) 2019 Thiago S. Silva
# Read the full license in text file LICENSE

# Mensagem de boas vindas
print("============================================================================\n"
      "= Olá! Meu nome é Criptor e eu sou um algorítmo criado por Thiago Silva.=\n"
      "= Sou especialista na cifra de Júlio César.                                =\n"
      "============================================================================")
# Método básico
modo = input('Decriptar (D*) ou encriptar (E)? ')
modo = modo.upper()
if not (modo == 'D' or modo == 'E'):
    modo = 'D'

# Texto a ser trabalhado
if modo == 'D':
    texto = input('O que quer decriptar? ')
else:
    texto = input('O que quer encriptar? ')

# Chave numérica
while True:
    try:
        chave = int(input('Qual é a chave? '))
        break
    except ValueError:
        print('Essa entrada apenas admites valores inteiros.')

# Caracteres que serão levados em conta, os outros serão ignorados
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caracteres = 'abcdefghijklmnopqrstuvwxyz'

# Armazenará o resultado dos cálculos
resultado = ''

# A codificação/decodificação propriamente dita
for caractere in texto:
    if (caractere in CARACTERES):
        num = CARACTERES.find(caractere)
        if modo == 'D':
            num -= chave
        else:
            num += chave
        if num < 0:
            num += len(CARACTERES)
        if num >= len(CARACTERES):
            num -= len(CARACTERES)
        resultado += CARACTERES[num]
    elif (caractere in caracteres):
        num = caracteres.find(caractere)
        if modo == 'D':
            num -= chave
        else:
            num += chave
        if num < 0:
            num += len(caracteres)
        if num >= len(caracteres):
            num -= len(caracteres)
        resultado += caracteres[num]
    else:
        resultado += caractere

# Momento em que o resultado deve ser mostrado
if modo == 'D':
    print('\nDecriptando...\nO texto decriptado é:', resultado,end='\n\n')
else:
    print('\nEncriptando...\nO texto encriptado é:', resultado,end='\n\n')

# Opcionalmente, gerar um resumo criptográfico
resumo = input("Gerar resumo criptográfico? (S/n*): ")
resumo = resumo.upper()
if resumo == 'S':
    import hashlib
    function = "hashlib."+input("Digite uma função de hash (Default: sha1): ")
    if len(function) == 8:
        function = hashlib.sha1
        abort = 0
    else:
        try:
            function = eval(function)
            abort = 0
        except AttributeError:
            function = str(function)
            print("Função de hash",'"'+function[9:]+'"',"desconhecida. Abortando...")
            abort = 1
    if abort == 0:
        print('Seu resumo criptográfico é:',function(resultado.encode('utf-8')).hexdigest(),end='\n\n')