import gdown
import os

files = {
    "model_w2v.model": "1zKRiCSlb2V99xo97UXmJSyZ39omVK9D3",
    "StremlitClustering.csv": "1kiH5q2p3a9uKp2xc9V9zOuJjiYaAhcjT",
    "streamlit.csv": "1exwAtDvLgHthuHMUROr2OihQtgRC1B3Y"
}

for filename, file_id in files.items():
    if not os.path.exists(filename):
        print(f"⬇️ Downloading {filename}...")
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, filename, quiet=False)
        print(f"✅ Downloaded {filename}")
    else:
        print(f"✅ {filename} already exists.")
