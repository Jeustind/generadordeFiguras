import math

def dibujar_circulo(radio):
    for i in range((radio * 2) + 1):
        for j in range((radio * 2) + 1):
            distancia = math.sqrt((i - radio) ** 2 + (j - radio) ** 2)
            if distancia < radio + 0.5:
                print('*', end='')
            else:
                print(' ', end='')
        print()        

def dibujar_triangulo(altura):
    for i in range(1, altura + 1):
        print('* ' + i)

def dibujar_cuadrado(lado):
    for i in range(lado):
        print('* ' * lado)

def menú():
    while True:
        print("\nEliga una figura para dibujar")
        print("Circulo")
        print("Triangulo")
        print("Cuadrado")
        print("Salir")

        opcion = input("Elige la opción que deseas")
        
        if opcion == 'Circulo':
            radio = int(input("Introduzca el radio del circulo"))
            dibujar_circulo(radio)
        elif opcion == 'Triangulo':
            altura = int(input("Introduce la altura del triangulo: "))

            dibujar_triangulo(altura)
        elif opcion == 'Cuadrado':
            lado = int(input("Introduzca el tamañado de los lados del cuadrado: "))

            dibujar_cuadrado(lado)
        elif opcion == 'Salir':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no disponible, intentelo de nuevo")