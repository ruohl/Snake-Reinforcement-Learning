import pygame 

class Grilla:
	def __init__(self, width, height, screen, tamanoCelda) -> None:
		self.width = width
		self.height = height
		self.tamanoCelda = tamanoCelda
		self.screen = screen
		
		self.grid = [[0 for y in range(tamanoCelda)] for x in range(tamanoCelda)]
		self.tile_size = int((height * 0.8) / (self.tamanoCelda))
  
		self.renderGrid()

	def renderGrid(self):
		firstColor = (42, 144, 30, 230)
		thirdColor = (255, 255, 255, 230)
		tamanoFinal = int(self.height * 0.8)
		tile_size = int(tamanoFinal / self.tamanoCelda)

		# Calcula el tamaño total de la grilla
		grid_width = self.tamanoCelda * tile_size
		grid_height = self.tamanoCelda * tile_size

		# Calcula el desplazamiento necesario para centrar la grilla
		offset_x = (self.width - grid_width) // 2
		offset_y = (self.height - grid_height) // 2

		# Dibuja la grilla centrada
		for x in range(0, grid_width, tile_size):
			for y in range(0, grid_height, tile_size):
				rect = pygame.Rect(x + offset_x, y + offset_y, tile_size, tile_size)
				pygame.draw.rect(self.screen, (255, 255, 255), rect)
				color = firstColor if (x // tile_size + y // tile_size) % 2 == 0 else thirdColor
				pygame.draw.rect(self.screen, color, rect.inflate(0,0))

				indX, indY = x // tile_size, y // tile_size
				if (self.grid[indX][indY] != 0):
					color = (0, 0, 255) if self.grid[indX][indY] == 1 else (255, 0, 0)
					pygame.draw.rect(self.screen, color, rect.inflate(0,0))
					
	
	def obtenerPosicion(self, gridX, gridY):
		tamanoFinal = int(self.height * 0.8)  # Mantén la proporción de 0.8 para las celdas
		tile_size = int(tamanoFinal / self.tamanoCelda)

		# Calcula el tamaño total de la grilla
		grid_width = self.tamanoCelda * tile_size
		grid_height = self.tamanoCelda * tile_size

		# Calcula los offsets para centrar la grilla
		offset_x = (self.width - grid_width) // 2
		offset_y = (self.height - grid_height) // 2

		# Convierte las coordenadas de grilla (índices) a coordenadas en píxeles
		x = gridX * tile_size + offset_x
		y = gridY * tile_size + offset_y

		return x, y