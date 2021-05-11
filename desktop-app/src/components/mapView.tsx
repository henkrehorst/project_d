import React from "react";
import { FunctionComponent } from "react";
import GoogleMapsView from "./googleMapsView";

interface MapProps {
}

const MapView: FunctionComponent<MapProps> = ({}) => (
  <GoogleMapsView />
);

export default MapView;