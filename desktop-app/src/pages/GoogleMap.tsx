import {Box, Flex} from "@chakra-ui/react";
import {NavBar} from "../components/navBar";
import {HistoryView} from "../components/historyView";
import { FunctionComponent } from "react";
import React from "react";
import GoogleMapsView from "../components/googleMapsView";

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
          <GoogleMapsView/>
        </Box>
      </Flex>
    </>
  )
}

export default GoogleMap;