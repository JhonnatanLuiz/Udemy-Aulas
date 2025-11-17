try:
    import pygame # type: ignore
except ImportError:
    print("Error: pygame is not installed. Please install it using: pip install pygame")
    exit(1)
import random

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
CIANO = (0, 255, 255)
MAGENTA = (255, 0, 255)
LARANJA = (255, 165, 0)

# Configurações do jogo
LARGURA = 500
ALTURA = 600
TAMANHO_BLOCO = 30
LARGURA_GRADE = 10
ALTURA_GRADE = 20

# Formas das peças
FORMAS = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

CORES = [AZUL, VERDE, VERMELHO, AMARELO, CIANO, MAGENTA, LARANJA]

class Peca:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forma = random.choice(FORMAS)
        self.cor = random.choice(CORES)
        self.rotacao = 0

def criar_grade():
    return [[PRETO for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]

def adicionar_a_grade(grade, peca):
    for y, linha in enumerate(peca.forma):
        for x, bloco in enumerate(linha):
            if bloco:
                grade[y + peca.y][x + peca.x] = peca.cor
    return grade

def colisao(grade, peca):
    for y, linha in enumerate(peca.forma):
        for x, bloco in enumerate(linha):
            if bloco:
                if (x + peca.x < 0 or x + peca.x >= LARGURA_GRADE or
                    y + peca.y >= ALTURA_GRADE or
                    grade[y + peca.y][x + peca.x] != PRETO):
                    return True
    return False

def rotacionar(peca):
    return list(zip(*peca[::-1]))

def remover_linhas(grade):
    linhas_removidas = 0
    for y in range(ALTURA_GRADE):
        if PRETO not in grade[y]:
            del grade[y]
            grade.insert(0, [PRETO for _ in range(LARGURA_GRADE)])
            linhas_removidas += 1
    return linhas_removidas

def desenhar_grade(tela, grade):
    for y, linha in enumerate(grade):
        for x, cor in enumerate(linha):
            pygame.draw.rect(tela, cor, (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO - 1, TAMANHO_BLOCO - 1))

def desenhar_peca(tela, peca):
    for y, linha in enumerate(peca.forma):
        for x, bloco in enumerate(linha):
            if bloco:
                pygame.draw.rect(tela, peca.cor, ((peca.x + x) * TAMANHO_BLOCO, (peca.y + y) * TAMANHO_BLOCO, TAMANHO_BLOCO - 1, TAMANHO_BLOCO - 1))

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    
    grade = criar_grade()
    peca_atual = Peca(LARGURA_GRADE // 2 - 1, 0)
    proxima_peca = Peca(LARGURA_GRADE // 2 - 1, 0)
    
    pontuacao = 0
    nivel = 1
    tempo_queda = 0.5
    tempo_ultima_queda = pygame.time.get_ticks()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    peca_atual.x -= 1
                    if colisao(grade, peca_atual):
                        peca_atual.x += 1
                elif evento.key == pygame.K_RIGHT:
                    peca_atual.x += 1
                    if colisao(grade, peca_atual):
                        peca_atual.x -= 1
                elif evento.key == pygame.K_DOWN:
                    peca_atual.y += 1
                    if colisao(grade, peca_atual):
                        peca_atual.y -= 1
                elif evento.key == pygame.K_UP:
                    peca_atual.forma = rotacionar(peca_atual.forma)
                    if colisao(grade, peca_atual):
                        peca_atual.forma = rotacionar(peca_atual.forma)
                        peca_atual.forma = rotacionar(peca_atual.forma)
                        peca_atual.forma = rotacionar(peca_atual.forma)

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_ultima_queda > tempo_queda * 1000:
            peca_atual.y += 1
            if colisao(grade, peca_atual):
                peca_atual.y -= 1
                grade = adicionar_a_grade(grade, peca_atual)
                linhas_removidas = remover_linhas(grade)
                pontuacao += linhas_removidas * 100
                if linhas_removidas > 0:
                    nivel = pontuacao // 1000 + 1
                    tempo_queda = max(0.1, 0.5 - (nivel - 1) * 0.05)
                peca_atual = proxima_peca
                proxima_peca = Peca(LARGURA_GRADE // 2 - 1, 0)
                if colisao(grade, peca_atual):
                    rodando = False
            tempo_ultima_queda = tempo_atual

        tela.fill(PRETO)
        desenhar_grade(tela, grade)
        desenhar_peca(tela, peca_atual)
        
        fonte = pygame.font.Font(None, 36)
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO)
        texto_nivel = fonte.render(f'Nível: {nivel}', True, BRANCO)
        tela.blit(texto_pontuacao, (LARGURA - 200, 10))
        tela.blit(texto_nivel, (LARGURA - 200, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()