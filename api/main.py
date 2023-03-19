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
    
    import numpy as np
    import pandas as pd
    from src.features_extraction_algorithms.hog_algorithm import img_to_array, img_cut_box, convert_to_hog, make_pred_hog_vc
    from src.databases import dwh
        
    img_bgr_array = img_to_array(file_location)
    df_labels = dwh.select_db_labels(selectedFile.filename, 'labels_train')
    prediction = (
        df_labels[lambda df: np.invert(df.box2d_x1.isna())]
            .apply(lambda df: img_cut_box(img_bgr_array, df.box2d_x1, df.box2d_y1, df.box2d_x2, df.box2d_y2), 
                axis=1)
            .apply(convert_to_hog)
            .apply(make_pred_hog_vc)
            .apply(np.squeeze)
            .to_list()
    )
    return prediction