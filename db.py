import os
import librosa
import numpy as np
from tqdm import tqdm

dataset_path = r"D:\TUIT\amaliy_intellekt"

hashes = set()

for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)

    if os.path.isdir(folder_path): 
        for file in tqdm(os.listdir(folder_path), desc=f"{folder} ni tekshirish"):
            file_path = os.path.join(folder_path, file)

            if file.endswith(".wav"):
                try:
                    y, sr = librosa.load(file_path, sr=None)

                    if len(y) < 1000:
                        os.remove(file_path)
                        print(f" {file} juda kichik - o‘chirildi!")

                    hash_val = hash(tuple(np.round(y, decimals=3))) 
                    if hash_val in hashes:
                        os.remove(file_path)
                        print(f" {file} dublikat - o‘chirildi!")
                    else:
                        hashes.add(hash_val)

                except Exception as e:
                    print(f"Xatolik: {file} - {str(e)}")
                    os.remove(file_path) 
