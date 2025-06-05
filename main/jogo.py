import pygame
import sys
from monstros import Monstro

def tela_jogo(tela, largura, altura, fonte_titulo):
    rodando_jogo = True

    monstro_exemplo = Monstro("Goblin", 80, 10, 3, 20, 10, largura // 2, altura // 4, 640, 640, "../res/sprites/goblin.png")

    while rodando_jogo:
        tela.fill(("pink"))  

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
                    rodando_jogo = False 
                elif evento.key == pygame.K_SPACE:
                    if monstro_exemplo.esta_vivo():
                        monstro_exemplo.receber_dano(20)