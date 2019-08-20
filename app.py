import minecart
import PIL
import io


pdffile = open(r"C:\Users\d59999\Documents\Python\Python-PDF_KCs\atos.pdf", 'rb')
doc = minecart.Document(pdffile)
page = doc.get_page(1)
for shape in page.images:
	print('hi')
	im=page.images[0].as_pil()
# for shape in page.images.iter_in_bbox((0, 0, 100, 200)):
	# print(shape.path)
# im = page.images[0].as_pil()  # requires pillow
# im.show()