def buscar_en_txt(nombre_archivo, texto_a_buscar):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for numero_linea, linea in enumerate(lineas, 1):
                if texto_a_buscar in linea:
                    print(f'Texto encontrado linea:{numero_linea}: {linea.strip()}')
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no se encontró.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Ejemplo de uso
nombre_archivo = 'informacion.txt'
texto_a_buscar = '@example.org'
buscar_en_txt(nombre_archivo, texto_a_buscar)
