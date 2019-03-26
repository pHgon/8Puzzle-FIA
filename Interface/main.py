import pygame, os, sys
from pygame.locals import *
import pygame_functions as pyf
import constants as c
import time
import controls as co
import shuffle



class Game_Interface:
    def __init__(self):
        pyf.screenSize(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
        pyf.setBackgroundColour(c.GRAY)

        n0 = pyf.makeSprite("images/0.png")
        n1 = pyf.makeSprite("images/1.png")
        n2 = pyf.makeSprite("images/2.png")
        n3 = pyf.makeSprite("images/3.png")
        n4 = pyf.makeSprite("images/4.png")
        n5 = pyf.makeSprite("images/5.png")
        n6 = pyf.makeSprite("images/6.png")
        n7 = pyf.makeSprite("images/7.png")
        n8 = pyf.makeSprite("images/8.png")

        self.plus = pyf.makeSprite("images/plus.png")
        self.minus = pyf.makeSprite("images/minus.png")
        self.shuffle_button = pyf.makeSprite("images/shuffle.png")
        self.text_shuffler_label = pyf.makeLabel("Numero de iteracoes: ", 30, 50, 690, "black", "Arial", "clear")
        self.number_shuffler_label = pyf.makeLabel(str(c.IT), 30, 332, 692, "black", "Arial", "clear")
        self.spriteList = [n0, n1, n2, n3, n4, n5, n6, n7, n8]

        pyf.moveSprite(self.spriteList[1], 150, 150, True)
        pyf.moveSprite(self.spriteList[2], 350, 150, True)
        pyf.moveSprite(self.spriteList[3], 550, 150, True)
        pyf.moveSprite(self.spriteList[4], 150, 350, True)
        pyf.moveSprite(self.spriteList[5], 350, 350, True)
        pyf.moveSprite(self.spriteList[6], 550, 350, True)
        pyf.moveSprite(self.spriteList[7], 150, 550, True)
        pyf.moveSprite(self.spriteList[8], 350, 550, True)
        pyf.moveSprite(self.spriteList[0], 550, 550, True)
        pyf.moveSprite(self.shuffle_button, 490, 710, True)
        pyf.moveSprite(self.plus, 400, 710, True)
        pyf.moveSprite(self.minus, 440, 710, True)
        #pyf.transformSprite(self.shuffle_button, 0, 0.7)  Usar para tabuleiro maior que 3x3

        pyf.showSprite(self.spriteList[0])
        pyf.showSprite(self.spriteList[1])
        pyf.showSprite(self.spriteList[2])
        pyf.showSprite(self.spriteList[3])
        pyf.showSprite(self.spriteList[4])
        pyf.showSprite(self.spriteList[5])
        pyf.showSprite(self.spriteList[6])
        pyf.showSprite(self.spriteList[7])
        pyf.showSprite(self.spriteList[8])
        pyf.showSprite(self.shuffle_button)
        pyf.showSprite(self.plus)
        pyf.showSprite(self.minus)
        pyf.showLabel(self.text_shuffler_label)
        pyf.showLabel(self.number_shuffler_label)
        pyf.transformSprite(self.shuffle_button, 0, 0.35)
        pyf.transformSprite(self.plus, 0, 0.25)
        pyf.transformSprite(self.minus, 0, 0.25)

        self.shuffler = shuffle.Shuffle()

    def run(self):
        # RODA ATE A TECLA ESC SER PRESSIONADA
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        waittime = 0
        while not keys[pygame.K_ESCAPE]:
            current_time = pygame.time.get_ticks()
            if current_time > waittime:
                pygame.event.clear()
                keys = pygame.key.get_pressed()
                waittime += 20

            if pyf.spriteClicked(self.plus):
                c.IT += 1
                pyf.changeLabel(self.number_shuffler_label, str(c.IT))
            if pyf.spriteClicked(self.minus):
                c.IT -= 1
                pyf.changeLabel(self.number_shuffler_label, str(c.IT))
            if pyf.spriteClicked(self.shuffle_button): # ao clicar o sprite do shuffler chama o metodo para embaralhar
                self.shuffler_method(c.IT)

        pyf.endWait()

    def shuffler_method(self, n_moves):
        print(c.IT)
        self.shuffler.shuffle_algorithm(n_moves)
        moves_list = self.shuffler.get_moves_list()
        self.move_numbers(moves_list)

    def change_position(self, m): #m=n?
        n0_x, n0_y = self.spriteList[0].getPosition()
        x_pos, y_pos = self.spriteList[m].getPosition()
        x_temp, y_temp = self.spriteList[m].getPosition()
        n0_y += 100
        n0_x += 100
        y_temp = y_temp+100
        x_temp = x_temp+100
        y_pos += 100
        x_pos += 100

        pyf.moveSprite(self.spriteList[0], x_pos, y_pos, True) # muda posição do 0

        if n0_y > y_temp:
            for x in range(0, 50):
                y_pos += 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_y < y_temp:
            for x in range(0, 50):
                y_pos -= 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_x > x_temp:
            for x in range(0, 50):
                x_pos += 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)
        elif n0_x < x_temp:
            for x in range(0, 50):
                x_pos -= 4
                pyf.moveSprite(self.spriteList[m], x_pos, y_pos, True)
                time.sleep(c.TIME_CONST)

    def move_numbers(self, moves):
        for move in moves:
            self.change_position(move)

game = Game_Interface()
game.run()