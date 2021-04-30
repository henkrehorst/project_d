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
            zoom: 15,
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
    });
};

