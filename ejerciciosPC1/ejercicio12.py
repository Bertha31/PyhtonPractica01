import mimetypes

def obtener_tipo_mime(nombre_archivo):
    # Obtiene la extensión del archivo (parte después del último punto)
    extension = nombre_archivo.lower().split('.')[-1]

    # Define una lista de extensiones válidas
    extensiones_validas = ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']

    # Verifica si la extensión está en la lista de extensiones válidas
    if extension in extensiones_validas:
        # Si es válida, obtiene el tipo MIME correspondiente
        tipo_mime, _ = mimetypes.guess_type(nombre_archivo)
        return tipo_mime

    # Si la extensión no es válida, devuelve 'application/octet-stream'
    return 'application/octet-stream'

def main():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    tipo_mime = obtener_tipo_mime(nombre_archivo)
    
    print(f"El tipo MIME del archivo {nombre_archivo} es: {tipo_mime}")

if __name__ == "__main__":
    main()
