import {FunctionComponent, useContext, useEffect, useState} from "react";
import {Box, Button, Menu, MenuButton, MenuItem, MenuList, Select} from "@chakra-ui/react";
import {ChevronDownIcon} from "@chakra-ui/icons";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {addMarker, refreshMap} from "../services/googleMapsService";

type stateProps = {
    status: 'loading' | 'ready',
    data: [{
        centerCoordinate: { lat: number, lng: number },
        id: number,
        link: string,
        location: string,
        lowerLeft: { lat: number, lng: number },
        upperRight: { lat: number, lng: number },
    }] | null
}

export const MapSelection = observer(() => {
    const map = useContext(MapContext);
    const [locationData, setLocationData] = useState<stateProps>({data: null, status: 'loading'});

    useEffect(() => {
        if (locationData.status === 'loading') {
            fetch(process.env.NEXT_PUBLIC_API_URL + 'data').then((res) => {
                res.json().then(data => {
                    setLocationData({
                        // @ts-ignore
                        data: Object.values(data).map(item => ({
                            centerCoordinate: {
                                lat: Number(item['centercoordinate'].split(',')[0]),
                                lng: Number(item['centercoordinate'].split(',')[1])
                            },
                            id: item['id'],
                            link: item['link'],
                            location: item['location'],
                            lowerLeft: {
                                lat: Number(item['lowerleft'].split(',')[0]),
                                lng: Number(item['lowerleft'].split(',')[1])
                            },
                            upperRight: {
                                lat: Number(item['upperright'].split(',')[0]),
                                lng: Number(item['upperright'].split(',')[1])
                            }
                        })), status: 'ready'
                    });
                })
            })
        }
    });


    const locationChange = (event) => {
        if (locationData.status === 'ready') {
            let locationIndex = Number(event.target.value) - 1;

            map.changeLocation(
                locationData.data[locationIndex].location,
                locationData.data[locationIndex].link,
                locationData.data[locationIndex].lowerLeft,
                locationData.data[locationIndex].upperRight,
                locationData.data[locationIndex].centerCoordinate,
                locationData.data[locationIndex].id
            );

            refreshMap(map);

        }
    }

    return (
        <Select onChange={locationChange} w={60} bg={'white'}>
            {locationData.status === 'loading' ? <option value="Goeree">loading ...</option> :
                locationData.data.map(item => <option key={item.id} value={item.id}>{item.location}</option>)}
        </Select>
    )
});