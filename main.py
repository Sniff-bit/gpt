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
    def __init__(self, pos, color=(0, 200, 255), name="", item=None):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.dialogue = []
        self.name = name
        self.item = item
        self.given = False

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Aventure de Max")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)

        self.player = Player((WIDTH // 2, HEIGHT // 2))

        self.setup_zones()
        self.load_zone(0)

        self.inventory = []
        self.active_npc = None

        self.dialogue_lines = []
        self.show_dialogue = False

    def show_title_screen(self):
        options = ["Nouvelle partie", "Quitter"]
        selected = 0
        title_font = pygame.font.Font(None, 64)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    if event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    if event.key == pygame.K_RETURN:
                        if selected == 0:
                            return
                        else:
                            pygame.quit()
                            sys.exit()

            self.screen.fill((0, 0, 0))
            title = title_font.render("Aventure de Max", True, (255, 255, 0))
            title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3))
            self.screen.blit(title, title_rect)

            for i, opt in enumerate(options):
                color = (255, 255, 255) if i == selected else (150, 150, 150)
                txt = self.font.render(opt, True, color)
                rect = txt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
                self.screen.blit(txt, rect)

            pygame.display.flip()
            self.clock.tick(60)

    def setup_zones(self):
        self.zones = []

        chambre_npcs = pygame.sprite.Group()
        leo = NPC((200, 200), name="Léo", item="Stilnox 10mg")
        leo.dialogue = [
            "Léo : Salut Max...",
            "Je suis un peu perdu, tu sais...",
            "Mais tu devrais aller explorer dehors."
        ]
        chambre_npcs.add(leo)
        self.zones.append({
            "name": "Chambre de Léo",
            "bg": (30, 30, 30),
            "npcs": chambre_npcs,
        })

        bar_npcs = pygame.sprite.Group()
        mathias = NPC((400, 150), color=(0, 255, 0), name="Mathias", item="Briquet vide")
        mathias.dialogue = [
            "Mathias : J’ai arrêté la clope.",
            "...",
            "*Il tire une taffe devant toi.*",
        ]
        denis = NPC((100, 350), color=(255, 0, 0), name="Denis", item="Glock 17")
        denis.dialogue = [
            "Denis : T’as vu cette vidéo où un mec se fait arracher la tête ?",
            "Non ? T’es pas un vrai.",
        ]
        nao = NPC((600, 450), color=(255, 105, 180), name="Nao", item="Canette 8.6 vide")
        nao.dialogue = [
            "Nao : Tu veux passer cette porte ?",
            "Faut boire une 8.6 cul sec d’abord.",
        ]
        bar_npcs.add(nao, mathias, denis)
        self.zones.append({
            "name": "Bar de Nao",
            "bg": (20, 20, 60),
            "npcs": bar_npcs,
        })

    def load_zone(self, index):
        zone = self.zones[index]
        self.npcs = zone["npcs"]
        self.background_color = zone["bg"]
        self.current_zone_index = index

    def change_zone(self):
        next_index = (self.current_zone_index + 1) % len(self.zones)
        self.load_zone(next_index)

    def draw_text_box(self, text):
        box = pygame.Rect(50, HEIGHT - 150, WIDTH - 100, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), box)
        pygame.draw.rect(self.screen, (255, 255, 255), box, 2)
        rendered = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(rendered, (box.x + 10, box.y + 10))

    def draw_inventory(self):
        y = 10
        header = self.font.render("Inventaire:", True, (255, 255, 0))
        self.screen.blit(header, (10, y))
        y += 20
        for item in self.inventory:
            text = self.font.render(f"- {item}", True, (255, 255, 255))
            self.screen.blit(text, (10, y))
            y += 20

    def give_item(self, npc):
        if npc and npc.item and not npc.given:
            if npc.item not in self.inventory and len(self.inventory) < 4:
                self.inventory.append(npc.item)
            npc.given = True

    def run(self):
        self.show_title_screen()
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
                            if self.active_npc:
                                self.give_item(self.active_npc)
                                self.active_npc = None
                    else:
                        for npc in self.npcs:
                            if self.player.rect.colliderect(npc.rect):
                                self.dialogue_lines = list(npc.dialogue)
                                self.show_dialogue = True
                                self.active_npc = npc
                                break

            keys = pygame.key.get_pressed()
            if not self.show_dialogue:
                self.player.handle_input(keys)
                if self.player.rect.bottom >= HEIGHT:
                    self.player.rect.bottom = 0
                    self.change_zone()

            self.screen.fill(self.background_color)
            self.npcs.draw(self.screen)
            # Draw NPC names above their heads
            for npc in self.npcs:
                if npc.name:
                    text_surf = self.font.render(npc.name, True, (255, 255, 255))
                    text_rect = text_surf.get_rect(midbottom=(npc.rect.centerx, npc.rect.top - 4))
                    self.screen.blit(text_surf, text_rect)

            self.screen.blit(self.player.image, self.player.rect)
            self.draw_inventory()

            if self.show_dialogue and self.dialogue_lines:
                self.draw_text_box(self.dialogue_lines[0])

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()
