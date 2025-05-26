import pygame
import sys

def tela_jogo(tela, largura, altura, fonte_titulo):
    rodando_jogo = True

    while rodando_jogo:
        tela.fill(("pink"))  # Cor de fundo da tela do jogo

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
