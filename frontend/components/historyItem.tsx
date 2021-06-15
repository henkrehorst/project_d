import {FunctionComponent, useContext} from "react";
import {Button, Link, Text, Tooltip} from "@chakra-ui/react";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {displayResultOverlay, goTo, removeMarkers} from "../services/googleMapsService";

interface HistoryItemProps {
    id: number,
    name: string,
    source: string,
    upperRight: { lat: number, lng: number },
    lowerLeft: { lat: number, lng: number },
    duneLocation: number,
    waterLevel: number
}

export const HistoryItem = observer<HistoryItemProps>(({
                                                           id,
                                                           name,
                                                           source,
                                                           upperRight,
                                                           lowerLeft,
                                                           duneLocation,
                                                           waterLevel
                                                       }) => {
    const map = useContext(MapContext);

    const itemClick = () => {
        displayResultOverlay(source, lowerLeft, upperRight);
        removeMarkers();
        map.disablePoints();
        map.setStatus('result');
        map.setHeight(waterLevel);
        goTo(16, upperRight);
    }

    return (
        <Tooltip label={"Water level: " + waterLevel}>
            <Button marginBottom={2} marginTop={2} w={'100%'} as={'button'} bg={'white'}
                    onClick={itemClick}>{name}</Button>
        </Tooltip>
    )
})