from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def upload_file(selectedFile: UploadFile):
    file_location = f"{selectedFile.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(selectedFile.file.read())
    print(selectedFile.filename)
    #Затычка для предикта, дальше вовзращаться будут результаты предсказания
    return {"selectedFile": selectedFile.filename}