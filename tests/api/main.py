import io
import zipfile
from os import path

import cv2
import uvicorn
from fastapi import FastAPI, UploadFile
from starlette.responses import StreamingResponse

from src.factoring.yolo_manager_factory import YoloManagerFactory

manager = YoloManagerFactory().get_final_dl_manager("models/detection_model.onnx")
app = FastAPI()

def get_filename_without_ext(filename):
    return path.splitext(filename)[0]

@app.post("/uploadfile/")
async def upload_file(selected_file: UploadFile):
    pred = manager.predict(selected_file.file.read())
    filename = get_filename_without_ext(selected_file.filename)

    response = StreamingResponse(io.BytesIO(pred), media_type="image/jpg")
    response.headers["Content-Disposition"] = f"attachment;filename={filename}_predicted.jpg"

    return response

def archivate(pred, files):
    zip_io = io.BytesIO()

    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as temp_zip:
        for i, p in enumerate(pred):
            img_filename = f"{get_filename_without_ext(files[i])}_predicted.jpg"
            temp_zip.writestr(img_filename, p)

    return zip_io



@app.post("/uploadfiles/")
async def upload_file(selected_files: list[UploadFile]):
    pred = manager.predict([sf.file.read() for sf in selected_files])

    zip_io = archivate(pred, [sf.filename for sf in selected_files])

    return StreamingResponse(
        iter([zip_io.getvalue()]),
        media_type="application/x-zip-compressed",
        headers = { "Content-Disposition": f"attachment; filename=predictions.zip"}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
