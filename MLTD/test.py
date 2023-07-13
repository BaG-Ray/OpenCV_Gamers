import cv2
import pytesseract
from PIL import Image

Log_Dir = './MLTD/log'


Pic_Dir = Log_Dir + '/Game_Pic.jpg'
Ocr_Pic = cv2.imread(Pic_Dir)
Ocr_Auto_Pic = Ocr_Pic[1358:1408,1363:1441]
Ocr_Auto_Pic_Gray = cv2.cvtColor(Ocr_Auto_Pic,cv2.COLOR_BGR2GRAY)
Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic_Gray, lang='jpn')
    
cv2.imshow("Ocr_Auto_Pic_Gray",Ocr_Auto_Pic_Gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
