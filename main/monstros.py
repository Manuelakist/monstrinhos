import pygame
import sys
import os

class Monstro: 
    
    def __init__ (self, nome, vida_max, ataque, critico, magia, defesa, x, y, largura, altura, caminho_imagem):
        self.nome = nome
        self.vida_max = vida_max
        self.vida_atual = vida_max
        self.ataque = ataque
        self.critico = critico
        self.magia = magia
        self.defesa = defesa
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        
        # Carregar a imagem
        caminho_base = os.path.dirname(os.path.abspath(__file__))
        # O caminho_imagem deve ser relativo à pasta 'main' se 'monstro.py' estiver lá
        # Ex: "../res/sprites/goblin.png"
        caminho_completo_imagem = os.path.join(caminho_base, caminho_imagem)
        
        # Carrega a imagem, e usa .convert_alpha() para lidar com transparência
        self.imagem = pygame.image.load(caminho_completo_imagem).convert_alpha()
        # Redimensiona a imagem para a largura e altura do monstro
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
        
        self.rect = pygame.Rect(x, y, largura, altura)
        
    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
        fonte_pequena = pygame.font.SysFont("arial", 20)
        texto_nome = fonte_pequena.render(self.nome, True, (255, 255, 255))
        texto_vida = fonte_pequena.render(f"HP: {self.vida_atual}/{self.vida_max}", True, (255, 255, 255))
        tela.blit(texto_nome, (self.x + 5, self.y + 5))
        tela.blit(texto_vida, (self.x + 5, self.y + 30))

    def receber_dano(self, dano):
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida_atual}")

    def esta_vivo(self):
        return self.vida_atual > 0