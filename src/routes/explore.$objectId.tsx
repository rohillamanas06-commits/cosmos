import { createFileRoute, Link } from "@tanstack/react-router";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ArrowLeft, ExternalLink } from "lucide-react";
import { loadCosmicObjectById, getCategoryBadgeClass } from "@/lib/cosmic-data";
import type { CosmicObject } from "@/lib/cosmic-data";

// Image map for cosmic objects
const CATEGORY_IMAGES: Record<string, string[]> = {
  "Galaxy": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg",
  ],
  "Black Hole": [
    "/Cygnus X-1.jpg",
    "/M87 (Virgo A Black Hole).jpg",
    "/M87.jpg",
    "/Sagittarius A.jpg",
    "/TON 618.jpg",
    "/NGC 1277 Black Hole.jpg",
    "/M82 X-1.jpg",
    "/AT2019qiz — Tidal Disruption Event.jpg",
    "/GW150914 — First Gravitational Wave Event.jpg",
    "/GW170817 — Neutron Star Merge.jpg",
  ],
  "Nebula": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Crab_Nebula.jpg/1200px-Crab_Nebula.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/NGC_604.jpg/1200px-NGC_604.jpg",
  ],
  "Star": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/1200px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg",
  ],
  "Pulsar": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Crab_Nebula.jpg/1200px-Crab_Nebula.jpg",
  ],
  "Quasar": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg",
  ],
  "Supernova": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_nebula_original.jpg/1200px-Crab_nebula_original.jpg",
  ],
  "Exoplanet": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Exoplanet_Comparison_WASP-17b.png/1200px-Exoplanet_Comparison_WASP-17b.png",
  ],
  "Galaxy Cluster": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg",
  ],
};

const FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg";

// Specific name-based mapping for galaxies - matches exact names from database
const GALAXY_NAME_MAP: Record<string, string> = {
  "Milky Way": "/milky way galaxy.jpg",
  "Triangulum Galaxy": "/triangulum galaxy.jpg",
  "Whirlpool Galaxy": "/Whirlpool Galaxy (M51a).jpg",
  "Cartwheel Galaxy": "/Cartwheel Galaxy.jpg",
  "Sombrero Galaxy": "/Sombrero Galaxy (M104).jpg",
  "Pinwheel Galaxy": "/Pinwheel Galaxy (M101).jpg",
  "Centaurus A": "/Centaurus A (NGC 5128).jpg",
  "Messier 87": "/Messier 87 (M87).jpg",
  "Sculptor Galaxy": "/Sculptor Galaxy (NGC 253).jpg",
  "Cigar Galaxy": "/Cigar Galaxy (M82).jpg",
  "Large Magellanic Cloud": "/Large Magellanic Cloud (LMC).jpg",
  "Small Magellanic Cloud": "/Small Magellanic Cloud (SMC).jpg",
};

const PULSAR_NAME_MAP: Record<string, string> = {
  "PSR J1748-2446ad": "/PSR J1748-2446ad.jpg",
};

