import React from "react";
import axios from "axios";

function Homepage() {
  const signUp = async () => {
    const email = "stanford@gmail.com";
    const password = "test";
    const response = await axios.post("/api/signup");
    console.log(response);
  };
  return (
    <div>
      <h1>Welcome to our Restaurant</h1>
      {/* <button>Sign Up</button>
      <button>Login</button>
      <button>Log Out</button> */}
    </div>
  );
}

export default Homepage;
