import "./Home.css";
import KodestLogo from "../assets/images/kodest-logo.png";
import { Card, CardDescription, CardHeader } from "../components/card/Card";
import CodeEditor from "../components/code-editor/CodeEditor";

function Home() {
  return (
    <div className="main">
      <div className="main-left">
        <div className="logo">
          <img src={KodestLogo} alt="kodest-logo" />
        </div>
        <div className="description">
          <Card>
            <CardHeader>What is Kodest?</CardHeader>
            <CardDescription>
              Kodest is your universal AI study buddy, designed to help you conquer educational programming tasks and tests - all without giving away the answers!
              Whether you're a coding newbie or a seasoned pro, Kodest is here to guide you through problems and empower you to learn independently.
            </CardDescription>
          </Card>
        </div>
      </div>
      <div className="main-right">
        <CodeEditor />
      </div>
    </div>
  );
}

export default Home;
