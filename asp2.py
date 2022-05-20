#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) == 2:
    # todo bien
    a_buscar = sys.argv[1]
    word_jumble= ['DEYQAUG',\
                 'XRGTUAV',\
                 'SCASABE',\
                 'XAJGUHV',\
                 'FMOROLB',\
                 'GAHJENE',\
                 ]
    splitem = []
    for i in word_jumble:
        splitem.append(list(i))

    element_lenght = len(splitem[0])

    # splitem es ahora una lista de listas donde cada letra tiene índice


    #def is_next(value, pos):
    def is_next(value, element, index):
        if (value+1) < len(a_buscar):
            if a_buscar[value+1] == check_right(element,index):
                final_value.append(value+1)
                is_next(value,element,index)

            #print(f'\t\t\t{a_buscar[value+1]}')

    def check_next(element, index, index_letter):
        #print(splitem[element])
        #if check_right(element,index) and check_left(element,index):
            #print(f'derecha: {splitem[element][index+1]}')
            #print(f'izquierda: {splitem[element][index-1]}')
        if check_left(element,index):
            # is next
            is_next(index_letter)
        #    print(f'izquierda: {splitem[element][index-1]}')
        elif check_right(element,index):
            is_next(index_letter)
            #print(f'derecha: {splitem[element][index+1]}')

    def check_left(element,index):
        if (index-1) < 0:
#           print(f'\t\t{splitem[element]}')
            #print(f'\t\tno hay nada a la izquierda!')
            return False
        else:
            return index-1

    def check_right(element,index):
        if (index+1) >= element_lenght:
#            print(f'\t\t{splitem[element]}')
            #print(f'\t\tno hay nada a la derecha!')
            return False
        else:
            return index+1

    def check_down(element):
        if (element+1) > len(splitem):
#            print(f'\t\t{splitem[element]}')
            return False #print(f'\t\tno hay elementos abajo')
        else:
            return True

    def check_up(element):
        if (element-1) < 0:
#            print(f'\t\t{splitem[element]}')
            return False #print(f'\t\tno hay elementos arriba')
        else:
            return True

    def up_right():
        pass
    def up_left():
        pass
    def down_right():
        pass
    def down_left():
        pass
        
    for i,num in enumerate(a_buscar):
        # i --> índice
        # num --> valor
        num = num.upper()
        for e,ls in enumerate(splitem):
            if num in ls:
                print(f'Encontré {num} en la fila {e} en la posición {splitem[e].index(num)}!')
                #check_next(e, splitem[e].index(num), i)
                is_next(i,e,splitem[e].index(num))
                #check_right(e, splitem[e].index(num))
                #check_left(e, splitem[e].index(num))
                #check_up(e)
                #check_down(e)

    final_value = []

    if ''.join(final_value) == a_buscar:
        print(f'Logramos encontrar la palabra {a_buscar} :)')
    else:
        print(f'La palabra {a_buscar} no se puede formar :(')

    print(final_value)
else:
    print('Error')
    print('El modo de uso es: python asp2.py <palabra a buscar>')

