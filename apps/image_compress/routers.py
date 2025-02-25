from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from apps.image_compress.scripts.image_compress import compress_image

router = APIRouter()

ALLOWED_FORMATS = ["image/jpeg", "image/png", "image/webp"]

@router.post("/compress")
async def compress_image_endpoint(file: UploadFile = File(...), quality: int = 70):
    """
    API endpoint to trigger the image compression script.
    """
    try:
        # Ensure the uploaded file is an image
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Uploaded file is not an image.")
        
        # Read file content as bytes
        original_content = await file.read()

        # 🔥 Run the compression script
        output_path = compress_image(original_content, quality)

        # Return the result
        return JSONResponse(content={
            "filename": file.filename,
            "compressed_image_path": output_path,
            "quality": quality
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
