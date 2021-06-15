import {Loader} from "@googlemaps/js-api-loader";
import {MapStore} from "../stores/mapStore";

const loader = new Loader({
    apiKey: process.env.NEXT_PUBLIC_GOOGLE_MAP_KEY,
    version: "weekly"
})

let map: google.maps.Map;
let overlay: any;
let markers = [];
let resultOverlay = null;


interface latLng {
    lat: number,
    lng: number
}

export const initMap = (id: string, mapStore: MapStore): void => {

    //load google map by element id
    loader.load().then(() => {
        map = new google.maps.Map(document.getElementById(id), {
            center: mapStore.centerPoint,
            zoom: 13,
        });

        //get location and add marker on click event
        map.addListener('click', (event) => {
            if (!mapStore.pointAExists || !mapStore.pointBExists) {
                console.log(event.latLng.lng());
                const marker = new google.maps.Marker({
                    position: event.latLng.toJSON(),
                    map,
                    title: "click to remove"
                });

                if (!mapStore.pointAExists) {
                    mapStore.setPointA(event.latLng.lat(), event.latLng.lng());
                } else {
                    mapStore.setPointB(event.latLng.lat(), event.latLng.lng());
                }

                markers.push(marker);
                marker.addListener('click', (event) => {
                    if (marker.getPosition().lat() === mapStore.pointALat &&
                        marker.getPosition().lat() === mapStore.pointALat) {
                        mapStore.removePointA();
                    } else {
                        mapStore.removePointB();
                    }
                    marker.setMap(null);
                });
            }
        });

        class GoogleMapsCustomOverlay extends google.maps.OverlayView {
            private bounds: google.maps.LatLngBounds;
            private image: string;
            private div?: HTMLElement;

            constructor(startCoordinate: latLng, endCoordinate: latLng, imageSrc: string) {
                super();

                this.bounds = new google.maps.LatLngBounds(
                    new google.maps.LatLng(startCoordinate.lat, startCoordinate.lng),
                    new google.maps.LatLng(endCoordinate.lat, endCoordinate.lng)
                );
                this.image = imageSrc;
            }

            onAdd() {
                this.div = document.createElement("div");
                this.div.style.borderStyle = "none";
                this.div.style.borderWidth = "0px";
                this.div.style.position = "absolute";

                // Create the img element and attach it to the div.
                const img = document.createElement("img");
                img.src = this.image;
                img.style.width = "100%";
                img.style.height = "100%";
                img.style.position = "absolute";
                this.div.appendChild(img);

                // Add the element to the "overlayLayer" pane.
                const panes = this.getPanes()!;
                panes.overlayLayer.appendChild(this.div);
            }

            draw() {
                const projection = this.getProjection();

                const sw = projection.fromLatLngToDivPixel(
                    this.bounds.getSouthWest()
                )!;
                const ne = projection.fromLatLngToDivPixel(
                    this.bounds.getNorthEast()
                )!;

                // Resize the image's div to fit the indicated dimensions.
                if (this.div) {
                    this.div.style.left = sw.x + "px";
                    this.div.style.top = ne.y + "px";
                    this.div.style.width = ne.x - sw.x + "px";
                    this.div.style.height = sw.y - ne.y + "px";
                }
            }

            onRemove() {
                if (this.div) {
                    (this.div.parentNode as HTMLElement).removeChild(this.div);
                    delete this.div;
                }
            }
        }

        overlay = new GoogleMapsCustomOverlay(
            mapStore.mapImageLowerLeft,
            mapStore.mapImageUpperRight,
            mapStore.mapImageSrc
        );

        overlay.setMap(map);
    });
};


