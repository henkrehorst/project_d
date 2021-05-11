import {Box, Flex} from "@chakra-ui/react";
import {NavBar} from "../components/navBar";
import {HistoryView} from "../components/historyView";
import MapView from "../components/mapView";
import { FunctionComponent } from "react";
import React from "react";

interface PageProps {
}

const GoogleMap: FunctionComponent<PageProps> = () => {
  return (
    <>
      <NavBar/>
      <Flex color={'black'}>
        <Box w={'300px'} p={4} h={'calc(100vh - 72px)'} bg={'gray.100'}>
          <HistoryView/>
        </Box>
        <Box flex={1}>
          <MapView/>
        </Box>
      </Flex>
    </>
  )
}

export default GoogleMap;