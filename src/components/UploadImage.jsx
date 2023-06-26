import { useEffect, useState } from "react";
import axios from "axios";

export const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState();
  const [preview, setPreview] = useState();
  const [result, setResult] = useState();
  const [prediction, setPrediction] = useState();

  useEffect(() => {
    if (!selectedFile) {
      setPreview(undefined);
      return;
    }

    const objectUrl = URL.createObjectURL(selectedFile);
    setPreview(objectUrl);

    return () => URL.revokeObjectURL(objectUrl);
  }, [selectedFile]);

  const onSelectFile = (e) => {
    if (!e.target.files || e.target.files.length === 0) {
      setSelectedFile(undefined);
      return;
    }

    setSelectedFile(e.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("selectedFile", selectedFile);
    try {
      setResult(true);
      const response = await axios.post("https://annualcv.ru:3000/uploadfile/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
        responseType: 'blob'
      });
      setResult(false);
      const imageUrl = URL.createObjectURL(new Blob([response.data]));
      setPrediction(imageUrl);
    } catch (error) {
      console.log(error);
      setResult(false);
    }
  };

  return (
    <div className="flex flex-col h-screen items-center justify-center mt-20">
      <form onSubmit={handleSubmit} className="">
        <div className="bg-slate-300 bg-opacity-40 rounded-xl p-4 place-items-center flex flex-col">
          <input
            accept='image/png, image/jpeg, image/jpg'
            multiple
            type="file"
            onChange={onSelectFile}
            className="mb-2 text-sm text-grey-500
            file:py-2 file:px-6
            file:rounded-full file:border-0
            file:text-lg file:font-medium
            file:bg-blue-50 file:text-blue-700
            hover:file:cursor-pointer hover:file:bg-amber-50
            hover:file:text-amber-700"
          />
          {selectedFile && <img className="h-auto max-h-96 max-w-full" src={preview} alt="Preview" />}

          {selectedFile ? (
            <input
              type="submit"
              className="mt-3 text-grey-500
              py-2 px-6
              rounded-full border-0
              text-lg font-medium
              bg-blue-50 text-blue-700
              hover:cursor-pointer hover:bg-amber-50
              hover:text-amber-700"
              value="Отправить"
            />
          ) : (
            <label></label>
          )}

          {result && (
            <div>
              <label className="text-white text-xl">Файл успешно загружен, ожидайте...</label>
              <svg
                aria-hidden="true"
                className="mx-auto mt-2 mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                viewBox="0 0 100 101"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                {/* SVG path data */}
              </svg>
            </div>
          )}

          {prediction && <img src={prediction} className="my-3 h-auto max-h-96 max-w-full" alt="Prediction" />}
        </div>
      </form>
    </div>
  );
};
