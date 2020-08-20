import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((500, 440))
pygame.display.set_caption("2 Dice Roller")

# Can use any font that you have on your system here
arial = pygame.font.SysFont("Arial", 35)


class Die():
    def __init__(self, x, y, width, height):
        self.num = 6
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Special function to print the number as they would appear on a die
    def _numDraw(self, window):
        if self.num == 1:
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 90, self.y + 90), 10)  # Center

        elif self.num == 2:
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 45), 10)  # Top Left
            pygame.draw.circle(
                window, (0, 0, 0), (self.x + 135, self.y + 135), 10)  # Bottom Right

        elif self.num == 3:
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 45), 10)  # Top Left
            pygame.draw.circle(
                window, (0, 0, 0), (self.x + 135, self.y + 135), 10)  # Bottom Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 90, self.y + 90), 10)  # Center

        elif self.num == 4:
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 45), 10)  # Top Left
            pygame.draw.circle(
                window, (0, 0, 0), (self.x + 135, self.y + 135), 10)  # Bottom Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 135, self.y + 45), 10)  # Top Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 135), 10)  # Bottom Left

        elif self.num == 5:
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 45), 10)  # Top Left
            pygame.draw.circle(
                window, (0, 0, 0), (self.x + 135, self.y + 135), 10)  # Bottom Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 135, self.y + 45), 10)  # Top Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 135), 10)  # Bottom Left
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 90, self.y + 90), 10)  # Center

        elif self.num == 6:
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 45), 10)  # Top Left
            pygame.draw.circle(
                window, (0, 0, 0), (self.x + 135, self.y + 135), 10)  # Bottom Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 135, self.y + 45), 10)  # Top Right
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 135), 10)  # Bottom Left
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 45, self.y + 90), 10)  # Left Center
            pygame.draw.circle(window, (0, 0, 0),
                               (self.x + 135, self.y + 90), 10)  # Right Center

    # Function to draw the die outline and the number
    def draw(self, window):
        pygame.draw.rect(window, (150, 150, 150),
                         (self.x, self.y, self.width, self.height), 4)

        self._numDraw(window)


class RollButton():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Function to draw the button with text inside
    def draw(self, window):
        pygame.draw.rect(window, (150, 150, 150),
                         (self.x, self.y, self.width, self.height), 4)

        roll = arial.render("Roll Dice", True, (0, 0, 0))
        window.blit(roll, (180, 325))


# Function to be called in the main loop, so that window is redrawn
def redrawWindow():
    # White BG
    window.fill((255, 255, 255))

    # Drawing both dice
    dice1.draw(window)
    dice2.draw(window)

    # Drawing Roll Button
    roll.draw(window)

    # Updating Display
    pygame.display.update()


# Function to generate random number between 1 and 6 and assign to the two dice
def rollDice():
    dice1.num = randint(1, 6)
    dice2.num = randint(1, 6)


# Initializing the two dice and the roll button
dice1 = Die(50, 70, 180, 180)
dice2 = Die(270, 70, 180, 180)

roll = RollButton(150, 320, 200, 50)

run = True   # For running main loop
rolling = False    # To indicate if the dice is being rolled
rollCount = 0     # To count intermediate rolls of die before giving final value
while run:
    pygame.time.delay(10)
    redrawWindow()

    # Changing value of both die until its been changed 100 times
    if rolling:
        rollDice()
        rollCount += 1

        if rollCount > 100:
            rolling = False
            rollCount = 0

    # Making Roll Button bigger when mouse hovers
    mouse = pygame.mouse.get_pos()
    if 150 <= mouse[0] <= 350 and 320 <= mouse[1] <= 370:
        roll.x = 145
        roll.width = 210

        roll.y = 315
        roll.height = 60
    else:
        roll.x = 150
        roll.width = 200

        roll.y = 320
        roll.height = 50

    for event in pygame.event.get():
        # Closing window
        if event.type == pygame.QUIT:
            run = False

        # Rolling Dice
        if event.type == pygame.MOUSEBUTTONDOWN and rolling == False:
            if 150 <= mouse[0] <= 350 and 320 <= mouse[1] <= 370:
                rolling = True

pygame.quit()
