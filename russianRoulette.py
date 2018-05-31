from random import randint
print ('\nWelcome to Russian Roulette 1.0\n   ©2017 Giacomo Scarabicchi')
print ('''          _=___________________________-_
    =< '   | ========|___________________
      \|   | ========|___________________
      /    | ========|/
     |     | ========|'
     |______| ________'
    '.... /  |  
   |......|  \\
   |......|   \\
   |......|
  '.......|
  |.......|
  |_______)''')
selection = 'y'
while selection == 'y':
  while True:
    while True:
      bullets = input('\nInsert the number of bullets to use:')
      if bullets.isdigit() == False:
        print ('\nYou need to insert a number!')
      else:
        break
    bullets = int(bullets)
    if bullets > 6:
      print ('\nToo many bullets! This is a six-shot Bodeo revolver!')
    elif bullets == 0:
      print('\nThat\'s too easy, isn\'t it?\n\nNow you have to play, you can\'t back out...')
    else:
      break
  input('\nPress enter to spin the cylinder')
  print('\n.....trrrrrrr.....')
  result = randint(0, 6 - bullets)
  input('\nPress enter to aim at your head')
  input('\nPress enter to pull the trigger\n\nTake your time')
  if result == 0:
    print('\n\nBAAAANNNNNGGGGG!!!!!!\n\n\nYou\'re dead.\n')
  else:
    print('\n\n\nCLICK!\n\n\n\nFiuuuu, that was a close one!\n')
  selection = input('\nDo you want to play again? y/n')
  while selection != 'y' and selection != 'n':
    selection = input('\nDo you want to play again? y/n')
print('\n\nBye!\n\n')