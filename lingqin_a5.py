book_1 = {1: "Harry Potter and the Sorcerer's Stone"}
book_2 = {2: "Harry Potter and the Chamber of Secrets"}
book_3 = {3: "Harry Potter and the Prisoner of Azkaban"}
book_4 = {4: "Harry Potter and the Goblet of Fire"}
book_5 = {5: "Harry Potter and the Order of Phoenix"}
book_6 = {6: "Harry Potter and the Half Blood Prince"}
book_7 = {7: "Harry Potter and the Deathly Hallows"}
book_all = (book_1 | book_2 | book_3 | book_4 | book_5 | book_6 | book_7)
# "|" only works for python 3.9 and up to merge dictionaries)  
print ("\n#############################################") 
print ("Welcome to Know Your Harry Potter Book Series")
print ("#############################################")
choice = "notQ"
while (choice != "Q"):
    print ()
    for key in book_all:
        print (key, ':', book_all[key],"\n")
    book = input ("Which Harry Potter book is your favorite? (Enter 1 - 7): ")
    book = int (book)
    if (book >=1 and book <= 7):
        print ("\n""   ", book,":",book_all[book])
        print ("\nExcellent choice!")
        print (f"\nWhat happened to these Hogwarts students in book {book}?:",
" Harry   Hermione   Ron\n")
        name = input ("Type in the name of your favorite Hogwarts student to find out: ")
        story_1 = {"Harry":"got an invisible cloath.", "Hermione":"encountered a troll.", 
"Ron":"won a game in chess."}  
        story_2 = {"Harry":"met Tom Riddle through his diary.", "Hermione":"got petrified.", 
"Ron":"drove a flying car."}  
        story_3 = {"Harry":"warded off dementors.", "Hermione":"used Time Turner to study more.", 
"Ron":"found out more about his rat."} 
        story_4 = {"Harry":"entered the Triwizard Tournament.", "Hermione":"founded S.P.E.W.", 
"Ron":"asked Hermione to the Yule Ball."} 
        story_5 = {"Harry":"Lost his Godfather.", "Hermione":"co-founded Dumbledore's Army with Ron.", 
"Ron":"joined the Gryffindor Quidditch team."} 
        story_6 = {"Harry":"learned about Horcruxes.", "Hermione":"tried to make Ron jealous.", 
"Ron":"got poisoned."} 
        story_7 = {"Harry":"understood Prof. Snape's sacrifices.", 
"Hermione":"altered her parents' memories of her.", "Ron":"smashed the Horcrux locket."} 
        if (book == 1):
            print (f"\n    In book {book}, {name}", story_1[name])   
        if (book == 2):
            print (f"\n    In book {book}, {name}", story_2[name])
        if (book == 3):
            print (f"\n    In book {book}, {name}", story_3[name])
        if (book == 4):
            print (f"\n    In book {book}, {name}", story_4[name])
        if (book == 5):
            print (f"\n    In book {book}, {name}", story_5[name])
        if (book == 6):
            print (f"\n    In book {book}, {name}", story_6[name])
        if (book == 7):
            print (f"\n    In book {book}, {name}", story_7[name])
        choice = input ("\nWant to find out more about the Series? Enter Q to quit, or any other key to play again: ")
    else:
        print ("\n    Sorry. Wrong choice, try again:\n")
print ("\n    #############################")
print ("    Thank you and come back soon!")
print ("    #############################")