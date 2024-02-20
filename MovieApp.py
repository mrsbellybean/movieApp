import datetime
from datetime import datetime

import random
from datetime import date, datetime

import string

global actorsList
actorsList = {} 

global movieList
movieList = {}

ID_list = []

class MovieClass():

    def __init__ (self):       
        self.title = ""     #Initialise all the variables for the class file
        self.year = ""
        self.genre = ""
        self.dateReleased = None    #initialised as none so that when dateReleased is entered in the main class, it can be stored as datetime
        self.ID = random.randint(1000,9999)
        pass

#Getters and setters
        
    def setMovieTitle (self, title):        #Set all the object attributes from the user input parameters
        self.title = title
    def setMovieYear (self, year):
        self.year = str(year)
    def setMovieGenre (self, genre):
        self.genre = genre
    def setDateReleased (self, dateReleased):
        try:
            # Check if dateReleased is a datetime object
            if isinstance(dateReleased, datetime):
                self.dateReleased = dateReleased
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
    #Unique ID generator
    
    def setID(self):
        def generate_id():
            generate_id = ''.join(random.choice(string.digits) for n in range(4))
            return generate_id
        id = generate_id()
        while id not in ID_list:
            ID_list.append(id)
        else:
            id = generate_id()
            
        self.ID = id #Generate a random 4 digit ID number for the movie 


    def getMovieTitle (self):   #Retrieve object attributes
        return self.title
    def getMovieYear (self):
        return self.year
    def getMovieGenre (self):
        return self.genre
    def getDateReleased (self):
        return self.dateReleased
    def getID (self):
        return self.ID
    
    def displayDetails(self):       #Display the movie details for the current movie object
        print ("Movie Details:")
        print ("Title: ", self.title)
        print ("Year: ", self.year)
        print ("Genre: ", self.genre)
        print ("Date released: "+ self.dateReleased.strftime("%d %B %Y")) #Convert the date, eg. from '1990,12,03' to '3 December 1990'
        print ("Movie ID: ", self.ID)

    def addToMovieList(self):
        #ml = MovieListClass()
        try:
            # Check if the movie object has the necessary attributes
            if hasattr(self, 'title') and hasattr(self, 'year') and hasattr(self,'genre') and hasattr(self,'dateReleased'):
                movieList[self.title] = [self.title, self.year, self.genre, self.dateReleased, self.ID]        #Add the movie to the dictionary with the title as the key
            else:
                print("Invalid movie object. It should have the following attributes: title, year, genre and release date")
        except Exception as e:
            print(f"An unexpected error occurred while adding the movie to the list: {e}")

#global movieList #Make movieList a global variable so it doesn't need to be accessed from a specific class


