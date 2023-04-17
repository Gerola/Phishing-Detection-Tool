
# Author Matthew Gerola
# Assignment: CptS 427 Course Project 2023
# Date: 4/17/2023

import tkinter as tk
import tkinter.messagebox
from machine_learn import MachineLearn


class Phishing_GUI():

    def __init__(self):
        #Get the machine learning object
        self.forestModel = MachineLearn()
        #Start the beginning of the program by having the selection GUI
        self.create_Selection()
        
    def continueing(self,text,GUI):
        #       Decide where to go after the user chooses
        #       what type of phishing attempt they received

        #Go to the email GUI and questions
        if text == "email":
                self.destroy_GUI(GUI)
                self.create_Email()
        else:
                self.destroy_GUI(GUI)
                self.create_Text()
        #Go to the text GUI and questions


    def create_Email(self):
        #-----------------Create the GUI-----------------
        emailGUI = tk.Tk()
        emailGUI.geometry("525x525")
        emailGUI.configure(background="#5EA9BE")
        emailGUI.title("Email-Tool")
        #------------------------------------------------

        #This will be all the variables that
        #hold the values that the user will click on
        Now = tk.IntVar()
        Confirm = tk.IntVar()
        Compromise = tk.IntVar()
        Money = tk.IntVar()
        Best_Interest = tk.IntVar()
        emailat = tk.IntVar()
        Mistakes= tk.IntVar()
        Too_Good= tk.IntVar()
        FOMO= tk.IntVar()
        Expect= tk.IntVar()
        attach= tk.IntVar()
        Missed= tk.IntVar()
        Personal= tk.IntVar()

        #Opening Label:
        tk.Label(emailGUI,text="Click on the values that are true for this email \nThe More Info button will provided more details about what each is asking.\nThe back button will take you back to the start.",background="#5EA9BE",font=("Times",10)).grid(row=0,column=0,columnspan=2,pady=8)
        
        #All the Checkboxes that the user will click on if the phishing email satisifies the given thing

        tk.Label(emailGUI,text="Was there a sense of urgency in the email?",background="#5EA9BE").grid(row=1,column=0,padx=40)
        tk.Checkbutton(emailGUI,variable = Now, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=1,column=1)
        
        tk.Label(emailGUI,text="Was this a confirmation/verification email?",background="#5EA9BE").grid(row=2,column=0)
        tk.Checkbutton(emailGUI,variable = Confirm, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=2,column=1)
        
        tk.Label(emailGUI,text="Was a company compromised or account compromised?",background="#5EA9BE").grid(row=3,column=0)
        tk.Checkbutton(emailGUI,variable = Compromise, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=3,column=1)

        tk.Label(emailGUI,text="Is there money involved?",background="#5EA9BE").grid(row=4,column=0)
        tk.Checkbutton(emailGUI,variable = Money, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=4,column=1)

        tk.Label(emailGUI,text="Is the email making it seem like the best option is to click the link provided?",background="#5EA9BE").grid(row=5,column=0)
        tk.Checkbutton(emailGUI,variable = Best_Interest, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=5,column=1)

        tk.Label(emailGUI,text="Is this email from the correct company/person?",background="#5EA9BE").grid(row=6,column=0)
        tk.Checkbutton(emailGUI,variable = emailat, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=6,column=1)

        tk.Label(emailGUI,text="Are there any mistakes in the email?",background="#5EA9BE").grid(row=7,column=0)
        tk.Checkbutton(emailGUI,variable = Mistakes, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=7,column=1)

        tk.Label(emailGUI,text="Is this too good to be true?",background="#5EA9BE").grid(row=8,column=0)
        tk.Checkbutton(emailGUI,variable = Too_Good, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=8,column=1)

        tk.Label(emailGUI,text="Is this email making you have FOMO?",background="#5EA9BE").grid(row=9,column=0)
        tk.Checkbutton(emailGUI,variable = FOMO, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=9,column=1)

        tk.Label(emailGUI,text="Were you expecting this email?",background="#5EA9BE").grid(row=10,column=0)
        tk.Checkbutton(emailGUI,variable = Expect, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=10,column=1)

        tk.Label(emailGUI,text="Was an attachment included?",background="#5EA9BE").grid(row=11,column=0)
        tk.Checkbutton(emailGUI,variable = attach, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=11,column=1)

        tk.Label(emailGUI,text="Is this email informing you that you missed something?",background="#5EA9BE").grid(row=12,column=0)
        tk.Checkbutton(emailGUI,variable = Missed, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=12,column=1)

        tk.Label(emailGUI,text="Is this email asking for information?",background="#5EA9BE").grid(row=13,column=0)
        tk.Checkbutton(emailGUI,variable =Personal, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=13,column=1)


        #       If the user gets confused, when the more details is pressed the following will be displayed and
        #       hopefully clear up any confusion
        moredetails = """
        Sense of Urgency: 
                \tThis email has buzzword, some include Urgent, Mandatory, Now. The sense of this needs to be done now is felt.\n
        Order/Verification: 
                \tHyperlink to verify an account was made. Or an order was placed and you were given the details.\n
        Compromised: 
                \tAn Account was compromised and you need to take some type of action to ensure nothing bad happens. Either the company or a personal account.\n
        Money: 
                \tDoes this email have money involved? Credit card debt needing to be paid or gift card given to you, paid position offered?\n
        Help a person out with a link provided: 
                \tDoes this email make it seem like the sender is looking out for you and the best thing to do is click the link they provided for convenience?\n
        Is the email from the person who sent it: 
                \tDoes the @ match the company that sent the email if not then it can't be trusted.\n
                \tDoes the person who sent it match the email?\n
        Mistakes: 
                \tAny grammar/misspellings or information that is not correct?\n
        Too Good: 
                \tA raffle and you won the grand prize or a gift card with a lot of money involved or catching a lucky break like a high paying job.\n
        FOMO: 
                \tFOMO --> Fear of Missing Out. Does this email make you want to do what's in the email? Get a drink from a certain place, see what people are up to reconnect.\n
        Expecting: 
                \tWere you expecting to receive and email similar to this one or did you trigger an event to create the email?\n
                \tPerhaps you reset a password or signed in to an account from a different device.\n
        Was an Attachment included in the email: 
                \tWas an attachment of any kind included in the email sent to you (PDF)?\n
        Informing: 
                \tIs this email telling you an event was missed and to view the current state you can click on a link? \n
        Asking for Information: 
                \tIs this email asking for more personal information and for it to be sent back for more details about something?\n
        """

        #The helping, go back, and continue buttons are below
        helping = tk.Button(emailGUI,text="More Info", width=8,height=2,command=lambda: tk.messagebox.showinfo("--More information--", moredetails),font=("Times",11)).grid(row=15,column=1,pady=15)
        back = tk.Button(emailGUI,text="Back", width=8,height=2,command=lambda: self.startofProgram(emailGUI) ,font=("Times",11)).grid(row=15,column=0,pady=15)
        move_on = tk.Button(emailGUI,text="Continue", width=8,height=2,command=lambda: self.resultsFromMachine([Now.get(),Confirm.get(),Compromise.get(),Money.get(),Best_Interest.get(),emailat.get(),Mistakes.get(),Too_Good.get(),FOMO.get(),Expect.get(),attach.get(),Missed.get(),Personal.get()],emailGUI,"Email"),font=("Times",11)).grid(row=16,column=1)
        
    def create_Text(self):
        #-----------Create the text GUI-----------
        textGUI = tk.Tk()
        textGUI.geometry("525x525")
        textGUI.configure(background="#5EA9BE")
        textGUI.title("Text-Tool")
        #-----------------------------------------

        #All the variables that will hold the values for the possible phishing text message
        money = tk.IntVar()
        Too_Good = tk.IntVar()
        accounttroubles = tk.IntVar()
        information = tk.IntVar()
        conversation = tk.IntVar()
        link = tk.IntVar()
        Norel= tk.IntVar()
        Pictures= tk.IntVar()
        poorgrammar= tk.IntVar()
        buzz= tk.IntVar()
        oddnumber= tk.IntVar()
        knowtheperson= tk.IntVar()
        
        #Opening Label
        tk.Label(textGUI,text="Click on the values that are true for this text \nThe More Info button will provided more details about what each is asking.\nThe back button will take you back to the start.",background="#5EA9BE",font=("Times",10)).grid(row=0,column=0,columnspan=2,pady=8)
        back = tk.Button(textGUI,text="Back", width=8,height=2,command=lambda: self.startofProgram(textGUI) ,font=("Times",11)).grid(row=15,column=0,pady=15)
        #The back button

        #All the Checkboxes that the user will click on if the phishing text satisfies the given thing
        
        tk.Label(textGUI,text="Was money involved in the text?",background="#5EA9BE").grid(row=1,column=0)
        tk.Checkbutton(textGUI,variable = money, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=1,column=1)
        
        tk.Label(textGUI,text="Is this too good to be true?",background="#5EA9BE").grid(row=2,column=0)
        tk.Checkbutton(textGUI,variable = Too_Good, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=2,column=1)
        
        tk.Label(textGUI,text="Was a company compromised or account compromised?",background="#5EA9BE").grid(row=3,column=0)
        tk.Checkbutton(textGUI,variable = accounttroubles, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=3,column=1)

        tk.Label(textGUI,text="Is this email asking for more information regarding you?",background="#5EA9BE").grid(row=4,column=0)
        tk.Checkbutton(textGUI,variable = information, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=4,column=1)
        
        tk.Label(textGUI,text="Does it seem like they want to start a conversation?",background="#5EA9BE").grid(row=5,column=0)
        tk.Checkbutton(textGUI,variable = conversation, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=5,column=1)
        
        tk.Label(textGUI,text="Was a link provided that they want you to go to?",background="#5EA9BE").grid(row=6,column=0)
        tk.Checkbutton(textGUI,variable = link, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=6,column=1)

        tk.Label(textGUI,text="Could this text be given to someone else and it would have the same effect?",background="#5EA9BE").grid(row=7,column=0)
        tk.Checkbutton(textGUI,variable = Norel, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=7,column=1)
        
        tk.Label(textGUI,text="Was a weird picture in the text?",background="#5EA9BE").grid(row=8,column=0)
        tk.Checkbutton(textGUI,variable = Pictures, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=8,column=1)
        
        tk.Label(textGUI,text="Was poor grammar/spelling present in the text?",background="#5EA9BE").grid(row=9,column=0)
        tk.Checkbutton(textGUI,variable = poorgrammar, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=9,column=1)

        tk.Label(textGUI,text="Was there a sense of urgency in the text?",background="#5EA9BE").grid(row=10,column=0)
        tk.Checkbutton(textGUI,variable = buzz, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=10,column=1)
        
        tk.Label(textGUI,text="Does this text come from an odd number?",background="#5EA9BE").grid(row=11,column=0)
        tk.Checkbutton(textGUI,variable = oddnumber, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=11,column=1)
        
        tk.Label(textGUI,text="Do you know the person who sent the text?",background="#5EA9BE").grid(row=12,column=0)
        tk.Checkbutton(textGUI,variable = knowtheperson, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=12,column=1)

        

        #       If the user gets confused, when the more details is pressed the following will be displayed and
        #       hopefully clear up any confusion

        moredetails = """
        Money:
                \tDoes this text have money involved? Credit card debt needing to be paid or gift card given to you.\n
        Too Good:
                \tA raffle and you won the grand prize or a gift card with a lot of money involved or catching a lucky break\n
        Account Troubles:
                \tAn Account was compromised and you need to take some type of action to ensure nothing bad happens. Either the company or a personal account.\n
        Information:
                \tIs this text asking for more personal information?\n
        Conversation:
                \tDoes it seem like this person wants a conversation to start from the text?\n
        Link:
                \tWas a link provided, but weird looking?\n
        No relevance:
               \tDoes this seem like anyone could have gotten the text? Not very personal, sorta like a template?\n
        Pictures:
                \tWas a picture that was weird included in the text?\n
        Poor Grammar:
                \tIs poor grammar/spelling included in the text?\n
        Urgency:
                \tThis has many buzzwords, some include Urgent, Mandatory, Now. The sense of this needs to be done now is felt.\n
        Odd Number:
                \tIs the number from a weird zip code a quick google search should help with this question\n
        Know the Person who sent the text:
                \tDo you know the person who sent the message, perhaps you have already talked on this message thread?\n

        """
        
        #The helping button and the continue button
        helping = tk.Button(textGUI,text="More Info", width=8,height=2,command=lambda: tk.messagebox.showinfo("--More information--", moredetails),font=("Times",11)).grid(row=15,column=1,pady=15)
        move_on = tk.Button(textGUI,text="Continue", width=8,height=2,command=lambda: self.resultsFromMachine([money.get(),Too_Good.get(),accounttroubles.get(),information.get(),conversation.get(),link.get(),Norel.get(),Pictures.get(),poorgrammar.get(),buzz.get(),oddnumber.get(),knowtheperson.get()],textGUI,"Text"),font=("Times",11)).grid(row=16,column=1)
        

        #This is the function that will decide what GUI to display after the values have been run on the
        #machine learning trees
    def resultsFromMachine(self,valuesChosen,GUI,whattree):
        self.destroy_GUI(GUI)
        #Email tree
        if(whattree == "Email"):
                if(self.forestModel.results("Email",valuesChosen)):
                        self.PhishingP()
                else:
                        self.PhishingN()
        else:#Text tree
                if(self.forestModel.results("Text",valuesChosen)):
                        self.PhishingP()
                else:
                        self.PhishingN()
                


        #When the user wants to go back start the beginning of the program 
        #destroy the GUI that was being displayed
    def startofProgram(self,GUI):
        self.destroy_GUI(GUI)
        self.create_Selection()


    def create_Selection(self):
        #-----------Create the starting Menu-----------
        root = tk.Tk()
        root.geometry("450x450")
        root.configure(background="#5EA9BE")
        root.title("Phishing-Tool")    
        what_did_you_get = tk.Label(root,text="What type of message did you get email or text",font=("Times",11),background="#5EA9BE").pack(pady=5)
        please = tk.Label(root,text="Please click the one you received and it will take you \nto the correct checklist...",font=("Times",11),background="#5EA9BE").pack(pady=5)
        emailCheck = tk.Button(root, text="Email",width=12,height=2,command=lambda: self.continueing("email",root) ,font=("Times",11)).pack(pady=45)
        textCheck = tk.Button(root, text="Text",width=12,height=2,command=lambda: self.continueing("text",root) ,font=("Times",11)).pack()
        please = tk.Label(root,text="The creator is not liable for any damages that \nare sustained from using the program to diagnose phishing attempts",font=("Times",8),background="#5EA9BE").pack(pady=75)
        root.mainloop()
        #----------------------------------------------

        #Get rid of the GUI that is being displayed to the user
    def destroy_GUI(self,GUI):
        GUI.destroy()

