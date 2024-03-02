import { Editor } from "@monaco-editor/react";
import { Button } from "../button/Button";
import "./CodeEditor.css";
import { useRef, useState } from "react";

function CodeEditor({ setLoading, setFeedback }) {
  const hiddenFileInput = useRef(null);
  const [fileContent, setFileContent] = useState("");
  let fileReader;

  const handleClick = () => {
    hiddenFileInput.current.click();
  };

  const handleFileRead = (e) => {
    const content = fileReader.result;
    setFileContent(content);
  };

  const handleFile = (file) => {
    fileReader = new FileReader();
    fileReader.onloadend = handleFileRead;
    fileReader.readAsText(file);
  };

  const handleChange = (event) => {
    const fileUploaded = event.target.files[0];
    handleFile(fileUploaded);
  };

  const handleSubmit = () => {
    setLoading(true);
  };

  return (
    <div>
      <div className="line">
        <h2 className="scroll-m-20 text-3xl font-semibold tracking-tight first:mt-0 p-6">Code Editor</h2>
        <Button onClick={handleClick} variant="secondary">
          Upload a File
        </Button>
        <input ref={hiddenFileInput} multiple={false} type="file" onChange={handleChange} style={{ display: "none" }} />
      </div>
      <Editor height="83vh" defaultLanguage="kotlin" value={fileContent} />
      <Button onClick={handleSubmit} className="submit-btn">
        Submit
      </Button>
    </div>
  );
}

export default CodeEditor;
