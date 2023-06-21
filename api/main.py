from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

import numpy as np
import pandas as pd
from src.features_extraction_algorithms.hog_algorithm import HogPredict

from starlette.responses import StreamingResponse

from src.factoring.yolo_manager_factory import YoloManagerFactory
import io
import zipfile
from os import path
import cv2

app = FastAPI(ssl_keyfile="api/private.key", ssl_certfile="api/cert.crt")


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

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

#@app.post("/uploadfile/")
#async def upload_file(selectedFile: UploadFile):
#    file_location = f"{selectedFile.filename}"
#    
#    with open(file_location, "wb+") as file_object:
#        file_object.write(selectedFile.file.read())
#        
#    print(selectedFile.filename)
#    
#    prediction = HogPredict(img_path=file_location) \
#        .convert_to_hog() \
#        .make_pred()
#        
#    return prediction



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

