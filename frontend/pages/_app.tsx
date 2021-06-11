import type {AppProps} from "next/app";
import {ChakraProvider} from "@chakra-ui/react";
import React, {createContext} from "react";
import {MapStore, MapContext} from "../stores/mapStore";

let store = new MapStore(
    'goeree',
    'https://projectdimages.blob.core.windows.net/images/goereeMap.png',
    {lat: 51.7794255, lng: 3.8526257},
    {lat: 51.8453395, lng: 3.9692927},
    {lng: 3.96, lat: 51.844},
);

function ProjectFrontend({Component, pageProps}: AppProps) {
    return (
        <MapContext.Provider value={store}>
            <ChakraProvider>
                <Component {...pageProps} />
            </ChakraProvider>
        </MapContext.Provider>
    )
}

export default ProjectFrontend;

