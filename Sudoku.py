import pandas as pd
import pygame as pg
import random
import math


#Cores Usadas

preto = (0,0,0)
vermelho = (255, 0, 0)
azul_claro = (200, 200, 255)
azul = (100, 100, 255)
azul_petroleo = (0, 128, 128)
verde = (0, 255, 0)
branco = (255, 255, 255)

# Declaração da Janela e Resolução
janela = pg.display.set_mode((1080,720))

# Inicio da Declaração da Fonte

pg.font.init()

fonte = pg.font.SysFont('Nimbus Sans', 50 )


dado_tabuleiro = [["n" for _ in range(9)] for _ in range(9)]
dado_jogo = [["n" for _ in range(9)] for _ in range(9)]

esconder_numeros = True
tabuleiro_preenchido = True
click_last_stat = False
click_pos_x = -1
click_pos_y = -1
numero = 0

def Tabuleiro_Hover(janela,mouse_pos_x,mouse_pos_y):
    celula = 66.7
    ajuste = 50
    x = (math.ceil((mouse_pos_x - ajuste) / celula) - 1)
    y = (math.ceil((mouse_pos_y - ajuste) / celula) - 1)
    pg.draw.rect(janela, branco, (0, 0, 1080, 720))
    if (x >= 0 and x <= 8 and y >= 0 and y <= 8):
        pg.draw.rect(janela, azul_claro, ((ajuste + x * celula, ajuste + y * celula, celula, celula)))

def Celula_Selecionada(janela, mouse_pos_x, mouse_pos_y, click_last_stat, click, x, y):
    celula = 66.7
    ajuste = 50
    if (click_last_stat == True and click == True):
        x = (math.ceil((mouse_pos_x - ajuste) / celula) - 1)
        y = (math.ceil((mouse_pos_y - ajuste) / celula) - 1)
    if (x >= 0 and x <= 8 and y >= 0 and y <= 8):
        pg.draw.rect(janela, azul, ((ajuste + x * celula, ajuste + y * celula, celula, celula)))
    return x, y

def Grade_Tabuleiro(janela):
    pg.draw.rect(janela, preto, (50, 50, 600, 600), 6)
    pg.draw.rect(janela, preto, (50, 250, 600, 200), 6)
    pg.draw.rect(janela, preto, (250, 50, 200, 600), 6)
    pg.draw.rect(janela, preto, (50, 117, 600, 67), 2)
    pg.draw.rect(janela, preto, (50, 317, 600, 67), 2)
    pg.draw.rect(janela, preto, (50, 517, 600, 67), 2)
    pg.draw.rect(janela, preto, (117, 50, 67, 600), 2)
    pg.draw.rect(janela, preto, (317, 50, 67, 600), 2)
    pg.draw.rect(janela, preto, (517, 50, 67, 600), 2)

def Novo_Jogo(janela):
    pg.draw.rect(janela, azul_petroleo, (750, 50, 250, 100))
    frase = fonte.render("Novo jogo", True, branco)
    janela.blit(frase, (795, 80))

def Linha_Escolhida(dado_tabuleiro, y):
    linha_escolhida = dado_tabuleiro[y]
    return linha_escolhida

def Coluna_Escolhida(dado_tabuleiro, x):
    coluna_escolhida = []
    for i in range(8): # 9 elementos da coluna
        coluna_escolhida.append(dado_tabuleiro[i][x])
    return coluna_escolhida

