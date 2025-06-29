{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a31748f4-2b3e-4562-b56e-035907717aa3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Files already exist.\n"
     ]
    }
   ],
   "source": [
    "import gdown\n",
    "import zipfile\n",
    "import os\n",
    "\n",
    "if not os.path.exists(\"model_w2v.model\"):\n",
    "    print(\"📦 Downloading model zip from Google Drive...\")\n",
    "    file_id = \"1KFTXoq-KskOUCCV8XfxWa8qrQRt8EILe\"\n",
    "    url = f\"https://drive.google.com/uc?id={file_id}\"\n",
    "    output = \"model_files.zip\"\n",
    "\n",
    "    gdown.download(url, output, quiet=False)\n",
    "\n",
    "    with zipfile.ZipFile(output, 'r') as zip_ref:\n",
    "        zip_ref.extractall()\n",
    "\n",
    "    print(\"✅ Done downloading and extracting files.\")\n",
    "else:\n",
    "    print(\"✅ Files already exist.\")\n"
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
