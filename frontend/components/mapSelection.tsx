import {FunctionComponent, useContext} from "react";
import {Box, Button, Menu, MenuButton, MenuItem, MenuList, Select} from "@chakra-ui/react";
import {ChevronDownIcon} from "@chakra-ui/icons";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {refreshMap} from "../services/googleMapsService";

export const MapSelection = observer(() => {
    const map = useContext(MapContext);

    const locationChange = (event) => {
        console.log('hello');
        if (event.target.value === 'goeree') {
            map.changeLocation(
                'goeree',
                '/goeree_full.png',
                {lat: 51.7794255, lng: 3.8526257},
                {lat: 51.8453395, lng: 3.9692927},
                {lng: 3.96, lat: 51.844},
            );
            refreshMap(map);
        } else if (event.target.value === 'voorne') {
            map.changeLocation(
                'voorne',
                '/voorne.png',
                {lat: 51.844046, lng: 4.0294408},
                {lat: 51.9248775, lng: 4.0703739},
                {lng: 4.0703739, lat: 51.9248775},
            );
            refreshMap(map);
        }
    }

    return (
        <Select placeholder="Choose location" onChange={locationChange} w={60} bg={'white'}
                defaultValue={map.mapLocation}>
            {map.pointAExists ? console.log('hello'): console.log('jammer')}
            <option value="goeree">Goeree</option>
            <option value="voorne">Voorne</option>
        </Select>
    )
});