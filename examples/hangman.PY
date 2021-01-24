#
# Peter Jiang
# This is an updated version of the guess master 2.0.
#   This version creates a graphics window, for a more fun experience. You get 10 tries to guess the word
#   If you do not manage to guess the word, the game is over and you go back to just the welcome screen.
#   If you do guess the word, you get 10 extra score and a new word.
#   As an updated game, new changes include a hint button for the user, the ability to save
#   game scores and display game scores. Custom additions include a timer, , the ability to skip a word,
#   a potential to guess the entire word, and the ability to forfeit the game
#

'''
The three features added are a timer when it comes to choosing a guess, an option to straight up guess the word
and potentially earn 2 bonus points while if the guess is incorrect then you lose two polygons and lose 1 score,
and an option to skip the word up to three times per attempt. There is also a forfeit button which allows you to
give up and save your name with your current score.
'''


"""
this file and the score file is a demonstration of the graphics module
that you can reference

it will be removed just like the example plotly file
"""


from graphics import *
import random
from math import sqrt
#import needed libraries

def clicked_circle(point,circle):
    #define the click function
    px = point.getX()
    py = point.getY()
    #get x and y coordinates from the click
    cenC = circle.getCenter()
    #get center point from circle
    radi = circle.getRadius()
    # get radius from circle 
    cx = cenC.getX()
    cy = cenC.getY()
    #get x and y coordinates from circle
    if sqrt((px-cx)*(px-cx)+(py-cy)*(py-cy))< radi:
        #if the distance of point from center is less than radius return True
        return True
    return False
    #otherwise return false

def scrolling_scores(score_objects):
    #define the scolling scores function
    for x in range (0,len(score_objects),1):
        #loop through each of the score objects 
        score_objects[x].move(0,-2)
        #move the score object downwards to scroll
        if score_objects[x].getAnchor().getY() <= -10:
            #if the y coordinate of the center point of the score object is less
            #than or equal to -10, move the object to new y position
            score_objects[x].move(0,350)

            
def display_scores():
    #this function displays the top 7 scores
    infile = open ("scores.txt","r")
    lines = infile.readlines()
    #open and read the file that holds the scores
    for x in range (0,len(lines),1):
        #format the score data from the text file
        lines[x] = lines[x].strip()
        lines[x] = lines[x].split(",")
    used_lines = lines[0:7]
    #get the top 7 scores, which will be used
    score_win = GraphWin("High Scores",250,310)
    score_objects = []
    #create a list holding all the text objects that will be displayed
    label = Text(Point(125,30),"Player    Rounds  Score")
    label.setFace("courier")
    #courier sets all text to take the same width
    label.draw(score_win)
    #display in the score window
    score_objects.append(label)
    #add label to list of objects for the score window
    separater = Text(Point(125,45),"=-=-=-=-=-=-=-=-=-=-=-=")
    separater.setFace("courier")
    separater.draw(score_win)
    #create, format, and display the separator between the score label & scores
    score_objects.append(separater)
    #add separator to list of objects for the score window
    for x in range (0,len(used_lines),1):
        #append text objects displaying the 7 highest scores.
        string_used = used_lines[x][0].ljust(12)+used_lines[x][1].ljust(8)+used_lines[x][2].ljust(3)
        placehold = Text(Point(125,60+30*x),string_used)
        placehold.setFace("courier")
        placehold.draw(score_win)
        score_objects.append(placehold)
    #append all the format and the 7 highest scores to the objects list
    infile.close()
    #close the file
    return score_win,True,score_objects
    #return the score window, that there are scores (true), and score window objects

def insert_into(name,score,game_round):
    #define function for when additional scores are added to the game
    string_save = name+","+str(game_round)+","+str(score)+"\n"
    #create string of the user's name, played game rounds, and game score
    infile = open("scores.txt","r")
    raw_lines = infile.readlines()
    #open and read the file that holds the scores
    lines = []
    #create empty list for score data
    for x in range (0,len(raw_lines),1):
        #format the score data from the text file
        placehold = raw_lines[x].strip()
        lines.append(placehold.split(","))
        #append the text file data to list
    indexof = None
    for x in range (0,len(lines),1):
        #loop through the 
        if int(lines[x][2])<=score:
            #if the score of the user in the is less that the user's score change the index
            indexof = x
            break
            #exit loop
    try:
    #try to see if the new index and user data can be added into the original text file data
        raw_lines.insert(indexof,string_save)
    except:
    #if data cannot be added, only add user data to original text file data
        raw_lines.append(string_save)
    infile.close()
    #close the scores text file
    infile = open("scores.txt","w")
    written_string = ""
    #open scores text file to write in data
    for x in range (0,len(raw_lines),1):
        #loop through the updated score data and add to string of data to be written into file
        written_string += raw_lines[x]
    infile.write(written_string)
    #write in the updated score data into game score file
    infile.close()
    #close the game score text file


