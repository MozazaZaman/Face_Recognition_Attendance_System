Here’s a `README.md` file tailored for your **Face Recognition Attendance System** project. 

### 📘 `README.md`

```markdown
# Face Recognition Attendance System 
This project is a desktop-based face recognition attendance system designed for a classroom (22 batch). It includes:
- Face recognition using the `face_recognition` library.
- Real-time camera capture with `OpenCV`.
- Attendance logging with date and time.
- Attendance export to Excel (.csv format).

---

## 🔧 Features


- 🎓 Attendance taken by facial recognition.
- 📅 Prevents duplicate attendance on the same day.
- 📤 Export attendance records to CSV.
- 🧠 Custom dataset encoding for student faces.

---

## 📂 Project Structure

```

face\_recognition\_system/
│
├── dataset/
│   └── \<student\_name>/
│       └── <images>.jpg
│
├── encodings.pickle       # Face encodings
├── main.py                # Captures student images
├── encode\_faces.py        # Generates face encodings
├── recognize.py           # Real-time recognition and attendance
├── attendance.csv         # Attendance output
└── README.md

````

---

## 🛠️ Requirements

- Python 3.10+
- OpenCV
- face_recognition
- numpy
- imutils
- dlib
- scikit-learn
- tensorflow / keras
- pandas

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🧑‍💻 How to Run

### 1. Capture student images:

```bash
python main.py
```

### 2. Encode faces:

```bash
python encode_faces.py
```

### 3. Run the recognition system:

```bash
python recognize.py
```

---

## ✅ To Do

* [x] Face Capture and Recognition
* [x] Attendance CSV Export
* [x] Mask/Niqab Detection Integration
* [ ] Add real-time dashboard
* [ ] Improve GUI styling

---

## 📝 Notes

* Use consistent lighting and face angle when capturing student images.
* Run encoding again if you add new students.

---

## 🤝 Author

**Roza**
Computer Science & Engineering, Khulna University
Contact: \[https://github.com/MozazaZaman]

---

