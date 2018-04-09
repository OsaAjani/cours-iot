#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
import cryptocompare

def quit () :

    print('Merci d\'avoir utilisé CryptoPrice !')
    exit(0)


def show_coin_list () :

    coin_list = cryptocompare.get_coin_list(format = True)
    for coin in coin_list :
        print(coin)


def show_coin_price (coin) :

    if coin not in cryptocompare.get_coin_list(format = True) :
        print('Désolé, cette crypto n\'existe pas !')
        return False

    coin_price = cryptocompare.get_price(coin, full = False, curr = 'USD')
    print('1 {coin} = {coin_price} $'.format(coin = coin, coin_price = coin_price[coin]['USD']))



#Main part
print('###########################\nBienvenu dans CryptoPrice !\n###########################\n')

while True :
    coin = input("""
Entrez l\'acronyme de la monnaie dont vous voulez le prix ?
Sinon, pour voir la liste des monnaies : list.
Et pour quitter : quit.
Acronyme : """)
   
    if coin == 'quit' :
        exit()

    if coin == 'list' :
        show_coin_list()
        continue
    
    show_coin_price(coin)

quit()
