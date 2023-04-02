
# Author Matthew Gerola
# Assignment: CptS 427 Course Project 2023
# Date: ?/?/2023


from sklearn.ensemble import RandomForestClassifier


class MachineLearn():
    def __init__(self):
        self.text = []
        self.textValues = []
        
        self.email = []
        self.emailValues = []
        
        #The Trees that will be used to diagnose a phishing attempt
        self.emailTree = RandomForestClassifier(n_estimators = 12, max_depth = 3, random_state = 0)
        self.textTree = RandomForestClassifier(n_estimators = 12, max_depth = 3, random_state = 0)

        self.setup()
        self.train()

    def setup(self):
        #Read in the Data that will be used to train the trees:

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
        readT.close()
    
    def train(self):
        #----------Fit the trees so they can be used to diagnose phishing attempts----------
        self.emailTree.fit(self.email,self.emailValues)
        self.textTree.fit(self.text,self.textValues)
        #-----------------------------------------------------------------------------------


    def results(self,Ptype,values):
        #--------Get the results from the user inputs and diagnose the email/text as phishing or not--------
        if Ptype == "Email":
            return self.emailTree.predict([values])#Email
        return self.textTree.predict([values]) #Text message
        #---------------------------------------------------------------------------------------------------