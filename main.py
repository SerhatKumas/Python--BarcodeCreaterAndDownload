# import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter


# Barcode creator and saver method
def generate_and_save_barcode(barcode_number):
    # Creation of barcode
    barcode = EAN13(barcode_number, writer=ImageWriter())

    # Our barcode is ready. Let's save it.
    barcode.save("barcode")


# Barcode generator and downloader runner code
if __name__ == '__main__':
    # User barcode number input
    user_barcode_number = input("Enter 12 characters barcode number that you want to embed  :")
    # Method invoker
    generate_and_save_barcode(user_barcode_number)
