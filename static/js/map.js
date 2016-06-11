mapboxgl.accessToken = 'pk.eyJ1IjoiYXNoaXNoMzE5NyIsImEiOiJjaW10YzluNWgwMXhkdjlrazVsb3BhdnZ1In0.BzeOLoPxqc8-ottHp7tWAg';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v8',
    center: [41.850, -107.650],
    zoom: 3
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
            "icon-image": "library-15",
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

map.on('click', function(e) {

    var cluster_features = map.queryRenderedFeatures(e.point, {
        layers: [
            'cluster-0',
            'cluster-1',
            'cluster-2'
        ]
    });
    if (!cluster_features.length) {
        console.log('point');
        console.log($('#footer').css('height'));
        if($('#footer').css('height')=='83px')
        {
            $('#footer').css('height','90%');
            $('#map').css('opacity','0.5');
        }
        else
        {
            $('#footer').css('height','10%');
            $('#map').css('opacity','1');
        }
    } else {
        console.log('cluster');
    }
    var cluster_feature = cluster_features[0];
    if (cluster_feature && cluster_feature.properties.cluster) {
        map.flyTo({
            center: e.lngLat,
            zoom: map.getZoom() + 1.1
        });
    }
});


