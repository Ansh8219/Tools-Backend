# from PIL import Image
# import io
# import os

# # Create output directory if not exists
# OUTPUT_DIR = "compressed_images"
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# def compress_image(file: bytes, quality: int = 70, output_format: str = "JPEG") -> str:
#     """
#     Compress an image and save to disk.
#     :param file: Image file as bytes.
#     :param quality: Compression quality (1-100).
#     :param output_format: Output image format (JPEG, PNG).
#     :return: Path to the saved compressed image.
#     """
#     try:
#         # Open image from bytes
#         image = Image.open(io.BytesIO(file))

#         # Convert unsupported formats to JPEG
#         if image.format not in ["JPEG", "PNG", "WEBP"]:
#             image = image.convert("RGB")
#             output_format = "JPEG"

#         # Define output path
#         output_path = os.path.join(OUTPUT_DIR, f"compressed_image.{output_format.lower()}")

#         # Save compressed image to disk
#         image.save(output_path, format=output_format, quality=quality)

#         return output_path

#     except Exception as e:
#         raise RuntimeError(f"Error compressing image: {e}")
