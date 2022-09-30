import random



print('''Welcome to H.A.N.G.M.A.N Game By VIVEK_DHOK    
              +------+ 
              |      |
              O      |
             /|\     |
             / \     |
           ===========
                         ''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


Fruits=["apple","mango","watermelon","lemon","banana","lemon","strawberry","dragonfruit","pineapple","orange","kiwi","papaya","grape","cherry"]
word=random.choice(Fruits)
len_word=len(word)
lives=6



display=[]

for _ in range(len_word):
    display+="_"


end_of_game=False

while not end_of_game:
    guess=input("Guess The Fruit letter :- ").lower()

    for position in range(len_word):
        letter=word[position]
        if letter==guess:
            display[position]=letter

    print(f"\nYour Word is :-  {''.join(display)}")
    
    
    if guess not in word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("\nOops You Lose The Game ")
            print(f"\nThe Real Word is {word}")
    

    if "_" not in display:
        end_of_game=True
        print("\nCongratulations You Win ")

    print(stages[lives])



