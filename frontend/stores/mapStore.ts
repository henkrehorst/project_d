import {action, computed, entries, makeAutoObservable} from "mobx";
import {createContext} from "react";

export const MapContext = createContext<MapStore>(null);

export class MapStore {
    status: 'selection' | 'confirm' |'calculation' | 'result';
    mapLocation: string;
    locationId: number;
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
    reloadHistory: boolean;

    constructor(
        location: string,
        mapSource: string,
        lowerLeft: { lat: number, lng: number },
        upperRight: { lat: number, lng: number },
        center: { lat: number, lng: number },
        id: number
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
        this.locationId = id;
        this.reloadHistory = true;
        // @ts-ignore
    }

    changeLocation(
        location: string,
        mapSource: string,
        lowerLeft: { lat: number, lng: number },
        upperRight: { lat: number, lng: number },
        center: { lat: number, lng: number },
        id: number
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
        this.locationId = id;
        this.status = 'selection';
        this.reloadHistory = true;
        // @ts-ignore
    }

    setHistory(val: boolean){
        this.reloadHistory = val;
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

    disablePoints(){
        this.pointAExists = false;
        this.pointBExists = false;
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