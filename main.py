import pygame as pg 
from sys import exit

from settings import *
from game import *



title = "Game engine"
bg_color = "white"




if THEME == 'dark':
        bg_color = "black"



class MainCycle:
	def __init__(self):
		self.w, self.h = WIDTH, HEIGHT
		pg.init()
		self.screen = pg.display.set_mode((self.w, self.h), vsync=1)
		self.clock = pg.time.Clock()
		self.core = Game();
		self.core.update();


	def checkEvents(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				exit()

	def draw(self):
		self.screen.fill(bg_color)
		self.core.game()

	def update(self):
		pg.display.flip()
		self.clock.tick(FPS)
		pg.display.set_caption(title)
		self.d_time = self.clock.tick(FPS)
		self.core.update()
		
	def run(self):
		while True:
			self.checkEvents()
			self.update()
			self.draw()

if __name__ == "__main__":
	game = MainCycle()
	game.run()
