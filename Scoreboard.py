import pygame

class Scoreboard():
    """Displays score"""
    def __init__(self, screen):
        self.screen = screen
        self.text_colour = (100,0,0)
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont("Arial", 40)
        self.score = 0
    
    def prep_score(self):
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_colour, (0, 0, 0))
        #self.score_rect = self.score_image.get_rect()
        #self.score_rect.right = self.screen.right - 20
        #self.score_rect.top = 20
        
    def show_score(self):
        self.screen.blit(self.score_image, (0, 0))
        
    def check_high_score(self):
        with open("highscore.txt") as highscore:
            lines = highscore.readlines()
            high_score = lines[0]
            high_score = int(high_score)
        return high_score
        
    def prep_high_score(self, highscore):
        self.high_score_image = self.font.render(str(highscore), True, self.text_colour, (0, 0, 0))
        
    def show_high_score(self):
        self.screen.blit(self.high_score_image, (200, 0))
        
    def incr_high_score(self, highscore, score):
        if score > highscore:
            with open("highscore.txt", mode='w') as file:
                file.write(str(score))
                
    def prep_msg(self, str):
        self.msg_img = self.font.render(str, True, self.text_colour, (0, 0, 0))
                
    def show_msg(self, str):
        self.prep_msg(str)
        self.screen.blit(self.msg_img, (300, 325))

                

        
        
    
        
        