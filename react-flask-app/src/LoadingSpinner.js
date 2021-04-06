import React from "react";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";
import './LoadingSpinner.css';

function LoadingSpinner() {
        return (
          <Loader
            className="loader"
            type="ThreeDots"
            color="violet"
            height={80}
            width={80}
            timeout={3000}
          />
        );
}
         
export default LoadingSpinner;