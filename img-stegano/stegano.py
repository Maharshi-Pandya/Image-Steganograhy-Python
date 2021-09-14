import cv2 as cv    # opencv
import imageclass    # custom image class

class ImageStegano:
    """
        Generate steganographic images using the LSB technique
    """
    def __init__(self, img=None, m2h=""):
        self.image = img
        self.msg_to_hide: str = m2h
        self._msg_bin: str = ""

    @property
    def msg_to_hide(self):
        return self._msg_to_hide

    @msg_to_hide.setter
    def msg_to_hide(self, msg):
        if type(msg) != str:
            raise ValueError("The message to hide must be a string")
        
        self._msg_to_hide = msg


# init the image and read it
image = imageclass.Image("testimage.jpeg")
image.read_img(cv.IMREAD_COLOR)

# then pass it to stegano
stegano = ImageStegano(image, m2h="Maharshi")

print(stegano.msg_to_hide)