import { Editor } from "@monaco-editor/react";

function CodeEditor() {
  return (
    <div>
      <h2 className="scroll-m-20 text-3xl font-semibold tracking-tight first:mt-0 p-6">Code Editor</h2>
      <Editor height="90vh" defaultLanguage="kotlin" />
    </div>
  );
}

export default CodeEditor;
