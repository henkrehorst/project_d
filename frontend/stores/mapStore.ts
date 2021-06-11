import {action, computed, entries, makeAutoObservable} from "mobx";
import {createContext} from "react";

export const MapContext = createContext<MapStore>(null);

export class MapStore {
    status: 'selection' | 'confirm' |'calculation' | 'result';
    mapLocation: string;
    centerPoint: { lat: number, lng: number };
    mapImageUpperRight: { lat: number, lng: number };
    mapImageLowerLeft: { lat: number, lng: number };
    pointAExists: boolean;
    pointBExists: boolean;
    mapImageSrc: string;
    pointALat: number;
    pointALng: number;
    pointBLat: number;
    pointBLng: number;
    height: number;
    width: number;

    constructor(
        location: string,
        mapSource: string,
        lowerLeft: { lat: number, lng: number },
        upperRight: { lat: number, lng: number },
        center: { lat: number, lng: number }
    ) {
        makeAutoObservable(this)
        this.mapLocation =location;
        this.mapImageSrc = mapSource;
        this.mapImageLowerLeft = lowerLeft;
        this.mapImageUpperRight = upperRight;
        this.centerPoint = center;
        this.pointAExists = false;
        this.pointBExists = false;
        this.status = 'selection'
        this.height = 4;
        this.width = 100;
        // @ts-ignore
    }

    changeLocation(
        location: string,
        mapSource: string,
        lowerLeft: { lat: number, lng: number },
        upperRight: { lat: number, lng: number },
        center: { lat: number, lng: number }
    ) {
        this.mapLocation =location;
        this.mapImageSrc = mapSource;
        this.mapImageLowerLeft = lowerLeft;
        this.mapImageUpperRight = upperRight;
        this.centerPoint = center;
        this.pointAExists = false;
        this.pointBExists = false;
        this.height = 4;
        this.width = 100;
        // @ts-ignore
    }

    setPointA(lat: number, lng: number){
        this.pointALat = lat;
        this.pointALng = lng;
        this.pointAExists = true;
    }

    removePointA(){
        this.pointALat = 0;
        this.pointALng = 0;
        this.pointAExists = false;
    }

    setPointB(lat: number, lng: number){
        this.pointBLat = lat;
        this.pointBLng = lng;
        this.pointBExists = true;
    }

    setHeight(val: number){
        this.height = val;
    }

    setWidth(val: number){
        this.width = val;
    }

    removePointB(){
        this.pointBLat = 0;
        this.pointBLng = 0;
        this.pointBExists = false;
    }

    setStatus(msg: 'selection' | 'confirm' |'calculation' | 'result'){
        this.status = msg;
    }
}