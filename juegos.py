# En este archivo tenemos la clase que representa el juego a programar, es importante que siga la interfaz que tiene esta clase, o sea que tenga las funciones que hay en este archivo.

import pygame 

class Snake():
    def __init__(self, tamano):
        self.tamano = tamano

        ### Completar
        pygame.init()
        self.width, self.height = 800, 600
        firstColor = (42, 144, 30)
        secondColor = (66, 226, 48)
        thirdColor = (255, 255, 255, 0.9)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        
                # Variable para mantener el juego en ejecución
        running = True


        # Bucle principal del juego
        while running:
            # Rellena la pantalla con un color
            self.screen.fill(secondColor)
            self.createGrid(self.width, self.height)

            # Iterar sobre la lista de eventos
            for event in pygame.event.get():
                # Si se cierra la ventana, salir del bucle
                if event.type == pygame.QUIT:
                    running = False
                

            # Aquí dibujamos en la pantalla
            # pygame.draw.rect(screen, rojo, (100, 100, 50, 50))  # Ejemplo: dibujar un rectángulo

            # Actualizar la pantalla
            pygame.display.flip()

        # Salir de Pygame
        pygame.quit()



        self.reset()
    
    def createGrid(self, width, height):
        height -= 100
        offset_x = (self.width - height) // 2
        offset_y = (self.height - height) // 2
        tile_size = int(height / (self.tamano - 1))
        for x in range(0, height, tile_size):
            for y in range(0, height, tile_size):
                rect = pygame.Rect(x + offset_x, y + offset_y, tile_size, tile_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)
                color = (42, 144, 30, 230) if (x // tile_size + y // tile_size) % 2 == 0 else (255, 255, 255, 230)
                pygame.draw.rect(self.screen, color, rect.inflate(-1, -1))
                

    # Reinicia el juego:
    #   - Pone la longitud de la serpiente en 1.
    #   - Coloca la serpiente en un lugar random.
    #   - Pone la fruta en una posicion random
    def reset(self):
        ### Completar
        pass

    # Mueve al jugador una vez, en fuincion a la accion realizada.
    # Devuelve 3 cosas:
    #   - El nuevo estado del juego
    #   - Si el juego termino o no (o sea si la serpiente murio o no)
    #   - La recompenza de la accion realizada (0 si no pasa nada, 1 si agarro una fruta, -1 si perdio)
    # Recordatorio: un estado es una lista de 11 numeros bienarios (1 o 0), cada uno de estos bits indican si se cumple una condicion o no (estas 11 condiciones estan detalladas en el informe).
    def step(self, accion):
        assert accion in {0,1,2}, "Accion invalida"     # Chequea que la accion sea valida (0 = sigue derecho, 1 = dobla a la izquierda, 2 = dobla a la derecha)

        estado_nuevo = None ### Completar
        recompenza = None   ### Completar
        termino = None      ### Completar
        ### Completar
        
        self.render()
        return estado_nuevo, recompenza, termino
    
    
    # Actualiza la informacion que se muestra en pantalla usando pygame.
    def render(self):
        ### Completar
        pass