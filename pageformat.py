from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black, lightgrey
from reportlab.lib.pagesizes import A4
import pandas as pd

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

        

    def writeNotes(self):

        data = ExtractData()

        name, sender_class, recipients, recipients_class, message = data.compile_data()

        textObject = self.pdf.beginText()
        textObject.setTextOrigin(30,800)
        textObject.textLines('''
        My name is Natasha Alia
        ''')
        self.pdf.drawText(textObject)


    def cookie_project(self):

        self.create_grid()
        self.pdf.save()

class ExtractData:

    def __init__(self):

        self.dataFrame = pd.read_excel("cookie_project.xlsx")
        
    def compile_data(self):

        self.name_list = self.dataFrame["Name "]
        self.sender_class = self.dataFrame["Class"]
        self.recipients = self.dataFrame["Recipients"]
        self.message = self.dataFrame["message"]
        self.recipients_class = self.dataFrame["recipients_class"]
        
        return self.name_list, self.sender_class, self.recipients, self.recipients_class, self.message 

if __name__ == '__main__':
    
    PageFormat().cookie_project()
    ExtractData().compile_data()


