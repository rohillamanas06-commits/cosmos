let cachedData = null;
const API_BASE_URL = "http://localhost:8000";
async function loadCosmicData() {
  if (cachedData) return cachedData;
  try {
    let allObjects = [];
    let skip = 0;
    let hasMore = true;
    while (hasMore) {
      const res = await fetch(`${API_BASE_URL}/objects?skip=${skip}&limit=100`);
      if (!res.ok) {
        throw new Error(`API error: ${res.status}`);
      }
      const data = await res.json();
      if (data.length === 0) {
        hasMore = false;
      } else {
        allObjects = [...allObjects, ...data];
        skip += 100;
        if (hasMore) {
          await new Promise((resolve) => setTimeout(resolve, 100));
        }
      }
    }
    cachedData = allObjects;
    return cachedData;
  } catch (error) {
    console.error("Failed to load cosmic data from API, falling back to static file:", error);
    const res = await fetch("/cosmic_data.json");
    cachedData = await res.json();
    return cachedData;
  }
}
async function loadCosmicObjectById(objectId) {
  try {
    const res = await fetch(`${API_BASE_URL}/objects/${objectId}`);
    if (!res.ok) {
      if (res.status === 404) {
        return null;
      }
      throw new Error(`API error: ${res.status}`);
    }
    return await res.json();
  } catch (error) {
    console.error(`Failed to load object ${objectId} from API:`, error);
    const allData = await loadCosmicData();
    return allData.find((o) => o.id === objectId) || null;
  }
}
function getCategoryBadgeClass(category) {
  return "border-white/20 text-white/80 bg-white/5";
}
const CATEGORIES = [
  "Galaxy",
  "Black Hole",
  "Star",
  "Nebula",
  "Pulsar",
  "Quasar",
  "Exoplanet",
  "Supernova Remnant",
  "Galaxy Cluster",
  "Neutron Star",
  "Planet",
  "Moon",
  "Brown Dwarf",
  "Variable Star",
  "Blazar",
  "Dark Matter Structure",
  "Cosmic String",
  "Primordial Black Hole",
  "Axion Star",
  "Gamma-Ray Burst",
  "Fast Radio Burst",
  "X-ray Source",
  "Interstellar Object",
  "Space Mission",
  "Star Cluster",
  "Dwarf Planet",
  "Ring Galaxy",
  "Interacting Galaxies",
  "Planetary Nebula",
  "Dark Nebula",
  "Protoplanetary Nebula",
  "Cosmic Structure",
  "Cosmological Structure",
  "Edge-Case Phenomenon",
  "Hypothetical Discovery",
  "Simulated Object"
];
export {
  CATEGORIES as C,
  loadCosmicObjectById as a,
  getCategoryBadgeClass as g,
  loadCosmicData as l
};
