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
        s_font = pygame.font.
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        