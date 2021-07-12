from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

class Message:

    from reportlab.pdfgen import canvas

    def __init__(self):
        self.path = "pdf_file/test.pdf"
        self.list = ['message1','message2','message3','message4','message5','message6',
                    'message7','message8','message9','message10','message11','message12']
        self.offset_x = 0.7*cm
        self.offset_y = 1*cm
        self.index = 1
        self.box_number = 1

    def drawMyRuler(self, canvas):

        from reportlab.pdfgen import canvas

        

    def create_grid(self, canvas):

        from reportlab.lib.units import cm
        from reportlab.lib.colors import black
        
        # Create a grid of 4 columns
        for i in range(5):

            # Define the width and length of each grid which in this case is 6.5 cm
            x = y = 6.5*cm

            # Define the columns and rows of the grid
            x_grid = [x*0, x*1, x*2, x*3]
            y_grid = [y*0, y*1, y*2, y*3, y*4]

            # Draw the grid onto our pdf file
            pdf = canvas
            pdf.setStrokeColor(black)
            pdf.translate(self.offset_x, self.offset_y)
            pdf.grid(x_grid, y_grid)
    
            # Draw fonts onto our pdf file
            #c.setFont("Times-Roman", 20)
            #c.drawString(0,0, "y")
            
            # End page
            pdf.showPage()

    def create_pdf(self):

        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4

        # Name our pdf file and set its pagesize as an A4
        pdf = self.canvas.Canvas("pdf_file/test.pdf", pagesize=A4)
        self.create_grid(pdf)
        #self.drawMyRuler(c)
        pdf.save()


if __name__ == '__main__':

    Message().create_pdf()

