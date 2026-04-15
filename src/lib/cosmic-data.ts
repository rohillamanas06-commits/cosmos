export interface CosmicObject {
  id: string;
  name: string;
  category: string;
  subtype?: string;
  tags?: string[];
  difficulty_level?: string;
  spatial?: Record<string, any>;
  physical?: Record<string, any>;
  detailed_description?: string;
  scientific_facts?: string[];
  did_you_know?: string[];
  formation_process?: string;
  future_evolution?: string;
  related_objects?: string[];
  parent_system?: string;
  child_objects?: string[];
  nasa_reference?: string;
}

let cachedData: CosmicObject[] | null = null;

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function loadCosmicData(): Promise<CosmicObject[]> {
  if (cachedData) return cachedData;
  
  try {
    // Fetch all objects from the backend API (max limit is 100, but we'll fetch with skip to get all)
    let allObjects: CosmicObject[] = [];
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
        // Add small delay between requests to prevent connection issues
        if (hasMore) {
          await new Promise(resolve => setTimeout(resolve, 100));
        }
      }
    }
    
    cachedData = allObjects;
    return cachedData!;
  } catch (error) {
    console.error("Failed to load cosmic data from API, falling back to static file:", error);
    // Fallback to static JSON file if API is not available
    const res = await fetch("/cosmic_data.json");
    cachedData = await res.json();
    return cachedData!;
  }
}

export async function loadCosmicObjectById(objectId: string): Promise<CosmicObject | null> {
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
    // Fallback to loading all data and searching
    const allData = await loadCosmicData();
    return allData.find((o) => o.id === objectId) || null;
  }
}

export function getCategoryBadgeClass(category: string): string {
  const lower = category.toLowerCase();
  if (lower.includes("galaxy")) return "badge-galaxy";
  if (lower.includes("black hole")) return "badge-black-hole";
  if (lower.includes("star") && !lower.includes("axion")) return "badge-star";
  if (lower.includes("nebula")) return "badge-nebula";
  if (lower.includes("pulsar") || lower.includes("neutron")) return "badge-pulsar";
  if (lower.includes("quasar") || lower.includes("blazar")) return "badge-quasar";
  if (lower.includes("exoplanet") || lower.includes("planet")) return "badge-exoplanet";
  return "badge-default";
}

export function getDifficultyColor(level?: string): string {
  switch (level) {
    case "beginner": return "text-cosmos-aurora";
    case "intermediate": return "text-cosmos-solar";
    case "advanced": return "text-cosmos-supernova";
    case "expert": return "text-cosmos-nebula";
    default: return "text-muted-foreground";
  }
}

export const CATEGORIES = [
  "Galaxy", "Black Hole", "Star", "Nebula", "Pulsar", "Quasar",
  "Exoplanet", "Supernova Remnant", "Galaxy Cluster", "Neutron Star",
  "Planet", "Moon", "Brown Dwarf", "Variable Star", "Blazar",
  "Dark Matter Structure", "Cosmic String", "Primordial Black Hole",
  "Axion Star", "Gamma-Ray Burst", "Fast Radio Burst", "X-ray Source",
  "Interstellar Object", "Space Mission", "Star Cluster", "Dwarf Planet",
  "Ring Galaxy", "Interacting Galaxies", "Planetary Nebula", "Dark Nebula",
  "Protoplanetary Nebula", "Cosmic Structure", "Cosmological Structure",
  "Edge-Case Phenomenon", "Hypothetical Discovery", "Simulated Object",
  "Luminous Fast Blue Optical Transient",
];

export const DIFFICULTIES = ["beginner", "intermediate", "advanced", "expert"];
