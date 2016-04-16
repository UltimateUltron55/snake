import pygame
import random




class Arena:
    def __init__(self, screen):
        self.snake = None
        self.screen = screen
        self.size = (40, 30)
        self.walls = self.make_walls([ \
            '1111111111111111111111111111111111111111', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000011111110000000000000000001', \
            '1000000000000000000010000000000000000001', \
            '1000000000000000000010000000000000000001', \
            '1000000000000000000010000000000000000001', \
            '1000000000000011111110000000000000000001', \
            '1000000000000000000000000000000100000001', \
            '1000000000000000000000000000011111000001', \
            '1000000000000000000111000000000100000001', \
            '1000000111110000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000011000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000001000000000000000000000000001', \
            '1000000000000000000000000001000000000001', \
            '1000000000000000000000000001000000000001', \
            '1000000000000010000000000001111000000001', \
            '1000000000001111100000000001000000000001', \
            '1000000000000010000000000001000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000001111111111000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1000000000000000000000000000000000000001', \
            '1111111111111111111111111111111111111111'])
        self.wall_image = pygame.image.load('wall.png')
        self.food_image = pygame.image.load('Food.png')
        self.wall_size = self.wall_image.get_size()
    
    def make_walls(self, layout):
    	walls = []
    	for row in range(0, self.size[1]):
    		row_layout = layout[row]
    		for col in range(0, self.size[0]):
    			col_layout = row_layout[col]
    			if col_layout == '1':
    				walls.append((col, row))
    	return walls
    	
    def draw_walls(self):
        for wall in self.walls:
            x = wall[0]*self.wall_size[0]
            y = (wall[1]*self.wall_size[1]) + 50
            self.screen.blit(self.wall_image, (x, y))
    
    def make_food(self):
        found = False
        while not found:
            food_x = random.randint(0, 39)
            food_y = random.randint(0, 29)
            if self.snake != None:
                if (food_x, food_y) not in self.walls and (food_x, food_y) not in self.snake.positions:
                    found = True
        print((food_x, food_y))
        return [(food_x, food_y)]

    
    def draw_food(self):
        if len(self.food) > 0:
            self.screen.blit(self.food_image, (self.food[0][0] * 20, (self.food[0][1] * 20) + 50))
        
    def destroy_food(self):
        del self.food[0]
    
    def update_food(self):
        self.food = self.make_food()
        
        
        

    
    	
            
            