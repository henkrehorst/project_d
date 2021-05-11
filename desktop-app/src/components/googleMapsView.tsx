import { FunctionComponent, useEffect } from "react";
import { initMap } from "../services/googleMapsService";
import { Box } from "@chakra-ui/react";
import React from "react";

interface MapProps {
}

const GoogleMapsView: FunctionComponent<MapProps> = ({}) => {
  useEffect(() => {
    initMap("google-maps-placeholder");
  });

  return <Box h={"100%"} id={"google-maps-placeholder"} />;
};

export default GoogleMapsView;