import gdown
import os

# Model
model_id = "1zKRiCSlb2V99xo97UXmJSyZ39omVK9D3"
model_output = "model_w2v.model"

# Streamlit CSV
csv_main_id = "1exwAtDvLgHthuHMUROr2OihQtgRC1B3Y"
csv_main_output = "streamlit.csv"

# Cluster CSV
csv_cluster_id = "1kiH5q2p3a9uKp2xc9V9zOuJjiYaAhcjT"
csv_cluster_output = "StreamlitClustering.csv"


def download_file(file_id, output_path):
    if not os.path.exists(output_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        print(f"⬇️ Downloading {output_path}...")
        gdown.download(url, output_path, quiet=False)
        print(f"✅ Downloaded {output_path}")
    else:
        print(f"✅ {output_path} already exists.")


download_file(model_id, model_output)
download_file(csv_main_id, csv_main_output)
download_file(csv_cluster_id, csv_cluster_output)
