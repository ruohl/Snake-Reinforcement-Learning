import pygame 

class Grilla:
	def __init__(self, width, height, screen, tamanoCelda) -> None:
		self.width = width
		self.height = height
		self.tamanoCelda = tamanoCelda
		self.screen = screen
		
		self.grid = [[0 for y in range(tamanoCelda)] for x in range(tamanoCelda)]
		print(self.grid)
		self.tile_size = int(height / (self.tamanoCelda))
  
		self.createGrid()

	def createGrid(self):
		firstColor = (42, 144, 30, 230)
		thirdColor = (255, 255, 255, 230)
  
		offset_x = (pygame.display.Info().current_w - (self.height - 100)) // 2
		offset_y = (pygame.display.Info().current_h - (self.height - 100)) // 2
		tile_size = int(self.height / (self.tamanoCelda - 1))
		for x in range(0, self.height, tile_size):
			for y in range(0, self.height, tile_size):
				rect = pygame.Rect(x + offset_x, y + offset_y, tile_size, tile_size)
				print(f"X: {x} Y:{y}")
				pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)
				color = firstColor if (x // tile_size + y // tile_size) % 2 == 0 else thirdColor
				pygame.draw.rect(self.screen, color, rect.inflate(-1, -1))
	
	def obtenerPosicion(self, gridX, gridY): ## A partir de la posicion en INDICE devuelve la posición en PIXELES
		tile_size = int(self.height / (self.tamanoCelda - 1))
		offset_x = (pygame.display.Info().current_w - (self.height - 100)) // 2
		offset_y = (pygame.display.Info().current_h - (self.height - 100)) // 2
		x = gridX * tile_size + offset_x
		y = gridY * tile_size + offset_y
		return x, y