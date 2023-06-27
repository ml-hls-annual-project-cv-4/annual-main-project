import io
import zipfile
from os import path
from typing import List

from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse
from starlette_exporter import PrometheusMiddleware, handle_metrics

from src.factoring.yolo_manager_factory import YoloManagerFactory

app = FastAPI(ssl_keyfile="api/private.key", ssl_certfile="api/cert.crt")
manager = YoloManagerFactory().get_final_dl_manager("models/detection_model.onnx")

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


# @app.post("/uploadfile/")
# async def upload_file(selectedFile: UploadFile):
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


def get_filename_without_ext(filename):
    return path.splitext(filename)[0]


def get_extension(filename):
    return path.splitext(filename)[-1].replace(".", "")


@app.post("/uploadfile/")
async def upload_file(selectedFile: UploadFile):
    """
    Запрашивает изображение для детекции на ней объектов
    @param selectedFile: Изображение для предсказания
    @return: Изображение с детектированными объектами
    """
    pred = manager.predict(selectedFile.file.read())
    filename = get_filename_without_ext(selectedFile.filename)
    ext = get_extension(selectedFile.filename)

    response = StreamingResponse(io.BytesIO(pred), media_type=f"image/{ext}")
    response.headers["Content-Disposition"] = f"attachment;filename={filename}_predicted.{ext}"

    return response


@app.post("/uploadfiles/")
async def upload_file(selectedFiles: List[UploadFile]):
    """
    Запрашивает изображения для предсказания на них объектов
    @param selectedFiles: Изображения для предсказания
    @return: Архив с изображениями с детектированными объектами
    """
    pred = manager.predict([sf.file.read() for sf in selectedFiles])

    zip_io = archivate(pred, [sf.filename for sf in selectedFiles])

    return StreamingResponse(
        iter([zip_io.getvalue()]),
        media_type="application/x-zip-compressed",
        headers={"Content-Disposition": f"attachment; filename=predictions.zip"}
    )


def archivate(pred, files):
    zip_io = io.BytesIO()

    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as temp_zip:
        for i, p in enumerate(pred):
            img_name = get_filename_without_ext(files[i])
            img_ext = get_extension(files[i])

            img_filename = f"{img_name}_predicted.{img_ext}"
            temp_zip.writestr(img_filename, p)

    return zip_io
