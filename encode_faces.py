import os
import face_recognition
import cv2
import pickle

dataset_path = "dataset"
known_encodings = []
known_names = []
known_ids = []

# Loop through student folders
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if not os.path.isdir(folder_path):
        continue

    # Extract student ID and name from folder name
    try:
        student_id, student_name = folder.split("_", 1)
    except ValueError:
        continue  # skip folders not following format

    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        image = cv2.imread(img_path)
        if image is None:
            continue

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(student_name)
            known_ids.append(student_id)

# Save to pickle
data = {"encodings": known_encodings, "names": known_names, "ids": known_ids}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Encoding complete. Data saved to encodings.pickle")
