import cv2
import os

# Input student info
student_id = input("Enter student ID: ")
student_name = input("Enter student name (no spaces): ")
folder_name = f"{student_id}_{student_name}"
save_path = f"dataset/{folder_name}"
os.makedirs(save_path, exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Face Capture - Press 's' to save & 'q' to quit", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        img_name = f"{save_path}/{student_name}_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved {img_name}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
