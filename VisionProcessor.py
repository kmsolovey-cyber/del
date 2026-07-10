import cv2

class VisionProcessor:
    def __init__(self, path):
        self.img_bgr = cv2.imread(path)
        self.img_ycrcb = None

    def convert(self):
        if self.img_bgr is None:
            return None
        self.img_ycrcb = cv2.cvtColor(self.img_bgr, cv2.COLOR_BGR2YCrCb)
        return self.img_ycrcb

    def get_cr_mask(self, threshold_value):
        img_ycrcb = self.convert()
        y, cr, cb = cv2.split(img_ycrcb)
        _, mask = cv2.threshold(cr, threshold_value, 255, cv2.THRESH_BINARY)
        return mask
