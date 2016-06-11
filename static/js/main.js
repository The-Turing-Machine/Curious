mapboxgl.accessToken = 'pk.eyJ1IjoiYXNoaXNoMzE5NyIsImEiOiJjaW10YzluNWgwMXhkdjlrazVsb3BhdnZ1In0.BzeOLoPxqc8-ottHp7tWAg';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v8',
    center: [-32.51469952959991, 18.890056173909848],
    zoom: 1,
});
map.on('load', function() {

    map.addSource("earthquakes", {
        type: "geojson",
        data: "https://www.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson",
        cluster: true,
        clusterMaxZoom: 14, 
        clusterRadius: 50 
    });

    map.addLayer({
        "id": "non-cluster-markers",
        "type": "symbol",
        "source": "earthquakes",
        "layout": {
            "icon-image": "marker-15"
        }
    });

    var layers = [
        [150, '#f28cb1'],
        [20, '#f1f075'],
        [0, '#51bbd6']
    ];

    layers.forEach(function(layer, i) {
        map.addLayer({
            "id": "cluster-" + i,
            "type": "circle",
            "source": "earthquakes",
            "paint": {
                "circle-color": layer[1],
                "circle-radius": 18
            },
            "filter": i == 0 ? [">=", "point_count", layer[0]] : ["all", [">=", "point_count", layer[0]],
                ["<", "point_count", layers[i - 1][0]]
            ]
        });
    });

    // Add a layer for the clusters' count labels
    map.addLayer({
        "id": "cluster-count",
        "type": "symbol",
        "source": "earthquakes",
        "layout": {
            "text-field": "{point_count}",
            "text-font": [
                "DIN Offc Pro Medium",
                "Arial Unicode MS Bold"
            ],
            "text-size": 12
        }
    });
});
