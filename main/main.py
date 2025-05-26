import pygame
import sys
import os
from jogo import tela_jogo

pygame.init()

# 🎵 Música de fundo (carrega com caminho seguro)
pygame.mixer.init()

# Caminho absoluto da música
caminho_base = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(caminho_base, "..", "res", "musica", "trilha.ogg")

pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play(-1)  # Loop infinito

# Controle de volume
volume = 0.5  # 50%
mutado = False
pygame.mixer.music.set_volume(volume)

# Tamanho da tela baseado no usuário
info = pygame.display.Info()
largura, altura = info.current_w, info.current_h
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu - Monstrinhos")

# Fontes
fonte_titulo = pygame.font.SysFont("arial", 60)
fonte_opcao = pygame.font.SysFont("arial", 40)
fonte_texto = pygame.font.SysFont("arial", 30)

# Cores
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)
COR_HOVER = (255, 255, 0)
COR_TITULO = (0, 200, 255)

# Opções do menu principal
opcoes = ["Iniciar", "Instruções", "Sair"]

def desenhar_menu(pos_mouse):
    tela.fill(COR_FUNDO)

    # Título
    titulo = fonte_titulo.render("Monstrinhos", True, COR_TITULO)
    titulo_rect = titulo.get_rect(center=(largura // 2, altura // 5))
    tela.blit(titulo, titulo_rect)

    botoes = []
    espacamento = 70
    y_inicial = altura // 2 - (len(opcoes) * espacamento) // 2

    for i, opcao in enumerate(opcoes):
        y = y_inicial + i * espacamento
        texto = fonte_opcao.render(opcao, True, COR_TEXTO)
        rect = texto.get_rect(center=(largura // 2, y))

        if rect.collidepoint(pos_mouse):
            texto = fonte_opcao.render(opcao, True, COR_HOVER)

        tela.blit(texto, rect)
        botoes.append((opcao, rect))

    # --- CONTROLE DE SOM ---
    botoes_som = []

    # Volume %
    volume_txt = fonte_texto.render(f"Volume: {int(volume * 100)}%", True, COR_TEXTO)
    volume_rect = volume_txt.get_rect(topleft=(30, 30))
    tela.blit(volume_txt, volume_rect)

    # Botões de volume - e +
    botao_menos = fonte_opcao.render("-", True, COR_TEXTO)
    rect_menos = botao_menos.get_rect(topleft=(30, 70))
    tela.blit(botao_menos, rect_menos)
    botoes_som.append(("menos", rect_menos))

    botao_mais = fonte_opcao.render("+", True, COR_TEXTO)
    rect_mais = botao_mais.get_rect(topleft=(80, 70))
    tela.blit(botao_mais, rect_mais)
    botoes_som.append(("mais", rect_mais))

    # Botão mutar/desmutar
    texto_mute = "🔈 Desmutar" if mutado else "🔊 Mutar"
    botao_mute = fonte_texto.render(texto_mute, True, COR_TEXTO)
    rect_mute = botao_mute.get_rect(topleft=(30, 120))
    tela.blit(botao_mute, rect_mute)
    botoes_som.append(("mute", rect_mute))

    pygame.display.flip()
    return botoes + botoes_som

def tela_instrucoes():
    rodando_instrucoes = True

    while rodando_instrucoes:
        pos_mouse = pygame.mouse.get_pos()
        tela.fill(COR_FUNDO)

        # Título
        titulo = fonte_titulo.render("Instruções", True, COR_TITULO)
        titulo_rect = titulo.get_rect(center=(largura // 2, altura // 6))
        tela.blit(titulo, titulo_rect)

        # Texto das instruções
        instrucoes = [
            "Use as setas do teclado para mover seu personagem.",
            "Aperte 'A' para atacar e 'S' para defender.",
            "Ganhe derrotando os monstros em combate.",
        ]

        for i, linha in enumerate(instrucoes):
            texto = fonte_texto.render(linha, True, COR_TEXTO)
            rect = texto.get_rect(center=(largura // 2, altura // 3 + i * 40))
            tela.blit(texto, rect)

        # Botão "Voltar"
        voltar_texto = fonte_opcao.render("Voltar", True, COR_TEXTO)
        voltar_rect = voltar_texto.get_rect(center=(largura // 2, altura - 100))

        if voltar_rect.collidepoint(pos_mouse):
            voltar_texto = fonte_opcao.render("Voltar", True, COR_HOVER)

        tela.blit(voltar_texto, voltar_rect)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltar_rect.collidepoint(pos_mouse):
                    rodando_instrucoes = False

# Loop principal do menu
rodando = True
while rodando:
    pos_mouse = pygame.mouse.get_pos()
    botoes = desenhar_menu(pos_mouse)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for nome, rect in botoes:
                if rect.collidepoint(pos_mouse):
                    if nome == "Iniciar":
                        tela_jogo(tela, largura, altura, fonte_titulo)
                    elif nome == "Instruções":
                        tela_instrucoes()
                    elif nome == "Sair":
                        rodando = False
                    elif nome == "menos":
                        volume = max(0.0, volume - 0.1)
                        if not mutado:
                            pygame.mixer.music.set_volume(volume)
                    elif nome == "mais":
                        volume = min(1.0, volume + 0.1)
                        if not mutado:
                            pygame.mixer.music.set_volume(volume)
                    elif nome == "mute":
                        if mutado:
                            pygame.mixer.music.set_volume(volume)
                            mutado = False
                        else:
                            pygame.mixer.music.set_volume(0)
                            mutado = True

pygame.quit()
sys.exit()
