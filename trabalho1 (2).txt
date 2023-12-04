#caracteres e chave
import random
import string
chars = "abcdefghijklmnopqrstuvwxyz1234567890 "
chars = list(chars)
key = chars.copy()
random.shuffle(key)
palavras = []
#criptografar string
def cryptostr(palavra):
    stcrypto = ''
    for letra in palavra:
        index=chars.index(letra)
        stcrypto += key[index]
    return stcrypto
#crptografar a lista
def cryptolis(lista):
    listay = []
    for item in lista:
        listay.append(cryptostr(item))
    return listay
# Descriptografar uma string
def decryptostr(stcrypto):
    original = ''
    for char in stcrypto:
        index = key.index(char)
        original += chars[index]
    return original
#decriptografar lista
def decryptolis(crypto_lista):
    listaog = []
    for item in crypto_lista:
        listaog.append(decryptostr(item))
    return listaog
#configurar o jogo
def configurar():
    global palavras
    while True:
        palavra = input("Digite uma palavra (ou 'sair' para encerrar): ")
        palavra = palavra.lower()
        palavracr = cryptostr(palavra)
        if palavra == 'sair':
            return
            break
        elif palavracr in palavras:
            print("Essa palavra já está na lista. Digite outra palavra.")
        else:
            palavras.append(palavracr)
    return palavras
#jogar
#pegar palavra aleatoria
def palavra_random(lista):
    return random.choice(lista)
def leng(p):
    leng = 0
    for item in p:
        leng +=1
    return leng
#jogo
def jogo():
    ganho = []
    erros = []
    global palavras
    print('numero de rodadas: ', leng(palavras))
    while palavras:
        pep = palavra_random(palavras)
        tentativas = 3
        print('tentativas restantes: ', tentativas)
        print('palavra:', '_ '* len(pep))
        while tentativas > 0:
            palpite = input('digite uma palavra:').lower()
            papit = cryptostr(palpite)
            if papit == pep:
                print('voce acertou!')
                ganho.append(pep)
                palavras.remove(pep)
                break
            else:
                print('palavra incorreta. tente novamente.')
                tentativas -=1
                print('tentativas restantes: ', tentativas)
        if tentativas == 0:
            print('voce perdeu... a palavra era:', decryptostr(pep))
            erros.append(pep)
            palavras.remove(pep)
    print('fim de jogo!')
    print('vitorias', len(ganho))
    print('erros', len(erros))
    #feedback = input('gostou?')
#menu do jogo
def menu():
    global palavras
    while True:
        print('para configurar o jogo digite 1')
        print('para jogar digite 2')
        print('para sair digite 3')
        escolha = int(input('escolha:'))
        if escolha == 1:
            #palavras =
            configurar()
        elif escolha == 2:
            if leng(palavras) >0:
                jogo()
            else:
                print('o jogo ainda nao esta configurado')
        elif escolha == 3:
            return False
        else:
            print('escolha invalida')

while True:
    menu()
#configurar()
#jogo()
