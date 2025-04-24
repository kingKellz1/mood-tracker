import datetime
from pathlib import Path

<<<<<<< HEAD
#Gets the directory of the parent folder
current_dir = Path(__file__).parent

#Points to the file in the same directory
file_path = current_dir / "mood_log.txt"

if not file_path.exists():
    file_path.touch()  # Creates an empty file if it doesn’t exist yet


def view_mood_log(): 
    '''Creates a function to view the log file'''
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())

def add_mood_log(): 
    '''Creates a function so user can add a log enty'''
    users_feeling = input("\nHow are you feeling today?: (Happy, Sad, Mad, Angry, Flat) \n")
    users_day = input("\nHow was your day?: \n")

    #Stores the current date and time to a variable called "now"
    now = datetime.datetime.now() 
    
    #Stores only the date in the variable
    formated_now = now.strftime("%Y-%m-%d") 

    with open(file_path, "a") as file:
=======
def user_choice_1(): #This creates a function so view the log file
    with open("/Users/username/Desktop/python_projects/mood_tracker/mood_log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def user_choice_2(): #This creates a function so user cna add a log enty
    users_feeling = input("How are you feeling today?: (Happy, Sad, Mad, Angry, Flat) ")
    users_day = input("How was your day?: ")
    now = datetime.datetime.now() #Stores the current date and time to a variable called "now"
    formated_now = now.strftime("%Y-%m-%d") #Stores only the date in the variable
    with open("/Users/username/Desktop/python_projects/mood_tracker/mood_log.txt", "a") as file:
>>>>>>> bb1ba1a732370722a7e0de309439a9c187eb7380
        line = f"{formated_now} | {users_feeling} | {users_day}\n"
        file.write(line)

def main():
    print("\n***********************************")
    print("Hello, Welcome to your mood tracker")
    print("***********************************\n")
    while True:
        user_choice = input("What would you like to do: \n1 - View logs \n2 - Log your day \n")
        if user_choice == "1":
            view_mood_log()
            break
        elif user_choice == "2":
            add_mood_log()
            break
        else:
            #Prompts the user to enter a valid choice
            print("Please make a valid choice!\n") 

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
else:
    print("Please make a valid choice!") #Prompts the user to enter a valid choice
>>>>>>> bb1ba1a732370722a7e0de309439a9c187eb7380
