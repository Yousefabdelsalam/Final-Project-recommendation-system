import gdown
import zipfile
import os

ZIP_FILENAME = "recommndation system app deplyment.zip"
CHECK_FILENAME = "model_w2v.model"

if not os.path.exists(CHECK_FILENAME):
    print("📦 Downloading zip from Google Drive...")

    file_id = "1KFTXoq-KskOUCCV8XfxWa8qrQRt8EILe"
    url = f"https://drive.google.com/uc?id={file_id}"

    gdown.download(url, ZIP_FILENAME, quiet=False)

    print("📂 Extracting files...")
    with zipfile.ZipFile(ZIP_FILENAME, 'r') as zip_ref:
        zip_ref.extractall()

    print("✅ All files extracted successfully.")
else:
    print("✅ Files already exist.")
