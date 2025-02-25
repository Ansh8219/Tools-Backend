from fastapi import FastAPI
from core.config import settings
from apps.image_compress.routers import router as image_compress_router


app = FastAPI(title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG
)


app.include_router(image_compress_router,prefix="/image_compress",tags=["Image Compress"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}!"}
