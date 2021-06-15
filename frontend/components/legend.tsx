import {observer} from "mobx-react-lite";
import {useContext} from "react";
import {MapContext} from "../stores/mapStore";
import {
    Box,
    Button,
    Popover, PopoverArrow,
    PopoverBody,
    PopoverCloseButton,
    PopoverContent,
    PopoverHeader,
    PopoverTrigger, Text
} from "@chakra-ui/react";

export const Legend = observer(() => {
    const mapStore = useContext(MapContext);
    return (
        <Popover>
            <PopoverTrigger>
                <Button colorScheme={'orange'} marginLeft={'20px'}>Legend</Button>
            </PopoverTrigger>
            <PopoverContent>
                <PopoverArrow/>
                <PopoverCloseButton/>
                <PopoverHeader>Legend (water level: {mapStore.height})</PopoverHeader>
                <PopoverBody fontWeight={'bold'}>
                    <Text display={'flex'} marginBottom={2} >
                        <Box w={'30px'} h={'25px'} border={'1px solid black'} bg={'red'} marginRight={'15px'}/>
                        {'<='} {Math.floor(mapStore.height / 3)} meter
                    </Text>
                    <Text display={'flex'} marginBottom={2}>
                        <Box w={'30px'} h={'25px'} border={'1px solid black'} bg={'orange'} marginRight={'15px'}/>
                        {'>'} {Math.floor(mapStore.height / 3) } meter and {'<='} {Math.floor(mapStore.height / 3) * 2 } meter
                    </Text>
                    <Text display={'flex'} marginBottom={2}>
                        <Box w={'30px'} h={'25px'} border={'1px solid black'} bg={'yellow'} marginRight={'15px'}/>
                        {'>'} {Math.floor(mapStore.height / 3) * 2 } meter and {'<='} {mapStore.height} meter
                    </Text>
                </PopoverBody>
            </PopoverContent>
        </Popover>
    )
})