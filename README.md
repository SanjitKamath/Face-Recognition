Got it! Here's the **README.md** without any references mentioned:

---

# Welcome to the Attendance System Project! 👋

This repository provides a full pipeline for object detection, face recognition, and attendance management, using a combination of OpenCV, Dlib, and MySQL database integration.

All the required files are available for download here:  
🔗 [Download Required Files](https://www.mediafire.com/file/bwt563swvaa7phl/Required_Files.zip/file)

---

## Project Modules

### 1. **Required modules installation** (`1. Required modules.py`)
This script installs all the necessary libraries and sets up MySQL:
- Installs: `mysql-connector-python`, `opencv-python`, `dlib`, `numpy`, `pandas`
- Starts MySQL service

📌 Run this first to prepare your environment.

---

### 2. **Database setup and test entry** (`2. DB.py`)
- Sets up MySQL user and database.
- Creates a table `attendance`.
- Inserts a sample entry and displays the table contents.

---

### 3. **Load Image for Detection** (`3. Load Image.py`)
- Loads a pretrained object detection model (SSD MobileNet v3).
- Loads an image and displays it.

---

### 4. **Detect Objects** (`4. Detect Objects.py`)
- Detects objects in the loaded image.
- Crops only detected people using the `crop_images` function.

---

### 5. **Crop Detected People** (`5. Crop People.py`)
- Filters detected objects to only **persons**.
- Crops and displays individual detected people from the image.

---

### 6. **Face Detection and Recognition** (`6. Face Detection.py`)
- Detects faces in the cropped person images.
- Compares faces with known faces.
- Labels the images.
- Stores the results (`name` and `time`) in `output.csv`.

---

### 7. **Update Database with Recognized Faces** (`7. Update DB.py`)
- Reads the `output.csv`.
- Inserts recognized names and timestamps into the MySQL `attendance` table.

---

## How to Use 🛠️

1. **Download the Required Files**:  
   [Download from here](https://www.mediafire.com/file/bwt563swvaa7phl/Required_Files.zip/file)

2. **Install Modules and Set Up Environment**:  
   Run `1. Required modules.py` to install necessary libraries and start MySQL.

3. **Set Up Database**:  
   Run `2. DB.py` to create your MySQL database and table.

4. **Load and Prepare Image**:  
   Run `3. Load Image.py` to load the target group image.

5. **Detect and Crop Persons**:  
   Run `4. Detect Objects.py` and `5. Crop People.py` to detect people and crop images.

6. **Face Detection and Attendance Recording**:  
   Run `6. Face Detection.py` to recognize faces and create a CSV file with names and timestamps.

7. **Update Attendance in Database**:  
   Run `7. Update DB.py` to insert attendance records into the MySQL database.

---

## Requirements

- Python 3.x
- OpenCV
- Dlib
- NumPy
- Pandas
- MySQL Server

---

## Notes 📋
- Make sure MySQL is running before running the database scripts.
- Default MySQL username is `root` and password is `root123`. Modify it if needed.
- Store known face images inside a folder named `known/` in your project directory.
- The models (`labels.txt`, `shape_predictor_68_face_landmarks.dat`, `dlib_face_recognition_resnet_model_v1.dat`) are required from the provided zip file.

---

## License

This project is for educational purposes. Feel free to modify and extend it for your own needs!

---