const NEBULA_NAME_MAP: Record<string, string> = {
  "Orion Nebula": "/Orion Nebula (M42).jpg",
  "Orion Nebula (M42)": "/Orion Nebula (M42).jpg",
  "M42": "/Orion Nebula (M42).jpg",
  "Crab Nebula": "/Crab Nebula (M1).jpg",
  "Crab Nebula (M1)": "/Crab Nebula (M1).jpg",
  "Crab Nebula (M1, NGC 1952)": "/Crab Nebula (M1, NGC 1952).jpg",
  "M1": "/Crab Nebula (M1).jpg",
  "Eagle Nebula": "/Eagle Nebula (M16).jpg",
  "Eagle Nebula (M16)": "/Eagle Nebula (M16).jpg",
  "M16": "/Eagle Nebula (M16).jpg",
  "Ring Nebula": "/Ring Nebula (M57).jpg",
  "Ring Nebula (M57)": "/Ring Nebula (M57).jpg",
  "M57": "/Ring Nebula (M57).jpg",
  "Lagoon Nebula": "/Lagoon Nebula (M8).jpg",
  "Lagoon Nebula (M8)": "/Lagoon Nebula (M8).jpg",
  "M8": "/Lagoon Nebula (M8).jpg",
  "Trifid Nebula": "/Trifid Nebula (M20).jpg",
  "Trifid Nebula (M20)": "/Trifid Nebula (M20).jpg",
  "M20": "/Trifid Nebula (M20).jpg",
  "Helix Nebula": "/Helix Nebula (NGC 7293).jpg",
  "Helix Nebula (NGC 7293)": "/Helix Nebula (NGC 7293).jpg",
  "NGC 7293": "/Helix Nebula (NGC 7293).jpg",
  "Cat's Eye Nebula": "/Cat's Eye Nebula (NGC 6543).jpg",
  "Cat's Eye Nebula (NGC 6543)": "/Cat's Eye Nebula (NGC 6543).jpg",
  "NGC 6543": "/Cat's Eye Nebula (NGC 6543).jpg",
  "Butterfly Nebula": "/Butterfly Nebula (NGC 6302).jpg",
  "Butterfly Nebula (NGC 6302)": "/Butterfly Nebula (NGC 6302).jpg",
  "NGC 6302": "/Butterfly Nebula (NGC 6302).jpg",
  "Horsehead Nebula": "/Horsehead Nebula (Barnard 33).jpg",
  "Horsehead Nebula (Barnard 33)": "/Horsehead Nebula (Barnard 33).jpg",
  "Barnard 33": "/Horsehead Nebula (Barnard 33).jpg",
  "Carina Nebula": "/Carina Nebula (NGC 3372).jpg",
  "Carina Nebula (NGC 3372)": "/Carina Nebula (NGC 3372).jpg",
  "NGC 3372": "/Carina Nebula (NGC 3372).jpg",
  "NGC 2440": "/NGC 2440 — The Colorful Nebula.jpg",
  "NGC 2440 — The Colorful Nebula": "/NGC 2440 — The Colorful Nebula.jpg",
};

const QUASAR_NAME_MAP: Record<string, string> = {
  "3C 273": "/3C 273.jpg",
  "PKS 2126-158": "/PKS 2126-158.jpg",
  "Quasar J0313-1806": "/Quasar J0313-1806.jpg",
  "S5 0014+81": "/S5 0014+81.jpg",
};

const EXOPLANET_NAME_MAP: Record<string, string> = {
  "51 Pegasi b": "/51 Pegasi b.jpg",
  "Gliese 436b": "/Gliese 436b.jpg",
  "Kepler-186f": "/Kepler-186f.jpg",
  "Kepler-452b": "/Kepler-452b.jpg",
  "Proxima Centauri b": "/Proxima Centauri b.jpg",
  "TRAPPIST-1": "/TRAPPIST-1 System.jpg",
  "TRAPPIST-1 System": "/TRAPPIST-1 System.jpg",
  "TRAPPIST-1b": "/TRAPPIST-1b.jpg",
  "TRAPPIST-1e": "/TRAPPIST-1e.jpg",
  "WASP-12b": "/WASP-12b.jpg",
  "WASP-39b": "/WASP-39b.jpg",
};

const SUPERNOVA_NAME_MAP: Record<string, string> = {
  "SN 1987A": "/SN 1987A.jpg",
  "Crab Nebula (M1, NGC 1952)": "/Crab Nebula (M1, NGC 1952).jpg",
  "Tycho Supernova Remnant — SNR B1572+0449": "/Tycho Supernova Remnant — SNR B1572+0449.jpg",
};

const GALAXY_CLUSTER_NAME_MAP: Record<string, string> = {
  "El Gordo (ACT-CL J0102-4915)": "/El Gordo (ACT-CL J0102-4915).jpg",
  "Bullet Cluster (1E 0657-56)": "/Bullet Cluster (1E 0657-56).jpg"
};

const PLANET_NAME_MAP: Record<string, string> = {
  "Mercury": "/mercury.jpg",
  "Venus": "/venus.jpg",
  "Earth": "/earth.jpg",
  "Mars": "/mars.jpg",
  "Jupiter": "/jupiter.jpg",
  "Saturn": "/saturn.jpg",
  "Uranus": "/uranus.jpg",
  "Neptune": "/neptune.jpg",
};

const MOON_NAME_MAP: Record<string, string> = {
  "Titan": "/titan.jpg",
  "Europa": "/europa.jpg",
  "Io": "/io.jpg",
  "Enceladus": "/Enceladus.jpg",
  "Ganymede": "/Ganymede.jpg",
};

