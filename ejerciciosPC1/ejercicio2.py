consumo= int(input('¿Cuánto fue su consumo?: S/.'))
propina= int(input('¿Qué porcentaje de propina desea dejar al mesero?: '))
total= consumo + consumo*propina/100
print(f'El monto total a pagar es: S/. {total}')