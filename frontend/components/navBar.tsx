import {FunctionComponent, useContext} from "react";
import {
    Alert,
    AlertIcon,
    Box,
    Button,
    Flex, Modal,
    ModalBody,
    ModalCloseButton, ModalContent,
    ModalFooter,
    ModalHeader, ModalOverlay, Progress, Slider, SliderFilledTrack, SliderThumb, SliderTrack,
    Spacer, Text,
    useDisclosure
} from "@chakra-ui/react";
import {MapSelection} from "./mapSelection";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {displayResultOverlay, refreshMap} from "../services/googleMapsService";
import {Legend} from "./legend";


export const NavBar = observer(() => {
    const map = useContext(MapContext);
    const {isOpen, onOpen, onClose} = useDisclosure();

    const onClearClick = () => {
        map.setStatus('selection');
        map.removePointA();
        map.removePointB();
        refreshMap(map);
    }

    const changeHeight = (value: number) => {
        map.setHeight(value);
    }

    const changeWidth = (value: number) => {
        map.setWidth(value);
    }

    const runCalculation = () => {
        map.setStatus('calculation');
        fetch(process.env.NEXT_PUBLIC_API_URL + 'algorithm', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                punt_a: {
                    x: map.pointALat,
                    y: map.pointALng
                },
                punt_b: {
                    x: map.pointBLat,
                    y: map.pointBLng
                },
                waterlevel: map.height,
                breedte: map.width,
                locatie: map.mapLocation,
                locatieId: map.locationId,
                waterLevel: map.height
            })
        }).then(response => {
            if (response.ok) {
                response.json().then((data: { imageid: number }) => {
                    console.log(data.imageid);
                    let interval = setInterval(() => {
                        fetch(process.env.NEXT_PUBLIC_API_URL + 'image/' + data.imageid).then(res => {
                            if (res.ok) {
                                res.json().then((result: {
                                    BottomCoordinate: string | null,
                                    DuneLocation: number,
                                    Id: number,
                                    Link: string | null,
                                    Name: string,
                                    TopCoordinate: null,
                                    WaterLevel: number
                                }) => {
                                    if (result.Link != null) {
                                        console.log(result)
                                        clearInterval(interval);
                                        displayResultOverlay(
                                            result.Link,
                                            // @ts-ignore
                                            {
                                                // @ts-ignore
                                                lat: Number(result.TopCoordinate.split(',')[0]),
                                                // @ts-ignore
                                                lng: Number(result.TopCoordinate.split(',')[1])
                                            },
                                            // @ts-ignore
                                            {
                                                lat: Number(result.BottomCoordinate.split(',')[0]),
                                                lng: Number(result.BottomCoordinate.split(',')[1])
                                            });
                                        onClose();
                                        map.setHistory(true);
                                        map.setStatus('result');
                                    }
                                });
                            }
                        })
                    }, 10000)
                })
            }
        })
    }

    return (
        <>
            <Flex backgroundColor={"blue.600"} w={'100%'} p={4} h={'72px'}>
                <MapSelection/>
                {map.status != 'result' ?
                    <Button marginLeft={'20px'} onClick={onOpen} colorScheme="green">New Calculation</Button> : <Legend/>}
                <Spacer/>
                <Button colorScheme="red" onClick={onClearClick}>Clear</Button>
            </Flex>
            <Modal closeOnOverlayClick={false} isOpen={isOpen} onClose={onClose}>
                <ModalOverlay/>
                <ModalContent>
                    <ModalHeader>{map.status === 'selection' ? 'Start Calculation' : 'Running Calculation'}</ModalHeader>
                    {map.status === 'selection' ? <ModalCloseButton/> : ''}
                    <ModalBody pb={6}>
                        {!map.pointAExists || !map.pointBExists ?
                            <Alert status="error">
                                <AlertIcon/>
                                Select two points before starting the path finding algorithm!
                            </Alert>
                            : map.status === 'selection' ? <>
                                    <Text>
                                        Click on ‘Run calculation’ to start the path finding algorithm.
                                    </Text>
                                    <Text fontWeight={'bold'} marginTop={'20px'}>Water level: {map.height}</Text>
                                    <Slider defaultValue={map.height} onChange={changeHeight} min={3} max={15} step={1}>
                                        <SliderTrack bg="blue.100">
                                            <Box position="relative" right={10}/>
                                            <SliderFilledTrack bg="blue.800"/>
                                        </SliderTrack>
                                        <SliderThumb boxSize={6}/>
                                    </Slider>
                                    <Text fontWeight={'bold'}>Width calculation area: {map.width}</Text>
                                    <Slider defaultValue={map.width} onChange={changeWidth} min={40} max={200} step={20}>
                                        <SliderTrack bg="blue.100">
                                            <Box position="relative" right={10}/>
                                            <SliderFilledTrack bg="blue.800"/>
                                        </SliderTrack>
                                        <SliderThumb boxSize={6}/>
                                    </Slider>
                                </> :
                                <>
                                    <Text marginBottom={2}>Please wait a moment, the calculation is in progress.</Text>
                                    <Progress size="sm" isIndeterminate/>
                                </>}
                    </ModalBody>
                    <ModalFooter>
                        {map.status === 'selection' ?
                            map.pointAExists && map.pointBExists ?
                                <Button colorScheme="green" mr={3} onClick={runCalculation}>
                                    Run calculation
                                </Button>
                                : '' : ''}
                        {map.status === 'selection' ?
                            <Button onClick={onClose}>Cancel</Button> : ''}
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
});