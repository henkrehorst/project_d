import React from "react";
import Home from "./pages/Home";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import GoogleMap from "./pages/GoogleMap";
import {ChakraProvider} from "@chakra-ui/react";

export default function App() {
  return (
    <Router>
      <ChakraProvider>
        <Switch>
          <Route path="/map" component={GoogleMap} />
          <Route path="/" component={Home} />
        </Switch>
      </ChakraProvider>
    </Router>
  );
}