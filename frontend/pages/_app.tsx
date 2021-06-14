import type {AppProps} from "next/app";
import {ChakraProvider} from "@chakra-ui/react";
import React, {createContext} from "react";
import {MapStore, MapContext} from "../stores/mapStore";

function ProjectFrontend({Component, pageProps}: AppProps) {
    let store = new MapStore(
        'Goeree',
        'https://projectdimages.blob.core.windows.net/images/goereeMap.png',
        {lat: 51.7794255, lng: 3.8526257},
        {lat: 51.8453395, lng: 3.9692927},
        {lng: 3.96, lat: 51.844},
        1
    );

    return (
        <MapContext.Provider value={store}>
            <ChakraProvider>
                <Component {...pageProps} />
            </ChakraProvider>
        </MapContext.Provider>
    )
}

export default ProjectFrontend;

