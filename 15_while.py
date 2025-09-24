contador = 0
while contador < 5:
    print(contador)
    contador += 1 # contador = contador + 1

print('')
while contador > 0:
    print(contador)
    contador -= 1 # contador = contador - 1

print('Contador ', contador)

respuesta = 'S'
while respuesta.upper() == 'S':
    valor = input('Introducir valor: ')
    respuesta = input('Deseas continuar s/n?')