def Quadrante_Selecionado(dado_tabuleiro, x, y):
    quadrante = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrante.extend([dado_tabuleiro[0][0], dado_tabuleiro[0][1], dado_tabuleiro[0][2],
                          dado_tabuleiro[1][0], dado_tabuleiro[1][1], dado_tabuleiro[1][2],
                          dado_tabuleiro[2][0], dado_tabuleiro[2][1], dado_tabuleiro[2][2]])
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrante.extend([dado_tabuleiro[0][3], dado_tabuleiro[0][4], dado_tabuleiro[0][5],
                          dado_tabuleiro[1][3], dado_tabuleiro[1][4], dado_tabuleiro[1][5],
                          dado_tabuleiro[2][3], dado_tabuleiro[2][4], dado_tabuleiro[2][5]])
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrante.extend([dado_tabuleiro[0][6], dado_tabuleiro[0][7], dado_tabuleiro[0][8],
                          dado_tabuleiro[1][6], dado_tabuleiro[1][7], dado_tabuleiro[1][8],
                          dado_tabuleiro[2][6], dado_tabuleiro[2][7], dado_tabuleiro[2][8]])
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrante.extend([dado_tabuleiro[3][0], dado_tabuleiro[3][1], dado_tabuleiro[3][2],
                          dado_tabuleiro[4][0], dado_tabuleiro[4][1], dado_tabuleiro[4][2],
                          dado_tabuleiro[5][0], dado_tabuleiro[5][1], dado_tabuleiro[5][2]])
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrante.extend([dado_tabuleiro[3][3], dado_tabuleiro[3][4], dado_tabuleiro[3][5],
                          dado_tabuleiro[4][3], dado_tabuleiro[4][4], dado_tabuleiro[4][5],
                          dado_tabuleiro[5][3], dado_tabuleiro[5][4], dado_tabuleiro[5][5]])
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrante.extend([dado_tabuleiro[3][6], dado_tabuleiro[3][7], dado_tabuleiro[3][8],
                          dado_tabuleiro[4][6], dado_tabuleiro[4][7], dado_tabuleiro[4][8],
                          dado_tabuleiro[5][6], dado_tabuleiro[5][7], dado_tabuleiro[5][8]])
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrante.extend([dado_tabuleiro[6][0], dado_tabuleiro[6][1], dado_tabuleiro[6][2],
                          dado_tabuleiro[7][0], dado_tabuleiro[7][1], dado_tabuleiro[7][2],
                          dado_tabuleiro[8][0], dado_tabuleiro[8][1], dado_tabuleiro[8][2]])
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrante.extend([dado_tabuleiro[6][3], dado_tabuleiro[6][4], dado_tabuleiro[6][5],
                          dado_tabuleiro[7][3], dado_tabuleiro[7][4], dado_tabuleiro[7][5],
                          dado_tabuleiro[8][3], dado_tabuleiro[8][4], dado_tabuleiro[8][5]])
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrante.extend([dado_tabuleiro[6][6], dado_tabuleiro[6][7], dado_tabuleiro[6][8],
                          dado_tabuleiro[7][6], dado_tabuleiro[7][7], dado_tabuleiro[7][8],
                          dado_tabuleiro[8][6], dado_tabuleiro[8][7], dado_tabuleiro[8][8]])
        
    return quadrante


def Completa_Quadrante(dado_tabuleiro, x2, y2):


    def E_Valido(tabuleiro, x, y, numero):
        linha = Linha_Escolhida(tabuleiro, y)
        coluna = Coluna_Escolhida(tabuleiro, x)
        quadrante = Quadrante_Selecionado(tabuleiro, x, y)
        return tabuleiro[y][x] == "n" and numero not in linha and numero not in coluna and numero not in quadrante


    def Limpar_Quadrante(tabuleiro, x2, y2):
        for i in range(3):
            for j in range(3):
                dado_tabuleiro[y2 + i][x2 + j] = 'n'

    


    quadrante_preenchido = False
    loop = 0
    contador_try = 0
    numero = 1

    while not quadrante_preenchido:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        
        if E_Valido(dado_tabuleiro, x, y, numero):
            dado_tabuleiro[y][x] = numero
            numero += 1

        loop += 1

        if loop == 50:
            Limpar_Quadrante(dado_tabuleiro, x2, y2)
            loop = 0
            numero = 1
            contador_try += 1

        if contador_try == 10:
            break


        quadrante = Quadrante_Selecionado(dado_tabuleiro, x2, y2)
        if all(cell != "n" for cell in quadrante):
            quadrante_preenchido = True

    return dado_tabuleiro

def Reset_Dado_Tabuleiro(dado_tabuleiro):

    dado_tabuleiro = [["n" for _ in range(9)] for _ in range(9)]

    return dado_tabuleiro


def Verifica_Tabuleiro_Completo(dado_tabuleiro):
    for l in dado_tabuleiro:
        for numero in l:
            if numero == "n":
                return True
    return False




