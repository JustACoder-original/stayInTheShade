var map = L.map("map").setView([44.58207622, -103.461760283], 5);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {}).addTo(map);

const provider = new GeoSearch.OpenStreetMapProvider();
const searchControl = new GeoSearch.SearchControl({
    provider,
    style: "button",
});

map.addControl(searchControl)