class MovieListClass():

    def __init__(self):
        print("Hello")
        pass
        
    def printMovieList(self):
        #pprint.pprint(movieList) #Print out the dictionary of movies in a pretty print format
        for movie in movieList:
            print ("Movie ", movieList[movie][0])
            print ("Title: ", movieList[movie][0]) #Access the dictionary movie index 0 for title
            print ("Year: ", movieList[movie][1])
            print ("Genre: ", movieList[movie][2])
            print ("Date released: ", movieList[movie][3].strftime("%d %B %Y")) #Convert the date, eg. from '1990,12,03' to '3 December 1990'
            print ("Movie ID: ", movieList[movie][4])
    
    def displayDetails(self, i):       #Display the movie details for the current movie object
        print ("Movie Details:")
        print ("Title: ", movieList[i][0]) #Access the dictionary movie index 0 for title
        print ("Year: ", movieList[i][1])
        print ("Genre: ", movieList[i][2])
        print ("Date released: ", movieList[i][3].strftime("%d %B %Y")) #Convert the date, eg. from '1990,12,03' to '3 December 1990'
        print ("Movie ID: ", movieList[i][4])

    def searchMovie(self):
        choicelist = ["title", "year", "genre", "date (format yyyy, mm, dd)", "ID"]
        print("Enter the number of the attribute you wish to search for: ")
        print("1: Movie Title")
        print("2: Movie Year")
        print("3: Movie Genre")
        print("4: Movie Date")
        print("5: Movie ID")
        choice = input()
        choice = int(choice) - 1
        while True:
            result = []
            try:
                attribute = input("Enter the " + choicelist[choice] + " you'd like to search for:   ")
                for movie in movieList:
                    if movieList[movie][choice] == attribute:
                        result.append(movie)
                for value in result:
                    self.displayDetails(value)
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                searchagain = input("That wasn't found. Search again? Press y or n")
                if searchagain == 'y':
                    continue
                else:
                    break
                 

    def removeMovie(self):
        try:
            movieremove = input("What movie would you like to remove from the list?   ")    #User inputs the title of the movie they wish to remove
            movieList.pop(movieremove)          #Since movieList uses titles as keys, the movie can be popped from the dictionary by using its title
        except KeyError:
            print(f"Movie with title '{movieremove}' not found in the list.")

    def movieCount(self):
        return len(movieList)       #Generate the number of entries in the dictionary and store it as movieCount
    
    def getMovieDetails(self, title):
        try:
            for movie in movieList:
                if movieList[movie][0] == title:
                    return self.displayDetails(title)
            print(f"Movie with title '{title}' not found in the list.")
        except Exception as e:
            print(f"An unexpected error occurred while getting movie details: {e}")    #Retrieve movieList entry by its title

    def movielistmenu(self):
            while True:
                print("Welcome to the movie list menu!")
                print("Movie List Menu")
                print("1: Display movie list")
                print("2: Search for a movie")
                print("3: Remove a movie from the list")
                print("4: Count the number of movies in the list")
                print("5: Get movie details")
                print("6: Return to the main menu")
                try:
                    choice = input("Enter your choice (1-6):\n")
                    if choice == '1':
                        self.printMovieList()
                        break

                    elif choice == '2':
                        self.searchMovie()
                        break

                    elif choice == '3':
                        self.removeMovie()
                        break

                    elif choice == '4':
                        print(f"Number of movies in the list: {self.movieCount()}")
                        break

                    elif choice == '5':
                        title = input("Please enter the title of the movie you'd like to see details for:\n")
                        print(self.getMovieDetails(title))
                        break

                    elif choice == '6':
                        print("Taking you back to the main menu...")
                        Main.run()
                except:
                    print("Please enter a number from the menu:\n")
                    continue

class ActorsClass():
    def __init__(self):
        self.firstName = ""
        self.surname = ""
        self.dateOfBirth = None #initialised as none so that when dateOfBirth is entered in the main class, it can be stored as datetime
        self.gender = ""
        pass
    
    def setfirstName(self, firstName):         #Set all the object attributes from the user input parameters
        self.firstName = firstName
    def setSurname(self, surname):
        self.surname = surname
    def setDateofBirth(self, dateOfBirth):
        try:
            # Check if dateReleased is a datetime object
            if isinstance(dateOfBirth, datetime):
                self.dateOfBirth = dateOfBirth
        except Exception as e:
            print(f"An unexpected error occurred: {e}")     
    def setGender(self, gender):
        self.gender = gender
    def setFullName (self, fullname):
        self.fullname = fullname


    def getFirstName(self):                 #Retrieve object attributes
        return self.firstName
    def getsurname(self):
        return self.surname
    def getDateOfBirth(self):
        return self.dateOfBirth
    def getGender(self):
        return self.gender
    def getFullName(self):
        return self.fullname
    
    def displayActorDetails(self):          #Display the actor details for the current actor object
        print ("Actor Details:")
        print ("Name: ", self.firstName, self.surname)
        print ("Birthday: ", self.dateOfBirth.strftime("%d %B %Y"))     #Convert the date, eg. from '1990,12,03' to '3 December 1990'
        print ("Gender: ", self.gender)

    def addToActorsList(self):
        #al = ActorsListClass()
        try:
            if hasattr(self, 'fullname') and hasattr(self, 'firstName') and hasattr(self, 'surname') and hasattr(self,'dateOfBirth') and hasattr(self,'gender'):
                actorsList[self.fullname] = [self.firstName, self.surname, self.dateOfBirth, self.gender]   #Add the actor to the actorsList dictionary with their fullname as the key
            else:
                print("Invalid actor object. It should have the following attributes: first name, surname, date of birth and gender")
                # Check if the actor object has the necessary attributes           
        except Exception as e:
            print(f"An error occurred while adding the movie to the list: {e}")

