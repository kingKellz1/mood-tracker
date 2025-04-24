import datetime
from pathlib import Path

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

if __name__ == "__main__":
    main()