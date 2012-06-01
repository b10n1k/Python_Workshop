import pygame,os,sys,random
from pygame.locals import *

class Spinner:
	
	def __init__(self):
		pygame.init()
		self.orange=pygame.image.load("orange.jpg")
		self.apple=pygame.image.load("apple.jpg")
		self.lemon=pygame.image.load("lemon.jpg")
		self.bingo=pygame.image.load("bingo.jpg")
		self.icons=[self.orange, self.apple, self.lemon, self.bingo]
		self.interface=pygame.display.set_mode((300, 400))
		self.interface.blit(self.icons[0],(0,0))
		pygame.display.set_caption("Spinner")
		#self.background=pygame.Surface(self.interface.get_size())
		#self.background=self.background.convert()
		#self.background.fill((100,144,189))			
		
	
	def spin(self):
		for event in pygame.event.get():
			if event.type==K_ESCAPE:
				pass
			
	
	def display(self):
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				pygame.display.update()

	
sp=Spinner()
while 1:
	sp.interface.blit(pygame.image.fromstring("text",(200,200),'RGB'),(0,0))
	sp.interface.fill((211,211,100))
	sp.display.update()

