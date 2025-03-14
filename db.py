import os
import librosa
import numpy as np
from tqdm import tqdm

# Dataset manzili
dataset_path = r"D:\TUIT\amaliy_intellekt"

# Dublikatlarni aniqlash uchun to‘plam
hashes = set()

# Keraksiz yoki buzilgan fayllarni aniqlash va o‘chirish
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)

    if os.path.isdir(folder_path):  # Faqat papkalarni tekshirish
        for file in tqdm(os.listdir(folder_path), desc=f"⏳ {folder} ni tekshirish"):
            file_path = os.path.join(folder_path, file)

            # Faqat .wav fayllarni tekshiramiz
            if file.endswith(".wav"):
                try:
                    # Ovoz faylni yuklash
                    y, sr = librosa.load(file_path, sr=None)

                    # Agar fayl juda kichik bo‘lsa (kamroq ma’lumotga ega bo‘lsa), o‘chiramiz
                    if len(y) < 1000:
                        os.remove(file_path)
                        print(f"🗑️ {file} juda kichik - o‘chirildi!")

                    # Dublikatlarni tekshirish (hash orqali)
                    hash_val = hash(tuple(np.round(y, decimals=3)))  # Ovoz signali hash qilinadi
                    if hash_val in hashes:
                        os.remove(file_path)
                        print(f"🗑️ {file} dublikat - o‘chirildi!")
                    else:
                        hashes.add(hash_val)

                except Exception as e:
                    print(f"❌ Xatolik: {file} - {str(e)}")
                    os.remove(file_path)  # Buzilgan faylni o‘chirish
