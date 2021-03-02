import * as React from 'react';
import FeatureLayer from '@arcgis/core/layers/FeatureLayer';
import EsriMap from '@arcgis/core/Map';
import MapView from '@arcgis/core/views/MapView';
import Extent from '@arcgis/core/geometry/Extent';
import { whenFalseOnce, whenTrueOnce } from '@arcgis/core/core/watchUtils';

const defaultExtent = new Extent({
  xmax: -12612006,
  xmin: -12246370,
  ymax: 5125456,
  ymin: 4473357,
  spatialReference: 3857,
});

function App() {
  const mapDiv = React.useRef(null);
  const view = React.useRef(null);
  const layerView = React.useRef(null);
  const clickEvent = React.useRef(null);

  // init map
  React.useEffect(() => {
    if (!mapDiv.current) {
      return;
    }

    console.log('initializing map');

    const layer = new FeatureLayer({
      url: 'https://services1.arcgis.com/99lidPhWCzftIe9K/arcgis/rest/services/PublicLibraries/FeatureServer/0',
      outFields: '*'
    });

    const map = new EsriMap({
      basemap: 'gray'
    });

    view.current = new MapView({
      map,
      container: mapDiv.current,
      extent: defaultExtent,
      ui: {
        components: ['zoom'],
      },
      popup: {
        actions: null,
        spinnerEnabled: false,
        collapseEnabled: false,
        highlightEnabled: false,
        dockOptions: {
          breakpoint: false,
          buttonEnabled: false,
          position: 'top-right',
        },
      },
    });

    map.add(layer);

    layerView.current = view.current.whenLayerView(layer).then((lv) => {
      layerView.current = lv;
    });

    const handle = setTimeout(async () => {
      const layerView = await view.current.whenLayerView(layer);
      layer.definitionExpression = "COUNTY='SALT LAKE'";

      whenTrueOnce(layerView, 'updating', () => {
        whenFalseOnce(layerView, 'updating', async () => {
          const result = await layerView.queryExtent();

          console.log('updating extent', result);

          // this is in case there is a point way outside of the state...
          if (result.count === 0 || result.extent.contains(defaultExtent)) {
            return view.current.goTo(defaultExtent);
          }

          let extent = result.extent;
          if (result.count === 1) {
            extent = {
              target: result.extent,
              scale: 16000,
            };
          }

          return view.current.goTo(extent);
        });
      });
    }, 1000);

    return () => {
      if (handle) {
        clearTimeout(handle);
      }
    }
  }, []);

  // identify
  const identify = React.useCallback(async (where) => {
    if (!where) {
      return;
    }

    console.log('identifying');

    const queryFeatures = async (opts) => {
      const query = {
        geometry: opts.mapPoint,
        distance: view.current.resolution * 7,
        outFields: 'TYPE',
        orderByFields: 'TYPE ASC',
        returnGeometry: true,
      };

      const featureSet = await layerView.current.queryFeatures(query);
      console.log(featureSet.features.length);
    };


    whenFalseOnce(layerView.current, 'updating', () => {
      queryFeatures(where);
    });
  }, [layerView]);

  // init click event
  React.useEffect(() => {
    if (view.current) {
      console.log('adding click event handler');
      clickEvent.current?.remove();
      clickEvent.current = view.current.on('click', (event) => identify(event));
    }
  }, [identify]);

  return (
    <div ref={mapDiv} style={{ height: '100%', width: '100%' }}>
    </div>
  );
}

export default App;
