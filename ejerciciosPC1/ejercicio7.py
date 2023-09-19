numero1 = float(input('Ingrese el primer numero: '))
numero2 = float(input('Ingrese el segundo numero: '))

print('Eliga un numero: ')
print(' 1. Mostrar una suma de los dos números')
print(' 2. Mostrar una resta de los dos números (el primero menos el segundo)')
print(' 3. Mostrar una multiplicación de los dos números')

elegir= int(input('Digite el número: '))
if elegir==1:
    operacion= numero1+numero2
    print(f'La operación elegida dio como resultado: {operacion}')
elif elegir==2:
    operacion= numero1-numero2
    print(f'La operación elegida dio como resultado: {operacion}')
elif elegir==3:
    operacion=numero1*numero2
    print(f'La operación elegida dio como resultado: {operacion}')
else:
    print('no es correcto, intente de nuevo')