def Gabarito_Tabuleiro(dado_tabuleiro, tabuleiro_preenchido):

    while tabuleiro_preenchido:
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 0, 0)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 3, 0)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 6, 0)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 0, 3)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 3, 3)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 6, 3)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 0, 6)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 3, 6)
        dado_tabuleiro = Completa_Quadrante(dado_tabuleiro, 6, 6)

        for nn in range(9):
            for n in range(9):
                if dado_tabuleiro[nn][n] == "n":
                    dado_tabuleiro = Reset_Dado_Tabuleiro(dado_tabuleiro)
        cont = 0
        for nn in range(9):
            for n in range(9):
                if dado_tabuleiro[nn][n] != "n":
                    cont += 1
        if cont == 81:
            tabuleiro_preenchido = False
    return dado_tabuleiro, tabuleiro_preenchido



def Esconder_Numeros(dado_tabuleiro, dado_jogo, esconder_numeros):
    if esconder_numeros:
        for n in range(40):
            sorteando_numero = True
            while sorteando_numero == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if dado_jogo[y][x] == 'n':
                    dado_jogo[y][x] = dado_tabuleiro[y][x]
                    sorteando_numero = False
        esconder_numeros = False
    print (pd.DataFrame(dado_jogo))
    return dado_jogo, esconder_numeros

def Escrever_Numeros(window, jogo_data):
    quadrado = 66.7
    ajuste = 67
    cor_texto = preto
    cor_x = vermelho

    for nn in range(9):
        for n in range(9):
            if jogo_data[nn][n] != 'n':
                cor = cor_texto if jogo_data[nn][n] != "X" else cor_x
                palavra = fonte.render(str(jogo_data[nn][n]), True, cor)
                window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))

def Digitando_Numero(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero

def Checando_Numero_Digitado(tabuleiro_data, jogo_data, click_pos_x, click_pos_y, numero):
    x, y = click_pos_x, click_pos_y
    if 0 <= x <= 8 and 0 <= y <= 8:
        celula = tabuleiro_data[y][x]
    if numero != 0 and celula in (numero, 'n'):
        jogo_data[y][x] = numero
    elif numero != 0 and celula not in (numero, 'X'):
        jogo_data[y][x] = 'X'
    numero = 0
    return jogo_data, numero

def Click_Botao_Restart(mouse_pos_x, mouse_pos_y, click_last_stat, click, tabuleiro_preenchido, esconder_numeros, dado_tabuleiro, dado_jogo):
    x = mouse_pos_x
    y = mouse_pos_y
    if x >= 750 and x <= 1000 and y >= 50 and y <= 150 and click_last_stat == False and click == True:
        tabuleiro_preenchido = True
        esconder_numeros = True
        dado_tabuleiro = Reset_Dado_Tabuleiro(dado_tabuleiro)
        dado_jogo = Reset_Dado_Tabuleiro(dado_jogo)
    return tabuleiro_preenchido, esconder_numeros, dado_tabuleiro, dado_jogo






# Identificação de Mouse e Interações

continuar = True

while(continuar):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)

    mouse = pg.mouse.get_pos()
    mouse_pos_x = mouse[0]
    mouse_pos_y = mouse[1]

    click = pg.mouse.get_pressed()

#Jogo

    Tabuleiro_Hover(janela,mouse_pos_x,mouse_pos_y)
    click_pos_x, click_pos_y = Celula_Selecionada(janela, mouse_pos_x, mouse_pos_y, click_last_stat, click[0], click_pos_x, click_pos_y)
    Grade_Tabuleiro(janela)
    Novo_Jogo(janela)
    dado_tabuleiro, tabuleiro_preenchido = Gabarito_Tabuleiro(dado_tabuleiro, tabuleiro_preenchido)
    dado_jogo, esconder_numeros = Esconder_Numeros(dado_tabuleiro, dado_jogo, esconder_numeros)
    Escrever_Numeros(janela, dado_jogo)
    numero = Digitando_Numero(numero)
    dado_jogo, numero = Checando_Numero_Digitado(dado_tabuleiro, dado_jogo, click_pos_x, click_pos_y, numero)
    tabuleiro_preenchido, esconder_numeros, dado_tabuleiro, dado_jogo = Click_Botao_Restart(mouse_pos_x, mouse_pos_y, click_last_stat, click[0], tabuleiro_preenchido, esconder_numeros, dado_tabuleiro, dado_jogo)
    
   
    
    #Click Last Status

    if click[0] == True:
        click_last_stat = True
    else:
        click_last_stat = False

    pg.display.update()


