import random

zahl = random.randint(1,100)
versuche = 5
nachrticht = ''
print('''Hey du, Willst du ein cooles Spiel mit mir Spielen?
Ich denke mir eine Zahl zwischen 1-100 aus und du muss sie schätzen.
Du hast nur 5 Versuche.
Lass uns anfangen! (⌐■_■)''')
while versuche > 0:

  schaetzen = int(input('Gib deine Zahl ein:'))
  if schaetzen == zahl:
   nachrticht = '''
Wow! Genau das ist es!! Du hast das Spiel gewonnen und somit unseren Repsekt. ༼ ▀̿̿Ĺ̯̿̿▀̿ ༼▀̿̿Ĺ̯̿̿▀̿༽▀̿̿Ĺ̯̿̿▀̿ ༽
   '''
   break

  elif schaetzen > zahl:
    print(f'''
{schaetzen} ist zu groß. Versuch es mal mit eine kleinere Zahl. ┗(▀̿ĺ̯▀̿ ̿)┓ \nVerbleibende Versuche: {versuche-1}.
    ''')
    versuche -= 1
  elif schaetzen < zahl:
    print(f'''
{schaetzen} ist zu klein. Versuch es mal mit eine großere Zahl. ┗(▀̿ĺ̯▀̿ ̿)┓ \nVerbleibende Versuche: {versuche-1}.
    ''')
    versuche -= 1
  else:
    print('Hopla etwas ist schiefgelaufen. Bitte Starten Sie das Program neu.')
    break

print(nachrticht)