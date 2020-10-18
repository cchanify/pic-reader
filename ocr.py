
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def single_img_print(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # print("===========" + filename + "===========")
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


print(single_img_print('/Users/Connor/READER/TEST/IMG_4231.png'))


