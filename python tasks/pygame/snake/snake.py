import pygame
import sys
import random
import time

class Game():
    
    def __init__(self):
        #размер экрана
        self.screen_wedth = 720
        self.screen_height = 480
        
        #цвета для змейки
        self.red = pygame.Color (225, 0, 0)
        self.green = pygame.Color (0, 225, 0)
        self.black = pygame.Color (0, 0, 0)
        self.white = pygame.COlor (225, 225, 225)
        self.brown = pygame.Color (165, 42, 42)
        
        #Количество кадров в секунду (Frame per second control)
        self.fps_controller = pygame.time.Clock()
        
        #Очки (съеденная нямка)
        self.score = 0
        
    
    def init_and_check_for_errors(self):
        """Проверка начальных параметров запуска"""
        chek_errors = pygame.init()
        
        if chek_errors[1]>0:
            sys.exit()
        print("Ok")
        
    
    def event_loop (self)
        """Цикл событий: отслеживает события (нажатия клавиш)"""

        #Запуск цикла по событиям-ивентам
        for event in pygame.event.get():
            #если кнопулька нажата
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                # нажали escape
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to    
    
    
    def refresh_screen(self):
        #Обновление экрана
        pygame.display.flip()
        game.fps_controller.tick(23)
        
    def show_score(self, choice=1):
        """Отображает результат"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render("Score: {0}".format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        
        if choice == 1:
            s_rect.midtop(80, 10)
        else:
            s.rect.midtop(360, 120)
        
        self.play_surface.blit(s_surf, s_rect)
        
    
    def game_over(self):
        """Выводит результат и надпись геймовер в случае выхода"""
        go_font = pygame.font.SysFont('monaco', 24)
        go_surf = go_font.render.('Game over', True, self.red)
        gp_rect = go_surf.get_rect()
        go_rect.midtop(360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Snake():
    
    def __init__(self, snake_color):
        self.snake_head_pos = [100, 50] #Позиция змеиной головушки
        self.snake_body_pos = [[100, 50],[90, 50],[80,50]]
        self.snake_color = snake_color
        self.direction = "RIGHT"
        self.change_to = self.direction
    
    def snake_body_mechanism(self, score, food_pos, screen_wedth, screen_height):
        """Механизм работы тела змейки"""
        
        self.snake_body.insert(0, list(self,snake_head_pos))
        
        # Eat the food
        if (self.snake_head_pos[0] == food_pos [0] and self.snake_head_pos[1] == food_pos[1]):
            food_pos = [random.randrange(1,screen_wedth/10)*10, random.randrange(1,screen_height/10)*10]
            score += 1
        
        else:
            self.snake_body.pop()
        
        return score, food_pos
    
    def draw_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
    
    def check_for_boundaries(self, game_over, screen_wedth, screen_height):
    
    if any((
        self.snake_head_pos[0] > screen_wedth-10 or
        self.snake_head_pos[0] < 0,
        self.snake_head_pos[1] > screen_height-10 or
        self.snake_head_pos[1] < 0
        )):
        game_over()
    
    for block in self.snake_body[1:]:
        if (block[0] == self.snake_head_pos[0] and block [1] == self.snake_head_pos[1]):
            game_over()
    
    
class Food():
    
    def __init__(self, food_color, screen_wedth, screen_height):
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1,screen_wedth/10)*10, random.randrange(1,screen_height/10)*10]
    
    def food_draw(self):
        pygame.draw.rect(play_surface, self.food_color, pygame.Rect(pos[0], pos[1], 10, 10))


def main():
   
    # Объявляем циклы.
    game = Game()
    snake = Snake(game.green)
    food = Food(game.brown, game.screen_wedth, game.screen_height)
   
    game.init_and_check_for_errors()
    game.set_surface_and_title() #!!!!
    
    while True:
        snake.change_to = game.event_loop(snake.change_to)
        
        snake.validation_direction_and_change()
        snake.change_head_position()
        
        game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)
        snake.draw_snake(game.play_surface, game.white)
        
        food.draw_food(game.play_surface)

        snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)

        game.show_score()
        game.refresh_screen()



if __name__ == "__main__":
    main ()    
    