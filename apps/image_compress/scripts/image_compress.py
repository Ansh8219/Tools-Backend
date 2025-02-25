from PIL import Image
import io
import os

# Create output directory if not exists
OUTPUT_DIR = "compressed_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def compress_image(input_bytes: bytes, quality: int = 70) -> str:
    """
    Compress an image and save the compressed file.
    :param input_bytes: Original image as bytes.
    :param quality: Compression quality (1-100).
    :return: Path to the compressed image.
    """
    try:
        # Open the image from bytes
        image = Image.open(io.BytesIO(input_bytes))

        # Set output format (JPEG if PNG or unsupported)
        output_format = "JPEG" if image.format not in ["JPEG", "PNG"] else image.format

        # Output file path
        output_path = os.path.join(OUTPUT_DIR, f"compressed_image.{output_format.lower()}")

        # Convert PNG to JPEG (if needed)
        if image.format == "PNG":
            image = image.convert("RGB")

        # Compress and save the image
        image.save(output_path, format=output_format, quality=quality)

        return output_path

    except Exception as e:
        raise RuntimeError(f"Error compressing image: {e}")
