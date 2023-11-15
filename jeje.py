import hashlib

def calificaciones_alumno(diccionario_calificaciones):
    calificaciones_por_asignatura = diccionario_calificaciones.items()

    materias_recusar = []
    materias_media = []
    materias_excelencia = []

    for materia, calificacion in calificaciones_por_asignatura:
        if calificacion < 7:
            materias_recusar.append(materia)
        elif 7 <= calificacion < 9:
            materias_media.append(materia)
        else:
            materias_excelencia.append(materia)

    print("------------------------------------------------------------------")
    print("Ejercicio 1: Calificaciones")
    print("------------------------------------------------------------------")
    print("Materias a recusar:", materias_recusar)
    print("Materias aprobadas con calificación media:", materias_media)
    print("Materias aprobadas con excelencia:", materias_excelencia)

def cifrado_cesar(palabra):
    abc = "abcdefghijklmnñopqrstuvwxyz"
    desplazamiento = 5
    palabra_cifrada = ""
    abc_modificado=""
    # Recorremos cada letra de la palabra
    for letra in palabra:
        if letra in abc:
            pos_letra = abc.index(letra)
            pos_letra = (pos_letra - desplazamiento) % len(abc)
            palabra_cifrada += abc[pos_letra]
        else:
            palabra_cifrada += letra

    for letra in abc:
        pos_letra=abc.index(letra)
        pos_letra=(pos_letra-desplazamiento)%len(abc)
        abc_modificado+=abc[pos_letra]
    
    print("------------------------------------------------------------------")
    print("Ejercicio 2: Cifrado")
    print("------------------------------------------------------------------")                                                                                                    
    print("Abecedario: " + abc)
    print("Abecedario modificado: " + abc_modificado)
    print("Palabra: " + palabra)
    print("La palabra cifrada: " + palabra_cifrada)

def comparar_hash(archivo1, archivo2, algoritmo='md5'):
    hasher1 = hashlib.new(algoritmo)
    hasher2 = hashlib.new(algoritmo)

    with open(archivo1, 'rb') as f1, open(archivo2, 'rb') as f2:
        while (chunk1 := f1.read(8192)) and (chunk2 := f2.read(8192)):
            hasher1.update(chunk1)
            hasher2.update(chunk2)

    hash_archivo1 = hasher1.hexdigest()
    hash_archivo2 = hasher2.hexdigest()

    print("------------------------------------------------------------------")
    print("Ejercicio 3: Archivos Hash")
    print("------------------------------------------------------------------")
    if hash_archivo1 == hash_archivo2:
        print("Los archivos son iguales")
    else:
        print("Los archivos son diferentes")


def general():
    palabra = input("Introduce la palabra a cifrar: ")

    # Ejercicio 1
    calificaciones = {
        'Matemáticas': 8,
        'Historia': 6,
        'Ciencias': 9,
        'Programación': 10,
        'Inglés': 7
    }
    calificaciones_alumno(calificaciones)

    # Ejercicio 2
    cifrado_cesar(palabra)

    # Ejercicio 3
    archivo1 = 'archivo1.txt'
    archivo2 = 'archivo2.txt'
    comparar_hash(archivo1, archivo2)


# Llamada al método general
general()