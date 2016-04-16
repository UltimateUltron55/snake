import sys
import time
import pygame
import Arena
import Snake
import scoreboard

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((800, 650))
  pygame.display.set_caption("Snake")
  endgame = False
  arena = Arena.Arena(screen)
  snake = Snake.Snake(screen, arena)
  arena.snake = snake
  scoreboard1= scoreboard.Scoreboard(screen)
  highscore = scoreboard1.check_high_score()
  print(type(highscore))
  scoreboard1.prep_high_score(highscore)
  scoreboard1.show_high_score()
  print(arena.snake)
  arena.update_food()
  snake.blitme()
  arena.draw_walls()
  arena.draw_food()
  scoreboard1.prep_score()
  scoreboard1.show_score()
  pygame.display.flip()
  print(len(snake.positions))
  time.sleep(2)
  while True:
      if endgame == False:
          if snake.collided():
             endgame = True
          if snake.eaten_food():
             print("Snake has eaten food")
             snake.extend = True
             arena.destroy_food()
             arena.update_food()
             arena.draw_food()
             print(len(snake.positions))
             scoreboard1.score += 10
             scoreboard1.prep_score()
             scoreboard1.show_score()

          if endgame == False:
             snake.move()
             time.sleep(0.3) 
    
      else:
          highscore = scoreboard1.incr_high_score(highscore, scoreboard1.score)
          scoreboard1.prep_high_score(highscore)
          scoreboard1.show_high_score()
      snake.check_events()
      pygame.display.flip()

      
      
run_game()

