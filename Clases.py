import pygame, json


class GameManager:
	def __init__(self, states):
		self.i = 0
		self.states = states #array
		self.st_list = self.states[self.i] #item con el estado actual
		nivel = globals()[self.st_list["nombre"]] #Instanciacion dinamica usando string
		self.state = nivel()

		self.SCREEN_WIDTH = 800
		self.SCREEN_HEIGHT = 600
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

	def eventos_ui(self):
		self.state.eventos_ui(self.st_list["eventos"])

	def update_logica(self):
		self.state.update_logica()
		if not self.state.active:
			self.next_state()

	def render(self):
		self.state.render(self.screen)

	def next_state(self):
		try:
			self.i += 1
			self.st_list = self.states[self.i] #item con el estado actual
			nivel = globals()[self.st_list["nombre"]] #Instanciacion dinamica usando string
			self.state = nivel()
		except IndexError:
			pass


class GameState:
	def __init__(self):
		self.active = True

	def eventos_ui(self, eventos):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				for evento in eventos:
					if event.key == getattr(pygame, evento["tecla"]):
						print(evento["accion"])
						self.active = False

	def update_logica(self):
		pass

	def render(self, screen):
		self.screen = screen
		self.text = pygame.font.Font(None, 40)
		self.screen.fill(self.fondo)
		mensaje = self.text.render(self.titulo, True, (0,0,0), (255,255,255))
		self.screen.blit(mensaje, (300,200))
		pygame.display.flip()


class MenuPrincipal(GameState):
	def __init__(self):
		GameState.__init__(self)
		self.titulo = "Soy un menu xd"
		self.fondo = (150,150,150)

	def render(self, screen):
		GameState.render(self, screen)

class NivelRandom(GameState):
	def __init__(self):
		GameState.__init__(self)
		self.titulo = "Soy un level"
		self.fondo = (0,102,0)

	def render(self, screen):
		GameState.render(self, screen)

class Video(GameState):
	def __init__(self):
		GameState.__init__(self)
		self.titulo = "Un videito"
		self.fondo = (76,0,153)

	def render(self, screen):
		GameState.render(self, screen)
