import fastapi
import uvicorn
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)