def check_box(point,square):
    #create a move function to call
    px = point.getX()
    py = point.getY()
    #get the x,y coordinates of click
    rp1 = square.getP1()
    rp2 = square.getP2()
    #get the two corner points of the square
    r1x = rp1.getX()
    r1y = rp1.getY()
    r2x = rp2.getX()
    r2y = rp2.getY()
    #get the x and y coordinates of the corner points
    if int(px) in range (int(r1x),int(r2x))and int(py) in range (int(r1y),int(r2y)):
        #check if the click is within the box
        return True
    return False
    #if click is not within the text box, return false

def insert_into(name,score,game_round):
    #function is used to insert the score into the right position so that the scores are saved highest
    #to lowest
    string_save = name+","+str(game_round)+","+str(score)+"\n"
    #create a string that will be appended to the score file
    infile = open("scores.txt","r")
    raw_lines = infile.readlines()
    #open and read the lines
    lines = []
    for x in range (0,len(raw_lines),1):
        placehold = raw_lines[x].strip()
        lines.append(placehold.split(","))
    indexof = None
    for x in range (0,len(lines),1):
        #if the score being saved is higher, it is placed right in front of the next highest score,
        #or a matching score
        if int(lines[x][2])<=score:
            indexof = x
            break
    try:
        #if the indexof is found, insert the line in
        raw_lines.insert(indexof,string_save)
    except:
        #if the score is lower than all previous scores, add it to the end.
        raw_lines.append(string_save)
    infile.close()
    #close the file
    infile = open("scores.txt","w")
    #open it again, but this time in writing mode
    written_string = ""
    for x in range (0,len(raw_lines),1):
        #rewrite the score file, this time with the inserted score
        written_string += raw_lines[x]
    infile.write(written_string)
    infile.close()
    #close the file again

def pick():
    # define the word picker function
    infile = open("./words.txt","r")
    lines = infile.readlines()
    #divide the lines read apart
    line = lines[random.randint(1,1200)]
    #pick a random line
    line = line.strip()
    #remove the \n at the end
    infile.close()
    #always close the file :)
    return line
    # return the random word



def guess(gc,sw,secret_word_object,window,placeholderword):
    #define the guess function
    y = 0
    for x in range (0,len(sw),1):
        if gc == sw[x]:
            try:
                #if the character is correct, draw each instance of the character
                secret_word_object[x].draw(window)
                y+=1
                placeholderword[x]=gc
            except GraphicsError:
                # if the object is already drawn, nothing happens now
                y+=1
    if y>0:
        return True
    return False
    
def box_center(box):
    # get and return the center of a rectangle
    x1 = (box.getP1().getX() + box.getP2().getX())/2
    y1 = (box.getP1().getY() + box.getP2().getY())/2
    return Point(x1,y1)


