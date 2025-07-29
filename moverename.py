import os
import shutil

folder = "./files"
start = 1

IMAGE_EXTS = {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp", "avif"}
VIDEO_EXTS = {"mp4", "avi", "mov", "mkv", "flv", "wmv", "mpeg", "mpg"}

img_count = 1
vid_count = 1

for fname in sorted(os.listdir(folder)):
    if '.' not in fname:
        continue

    ext = fname.rsplit('.', 1)[1].lower()

    if ext in IMAGE_EXTS:
        cat_folder = "img"
        new_name = f"img_{img_count}.{ext}"
        img_count += 1

    elif ext in VIDEO_EXTS:
        cat_folder = "video"
        new_name = f"video_{vid_count}.{ext}"
        vid_count += 1

    else:
        continue  # Skip unsupported files

    dest_folder = os.path.join(folder, cat_folder)
    os.makedirs(dest_folder, exist_ok=True)

    src = os.path.join(folder, fname)
    dst = os.path.join(dest_folder, new_name)
    shutil.move(src, dst)

    print(f"Moved & Renamed: {fname} → {cat_folder}/{new_name}")


