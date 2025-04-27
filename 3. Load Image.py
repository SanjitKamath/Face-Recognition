import cv2
import matplotlib.pyplot as plt

config_file='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model='frozen_inference_graph.pb'

model =cv2.dnn_DetectionModel(frozen_model,config_file)
classLabels = []
file_name="labels.txt"
with open(file_name,'rt') as fpt:
    classLabels=fpt.read().rstrip('\n').split('\n')

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127,5,127.5))
model.setInputSwapRB(True)

img=cv2.imread("/content/known/group1.jpg")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()