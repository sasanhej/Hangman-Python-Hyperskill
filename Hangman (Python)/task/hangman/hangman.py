import random
win=0
lost=0
while True:
    print("H A N G M A N\n")
    menu=input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu not in ["play","results","exit"]:
        continue
    if menu=="play":
        words="python","swift","java","javascript"
        word=random.choice(words)
        prompt=list(len(word)*"-")
        lives=8
        before=set()
        while lives>0:
            letter=input("".join(prompt)+"\n"+"Input a letter:")
            if len(letter)!=1:
                print("Please, input a single letter.")
                continue
            elif letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            elif letter in before:
                print("You've already guessed this letter.")
                continue
            for j in range(len(list(word))):
                if list(word)[j]==letter:
                    prompt[j]=letter
            if letter not in word:
                print("That letter doesn't appear in the word.")
            if (letter not in word) or (letter in before):
                lives-=1
            if "-" not in prompt:
                print("You guessed the word {}!\nYou survived!".format(word))
                win+=1
                break
            before.add(letter)
            print("Lives remaining: ",lives)

        if lives==0:
            print("You lost!")
            lost+=1
    elif menu=="results":
        print("You won: {} times.\nYou lost: {} times.".format(win,lost))
    elif menu=="exit":
        break

