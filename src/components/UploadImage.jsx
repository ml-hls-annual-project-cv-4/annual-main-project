import { useEffect, useState } from "react"

export const ImageUpload = () => {
    const [selectedFile, setSelectedFile] = useState()
    const [preview, setPreview] = useState()

    // create a preview as a side effect, whenever selected file is changed
    useEffect(() => {
        if (!selectedFile) {
            setPreview(undefined)
            return
        }

        const objectUrl = URL.createObjectURL(selectedFile)
        setPreview(objectUrl)

        // free memory when ever this component is unmounted
        return () => URL.revokeObjectURL(objectUrl)
    }, [selectedFile])

    const onSelectFile = e => {
        if (!e.target.files || e.target.files.length === 0) {
            setSelectedFile(undefined)
            return
        }

        // I've kept this example simple by using the first image instead of multiple
        setSelectedFile(e.target.files[0])
    }
    const handleSubmit = event => {
        // 👇️ prevent page refresh
        event.preventDefault();
    
        console.log('form submitted ✅');
      };

    return (
        <form onSubmit={handleSubmit}>
        <div className="type-input">
            <input type="file" onChange={onSelectFile} className="mb-10 text-sm text-grey-500
            file:py-2 file:px-6
            file:rounded-full file:border-0
            file:text-lg file:font-medium
            file:bg-blue-50 file:text-blue-700
            hover:file:cursor-pointer hover:file:bg-amber-50
            hover:file:text-amber-700
          " />
          {selectedFile && <img src={preview} /> }

          {selectedFile ? (
            <input type="submit" className="mt-4 mb-10 text-grey-500
            py-2 px-6
            rounded-full border-0
            text-lg font-medium
            bg-blue-50 text-blue-700
            hover:cursor-pointer hover:bg-amber-50
            hover:text-amber-700" value="Submit" />
          ): <label></label> } 

        </div>
        </form>

        

        
    )
}