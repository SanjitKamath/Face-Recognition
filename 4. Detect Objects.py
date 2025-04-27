def detect_objects(img):
  ClassIndex,confidence,bbox=model.detect(img,confThreshold=0.5)
  font_scale=2
  font=cv2.QT_FONT_NORMAL
  for ClassInd,conf,boxes in zip(ClassIndex.flatten(),confidence.flatten(),bbox):
      #cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40),font,fontScale=font_scale,color=(255,255,255),thickness=2)
      print(classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40))

  plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
  plt.show()
  cropped_images = crop_images(img,ClassIndex,confidence,bbox)
  return cropped_images