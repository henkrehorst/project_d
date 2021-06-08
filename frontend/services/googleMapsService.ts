import { Loader} from "@googlemaps/js-api-loader";

const loader = new Loader({
    apiKey: process.env.NEXT_PUBLIC_GOOGLE_MAP_KEY,
    version: "weekly"
})

let map: google.maps.Map;

export const initMap = (id: string): void => {
    //load google map by element id
    loader.load().then(() => {
        map = new google.maps.Map(document.getElementById(id), {
            center: { lat: 51.844, lng: 3.96 },
            zoom: 13,
        });

        //get location and add marker on click event
        map.addListener('click', (event) => {
            console.log(event.latLng.toJSON());
            new google.maps.Marker({
                position: event.latLng.toJSON(),
                map,
                title: "click"
            })
        });

        interface latLng {
            lat: number,
            lng: number
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

            draw(){
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

        const overlay = new GoogleMapsCustomOverlay(
            {lat: 51.7794255, lng: 3.8526257},
            {lat: 51.8453395, lng: 3.9692927},
            'http://localhost:3000/goeree_full.png'
        );

        overlay.setMap(map);
    });
};

