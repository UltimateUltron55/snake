import pygame
import sys

class Snake:
    """A class to represent a snake in the game"""
    def __init__(self, screen, arena):
        self.extend = False
        self.arena = arena
        self.direction = 'right'
        self.screen = screen
        self.image = pygame.image.load('snake_head.png')
        self.positions = [(20, 12),(20, 13),(20, 14),(20,15), (20,16), (20,17), (20,18), (20, 19), (20,20)]
    
    def check_events(self):
        """Checks events like keypresses"""
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              sys.exit()
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RIGHT and not self.direction == 'left':
                  self.direction = 'right'
               elif event.key == pygame.K_LEFT and not self.direction == 'right':
                   self.direction = 'left'
               elif event.key == pygame.K_DOWN and not self.direction == 'up':
                   self.direction = 'down'
               elif event.key == pygame.K_UP and not self.direction == 'down':
                   self.direction = 'up'
                
    def get_next_step(self):
        """Gets the snake's next step"""
        if self.direction == 'right':
            next_x = self.positions[0][0] + 1
            next_y = self.positions[0][1]
        elif self.direction == 'left':
            next_x = self.positions[0][0] + -1
            next_y = self.positions[0][1]
        elif self.direction == 'down':
            next_x = self.positions[0][0]
            next_y = self.positions[0][1] + 1
        elif self.direction == 'up':
            next_x = self.positions[0][0]
            next_y = self.positions[0][1] + -1
        next_position = (next_x, next_y)
        return next_position

    def update_position(self, new_pos):
        """Updates the snake's position"""
        if self.extend == False:
           del self.positions[-1] 
        self.positions.insert(0, new_pos)
        if self.extend == True:
           self.extend = False

    def erase(self):
        """Erases previous snake positions"""
        x = 20*self.positions[-1][0]
        y = 20*self.positions[-1][1] + 50
        self.screen.fill((0, 0, 0), (x, y, 20, 20))
        
    def blitme(self):
        """Draws the snake to the screen"""
        for pos in self.positions:
            x_and_y = (20*pos[0], 20*pos[1] + 50)
            self.screen.blit(self.image, x_and_y)
            
    def move(self):
        """A function to move the snake"""
        self.check_events()
        next_step = self.get_next_step()
        self.erase()
        self.update_position(next_step)
        self.blitme()
        
    def collided(self):
        """Checks for collisions with the snake or the walls"""
        if self.positions[0] in self.positions[1:] or self.positions[0] in self.arena.walls:
            return True
        else:
            return False
                   
    def eaten_food(self):
        """Checks if snake has eaten food"""
        if self.positions[0] in self.arena.food:
            return True
        else:
            return False
             
        

        
        
    