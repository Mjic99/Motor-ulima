import pygame, json
from Clases import *
from linked_list import *

pygame.init()
pygame.display.set_caption("Ejemplo")
pygame.font.init()

#Leer los estados del json y pasarlos a una lista enlazada en orden
data = json.load(open("estados.json"))
array = data["estados"]

lista = List()
for i in range(len(array)-1, -1, -1):
	lista.add(array[i]["nombre"])

clock = pygame.time.Clock()

manager = GameManager(array)


while True:

    manager.eventos_ui()
    manager.update_logica()
    manager.render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
