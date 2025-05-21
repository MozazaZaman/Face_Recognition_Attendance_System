import face_recognition
import cv2
import pickle
import datetime
import csv

# Load encoded data
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]
known_ids = data["ids"]

# Start webcam
cap = cv2.VideoCapture(0)
recognized = set()

# Create attendance filename
filename = f"attendance_{datetime.date.today()}.csv"

with open(filename, "w", newline="") as csvfile:
    fieldnames = ["ID", "Name", "Time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            matches = face_recognition.compare_faces(known_encodings, encoding)
            if True in matches:
                match_index = matches.index(True)
                student_id = known_ids[match_index]
                student_name = known_names[match_index]

                if student_id not in recognized:
                    now = datetime.datetime.now().strftime("%H:%M:%S")
                    writer.writerow({"ID": student_id, "Name": student_name, "Time": now})
                    print(f"[ATTENDANCE] {student_id} - {student_name} at {now}")
                    recognized.add(student_id)

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
