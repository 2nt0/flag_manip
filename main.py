from PIL import Image
import numpy as np

def main():
    img = Image.open("flag_gb.png", "r").convert("RGB")
    pix = list(img.getdata())
    width, height = img.size

    pixel_values = np.array(pix).reshape((width*height, 3))

    RGBs = np.array([0,0,0])
    for pixel in pixel_values:
        RGBs += np.array(pixel)
    
    avgint = tuple((RGBs/(width*height)).astype(int))
    print(avgint)

if __name__ == "__main__":
    main()