# usr/local/bin/python3
"""
Snakes!
author: kay hudson
"""
import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1] > 0: print("Errors: {}".format(check_errors))

play_surface = pygame.display.set_mode((720, 460))

