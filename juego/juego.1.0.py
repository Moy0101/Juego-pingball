import pygame

# Inicializar Pygame
pygame.init()

# Definir constantes
ANCHO = 1000
ALTURA = 700
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTURA))
pygame.display.set_caption("Pong")

# Inicializar variables del juego
jugando = True
reloj = pygame.time.Clock()

# Posiciones y dimensiones de las paletas
paleta_ancho = 20
paleta_alto = 150
paleta1_x = 50
paleta1_y = ALTURA // 2 - paleta_alto // 2
paleta2_x = ANCHO - 50 - paleta_ancho
paleta2_y = ALTURA // 2 - paleta_alto // 2

# Velocidad de las paletas
vel_paleta = 12

# Posición y velocidad de la pelota
pelota_x = ANCHO // 2
pelota_y = ALTURA // 2
pelota_vel_x = 5
pelota_vel_y = 5
pelota_radio = 15

# Bucle principal del juego
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Mover paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1_y > 0:
        paleta1_y -= vel_paleta
    if teclas[pygame.K_s] and paleta1_y < ALTURA - paleta_alto:
        paleta1_y += vel_paleta
    if teclas[pygame.K_UP] and paleta2_y > 0:
        paleta2_y -= vel_paleta
    if teclas[pygame.K_DOWN] and paleta2_y < ALTURA - paleta_alto:
        paleta2_y += vel_paleta

    # Mover la pelota
    pelota_x += pelota_vel_x
    pelota_y += pelota_vel_y

    # Colisiones con los bordes superiores e inferiores
    if pelota_y - pelota_radio < 0 or pelota_y + pelota_radio > ALTURA:
        pelota_vel_y *= -1

    # Colisiones con las paletas
    if (pelota_x - pelota_radio < paleta1_x + paleta_ancho and
        paleta1_y < pelota_y < paleta1_y + paleta_alto):
        pelota_vel_x *= -1

    if (pelota_x + pelota_radio > paleta2_x and
        paleta2_y < pelota_y < paleta2_y + paleta_alto):
        pelota_vel_x *= -1

    # Colisiones con los bordes laterales (reiniciar pelota)
    if pelota_x - pelota_radio < 0 or pelota_x + pelota_radio > ANCHO:
        pelota_x = ANCHO // 2
        pelota_y = ALTURA // 2
        pelota_vel_x *= -1

    # Dibujar todo
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, BLANCO, (paleta1_x, paleta1_y, paleta_ancho, paleta_alto))
    pygame.draw.rect(ventana, BLANCO, (paleta2_x, paleta2_y, paleta_ancho, paleta_alto))
    pygame.draw.circle(ventana, VERDE, (pelota_x, pelota_y), pelota_radio)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

jugando = True
while jugando:

    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    
    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame correctamente
pygame.quit()






