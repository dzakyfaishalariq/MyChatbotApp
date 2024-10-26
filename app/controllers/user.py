from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/")
async def info():
    return {
        "name": "MyChatbotApp",
        "version": "0.0.0",
        "decription": "Aplikasi ini merupakan chatbot untuk menjawab permasalahan ilmu pengetahuan terkait pelajaran yang ada di sekolah",
    }