class ActorsListClass():
    def __init__(self):                            
        print("Hello")
        pass
  
    def printActorsList(self):
        for actor in actorsList:
            print ("Actor ", actorsList[actor][0])
            print ("First Name: ", actorsList[actor][0]) #Access the dictionary movie index 0 for title
            print ("Surname: ", actorsList[actor][1])
            print ("Date of Birth: ", actorsList[actor][2])
            print ("Gender: ", actorsList[actor][3].strftime("%d %B %Y")) #Convert the date, eg. from '1990,12,03' to '3 December 1990'
            
    def removeActor(self):
        removename = input("Enter the name of the actor you wish to remove")
        new_list = []
        for actor in actorsList:                            #To delete an actor by their first name, the system must inform users of several actors with the same first name
            if removename!= actorsList[actor][0]:           #Populate new_list with all the actors that do not have the entered name 
                new_list.append(actorsList[actor][0])
        if len(new_list)== len(actorsList):                 #If none of the entries have the entered first name, then new_list will have the same no. of entries as actorsList
            print("No actor with the first name {removename} found.")
        elif (len(actorsList)-len(new_list)) == 1:          #This means that one entry had the entered first name
            print ("There is one actor with that first name. This actor will be deleted...")
            name = new_list[0]
            actorsList.pop(name)
        elif (len(actorsList)-len(new_list)) > 1:              #This means that some entries had the entered first name
            print("There are multiple actors with that first name. All of which will be deleted...")
            name = new_list[0]
            actorsList.pop(name)

    def displayActorDetails(self, i):          #Display the actor details for the current actor object
        print ("Actor Details:")
        print ("Name: ", actorsList[i][0], actorsList[i][1])            #Access the dictionary actor index 0 for first name and index 1 for surname
        print ("Birthday: ", actorsList[i][2].strftime("%d %B %Y"))     #Convert the date, eg. from '1990,12,03' to '3 December 1990'
        print ("Gender: ", actorsList[i][3])

    
    def countActors(self):
        return len(actorsList)      #Get the number of entries in the actorsList dictionary and save this number as the actors count

    def searchActor(self):
        choicelist = ["firstname","surname","date of birth (format yyyy,mm,dd)","gender"]
        print("Enter the number of the attribute you wish to search for: ")
        print("1: Actor Firstname")
        print("2: Actor Surname")
        print("3: Actor Date of Birth")
        print("4: Actor Gender")
        choice = input()
        choice = int(choice)-1      #Get the index to search for, eg. option 1 is index 0 in the dictionary
        while True:
            result = []
            try:
                attribute = input("Enter the "+ choicelist[choice]+" you'd like to search for:   ")
                for actor in actorsList:
                    if actorsList[actor][choice] == attribute:
                        result.append(actor)
                for value in result:
                    self.displayActorDetails(value)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                searchagain = input("That wasn't found. Search again? Press y or n")
                if searchagain == 'y':
                    continue
                else:
                    break
            
    def getActorDetails(self, firstName):
        for actor in actorsList:
            while actorsList[actor][0] == firstName:                                #Displays the details of all actors with that first name
                print("Actor name: ", actorsList[actor][0], actorsList[actor][1])
                print("Date of Birth: ", actorsList[actor][2])
                print("Gender: ", actorsList[actor][3])
            else:
                print("Sorry that actor's name is unrecognised...")

    def actorlistmenu(self):
        print("Welcome to the actor list menu!")
        print("Actor List Menu")
        print("1: Display actor list")
        print("2: Search for an actor")
        print("3: Remove an actor from the list")    
        print("4: Count the number of actors in the list")
        print("5: Get actor details")
        print("6: Return to the main menu")

        while True:
            try:
                choice = input("Enter your choice (1-6):\n")
                if choice == '1':
                    self.printActorsList()

                elif choice == '2':
                    self.searchActor()
            
                elif choice == '3':
                    self.removeActor()
            
                elif choice == '4':
                    self.countActors()
            
                elif choice == '5':
                    firstName = input("Please enter the first name of the actor you wish to retrieve details for:\n")
                    self.getActorDetails(firstName)

                elif choice == '6':
                    print("Taking you back to the main menu...")
                    Main.run()
                
            except:
                print('Invalid choice. Please enter a number from 1 to 6:\n')




