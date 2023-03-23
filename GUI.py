
# Author Matthew Gerola
# Assignment: CptS 427 Course Project 2023
# Date: ?/?/2023

import tkinter as tk
import tkinter.messagebox
from machine_learn import MachineLearn


class Phishing_GUI():

    def __init__(self):    
        self.email_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] #This will hold all the values that the user inputs to the program
        self.text_values = [0,0,0,0,0,0,0,0,0,0,0,0] #This will hold all the values that the user inputs for the text GUI
        self.forestModel = MachineLearn()
        self.create_Selection()
        
    def continueing(self,text,GUI):
        if text == "email":
                self.destroy_GUI(GUI)
                self.create_Email()
        else:
                self.destroy_GUI(GUI)
                self.create_Text()


    def create_Email(self):
        emailGUI = tk.Tk()
        emailGUI.geometry("525x525")
        emailGUI.configure(background="#5EA9BE")
        emailGUI.title("Email-Tool")

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

        tk.Label(emailGUI,text="Click on the values that are true for this email \nThe More Info button will provided more details about what each is asking.\nThe back button will take you back to the start.",background="#5EA9BE",font=("Times",10)).grid(row=0,column=0,columnspan=2,pady=8)
        
        tk.Label(emailGUI,text="Was there a sense of urgegncy in the email?",background="#5EA9BE").grid(row=1,column=0,padx=40)
        tk.Checkbutton(emailGUI,variable = Now, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=1,column=1)
        

        tk.Label(emailGUI,text="Was this an order confirmation/verification?",background="#5EA9BE").grid(row=2,column=0)
        tk.Checkbutton(emailGUI,variable = Confirm, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=2,column=1)
        
        tk.Label(emailGUI,text="Was the company compromised or account compromised?",background="#5EA9BE").grid(row=3,column=0)
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

        tk.Label(emailGUI,text="Is this email infomring you that you missed something?",background="#5EA9BE").grid(row=12,column=0)
        tk.Checkbutton(emailGUI,variable = Missed, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=12,column=1)

        tk.Label(emailGUI,text="Is this email asking for information?",background="#5EA9BE").grid(row=13,column=0)
        tk.Checkbutton(emailGUI,variable =Personal, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=13,column=1)

        moredetails = """
        Sense of Urgency: 
                \tThis has many buzy words some include Urgent, Mandatory, Now. The sense of this needs to be done now is felt.\n
        Order/Verification: 
                \tHyperlink to verify an account was made. Or an account was made and you need to click a link to verify.\n
        Compromised: 
                \tAn Account was compromised and you need to take some type of action to ensure nothing bad happens. Either the company or a personal account.\n
        Money: 
                \tDoes this email have money involved? Credit card debt needing to be paid or gift card given to you, paid position offered?\n
        Help a person out with a link provided: 
                \tDoes this email make it seem like the sender is looking out for you and the best thing to do is click the link they provided for convience?\n
        Is the email from the person who sent it: 
                \tDoes the @ match the company that sent the email some odd ones would be ....\n
        Mistakes: 
                \tAny grammar/misspellings or information that is not correct?\n
        Too Good: 
                \tA raffle and you won the grand prize or a gift card with a lot of money involved or catching a lucky break\n
        FOMO: 
                \tFOMO --> Fear of Missing Out. Does this email make you want to do whats in the email. Get a drink from a certain place, see what people are up to, \treconnect.\n
        Expecting: 
                \tWere you expecting to receive and email similar to this one or did you trigger an event to create the email?\n
                \tPerhaps you reset a password or signed in to an account from a different device.\n
        Was an Attachment included in the email: 
                \tWas an attachment of any kind included in the email sent to you?\n
        Informing: 
                \tIs this email telling you an event was missed and to view the current state you can click on a link that you don't know about? \n
        Asking for Information: 
                \tIs this email asking for more personal information and for it to be sent back for more details about something?\n
        """

        helping = tk.Button(emailGUI,text="More Info", width=8,height=2,command=lambda: tk.messagebox.showinfo("--More information--", moredetails),font=("Times",11)).grid(row=15,column=1,pady=15)
        back = tk.Button(emailGUI,text="Back", width=8,height=2,command=lambda: self.startofProgram(emailGUI) ,font=("Times",11)).grid(row=15,column=0,pady=15)
        move_on = tk.Button(emailGUI,text="Continue", width=8,height=2,command=lambda: self.resultsFromMachine(self.email_values,emailGUI),font=("Times",11)).grid(row=16,column=1)
        
    def create_Text(self):
        textGUI = tk.Tk()
        textGUI.geometry("525x525")
        textGUI.configure(background="#5EA9BE")
        textGUI.title("Text-Tool")

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
        
        tk.Label(textGUI,text="Click on the values that are true for this text \nThe More Info button will provided more details about what each is asking.\nThe back button will take you back to the start.",background="#5EA9BE",font=("Times",10)).grid(row=0,column=0,columnspan=2,pady=8)
        back = tk.Button(textGUI,text="Back", width=8,height=2,command=lambda: self.startofProgram(textGUI) ,font=("Times",11)).grid(row=15,column=0,pady=15)

        tk.Label(textGUI,text="Was money involved in the text?",background="#5EA9BE").grid(row=1,column=0)
        tk.Checkbutton(textGUI,variable = money, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=1,column=1)
        

        tk.Label(textGUI,text="Is this too good to be true?",background="#5EA9BE").grid(row=2,column=0)
        tk.Checkbutton(textGUI,variable = Too_Good, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=2,column=1)
        
        tk.Label(textGUI,text="Was the company compromised or account compromised?",background="#5EA9BE").grid(row=3,column=0)
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

        tk.Label(textGUI,text="Was there a use of buzz words to eleicie urgency in the text?",background="#5EA9BE").grid(row=10,column=0)
        tk.Checkbutton(textGUI,variable = buzz, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=10,column=1)
        

        tk.Label(textGUI,text="Does this text come from an odd number?",background="#5EA9BE").grid(row=11,column=0)
        tk.Checkbutton(textGUI,variable = oddnumber, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=11,column=1)
        
        tk.Label(textGUI,text="Do you know the person who sent the text?",background="#5EA9BE").grid(row=12,column=0)
        tk.Checkbutton(textGUI,variable = knowtheperson, onvalue=1,offvalue=0,height=1,width=2,background="#5EA9BE").grid(row=12,column=1)

        moredetails = """
        Money:
                \tDoes this email have money involved? Credit card debt needing to be paid or gift card given to you.\n
        Too Good:
                \tA raffle and you won the grand prize or a gift card with a lot of money involved or catching a lucky break\n
        Account Troubles:
                \tAn Account was compromised and you need to take some type of action to ensure nothing bad happens. Either the company or a personal account.\n
        Information:
                \tIs this email asking for more personal information?\n
        Conversation:
                \tDoes it seem like this person whats a conversation to start from the text?\n
        Link:
                \tWas a link provided, but weird looking?\n
        No relevance:
               \tDoes this seem like anyone could have gotten the text. Not very personal, sorta like a template?\n
        Pictures:
                \tWas a picture that was weird included in the text?\n
        Poor Grammar:
                \tIs poor grammar/spelling included in the text?\n
        Urgency:
                \tThis has many buzy words some include Urgent, Mandatory, Now. The sense of this needs to be done now is felt.\n
        Odd Number:
                \tIs the number from a weird zip code a quick google search should help with this question\n
        Know the Person who sent the text:
                \tDo you know the person who sent the message?\n

        """
        helping = tk.Button(textGUI,text="More Info", width=8,height=2,command=lambda: tk.messagebox.showinfo("--More information--", moredetails),font=("Times",11)).grid(row=15,column=1,pady=15)
        move_on = tk.Button(textGUI,text="Continue", width=8,height=2,command=lambda: self.resultsFromMachine(self.text_values,textGUI),font=("Times",11)).grid(row=16,column=1)
        

    def resultsFromMachine(self,valuesChosen,GUI):
        self.destroy_GUI(GUI)
        self.PhishingN()
        self.PhishingP()


    def startofProgram(self,GUI):
        self.destroy_GUI(GUI)
        self.create_Selection()


    def create_Selection(self):
        root = tk.Tk()
        root.geometry("450x450")
        root.configure(background="#5EA9BE")
        root.title("Phishing-Tool")    
        what_did_you_get = tk.Label(root,text="What type of message did you get email or text",font=("Times",11),background="#5EA9BE").pack(pady=5)
        please = tk.Label(root,text="Please click the one you received and it will take you \nto the correct checklist...",font=("Times",11),background="#5EA9BE").pack(pady=5)
        emailCheck = tk.Button(root, text="Email",width=12,height=2,command=lambda: self.continueing("email",root) ,font=("Times",11)).pack(pady=45)
        textCheck = tk.Button(root, text="Text",width=12,height=2,command=lambda: self.continueing("text",root) ,font=("Times",11)).pack()
        please = tk.Label(root,text="The creator is not liable for any damages that \nare sustained from using the program",font=("Times",8),background="#5EA9BE").pack(pady=75)
        root.mainloop()

    def destroy_GUI(self,GUI):
        GUI.destroy()

    def PhishingP(self):
        root = tk.Tk()
        root.geometry("325x325")
        root.configure(background="#86DC3D")
        root.title("Phishing-Positive")
        tk.Label(root,text="From what the Machine Learning has done it would appear\n this is indeed a phishing attempt.\n ",font=("Times",10),background="#86DC3D").grid(row=0,column=0)
        tk.Label(root,text="You should not click on any links that are provided \nand not download any attachements(if included).\n",font=("Times",10),background="#86DC3D").grid(row=1,column=0)
        tk.Label(root,text="If email please report this email to the abuse email your \nbusiness/university uses and delete the email.\n",font=("Times",10),background="#86DC3D").grid(row=2,column=0)
        tk.Label(root,text="If text please block and report this number \n built into your messaging app.\n",font=("Times",10),background="#86DC3D").grid(row=3,column=0)
        tk.Button(root,text="Restart", width=8,height=2,command=lambda: self.startofProgram(root) ,font=("Times",10)).grid(row=5,column=0,pady=15)


    def PhishingN(self):
        root = tk.Tk()
        root.geometry("325x325")
        root.configure(background="#E60026")
        root.title("Phishing-Negative")
        tk.Label(root,text="From what the Machine Learning has done it would appear\n this is NOT a phishing attempt.\n ",font=("Times",10),background="#E60026").grid(row=0,column=0)
        tk.Label(root,text="This may not be 100% though with the better \nphishing attempts each year.\n",font=("Times",10),background="#E60026").grid(row=1,column=0)
        tk.Label(root,text="So if you are worried about an account or something,\n independently go to the site and see if everything is ok.\n",font=("Times",10),background="#E60026").grid(row=2,column=0)
        tk.Label(root,text="Do Not Click on the link(s) provided unless\n you are 100% sure they are not malicious.\n",font=("Times",10),background="#E60026").grid(row=3,column=0)
        tk.Button(root,text="Restart", width=8,height=2,command=lambda: self.startofProgram(root) ,font=("Times",10)).grid(row=5,column=0,pady=15)
