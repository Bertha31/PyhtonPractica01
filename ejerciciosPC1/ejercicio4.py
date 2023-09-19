numero= int(input('Ingrese un numero entero positivo: '))
if numero <0:
    print('numero no es positivo, intente de nuevo')
else:
    suma=numero*(numero+1)/2
    print(f'la suma total de los primeros {numero} numeros positivos es: {suma}')
