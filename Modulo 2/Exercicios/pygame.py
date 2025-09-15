import pygame
import random
import sys

# Inicialização
pygame.init()

# Tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Fuja da Polícia com Ajuda do Amigo!")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (200, 0, 0)
AZUL = (0, 0, 200)
VERDE = (0, 200, 0)
PRETO = (0, 0, 0)

# Fonte
fonte = pygame.font.SysFont(None, 40)

# Jogador
jogador = pygame.Rect(100, 100, 40, 40)
vel_jogador = 5

# Policial
policial = pygame.Rect(700, 500, 40, 40)
vel_policial = 2.5

# Amigo
amigo = pygame.Rect(-100, -100, 50, 50)  # começa fora da tela
protecao_ativa = False
tempo_ultima_protecao = pygame.time.get_ticks()
duracao_protecao = 5000        # 5 segundos
intervalo_protecao = 30000     # 30 segundos

# Relógio
clock = pygame.time.Clock()

# Função de fim de jogo
def game_over():
    texto = fonte.render("Você foi pego!", True, VERMELHO)
    tela.blit(texto, (largura//2 - texto.get_width()//2, altura//2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= vel_jogador
    if teclas[pygame.K_RIGHT]:
        jogador.x += vel_jogador
    if teclas[pygame.K_UP]:
        jogador.y -= vel_jogador
    if teclas[pygame.K_DOWN]:
        jogador.y += vel_jogador

    # Limites da tela
    jogador.x = max(0, min(largura - jogador.width, jogador.x))
    jogador.y = max(0, min(altura - jogador.height, jogador.y))

    # Movimento do policial
    if policial.x < jogador.x:
        policial.x += vel_policial
    if policial.x > jogador.x:
        policial.x -= vel_policial
    if policial.y < jogador.y:
        policial.y += vel_policial
    if policial.y > jogador.y:
        policial.y -= vel_policial

    # 🛡️ Ativa proteção a cada 30 segundos
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_ultima_protecao > intervalo_protecao:
        amigo.topleft = (jogador.x - 60, jogador.y)
        protecao_ativa = True
        tempo_ultima_protecao = tempo_atual

    # ⏱️ Desativa após 5 segundos
    if protecao_ativa and tempo_atual - tempo_ultima_protecao > duracao_protecao:
        amigo.topleft = (-100, -100)
        protecao_ativa = False

    # 👮 Colisão
    if jogador.colliderect(policial):
        if protecao_ativa and amigo.colliderect(policial):
            policial.topleft = (random.randint(600, 750), random.randint(400, 550))  # amigo salva você
        else:
            game_over()

    # 🎨 Desenha tudo
    tela.fill(BRANCO)
    pygame.draw.rect(tela, AZUL, jogador)
    pygame.draw.rect(tela, VERMELHO, policial)
    if protecao_ativa:
        pygame.draw.rect(tela, VERDE, amigo)

    # 🕓 Texto informativo
    if protecao_ativa:
        texto = fonte.render("🛡️ Protegido pelo amigo!", True, PRETO)
    else:
        restante = max(0, (intervalo_protecao - (tempo_atual - tempo_ultima_protecao)) // 1000)
        texto = fonte.render(f"⌛ Próxima proteção em: {restante}s", True, PRETO)
    tela.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)
