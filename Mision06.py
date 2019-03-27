#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#MISION IMPOSIBLE
import math
import random

import pygame  # Librería de pygame

    # Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
    # Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
def generarColorFi():  #Funcion que crea colores aleatorios
    rojo = random.randint(0, 255)
    verde = random.randint(0, 15)
    azul = random.randint(0, 20)
    return (rojo, verde, azul)
def generarColorFi2():  # Funcion que crea colores aleatorios
    rojo = random.randint(0, 20)
    verde = random.randint(0, 255)
    azul = random.randint(0, 15)
    return (rojo, verde, azul)

    # Estructura básica de un programa que usa pygame para dibujar

def figura(r, rR, l,r2,rR2,l2):
        # Inicializa el motor de pygame
    pygame.init()
        # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
            # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

            # Borrar pantalla
        ventana.fill(BLANCO)

            # Dibujar, aquí haces todos los trazos que requieras

        k = r / rR
        p = r // math.gcd(r, rR)

        for angulo in range(0, 361 * p, 1):
            a = math.radians(angulo)
            x = int(rR * (((1 - k) * math.cos(a)) + ((l * k) * (math.cos((((1 - k) / k) * (a)))))))
            y = int(rR * (((1 - k) * math.sin(a)) - ((l * k) * (math.sin((((1 - k) / k) * (a)))))))
            color= generarColorFi()
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1, 1)

        k2 = r / rR
        p2 = r // math.gcd(r2, rR2)

        for angulo2 in range(0, 361 * p2, 1):
            a = math.radians(angulo2)
            x2 = int(rR2 * (((1 - k2) * math.cos(a)) + ((l2 * k2) * (math.cos((((1 - k2) / k2) * (a)))))))
            y2 = int(rR2 * (((1 - k2) * math.sin(a)) - ((l2 * k2) * (math.sin((((1 - k2) / k2) * (a)))))))
            color2 = generarColorFi2()
            pygame.draw.circle(ventana, color2, (x2 + ANCHO // 2, ALTO // 2 - y2), 1, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(60)  # 60 fps

        # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    r= int(input( "valor de r: "))
    rR= int(input("valor de R: "))
    l= float(input("valor de l: "))
    r2= int(r*.5)
    rR2= int(rR*.7)
    l2= float(l*1.5)
    figura(r, rR, l,r2,rR2,l2)


main()