const STAR_NAME_MAP: Record<string, string> = {
  "The Sun": "/the sun.jpg",
  "Sirius": "/Sirius (Alpha Canis Majoris).jpg",
  "Sirius A": "/Sirius (Alpha Canis Majoris).jpg",
  "Alpha Canis Majoris": "/Sirius (Alpha Canis Majoris).jpg",
  "Sirius (Alpha Canis Majoris)": "/Sirius (Alpha Canis Majoris).jpg",
  "Proxima Centauri": "/Proxima Centauri.jpg",
  "Alpha Centauri A": "/Alpha Centauri A (Rigil Kentaurus).jpg",
  "Rigil Kentaurus": "/Alpha Centauri A (Rigil Kentaurus).jpg",
  "Alpha Centauri A (Rigil Kentaurus)": "/Alpha Centauri A (Rigil Kentaurus).jpg",
  "Alpha Centauri B": "/Alpha Centauri B (Toliman).jpg",
  "Toliman": "/Alpha Centauri B (Toliman).jpg",
  "Alpha Centauri B (Toliman)": "/Alpha Centauri B (Toliman).jpg",
  "Alpha Centauri": "/Alpha Centauri System.jpg",
  "Alpha Centauri System": "/Alpha Centauri System.jpg",
  "Betelgeuse": "/Betelgeuse (Alpha Orionis).jpg",
  "Alpha Orionis": "/Betelgeuse (Alpha Orionis).jpg",
  "Betelgeuse (Alpha Orionis)": "/Betelgeuse (Alpha Orionis).jpg",
  "Rigel": "/Rigel.jpg",
  "Beta Orionis": "/Rigel.jpg",
  "Arcturus": "/Arcturus (Alpha Boötis).jpg",
  "Alpha Boötis": "/Arcturus (Alpha Boötis).jpg",
  "Arcturus (Alpha Boötis)": "/Arcturus (Alpha Boötis).jpg",
  "Vega": "/Vega (Alpha Lyrae).jpg",
  "Alpha Lyrae": "/Vega (Alpha Lyrae).jpg",
  "Vega (Alpha Lyrae)": "/Vega (Alpha Lyrae).jpg",
  "Polaris": "/Polaris (Alpha Ursae Minoris).jpg",
  "Alpha Ursae Minoris": "/Polaris (Alpha Ursae Minoris).jpg",
  "Polaris (Alpha Ursae Minoris)": "/Polaris (Alpha Ursae Minoris).jpg",
  "Aldebaran": "/Algol (Beta Persei).jpg",
  "Algol": "/Algol (Beta Persei).jpg",
  "Beta Persei": "/Algol (Beta Persei).jpg",
  "Algol (Beta Persei)": "/Algol (Beta Persei).jpg",
  "Tau Ceti": "/Tau Ceti.jpg",
  "Barnard's Star": "/Barnard's Star.jpg",
  "Mira": "/Mira (Omicron Ceti).jpg",
  "Omicron Ceti": "/Mira (Omicron Ceti).jpg",
  "Mira (Omicron Ceti)": "/Mira (Omicron Ceti).jpg",
  "Eta Carinae": "/Eta Carinae.jpg",
  "S5-HVS1": "/S5-HVS1.jpg",
  "US 708": "/US 708.jpg",
};

const BLACK_HOLE_NAME_MAP: Record<string, string> = {
  "Cygnus X-1": "/Cygnus X-1.jpg",
  "M87* (Virgo A Black Hole)": "M87 (Virgo A Black Hole).jpg",
  "M87*": "/M87.jpg",
  "Sagittarius A": "/Sagittarius A.jpg",
  "Sagittarius A*": "/Sagittarius A.jpg",
  "TON 618": "/TON 618.jpg",
  "NGC 1277 Black Hole": "/NGC 1277 Black Hole.jpg",
  "M82 X-1": "/M82 X-1.jpg",
  "AT2019qiz — Tidal Disruption Event": "/AT2019qiz — Tidal Disruption Event.jpg",
  "GW150914 — First Gravitational Wave Event": "/GW150914 — First Gravitational Wave Event.jpg",
  "GW170817 — Neutron Star Merger": "/GW170817 — Neutron Star Merge.jpg",
};

