{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "model-download-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "import gdown\n",
    "import zipfile\n",
    "import os\n",
    "\n",
    "# اسم الملف اللي هيتفك من ال zip\n",
    "MODEL_FILENAME = \"model_w2v.model\"\n",
    "ZIP_FILENAME = \"recommndation system app deplyment.zip\"\n",
    "\n",
    "# لو الموديل مش موجود، نزّل ال zip وفكّه\n",
    "if not os.path.exists(MODEL_FILENAME):\n",
    "    print(\"📦 Downloading model zip from Google Drive...\")\n",
    "    \n",
    "    file_id = \"1KFTXoq-KskOUCCV8XfxWa8qrQRt8EILe\"\n",
    "    url = f\"https://drive.google.com/uc?id={file_id}\"\n",
    "\n",
    "    gdown.download(url, ZIP_FILENAME, quiet=False)\n",
    "\n",
    "    with zipfile.ZipFile(ZIP_FILENAME, 'r') as zip_ref:\n",
    "        zip_ref.extractall()\n",
    "\n",
    "    print(\"✅ Done downloading and extracting files.\")\n",
    "else:\n",
    "    print(\"✅ Files already exist.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
