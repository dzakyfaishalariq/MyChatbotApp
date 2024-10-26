from fastapi import FastAPI
from controllers import user
import uvicorn

app = FastAPI(title="Partner Ku", version="0.0.0")

app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
