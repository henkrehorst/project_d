import {NextPage} from "next";
import {Box, Flex, Menu, Text} from "@chakra-ui/react";
import {NavBar} from "../components/navBar";
import {HistoryView} from "../components/historyView";
import MapView from "../components/mapView";

interface PageProps {
}

const Page: NextPage<PageProps> = () => {
    return (
        <>
            <NavBar/>
            <Flex color={'black'}>
                <Box w={'300px'} overflow={'auto'} p={4} h={'calc(100vh - 72px)'} bg={'gray.100'}>
                    <HistoryView/>
                </Box>
                <Box flex={1}>
                    <MapView/>
                </Box>
            </Flex>
        </>
    )
}

export default Page;