def welcome_setup() :
    main_win = GraphWin('Welcome to:',600,600)
    main_win.setBackground('grey70')
    #create the graphics window and set background to right color
    
    GM_rect = Rectangle(Point(0,0),Point(600,60))
    GM_rect.setFill('black')
    GM_rect.draw(main_win)
    #create and draw the border on the top of the welcome window
    
    intro_text = Text(Point(300,30),'GUESS MASTER 2.0')
    intro_text.setSize(30)
    intro_text.setStyle('bold')
    intro_text.setTextColor('gold')
    intro_text.draw(main_win)
    #create and draw the title 
    
    des_rect = Rectangle(Point(40,200),Point(560,380))
    des_rect.setFill('white')
    des_rect.draw(main_win)
    #create and draw the box in the middle where the description will go
    

    des_text1 = Text(Point(300,280),'This is a game where your score is\nbased on the number of 4-6 letter\nwords that you can guess within 10 tries.\nYou get 3 free word skips.')
    des_text1.setSize(19)
    des_text1.draw(main_win)
    #create and draw a text object that describes the game within the white box
    
    instruct_text = Text(Point(300,430),'Click NEW to start a game...')
    instruct_text.setSize(22)
    instruct_text.draw(main_win)
    #create and draw text object that tells user to click NEW in order to start a game
    

    new_rect = Rectangle(Point(37,100),Point(137,160))
    new_rect.setFill('gold')
    new_rect.draw(main_win)
    #create and draw a box that holds the new button
    
    hint_rect = Rectangle(Point(250,100),Point(350,160))
    hint_rect.setFill('red')
    hint_rect.draw(main_win)
    #create and draw a box that holds hint button

    hint_text = Text(Point(300,130),"HINT")
    hint_text.setSize(22)
    hint_text.draw(main_win)
    
    quit_rect = Rectangle (Point(463,100),Point(563,160))
    quit_rect.setFill('black')
    quit_rect.draw(main_win)
    #create and draw a box that holds the quit button

    new_text = Text(Point (87,130),'NEW')
    new_text.setSize(20)
    new_text.setStyle('bold')
    new_text.draw(main_win)
    #create and draw text object NEW that labels the box

    quit_text = Text (Point (513,130),'QUIT')
    quit_text.setStyle('bold')
    quit_text.setSize(20)
    quit_text.setFill('gold')
    quit_text.draw(main_win)
    #same as above except for the quit box

    score_rect = Rectangle(Point(200,500),Point(400,560))
    score_rect.setFill("green")
    score_rect.draw(main_win)

    score_text = Text(Point(300,530),"TOP SCORES")
    score_text.setStyle("bold")
    score_text.setSize(20)
    score_text.draw(main_win)
    
    objects = [new_rect,quit_rect,hint_rect,score_rect]
    #assign the two buttons to a single list
    return objects, main_win
    #return the buttons, as well as the main window


def game_set(score):
    secret_word = pick()
    #pick the secret word using the pick function
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #create and alphabet string as I'll need it to create the letter buttons later
    
    game_win = GraphWin('Save the Block P',600,600)
    game_win.setBackground('gold')
    #create the graphics window with the specified color

    counter=0
    #used for creating the secret word text object
    
    circlebutton = []
    text_button = []
    letter_holder = []
    printed_letter_box = []
    secret_word_ob = []
    #initialize lists that will contain 
    
    arrange_letter_box = [3,2,4,1,5,0,6]
    #this is the order that the letter boxes will be printed depending on length of secret word
    #this way it is more centered and won't be really off center if the word is short.
    
    for x in range (0,7,1):
        placehold = Rectangle(Point(90+60*x,60),Point(150+60*x,120))
        placehold.setFill('gold')
        letter_holder.append(placehold)
    #create the rectangles so letter holders

    
        
    for x in range (0,2,1):
        for y in range (0,13,1):
            circlebutton.append(Circle(Point(60+40*y,530+40*x),19))
    #create the circle buttons for letters
    
    for x in range (0,len(circlebutton),1):
        text_button.append(Text(circlebutton[x].getCenter(),alphabet[x]))
        text_button[x].setFill('white')
        circlebutton[x].setFill('black')
        circlebutton[x].draw(game_win)
    #create text objects at the center of each circle, corresponding to letters of the alphabet
    
    for x in range (0,len(text_button),1):
         text_button[x].draw(game_win)
    backgroundPs = []
    polygonPs = []
    #initiate lists for droppable polygons
    #need two so there is one in the back after the one in the front drops
    
    firstPoly = Polygon (Point(200,475),Point(210,435),Point(280,435),Point(270,475))
    polygonPs.append(firstPoly)
    backgroundPs.append(Polygon (Point(200,475),Point(210,435),Point(280,435),Point(270,475)))
    for x in range (0,4,1):
        polygonPs.append(Polygon(Point(220+10*x,435-70*x),Point(230+10*x,365-70*x),Point(280+10*x,365-70*x),Point(270+10*x,435-70*x)))
        backgroundPs.append(Polygon(Point(220+10*x,435-70*x),Point(230+10*x,365-70*x),Point(280+10*x,365-70*x),Point(270+10*x,435-70*x)))
        
    for x in range (0,2,1):
        polygonPs.append(Polygon(Point(300+50*x,225),Point(310+50*x,155),Point(360+50*x,155),Point(350+50*x,225)))
        backgroundPs.append(Polygon(Point(300+50*x,225),Point(310+50*x,155),Point(360+50*x,155),Point(350+50*x,225)))
        

    for x in range (0,2,1):
        polygonPs.append(Polygon(Point(340-10*x,295+70*x),Point(350-10*x,225+70*x),Point(400-10*x,225+70*x),Point(390-10*x,295+70*x)))
        backgroundPs.append(Polygon(Point(340-10*x,295+70*x),Point(350-10*x,225+70*x),Point(400-10*x,225+70*x),Point(390-10*x,295+70*x)))

        
    polygonPs.append(Polygon(Point(330,365),Point(340,295),Point(290,295),Point(280,365)))
    backgroundPs.append(Polygon(Point(330,365),Point(340,295),Point(290,295),Point(280,365)))
    #create all the polygons at the specified place

    for x in range (0,len(secret_word),1):
        letter_holder[arrange_letter_box[x]].draw(game_win)
        printed_letter_box.append(letter_holder[arrange_letter_box[x]])
    #append a number of letter boxes to the printed letter holder list, depending on length of secret word
    
    for x in range (3-int(len(secret_word)/2),3-int(len(secret_word)/2)+len(secret_word),1):
        secret_word_ob.append(Text(box_center(letter_holder[x]),secret_word[counter]))
        counter +=1
        #counter is used so that the secret word goes in order
        
    for x in range (0,len(polygonPs),1):
        backgroundPs[x].setFill('white')
        polygonPs[x].setFill('black')
        backgroundPs[x].draw(game_win)
        polygonPs[x].draw(game_win)
    #set the colors of the polygons, and draw them in order
        
    score_text = Text(Point(300,30),'Score:\t'+str(score))
    score_text.setSize(20)
    score_text.draw(game_win)
    #create and display the score in the game window
    return secret_word,polygonPs,circlebutton,text_button,printed_letter_box,secret_word_ob,game_win,score_text
    #return random words and graphics objects


