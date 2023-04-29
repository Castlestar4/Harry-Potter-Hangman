from random import randint
hangmanPics = ['Oh no',

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""]
print ('Do you want to play harry potter hangman?')
play = input()
while play == 'y' or play == 'Y' or play == 'yes' or play == 'Yes':
  print ('YAY! Let\'s play!')
  name = input('What is your name: ')
  from time import sleep
  sleep(1)
  print ('I\'m going to pick a character from Harry Potter')
  Words = ['ronweasley', 'harrypotter', 'hermionegranger', 'lunalovegood', 'remuslupin', 'siriusblack', 'nevillelongbottom', 'rubeushagrid', 'ginnywealsey', 'albusdumbledore', 'severussnape', 'tomriddle', 'voldemort', 'lavenderbrown', 'peterpettigrew', 'jamespotter', 'lilypotter', 'fredweasley', 'minervamcgonagall', 'dracomalfoy', 'cedricdiggory', 'nymphadoratonks', 'georgeweasley', 'dobbythehouseelf', 'bellatrixlestrange', 'hedwig', 'chochang', 'doloresumbridge', 'fleurdelacour', 'victorkrum', 'gilderoylockhart', 'alastormoody', 'argusfilch', 'horaceslughorn', 'moaningmyrtle', 'sybilltrelawney', 'filiusflitwick', 'seamusfinnigan', 'oliverwood', 'pansyparkinson', 'ritaskeeter', 'newtscamander', 'kreacher', 'deanthomas', 'fredweasley', 'mollyweasley', 'arthurweasley', 'percyweasley']
  word = Words[randint (1, len(Words))]
  letters = []
  userview = []
  guessed = []
  for i in range (len(word)):
    letters.append(word[i])
    userview.append('_')
  lives = 9
  count = 0
  while count < (len(word)) and lives != 0:
    print ('')
    print ('')
    print (userview)
    sleep (1)
    print ('You have', (lives), 'lives')
    print ('already guessed: ')
    print (guessed)
    sleep (1)
    print ('Guess a letter')
    correct = 2
    done = 2
    guess = input()
    print ('')
    if len(guessed) > 0:
      for i in range (len(guessed)):
        if guessed[i] == guess:
          print ('you\'ve done this letter')
          done = 1
    if done == 2:
      for i in range (len(word)):
        if guess == word[i]:
          userview[i] = guess
          count += 1
          correct = 1
          print ('YES!')
      if correct == 2:
        print ('no :(')
        print (hangmanPics[9-lives])
        lives -= 1
    guessed.append(guess)
  if count == len(word):
    score = lives * 3
    print (userview)
    print ('Well done!')
    print ('Your score was', score)
  if lives <= 0:
    score = 0
    print ('Out of lives :(')
    print ('correct answer: ')
    print (letters)
  text_file = open('hangman.txt', 'a')
  text_file.write (name + ' - ' + str(score))
  text_file.write ('\n')
  text_file.close ()
  print ('play agin?')
  play = input()
print ('Bye!')
