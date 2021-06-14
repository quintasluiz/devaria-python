def ficha(jog, gol):
    print(f'O jogador {jog} fez {gol} gol no campeonato')

#Programa principal
n = str(input('Nomedo jgador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)