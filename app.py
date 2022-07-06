from PIL import Image
import os
import time
import argparse


def app(args):
    ##(334, 48, width - 331, height - 48)
    global bbox
    start_time = time.time()
    os.chdir(args.link)
    try:
        os.mkdir("cropped")
    except:
        pass

    for file in os.listdir(os.getcwd()):
        if file.endswith(".jpg") or file.endswith(".png"):
            img = Image.open(file)
            w, h = img.size

            if args.bbox:
                bbox = tuple([int(i) for i in args.bbox])
            elif args.margin:
                margin = tuple([int(i) for i in args.margin])
                bbox = tuple([margin[0], margin[1], w - margin[2], h - margin[3]])

            cropped_img = img.crop(bbox)
            cropped_img.save("cropped/cropped_" + file)
    print("The process have been finish {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Toplu Fotoğraf Kırpma Scripti")
    parser.add_argument("-l", "--link", required=True,
                        help='[TR] Fotoğralarınızın bulunduğu klasör konumu\n'
                             '[EN] Location of photos to crop')
    parser.add_argument("-b", "--bbox", nargs=4, metavar=('Sol', 'Üst', 'Sağ', 'Alt'),
                        help='[TR] Fotoğrafın kırpılmasını istediğiniz alanı <Sol, Üst, Sağ, Alt>')
    parser.add_argument("-m", "--margin", nargs=4, metavar=('Sol', 'Üst', 'Sağ', 'Alt'),
                        help='[TR] Fotoğrafın kırpılmasını istediğiniz alanın fotoğrafın orjinal sınırlarına uzaklığı '
                             '<Sol, Üst, Sağ, Alt>')
    args = parser.parse_args()

    app(args)