#Software Engineering Course Project
#Group 3
#Cooper Poole
#Christian Chow Quan 
#Jason Barican
#Jian Gong
#Eloy Fernandes Ballesteros

#global arrays to store account information during runtime
loginUsername = ''
accUsernames = []
accPasswords = []
accFullNames = []
cont=True

def newAccount(accounts, accFile):
  count = 0
  for acc in accounts:
    count += 1

  #checking if amount of accounts has exceeded maximum
  if count >= 5:
    print("All permitted accounts have been created, please come back later\n")
  else:
    valid = False
    while valid is False:
      newUsername = input("Choose Username: ").replace(" ","")

      if len(accUsernames) == 0:
        valid = True
      else:
        for accUser in accUsernames:
          #ensuring username is unique
          if accUser == newUsername:
            print("Account username already in use.")
            valid = False
            break
          else:
            valid = True

    valid = False

    while valid is False:
      hasDigit = False
      hasNonAlphaNumeric = False
      password = input("Choose Password: ")
      #validation check for length and presence of upercase, special, and numeric character.
      if len(password) >= 8 and len(password) <= 12 and password.lower() != password:
        for char in password:
          if char.isdigit():
            hasDigit = True
          if not char.isalpha():
            hasNonAlphaNumeric = True
      if hasDigit is True and hasNonAlphaNumeric is True:
        valid = True
      else:
        print("Invalid password. Try a better password.")

    valid = False

    while valid is False:
      name = input("Enter your first and last name: ")
      nameCount = name.split()
      if len(nameCount) != 2:
        print("Invalid format, Two names not found.")
      else:
        valid = True
        
    #storing account data in file.
    accFile.write(newUsername + " " + password + " " + name + "\n")
    print("Account registered successfully!\n")

#function for playing video
def playvideo():
  print("\nVideo is now playing\n")
  option = input("Type 0 to go back\n")
  while option != "0":
    option = input()
  return
  
  
#populating arrays with account data from txt file
def loadAccounts(accounts):
  accUsernames.clear()
  accPasswords.clear()
  accFullNames.clear()
  for acc in accounts:
    accInfo = acc.split()
    accUsernames.append(accInfo[0])
    accPasswords.append(accInfo[1])
    accFullNames.append(accInfo[2] + " " + accInfo[3])

#checks entered credentials against stored user information for match
def login(accounts):
  global loginUsername
  loginUsername = input("Enter Username:\n")

  while loginUsername not in accUsernames:
    loginUsername = input("No registered username. Please try again\nEnter Username:\n")

  for i in range(len(accUsernames)):
    if accUsernames[i] == loginUsername:
      loginPassword = input("Enter Password:\n")

      while accPasswords[i] != loginPassword:
        loginPassword = input("Incorrect Password. Please try again\nEnter Password:\n")
      
      application_menu()
  


#presents menu for user to utilize application functions
def application_menu():
  cont = True
  print("\nYou have successfully logged in\n--------------------------------------")
  while(cont):
    print("Type number to select option:\n\n0. Exit\n1. Job Search/internship\n2. Find Someone You Know\n3. Learn a new skill\n4. Post a new job")
    menuSelect = input("")
    if menuSelect == "1":
      job_search()
    elif menuSelect == "2":
      find_someone()
    elif menuSelect == "3":
      learn_skills()
    elif menuSelect == "4":
      add_Job()
    elif menuSelect == "0":
      cont = False
    else:
      print("Invalid menu selection.")

#currently in progress job function
def job_search():
  cont = True
  while(cont):
    print("\nJob Search/internship\n--------------------------------------")
    print("Type number to select option:\n\n0. Exit\n1. Post job") 
    menuSelect = input("")
    if menuSelect == "1":
      add_Job()

    elif menuSelect == "0":
      cont = False

    else:
      print("Invalid menu selection.")

#title, description, employer,  location, salary and posted user
def add_Job():
  jobFile = open("jobs.txt","r+")
  jobs = jobFile.readlines()
  count = 0
  for job in jobs:
    count += 1

  #checking if amount of accounts has exceeded maximum
  if count >= 5:
    print("All permitted jobs have been created, please come back later\n")
  else:
    global loginUsername
    title = input("Enter title:\n")
    description = input("Enter description:\n")
    employer = input("Enter employer:\n")
    location = input("Enter location:\n")
    salary = input("Enter salary:\n")
    jobFile.write(title + " " + description + " " + employer + " " + location + " " + salary + " " + loginUsername +"\n")
    print("New job posted!\n")

#function lets logged in users check for mutual contacts in the InCollege system
def find_someone():
  SearchedName = input("Enter full name of person (0 to exit):\n")
  if SearchedName == '0':
    application_menu
  else:
    if SearchedName not in accFullNames:
      print("They are not a part of the InCollege system yet.")
    else:
      print(SearchedName + " is part of the InCollege system. Login or sign up to join them!")

#currently in progress skills function
def learn_skills():
  cont = True
  while(cont):
    print("\nLearn a new skill\n--------------------------------------")
    print("Type number to select option:\n\n0. Exit\n1. Learn Javascript\n2. Learn Webdesign") 
    print("3. Learn Java\n4. Learn Python\n5. Learn C++\n")
    menuSelect = input("")
    if menuSelect == "1":
      print("Under Construction.")
      cont = False

    elif menuSelect == "2":
      print("Under Construction.")
      cont = False

    elif menuSelect == "3":
      print("Under Construction.")
      cont = False

    elif menuSelect == "4":
      print("Under Construction.")
      cont = False

    elif menuSelect == "5":
      print("Under Construction.")
      cont = False

    elif menuSelect == "6":
      print("Under Construction.")
      cont = False

    elif menuSelect == "0":
      cont = False

    else:
      print("Invalid menu selection.")
  
            
def main():
    cont = True
    while(cont):
      accFile = open("accounts.txt","r+")
      accounts = accFile.readlines()
      loadAccounts(accounts)
      print("--------------------------------------\nWelcome to InCollege beta v0.2.3\n--------------------------------------\n")

      print("INCOLLEGE SUCCESS STORY\n--------------------------------------")
      print('"John used LinkedIn.\nHe could not get a job.\nJohn then started using InCollege.\nHe got a job."')
      print("--------------------------------------\n")

      print("Type number to select option:\n\n0. Exit\n1. Login\n2. New Account\n3. Play Video\n4. Find someone who can help\n")

     
      menuSelect = input("")
      if menuSelect == "1":
        login(accounts)
      elif menuSelect == "2":
        newAccount(accounts, accFile)
      elif menuSelect == "3":
        playvideo()
      elif menuSelect == "4":
        find_someone()
      elif menuSelect == "0":
        cont = False
      else:
        print("Invalid menu selection.")
      accFile.close()

if __name__ == "__main__":
    main()