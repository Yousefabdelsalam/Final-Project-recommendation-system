import gdown
import zipfile
import os

# اسم الملف اللي هيتفك من ال zip
MODEL_FILENAME = "model_w2v.model"
ZIP_FILENAME = "recommndation system app deplyment.zip"

# لو الموديل مش موجود، نزّل ال zip وفكّه
if not os.path.exists(MODEL_FILENAME):
    print("📦 Downloading model zip from Google Drive...")

    file_id = "1KFTXoq-KskOUCCV8XfxWa8qrQRt8EILe"
    url = f"https://drive.google.com/uc?id={file_id}"  # ✅ سطر URL زي ما هو

    gdown.download(url, ZIP_FILENAME, quiet=False)

    with zipfile.ZipFile(ZIP_FILENAME, 'r') as zip_ref:
        zip_ref.extractall()

    print("✅ Done downloading and extracting files.")
else:
    print("✅ Files already exist.")
