from ssl import create_default_context
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black, lightgrey
from reportlab.lib.pagesizes import A4

def drawMyRuler(pdf):
    
    # Create a coordinate system for easy reference
    pdf.drawString(0,0, "0")
    pdf.drawString(100,0, "100")
    pdf.drawString(200,0, "200")
    pdf.drawString(300,0, "300")
    pdf.drawString(400,0, "400")
    pdf.drawString(500,0, "500")
    pdf.drawString(600,0, "600")


    pdf.drawString(0,0,"0")
    pdf.drawString(0,100,"100")
    pdf.drawString(0,200,"200")
    pdf.drawString(0,300,"300")
    pdf.drawString(0,400,"400")
    pdf.drawString(0,500,"500")
    pdf.drawString(0,600,"600")
    pdf.drawString(0,700,"700")
    pdf.drawString(0,800,"800")
    pdf.drawString(0,900,"900")
    pdf.drawString(0,1000,"1000")
    pdf.drawString(0,1100,"1100")

def smallGrids(pdf):
    
    pdf.setStrokeColor(lightgrey)
    # Create small grids to make it easier to adjust our fonts
    for column in range(0,600, 10):
        pdf.line(column, 0, column, 900)

    for row in range(0,900,10):
        pdf.line(0, row, 600, row)
        
    

def create_grid(pdf):

    # Create an offset for our grid
    offset_x = 20
    offset_y = 100 # 3*cm

    # Create a small grids to make it easier for us to position our fonts
    smallGrids(pdf)
    # Draw the coordinate system
    drawMyRuler(pdf)

    # Create a grid of 4 columns
    for i in range(1):

        # Define the width and length of each grid which in this case is 6.5 cm
        x = y = 180

        # Define the columns and rows of the grid
        x_grid = [x*0, x*1, x*2, x*3]
        y_grid = [y*0, y*1, y*2, y*3, y*4]

        # Draw the grid onto our pdf file
        pdf.setStrokeColor(black)
        pdf.translate(offset_x, offset_y)
        pdf.grid(x_grid, y_grid)
        
        # End page
        pdf.showPage()

def cookie_project():

    # Create the canvas with the given name
    pdf = canvas.Canvas("pdf_file/test.pdf", pagesize=A4)
    create_grid(pdf)
    #smallGrids(pdf)
    pdf.save()


if __name__ == '__main__':
    cookie_project()
    #smallGrids(pdf)
    print(cm)


