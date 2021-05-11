import { FunctionComponent } from "react";
import { Box } from "@chakra-ui/react";
import { MapSelection } from "./mapSelection";
import React from "react";
interface NavProps {
}

export const NavBar: FunctionComponent<NavProps> = ({}) => (
  <Box backgroundColor={"blue.600"} w={"100%"} p={4} h={"72px"}>
    <MapSelection />
  </Box>
);