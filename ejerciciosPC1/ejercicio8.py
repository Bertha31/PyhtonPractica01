hora_usuario = input("Por favor, ingrese la hora en formato (HH:MM): ")
try:
    horas, minutos = map(int, hora_usuario.split(":"))
except ValueError:
    print("Formato de hora incorrecto. Use HH:MM.")
    exit()

if 7 <= horas and horas< 8 or (horas == 8 and minutos == 0):
    print("Es hora de desayunar.")
elif 12 <= horas and horas < 13 or (horas == 13 and minutos == 0):
    print("Es hora de almorzar.")
elif 18 <= horas and horas< 19 or (horas == 19 and minutos == 0):
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")
