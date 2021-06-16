import {
    Button, Heading, IconButton, Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay, Text, useDisclosure
} from "@chakra-ui/react";
import {InfoIcon} from "@chakra-ui/icons";

export const Manual = () => {
    const {isOpen, onOpen, onClose} = useDisclosure()
    return (
        <>
            <IconButton marginLeft={3} onClick={onOpen} icon={<InfoIcon/>} colorScheme={'blue'} aria-label={'help'}/>
            <Modal
                onClose={onClose}
                isOpen={isOpen}
                motionPreset="slideInBottom"
                size='xl'
            >
                <ModalOverlay/>
                <ModalContent>
                    <ModalHeader>Help</ModalHeader>
                    <ModalCloseButton/>
                    <ModalBody>
                        <Heading size={'md'} marginBottom={2}>
                            Change dune area
                        </Heading>
                        <Text marginBottom={3}>
                            In the upper left corner of the screen you can see a dune area. If you click on this button, it will open the drop-down menu that will show you your options. You can click on the dune area you want to go to.
                        </Text>
                        <Heading size={'md'} marginBottom={2}>
                            Make a calculation
                        </Heading>
                        <Text marginBottom={2}>
                            To make a calculation you first need to select two points. The first point to select is on the sea side and the second point should be more land inwards. For the best result select the points on the black and white part. To select a point, you need to click on the map. By clicking on an existing point, you will delete the existing point. Another method of clearing points is pressing the clear button in the upper right corner.
                        </Text>
                        <Text marginBottom={3}>
                            After selecting two points you can click on the button new calculations. Here you will see two sliders. The first slider is the input that will determine at what water level you test. The second slider will determine how wide the calculation area is. After setting this to the values you want you can press run calculation. The calculation can take some time please wait till it is done.
                        </Text>
                        <Heading size={'md'} marginBottom={2}>
                            Calculation History
                        </Heading>
                        <Text marginBottom={3}>
                            On the left you can see the calculation history. You can see the time and date on which the calculation was made. If you hover over a history point it will show you the water level. If you click on a history item it will show the result on the map.
                        </Text>
                        <Heading size={'md'} marginBottom={2}>
                            Legend
                        </Heading>
                        <Text marginBottom={3}>
                            If a result is open the legend button will appear in the left corner of the screen. When clicked on this button it will show the meaning of the colors.
                        </Text>
                        <Heading size={'md'} marginBottom={2}>
                            Clear
                        </Heading>
                        <Text marginBottom={3}>
                            To clear the website of results and points the clear button in the upper right corner of the screen. By clicking on the clear button everything placed on the map will be removed and the map will center itself.
                        </Text>
                    </ModalBody>
                    <ModalFooter>
                        <Button colorScheme="blue" mr={3} onClick={onClose}>
                            Close
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}