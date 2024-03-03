import "./Home.css";
import * as React from "react";
import KodestLogo from "../assets/images/kodest-logo.png";
import { Card, CardDescription, CardFooter, CardHeader } from "../components/card/Card";
import CodeEditor from "../components/code-editor/CodeEditor";
import { useState, useEffect } from "react";
import { LinearProgress } from "@mui/material";
import { Button } from "../components/button/Button";

function Home() {
  const [hints, setHints] = useState([]);
  const [loading, setLoading] = useState(false);
  const [problems, setProblems] = useState([]);
  const [currentHint, setCurrentHint] = useState(0);

  useEffect(() => {
    const fetchProblems = async () => {
      const problemsResponse = await fetch("http://localhost:8000/api/problems");
      const problemsJson = await problemsResponse.json();

      setProblems(problemsJson.problems);
    };

    fetchProblems();

    return () => {
      setProblems([]);
    };
  }, []);

  const handlePrevious = () => {
    setCurrentHint(currentHint - 1);
  };

  const handleNext = () => {
    setCurrentHint(currentHint + 1);
  };

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
              <br /> <br /> Select a problem you want to solve, submit a solution and Kodest will evaluate it for you along with some hints!
            </CardDescription>
          </Card>
        </div>
        <div className="submission-results">
          <Card>
            <CardHeader>
              Submission results <br /> <br /> {hints?.length > 0 ? `Hint ${currentHint + 1} / ${hints?.length}` : ""}
            </CardHeader>
            <CardDescription>
              {loading ? (
                <LinearProgress />
              ) : hints?.length > 0 ? (
                hints[currentHint]
              ) : (
                "In order to see your submission results, you have to first submit the solution."
              )}
            </CardDescription>
            {hints?.length > 0 ? (
              <CardFooter>
                <div className="button-footer">
                  <Button disabled={currentHint === 0} onClick={handlePrevious}>
                    Previous
                  </Button>
                  <Button disabled={currentHint === hints?.length - 1} onClick={handleNext}>
                    Next
                  </Button>
                </div>
              </CardFooter>
            ) : (
              ""
            )}
          </Card>
        </div>
      </div>
      <div className="main-right">
        <CodeEditor setLoading={setLoading} setHints={setHints} problems={problems} />
      </div>
    </div>
  );
}

export default Home;
