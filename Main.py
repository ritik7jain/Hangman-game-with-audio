#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
#print("Welcome to the RJ Gaming World")
#speak("Welcome to the RJ Gaming World") 
#print("This is the Brand New Game of RJ gaming world, in which you have to predict the name of bollywood movie,by guessing its letters,lets see it")
#speak("This is the Brand New Game of RJ gaming world, in which you have to predict the name of bollywood movie,by guessing its letters,lets see it")
#print("hey,Buddy you have to guess the movie Dil Bechara by guessing its letters like D , i , l like that")
#speak("hey,Buddy you have to guess the movie Dil Bechara by guessing its letters like D , i , l like that") 
#print("Want to play this Trending games")
speak("Enter your name")
k=input("Enter your name")
print("Hey {} Best of luck for the game".format(k))
speak("Hey {} Best of luck for the game".format(k))
#print("Here are some Of the rules")
#print("1. ")
ls=["dilbechara","kick","karanarjun","sooryavanshi","chichore","pink","ramleela","dilwale","golmal","lagaan","race"]
guess = random.choice(ls)
ls1=list(guess)
print(len(ls1))
ug=[]
g=[None]*len(ls1)
#at=len(ls1)
at=len(ls1)
for i in ls1:
    print("_",end=" ")
while True:
    speak("hey {} Enter a letter".format(k))
    p=input()
    if p in ug:
        print("hey {} you have Already Guessed it".format(k))
        speak("hey {} you have Already Guessed it".format(k))
        at=at-1
        if at>0:
            print("hey {} You have",at,"guesses left".format(k))
            speak("hey {} you have {} guesses left".format(k,at))
        else:
            print("Oops {} you loose the game".format(k))
            speak("oops {} you loose the game".format(k))
            break;     
    else:    
        ug.append(p)
        if p in ls1:
            print("Hurry {} Right Guess,Nice Play".format(k))
            speak("Hurry {} Right Guess,Nice Play".format(k))
            for i in range(len(ls1)):
                        if p == ls1[i]:
                            g[i]=p
            for i in g:
                if i==None:
                    print("_",end=" ")
                else:    
                    print(i,end=" ")
            print()
            if g==ls1:
                print("Hurry {} ,you won the game".format(k))
                speak("Hurry {} ,you won the game".format(k))
                break
        else:
            print("Wrong guess {} ".format(k))
            speak("Wrong guess {} ".format(k))
            at=at-1
            if at>0:
                print("You have",at,"guesses left")
                speak("hey {} you have {} guesses left".format(k,at))
            else:
                print("Oops {} you loose the game".format(k))
                speak("oops {} you loose the game".format(k))
                break;


# 
