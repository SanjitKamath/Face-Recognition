import dlib
import os
from datetime import datetime
import csv
import cv2
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_rec_model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

def load_known_faces(known_faces_dir):
    encodings = []
    names = []
    for filename in os.listdir(known_faces_dir):
        name = os.path.splitext(filename)[0]
        img = cv2.imread(os.path.join(known_faces_dir, filename))
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        for face in detector(rgb_img):
            shape = predictor(rgb_img, face)
            descriptor = np.array(face_rec_model.compute_face_descriptor(rgb_img, shape))
            encodings.append(descriptor)
            names.append(name)
    return encodings, names

known_face_encodings, known_face_names = load_known_faces("known")

def compare_faces(known_encodings, face_encoding, tolerance=0.6):
    distances = np.linalg.norm(known_encodings - face_encoding, axis=1)
    min_distance_index = np.argmin(distances)
    if distances[min_distance_index] < tolerance:
        return True, min_distance_index
    return False, None

# Initialize CSV output
csv_filename = "output.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'time'])

# Process each person image
for i, person_img in enumerate(cropped_imgs):
    person_img_rgb = cv2.cvtColor(person_img, cv2.COLOR_BGR2RGB)
    dets = detector(person_img_rgb)
    face_descriptors = []
    for d in dets:  # Use `d` within the loop
        shape = predictor(person_img_rgb, d)
        face_descriptor = face_rec_model.compute_face_descriptor(person_img_rgb, shape)
        face_descriptors.append(np.array(face_descriptor))

        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            for face_descriptor in face_descriptors:
                match, idx = compare_faces(known_face_encodings, face_descriptor)
                name = known_face_names[idx] if match else "Unknown"
                writer.writerow([name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

                top, right, bottom, left = (d.top(), d.right(), d.bottom(), d.left())
                cv2.rectangle(person_img, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(person_img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)

print(f"Detection results saved to {csv_filename}")