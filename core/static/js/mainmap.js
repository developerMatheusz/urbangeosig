const geoServer = $("#geoserver").val() + "/wms";
const clickUrl = $("#click").val().replace("0/0/", "");

const registerSetor = L.tileLayer.wms(geoServer, {
  layers: "urbangeosig:register_setor",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
  maxZoom: 20,
  zIndex: 1,
  attribution: "Prefeitura Municipal de Cassilândia"
});

const registerQuadra = L.tileLayer.wms(geoServer, {
  layers: "urbangeosig:register_quadra",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
  maxZoom: 20,
  zIndex: 1,
  attribution: "Prefeitura Municipal de Cassilândia"
});

const registerLote = L.tileLayer.wms(geoServer, {
  layers: "urbangeosig:register_lote",
  format: "image/png",
  transparent: true,
  version: "1.1.0",
  maxZoom: 20,
  zIndex: 1,
  attribution: "Prefeitura Municipal de Cassilândia"
});

const googleStreets = L.tileLayer(
  "https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
  {
    maxZoom: 20,
    subdomains: ["mt0", "mt1", "mt2", "mt3"],
    attribution: "Google Maps"
  }
);

const googleSat = L.tileLayer(
  "https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
  {
    maxZoom: 20,
    subdomains: ["mt0", "mt1", "mt2", "mt3"],
    attribution: "Google Maps"
  }
);

const googleTerrain = L.tileLayer(
  "https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
  {
    maxZoom: 20,
    subdomains: ["mt0", "mt1", "mt2", "mt3"],
    attribution: "Google Maps"
  }
);

const osm = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});

const map = L.map("map", {
  center: [-19.1126910811961, -51.73431873321534],
  zoom: 15,
  zoomControl: false,
  layers: [googleSat, registerLote, registerQuadra, registerSetor]
});

const baseLayers = {
  "Google Satélite": googleSat,
  "Google Streets": googleStreets,
  "Google Terreno": googleTerrain
};

const overlays = {
  Lotes: registerLote,
  Quadras: registerQuadra,
  Setores: registerSetor
};

const layerControl = L.control.layers(baseLayers, overlays).addTo(map);

const zoomHome = L.Control.zoomHome();
zoomHome.addTo(map);

var popup = L.popup();

function onMapClick(e) {
  let url = `${clickUrl}${e.latlng.lng}/${e.latlng.lat}/`;

  axios
    .get(url)
    .then(function (response) {
      if (!response.data.includes("******")) {
        popup.setLatLng(e.latlng).setContent(response.data).openOn(map);
      }
    })
    .catch(function (error) {
      console.log(error);
    })
    .finally(function () {});
}

map.on("click", onMapClick);
