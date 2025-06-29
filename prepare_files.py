import gdown
import zipfile
import os

# ملفات Google Drive IDs
FILES = [
    {
        "filename": "model_w2v.model",
        "file_id": "1zKRiCSlb2V99xo97UXmJSyZ39omVK9D3",
        "output": "model_w2v.model"
    },
    
    {
        "filename": "stremlit.csv",
        "file_id": "1exwAtDvLgHthuHMUROr2OihQtgRC1B3Y",
        "output": "stremlit.csv"
    }
]

# تحميل الملفات الناقصة فقط
for file in FILES:
    if not os.path.exists(file["filename"]):
        print(f"⬇️ Downloading {file['filename']}...")
        url = f"https://drive.google.com/uc?id={file['file_id']}"
        gdown.download(url, file['output'], quiet=False)
        print(f"✅ Downloaded {file['filename']}")
    else:
        print(f"✅ {file['filename']} already exists.")