def if_in_secret(alphabet,secret_word):
    #define function to compare letters in random word to alphabet for hint
    for ch in secret_word:
        #loop through the characters in the random/secret word
        if alphabet == ch:
            #if a character in the secret word matches to the alphabet return True
            return True
    return False
    #if none of the characters in the secret word are the alphabet return False

    
def drop(polygon):
    #function used to move the polygons downward until it is off the screen
    polygon.setFill('red')
    #change black polygon to red
    while polygon.getPoints()[0].getY()<670:
        #move the polygon off screen
        polygon.move(0,7)
        update(60)
        

def winning(game_win,third_loop):    
    # if the string is the same as the secret word, create objects that congratulate user
    congratulations = Text(Point(300,300),'YOU WIN - BOILER UP!')
    congratulations.setSize(28)
    congratulations.setFill('grey')
    congratulations.draw(game_win)
    #create and display congratulations message
    instruct_em = Text (Point (300,340),'click to continue')
    instruct_em.setSize(12)
    instruct_em.setFill('grey')
    instruct_em.draw(game_win)
    #create and display instructions for user to click window to continue
    wait = game_win.getMouse()
    game_win.close()
    #wait for mouse click and close game window
    third_loop=False
    return third_loop
    #set third_loop to False so new round starts

def losing(game_win,third_loop,second_loop,secret_word,score,game_round):
    #if all polygons fall, tell the user they lose
    congratulations = Text(Point(300,300),'The correct word was: '+secret_word)
    congratulations.setSize(28)
    congratulations.setFill('red')
    congratulations.draw(game_win)
    #tell the user the real word
    #the variable is set as congratulations because I copied from the winning function
    #and am too lazy to change it
    instruct_em = Text (Point (300,340),'Submit your name to continue')
    instruct_em.setSize(12)
    instruct_em.setFill('red')
    instruct_em.draw(game_win)
    #inform user to submit their name to continue
    entry_name = Entry(Point (300,200),20)
    entry_name.setFill("white")
    entry_name.draw(game_win)
    #create an entry box for the user
    submit_box = Rectangle(Point(250,50),Point(350,130))
    submit_box.setFill("black")
    submit_box.draw(game_win)
    #create a button to let user submit
    submit_text = Text(Point(300,90),"Submit\nName")
    submit_text.setSize(20)
    submit_text.setFill("gold")
    submit_text.draw(game_win)
    #label the box
    while True:
        #the program will stop until a name is submitted.
        click = None
        click = game_win.getMouse()
        if click !=None:
            if check_box(click,submit_box) == True:
                insert_into (entry_name.getText(),score,game_round)
                break
    
    return False,False
    # set third and second loop to false, so that the it returns to main loop, and game ends
    

