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
    ModalHeader, ModalOverlay,
    Spacer,
    useDisclosure
} from "@chakra-ui/react";
import {MapSelection} from "./mapSelection";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {refreshMap} from "../services/googleMapsService";


export const NavBar = observer(() => {
    const map = useContext(MapContext);
    const {isOpen, onOpen, onClose} = useDisclosure();

    const onClearClick = () => {
        map.setStatus('selection');
        map.removePointA();
        map.removePointB();
        refreshMap(map);
    }

    return (
        <>
            <Flex backgroundColor={"blue.600"} w={'100%'} p={4} h={'72px'}>
                <MapSelection/>
                <Button marginLeft={'20px'} onClick={onOpen} colorScheme="green">Start berekening</Button>
                <Spacer/>
                <Button colorScheme="red" onClick={onClearClick}>Clear</Button>
            </Flex>
            <Modal closeOnOverlayClick={false} isOpen={isOpen} onClose={onClose}>
                <ModalOverlay/>
                <ModalContent>
                    <ModalHeader>Start berekening</ModalHeader>
                    <ModalCloseButton/>
                    <ModalBody pb={6}>
                        {!map.pointAExists || !map.pointBExists ?
                            <Alert status="error">
                                <AlertIcon/>
                                Selecteer eerst twee punten om het path finding algoritme tussen de twee punten te kunnen starten!
                            </Alert>
                            : 'Klik op run calculation om het path finding algoritme tussen de twee geselecteerde punten te starten.'}
                    </ModalBody>
                    <ModalFooter>
                        {map.pointAExists && map.pointBExists ?
                            <Button colorScheme="green" mr={3}>
                                Run calculation
                            </Button> : ''}
                        <Button onClick={onClose}>Cancel</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
});