import "./Home.css";
import KodestLogo from "../assets/images/kodest-logo.png";

function Home() {
  return (
    <div className="main">
      <div className="main-left">
        <div className="logo">
          <img src={KodestLogo} alt="kodest-logo" />
        </div>
      </div>
      <div className="main-right"></div>
    </div>
  );
}

export default Home;
