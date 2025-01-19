# Automated Image Upload and Folder Monitoring System

## 📷 Overview

This Python script **monitors a folder for new images**, uploads them to a remote server using `cURL`, and moves them to an "uploaded" folder upon successful upload. It ensures files are processed only once and handles errors efficiently.

## 🚀 Features

- ✅ **Real-time monitoring** – Watches a specified folder for new image files.
- ✅ **Automated upload** – Uses `cURL` to send images to a remote server.
- ✅ **File management** – Moves successfully uploaded files to a designated folder.
- ✅ **Processed files tracking** – Ensures the same file is not uploaded multiple times.
- ✅ **Error handling** – Logs failures and retries if necessary.
- ✅ **Lightweight & Efficient** – Runs in the background with minimal resource usage.

## 🛠 Requirements

- Python 3.x
- cURL (pre-installed on macOS/Linux, [download for Windows](https://curl.se/windows/))

## 📂 Project Structure

```
/project-folder
│── upload_monitor.py   # Main script
│── /camera_captures    # Monitored folder for new images
│── /uploaded           # Folder for successfully uploaded images
│── README.md           # Documentation
```

## ⚙️ Setup & Usage

### 1️⃣ Clone the repository

```sh
git clone https://github.com/yourusername/auto-image-uploader.git
cd auto-image-uploader
```

### 2️⃣ Install dependencies (if needed)

```sh
pip install -r requirements.txt  # Not required if using standard libraries
```

### 3️⃣ Modify configuration

Edit `upload_monitor.py` to set:

- `MONITOR_FOLDER` → Your image source directory
- `UPLOADED_FOLDER` → Folder to move processed files
- `UPLOAD_URL` → Server endpoint for uploads

### 4️⃣ Run the script

```sh
python upload_monitor.py
```

### 5️⃣ Test upload manually (optional)

```sh
curl -X POST -F "imageFile=@path/to/image.jpg" https://your-server.com/upload.php
```

## 🔧 Customization

- Adjust `CHECK_INTERVAL` to change how often the script checks for new files.
- Implement additional logging for better tracking.
- Extend functionality to support multiple file types or cloud storage.
- Modify `processed_files` tracking to persist across restarts.

###
---

🚀 **Feel free to contribute! Fork the repo and submit pull requests.**

