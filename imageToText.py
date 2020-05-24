from PIL import Image, ImageDraw, ImageFont
import csv

xAxis = 500
with open('address.csv','rb') as addressFile:
    csvReader = csv.reader(addressFile, delimiter=',')
    for row in csvReader:
        print row
        fileName = row[5]+'.jpg'
        image = Image.open('2.jpg')
        font_type = ImageFont.truetype('Beyond Wonderland.ttf',60)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(xAxis,900), text = "To,", fill = (255,0,0), font = font_type)
        draw.text(xy=(xAxis,1000), text = row[1], fill = (255,0,0), font = font_type)
        draw.text(xy=(xAxis,1100), text = row[2], fill = (255,0,0), font = font_type)
        draw.text(xy=(xAxis,1200), text = row[3], fill = (255,0,0), font = font_type)
        draw.text(xy=(xAxis,1300), text = row[4], fill = (255,0,0), font = font_type)
        image.save(fileName)

from fpdf import FPDF

with open('address.csv','rb') as addressFile:
    csvReader = csv.reader(addressFile, delimiter=',')
    for row in csvReader:
        print row
        pdf = FPDF()
        fileName = row[5]+'.jpg'
        pdfFileName = row[5]+'.pdf'
        imagelist = ['1.jpg',fileName,'3.jpg']
        for image in imagelist:
            pdf.add_page()
            pdf.image(image,0,0,210,297)
        pdf.output(pdfFileName, "F")
