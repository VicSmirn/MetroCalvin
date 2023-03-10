# Модуль с аугументацией и предоброботкой картинок (если они слишком темные)

from roboflow_downloads import download
import sys
import os
import pathlib
import numpy as np
from skimage.util import view_as_windows
import cv2

ABS_PATH = pathlib.Path(__file__).parent.absolute()
sys.path.append(str(ABS_PATH.parent.parent))
VERSION = 1
dataset_path = os.path.join(ABS_PATH, f's-{VERSION}')
if not os.path.exists(dataset_path):
    download(version=VERSION)

# Изменяем яркость, контрастность, выделяем контура (для пробы простого убора)
def prepeare_picturies():
    img_color = Image.open("/content/ImageNuberTrains/AntonsCalvin/23.02.17_13-13-05.jpg")
    img_color = np.array(im_output)
    width, height, chenal = img_color.shape
    x, y = 0, 50
    crop_img_color = img_color[y:y+height, x:240]
    lab_l_channel = cv2.cvtColor(crop_img_color, cv2.COLOR_BGR2LAB)[..., 0]
    tsize = 240
    tiles = view_as_windows(lab_l_channel, (tsize, tsize), (tsize, tsize))
    lightness = tiles.reshape(-1, tsize ** 2).mean(axis=-1).reshape(np.array(crop_img_color.shape[:2]) // tsize)

img = cv2.imread('./s-1/train/images/23-02-17_12-00-55_bmp.rf.eae1d931dc695ddd5ad6f528bb3a45ef.jpg')
cv2.imshow('my_photo', img)
size_f = 640
r = int(img.shape[0] * size_f / img.shape[1])
dim = (size_f, r)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('recised_image_photo', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()