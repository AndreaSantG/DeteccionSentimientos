import os
import EmotionRecognizer

imagesInputFolder = 'inputs/'
imagesInputList = os.listdir(imagesInputFolder)
var = 'inputs/cara9.png'
print(imagesInputList)
for frame in imagesInputList:
    EmotionRecognizer.emotion_recognizer(imagesInputFolder+frame, frame)