const NEUTRON_STAR_NAME_MAP: Record<string, string> = {
  "Crab Pulsar (PSR B0531+21)": "/Crab Pulsar (PSR B0531+21).jpg",
  "Vela Pulsar (PSR B0833-45)": "/Vela Pulsar (PSR B0833-45).jpg",
  "PSR J0437-4715 (Millisecond Pulsar)": "/PSR J0437-4715 (Millisecond Pulsar).jpg",
  "Geminga (PSR J0633+1746)": "/Geminga (PSR J0633+1746).jpg",
  "PSR B1919+21 (First Discovered Pulsar)": "/PSR B1919+21 (First Discovered Pulsar).jpg",
  "Double Pulsar (PSR J0737-3039)": "/Double Pulsar (PSR J0737-3039).jpg",
  "PSR B1821-24 (Millisecond Pulsar in Globular Cluster)": "/PSR B1821-24 (Millisecond Pulsar in Globular Cluster).jpg",
  "PSR J1748−2446ad (Fastest Pulsar)": "/PSR J1748−2446ad (Fastest Pulsar).jpg",
  "Black Widow Pulsar (PSR B1957+20)": "/Black Widow Pulsar (PSR B1957+20).jpg",
  "PSR J0030+0451 (NICER Mass-Radius)": "/PSR J0030+0451 (NICER Mass-Radius).jpg",
  "PSR J0030+0451": "/PSR J0030+0451.jpg",
  "Pulsar Wind Nebula (General Class)": "/Pulsar Wind Nebula (General Class).jpg",
  "SGR 0418+5729": "/SGR 0418+5729.jpg",
  "SGR J1745-2900": "/SGR J1745-2900.jpg",
  "SGR 1806-20": "/SGR 1806-20.jpg",
  "SGR 1806-20 (Magnetar)": "/SGR 1806-20 (Magnetar).jpg",
  "Cas A Neutron Star (CXO J232327.9+584842)": "/Cas A Neutron Star (CXO J232327.9+584842).jpg",
  "RCW 103 (1E 161348-5055.5)": "/RCW 103 (1E 161348-5055.5).jpg",
};

const NEUTRON_STAR_SUBTYPE_MAP: Record<string, Record<string, string>> = {
  "4U 0142+61": {
    "Magnetar \u2014 Anomalous X-ray Pulsar (AXP)": "/4U 0142+61 Magnetar \u2014 Anomalous X-ray Pulsar (AXP).jpg",
    "Magnetar with Protoplanetary Disk": "/4U 0142+61 Magnetar with Protoplanetary Disk.jpg",
  },
};

