import cv2
import numpy as np
import pytesseract
from PIL import Image

Log_Dir = './LegenClover/log'


Pic_Dir = Log_Dir + '/Game_Pic.jpg'
Ocr_Pic = cv2.imread(Pic_Dir)
Ocr_Auto_Pic = Ocr_Pic[17:70,1954:2065]  

Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='jpn')
print(Ocr_Text)
    
cv2.imshow("Ocr_Auto_Pic",Ocr_Auto_Pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
