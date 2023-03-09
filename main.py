# Importing the necessary libraries
import pygame
from random import *

pygame.init()

# Creating the game window
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket And Planets Game")

# Loop management boolean and difficulty (planets speed, rocket speed...)
stop_game = False
difficulty = 0.5

# Rocket variables
rocket_x = 210
rocket_y = 300
rocket_width = 88
rocket_height = 175
rocket_move_x = 0

# Planets variables
planet_x = randint(30, 130)
planet_y = 20
planet_width = 111
planet_heigth = 80
between_planets_x = 350
between_planets_y = 125
planets_speed = difficulty

# Printing the score
points = 0
font = pygame.font.Font(None, 24)
score = font.render("0 points", 1, (255, 0, 0))

# Loading images
rocket_img = pygame.image.load("img/rocket.png")
left_planet_img = pygame.image.load("img/planet.png")
right_planet_img = pygame.image.load("img/planet.png")

while not stop_game:

    # Event listener
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            # Escaping the game
            if event.key == pygame.K_ESCAPE:
                stop_game = True
            
            # Moving the rocket to the right
            elif event.key == pygame.K_RIGHT:
                rocket_move_x = difficulty

        # Moving the rocket to the left
        elif event.type == pygame.KEYUP:
            rocket_move_x = -difficulty

        # Stopping the game when the rocket is out of the screen
        if rocket_x < -10 or rocket_x > screen_width:
            stop_game = True

    if planet_y > screen_height:

        planet_x = randint(55, 150)
        planet_y = 0

        points += 1
        score = font.render(str(points) + "points", 1, (255, 0, 0))

    screen.fill((255, 255, 250))

    screen.blit(left_planet_img, (planet_x, planet_y))
    screen.blit(right_planet_img, (planet_x + between_planets_x, planet_y + between_planets_y))

    planet_y = planet_y + planets_speed

    # Left planet crash
    bottom_right_point_first_planet_x = planet_x + planet_width
    bottom_right_point_first_planet_y = planet_y + planet_heigth

    if bottom_right_point_first_planet_x > rocket_x:
        if bottom_right_point_first_planet_y > rocket_y:
            if bottom_right_point_first_planet_y < rocket_y + rocket_height:
                stop_game = True

    # Right planet crash
    bottom_left_point_second_planet_x = planet_x + between_planets_x
    bottom_left_point_second_planet_y = planet_y + between_planets_y + planet_heigth

    if rocket_x + rocket_width > bottom_left_point_second_planet_x:
        if rocket_x < bottom_left_point_second_planet_y:
            if rocket_x + rocket_height > bottom_left_point_second_planet_y:
                print("ee")
                stop_game = True

    # Refreshing the screen
    rocket_x += rocket_move_x
    screen.blit(score, (20, 580))
    screen.blit(rocket_img, (rocket_x, rocket_y))
    pygame.display.update()