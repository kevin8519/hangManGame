decision=True

while decision:

    import random
    import time
    
    HANGMANPICS=['''

    +---+
    |   |
        |
        |
        |
        |
     =========''','''

    +---+
    |   |
    O   |
        |
        |
        |
     =========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
     =========''','''
    +---+
    |   |
    O   |
    /|  |
        |
        |
     =========''','''
    +---+
    |   |
    O   |
    /|\ |
        |
        |
     =========''','''
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
     =========''','''
    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
     =========''']


    words='''ant baboon badger bat bear beaver camel cat clam cobra cougar
    coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion
    lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon
    python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake
    spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat
    zebra'''.split()
    time.sleep(3)

    
    print(" the game start")
    secret_lettr=""
    def selection(wordf):

        wordindex=random.randint(0,len(wordf)-1)
        return wordf[wordindex]

        
    secret_lettr=selection(words)
    time.sleep(3)
    

    def initdisplay(secretletter):
            time.sleep(2)
            blanks='-'*len(secretletter)
            hangpictindex=len(HANGMANPICS)
            print (blanks)
            print("it is a %d letter word" %len(secretletter))
            time.sleep(2)
            print(HANGMANPICS[0])

    initdisplay(secret_lettr)

    def call(secretletter):
       num=0
       store=[]
       print("enter only alphabets")
       
       indata=input("enter the letter")
       for i in range(0,len(secretletter)):
            for z in range(0,1):
                
                if secretletter[i]==indata :
                 
                    store.append(str(i))
                    
                    
                    print (store)  
                          


                    num=num+1
                else:
                    num=num
       for j in store:
                             
            print (" the guesed element at these positions",j)
   
       return num,indata




    def guess(secretletter):
        flag=True
        correctentry=0
        wrongentry=0
        correctresult=""
        while flag:
            x,z=call(secret_lettr)
        
            strsecretletter=str(secretletter)
            length=len(strsecretletter)
        
        
        
            if x >=1:
                
                 correctentry+=1
                 correctresult=correctresult+z
                 if correctresult==strsecretletter:
                       print (" you are winner and took and the guessed letter is ", strsecretletter)
                       flag=False
                       break
                 elif correctresult!=strsecretletter and len (correctresult)==len(strsecretletter):
                       print (" you are also awinner and took and the guessed letter is ", strsecretletter)
                       flag=False
                       break
                 else:
                        continue  
          
            elif x==0:
          
                wrongentry=wrongentry+1
                time.sleep(2)
                print (" entry not matching")
                hang_counter=len(HANGMANPICS)
                if wrongentry < hang_counter-1:
                        time.sleep(1)
                        print(HANGMANPICS[wrongentry])
                        continue
                elif wrongentry == hang_counter-1:
                        time.sleep(5)  
                        print ("last chance, guess well")   
                        print(HANGMANPICS[wrongentry])   
                        continue    
                elif wrongentry == hang_counter:
                        print (" you are looser and the guessed letter is ", strsecretletter)
                        print ("game over")
                        flag=False 
                        break
                  
                       
           
                

            
            
            

    guess(secret_lettr)                           
    print ("Do you want to play again")
                
    print ( "press yes or y to play again and No or n to quit")

    play=input('enter you interest>')
    if play=='y' or play=='yes' :

        decision=True

    elif play=='n' or play=='no' :

        decision=False

    else:
    
      print ( "wrong key pressed")
    
      decision=False
    
    
