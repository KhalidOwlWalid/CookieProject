from reportlab.pdfgen import canvas

def test(canvas):
    from reportlab.lib.units import cm

    c = canvas.Canvas("text_test.pdf")
    c.showPage()

if __name__ == '__main__':
    test(canvas)