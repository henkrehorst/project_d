import {FunctionComponent} from "react";
import {Box, Button, Menu, MenuButton, MenuItem, MenuList} from "@chakra-ui/react";
import {ChevronDownIcon} from "@chakra-ui/icons";

interface NavProps {
}

export const MapSelection: FunctionComponent<NavProps> = ({}) => (
        <Menu>
            <MenuButton as={Button} rightIcon={<ChevronDownIcon/>}>
                Choose location
            </MenuButton>
            <MenuList>
                <MenuItem>Goeree</MenuItem>
                <MenuItem>Voorne</MenuItem>
            </MenuList>
        </Menu>
);