import random

SCELTE = ['carta', 'forbice', 'sasso']
vittorie_pc = 0
vittorie_giocatore = 0

def partita(i, nome_giocatore):
    scelta_valida = False
    print(f'Partita n{i+1}')
    print(f'{nome_giocatore}, scegli carta forbice o sasso')

    scelta_giocatore = input()

    while not scelta_valida:
        if scelta_giocatore.lower() not in SCELTE:
            print('Scelta non valida')
            print('Per favore digita Carta, Forbice o Sasso')
            scelta_giocatore = input()
        else:
            scelta_valida = True
    if scelta_giocatore.lower() in SCELTE:
        gioca(scelta_giocatore)


def scelta_pc():
    numero_casuale = random.randint(1, 3)
    if numero_casuale == 1:
        return 'carta'
    elif numero_casuale == 2:
        return 'forbice'
    elif numero_casuale == 3:
        return 'sasso'
    else:
        return 'sasso'
    

def gioca(scelta_giocatore):
    global vittorie_pc, vittorie_giocatore 
    scelta_computer = scelta_pc()
    print(f'La scelta del computer è {scelta_computer}')
    if scelta_giocatore.lower() == scelta_computer:
        print('Pareggio')
    elif scelta_giocatore.lower() == 'carta' and scelta_computer == 'forbice':
        print('Hai perso')
        vittorie_pc = vittorie_pc + 1
    elif scelta_giocatore.lower() == 'forbice' and scelta_computer == 'sasso':
        print('Hai perso')
        vittorie_pc = vittorie_pc + 1
    elif scelta_giocatore.lower() == 'sasso' and scelta_computer == 'carta':
        print('Hai perso')
        vittorie_pc = vittorie_pc + 1
    else:
        print('Hai vinto')
        vittorie_giocatore = vittorie_giocatore + 1

# ----------------------------- Inizio esecuzione 
print('Benvenuto in carta forbici sasso')
nome_giocatore = input('Digita il tuo nome: ')

while True:
    try:
        n = int(input('Digita il numero di partite: '))
        break
    except ValueError:
        print("Per favore, inserisci un numero intero valido.")

for i in range(n):
    partita(i, nome_giocatore)

if vittorie_giocatore > vittorie_pc:
    print(f'Hai vinto {vittorie_giocatore} partite su {n}')
elif vittorie_giocatore > vittorie_pc:    
    print(f'Hai perso {vittorie_pc} partite su {n}')
else:
    print(f'Hai pareggiato {n} partite')

