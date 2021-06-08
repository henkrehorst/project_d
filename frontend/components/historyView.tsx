import {FunctionComponent} from "react";
import {Text} from "@chakra-ui/react";

interface HistoryProps {}

export const HistoryView: FunctionComponent<HistoryProps> = ({}) => (
  <Text fontWeight={'bold'}>Recente berekeningen</Text>
);