# En este archivo tenemos la clase que representa el juego a programar, es importante que siga la interfaz que tiene esta clase, o sea que tenga las funciones que hay en este archivo.

import pygame
from grilla import Grilla
import sys

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
		self.grilla = Grilla(self.width, self.height, self.screen, self.tamano)
		
		# Variable para mantener el juego en ejecución
		running = True


		# Bucle principal del juego
		while running:
			# Rellena la pantalla con un color
			self.button("Exit", pygame.quit)
			self.screen.fill(secondColor)
			self.grilla.createGrid()

			self.draw_snake()

			# Iterar sobre la lista de eventos
			for event in pygame.event.get():
				# Si se cierra la ventana, salir del bucle
				if event.type == pygame.QUIT:
					running = False
			# Actualizar la pantalla
			pygame.display.flip()

		# Salir de Pygame
		pygame.quit()



		self.reset()
  
	def button (self, text, event):
		textColor = (245, 245, 245)
		bgBtnColor = (40, 42, 50)
		hoverBtnColor = (58, 61, 70)
		width = self.screen.get_width()
		height = self.screen.get_height()
		textSize = 28
		font = pygame.font.SysFont('segoeuisemibold', textSize)
		text = font.render(text, True, textColor)
		text_rect = text.get_rect(center=(width/2 + 70, height/2 + 20))
		pygame.draw.rect(self.screen, bgBtnColor, [width/2, height/2, 140, 40], border_radius=40)
		self.screen.blit(text, text_rect)

		while True:
			for ev in pygame.event.get(): 
		  
				if ev.type == pygame.QUIT: 
					event()

				#checks if a mouse is clicked 
				if ev.type == pygame.MOUSEBUTTONDOWN: 
				
					#if the mouse is clicked on the j
					# button the game is terminated 
					if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
						pygame.quit() 
				pass	
			# self.screen.fill((bgColor))
			mouse = pygame.mouse.get_pos()
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
				pygame.draw.rect(self.screen,hoverBtnColor,[width/2,height/2,140,40]) 
			else:
				pygame.draw.rect(self.screen,bgBtnColor,[width/2,height/2,140,40]) 
			self.screen.blit(text , (width/2+50,height/2)) 
			pygame.display.update() 


	def draw_snake(self):
		pass

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