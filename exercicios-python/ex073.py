times = ('Corinthians','Palmeiras', 'Santos', 'Gremio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico MG','Botafogo','Atletico PR','Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitoria',
         'Coritiba', 'Avai','Ponte Preta', 'Atletico Go')

print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
                                                                     #for t in times:
print(f'Os 5 primeiros são {times[0:5]}')
print( '-=' * 15 )
print(f'Os 4 ultimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O chapecoense está na {times.index("Chapecoense") +1}ª posição')
