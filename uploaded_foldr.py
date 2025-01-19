import os
import time
import shutil
import subprocess

# Configuration
MONITOR_FOLDER = "./camera_captures"  # Folder to monitor
UPLOADED_FOLDER = "./uploaded"        # Folder to move uploaded files
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
CHECK_INTERVAL = 30  # Time interval (seconds) to check for new files

# Ensure the monitor and uploaded folders exist
os.makedirs(MONITOR_FOLDER, exist_ok=True)
os.makedirs(UPLOADED_FOLDER, exist_ok=True)

def upload_file(file_path):
    """Upload a file using curl and move it to the uploaded folder on success."""
    try:
        # Execute the curl command
        result = subprocess.run(
            [
                "curl", "-X", "POST", "-F", f"imageFile=@{file_path}", UPLOAD_URL
            ],
            capture_output=True, text=True
        )

        # Check the result
        if result.returncode == 0 and "success" in result.stdout.lower():
            print(f"Successfully uploaded: {file_path}")
            # Move the file to the uploaded folder
            shutil.move(file_path, os.path.join(UPLOADED_FOLDER, os.path.basename(file_path)))
        else:
            print(f"Failed to upload {file_path}. Response: {result.stdout}")
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")


def monitor_folder():
    """Monitor the folder and process new files."""
    processed_files = set()

    while True:
        try:
            # Get a list of files in the folder
            files = [
                f for f in os.listdir(MONITOR_FOLDER)
                if os.path.isfile(os.path.join(MONITOR_FOLDER, f))
            ]

            for file_name in files:
                file_path = os.path.join(MONITOR_FOLDER, file_name)

                if file_path not in processed_files:
                    print(f"New file detected: {file_name}")
                    time.sleep(CHECK_INTERVAL)  # Wait before uploading
                    upload_file(file_path)
                    processed_files.add(file_path)

        except FileNotFoundError as e:
            print(f"Error: {e}. Retrying...")

        time.sleep(5)  # Check the folder periodically


if __name__ == "__main__":
    print("Starting folder monitor...")
    monitor_folder()
