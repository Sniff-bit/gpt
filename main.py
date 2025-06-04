import sys
import pygame

WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 4

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=pos)

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, color=(0, 200, 255)):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.dialogue = []

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Aventure de Max")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)

        self.player = Player((WIDTH // 2, HEIGHT // 2))
        self.npcs = pygame.sprite.Group()
        self.create_world()

        self.dialogue_lines = []
        self.show_dialogue = False

    def create_world(self):
        leo = NPC((200, 200))
        leo.dialogue = [
            "L\xe9o : Salut Max...",
            "Je suis un peu perdu, tu sais...",
            "Mais tu devrais aller explorer dehors."
        ]
        self.npcs.add(leo)

    def draw_text_box(self, text):
        box = pygame.Rect(50, HEIGHT - 150, WIDTH - 100, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), box)
        pygame.draw.rect(self.screen, (255, 255, 255), box, 2)
        rendered = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(rendered, (box.x + 10, box.y + 10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.show_dialogue:
                        self.dialogue_lines.pop(0)
                        if not self.dialogue_lines:
                            self.show_dialogue = False
                    else:
                        for npc in self.npcs:
                            if self.player.rect.colliderect(npc.rect):
                                self.dialogue_lines = list(npc.dialogue)
                                self.show_dialogue = True
                                break

            keys = pygame.key.get_pressed()
            if not self.show_dialogue:
                self.player.handle_input(keys)

            self.screen.fill((30, 30, 30))
            self.npcs.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)

            if self.show_dialogue and self.dialogue_lines:
                self.draw_text_box(self.dialogue_lines[0])

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()
