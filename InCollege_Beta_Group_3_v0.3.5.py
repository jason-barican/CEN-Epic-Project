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
accEmailPrefs = "1"
accSMSPrefs = "1"
accTAPrefs = "1"
#accLangPrefs = "E"
PrevWindow = "MainMenu"
cont=True

#presents menu for user to utilize application functions
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.controller.geometry("800x800")
        self.controller.title('InCollege beta v0.3.4')
        accFile = open("accounts.txt","r+")
        accounts = accFile.readlines()
        self.controller.loadAccounts(accounts)
        
        tk.Label(self, text = "Welcome to InCollege Beta!\n\nINCOLLEGE SUCCESS STORY\nJohn used LinkedIn.\nHe could not get a job.\nJohn then started using InCollege.\nHe got a job.\n\nPlease select an option below.").place(x=300,y=25)
        self.pack(padx = 5, pady = 5)
        
        # Create a dropdown menu with the options "General", "Browse InCollege", "Business Solutions", and "Directories"
        menu_var = tk.StringVar()
        menu_var.set("Useful Links")
        options = ["General", "Browse InCollege", "Business Solutions", "Directories"]
        option_menu = tk.OptionMenu(self, menu_var, *options)
        option_menu.place(x=315, y=190)
        option_menu.config(width=25, height =2)

        
        # Create buttons to navigate to different frames based on the selected option
        loginButton = tk.Button(self, text="Login", command=lambda: controller.show_frame("LoginWindow"), width = 25, height = 2)
        loginButton.place(x=315, y=250)
        
        signInButton = tk.Button(self, text="Sign-Up", command=lambda: controller.show_frame("SignUpWindow"), width = 25, height = 2)
        signInButton.place(x=315, y=310)
        
        videoButton = tk.Button(self, text="Play Video", command=lambda: controller.show_frame("VideoWindow"), width = 25, height = 2)
        videoButton.place(x=315, y=370)
        
        findSomeoneButton = tk.Button(self, text="Find Someone", command=lambda: controller.show_frame("FindSomeoneFrame"), width = 25, height = 2)
        findSomeoneButton.place(x=315, y=430)
        
        option_menu['menu'].entryconfig(0, command=lambda: controller.show_frame("GeneralWindow"))
        # Bind the "Browse InCollege", "Business Solutions", and "Directories" options to the "under_construction" function
        option_menu['menu'].entryconfig(1, command=lambda: controller.show_frame("UnderConstruction"))
        option_menu['menu'].entryconfig(2, command=lambda: controller.show_frame("UnderConstruction"))
        option_menu['menu'].entryconfig(3, command=lambda: controller.show_frame("UnderConstruction"))
        
        exitButton = tk.Button(self, text="Exit", command=self.quit, width = 25, height = 2)
        exitButton.place(x=315, y=490)

        # Create the second dropdown menu with the options "Copyright Notice", "About", "Accessibility", "User Agreement", "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy", "Guest Controls", and "Languages"
        menu_var2 = tk.StringVar()
        menu_var2.set("InCollege Important Links")
        options2 = ["Copyright Notice",
                    "About",
                    "Accessibility",
                    "User Agreement",
                    "Privacy Policy",
                    "Cookie Policy",
                    "Copyright Policy",
                    "Brand Policy",
                    "Languages"]
        option_menu2 = tk.OptionMenu(self, menu_var2, *options2)
        option_menu2.place(x=315, y=550)
        option_menu2['menu'].entryconfig(0, command=lambda: controller.show_frame("CopyrightNoticeFrame"))
        option_menu2['menu'].entryconfig(1, command=lambda: controller.show_frame("InCollegeAboutFrame"))
        option_menu2['menu'].entryconfig(2, command=lambda: controller.show_frame("AccessibilityNoticeFrame"))
        option_menu2['menu'].entryconfig(3, command=lambda: controller.show_frame("UserAgreementFrame"))
        option_menu2['menu'].entryconfig(4, command=lambda: controller.show_frame("PrivacyPolicyFrame"))
        option_menu2['menu'].entryconfig(5, command=lambda: controller.show_frame("CookiePolicyFrame"))
        option_menu2['menu'].entryconfig(6, command=lambda: controller.show_frame("CopyrightPolicyFrame"))
        option_menu2['menu'].entryconfig(7, command=lambda: controller.show_frame("BrandPolicyFrame"))
        option_menu2['menu'].entryconfig(9, command=lambda: controller.show_frame("LanguageFrame"))
        option_menu2.config(width=25, height =2)

class CopyrightNoticeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Create label for the copyright notice
        tk.Label(self, text="Copyright © 2023 Group 3 SE. All rights reserved.\n\n"
                            "This program and its accompanying materials are protected under the copyright laws of United States of America and other countries. \nUnauthorized reproduction, distribution, or modification of this program, or any portion of it, may result in severe civil and criminal penalties, \nand will be prosecuted to the maximum extent possible under the law.\n\n"
                            "INCOLLEGE is a trademark of Group 3 SE. Any use of this trademark without express written permission from Group 3 SE is strictly prohibited.").grid(column=0,row=0)
        
        # Create back button
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.grid(row=1,column=0)

class InCollegeAboutFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="InCollege Features").grid(column=0,row=0)
        tk.Label(self, text="InCollege is a social networking platform designed specifically for college students, alumni, and faculty members. \nWith InCollege, users can create a professional profile, connect with classmates and colleagues, join interest groups, and\n explore career opportunities.").grid(column=0,row=1)
        tk.Label(self, text="One of the main features of InCollege is the ability to connect with other users based on shared interests or career\n aspirations. Users can join or create interest groups focused on specific industries, job functions, or hobbies, making\n it easy to find and connect with like-minded individuals.").grid(column=0,row=2)
        tk.Label(self, text="InCollege also provides a job search feature, where users can search for job opportunities and internships based on \ntheir field of study, location, or career interests. Employers can also use the platform to post job listings and connect\n with potential candidates.").grid(column=0,row=3)
        tk.Label(self, text="Overall, InCollege is a powerful tool for college students and alumni who are looking to expand their professional\n networks and explore career opportunities. Whether you're a recent graduate looking for your first job, or an established\n professional looking to connect with others in your field, InCollege has something to offer.").grid(column=0,row=4)
        
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        back_button.grid(column=0,row=5)

class AccessibilityNoticeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""Accessibility Notice:\n\n
                               InCollege is committed to making our software accessible to all users, regardless of their abilities or disabilities. 
                               Our team has taken great care to ensure that our application is designed to be as user-friendly as possible for all individuals.\n\n
                               Our software provides a range of accessibility features to ensure that users with disabilities can use it easily and effectively. 
                               Some of these features include adjustable font sizes, high contrast modes, support for screen readers, and keyboard shortcuts.\n\n
                               If you have any questions or suggestions for how we can further improve the accessibility of our application, please don't hesitate to contact us. 
                               We welcome your feedback and are committed to ensuring that our software is accessible to all users.""").grid(column=0,row=0)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.grid(column=0,row=1)
        


class UserAgreementFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text=("""InCollege User Agreement\n
                                Please read this User Agreement carefully before using the InCollege application (the "Application"). By using the Application, 
                                you agree to be bound by the terms and conditions of this Agreement.\n
                                Use of the Application\n
                                The InCollege Application is designed to help users create a professional network and explore career opportunities.
                                By using the Application, you agree to use it only for lawful purposes and in accordance with this Agreement.\n
                                User Conduct\n
                                You agree to use the Application in a responsible manner and to comply with all applicable laws and regulations. You may not 
                                use the Application to engage in any conduct that is prohibited by law or that interferes with the rights of others.\n
                                User Content\n
                                You are solely responsible for any content that you submit to the Application, including your user profile and any comments, messages, or other content 
                                that you post. You agree that you will not post or transmit any content that is unlawful, offensive, defamatory, or otherwise inappropriate.\n
                                Intellectual Property Rights\n
                                All content and materials on the Application, including trademarks, logos, and copyrights, are owned or licensed by InCollege or its affiliates. You 
                                agree not to copy, distribute, or use any of the content or materials on the Application without the prior written consent of InCollege.\n
                                Termination\n
                                InCollege may terminate this Agreement at any time and for any reason, without notice to you. In the event of termination, you must immediately cease 
                                using the Application and delete all copies of the Application from your computer or mobile device.\n
                                Disclaimer of Warranties\n
                                THE APPLICATION IS PROVIDED "AS IS" AND WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, WARRANTIES
                                OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. INCOLLEGE DOES NOT WARRANT THAT THE APPLICATION WILL BE
                                UNINTERRUPTED OR ERROR-FREE, OR THAT ANY DEFECTS WILL BE CORRECTED.
                                Limitation of Liability\n
                                IN NO EVENT WILL INCOLLEGE BE LIABLE TO YOU FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF OR IN 
                                CONNECTION WITH THE APPLICATION, INCLUDING, BUT NOT LIMITED TO, LOST PROFITS, LOSS OF USE, OR DATA LOSS, WHETHER IN AN ACTION IN 
                                CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, EVEN IF INCOLLEGE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
                                Governing Law\n
                                This Agreement shall be governed by and construed in accordance with the laws of the jurisdiction in which InCollege is located, 
                                without regard to its conflict of laws principles.\n
                                Entire Agreement\n\
                                This Agreement constitutes the entire agreement between you and InCollege and supersedes all prior agreements and understandings, whether written or oral.\n
                                By using the InCollege Application, you acknowledge that you have read and understand this User Agreement and agree to be bound by its terms and conditions.""")).grid(column=0,row=0)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.grid(column=0,row=1)
        


class PrivacyPolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Privacy Policy\n\nAt InCollege, we take your privacy very seriously. 
                               This Privacy Policy explains how we collect, use, and protect your personal information when you use the InCollege application (the "Application").\n\n
                               1. Collection of Personal Information\n
                               We collect personal information that you voluntarily provide to us when you use the Application, such as your name, email address, and other contact information. 
                               We may also collect information about your use of the Application, such as your browsing history, search queries, and other usage data.\n\n
                               2. Use of Personal Information\n
                               We use your personal information to provide you with the services and features of the Application, 
                               such as creating a professional profile and connecting with other users. We may also use your information to send you promotional and marketing materials, 
                               to improve the Application, and to customize your user experience.\n\n
                               3. Disclosure of Personal Information\n
                               We do not sell, trade, or rent your personal information to third parties. However, we may share your information with our affiliates and service providers, 
                               such as hosting and data processing vendors, for the purpose of operating and improving the Application.\n\n
                               4. Security of Personal Information\n
                               We take reasonable measures to protect your personal information from unauthorized access, disclosure, alteration, or destruction. 
                               We use industry-standard security technologies and procedures to help protect your personal information.\n\n
                               5. Cookies and Similar Technologies\n
                               We may use cookies, web beacons, and other similar technologies to collect information about your use of the Application. 
                               These technologies help us to analyze user behavior and provide a better user experience.\n\n
                               6. Children's Privacy\n
                               The Application is not intended for use by children under the age of 13. We do not knowingly collect personal information from children under the age of 13. 
                               If we become aware that we have collected personal information from a child under the age of 13, we will take steps to delete that information.\n\n
                               7. Changes to this Privacy Policy\n
                               We may update this Privacy Policy from time to time. We will post any changes on this page and indicate the date of the last update. 
                               Your continued use of the Application after any changes to this Privacy Policy will indicate your acceptance of the changes.\n\n
                               8. Contact Us\n
                               If you have any questions or concerns about this Privacy Policy, please contact us at [contact information].\n\n
                               By using the InCollege Application, you acknowledge that you have read and understand this Privacy Policy and agree to our collection, use, 
                               and disclosure of your personal information as described herein.""").pack(padx=10, pady=10)

        GuestControlsButton = tk.Button(self, text="Guest Controls", command=lambda: controller.show_frame("GuestControlsFrame"))
        GuestControlsButton.pack(padx=10, pady=10)

        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



class CookiePolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Cookie Policy\n\n
                               This Cookie Policy explains how InCollege "we" or "us" uses cookies on the InCollege website (the "Website"). 
                               By using the Website, you consent to the use of cookies in accordance with this policy.\n\n
                               What are cookies?\n
                               Cookies are small text files that are placed on your device when you visit the Website. 
                               They allow the Website to remember your preferences and enhance your user experience.\n\n
                               Types of cookies we use\n
                               We use the following types of cookies on the Website:\n\n
                               1. Essential cookies - These cookies are necessary for the Website to function properly. They enable you to navigate the Website and use its features.\n\n
                               2. Performance cookies - These cookies collect information about how you use the Website, such as which pages you visit most often. 
                               They help us to improve the performance of the Website.\n\n
                               3. Functionality cookies - These cookies remember your preferences and enable us to personalize your experience on the Website.\n\n
                               4. Advertising cookies - These cookies are used to deliver personalized advertisements to you based on your interests.\n\n
                               How we use cookies\nWe use cookies to:\n- Remember your preferences and personalize your experience on the Website\n
                               - Improve the performance of the Website\n
                               - Deliver personalized advertisements to you based on your interests\n\n
                               Third-party cookies\n
                               We may allow third-party service providers to place cookies on the Website for the purposes of delivering personalized advertisements to you based on your interests. 
                               These cookies are subject to the privacy policies of the third-party service providers.\n\n
                               Managing cookies\n
                               Most web browsers allow you to manage your cookie preferences. You can set your browser to refuse cookies, or to alert you when cookies are being sent. 
                               However, please note that disabling cookies may impact your ability to use the Website.\n\n
                               Changes to this policy\n
                               We may update this Cookie Policy from time to time. We will post any changes on this page and indicate the date of the last update. 
                               Your continued use of the Website after any changes to this Cookie Policy will indicate your acceptance of the changes.\n\n
                               Contact us\nIf you have any questions or concerns about this Cookie Policy, please contact us at [contact information].""").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



class CopyrightPolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Copyright Policy\n\n
                               All content included on the InCollege website, including but not limited to text, graphics, logos, images, audio clips, video clips, and software, 
                               is the property of InCollege or its content suppliers and is protected by United States and international copyright laws. 
                               The compilation of all content on this site is the exclusive property of InCollege and is protected by United States and international copyright laws. \n\n
                               InCollege reserves the right to terminate the accounts of users who infringe upon the intellectual property rights of others. 
                               If you believe that your work has been used on the InCollege website in a way that constitutes copyright infringement, 
                               please contact us at [contact information] with the following information:\n\n
                               - A physical or electronic signature of the person authorized to act on behalf of the owner of the copyright interest;\n
                               - A description of the copyrighted work that you claim has been infringed;\n
                               - A description of where the material that you claim is infringing is located on the site;\n
                               - Your address, telephone number, and email address;\n
                               - A statement by you that you have a good faith belief that the disputed use is not authorized by the copyright owner, its agent, or the law; and\n
                               - A statement by you, made under penalty of perjury, that the above information in your notice is accurate and that you are the copyright owner or 
                               authorized to act on the copyright owner's behalf.\n\n
                               InCollege may revise this Copyright Policy at any time without notice. By using this website, 
                               you are agreeing to be bound by the then-current version of this Copyright Policy.""").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



class BrandPolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Brand Policy\n\n
                               1. Ownership of InCollege Brand\n
                               The InCollege brand, including but not limited to the InCollege name, logo, and any other trademarks or service marks used on the InCollege website or applications, 
                               are the property of InCollege. No use of the InCollege brand may be made without the prior written authorization of InCollege.\n\n
                               2. Permitted Use of InCollege Brand\n
                               InCollege allows the use of its brand for certain purposes, including but not limited to the promotion of the InCollege website or applications, 
                               provided that the use complies with the following guidelines:\n
                               - The InCollege brand may only be used in a manner that is consistent with the InCollege mission and values;\n
                               - The InCollege brand must be used in its entirety and may not be altered in any way;\n
                               - The InCollege brand may not be used in a manner that suggests InCollege endorses or is affiliated with any other product or service;\n
                               - The InCollege brand may not be used in a manner that is likely to cause confusion among users or the public;\n
                               - The InCollege brand may not be used in any way that is harmful, defamatory, or otherwise objectionable to InCollege;\n
                               - The InCollege brand may not be used by any third party without the prior written authorization of InCollege.\n\n
                               3. Prohibited Use of InCollege Brand\nThe following uses of the InCollege brand are strictly prohibited:\n
                               - Any use that violates applicable laws or regulations;\n- Any use that is misleading, deceptive, or fraudulent;\n
                               - Any use that is disparaging or damaging to the InCollege brand or its reputation;\n
                               - Any use that is for commercial purposes or in connection with the promotion of a product or service that is not affiliated with InCollege;\n
                               - Any use that is likely to cause confusion or mistake among users or the public.\n\n
                               4. Enforcement of InCollege Brand Policy\n
                               InCollege reserves the right to take legal action to enforce its rights in the InCollege brand, including seeking injunctive relief and damages. 
                               InCollege may also terminate any relationship or agreement with any third party that uses the InCollege brand in violation of this policy.\n\n
                               5. Changes to InCollege Brand Policy\n
                               InCollege may revise this Brand Policy at any time without notice. By using the InCollege brand, 
                               you are agreeing to be bound by the then-current version of this Brand Policy.""").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)


class GuestControlsFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    # Create a label for the frame
    label = tk.Label(self, text="Guest Controls")
    label.pack(pady=10)

    # Create the InCollege Email checkbox
    email_var = tk.BooleanVar()
    email_checkbutton = tk.Checkbutton(self, text="InCollege Email", variable=email_var)
    email_checkbutton.pack()

    # Create the SMS checkbox
    sms_var = tk.BooleanVar()
    sms_checkbutton = tk.Checkbutton(self, text="SMS", variable=sms_var)
    sms_checkbutton.pack()

    # Create the Targeted Advertising checkbox
    targeting_var = tk.BooleanVar()
    targeting_checkbutton = tk.Checkbutton(self, text="Targeted Advertising", variable=targeting_var)
    targeting_checkbutton.pack()

    # Create a button to go back to the previous frame
    back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
    back_button.pack(pady=10)


class LanguageFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    # Create a label
    label = tk.Label(self, text="Please select your preferred language:")
    label.pack(pady=10)

    # Create a StringVar to hold the selected language
    self.language_var = tk.StringVar()

    self.bind("<<ShowFrame>>", self.on_show_frame)
    # Create two checkboxes for English and Spanish, and make them mutually exclusive
    self.english_checkbox = tk.Checkbutton(self, text="English", variable=self.language_var, onvalue="English", offvalue="")
    self.spanish_checkbox = tk.Checkbutton(self, text="Spanish", variable=self.language_var, onvalue="Spanish", offvalue="")
    self.english_checkbox.select()
    self.english_checkbox.pack(pady=5)
    self.spanish_checkbox.pack(pady=5)
    # Create a button to save the selected language and return to the previous frame
    save_button = tk.Button(self, text="Save and Return", command=self.save_language)
    save_button.pack(pady=10)

  def on_show_frame(self, event):
    selected_language = self.language_var.get()
    print(selected_language)
    print(PrevWindow)
    print(self.language_var.get())
    if selected_language == "English":
      self.english_checkbox.select()
    elif selected_language == "Spanish":
      self.spanish_checkbox.select()


  def save_language(self):
    # Get the selected language from the StringVar and save it
    selected_language = self.language_var

    if selected_language == "English":
      self.language_var = "English"
    elif selected_language == "Spanish":
      self.language_var = "Spanish"
    # Do something with the selected language, such as updating a user's preferences
    # ...

    # Return to the previous frame
    self.controller.show_frame(PrevWindow)




class GeneralWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text = "General", font = ("Arial", 14)).pack(pady = 10)
        
        signUpButton = tk.Button(self, text="Sign Up", command=lambda: controller.show_frame("SignUpWindow"))
        signUpButton.pack(pady = 10)
        
        helpCenterButton = tk.Button(self, text="Help Center", command=lambda: controller.show_frame("HelpCenterFrame"))
        helpCenterButton.pack(pady = 10)
        
        aboutButton = tk.Button(self, text="About", command=lambda: controller.show_frame("AboutFrame"))
        aboutButton.pack(pady = 10)
        
        pressButton = tk.Button(self, text="Press", command=lambda: controller.show_frame("PressFrame"))
        pressButton.pack(pady = 10)
        
        blogButton = tk.Button(self, text="Blog", command=lambda: controller.show_frame("UnderConstruction"))
        blogButton.pack(pady = 10)
        
        careersButton = tk.Button(self, text="Careers", command=lambda: controller.show_frame("UnderConstruction"))
        careersButton.pack(pady = 10)
        
        developersButton = tk.Button(self, text="Developers", command=lambda: controller.show_frame("UnderConstruction"))
        developersButton.pack(pady = 10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(pady = 10)

class HelpCenterFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="We're here to help").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)


class AboutFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)


class PressFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="In College Pressroom: Stay on top of the latest news, updates, and reports").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



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
                          command = lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx=10, pady=10)



  def login(self):
    loginUsername = self.usernameEntry.get()
    loginPassword = self.passwordEntry.get()

    accFile = open("accounts.txt","r+")
    accounts = accFile.readlines()
    self.controller.loadAccounts(accounts)
    
    if loginUsername not in accUsernames:
      messagebox.showerror("Error", "Incorrect username/password. Please try again.")
    else:
      for i in range(len(accUsernames)):
        if accUsernames[i] == loginUsername:

          if accPasswords[i] == loginPassword:
            acc = accounts[i]
            accInfo = acc.split()
            accEmailPrefs = accInfo[4]
            accSMSPrefs = accInfo[5]
            accTAPrefs = accInfo[6]
            #accLangPrefs = accInfo[7]
            self.language_var = accInfo[7]
            print(self.language_var)

            self.controller.show_frame("ApplicationWindow")
          else:
            messagebox.showerror("Error", "Incorrect username/password. Please try again.")
    
class SignUpWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
         
    tk.Label(self, text="Create Username:").pack(padx=10, pady=10)
    self.newUsernameEntry = tk.Entry(self,bd = 5)
    self.newUsernameEntry.pack(padx=10, pady=10)

    self.enterButton = tk.Button(self, text = "Enter", 
                          command = lambda: self.usernameCheck())
    self.enterButton.pack(padx = 10, pady = 10)
    
    self.backButton = tk.Button(self, text = "Back", 
                        command = lambda: controller.show_frame("MainMenu"))
    self.backButton.pack(padx=10, pady=10)
        

  def usernameCheck(self):

    self.accFile = open("accounts.txt","r+")
    accounts = self.accFile.readlines()
    self.controller.loadAccounts(accounts)
    
    count = 0
    for acc in accounts:
      count+=1
    
    if count >= 5:
      tk.Label(self, text="All permitted accounts have been created. Please come back later.").pack(padx=10, pady=10)
    else:
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
        self.accFile.write(self.newUsername + " " + self.newPassword + " " + self.name + " 1 1 1 E\n")
        self.accFile.close()
        messagebox.showinfo("Account Created", "You have successfully created a new account.")
        self.destroy()


class VideoWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Video is now playing").pack(padx=10, pady=10)
    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx=10, pady=10)


class ApplicationWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller    

    tk.Label(self, text = "You have successfully logged in!\nPlease select an option.").pack(padx=10, pady=10) 

    menu_var = tk.StringVar()
    menu_var.set("Useful Links")
    options = ["General", "Browse InCollege", "Business Solutions", "Directories"]
    option_menu = tk.OptionMenu(self, menu_var, *options)
    option_menu.pack(padx = 10, pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

    option_menu['menu'].entryconfig(0, command=lambda: controller.show_frame("GeneralWindow"))
    # Bind the "Browse InCollege", "Business Solutions", and "Directories" options to the "under_construction" function
    option_menu['menu'].entryconfig(1, command=lambda: controller.show_frame("UnderConstruction"))
    option_menu['menu'].entryconfig(2, command=lambda: controller.show_frame("UnderConstruction"))
    option_menu['menu'].entryconfig(3, command=lambda: controller.show_frame("UnderConstruction"))

    jobSearchButton = tk.Button(self, text = "Job/Internship Search", command = lambda: controller.show_frame("JobSearchFrame"))
    jobSearchButton.pack(padx = 10, pady = 10)

    findSomeoneButton = tk.Button(self, text = "Find Someone", command = lambda: controller.show_frame("FindSomeoneFrame"))
    findSomeoneButton.pack(padx = 10, pady = 10)

    learnSkillButton = tk.Button(self, text = "Learn a new skill", command = lambda: controller.show_frame("LearnSkillWindow"))
    learnSkillButton.pack(padx = 10, pady = 10)

    postJobButton = tk.Button(self, text = "Post a new job", command = lambda: controller.show_frame("AddJobFrame"))
    postJobButton.pack(padx = 10, pady = 10)

    postJobButton = tk.Button(self, text = "Add friends", command = lambda: controller.show_frame("FriendFrame"))
    postJobButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx = 10, pady = 10)

# Create the second dropdown menu with the options "Copyright Notice", "About", "Accessibility", "User Agreement", "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy", "Guest Controls", and "Languages"
    menu_var2 = tk.StringVar()
    menu_var2.set("InCollege Important Links")
    options2 = ["Copyright Notice",
                "About",
                "Accessibility",
                "User Agreement",
                "Privacy Policy",
                "Cookie Policy",
                "Copyright Policy",
                "Brand Policy",
                "Languages"]
    option_menu2 = tk.OptionMenu(self, menu_var2, *options2)
    option_menu2.pack(padx = 10, pady = 10)
    option_menu2['menu'].entryconfig(0, command=lambda: controller.show_frame("CopyrightNoticeFrame"))
    option_menu2['menu'].entryconfig(1, command=lambda: controller.show_frame("InCollegeAboutFrame"))
    option_menu2['menu'].entryconfig(2, command=lambda: controller.show_frame("AccessibilityNoticeFrame"))
    option_menu2['menu'].entryconfig(3, command=lambda: controller.show_frame("UserAgreementFrame"))
    option_menu2['menu'].entryconfig(4, command=lambda: controller.show_frame("PrivacyPolicyFrame"))
    option_menu2['menu'].entryconfig(5, command=lambda: controller.show_frame("CookiePolicyFrame"))
    option_menu2['menu'].entryconfig(6, command=lambda: controller.show_frame("CopyrightPolicyFrame"))
    option_menu2['menu'].entryconfig(7, command=lambda: controller.show_frame("BrandPolicyFrame"))
    option_menu2['menu'].entryconfig(9, command=lambda: controller.show_frame("LanguageFrame"))

  def on_show_frame(self, event):
    PrevWindow = "ApplicationWindow"

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

    backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)




    
class UnderConstruction(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller  

    tk.Label(self, text="Under Construction.").pack(padx=10, pady=10)

    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx=10, pady=10)

          


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
                            command = lambda: self.controller.show_frame("MainMenu"))
      backButton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

  def search(self):
      searched_name = self.name_entry.get()

      if searched_name not in accFullNames:
          result_text = "They are not a part of the InCollege system yet."
      else:
          result_text = f"{searched_name} is part of the InCollege system. Login or sign up to join them!"
      result_label = tk.Label(self, text=result_text)
      result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
      
class JobSearchFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text="Welcome to Job/Internship Search!\nPlease select an option below.").pack(padx=10, pady=10)

    addJobButton = tk.Button(self, text = "Add Job",
                            command = lambda: controller.show_frame("AddJobFrame"))
    addJobButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx=10, pady=10)

class FriendFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    # Create Scrollbar widget and Canvas widget
    scrollbar = tk.Scrollbar(self)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    self.canvas = tk.Canvas(self, yscrollcommand=scrollbar.set)
    self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=self.canvas.yview)

    # Create a Frame widget to contain all the elements and buttons
    self.frame = tk.Frame(self.canvas)
    self.canvas.create_window((0, 0), window=self.frame, anchor='nw')



    # Read the specified elements from the file
    self.elements = self.read_file('accounts.txt', '"start"', '"end"')

    # Display the elements and buttons in the Frame widget
    self.add_elements()

    # Allow the Canvas widget to automatically adjust its size
    self.frame.update_idletasks()
    self.canvas.config(scrollregion=self.canvas.bbox('all'))

  def read_file(self, filename, start_elem, end_elem):
    elements = []
    with open(filename, 'r') as f:
        content = f.read()
        start_index = content.index(start_elem) + len(start_elem)
        end_index = len(content)  # Assume end of file is end index
        if end_elem in content[start_index:]:
            end_index = content.index(end_elem, start_index)
            # Split the content between start_elem and end_elem into elements
            content_between = content[start_index:end_index]
            elements = [e.strip() for e in content_between.split("\"")]
        else:
            end_index = len(content)  # Assume end of file is end index
    return elements
  
  def add_elements(self):
    if not self.elements:
        # Display "No new request" if there are no elements
        label = tk.Label(self.frame, text="No new request", width=50)
        label.grid(row=0, column=0, padx=5, pady=5)
    else:
        # Add elements and buttons to the Frame widget
        for i, element in enumerate(self.elements):
            label = tk.Label(self.frame, text=element, width=50)
            label.grid(row=i, column=0, padx=5, pady=5)
            button1 = tk.Button(self.frame, text='reject', command=lambda element=element: self.delete_element(element))
            button1.grid(row=i, column=1, padx=5, pady=5)
            button2 = tk.Button(self.frame, text='accept', command=lambda element=element: self.move_element(element))
            button2.grid(row=i, column=2, padx=5, pady=5)
    backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("ApplicationWindow"))
    backButton.pack(padx=5, pady=5)

  def delete_element(self, element):
    # Read the file and remove the specified element
    with open('accounts.txt', 'r') as f:
        lines = f.readlines()
    with open('accounts.txt', 'w') as f:
        for line in lines:
            if element not in line:
                f.write(line)
            else:
                # Remove the specified element from the line
                line = line.replace(element, "")
                line = line.replace('""', '"')
                f.write(line)
    self.update_frame()

  def move_element(self, element):
# Read the contents of the file into a variable
    with open('accounts.txt', 'r') as f:
        content = f.read()

    # Find the index of the "end" tag
    end_index = content.find('"end"')

    # Delete the element if it exists in the file
    if element in content:
        content = content.replace(element, '')



    # Write the updated content back to the file
    with open('accounts.txt', 'w') as f:
        content = content.replace('""', '"')
        f.write(content)

    # Update the Frame widget
    self.update_frame()


  def update_frame(self):
    # Reload the elements
    self.elements = self.read_file('accounts.txt', '"start"', '"end"')

    # Update the Frame widget
    self.frame.destroy()
    self.frame = tk.Frame(self.canvas)
    self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
    self.add_elements()

    # Allow the Canvas widget to automatically adjust its size
    self.frame.update_idletasks()
    self.canvas.config(scrollregion=self.canvas.bbox('all'))

class AddJobFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.create_widgets()

  def create_widgets(self):
      self.title_label = tk.Label(self, text="Enter title:")
      self.title_entry = tk.Entry(self)
      self.title_label.grid(row=0, column=0, padx=5, pady=5)
      self.title_entry.grid(row=0, column=1, padx=5, pady=5)

      self.description_label = tk.Label(self, text="Enter description:")
      self.description_entry = tk.Entry(self)
      self.description_label.grid(row=1, column=0, padx=5, pady=5)
      self.description_entry.grid(row=1, column=1, padx=5, pady=5)

      self.employer_label = tk.Label(self, text="Enter employer:")
      self.employer_entry = tk.Entry(self)
      self.employer_label.grid(row=2, column=0, padx=5, pady=5)
      self.employer_entry.grid(row=2, column=1, padx=5, pady=5)

      self.location_label = tk.Label(self, text="Enter location:")
      self.location_entry = tk.Entry(self)
      self.location_label.grid(row=3, column=0, padx=5, pady=5)
      self.location_entry.grid(row=3, column=1, padx=5, pady=5)

      self.salary_label = tk.Label(self, text="Enter salary:")
      self.salary_entry = tk.Entry(self)
      self.salary_label.grid(row=4, column=0, padx=5, pady=5)
      self.salary_entry.grid(row=4, column=1, padx=5, pady=5)

      self.post_button = tk.Button(self, text="Post job", command=self.post_job)
      self.post_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

      self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))
      self.back_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

  def post_job(self):
      jobFile = open("jobs.txt","r+")
      jobs = jobFile.readlines()
      count = 0
      for job in jobs:
        count += 1

      #checking if amount of accounts has exceeded maximum
      if count >= 5:
        result_text = "All permitted jobs have been created, please come back later"
      else:
        global loginUsername
        title = self.title_entry.get()
        description = self.description_entry.get()
        employer = self.employer_entry.get()
        location = self.location_entry.get()
        salary = self.salary_entry.get()
        jobFile.write(title + " " + description + " " + employer + " " + location + " " + salary + " " + loginUsername +"\n")
        result_text = "New job posted!"

      result_label = tk.Label(self, text=result_text)
      result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


class MainWindow(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    mainframe = tk.Frame()
    self.windowNum = 0
    self.geometry("800x800")
    mainframe.pack(padx = 5, pady = 5,)# fill = 'both', expand = 1)
    self.framelist = {}                 #dictionary for different pages

    for F in (MainMenu, LoginWindow, SignUpWindow,
              VideoWindow, ApplicationWindow, LearnSkillWindow,
              FindSomeoneFrame, JobSearchFrame, AddJobFrame, CopyrightNoticeFrame,
              InCollegeAboutFrame, AccessibilityNoticeFrame, UserAgreementFrame,
              PrivacyPolicyFrame, CookiePolicyFrame, CopyrightPolicyFrame,
              BrandPolicyFrame, GuestControlsFrame, LanguageFrame,
              GeneralWindow, HelpCenterFrame, AboutFrame, 
              PressFrame, UnderConstruction, FriendFrame):

      frame_name = F.__name__
      frame = F(parent = mainframe, controller = self)
      frame.grid(row = 0, column = 0, sticky = 'nsew')
      self.framelist[frame_name] = frame

    self.show_frame("MainMenu")

    accFile = open("accounts.txt","r+")
    accounts = accFile.readlines()
    self.loadAccounts(accounts)



  def show_frame(self, frame_name):
    frame = self.framelist[frame_name]
    frame.event_generate("<<ShowFrame>>")
    frame.tkraise()

  def loadAccounts(self, accounts):
    accUsernames.clear()
    accPasswords.clear()
    accFullNames.clear()

    for acc in accounts:
      accInfo = acc.split()
      if len(accInfo) > 7:
        accUsernames.append(accInfo[0])
        accPasswords.append(accInfo[1])
        accFullNames.append(accInfo[2] + " " + accInfo[3])

  
if __name__ == '__main__':
  window = MainWindow()
  window.mainloop()