def hint_button(incorrect,polygonPs,circlebutton,alphabet,secret_word,secret_word_ob,game_win,place_holder_word,remove_circle,remove_text,remove_alphabet,text_button):
    #define the function to give user a hint
    drop(polygonPs[incorrect])
    incorrect+=1
    drop(polygonPs[incorrect])
    incorrect +=1
    #cause the user to lose two polygons
    ridden1 = random.randint(0,len(circlebutton)-1)
    while if_in_secret(alphabet[ridden1],secret_word):
        ridden1 = random.randint(0,len(circlebutton)-1)
    ridden2 = random.randint(0,len(circlebutton)-1)
    while ridden2 ==ridden1 or if_in_secret(alphabet[ridden2],secret_word):
        ridden2 = random.randint(0,len(circlebutton)-1)
    ridden3 = random.randint(0,len(circlebutton)-1)
    while ridden3 == ridden2 or ridden3==ridden1 or if_in_secret(alphabet[ridden3],secret_word):
        ridden3 = random.randint(0,len(circlebutton)-1)
    #choose three random letters, that are not already chosen and also are incorrect
    guess(alphabet[ridden1],secret_word,secret_word_ob,game_win,place_holder_word)
    guess(alphabet[ridden2],secret_word,secret_word_ob,game_win,place_holder_word)
    guess(alphabet[ridden3],secret_word,secret_word_ob,game_win,place_holder_word)
    remove_circle.append(circlebutton[ridden1])
    remove_circle.append(circlebutton[ridden2])
    remove_circle.append(circlebutton[ridden3])
    circlebutton[ridden1].setFill("gold")
    circlebutton[ridden2].setFill("gold")
    circlebutton[ridden3].setFill("gold")
    remove_alphabet.append(alphabet[ridden1])
    remove_alphabet.append(alphabet[ridden2])
    remove_alphabet.append(alphabet[ridden3])
    text_button[ridden1].setFill("black")
    text_button[ridden2].setFill("black")
    text_button[ridden3].setFill("black")
    remove_text.append(text_button[ridden1])
    remove_text.append(text_button[ridden2])
    remove_text.append(text_button[ridden3])
    #change the color of the button and letter of the respective letteres
    return remove_text,remove_alphabet,remove_circle,incorrect
    #return remove_text,remove_alphabet,remove_circle,incorrect
    
