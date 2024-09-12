import sys
import pygame
import random

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.positions = []
        self.length = 5
        self.direction = "Right"

class Apple:
    def __init__(self):
        self.x = random.randint(0, 600 // 35 - 1) * 35
        self.y = random.randint(0, 400 // 35 - 1) * 35

class Snake:

    def __init__(self):
        pygame.init()
        self.player = Player()
        self.apple = Apple()
        self.scores = 0
        self.game_over = False

        # we define the title and the size of the screen
        self.display_surf = pygame.display.set_mode([600, 400])
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

    def on_render(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not self.game_over:
                self.move()
                self.display_surf.fill((0, 0, 0)) # Clear the screen

                # Draw each previous segment of the snake
                for i, pos in enumerate(self.player.positions):
                    pygame.draw.rect(self.display_surf, (0, 255, 0), pygame.Rect(pos[0], pos[1], 35, 35))
                    if i != len(self.player.positions) - 1 and self.player.x == pos[0] and self.player.y == pos[1]:
                        self.game_over = True
                        break

                pygame.draw.rect(self.display_surf, (255, 0, 0), pygame.Rect(self.apple.x, self.apple.y, 35, 35))
                pygame.display.flip()
                self.clock.tick(10)
            else:
                self.show_game_over()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player.direction != "Right":
            self.player.direction = "Left"
        elif keys[pygame.K_RIGHT] and self.player.direction != "Left":
            self.player.direction = "Right"
        elif keys[pygame.K_UP] and self.player.direction != "Down":
            self.player.direction = "Up"
        elif keys[pygame.K_DOWN] and self.player.direction != "Up":
            self.player.direction = "Down"

        if self.player.direction == "Right":
            self.player.x += 35
        elif self.player.direction == "Left":
            self.player.x -= 35
        elif self.player.direction == "Up":
            self.player.y -= 35
        elif self.player.direction == "Down":
            self.player.y += 35

        if self.player.x == self.apple.x and self.player.y == self.apple.y:
            self.scores += 1
            self.player.length += 1
            self.apple.x = random.randint(0, 600 // 35 - 1) * 35
            self.apple.y = random.randint(0, 400 // 35 - 1) * 35

            while True:
                flag = True
                for pos in self.player.positions:
                    if self.apple.x == pos[0] and self.apple.y == pos[1]:
                        self.apple.x = random.randint(0, 600 // 35 - 1) * 35
                        self.apple.y = random.randint(0, 400 // 35 - 1) * 35
                        flag = False
                        break
                if flag:
                    break

        # add to the position and remove if needed
        if len(self.player.positions) >= self.player.length:
            self.player.positions.pop(0)
        self.player.positions.append((self.player.x, self.player.y))

    def show_game_over(self):
        print("show")
        self.display_surf.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 80)
        game_over_text = font.render('GAME OVER', True, (255, 0, 0))
        scores_text = pygame.font.SysFont(None, 50).render(f'Score: {self.scores}', True, (0, 255, 0))
        self.display_surf.blit(game_over_text, (130, 100))
        self.display_surf.blit(scores_text, (235, 200))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    game = Snake()
    game.on_render()
