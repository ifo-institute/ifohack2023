import drive
import os


MIN_DRIVE_URL_LENGTH = 7


def upload_files(GDRIVE_FOLDER_ID):
    RECORD_FOLDER = os.getenv('RECORD_FOLDER', "")

    if len(GDRIVE_FOLDER_ID) > MIN_DRIVE_URL_LENGTH:
        # Check if folder exists
        if not os.path.isdir(RECORD_FOLDER):
            print("Folder " + RECORD_FOLDER + " does not exist, skip upload..")
            return

        print("Checking folder " + RECORD_FOLDER + "..")
        for file in os.listdir(RECORD_FOLDER):
            # Scan the path, get filenames and absolute paths, append terminal ID to filename
            filename = 'gdrive_' + file
            abs_path = os.path.abspath(os.path.join(RECORD_FOLDER, file))
            try:
                print("Uploading " + abs_path + "..")
                drive.Client().upload(abs_path, filename, GDRIVE_FOLDER_ID)
            except:
                print("Error! Cannot upload file " +
                      filename + " in " + abs_path + "..")
    else:
        print("Skip uploading of video records due to missing folder ID..")
