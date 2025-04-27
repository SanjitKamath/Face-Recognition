def crop_images(img,ClassIndex,confidence,bbox):

  # Create a list to store the person bounding boxes
  person_bboxes = []

  # Iterate through the detections
  for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(),bbox):
    # Check if the detected object is a person
    if classLabels[ClassInd - 1] == 'person':
        person_bboxes.append(boxes)

  # Crop the source image to only include the person bounding boxes
  cropped_images = []
  for bbox in person_bboxes:
    x, y, w, h = bbox
    cropped_img = img[y:y+h, x:x+w]
    cropped_images.append(cropped_img)

  # Display the cropped images
  for i, cropped_img in enumerate(cropped_images):
    plt.subplot(1, len(cropped_images), i+1)
    plt.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
    plt.title(f"Person {i+1}")
    plt.axis('off')

  plt.show()
  return cropped_images