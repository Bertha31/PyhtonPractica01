consumo= float(input('¿Cuánto fue su consumo?: S/.'))
propina= float(input('¿Qué porcentaje de propina desea dejar al mesero? (ingresar numero sin %): '))
total= consumo + consumo*propina/100
totalpropina= consumo*propina/100
print(f'Propina en total: S/. {totalpropina}')
print(f'El monto total a pagar (Consumo + Propina) es: S/. {total:.2f}')