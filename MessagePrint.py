from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

class Message:

    def __init__(self):
        self.path = "pdf_file/test.pdf"
        self.list = ['message1','message2','message3','message4','message5','message6','message7',
                    'message8','message9','message10','message11','message12','message13',
                    'message9','message10','message11','message12','message13',
                    'message1','message2','message3','message4','message5','message6','message7',
                    'message8','message9','message10','message11','message12','message13',
                    'message9','message10','message11','message12','message13']
        self.offset_x = 0.4*inch
        self.offset_y = 0.2*inch
        self.index = 1
        self.box_number = 1

    def create_grid(self, canvas):
        from reportlab.lib.units import inch
        from reportlab.lib.colors import pink, black, red, blue, green

        x1, x2, y1, y2 = (0, 2.5, 0, 2.5)
        index = 1
        box_number = 1

        c = canvas
        c.setStrokeColor(black)
        for i in range(len(self.list)):
            
            if self.index % 4 != 0:
                try:
                    c.grid([x1*inch + self.offset_x, x2*inch + self.offset_x],[y1*inch + self.offset_y, y2*inch + self.offset_y])
                    print("x1: {value} and x2: {value2}".format(value=(x1+0.4), value2=(x2+0.4)))
                    x1 += 2.5
                    x2 += 2.5
                except:
                    print("It is not working")
            elif self.index % 4 == 0:
                try:
                    y1 += 2.5
                    y2 += 2.5
                    c.grid([x1*inch + self.offset_x, x2*inch + self.offset_x],[y1*inch + self.offset_y, y2*inch + self.offset_y])
                    print("y1: {value} and y2: {value2}".format(value=y1, value2=y2))
                    x1, x2 = (0, 2.5)
                    self.index = 1
                except:
                    print("index % 4 == 0 doesnt work")

            if self.box_number % 12 == 0:
                x1, x2, y1, y2 = (0, 2.5, 0, 2.5)
                c.showPage()

            self.index += 1
            self.box_number += 1
            
    def create_pdf(self):

        from reportlab.pdfgen import canvas
        c = canvas.Canvas("pdf_file/test.pdf")
        self.create_grid(c)
        c.showPage()
        c.save()


if __name__ == '__main__':

    Message().create_pdf()

