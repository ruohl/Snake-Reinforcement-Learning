# En este archivo tenemos las clases que representan jugadores
import pickle
import random

class Random():
	def __init__(self, juego):
		self.juego = juego
		### Completar si hace falta

	# Juega al juego(de manera aleatoria) hasta que este termine
	def jugar(self):
		while True: # Esto es de prueba
			jugando = True
			tupla = (0, 1, 2)
			while jugando:
				tupla, jugando, recompenza = self.juego.step(random.randint(0, 2))
				print(str(tupla) + ": " + str(recompenza))
			self.juego.reset()
	

	def entrenar(self):
		raise NotImplementedError


class IA():
	def __init__(self, juego):
		self.juego = juego
		self.path = None
		self.Q = {}

		### Completar

	# Juega al juego hasta que este termine, cada vez que mueve (en cada step) decide cual es la mejor accion segun el diccionario Q.
	def jugar(self):
		### Completar
		pass

	# Juega el juego muchas veces y en cada vez completa la informacion de la tabla Q, en base al aprendizaje observado.,
	def entrenar(self):
		while True: # Esto es de prueba
			jugando = True
			estado_anterior = self.juego.reset()
			while jugando:
				action = random.randint(0, 2)
				estado, jugando, recompensa = self.juego.step(action)
				if estado not in self.Q:
					self.Q[estado] = [0, 0, 0]

				best_action = self.get_max_action(self.Q[estado])
				self.Q[estado_anterior][action] = self.Q[estado_anterior][action] + .05 * (recompensa - self.Q[estado_anterior][action] + self.Q[estado][best_action])
				estado_anterior = estado
			

	def get_max_action(self, state):
		max_value = max(state)
		if state[0] == state[1] == state[2]:
			return random.randint(0, 2)
		elif state[0] == state[1] == max_value:
			return random.choice([0, 1])
		elif state[0] == state[2] == max_value:
			return random.choice([0, 2])
		elif state[1] == state[2] == max_value:
			return random.choice([1, 2])
			
		return state.index(max_value)
	






	def set_path(self, path):
		self.path = path

	def save(self):
		if self.path is not None:
			with open(self.path, 'wb') as f:
				pickle.dump(self.Q, f, protocol=pickle.HIGHEST_PROTOCOL)

	def load(self):
		if self.path is not None:
			with open(self.path, 'rb') as f:
				self.Q = pickle.load(f)