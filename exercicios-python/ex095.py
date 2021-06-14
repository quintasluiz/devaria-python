time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Qunatas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantod gols na partida {c}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
         resp = str(input('Quer continuar? [S/N]')).upper()[0]
         if resp in 'SN':
             break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' *30)
print('cod', end='')
for i in jogador.keys():
    print(f'{k:>3} ', end='')
    print()
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)