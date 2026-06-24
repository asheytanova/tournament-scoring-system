# 4 team spaces with max 5 people each
# 20 individual spaces
# 5 events chosen - team or individ
# Possibility of only one event entry
# Sport and academic challenges

# Points for first = 30 points
# Points for second = 25 points
# Points for third = 20 points
# Points for participants = 5 points

# Imports
import time

# Arrays
teams = {}
individuals = []
entries = {}
scores = {}
members = []
individual_entries = {}
team_entries = {}

# Predetermined values
# Sport events array - Made up with 10 Sports    
team_sports = ["Badminton", "Football", "Tennis", "Rugby", "Obstacle Course", "Cricket", "Karate", "Relay", "Basketball", "Volleyball"]
individual_sport = ["Badminton", "Tennis", "Karate", "Swimming", "Rounders", "Long Jump", "Obstacle Course", "Sprint", "Shotput", "Javelin"]

# Academic events array - Made up with 10 Academic Events
team_academic = ["Chess", "Reading", "Maths", "General Knowledge", "Spelling", "Debate", "Coding", "Talent Show", "Science Fair", "Poetry Competition" ]
individual_academic = ["Chess", "Reading", "Maths", "Backgammon", "Debate", "Coding", "Checkers", "Battleships", "Minesweeper", "Poetry Competition"]

# Team Reg
def teams_reg():
# Makes the members blank so only the curent team being inputteds' members are put in the array
    members = []

    if len(teams) == 4:
        print("Maximum number of teams exceeded.") 
# Ensures that the number of teams does not exceed the maximum specified on the client brief
        menu()

    else:
# Enters the 5 members required in each time according to the client brief
        teamName = str(input("Enter your team name: "))
        for i in range(0,5):
            memberName = input("Enter member no." + str(i+1) +": ")
            members.append(memberName)
# Puts the team name + the members of the team in the array                
        teams[teamName] = members

        print("Thank you for your entry!")

# Makes the score array for the team for later.
        scores[teamName] = 0


# Returns the user back to the menu to choose their next step    
        menu()
    
    


# Individual Reg
def individ():

    if len(individuals) == 20:
        print("Maximum number of teams exceeded.")
# Ensures that the number of individuals does not exceed the maximum specified on the client brief
        menu()

    else:
        individualName = str(input("Enter your name: "))
# Puts the name in the array                         
        individuals.append(individualName)

        print("Thank you for your entry!")

# Makes the score array for the individual for later.
        scores[individualName] = 0

# Returns the user back to the menu to choose their next step      
        menu()


# Participants
def partic():
    print()
    print("Teams:")
# Prints all the teams including their members
    for teamName in teams:
        print(teamName, "=")
        print(teams[teamName])

    print()

    print("Individuals:")
# Prints all the individuals 
    for i in range(len(individuals)):
        print(individuals[i])

# Returns the user back to the menu to choose their next step   
    menu()


# Event Entry
def event_menu():
    time.sleep(1)
    print()
    print("Event Entry Menu:")
    print("1. Team Event Entry")
    print("2. Individual Event Entry")
    print("3. Back to Menu")

    time.sleep (1)
    
# Selection of menu item
    print()
    select = int(input("Enter the number of the option you have chosen: "))
    
# Making the menu open the next chosen step  
    if select == 1:
        teams_event_entry()
        
    elif select == 2:
        individual_event_entry()
        
    elif select == 3:
        menu()

# Giving users infinite chances to enter the correct input 
    else:
        x = False
        while x == False:
            print()
            select = int(input("Please re-enter: "))
            if select == 1:
                teams_event_entry()
        
            elif select == 2:
                individual_event_entry()
        
            elif select == 3:
                menu()
 

def teams_event_entry():
    time.sleep(1)
    print()
    
    teamName = str(input("What is your team name: "))
    print()


    if teamName in teams:
        event = str(input("What type of events have you entered: sport, academic or both: "))
        event = event.lower().strip()
        print()
           
        if event == "sport":
           print("Sport Events:")
           print()
           for i in range(len(team_sports)):
               print(team_sports[i])
        
        elif event == "academic":
        
            print("Academic Events:")
            print()
            for i in range(len(team_academic)):
                print(team_academic[i])


        elif event == "both":
            print("Academic Events:")
            print()
            for i in range(len(team_academic)):
                print(team_academic[i])
            print()
            print("Sport Events:")
            print()
            for i in range(len(team_sports)):
                print(team_sports[i])

        else:
            print("Please try again")
            event_menu()

    elif teamName not in teams:
        print("Go enter your team.")
        menu()

    else:
        print("Invalid, please try again.")
        event_menu()

    print()

# Entering events
    eventNum = int(input("Would you like to enter 1 or 5 events: "))
    
    events = []
    
    if eventNum == 1:

        eventName = input("Enter event no.1: ")
        
        if eventName in team_academic or eventName in team_sports:
            events.append(eventName)

        else: 
            print("Please try again.")
            event_menu()

    elif eventNum == 5:
        for i in range(0,5):
            eventName = input("Enter event no." + str(i+1) +": ")
        
            if eventName in team_academic or eventName in team_sports:
                events.append(eventName)

            else: 
                print("Please try again.")
                event_menu()

    team_entries[teamName] = events

    menu()
    