def main():
    alphabet_string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet=[]
    for ch in alphabet_string:
        alphabet.append(ch)
    #create an alphabet reference

    buttons, welcome_win = welcome_setup()
    #create the welcome window and assign button objects to variable
    main_loop= True
    exist_scores =False
    score_win=None
    score_objects = []
    game_lost = False
    submit_button=None
    entry_name = None
    #initiate the main loop
    while main_loop==True:
        skip_words_remain = 3
        #set the number of skips the user has left to 3
        score=0
        #when a new game is started set score to 0
        if exist_scores ==True:
            #create the scrolling effect if the scores exist
            scrolling_scores(score_objects)
            #call the scrolling scores function
            click = score_win.checkMouse()
            if click != None:
                #let the scores continue to scroll unless there's a click
                score_win.close()
                exist_scores = False
        second_loop=False
        click=None
        click = welcome_win.checkMouse()
        game_round = 0
        #set game round to 0

        if click != None:
            if check_box(click,buttons[0])==True:
                second_loop=True
            # if the new button is clicked, initiate second loop
        
            if check_box(click,buttons[1])==True:
                welcome_win.close()
                return 5
            # if quit button is clicked, use return to end the function immediately after closing the window
            if check_box(click,buttons[3])==True:
                score_win,exist_scores,score_objects = display_scores()
            # if the hint button is clicked, call scores function
            
        while second_loop ==True:
            #second loop is for the duration of the game, and each iteration is a round
            game_round+=1
            #add 1 to game round to keep track of the current game round
            alphabet_string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            alphabet = []
            #remake the alphabet list
            for ch in alphabet_string:
                alphabet.append(ch)
            #count the number of rounds that have passed
            score +=10
            secret_word, polygonPs, circlebutton, text_button,printed_letter_box,secret_word_ob,game_win,score_text = game_set(score)
            third_loop = True
            incorrect=0
            #set incorrect number to 0

            place_holder_word=[]
            #empty out place holder list
            for ch in secret_word:
                place_holder_word.append('_')
            #place_holder allows me to create a word that I can compare to the secret word
            #hint_count = 0
            hint_used = False
            timed_out = 1
            'this is one of the additions to the program, the timer'
            #initiate timer
            timer_label = Text(Point(50,25),"Time Left")
            timer_label.setSize(17)
            timer_label.draw(game_win)
            #label the timer
            timer_text_count = 15
            timer_text = Text(Point(50,50),"15")
            timer_text.setSize(17)
            timer_text.draw(game_win)
            #create the actual timer
            guess_word_rect = Rectangle (Point(10,225),Point(80,275))
            guess_word_rect.setFill("black")
            guess_word_rect.draw(game_win)
            #create a box that lets the user guess the word directly
            guess_word_text = Text(Point(45,250),"Guess")
            guess_word_text.setFill("white")
            guess_word_text.setStyle("bold")
            guess_word_text.draw(game_win)
            #label the guess box
            guess_word_entry = Entry(Point(85,175),10)
            guess_word_entry.setSize(20)
            guess_word_entry.setFill("white")
            guess_word_entry.draw(game_win)
            #create an entry that allows the user to guess directly
            skip_word_rect = Rectangle(Point(90,225),Point(160,275))
            skip_word_rect.setFill("black")
            skip_word_rect.draw(game_win)
            #create a rectangle that allows the user to skip the word
            skip_word_text = Text(Point(125,250),"Skip")
            skip_word_text.setFill("white")
            skip_word_text.setStyle("bold")
            skip_word_text.draw(game_win)
            #label the skip box
            forfeit_rect = Rectangle(Point(450,150),Point(580,200))
            forfeit_rect.setFill("black")
            forfeit_rect.draw(game_win)
            #create a box that forfeits
            forfeit_text = Text(Point(515,175),"Forfeit")
            forfeit_text.setFill("white")
            forfeit_text.setStyle("bold")
            forfeit_text.draw(game_win)
            #label the forfeit
            
            while third_loop ==True:
                #third loop is the duration of each round, and a new loop starts each round
                if exist_scores ==True:
                    scrolling_scores(score_objects)

                remove_circle = []
                remove_alphabet = []
                remove_text = []
                #initiate place holders for parts of the lists that will be removed
                
               
                click = None
                # initialize by setting click to none
                click = welcome_win.checkMouse()
                if click != None:
                    # if there was a click in the main window,check if the clicks were on the buttons
                    if check_box(click,buttons[0])==True:
                        #check if there is a click in the New rectangle
                        game_win.close()
                        score = 0
                        third_loop=False
                    if check_box(click,buttons[1])==True:
                        #check if there is a click in the Quit rectangle
                        game_win.close()
                        welcome_win.close()
                        if exist_scores==True:
                            score_win.close()
                        return 10
                        # use return so that the main function ends immediately
                    if check_box(click,buttons[2])==True:
                        #check if there is a click in the Hint rectangle
                        if (incorrect <len(polygonPs)-2)and hint_used !=True:
                            #call the hint function if a hint hasn't been used and there are enough polygons to fall
                            remove_text,remove_alphabet,remove_circle,incorrect = hint_button(incorrect,polygonPs,circlebutton,alphabet,secret_word,secret_word_ob,game_win,place_holder_word,remove_circle,remove_text,remove_alphabet,text_button)
                            hint_used = True
                            #note that a hint was used
                    if check_box(click,buttons[3])==True:
                        #check if scores button was clicked in ctrol panel
                        score_win,exist_scores,score_objects = display_scores()

                    
                if click == None:
                    #if there was no click in the main window, check game window
                    click = game_win.checkMouse()
                    if click!= None:
                        if check_box(click,guess_word_rect)==True:
                            'this is one of the additions to the program, to fully guess the word'
                            #if the guess word rectangle is clicked, get the text inside the entry
                            #box and if it is the secret word then the user wins
                            if guess_word_entry.getText().upper()==secret_word:
                                third_loop = winning(game_win,third_loop)
                                score+=2
                                #if the word is correct the user gets 2 additional points
                            else:
                                #if the user guesses wrong, then they lose two polygons, and lose 1 score
                                drop(polygonPs[incorrect])
                                incorrect+=1
                                drop(polygonPs[incorrect])
                                incorrect+=1
                                score -=1
                                score_text.setText('Score:\t'+str(score))
                                #set the score text to the current score

                        'this is the one of the additions to the program, the skip ability'
                        if check_box(click,skip_word_rect)==True and skip_words_remain>0:
                            #if the skip box is clicked, then skip the current word, and the
                            #user gets no points. This only happens if the amount of skips the
                            #user has is more than 0
                            third_loop=False
                            game_win.close()
                            score-=10
                            skip_words_remain-=1
                            #subtract 1 from the remaining skips so the user
                        'this is the one of the additions to the program, the forfeit ability'
                        if check_box(click,forfeit_rect):
                            #if the forfeit button is clicked, immediately end the game and have the
                            #user submit their name and save it and their score into the score file
                            second_loop,third_loop = losing(game_win,third_loop,second_loop,secret_word,score,game_round)
                            game_win.close()
                            #call the losing function and close the window

                        click_button= False
                        # initialize as false, and if the click was on a button set to True
                        for x in range (0,len(circlebutton),1):
                            check_guess = clicked_circle(click,circlebutton[x])
                            #call the click function
                            timed_out =1
                            timer_text_count = 15
                            timer_text.setText(str(timer_text_count))
                            #set the timer text
                            if check_guess==True:
                                correct_guess = guess(alphabet[x],secret_word,secret_word_ob,game_win,place_holder_word)
                                # use guess function to return true or false to correct_guess
                                circlebutton[x].setFill('gold')
                                remove_circle.append(circlebutton[x])
                                text_button[x].setFill('black')
                                remove_text.append(text_button[x])
                                remove_alphabet.append(alphabet[x])
                                #change colors of clicked button
                                click_button = True
                                #confirm there was a click
                                
                        if click_button == True:
                            if correct_guess == False:
                                #if a button was clicked, but it was not correct, drop a polygon
                                drop(polygonPs[incorrect])
                                incorrect +=1
                                #add one to incorrect so program knows which polygon to drop
                                score -=1
                                # decrease score by 1
                                score_text.setText('Score:\t'+str(score))
                    if click == None and exist_scores ==True:
                        #check if the score window is open, and if it is check for a click
                        click = score_win.checkMouse()
                        if click!=None:
                            #if the window is clicked, close the score window
                            score_win.close()
                            exist_scores = False


                                
                if remove_circle !=[]:
                    for circle in remove_circle:
                        circlebutton.remove(circle)
                if remove_alphabet != []:
                    for letter in remove_alphabet:
                        alphabet.remove(letter)
                if remove_text != []:
                    for txt in remove_text:
                        text_button.remove(txt)
                #do not allow user to click the same option multiple times
                    
                compare_word = ''
                for x in range (0,len(place_holder_word),1):
                    compare_word+=place_holder_word[x]
                    # create a string to compare to the secret word
                    
                if compare_word == secret_word:
                    #if user gets the word call winning function 
                    third_loop = winning(game_win,third_loop)
                if incorrect ==len(polygonPs):
                    #if the polygons run out call losing function and close game win
                    second_loop,third_loop = losing(game_win,third_loop,second_loop,secret_word,score,game_round)
                    game_win.close()
                if timed_out%30 == 0:
                    timer_text_count -=1
                    timer_text.setText(str(timer_text_count))
                    #every second decrease the timer by 1
                if timed_out >451:
                    #if 15 seconds pass(timed out reaches 451) then the user loses a polygon
                    timed_out =0
                    drop(polygonPs[incorrect])
                    incorrect +=1
                    score -=1
                    #lose a score and a polygon
                    score_text.setText('Score:\t'+str(score))
                    #change the score counter
                    timer_text_count = 15
                    timer_text.setText(str(timer_text_count))
                    #reset the timer
                    
                timed_out +=1
                #each time the while loop refreshes add 1 to timed out
                update(30)
                #set refresh rate so that timer can work and the score window can scroll properly           

        update(30)
        #update the main function 30 times a second so the score window can scroll properly
        
main()
#call entire program
