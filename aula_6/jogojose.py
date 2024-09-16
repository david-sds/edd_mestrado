import pygame
import random

# Inicializando o pygame
pygame.init()

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Definindo dimensões da janela
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Come-Come")

# Definindo o relógio para controlar o FPS
clock = pygame.time.Clock()

# Definindo a classe para o Come-Come (jogador)
class ComeCome:
    def __init__(self):
        self.size = 20
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5
        self.direction = "STOP"

    def move(self):
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed

        # Limitar o movimento à tela
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.size:
            self.x = WIDTH - self.size
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size

    def draw(self):
        pygame.draw.rect(screen, YELLOW, [self.x, self.y, self.size, self.size])

# Definindo a classe para os pontos (comida)
class Food:
    def __init__(self):
        self.size = 10
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(0, HEIGHT - self.size)

    def draw(self):
        pygame.draw.rect(screen, BLUE, [self.x, self.y, self.size, self.size])

# Função principal do jogo
def game_loop():
    # Criar o jogador e a comida
    come_come = ComeCome()
    food = Food()

    # Variável de controle do loop
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Movimentação com as setas do teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    come_come.direction = "UP"
                elif event.key == pygame.K_DOWN:
                    come_come.direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    come_come.direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    come_come.direction = "RIGHT"

        # Movimentar o jogador
        come_come.move()

        # Verificar colisão com a comida
        if (come_come.x < food.x + food.size and
            come_come.x + come_come.size > food.x and
            come_come.y < food.y + food.size and
            come_come.y + come_come.size > food.y):
            food = Food()  # Gerar nova comida em lugar aleatório

        # Desenhar tudo
        screen.fill(BLACK)
        come_come.draw()
        food.draw()

        # Atualizar a tela
        pygame.display.flip()

        # Controlar o FPS
        clock.tick(15)

    pygame.quit()

# Executar o jogo
game_loop()
