import pygame
import sys
from monstros import Monstro # Adicione esta linha!

# O restante do seu arquivo jogo.py continua aqui:

def tela_jogo(tela, largura, altura, fonte_titulo):
    rodando_jogo = True

    # Agora você pode criar instâncias de Monstro normalmente:
    monstro_exemplo = Monstro("Goblin", 80, 10, 3, 20, 10, largura - 250, altura // 2 - 75, 150, 150, "../res/sprites/agua_viva.png")

    while rodando_jogo:
        tela.fill(("pink"))  # Cor de fundo da tela do jogo

        if monstro_exemplo.esta_vivo():
            monstro_exemplo.desenhar(tela)

        texto = fonte_titulo.render("Jogo Iniciado!", True, (255, 255, 255))
        rect = texto.get_rect(center=(largura // 2, altura // 2))
        tela.blit(texto, rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando_jogo = False  # Volta para o menu
                elif evento.key == pygame.K_SPACE:
                    if monstro_exemplo.esta_vivo():
                        monstro_exemplo.receber_dano(20)