def individual_event_entry():
    time.sleep(1)
    print()
    
    individualName = str(input("What is your name: "))
    print()

    #Displays the event options

    print()


    if individualName in individuals:
        event = str(input("What type of events have you entered: sport, academic or both: "))
        event = event.lower().strip()
           
        if event == "sport":
           print("Sport Events:")
           print()
           for i in range(len(individual_sport)):
               print(individual_sport[i])
        
        elif event == "academic":
            print("Academic Events:")
            print()
            for i in range(len(individual_academic)):
                print(individual_academic[i])


        elif event == "both":
            print("Sport Events:")
            print()
            for i in range(len(individual_sport)):
               print(individual_sport[i])

            print("Academic Events:")
            print()
            for i in range(len(individual_academic)):
                print(individual_academic[i])

        else:
            print("Please try again")
            event_menu()

    elif individualName not in teams:
        print("Go enter your team.")
        menu()

    else:
        print("Invalid, please try again.")
        event_menu()

    print()

    #Entering events
    eventNum = int(input("Would you like to enter 1 or 5 events: "))
    
    events = []
    
    if eventNum == 1:

        eventName = input("Enter event no.1: ")
        
        if eventName in individual_academic or eventName in individual_sport:
            events.append(eventName)

        else: 
            print("Please try again.")
            event_menu()

    elif eventNum == 5:
        for i in range(0,5):
            eventName = input("Enter event no." + str(i+1) +": ")
        
            if eventName in individual_academic or eventName in individual_sport:
                events.append(eventName)

            else: 
                print("Please try again.")
                event_menu()

    individual_entries[individualName] = events

    menu()

# Results
def results():
    entry = str(input("Are you a team or individual: "))
    entry = entry.lower().strip()
    
    if entry == "team":
        team_score_entry()    

    elif entry == "individual":
        indiv_score_entry()
    else:
        print("Invalid entry, please try again.")
        menu()
    
    menu()

def team_score_entry():
    score = 0
    teamName = str(input("Enter your team name: "))

    if teamName in team_entries:
        for i in range(len(team_entries[teamName])):
            place = int(input(f"What place did you come in {team_entries[teamName][i]}(Write as 1, 2, 3, etc.): "))
            if place == 1:
                scoreNum = 30

            elif place == 2:
                scoreNum = 25

            elif place == 3:
                scoreNum = 20

            else: 
                scoreNum = 5

            scores[teamName] = scores[teamName] + scoreNum
            score = scores[teamName]
    else:
        print("Please go enter your events.")
        menu()

    menu()
        

def indiv_score_entry():
    score = 0
    individualName = str(input("Enter your name: "))

    if individualName in individual_entries:
        for i in range(len(individual_entries[individualName])):
            place = int(input(f"What place did you come in {individual_entries[individualName][i]}(Write as 1, 2, 3, etc.): "))
            if place == 1:
                scoreNum = 30

            elif place == 2:
                scoreNum = 25

            elif place == 3:
                scoreNum = 20

            else: 
                scoreNum = 5

            scores[individualName] = scores[individualName] + scoreNum
            score = scores[individualName]
    else:
        print("Please go enter your events.")
        menu()
    menu()


# Leaderboard
def leaderboard():
    if len(scores) == 0:
        print("No scores have been inputted")
    
    else:
        winner = max(scores)
        sortedScores = sorted(scores.items(), key=lambda x: x[1], reverse = True)
        for i in range(len(sortedScores)):
            team = sortedScores[i][0]
            score = sortedScores[i][1]
            print(f"{i+1}. {team} - {score} points")

    menu()

# Exit
def exit():
    print()
    print("Thank you for using the college tournament scoring system!")

# Menu
def menu():
    print()
    time.sleep(2)
    print("Menu:")
    print("1. Team Registration")
    print("2. Individual Registration")
    print("3. Participants")
    print("4. Event Entry")
    print("5. Results Entry")
    print("6. Leaderboard")
    print("7. Exit System")
    time.sleep (2)
    
    # Selection of menu item
    print()
    select = int(input("Enter the number of the option you have chosen: "))
    
    
    if select == 1:
        teams_reg()
        
    elif select == 2:
        individ()
        
    elif select == 3:
        partic()
        
    elif select == 4:
        event_menu()
        
    elif select == 5:
        results()
    
    elif select == 6:
        leaderboard()
        
    elif select == 7:
        exit()
        
    else:
        # Forcing users to re-enter until a valid option is entered
        x = False
        while x == False:
            print()
            select = int(input("Please re-enter: "))

            if select == 1:
                x = True
                teams_reg()
        
            elif select == 2:
                x = True
                individ()
        
            elif select == 3:
                x = True
                partic()
        
            elif select == 4:
                x = True
                event_menu()
        
            elif select == 5:
                x = True
                results()
    
            elif select == 6:
                x = True
                leaderboard()
        
            elif select == 7:
                x = True
                exit()
            
            else:
                x = False


# Welcome Message
print("*********************************************************")
print("*                                                       *")
print("*                                                       *")
print("*   WELCOME TO THE COLLEGE TOURNAMENT SCORING SYSTEM    *")
print("*                                                       *")
print("*                                                       *")
print("*********************************************************")

# Start Program

menu()


