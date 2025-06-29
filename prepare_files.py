{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a31748f4-2b3e-4562-b56e-035907717aa3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ model_w2v.model already exists.\n",
      "✅ StremlitClustring.csv already exists.\n",
      "✅ streamlit.csv already exists.\n"
     ]
    }
   ],
   "source": [
    "import gdown\n",
    "import os\n",
    "\n",
    "# === روابط Google Drive ===\n",
    "files = {\n",
    "    \"model_w2v.model\": \"1zKRiCSlb2V99xo97UXmJSyZ39omVK9D3\",\n",
    "    \"StremlitClustring.csv\": \"1kiH5q2p3a9uKp2xc9V9zOuJjiYaAhcjT\",\n",
    "    \"streamlit.csv\": \"1exwAtDvLgHthuHMUROr2OihQtgRC1B3Y\"\n",
    "}\n",
    "\n",
    "# === تحميل الملفات ===\n",
    "for filename, file_id in files.items():\n",
    "    if not os.path.exists(filename):\n",
    "        print(f\"⬇️ Downloading {filename}...\")\n",
    "        url = f\"https://drive.google.com/uc?id={file_id}\"\n",
    "        gdown.download(url, filename, quiet=False)\n",
    "    else:\n",
    "        print(f\"✅ {filename} already exists.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "271d1a1e-1263-4d3f-bd9a-7baa820984dc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
