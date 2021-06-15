import {FunctionComponent} from "react";
import {Text} from "@chakra-ui/react";

interface HistoryItemProps {
    id: number,
    name: string,
    source: string,
    upperRight: {lat: number, lng: number},
    lowerLeft: {lat: number, lng: number},
    duneLocation: number
}

export const HistoryItem: FunctionComponent<HistoryItemProps> = ({id,name,source,upperRight,lowerLeft,duneLocation}) => {
    return (
  <>
    <Text>{name}</Text>
  </>
)};