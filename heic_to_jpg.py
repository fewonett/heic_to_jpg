import sys
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(heic_path):
    pillow_heif.register_heif_opener()
    image = Image.open(heic_path)
    jpg_path = heic_path.rsplit('.', 1)[0] + '.jpg'
    image.save(jpg_path, "JPEG")
    print(f"Converted {heic_path} to {jpg_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python heic_to_jpg.py path_to_image")
        sys.exit(1)
    
    heic_path = sys.argv[1]
    convert_heic_to_jpg(heic_path)
