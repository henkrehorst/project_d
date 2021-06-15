import {FunctionComponent, useContext, useEffect, useState} from "react";
import {Center, Skeleton, Spinner, Stack, Text} from "@chakra-ui/react";
import {observer} from "mobx-react-lite";
import {MapContext} from "../stores/mapStore";
import {HistoryItem} from "./historyItem";
import {autorun} from "mobx";

type resItem = {
    Id: number,
    Name: string
    Link: string,
    TopCoordinate: string,
    BottomCoordinate: string,
    DuneLocation: number,
    WaterLevel: number
}

type stateProps = {
    status: 'loading' | 'ready',
    data: [resItem] | null
}

export const HistoryView = observer(() => {
    const map = useContext(MapContext);
    const [historyData, setHistoryData] = useState<stateProps>({data: null, status: 'loading'});

    useEffect(() =>
        autorun(() => {
            if (map.reloadHistory) {
            setHistoryData({data: null, status: 'loading'});
            fetch(process.env.NEXT_PUBLIC_API_URL + 'history/' + map.locationId).then(res => {
                if (res.ok) {
                    res.json().then((data: [resItem]) => {
                        setHistoryData({status: "ready", data: data});
                        map.setHistory(false);
                    })
                }
            })
        }
        }), [])

    return (
        <>
            <Text fontWeight={'bold'} marginBottom={2}>Calculation history</Text>
            {historyData.status === 'loading' ?
                <Center marginTop={'30px'}>
                    <Spinner/>
                </Center> : historyData.data.length <= 0 ? <Text>Calculation history not found</Text> :
                    historyData.data.map(item =>
                        <HistoryItem
                            key={item.Id}
                            id={item.Id}
                            name={item.Name}
                            source={item.Link}
                            upperRight={{
                                lat: Number(item.BottomCoordinate.split(',')[0]),
                                lng: Number(item.BottomCoordinate.split(',')[1])
                            }}
                            lowerLeft={{
                                lat: Number(item.TopCoordinate.split(',')[0]),
                                lng: Number(item.TopCoordinate.split(',')[1])
                            }}
                            duneLocation={item.DuneLocation}
                            waterLevel={item.WaterLevel}
                        />
                    )
            }

        </>
    )
});