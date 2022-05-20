#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#if len(sys.argv) == 3: 
if len(sys.argv) == 2:
    guess = sys.argv[1]
    #guess = input('Qué palabra buscar en la sopa de letras: ')
    word_jumble= ['DEYQAUG',\
                     'XRGTUAV',\
                     'SCASABE',\
                     'XAJGUHV',\
                     'FMOROLB',\
                     'GAHJENE',\
                     ]
    splitem = []
    
    # separamso la lista que recibmos en letras y armamos una lista nueva - splitem
    for i in word_jumble:
        splitem.append(list(i))
    
    def evaluate_right(element,orig):
        nexto = element[orig+1]
        print(nexto)

#    print(list(guess)[0].upper())
#    print(splitem)
    # buscamos la primera letra de la palabra que nos dieron
    words_guess = list(guess)

    for e,num in enumerate(words_guess):
        # e --> índice
        # num --> valor

        # si no es la última letra
        if e != words_guess[-1]:
            # en cada lista dentro de splitem
            for i in splitem:
                # si encontrás num.upper
                if num.upper() in i:
                    # dame la posicion dentro de i
                    zzz = i.index(num.upper())
                    # y evaluemos la siguiente posición
                    xxx = i[zzz+1]
                    evaluate_right(i, zzz)
    
    #                yyy = splitem.index(i)
    #                print(f'indice en splitem: {yyy}')
    
                    #print(f'indice dentro de la línea de spltem: {zzz}')
                    #print(splitem.index(i)[zzz+1])
                    print(i[zzz])


#        if num.upper() in :

#    for i in splitem:
#                if e != words_guess[-1]:
#                    position_in_splitem = i.index(num.upper())
#                    next_letter = words_guess.index(num)+1
#                    check_derecha(next_letter ,position_in_splitem)

#                check_derecha(num,e+1)

#        if words_guess[0].upper() in i:
#            print(words_guess[0].upper())
#            pass


else:
    print('Error')
    print('El modo de uso es: python asp.py <palabra a buscar>')

