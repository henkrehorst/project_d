import {FunctionComponent, useContext, useEffect} from "react";
import {initMap} from "../services/googleMapsService";
import {Box} from "@chakra-ui/react";
import {observer} from 'mobx-react-lite';
import {MapContext} from "../stores/mapStore";


const GoogleMapsView= () => {
    const map = useContext(MapContext);
    useEffect(() => {
        initMap('google-maps-placeholder', map)
    })


    return <Box h={'100%'} id={'google-maps-placeholder'}/>;
};

export default observer(GoogleMapsView);