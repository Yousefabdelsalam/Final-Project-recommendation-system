import gdown
import os

# قائمة الملفات ومعلوماتها
files_info = [
    {
        "filename": "model_w2v.model",
        "file_id": "1zKRiCSlb2V99xo97UXmJSyZ39omVK9D3"
    },
    {
        "filename": "stremlit_clustring & analysis.csv",
        "file_id": "1JkQTiucDpmqmUrKQd6PIwhokjMHAri6F"
    },
    {
        "filename": "streamlit.csv",
        "file_id": "1exwAtDvLgHthuHMUROr2OihQtgRC1B3Y"
    }
]

# تنزيل كل ملف لو مش موجود
for file in files_info:
    if not os.path.exists(file["filename"]):
        print(f"📥 Downloading {file['filename']}...")
        url = f"https://drive.google.com/uc?id={file['file_id']}"
        gdown.download(url, file["filename"], quiet=False)
        print(f"✅ Downloaded {file['filename']}")
    else:
        print(f"✅ {file['filename']} already exists.")

