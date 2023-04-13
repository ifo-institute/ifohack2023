import drive
import os


MIN_DRIVE_URL_LENGTH = 7


def upload_record_folder(gdrive_folder_id: str):
    record_folder = get_record_folder()
    if upload_is_allowed(gdrive_folder_id, record_folder):
        for f in os.listdir(record_folder):
            filename = f'gdrive_{f}'
            abs_file_path = os.path.abspath(os.path.join(record_folder, f))
            upload_to_drive(
                source_file=abs_file_path,
                target_file=filename,
                gdrive_folder_id=gdrive_folder_id
            )


def get_record_folder() -> str:
    return os.getenv('RECORD_FOLDER', "")


def upload_is_allowed(gdrive_folder_id: str, source_folder: str) -> bool:
    is_gdrive_folder_id = len(gdrive_folder_id) > MIN_DRIVE_URL_LENGTH
    folder_exists = os.path.isdir(source_folder)
    return is_gdrive_folder_id and folder_exists


def upload_to_drive(source_file: str, target_file: str, gdrive_folder_id: str):
    try:
        drive.Client().upload(source_file, target_file, gdrive_folder_id)
    except Exception as e:
        print(f"Error! Cannot upload file {source_file}: {e}")