export const refreshMap = (store: MapStore) => {
    map.setCenter(store.centerPoint);
    map.setZoom(13);
    //remove all markers on map
    for (let i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
    overlay.setMap(null);

    if (resultOverlay != null) {
        resultOverlay.setMap(null);
    }


    class GoogleMapsCustomOverlay extends google.maps.OverlayView {
        private bounds: google.maps.LatLngBounds;
        private image: string;
        private div?: HTMLElement;

        constructor(startCoordinate: latLng, endCoordinate: latLng, imageSrc: string) {
            super();

            this.bounds = new google.maps.LatLngBounds(
                new google.maps.LatLng(startCoordinate.lat, startCoordinate.lng),
                new google.maps.LatLng(endCoordinate.lat, endCoordinate.lng)
            );
            this.image = imageSrc;
        }

        onAdd() {
            this.div = document.createElement("div");
            this.div.style.borderStyle = "none";
            this.div.style.borderWidth = "0px";
            this.div.style.position = "absolute";

            // Create the img element and attach it to the div.
            const img = document.createElement("img");
            img.src = this.image;
            img.style.width = "100%";
            img.style.height = "100%";
            img.style.position = "absolute";
            this.div.appendChild(img);

            // Add the element to the "overlayLayer" pane.
            const panes = this.getPanes()!;
            panes.overlayLayer.appendChild(this.div);
        }

        draw() {
            const projection = this.getProjection();

            const sw = projection.fromLatLngToDivPixel(
                this.bounds.getSouthWest()
            )!;
            const ne = projection.fromLatLngToDivPixel(
                this.bounds.getNorthEast()
            )!;

            // Resize the image's div to fit the indicated dimensions.
            if (this.div) {
                this.div.style.left = sw.x + "px";
                this.div.style.top = ne.y + "px";
                this.div.style.width = ne.x - sw.x + "px";
                this.div.style.height = sw.y - ne.y + "px";
            }
        }

        onRemove() {
            if (this.div) {
                (this.div.parentNode as HTMLElement).removeChild(this.div);
                delete this.div;
            }
        }
    }

    overlay = new GoogleMapsCustomOverlay(
        store.mapImageLowerLeft,
        store.mapImageUpperRight,
        store.mapImageSrc
    );

    overlay.setMap(map);
};


export const displayResultOverlay = (source: string, lowerLeft: latLng, upperRight: latLng): void => {
    class GoogleMapsCustomOverlay extends google.maps.OverlayView {
        private bounds: google.maps.LatLngBounds;
        private image: string;
        private div?: HTMLElement;

        constructor(startCoordinate: latLng, endCoordinate: latLng, imageSrc: string) {
            super();

            this.bounds = new google.maps.LatLngBounds(
                new google.maps.LatLng(startCoordinate.lat, startCoordinate.lng),
                new google.maps.LatLng(endCoordinate.lat, endCoordinate.lng)
            );
            this.image = imageSrc;
        }

        onAdd() {
            this.div = document.createElement("div");
            this.div.style.borderStyle = "none";
            this.div.style.borderWidth = "0px";
            this.div.style.position = "absolute";

            // Create the img element and attach it to the div.
            const img = document.createElement("img");
            img.src = this.image;
            img.style.width = "100%";
            img.style.height = "100%";
            img.style.position = "absolute";
            this.div.appendChild(img);

            // Add the element to the "overlayLayer" pane.
            const panes = this.getPanes()!;
            panes.overlayLayer.appendChild(this.div);
        }

        draw() {
            const projection = this.getProjection();

            const sw = projection.fromLatLngToDivPixel(
                this.bounds.getSouthWest()
            )!;
            const ne = projection.fromLatLngToDivPixel(
                this.bounds.getNorthEast()
            )!;

            // Resize the image's div to fit the indicated dimensions.
            if (this.div) {
                this.div.style.left = sw.x + "px";
                this.div.style.top = ne.y + "px";
                this.div.style.width = ne.x - sw.x + "px";
                this.div.style.height = sw.y - ne.y + "px";
            }
        }

        onRemove() {
            if (this.div) {
                (this.div.parentNode as HTMLElement).removeChild(this.div);
                delete this.div;
            }
        }
    }

    if(resultOverlay != null){
        resultOverlay.setMap(null)
    }

    // @ts-ignore
    resultOverlay = new GoogleMapsCustomOverlay(lowerLeft, upperRight, source);

    resultOverlay.setMap(map);
}

export const addMarker = (x, y) => {
    new google.maps.Marker({
        position:{ lat: Number(x), lng: Number(y) },
        map,
        title: "click to remove"
    });
}

export const removeMarkers = () => {
    //remove all markers on map
    for (let i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
}

export const goTo = (zoom: number, position: latLng) => {
    map.setZoom(zoom);
    map.setCenter(position);
}