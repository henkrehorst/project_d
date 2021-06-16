import {FunctionComponent, useContext} from "react";
import {Button, ButtonGroup, IconButton, Link, Text, Tooltip} from "@chakra-ui/react";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {displayResultOverlay, goTo, removeMarkers} from "../services/googleMapsService";
import {MinusIcon} from "@chakra-ui/icons";

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

    const itemRemoveClick = (event) => {
        fetch(process.env.NEXT_PUBLIC_API_URL + 'delete/' + id, {
            method: 'DELETE'
        }).then(response => {
            if(response.ok){
                map.setHistory(true);
            }
        });
    }

    return (
        <ButtonGroup position={'relative'} w={'100%'}>
            <Tooltip label={"Water level: " + waterLevel}>
                <Button marginBottom={2} marginTop={2} w={'100%'} as={'button'} bg={'white'}
                        onClick={itemClick}>{name}
                </Button>
            </Tooltip>
            <IconButton
                size={'xs'}
                colorScheme="red"
                aria-label="Delete item"
                borderRadius="40px"
                icon={<MinusIcon/>}
                position={'absolute'}
                top={'0'}
                right={'-2'}
                zIndex={9}
                onClick={itemRemoveClick}
            />
        </ButtonGroup>
    )
})