class Main():
    def __init__(self):
        print ("Hello")
        pass

    def entermovie(self):
        movie = MovieClass()
        title = input("Please enter the movie title:\n")
        movie.setMovieTitle(title)
        while True:
            try:
                year = input("Please enter the movie year:\n")
                # Check if the year can be converted to an integer
                year = int(year)
                # Check if the year is within a reasonable range (eg. 1800 to current year)
                if 1800 <= year <= datetime.now().year:
                    movie.setMovieYear(year)
                    break
            except ValueError:
                print("Invalid input for year. Please enter a valid integer.")
                continue
        genre = input("Please enter the movie genre\n")
        movie.setMovieGenre(genre)
        while True:
            try:
                dateString = input("Please enter the movie date (format: yyyy,mm,dd):\n")
                # Parse the input string into a date object
                dateReleased = datetime.strptime(dateString, '%Y,%m,%d')
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format yyyy,mm,dd:\n")
                continue 
        movie.setDateReleased(dateReleased)
        movie.setID()
        print("The movie details you have entered are as follows:")
        movie.displayDetails()
        movie.addToMovieList()

    def enteractor(self):
        actor = ActorsClass()
        firstName = input("Please enter the actor's first name:\n")
        actor.setfirstName(firstName)
        surname = input("Please enter the actor's last name:\n")
        actor.setSurname(surname)
        while True:
            try:
                dateString = input("Please enter the actor's date of birth (format: yyyy,mm,dd):\n")
                # Parse the input string into a date object
                dateOfBirth = datetime.strptime(dateString, '%Y,%m,%d')
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format yyyy,mm,dd:\n")
                continue
           
        actor.setDateofBirth(dateOfBirth)
        gender = input("Please enter the actor's gender:\n")
        actor.setGender(gender)
        fullname = (firstName + surname)
        actor.setFullName(fullname)
        print("The actor details you have entered are as follows:")
        actor.displayActorDetails()
        actor.addToActorsList()
        

    @staticmethod
    def display_menu():
        print("Welcome to the Movie App!")
        print("Main Menu")
        print("1: Enter movie")
        print("2: Enter actor")
        print("3: Display movie list menu")
        print("4: Display actor list menu")
        print("5: Exit")

    def run(self):
        while True:
            Main.display_menu()
            choice = input("Enter your choice (1-5):\n")
            try:
                if choice == '1':
                    self.entermovie()

                elif choice == '2':
                    self.enteractor()
            
                elif choice == '3':
                    ml = MovieListClass()
                    ml.movielistmenu()
            
                elif choice == '4':
                    al = ActorsListClass()
                    al.actorlistmenu()
            
                elif choice == '5':
                    print("Thank you for using the Movie App. Goodbye.\n")
                    break

            except ValueError:
                print("Invalid choice. Please enter a number from 1 to 5:\n")
                continue

m = Main()
m.run()




