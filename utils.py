import cv2

def load_in_rgb(path):
    image_bgr = cv2.imread(path)
    rgb_image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return rgb_image