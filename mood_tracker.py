import datetime

def user_choice_1(): #This creates a function so view the log file
    with open("/Users/nichealhickson/Desktop/python_projects/mood_tracker/mood_log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def user_choice_2(): #This creates a function so user cna add a log enty
    users_feeling = input("How are you feeling today?: (Happy, Sad, Mad, Angry, Flat) ")
    users_day = input("How was your day?: ")
    now = datetime.datetime.now() #Stores the current date and time to a variable called "now"
    formated_now = now.strftime("%Y-%m-%d") #Stores only the date in the variable
    with open("/Users/nichealhickson/Desktop/python_projects/mood_tracker/mood_log.txt", "a") as file:
        line = f"{formated_now} | {users_feeling} | {users_day}\n"
        file.write(line)

#Start of program
print("Hello, Welcome to your mood tracker")
user_choice = input("What would you like to do: \n1 - View logs \n2 - Log your day \n")
if user_choice == "1":
    user_choice_1() #Calls function to view log file

elif user_choice == "2":
    user_choice_2() #Calls function to append log file

else:
    print("Please make a valid choice!") #Prompts the user to enter a valid choice