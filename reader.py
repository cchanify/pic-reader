""" Simple usage of the package """

#!/usr/bin/python3

import os.path
import osxphotos

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def main():
    #db = os.path.expanduser("~/Pictures/Photos Library .photoslibrary")
    export_path = os.path.expanduser("~/Desktop/pic_reader")

    #photosdb = osxphotos.PhotosDB(db)
    #photosdb = osxphotos.PhotosDB("/Users/Connor/Pictures/Photos Library .photoslibrary")
    photosdb = osxphotos.PhotosDB()
    # print("======KEYWORDS=======")
    # print(photosdb.keywords)
    # print("======PERSONS=======")
    # print(photosdb.persons)
    # print("======ALBUMS=======")
    # print(photosdb.albums)

    breakpoint()  
    # assumes photosdb is a PhotosDB object (see above)
    test=photosdb.photos(albums=["TEST"])
    print(f"found {len(test)} photos")

    for p in test:
        print(p)
        print(originalFilename)
        print(p.originalFilename)
        text = pytesseract.image_to_string(Image.open(p))
        print(text)

    # print("======KEYWORDS AS DICT=======")
    # print(photosdb.keywords_as_dict)
    # print("======PERSONS AS DICT=======")
    # print(photosdb.persons_as_dict)
    # print("======ALBUMS AS DICT=======")
    # print(photosdb.albums_as_dict)

    #pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Connor/Desktop/smart-desk'

    #print(pytesseract.image_to_string(r'C:/Users/Connor/Desktop/smart-desk'))

if __name__ == "__main__":
    main()
