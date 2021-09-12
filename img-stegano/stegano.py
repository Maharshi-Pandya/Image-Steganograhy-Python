import sys
import cv2 as cv    # opencv

# interface for image
class Image:
    def __init__(self, file_path=None):
        self.img_file_path = file_path
        self.img = None

    def read_img(self, read_flag):
        if self.img_file_path is not None and read_flag is not None:
            self.img = cv.imread(self.img_file_path, read_flag)
            
            if self.img is None:
                sys.exit("Couldn't read the specified image")

    def write_img(self, fname, file_format):
        if self.img is not None:
            cv.imwrite(f"{fname}.{file_format}", self.img)

    def pixel_at(self, x, y):
        if self.img is not None:
            return self.img[x, y]


# generate steganographic images
class ImageStegano:
    def __init__(self):
        self.image = None
        self.msg_to_hide: str = ""
        self._msg_bin: str = ""

    @property
    def msg_to_hide(self):
        return self._msg_to_hide

    @msg_to_hide.setter
    def msg_to_hide(self, msg):
        if type(msg) != str:
            raise ValueError("The message to hide must be a string")
        
        self._msg_to_hide = msg


image = Image()
image.img_file_path = "ss.png"
image.read_img(cv.IMREAD_COLOR)

pixel = image.pixel_at(10, 30)
print(pixel)

image.write_img("ssfinal", "png")