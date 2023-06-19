import { useEffect, useState } from "react";
import axios from "axios";
export const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState();
  const [preview, setPreview] = useState();
  const [result, setResult] = useState();
  const [prediction, setPrediction] = useState();

  // create a preview as a side effect, whenever selected file is changed
  useEffect(() => {
    if (!selectedFile) {
      setPreview(undefined);
      return;
    }

    const objectUrl = URL.createObjectURL(selectedFile);
    setPreview(objectUrl);

    // free memory when ever this component is unmounted
    return () => URL.revokeObjectURL(objectUrl);
  }, [selectedFile]);

  useEffect(() => {
    console.log(prediction);
  }, [prediction]);

  const onSelectFile = (e) => {
    if (!e.target.files || e.target.files.length === 0) {
      setSelectedFile(undefined);
      return;
    }

    // I've kept this example simple by using the first image instead of multiple
    setSelectedFile(e.target.files[0]);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("selectedFile", selectedFile);
    try {
      setResult(true);
      await axios({
        method: "post",
        url: "https://annualcv.ru:3000/uploadfile/",
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
      }).then((response) => {
        setResult(false);
        setPrediction(response.data);
      });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col items-center justify-center h-screen">
      <div className="flex flex-col items-center justify-center bg-slate-300 bg-opacity-40 rounded-xl p-4">
        <input
          type="file"
          onChange={onSelectFile}
          className="mb-10 text-sm text-grey-500
            file:py-2 file:px-6
            file:rounded-full file:border-0
            file:text-lg file:font-medium
            file:bg-blue-50 file:text-blue-700
            hover:file:cursor-pointer hover:file:bg-amber-50
            hover:file:text-amber-700
          "
        />
        {selectedFile && 
        <div className="w-2/4">
        <img className="object-scale-down" src={preview} />
        </div>}

        {selectedFile ? (
          <input
            type="submit"
            className="mt-4 mb-10 text-grey-500
            py-2 px-6
            rounded-full border-0
            text-lg font-medium
            bg-blue-50 text-blue-700
            hover:cursor-pointer hover:bg-amber-50
            hover:text-amber-700"
            value="Submit"
          />
        ) : (
          <label></label>
        )}

        {result ? (
          <div>
            <label className="text-white text-xl">
              {" "}
              Файл успешно загружен, ожидайте...{" "}
            </label>
            <svg
              aria-hidden="true"
              class="mx-auto mt-2 mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
              viewBox="0 0 100 101"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"
              />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"
              />
            </svg>
          </div>
        ) : (
          <></>
        )}
        {prediction ? <><h1 className="text-white text-4xl text-center">Предсказание: {prediction}</h1></> : <></>}
      </div>
    </form>
  );
};