#E60026 Color of the GUI
    def PhishingP(self):
        #--------------Create the Phishing Positive GUI-------------
        root = tk.Tk()
        root.geometry("325x325")
        root.configure(background="#ff9194")
        root.title("Phishing-Positive")
        tk.Label(root,text="From what the Machine Learning has done it would appear\n this is indeed a phishing attempt.\n ",font=("Times",10),background="#ff9194").grid(row=0,column=0)
        tk.Label(root,text="You should not click on any links that are provided \nand not download any attachements(if included).\n",font=("Times",10),background="#ff9194").grid(row=1,column=0)
        tk.Label(root,text="If email please report this email to the abuse email your \nbusiness/university uses and delete the email.\n",font=("Times",10),background="#ff9194").grid(row=2,column=0)
        tk.Label(root,text="If text please block and report this number \n built into your messaging app.\n",font=("Times",10),background="#ff9194").grid(row=3,column=0)
        tk.Button(root,text="Restart", width=8,height=2,command=lambda: self.startofProgram(root) ,font=("Times",10)).grid(row=5,column=0,pady=15)#Restart the Program
        #-----------------------------------------------------------
        

#86DC3D Color of the GUI
    def PhishingN(self):
        #--------------Create the Phishing Negative GUI--------------
        root = tk.Tk()
        root.geometry("325x325")
        root.configure(background="#86DC3D")
        root.title("Phishing-Negative")
        tk.Label(root,text="From what the Machine Learning has done it would appear\n this is NOT a phishing attempt.\n ",font=("Times",10),background="#86DC3D").grid(row=0,column=0)
        tk.Label(root,text="This may not be 100% though with the better \nphishing attempts each year.\n",font=("Times",10),background="#86DC3D").grid(row=1,column=0)
        tk.Label(root,text="So if you are worried about an account or something related,\n independently go to the service and see if everything is ok.\n",font=("Times",10),background="#86DC3D").grid(row=2,column=0)
        tk.Label(root,text="Do Not Click on the link(s) or download anything provided \nunless you are 100% sure they are not malicious.\n",font=("Times",10),background="#86DC3D").grid(row=3,column=0)
        tk.Button(root,text="Restart", width=8,height=2,command=lambda: self.startofProgram(root) ,font=("Times",10)).grid(row=5,column=0,pady=15)#Restart the Program
        #------------------------------------------------------------
        