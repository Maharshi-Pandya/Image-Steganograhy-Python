import sys
import cv2 as cv    # opencv

# interface for image
class Image:
    """
        Custom image class built on opencv for ez image manipulations
    """
    def __init__(self, file_path=None):
        self.img_file_path = file_path
        self.img = None

    def read_img(self, read_flag):
        if self.img_file_path is not None:
            self.img = cv.imread(self.img_file_path, read_flag)
            
            if self.img is None:
                sys.exit("Couldn't read the specified image")

    def write_img(self, fname, file_format):
        if self.img is not None:
            cv.imwrite(f"{fname}.{file_format}", self.img)

    def pixel_at(self, x, y):
        if self.img is not None:
            return self.img[x, y]

    def modify_pixel_at(self, x, y, value: list):
        if self.img is not None:
            self.img[x, y] = value