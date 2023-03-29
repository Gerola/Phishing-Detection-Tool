
# Author Matthew Gerola
# Assignment: CptS 427 Course Project 2023
# Date: ?/?/2023

#import more things that are needed in the future

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text


class MachineLearn():
    def __init__(self):
        self.text = []
        self.textValues = []
        
        self.email = []
        self.emailValues = []
        
        self.emailTree = RandomForestClassifier(n_estimators = 12, max_depth = 3, random_state = 0)
        self.textTree = RandomForestClassifier(n_estimators = 12, max_depth = 3, random_state = 0)

        self.setup()
        self.train()

    def setup(self):
        #Read in the email data
        readE = open("email_data.csv","r")
        for y in readE:
            if(y[0] == "0" or y[0] == "1"):
                y = y.replace("\n","")
                values = []
                for number in range(0,len(y)-1):
                    if y[number] == "1" or y[number] == "0":
                        values.append(int(y[number]))
                self.emailValues.append(int(y[26]))
                self.email.append(values)
            else:
                continue
        readE.close()
        
        #Read in the text data
        readT = open("text_data.csv","r")
        for y in readT:
            if(y[0] == "0" or y[0] == "1"):
                y = y.replace("\n","")
                values = []
                for number in range(0,len(y)-1):
                    if y[number] == "1" or y[number] == "0":
                        values.append(int(y[number]))
                self.textValues.append(int(y[24]))
                self.text.append(values)
            else:
                continue
        # self.text = pd.DataFrame(data=self.text[1:],columns=self.text[0])
        readT.close()
    
    def train(self):

        #  = clf.fit(X,Y)
        # # name = ["Do Now","Confirmation email,Account/System Compromise","Money Involved","Help Person Out/Hyperlink Provided for Convience","email from said company no weird a tag","Spelling Mistakes","Too Good to Be True","FOMO","Expecting/You did the action","Attachment Included","Missed somthing","Asking for Personal Information","Outcome"]
        # r = export_text(clf,feature_names=name)
        # print(clf.predict([[1,0,0,1,1,0,0,0,0,0,0,0,0]]))
        # print(r)
        #Fit the Data into the trees so they can be used to diagnose a phishing attempt
        self.emailTree.fit(self.email,self.emailValues)
        self.textTree.fit(self.text,self.textValues)

        # print(textTree.predict([[0,0,0,0,1,1,0,1,0,0,0,1]]))
        # print(clf2.predict([[0,0,0,1,0,1,0,0,0,1,0,0,0]]))
    
    def results(self,Ptype,values):
        if Ptype == "Email":
            return self.emailTree.predict([values])
        return self.textTree.predict([values])
