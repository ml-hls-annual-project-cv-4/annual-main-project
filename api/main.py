from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

import numpy as np
import pandas as pd
from src.features_extraction_algorithms.hog_algorithm import HogPredict

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

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

@app.post("/uploadfile/")
async def upload_file(selectedFile: UploadFile):
    file_location = f"{selectedFile.filename}"
    
    with open(file_location, "wb+") as file_object:
        file_object.write(selectedFile.file.read())
        
    print(selectedFile.filename)
    
    prediction = HogPredict(img_path=file_location) \
        .convert_to_hog() \
        .make_pred()
        
    return prediction
