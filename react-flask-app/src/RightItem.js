import "./RightItem.css";

// icons
import { GiBrain } from "react-icons/gi";
import { AiFillSafetyCertificate } from "react-icons/ai";
import { TiHeart } from "react-icons/ti";

const RightItem = ({pathos, logos, ethos}) => {
const total = pathos + logos + ethos;
  return (
    <div className="right">
      <h1 style={{marginLeft:"15px", marginTop: "-100px"}}>
      {/* <h1> */}
        Overall Score: <span>{total}</span>
      </h1>
      <div className="cards-container">
        <div className="card">
          <TiHeart />
          <p>PATHOS</p>
          <h6>{pathos}</h6>
        </div>
        <div className="card">
          <GiBrain />
          <p>LOGOS</p>
          <h6>{logos}</h6>
        </div>
        <div className="card">
          <AiFillSafetyCertificate />
          <p>ETHOS</p>
          <h6>{ethos}</h6>
        </div>
      </div>
    </div>
  );
};

export default RightItem;
