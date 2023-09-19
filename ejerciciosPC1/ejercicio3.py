pesopayaso= 112
pesomuñeca= 75

pedidopayaso= int(input('¿Cuántos pedidos son de payasos?: '))
pedidomuñeca= int(input('¿Cuántos pedidos son de muñecas?: '))

pesototalpayaso= pesopayaso*pedidopayaso
pesototalmuñeca= pesomuñeca*pedidomuñeca
pesototal=pesototalmuñeca+pesototalpayaso

print(f'El peso total del último pedido es: {pesototal} g.')

