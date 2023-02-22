#Software Engineering Course Project
#Group 3
#Cooper Poole
#Christian Chow Quan 
#Jason Barican
#Jian Gong
#Eloy Fernandes Ballesteros


import tkinter as tk
from tkinter import messagebox

#global arrays to store account information during runtime
loginUsername = ''
accUsernames = []
accPasswords = []
accFullNames = []
cont=True

#presents menu for user to utilize application functions
class OptionsWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    
    accFile = open("accounts.txt","r+")
    accounts = accFile.readlines()
    self.controller.loadAccounts(accounts)
    
    tk.Label(self, text = "Welcome to InCollege Beta!\n\nINCOLLEGE SUCCESS STORY\nJohn used LinkedIn.\nHe could not get a job.\nJohn then started using InCollege.\nHe got a job.\n\nPlease select an option below.").pack(padx = 10, pady = 10)
    self.pack(padx = 10, pady = 10)

    loginButton = tk.Button(self, text = "Login",
                            command = lambda: controller.show_frame("LoginWindow"))
    loginButton.pack(padx=10, pady=10)

    signInButton = tk.Button(self, text = "Sign-In",
                            command = lambda: controller.show_frame("SignInWindow"))
    signInButton.pack(padx = 10, pady = 10)

    videoButton = tk.Button(self, text = "Play Video",
                            command = lambda: controller.show_frame("VideoWindow"))
    videoButton.pack(padx = 10, pady = 10)

    findSomeoneButton = tk.Button(self, text = "Find Someone",
                            command = lambda: controller.show_frame("FindSomeoneFrame"))
    findSomeoneButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)

class LoginWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Please enter username and password.").pack(padx=10, pady=10)

    

    usernameLabel = tk.Label(self, text = "Username:")
    usernameLabel.pack(padx=10, pady=10)
    self.usernameEntry = tk.Entry(self, bd = 5)
    self.usernameEntry.pack(padx=10, pady=10)

    passwordLabel = tk.Label(self, text = "Password:")
    passwordLabel.pack(padx=10, pady=10)
    self.passwordEntry = tk.Entry(self, bd = 5)
    self.passwordEntry.pack(padx=10, pady=10)

    buttonframe = tk.Frame(self)
    buttonframe.pack()
    enterButton = tk.Button(buttonframe, text = "Enter", 
                            command = lambda: self.login())
    enterButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(buttonframe, text = "Back", 
                          command = lambda: controller.show_frame("OptionsWindow"))
    backButton.pack(padx=10, pady=10)



  def login(self):
    loginUsername = self.usernameEntry.get()
    loginPassword = self.passwordEntry.get()

    
    if loginUsername not in accUsernames:
      messagebox.showerror("Error", "Incorrect username/password. Please try again.")
    else:
      for i in range(len(accUsernames)):
        if accUsernames[i] == loginUsername:

          if accPasswords[i] == loginPassword:
            self.controller.show_frame("ApplicationWindow")
          else:
            messagebox.showerror("Error", "Incorrect username/password. Please try again.")
    
class SignInWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    
    self.accFile = open("accounts.txt","r+")
    accounts = self.accFile.readlines()
    self.controller.loadAccounts(accounts)
    
    count = 0
    for acc in accounts:
      count+=1
    
    if count >= 5:
      tk.Label(self, text="All permitted accounts have been created. Please come back later.").pack(padx=10, pady=10)
    else:
      
      tk.Label(self, text="Create Username:").pack(padx=10, pady=10)
      self.newUsernameEntry = tk.Entry(self,bd = 5)
      self.newUsernameEntry.pack(padx=10, pady=10)

      self.enterButton = tk.Button(self, text = "Enter", 
                            command = lambda: self.usernameCheck())
      self.enterButton.pack(padx = 10, pady = 10)
      
      self.backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("OptionsWindow"))
      self.backButton.pack(padx=10, pady=10)
        

  def usernameCheck(self):
    
    self.newUsername = self.newUsernameEntry.get().replace(" ","")
    valid = False
    while valid is False:
      if len(accUsernames) == 0:
        valid = True
        tk.Label(self,text= "Create Password:").pack(padx=10, pady=10)
        self.enterButton.pack_forget()
        self.backButton.pack_forget()
        
        self.newPasswordEntry = tk.Entry(self,bd = 5)
        self.newPasswordEntry.pack(padx=10, pady=10)

        self.enterButton = tk.Button(self, text = "Enter", 
                          command = lambda: self.passwordCheck())
        self.enterButton.pack(padx = 10, pady = 10)
        #ensuring username is unique
      else:
        if self.newUsername in accUsernames:
          messagebox.showerror("Error", "Account username already in use. Please try again.")
          break
        else:
          valid = True
          tk.Label(self,text= "Create Password:").pack(padx=10, pady=10)
          self.enterButton.pack_forget()
          self.backButton.pack_forget()
          
          self.newPasswordEntry = tk.Entry(self,bd = 5)
          self.newPasswordEntry.pack(padx=10, pady=10)

          self.enterButton = tk.Button(self, text = "Enter", 
                            command = lambda: self.passwordCheck())
          self.enterButton.pack(padx = 10, pady = 10)

       
  def passwordCheck(self):  
    valid = False
  
    while valid is False:
      hasDigit = False
      hasNonAlphaNumeric = False
      
      self.newPassword = self.newPasswordEntry.get().replace(" ","")

      #validation check for length and presence of upercase, special, and numeric character.
      if len(self.newPassword) >= 8 and len(self.newPassword) <= 12 and self.newPassword.lower() != self.newPassword:
        for char in self.newPassword:
          if char.isdigit():
            hasDigit = True
          if not char.isalpha():
            hasNonAlphaNumeric = True
      if hasDigit is True and hasNonAlphaNumeric is True:
        valid = True
        tk.Label(self,text= "Enter your first and last name:").pack(padx=10, pady=10)
        self.enterButton.pack_forget()
        self.fullNameEntry = tk.Entry(self,bd = 5)
        self.fullNameEntry.pack(padx=10, pady=10)

        self.enterButton = tk.Button(self, text = "Enter", 
                            command = lambda: self.fullName())
        self.enterButton.pack(padx = 10, pady = 10)

      else:
        messagebox.showerror("Error", "Invalid Password. Try a better password.")
        break

  def fullName(self):
    valid = False

    while valid is False:
      self.name = self.fullNameEntry.get()
      nameCount = self.name.split()

      if len(nameCount) != 2:
        messagebox.showerror("Error", "Invalid format, Two names not found. Please try again.")
        break

      else:
        valid = True
        self.accFile.write(self.newUsername + " " + self.newPassword + " " + self.name + "\n")
        self.accFile.close()
        messagebox.showinfo("Account Created", "You have successfully created a new account.")
        self.destroy()




class VideoWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Video is now playing").pack(padx=10, pady=10)
    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("OptionsWindow"))
    backButton.pack(padx=10, pady=10)


class ApplicationWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller    

    tk.Label(self, text = "You have successfully logged in!\nPlease select an option.").pack(padx=10, pady=10) 

    jobSearchButton = tk.Button(self, text = "Job/Internship Search",
                            command = lambda: controller.show_frame("UnderConstruction"))
    jobSearchButton.pack(padx = 10, pady = 10)

    findSomeoneButton = tk.Button(self, text = "Find Someone",
                                  command = lambda: controller.show_frame("FindSomeoneFrame"))
    findSomeoneButton.pack(padx = 10, pady = 10)

    learnSkillButton = tk.Button(self, text = "Learn a new skill",
                            command = lambda: controller.show_frame("LearnSkillWindow"))
    learnSkillButton.pack(padx = 10, pady = 10)

    postJobButton = tk.Button(self, text = "Post a new job",
                            command = lambda: controller.show_frame("UnderConstruction"))
    postJobButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)

class LearnSkillWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Please select a skill to learn.").pack(padx=10, pady=10) 


    skill1Button = tk.Button(self, text = "Skill 1",
                            command = lambda: controller.show_frame("UnderConstruction"))
    skill1Button.pack(padx = 10, pady = 10)

    skill2Button = tk.Button(self, text = "Skill 2",
                                  command = lambda: controller.show_frame("UnderConstruction"))
    skill2Button.pack(padx = 10, pady = 10)

    skill3Button = tk.Button(self, text = "Skill 3",
                            command = lambda: controller.show_frame("UnderConstruction"))
    skill3Button.pack(padx = 10, pady = 10)

    skill4Button = tk.Button(self, text = "Skill 4",
                            command = lambda: controller.show_frame("UnderConstruction"))
    skill4Button.pack(padx = 10, pady = 10)

    skill5Button = tk.Button(self, text = "Skill 5",
                            command = lambda: controller.show_frame("UnderConstruction"))
    skill5Button.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)




    
class UnderConstruction(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller  

    tk.Label(self, text="Under Construction.").pack(padx=10, pady=10)

    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx=10, pady=10)

          
          

class MainWindow(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    mainframe = tk.Frame()
    self.windowNum = 0

    mainframe.pack(padx = 10, pady = 10, fill = 'both', expand = 1)
    self.framelist = {}                 #dictionary for different pages

    for F in (OptionsWindow, LoginWindow, SignInWindow,
              VideoWindow, ApplicationWindow, LearnSkillWindow,
              FindSomeoneFrame, UnderConstruction):

      frame_name = F.__name__
      frame = F(parent = mainframe, controller = self)
      frame.grid(row = 0, column = 0, sticky = 'nsew')
      self.framelist[frame_name] = frame

    self.show_frame("OptionsWindow")

    accFile = open("accounts.txt","r+")
    accounts = accFile.readlines()
    self.loadAccounts(accounts)



  def show_frame(self, frame_name):
    frame = self.framelist[frame_name]
    frame.tkraise()

  def loadAccounts(self, accounts):
    accUsernames.clear()
    accPasswords.clear()
    accFullNames.clear()
    for acc in accounts:
      accInfo = acc.split()
      accUsernames.append(accInfo[0])
      accPasswords.append(accInfo[1])
      accFullNames.append(accInfo[2] + " " + accInfo[3])



class FindSomeoneFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller 
    self.create_widgets()

  def create_widgets(self):
      self.name_label = tk.Label(self, text="Enter full name of person:")
      self.name_entry = tk.Entry(self)
      self.name_label.grid(row=0, column=0, padx=5, pady=5)
      self.name_entry.grid(row=0, column=1, padx=5, pady=5)

      self.search_button = tk.Button(self, text="Search", command=self.search)
      self.search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

      backButton = tk.Button(self, text = "Back", 
                            command = lambda: self.controller.show_frame("OptionsWindow"))
      backButton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

  def search(self):
      searched_name = self.name_entry.get()

      if searched_name not in accFullNames:
          result_text = "They are not a part of the InCollege system yet."
      else:
          result_text = f"{searched_name} is part of the InCollege system. Login or sign up to join them!"
      result_label = tk.Label(self, text=result_text)
      result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
      

  
if __name__ == '__main__':
  window = MainWindow()
  window.mainloop()


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

      