"""
movie1= MovieClass.MovieClass()
movie1.setMovieTitle('The Shawshank Redemption')
movie1.setMovieYear(1994)
movie1.setMovieGenre('Drama')
movie1.setDateReleased(datetime.date(1994, 10, 14))
movie1.setID()
movie1.displayDetails()
MovieListClass.MovieListClass.addToMovieList(movie1)

movie2= MovieClass.MovieClass()
movie2.setMovieTitle('Dr. No')
movie2.setMovieYear(1962)
movie2.setMovieGenre('Action')
movie2.setDateReleased(datetime.date(1962, 10, 6))
movie2.setID()
movie2.displayDetails()
MovieListClass.MovieListClass.addToMovieList(movie2)

movie3 = MovieClass.MovieClass()
movie3.setMovieTitle('Inception')
movie3.setMovieYear(2010)
movie3.setMovieGenre('Sci-Fi')
movie3.setDateReleased(datetime.date(2010, 7, 16))
movie3.setID()
movie3.displayDetails()
MovieListClass.MovieListClass.addToMovieList(movie3)

movie4 = MovieClass.MovieClass()
movie4.setMovieTitle('The Dark Knight')
movie4.setMovieYear(2008)
movie4.setMovieGenre('Action')
movie4.setDateReleased(datetime.date(2008, 7, 18))
movie4.setID()
movie4.displayDetails()
MovieListClass.MovieListClass.addToMovieList(movie4)

# Creating actors
actor1 = ActorsClass.ActorsClass()
actor1.setfirstName('Leonardo')
actor1.setSurname('DiCaprio')
actor1.setDateofBirth(datetime.date(1974,11,11))
actor1.setGender('Male')
actor1.setFullName('leonardodicaprio')
ActorsListClass.ActorsListClass.addToActorsList(actor1)

actor2 = ActorsClass.ActorsClass()
actor2.setfirstName('Christian')
actor2.setSurname('Bale')
actor2.setDateofBirth(datetime.date(1974,1,30))
actor2.setGender('Male')
actor1.setFullName('christianbale')
ActorsListClass.ActorsListClass.addToActorsList(actor2)

# MovieListClass.MovieListClass.printMovieList()
OO7 = MovieClass.MovieClass()
OO7.setMovieTitle('Skyfall')
OO7.setMovieYear(2012)
OO7.setMovieGenre('Action')
OO7.setDateReleased(datetime.sate(2012, 10, 23))
OO7.setID()
MovieListClass.MovieListClass.addToMovieList(OO7)

JamesBond = ActorsClass.ActorsClass()
JamesBond.setfirstName('Daniel')
JamesBond.setSurname('Craig')
JamesBond.setDateofBirth(datetime.date(1968, 3, 2))
JamesBond.setGender('Male')
ActorsListClass.ActorsListClass.addToActorsList(JamesBond)

MovieListClass.MovieListClass.getMovieDetails(OO7)
"""


"""System testing: Write a python module to include appropriate code to automatically create the following objects:
1. A movie object named ‘007’ with all the details required for a movie.
2. A movie list object named ‘actions’ that contains ‘007’ object in the object’s collection.
3. An actor object named ‘JamesBond’ with all the details required for an actor in the class.
4. An actor list object named ‘all_actors’ that contains ‘JamesBond’ object in the object’s collection.
5. A statement to call the movie object method to get all the detail of the movie object “007”.
6. A statement to call the actor list object method to get the number of objects in its collection.
7. A statement to call the actor list object method to get the details of the actor James Bond
8. A statement to call the actor list object method to remove the details of the actor James Bond from the collection
"""


#MovieListClass.MovieListClass.searchCollection()




"""# Removing an actor
ActorsListClass.ActorsListClass.removeActor("Leonardo")
print("Total Actors:", ActorsListClass.ActorsListClass.countActors())
"""

# Getting actor details
"""actor_details = ActorsListClass.displayActorDetails("Christian")
print("Actor Details:", actor_details)"""
