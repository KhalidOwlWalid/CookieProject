import collections
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black, lightgrey
from reportlab.lib.pagesizes import A4
import pandas as pd

from datahandling import ExtractData

from collections import defaultdict

global x 

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
        #self.smallGrids()
        # Draw the coordinate system
        #self.drawMyRuler()

        self.writeNotes()
        '''
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
        '''
    # writeNotes only return a single message of the sender 

    def writeNotes(self):

        x_pos = 30
        y_pos = 800
        n_grid = 1
        n_row = 1
        num_printedMessage = 0
        font_size = 8
        offset_x = 20
        offset_y = 100 # 3*cm

        
        data = ExtractData().compiled_data()

        while num_printedMessage != len(data):

            for n_message in range(len(data)):
                
                try:
                    if n_row == 4 and n_grid % 4 == 0:

                        x_pos = 30
                        y_pos = 800
                        n_row = 1
                        n_grid = 1

                        # Define the width and length of each grid which in this case is 6.5 cm
                        x = y = 180

                        # Define the columns and rows of the grid
                        x_grid = [x*0, x*1, x*2, x*3]
                        y_grid = [y*0, y*1, y*2, y*3, y*4]

                        # Draw the grid onto our pdf file
                        self.pdf.setStrokeColor(black)
                        self.pdf.translate(offset_x, offset_y)
                        self.pdf.grid(x_grid, y_grid)
                
                        self.pdf.showPage()

                    if n_grid % 4 == 0:
                        n_grid = 1
                        n_row += 1
                        y_pos -= 180
                        x_pos = 30

                        print("Going next row")
                        message = ExtractData().split_message(n_message)

                        textObject = self.pdf.beginText()
                        textObject.setTextOrigin(x_pos,y_pos)
                        x_pos += 180
                        textObject.setFont("Times-Bold", font_size)
                        textObject.textLines('''To : ''' )
                        textObject.textLine("       ")

                        for line in message:          
                            textObject.textLine(line)

                        self.pdf.drawText(textObject)
                        

                    elif n_grid % 4 != 0:
                        
                        print("This is message number: ", num_printedMessage)
                        message = ExtractData().split_message(n_message)

                        textObject = self.pdf.beginText()
                        textObject.setTextOrigin(x_pos,y_pos)
                        x_pos += 180
                        textObject.setFont("Times-Bold", font_size)
                        textObject.textLines('''To : ''' )
                        textObject.textLine("       ")

                        for line in message:          
                            textObject.textLine(line)

                        self.pdf.drawText(textObject)

                except:
                    print(num_printedMessage)

                num_printedMessage += 1
                n_grid += 1

        x = y = 180

        # Define the columns and rows of the grid
        x_grid = [x*0, x*1, x*2, x*3]
        y_grid = [y*0, y*1, y*2, y*3, y*4]

        # Draw the grid onto our pdf file
        self.pdf.setStrokeColor(black)
        self.pdf.translate(offset_x, offset_y)
        self.pdf.grid(x_grid, y_grid)

        self.pdf.showPage()


    def cookie_project(self):

        self.create_grid()
        self.pdf.save()
