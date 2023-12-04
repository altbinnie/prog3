#algoritimo de criptografia simples usando random
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
