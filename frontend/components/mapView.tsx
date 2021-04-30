import {FunctionComponent} from "react";
import dynamic from "next/dynamic";

interface MapProps {}

const GoogleMapsView = dynamic(() => import('./googleMapsView'));

const MapView: FunctionComponent<MapProps> = ({}) => (
    <GoogleMapsView/>
);

export default MapView;