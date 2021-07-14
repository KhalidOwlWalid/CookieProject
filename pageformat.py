import collections
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black, lightgrey
from reportlab.lib.pagesizes import A4
import pandas as pd

from collections import defaultdict

class PageFormat:

    def __init__(self):

        # Create the canvas with the given name
        self.pdf = canvas.Canvas("pdf_file/test.pdf", pagesize=A4)

    def drawMyRuler(self):
        
        # Create a coordinate system for easy reference
        self.pdf.drawString(0,0, "0")
        self.pdf.drawString(100,0, "100")
        self.pdf.drawString(200,0, "200")
        self.pdf.drawString(300,0, "300")
        self.pdf.drawString(400,0, "400")
        self.pdf.drawString(500,0, "500")
        self.pdf.drawString(600,0, "600")


        self.pdf.drawString(0,0,"0")
        self.pdf.drawString(0,100,"100")
        self.pdf.drawString(0,200,"200")
        self.pdf.drawString(0,300,"300")
        self.pdf.drawString(0,400,"400")
        self.pdf.drawString(0,500,"500")
        self.pdf.drawString(0,600,"600")
        self.pdf.drawString(0,700,"700")
        self.pdf.drawString(0,800,"800")
        self.pdf.drawString(0,900,"900")
        self.pdf.drawString(0,1000,"1000")
        self.pdf.drawString(0,1100,"1100")

    def smallGrids(self):
        
        self.pdf.setStrokeColor(lightgrey)
        # Create small grids to make it easier to adjust our fonts
        for column in range(0,600, 10):
            self.pdf.line(column, 0, column, 900)

        for row in range(0,900,10):
            self.pdf.line(0, row, 600, row)
  
    def create_grid(self):

        # Create an offset for our grid
        offset_x = 20
        offset_y = 100 # 3*cm

        # Create a small grids to make it easier for us to position our fonts
        self.smallGrids()
        # Draw the coordinate system
        self.drawMyRuler()

        self.writeNotes()

        # Create a grid of 4 columns
        for i in range(1):

            # Define the width and length of each grid which in this case is 6.5 cm
            x = y = 180

            # Define the columns and rows of the grid
            x_grid = [x*0, x*1, x*2, x*3]
            y_grid = [y*0, y*1, y*2, y*3, y*4]

            # Draw the grid onto our pdf file
            self.pdf.setStrokeColor(black)
            self.pdf.translate(offset_x, offset_y)
            self.pdf.grid(x_grid, y_grid)
            
            # End page
            self.pdf.showPage()

    def checkMessage(self):

        message = 'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project'
        words_list = message.split()

        arranged_words = []
        for word in words_list:
            pass

        
    def writeNotes(self):

        #data = ExtractData()

        #name, sender_class, recipients, recipients_class, message_list = data.compile_data()
        messages = [['Khalid Al-Walid', 19.3, 
                    'name_1234', 14.2, 
                    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project'],
                    ['Khalid Al-Walid', 19.3, 
                    'name_1234', 14.2, 
                    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project']]

        """
        #################### FOR REFERENCE ####################
        messages[n_message][0] = Name of sender
        messages[n_message][1] = Sender's class
        messages[n_message][2] = Recipient
        messages[n_message][3] = Recipient's class
        messages[n_message][4] = Message
        """
        i = 1

        for message in messages:
            textObject = self.pdf.beginText()
            textObject.setTextOrigin(30,800)
            textObject.setFont("Times-Bold", 8)
            textObject.textLines('''To : ''' + message[2])
            textObject.textLines(message[4])
            self.pdf.drawText(textObject)


        ### Guide for tomorrow ###
        # Create a function that counts the number of characters in a mesage
        # Create a function that groups words together (for instance 5 words on each line)
        # Append it into a single list
        # Iterate through the list using for loop
        # and each elements will be the argument of the textLines() function





        ### Count the number of characters and arrange the text accordingly ###
        ### If the number of character exceeds a certain amount, you can try reducing the size of the font ###
        
        ### Draw the text onto the canvas ###
        ### Position the name and recipient accordingly ###

    def cookie_project(self):

        self.create_grid()
        self.pdf.save()

class ExtractData:

    def __init__(self):

        self.dataFrame = pd.read_excel("cookie_project.xlsx")
        
    def seperated_data(self):

        self.name_list = self.dataFrame["Name "]
        self.sender_class = self.dataFrame["Class"]
        self.recipients = self.dataFrame["Recipients"]
        self.message = self.dataFrame["message"]
        self.recipients_class = self.dataFrame["recipients_class"]
        
        return self.name_list, self.sender_class, self.recipients, self.recipients_class, self.message 

    def compiled_data(self):

        return self.dataFrame.values.tolist()

    def split_message(self):

        message = self.compiled_data()
        
        # Initialized an empty dictionary with default values
        dictionary = collections.defaultdict(list)

        for i, split in enumerate(message):
            dictionary["Name"].append(message[i][0])
            dictionary["Class"].append(message[i][1])
            dictionary["Recipient"].append(message[i][2])
            dictionary["Recipient_class"].append(message[i][3])
            dictionary["Message"].append(message[i][4])

        #print(dictionary)
        
        new_message = []
        final_message = []
        
        message_length = 0

        #print(dictionary["Message"])

        '''
        I think that it will be much simpler if you were to make a list which consists of only one sentence where it is much
        easier to handle rather than the fact that I take a huge amount of data and try to combine it in a single dictionary
        '''

        for i, sentence in enumerate(dictionary["Message"]):
            
            split_string = list(dictionary["Message"].split(" "))

            for j, word in enumerate(split_string):

                get_length = len(word) + 1
                message_length += get_length

                # We have to check if the word is the last one in the list so that we would append it before we break the loop
                if word == split_string[-1]:
                    new_message.append(word)
                    new_message = ' '.join(new_message)
                    final_message.append(new_message)
                    new_message = []
                    message_length = 0

                # Check the length of the total characters in one line so that it does not exceed the grid
                if message_length < 35:
                    new_message.append(word)
                    #print(new_message)

                # If it exceeds, clear the new_message list and set the message_length back to zero
                elif message_length > 35:
                    new_message.append(word)
                    new_message = ' '.join(new_message)
                    final_message.append(new_message)
                    new_message = []
                    message_length = 0
                

        print(final_message)


def split_message():

    message = ['My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project']
    message = message[0].split()
    new_message = []
    final_message = []
    
    message_length = 0

    for i, word in enumerate(message):

        get_length = len(message[i]) + 1
        message_length += get_length

        # We have to check if the word is the last one in the list so that we would append it before we break the loop
        if word == message[-1]:
            new_message.append(message[i])
            new_message = ' '.join(new_message)
            final_message.append(new_message)
            new_message = []
            message_length = 0

        # Check the length of the total characters in one line so that it does not exceed the grid
        if message_length < 35:
            new_message.append(message[i])
            print(new_message)

        # If it exceeds, clear the new_message list and set the message_length back to zero
        elif message_length > 35:
            new_message.append(message[i])
            new_message = ' '.join(new_message)
            final_message.append(new_message)
            new_message = []
            message_length = 0
        

    print(final_message)


def test():
    
    from collections import defaultdict

    message = [['Natasha Alia', 19.3, 'name_1296', 14.2, 
    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project'], 
    ['Khalid Al-Walid', 19.3, 'name_1297', 14.2, 
    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project'], 
    ['Peekabo', 19.3, 'name_1298', 14.2, 
    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project']]

    dictionary = collections.defaultdict(list)
    print(dictionary)

    for i, split in enumerate(message):
        dictionary["Name"].append(message[i][0])
        dictionary["Class"].append(message[i][1])
        dictionary["Recipient"].append(message[i][2])
        dictionary["Recipient_class"].append(message[i][3])
        dictionary["Message"].append(message[i][4])

    print(dictionary)


    
if __name__ == '__main__':
    
    #PageFormat().cookie_project()
    ExtractData().split_message()
    #test()
    #ExtractData().compiled_data()