const BROWN_DWARF_NAME_MAP: Record<string, string> = {
  "2MASS J0523-1403": "/2MASS J0523-1403.jpg",
  "WISE 0855-0714": "/WISE 0855-0714.jpg",
  "SDSS 1416+13B": "/SDSS 1416+13B.jpg",
};
function getImageForObject(obj: CosmicObject): string {
  const cat = obj.category;
  
  // Use name-based mapping for galaxies - check exact name match
  if (cat === "Galaxy") {
    if (GALAXY_NAME_MAP[obj.name]) {
      return GALAXY_NAME_MAP[obj.name];
    }
    // Fallback: try to find partial match
    for (const [key, value] of Object.entries(GALAXY_NAME_MAP)) {
      if (obj.name.toLowerCase().includes(key.toLowerCase())) {
        return value;
      }
    }
  }
  
  // Use name-based mapping for black holes
  if (cat === "Black Hole") {
    if (BLACK_HOLE_NAME_MAP[obj.name]) {
      return BLACK_HOLE_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for neutron stars
  if (cat === "Neutron Star") {
    // Special handling for 4U 0142+61 which has two entries with different subtypes
    if (obj.name === "4U 0142+61" && obj.subtype && NEUTRON_STAR_SUBTYPE_MAP["4U 0142+61"]) {
      const subtypeMap = NEUTRON_STAR_SUBTYPE_MAP["4U 0142+61"];
      if (subtypeMap[obj.subtype]) {
        return subtypeMap[obj.subtype];
      }
    }
    // Regular name-based lookup
    if (NEUTRON_STAR_NAME_MAP[obj.name]) {
      return NEUTRON_STAR_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for pulsars
  if (cat === "Pulsar") {
    if (PULSAR_NAME_MAP[obj.name]) {
      return PULSAR_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for nebulas
  if (cat === "Nebula") {
    if (NEBULA_NAME_MAP[obj.name]) {
      return NEBULA_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for quasars
  if (cat === "Quasar") {
    if (QUASAR_NAME_MAP[obj.name]) {
      return QUASAR_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for exoplanets
  if (cat === "Exoplanet") {
    if (EXOPLANET_NAME_MAP[obj.name]) {
      return EXOPLANET_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for supernovae and supernova remnants
  if (cat === "Supernova" || cat === "Supernova Remnant") {
    if (SUPERNOVA_NAME_MAP[obj.name]) {
      return SUPERNOVA_NAME_MAP[obj.name];
    }
  }

  // Use name-based mapping for galaxy clusters
  if (cat === "Galaxy Cluster") {
    if (GALAXY_CLUSTER_NAME_MAP[obj.name]) {
      return GALAXY_CLUSTER_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for planets
  if (cat === "Planet") {
    if (PLANET_NAME_MAP[obj.name]) {
      return PLANET_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for brown dwarfs
  if (cat === "Brown Dwarf") {
    if (BROWN_DWARF_NAME_MAP[obj.name]) {
      return BROWN_DWARF_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for moons
  if (cat === "Moon") {
    if (MOON_NAME_MAP[obj.name]) {
      return MOON_NAME_MAP[obj.name];
    }
  }
  
  // Use name-based mapping for stars
  if (cat === "Star") {
    if (STAR_NAME_MAP[obj.name]) {
      return STAR_NAME_MAP[obj.name];
    }
  }

  const images = CATEGORY_IMAGES[cat];
  if (images && images.length > 0) {
    const idx = obj.id.charCodeAt(obj.id.length - 1) % images.length;
    return images[idx];
  }
  return FALLBACK_IMAGE;
}

export const Route = createFileRoute("/explore/$objectId")({
  head: () => ({
    meta: [
      { title: "Object Detail — Cosmos" },
      { name: "description", content: "Detailed view of a cosmic object." },
    ],
  }),
  validateSearch: (search: Record<string, any>) => ({
    page: search.page ? Number(search.page) : 0,
    category: search.category || null,
  }),
  component: ObjectDetailPage,
});

function formatValue(val: any): string {
  if (val === null || val === undefined) return "—";
  if (typeof val === "object" && !Array.isArray(val)) {
    const parts: string[] = [];
    if (val.value !== undefined) {
      parts.push(typeof val.value === "number" ? val.value.toLocaleString() : String(val.value));
    }
    if (val.unit) parts.push(val.unit);
    if (val.note) parts.push(`(${val.note})`);
    if (val.range) parts.push(`[${val.range}]`);
    if (parts.length > 0) return parts.join(" ");
    return Object.entries(val)
      .map(([k, v]) => `${k}: ${formatValue(v)}`)
      .join(", ");
  }
  if (Array.isArray(val)) return val.join(", ");
  return String(val);
}

function ObjectDetailPage() {
  const { objectId } = Route.useParams();
  const { page, category } = Route.useSearch();
  const [obj, setObj] = useState<CosmicObject | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    document.documentElement.classList.add("dark");
    loadCosmicObjectById(objectId).then((foundObj) => {
      setObj(foundObj);
      setLoading(false);
    });
  }, [objectId]);

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-black/90">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-white/20 border-t-white" />
      </div>
    );
  }

  if (!obj) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-background">
        <h1 className="font-display text-2xl font-bold text-foreground">Object not found</h1>
        <Link to="/explore" search={{ page, ...(category && { category }) }} className="mt-4 text-primary hover:underline">Back to explorer</Link>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="sticky top-0 z-40 border-b border-white/10 bg-[#080808]/90 backdrop-blur-xl">
        <div className="mx-auto flex max-w-screen-xl items-center justify-between px-4 md:px-8 h-14">
          <Link
            to="/explore"
            search={{ page, ...(category && { category }) }}
            className="flex items-center gap-2 text-white hover:text-white/50 transition-colors text-sm font-medium"
          >
            <ArrowLeft className="h-4 w-4" />
            Back to {category ? category : "Explorer"}
          </Link>
        </div>
      </header>

      <div className="mx-auto max-w-screen-xl px-4 md:px-8 py-8">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }}>
          {/* Title area */}
          {/* Title and Image Section */}
          <div className="mb-8 rounded-2xl border border-white/10 bg-gradient-to-r from-white/5 to-transparent p-8 md:p-10">
            <div className="flex flex-col md:flex-row gap-8 items-center md:items-start">
              {/* Text Content */}
              <div className="flex-1">
                <div className="space-y-2">
                  <h1 className="font-display text-3xl md:text-4xl font-bold text-white leading-tight">{obj.name}</h1>
                  {obj.subtype && (
                    <p className="text-sm md:text-base text-white/60 font-light">{obj.subtype}</p>
                  )}
                </div>
              </div>
              
              {/* Image preview */}
              <div className="w-64 h-64 flex-shrink-0 md:w-72 md:h-72">
                <div className="relative w-full h-full rounded-2xl overflow-hidden border border-white/20 bg-black/40 shadow-2xl">
                  <img
                    src={getImageForObject(obj)}
                    alt={obj.name}
                    className="w-full h-full object-cover"
                    onError={(e) => {
                      (e.target as HTMLImageElement).src = FALLBACK_IMAGE;
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent" />
                </div>
              </div>
            </div>
          </div>

          {/* Description */}
          {obj.detailed_description && (
            <Section title="Description">
              <p className="text-white/70 leading-relaxed">{obj.detailed_description}</p>
            </Section>
          )}

          {/* Physical & Spatial data */}
          <div className="grid gap-6 md:gap-8 grid-cols-1 md:grid-cols-2 mt-6">
            {obj.physical && Object.keys(obj.physical).length > 0 && (
              <Section title="Physical Properties">
                <DataTable data={obj.physical} />
              </Section>
            )}
            {obj.spatial && Object.keys(obj.spatial).length > 0 && (
              <Section title="Spatial Data">
                <DataTable data={obj.spatial} />
              </Section>
            )}
          </div>

          {/* Scientific Facts */}
          {obj.scientific_facts && obj.scientific_facts.length > 0 && (
            <Section title="Scientific Facts" className="mt-6">
              <ul className="space-y-2">
                {obj.scientific_facts.map((fact, i) => (
                  <li key={i} className="flex gap-2 text-sm text-white/70">
                    <span className="shrink-0 mt-1 h-1.5 w-1.5 rounded-full bg-white/30" />
                    {fact}
                  </li>
                ))}
              </ul>
            </Section>
          )}

          {/* Did you know */}
          {obj.did_you_know && obj.did_you_know.length > 0 && (
            <Section title="Did You Know?" className="mt-6">
              <ul className="space-y-2">
                {obj.did_you_know.map((fact, i) => (
                  <li key={i} className="flex gap-2 text-sm text-white/70">
                    <span className="shrink-0 mt-1 text-white/60">💡</span>
                    {fact}
                  </li>
                ))}
              </ul>
            </Section>
          )}

          {/* Formation */}
          {obj.formation_process && (
            <Section title="Formation Process" className="mt-6">
              <p className="text-white/70 leading-relaxed text-sm">{obj.formation_process}</p>
            </Section>
          )}

          {/* Future evolution */}
          {obj.future_evolution && (
            <Section title="Future Evolution" className="mt-6">
              <p className="text-white/70 leading-relaxed text-sm">{obj.future_evolution}</p>
            </Section>
          )}

          {/* Related */}
          {obj.related_objects && obj.related_objects.length > 0 && (
            <Section title="Related Objects" className="mt-6">
              <div className="flex flex-wrap gap-2">
                {obj.related_objects.map((r) => (
                  <span key={r} className="rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-white/60">
                    {r}
                  </span>
                ))}
              </div>
            </Section>
          )}

          {/* NASA reference */}
          {obj.nasa_reference && (
            <div className="mt-8 text-center">
              <a
                href={obj.nasa_reference}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-sm text-white/60 hover:underline"
              >
                <ExternalLink className="h-4 w-4" />
                View NASA Reference
              </a>
            </div>
          )}
        </motion.div>
      </div>
    </div>
  );
}

function Section({ icon: Icon, title, children, className = "" }: {
  icon?: React.ComponentType<{ className?: string }>;
  title: string;
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div className={`rounded-xl border border-white/10 bg-white/5 p-4 sm:p-5 overflow-hidden ${className}`}>
      <div className="flex items-center gap-2 mb-3">
        {Icon && <Icon className="h-4 w-4 text-white/60" />}
        <h2 className="font-display text-xs sm:text-sm font-semibold text-white/90 uppercase tracking-wider">{title}</h2>
      </div>
      {children}
    </div>
  );
}

function DataTable({ data }: { data: Record<string, any> }) {
  return (
    <div className="space-y-2 overflow-hidden">
      {Object.entries(data).map(([key, value]) => (
        <div key={key} className="flex flex-col sm:flex-row sm:justify-between sm:gap-4 text-sm border-b border-white/8 pb-1.5 last:border-0">
          <span className="text-white/50 capitalize">{key.replace(/_/g, " ")}</span>
          <span className="text-white/70 text-right font-mono text-xs break-words overflow-hidden">
            {formatValue(value)}
          </span>
        </div>
      ))}
    </div>
  );
}
