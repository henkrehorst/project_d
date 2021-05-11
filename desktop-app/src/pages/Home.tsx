import {NavBar} from "../components/navBar";
import { FunctionComponent } from "react";
import React from "react";
import { Link } from "react-router-dom";

interface PageProps {
}

const Page: FunctionComponent<PageProps> = () => {
  return (
    <>
      <NavBar/>
      <Link to="/map">
        Map
      </Link>
      <h1>Homepage</h1>
    </>
  )
}

export default Page;