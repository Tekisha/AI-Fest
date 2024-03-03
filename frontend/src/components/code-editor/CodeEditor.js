import { Editor } from "@monaco-editor/react";
import { Button } from "../button/Button";
import "./CodeEditor.css";
import { useRef, useState } from "react";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "../select/Select";

function CodeEditor({ setLoading, setHints, problems }) {
  const hiddenFileInput = useRef(null);
  const [fileContent, setFileContent] = useState("");
  const [selectedProblemId, setSelectedProblemId] = useState("1");

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

  const getHints = async () => {
    const hintsResponse = await fetch(`http://localhost:8000/api/hints/${selectedProblemId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        student_solution: fileContent,
      }),
    });
    const hintsJson = await hintsResponse.json();

    setLoading(false);
    setHints(hintsJson.hints);
  };

  const handleSelectChange = (e) => {
    setSelectedProblemId(e);
  };

  const handleSubmit = async () => {
    setLoading(true);
    await getHints();
  };

  const handleEditorChange = (e) => {
    setFileContent(e);
  };

  return (
    <div>
      <div className="line">
        <h2 className="scroll-m-20 text-3xl font-semibold tracking-tight first:mt-0 p-6">Code Editor</h2>
        <Button onClick={handleClick} variant="secondary">
          Upload a File
        </Button>
        <input ref={hiddenFileInput} multiple={false} type="file" onChange={handleChange} style={{ display: "none" }} />
        <Select onValueChange={handleSelectChange} defaultValue="1">
          <SelectTrigger id="problem-select">
            <SelectValue placeholder="Select a problem" />
          </SelectTrigger>
          <SelectContent>
            {problems.map((pr) => (
              <SelectItem key={pr.id} value={pr.id}>
                {pr.problem_name}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
      <Editor height="83vh" defaultLanguage="kotlin" value={fileContent} onChange={handleEditorChange} />
      <Button onClick={handleSubmit} className="submit-btn">
        Submit
      </Button>
    </div>
  );
}

export default CodeEditor;
