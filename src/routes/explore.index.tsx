import { createFileRoute, Link, useNavigate } from "@tanstack/react-router";
import { useState, useEffect, useMemo, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, X, ChevronLeft, ChevronRight, SlidersHorizontal, ExternalLink, ArrowLeft } from "lucide-react";
import { loadCosmicData, CATEGORIES, getCategoryBadgeClass } from "@/lib/cosmic-data";
import type { CosmicObject } from "@/lib/cosmic-data";

export const Route = createFileRoute("/explore/")({
  head: () => ({
    meta: [
      { title: "Explore — Cosmos" },
      { name: "description", content: "Browse and search 169 cosmic objects with filters by category and difficulty." },
      { property: "og:title", content: "Explore — Cosmos" },
      { property: "og:description", content: "Browse and search 169 cosmic objects." },
    ],
  }),
  validateSearch: (search: Record<string, any>) => ({
    page: search.page ? Number(search.page) : 0,
  }),
  component: ExplorePage,
});

const PAGE_SIZE = 24;

// Curated NASA/public domain image map for cosmic object categories
const CATEGORY_IMAGES: Record<string, string[]> = {
  "Galaxy": [
    "/taneli-lahtinen-3G8p__Lv8iM-unsplash.jpg",
    "/Whirlpool Galaxy (M51a).jpg",
    "/Cartwheel Galaxy.jpg",
    "/Centaurus A (NGC 5128).jpg",
    "/Cigar Galaxy (M82).jpg",
    "/Messier 87 (M87).jpg",
    "/milky way galaxy.jpg",
    "/Pinwheel Galaxy (M101).jpg",
    "/Sculptor Galaxy (NGC 253).jpg",
    "/Triangulum galaxy.jpg",
    "/Small Magellanic Cloud (SMC).jpg",
    "/Sombrero Galaxy (M104).jpg",
    "/Large Magellanic Cloud (LMC).jpg",
  ],
  "Black Hole": [
    "/nasa-hubble-space-telescope-17hchodU6sA-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Black_hole_-_Messier_87_crop_max_res.jpg/600px-Black_hole_-_Messier_87_crop_max_res.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Black_hole_event_horizon_simulation.jpg/600px-Black_hole_event_horizon_simulation.jpg",
  ],
  "Nebula": [
    "/aldebaran-s-qtRF_RxCAo0-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Crab_Nebula.jpg/600px-Crab_Nebula.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/NGC_604.jpg/600px-NGC_604.jpg",
  ],
  "Star": [
    "/ivana-cajina-IwK0lkENPKY-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/600px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Sirius_A_and_B_Hubble_Photo_-_annotated.full.jpg/600px-Sirius_A_and_B_Hubble_Photo_-_annotated.full.jpg",
  ],
  "Pulsar": [
    "/nasa-hubble-space-telescope-e_VUMccLu-k-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Crab_Nebula.jpg/600px-Crab_Nebula.jpg",
  ],
  "Quasar": [
    "/nasa-hubble-space-telescope-gbw_PRLvhJA-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/600px-Hubble_ultra_deep_field.jpg",
  ],
  "Supernova Remnant": [
    "/tengyart-Q78W18T-dss-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_nebula_original.jpg/600px-Crab_nebula_original.jpg",
  ],
  "Exoplanet": [
    "/nasa-hubble-space-telescope-hdDjmN0iraw-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Exoplanet_Comparison_WASP-17b.png/600px-Exoplanet_Comparison_WASP-17b.png",
  ],
  "Galaxy Cluster": [
    "/nasa-hubble-space-telescope-tcgaCmVyueY-unsplash.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/600px-Hubble_ultra_deep_field.jpg",
  ],
  "Brown Dwarf": [
    "/brown dwarf.jpg",
  ],
  "Moon": [
    "/moon.jpg",
  ],
  "Neutron Star": [
    "/neutron star.jpg",
  ],
  "Planet": [
    "/planet.jpg",
  ],
  "Cosmic String": [
    "/cosmic string.jpg",
  ],
  "Dark Matter Structure": [
    "/dark matter.jpg",
  ],
  "Gamma-Ray Burst": [
    "/gamma ray.jpg",
  ],
  "Primordial Black Hole": [
    "/primordial black hole.jpg",
  ],
  "Axion Star": [
    "/axion star.jpg",
  ],
  "Fast Radio Burst": [
    "/radio burst.jpg",
  ],
  "Variable Star": [
    "/variable star.jpg",
  ],
  "Blazar": [
    "/blazer.jpg",
  ],
  "Space Mission": [
    "/space mission.jpg",
  ],
  "Ring Galaxy": [
    "/ring galaxies.jpg",
  ],
  "Interacting Galaxies": [
    "/interacting glaxies.jpg",
  ],
  "X-ray Source": [
    "/xray source.jpg",
  ],
  "Star Cluster": [
    "/star cluster.jpg",
  ],
  "Dwarf Planet": [
    "/dwarf planet.jpg",
  ],
  "Planetary Nebula": [
    "/planetery nebula.jpg",
  ],
  "Dark Nebula": [
    "/dark nebula.jpg",
  ],
  "Protoplanetary Nebula": [
    "/protoplanetry nebula.jpg",
  ],
  "Cosmic Structure": [
    "/cosmic structure.jpg",
  ],
  "Cosmological Structure": [
    "/cosmological structure.jpg",
  ],
  "Edge-Case Phenomenon": [
    "/edge class phenomenon.jpg",
  ],
  "Hypothetical Discovery": [
    "/hypothetical discovery.jpg",
  ],
  "Simulated Object": [
    "/simulated object.jpg",
  ],
  "Interstellar Object": [
    "/interstellar object.jpg",
  ],
};

const FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/600px-Hubble_ultra_deep_field.jpg";

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

const SUPERNOVA_NAME_MAP: Record<string, string> = {
  "SN 1987A": "/SN 1987A.jpg",
  "Crab Nebula (M1, NGC 1952)": "/Crab Nebula (M1, NGC 1952).jpg",
  "Tycho Supernova Remnant — SNR B1572+0449": "/Tycho Supernova Remnant — SNR B1572+0449.jpg",
};

const GALAXY_CLUSTER_NAME_MAP: Record<string, string> = {
  "El Gordo (ACT-CL J0102-4915)": "/El Gordo (ACT-CL J0102-4915).jpg",
  "Bullet Cluster (1E 0657-56)": "/Bullet Cluster (1E 0657-56).jpg"
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
  
  // Use name-based mapping for pulsars
  if (cat === "Pulsar") {
    if (PULSAR_NAME_MAP[obj.name]) {
      return PULSAR_NAME_MAP[obj.name];
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
  
  const images = CATEGORY_IMAGES[cat];
  if (images && images.length > 0) {
    // deterministic pick based on object id
    const idx = obj.id.charCodeAt(obj.id.length - 1) % images.length;
    return images[idx];
  }
  return FALLBACK_IMAGE;
}

function formatValue(val: any): string {
  if (val === null || val === undefined) return "—";
  if (typeof val === "object" && !Array.isArray(val)) {
    const parts: string[] = [];
    if (val.value !== undefined) parts.push(String(val.value));
    if (val.unit) parts.push(val.unit);
    if (val.note) parts.push(`(${val.note})`);
    return parts.join(" ") || JSON.stringify(val);
  }
  if (Array.isArray(val)) return val.join(", ");
  return String(val);
}

// ─── Image Panel ─────────────────────────────────────────────────────────────

function ImagePanel({ obj, onClose, dark, currentPage }: { obj: CosmicObject; onClose: () => void; dark: boolean; currentPage: number }) {
  const imageUrl = getImageForObject(obj);

  return (
    <motion.div
      initial={{ x: "100%", opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: "100%", opacity: 0 }}
      transition={{ type: "spring", stiffness: 300, damping: 30 }}
      className={`fixed top-0 right-0 h-full w-full sm:w-[420px] z-50 flex flex-col shadow-2xl border-l ${
        dark
          ? "bg-[#0a0a0a] border-white/10 text-white"
          : "bg-white border-black/10 text-black"
      }`}
    >
      {/* Panel Header */}
      <div className={`flex items-center justify-between px-5 py-4 border-b ${dark ? "border-white/10" : "border-black/10"}`}>
        <div className="flex items-center gap-2">
          <span className={`text-xs font-semibold uppercase tracking-widest ${dark ? "text-white/40" : "text-black/40"}`}>
            Object Detail
          </span>
        </div>
        <button
          onClick={onClose}
          className={`p-1.5 rounded-md transition-colors ${dark ? "hover:bg-white/10 text-white/60 hover:text-white" : "hover:bg-black/5 text-black/40 hover:text-black"}`}
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {/* Scrollable content */}
      <div className="flex-1 overflow-y-auto">
        {/* Image */}
        <div className="relative w-full aspect-video bg-black/20 overflow-hidden">
          <img
            src={imageUrl}
            alt={obj.name}
            className="w-full h-full object-cover"
            onError={(e) => {
              (e.target as HTMLImageElement).src = FALLBACK_IMAGE;
            }}
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
        </div>

        {/* Info */}
        <div className="px-5 py-5 space-y-5">
          <div>
            <h2 className="text-xl font-bold tracking-tight">{obj.name}</h2>
            {obj.subtype && (
              <p className={`text-sm mt-0.5 ${dark ? "text-white/50" : "text-black/50"}`}>{obj.subtype}</p>
            )}
          </div>

          {obj.detailed_description && (
            <p className={`text-sm leading-relaxed ${dark ? "text-white/70" : "text-black/70"}`}>
              {obj.detailed_description}
            </p>
          )}

          {/* Physical Properties */}
          {obj.physical && Object.keys(obj.physical).length > 0 && (
            <div>
              <h3 className={`text-xs font-semibold uppercase tracking-widest mb-2 ${dark ? "text-white/40" : "text-black/40"}`}>
                Physical Properties
              </h3>
              <div className={`rounded-lg overflow-hidden border ${dark ? "border-white/10" : "border-black/10"}`}>
                {Object.entries(obj.physical).slice(0, 5).map(([key, val], i) => (
                  <div
                    key={key}
                    className={`flex justify-between items-start px-3 py-2 text-sm ${
                      i % 2 === 0
                        ? dark ? "bg-white/5" : "bg-black/3"
                        : ""
                    }`}
                  >
                    <span className={`capitalize ${dark ? "text-white/50" : "text-black/50"}`}>
                      {key.replace(/_/g, " ")}
                    </span>
                    <span className={`font-mono text-xs text-right max-w-[55%] ${dark ? "text-white/80" : "text-black/80"}`}>
                      {formatValue(val)}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Scientific Facts */}
          {obj.scientific_facts && obj.scientific_facts.length > 0 && (
            <div>
              <h3 className={`text-xs font-semibold uppercase tracking-widest mb-2 ${dark ? "text-white/40" : "text-black/40"}`}>
                Key Facts
              </h3>
              <ul className="space-y-1.5">
                {obj.scientific_facts.slice(0, 4).map((fact, i) => (
                  <li key={i} className={`flex gap-2 text-sm ${dark ? "text-white/65" : "text-black/65"}`}>
                    <span className={`mt-1.5 w-1 h-1 rounded-full flex-shrink-0 ${dark ? "bg-white/40" : "bg-black/30"}`} />
                    {fact}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>

      {/* Footer action */}
      <div className={`px-5 py-4 border-t ${dark ? "border-white/10" : "border-black/10"}`}>
        <Link
          to="/explore/$objectId"
          params={{ objectId: obj.id }}
          search={{ page: currentPage }}
          className={`flex items-center justify-center gap-2 w-full py-2.5 rounded-lg text-sm font-medium transition-colors ${
            dark
              ? "bg-white text-black hover:bg-white/90"
              : "bg-black text-white hover:bg-black/90"
          }`}
        >
          View Full Details
          <ExternalLink className="w-3.5 h-3.5" />
        </Link>
      </div>
    </motion.div>
  );
}

// ─── Object Row Card ──────────────────────────────────────────────────────────

function ObjectCard({
  obj,
  index,
  dark,
  selected,
  onClick,
}: {
  obj: CosmicObject;
  index: number;
  dark: boolean;
  selected: boolean;
  onClick: () => void;
}) {
  const imageUrl = getImageForObject(obj);
  
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.2, delay: Math.min(index * 0.02, 0.3) }}
      onClick={onClick}
      className={`group cursor-pointer rounded-xl border overflow-hidden transition-all duration-150 flex flex-col ${
        selected
          ? dark
            ? "border-white/40 bg-white/8"
            : "border-black/30 bg-black/5"
          : dark
          ? "border-white/8 bg-white/3 hover:border-white/20 hover:bg-white/6"
          : "border-black/8 bg-black/2 hover:border-black/20 hover:bg-black/4"
      }`}
    >
      {/* Image */}
      <div className="relative w-full aspect-video bg-gradient-to-br from-gray-700 to-gray-900 overflow-hidden">
        <img
          src={imageUrl}
          alt={obj.name}
          className="w-full h-full object-cover"
          loading="lazy"
          decoding="async"
          onError={(e) => {
            (e.target as HTMLImageElement).src = FALLBACK_IMAGE;
          }}
        />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent to-black/40" />
      </div>
      
      {/* Content */}
      <div className="px-4 py-3 flex-1 flex flex-col justify-between">
        <div>
          <h3 className={`font-semibold text-sm tracking-tight ${dark ? "text-white" : "text-black"}`}>
            {obj.name}
          </h3>
          {obj.subtype && (
            <p className={`text-xs mt-1 ${dark ? "text-white/45" : "text-black/45"}`}>
              {obj.subtype}
            </p>
          )}
        </div>
        <div className="mt-3">
          <span className={`inline-block text-xs font-medium px-2.5 py-0.5 rounded-full border ${getCategoryBadgeClass(obj.category)}`}>
            {obj.category}
          </span>
        </div>
      </div>
    </motion.div>
  );
}

// ─── Main Page ────────────────────────────────────────────────────────────────

function ExplorePage() {
  const { page: initialPage } = Route.useSearch();
  const navigate = useNavigate({ from: "/explore/" });
  const [objects, setObjects] = useState<CosmicObject[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [showFilters, setShowFilters] = useState(false);
  const [page, setPage] = useState(initialPage);
  const [dark, setDark] = useState(true);
  const [activeObject, setActiveObject] = useState<CosmicObject | null>(null);

  // Helper to update page and URL
  const handlePageChange = useCallback((newPage: number) => {
    setPage(newPage);
    navigate({ search: { page: newPage } });
  }, [navigate]);

  useEffect(() => {
    loadCosmicData().then((data) => {
      setObjects(data);
      setLoading(false);
    });
  }, []);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);

  const filtered = useMemo(() => {
    let result = objects;
    if (search) {
      const q = search.toLowerCase();
      result = result.filter(
        (o) =>
          o.name.toLowerCase().includes(q) ||
          o.category.toLowerCase().includes(q)
      );
    }
    if (selectedCategory) result = result.filter((o) => o.category === selectedCategory);
    return result;
  }, [objects, search, selectedCategory]);

  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginated = filtered.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);

  useEffect(() => { handlePageChange(0); }, [search, selectedCategory, handlePageChange]);

  const activeCategories = useMemo(() => {
    const cats = new Set(objects.map((o) => o.category));
    return CATEGORIES.filter((c) => cats.has(c));
  }, [objects]);

  const handleCardClick = useCallback((obj: CosmicObject) => {
    setActiveObject((prev) => (prev?.id === obj.id ? null : obj));
  }, []);

  const bg = dark ? "bg-[#080808]" : "bg-[#f9f9f7]";
  const textPrimary = dark ? "text-white" : "text-black";
  const textMuted = dark ? "text-white/50" : "text-black/50";
  const borderColor = dark ? "border-white/10" : "border-black/10";
  const headerBg = dark ? "bg-[#080808]/90" : "bg-[#f9f9f7]/90";
  const inputBg = dark ? "bg-white/5 border-white/10 text-white placeholder:text-white/35 focus:border-white/30" : "bg-black/3 border-black/10 text-black placeholder:text-black/35 focus:border-black/30";
  const btnOutline = dark ? "border-white/15 hover:border-white/30 text-white/70 hover:text-white" : "border-black/15 hover:border-black/30 text-black/70 hover:text-black";

  if (loading) {
    return (
      <div className={`flex min-h-screen items-center justify-center ${bg}`}>
        <div className="text-center">
          <div className={`mx-auto h-8 w-8 animate-spin rounded-full border-2 ${dark ? "border-white/20 border-t-white" : "border-black/20 border-t-black"}`} />
          <p className={`mt-4 text-sm ${textMuted}`}>Loading cosmic data...</p>
        </div>
      </div>
    );
  }

  return (
    <div className={`min-h-screen ${bg} transition-colors duration-200`}>
      {/* Header */}
      <header className={`sticky top-0 z-40 border-b ${borderColor} ${headerBg} backdrop-blur-xl`}>
        <div className="mx-auto flex max-w-screen-xl items-center justify-between px-4 md:px-8 h-14">
          {/* Left */}
          <div className="flex items-center gap-6">
            <Link to="/" className={`flex items-center gap-2 ${textPrimary} hover:${textMuted} transition-colors text-sm font-medium`}>
              <ArrowLeft className="h-4 w-4" />
              Back to Home
            </Link>
          </div>

          {/* Right */}
          <div className="flex items-center gap-2">
          </div>
        </div>
      </header>

      {/* Page layout: list + panel */}
      <div className="mx-auto max-w-screen-xl px-4 md:px-8 py-7">
        {/* Category Selection Carousel */}
        {!selectedCategory && (
          <div className="mb-10">
            <div className="mb-4">
              <h2 className={`text-2xl font-bold ${textPrimary}`}>What would you like to explore?</h2>
              <p className={`text-sm ${textMuted} mt-1`}>Browse by category or search for specific objects</p>
            </div>
            <div className="grid grid-cols-3 gap-3">
              {activeCategories.map((cat) => {
                const categoryCount = objects.filter((o) => o.category === cat).length;
                return (
                  <motion.button
                    key={cat}
                    onClick={() => setSelectedCategory(cat)}
                    initial={{ opacity: 0, y: 8 }}
                    animate={{ opacity: 1, y: 0 }}
                    whileHover={{ y: -4 }}
                    className={`relative rounded-xl overflow-hidden border transition-all group cursor-pointer h-32 md:h-40 ${
                      dark
                        ? "border-white/10 hover:border-white/30 bg-black/20"
                        : "border-black/10 hover:border-black/30 bg-white/20"
                    }`}
                  >
                    {/* Category Image */}
                    <img
                      src={CATEGORY_IMAGES[cat]?.[0] || FALLBACK_IMAGE}
                      alt={cat}
                      className="w-full h-full object-cover"
                      loading="lazy"
                      decoding="async"
                      onError={(e) => {
                        (e.target as HTMLImageElement).src = FALLBACK_IMAGE;
                      }}
                    />
                    {/* Overlay Gradient */}
                    <div className={`absolute inset-0 ${dark ? "bg-gradient-to-t from-black/80 via-black/20 to-transparent" : "bg-gradient-to-t from-black/60 via-black/20 to-transparent"}`} />
                    
                    {/* Text */}
                    <div className="absolute inset-0 flex flex-col items-center justify-end p-3">
                      <h3 className={`text-sm md:text-base font-semibold ${dark ? "text-white" : "text-white"}`}>{cat}</h3>
                      <p className={`text-xs ${dark ? "text-white/60" : "text-white/70"}`}>{categoryCount} objects</p>
                    </div>
                  </motion.button>
                );
              })}
            </div>
          </div>
        )}

        {/* Active Category Header */}
        {selectedCategory && (
          <div className="mb-6">
            <div className="flex items-center justify-between mb-4">
              <div>
                <h2 className={`text-2xl font-bold ${textPrimary}`}>{selectedCategory}</h2>
                <p className={`text-sm ${textMuted} mt-1`}>{filtered.length} cosmic objects found</p>
              </div>
              <button
                onClick={() => setSelectedCategory(null)}
                className={`px-4 py-2 rounded-lg border text-sm font-medium transition-all ${btnOutline}`}
              >
                View All Categories
              </button>
            </div>
            
            {/* Search Bar */}
            <div className={`relative rounded-lg border transition-all ${inputBg}`}>
              <Search className={`absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 ${dark ? "text-white/40" : "text-black/40"}`} />
              <input
                type="text"
                placeholder="Search in this category..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className={`w-full pl-12 pr-4 py-3 bg-transparent outline-none text-sm`}
              />
              {search && (
                <button
                  onClick={() => setSearch("")}
                  className={`absolute right-4 top-1/2 -translate-y-1/2 transition-colors ${dark ? "hover:text-white/60" : "hover:text-black/60"}`}
                >
                  <X className="w-4 h-4" />
                </button>
              )}
            </div>
          </div>
        )}

        {/* Results grid - show when category is selected */}
        {selectedCategory && (
          <>
            {paginated.length === 0 ? (
              <div className="flex flex-col items-center justify-center py-24 text-center">
                <p className={`text-base font-medium ${textPrimary}`}>No objects found</p>
                <p className={`mt-1 text-sm ${textMuted}`}>Try adjusting your search or filters</p>
                <button
                  onClick={() => { setSearch(""); setSelectedCategory(null); }}
                  className={`mt-4 text-sm underline ${textMuted}`}
                >
                  Clear all filters
                </button>
              </div>
            ) : (
              <>
                {/* Cards — shift right when panel is open */}
                <div className={`grid gap-3 sm:grid-cols-2 lg:grid-cols-3 transition-all duration-300 ${activeObject ? "lg:pr-[440px]" : ""}`}>
                  {paginated.map((obj, i) => (
                    <ObjectCard
                      key={obj.id}
                      obj={obj}
                      index={i}
                      dark={dark}
                      selected={activeObject?.id === obj.id}
                      onClick={() => handleCardClick(obj)}
                    />
                  ))}
                </div>

                {/* Pagination */}
                {totalPages > 1 && (
                  <div className={`mt-8 flex items-center justify-center gap-3 transition-all duration-300 ${activeObject ? "lg:pr-[440px]" : ""}`}>
                    <button
                      onClick={() => handlePageChange(Math.max(0, page - 1))}
                      disabled={page === 0}
                      className={`flex items-center gap-1.5 px-4 py-2 rounded-lg border text-sm font-medium transition-all disabled:opacity-30 ${btnOutline}`}
                    >
                      <ChevronLeft className="w-4 h-4" />
                      Prev
                    </button>
                    <span className={`text-sm ${textMuted}`}>
                      {page + 1} / {totalPages}
                    </span>
                    <button
                      onClick={() => handlePageChange(Math.min(totalPages - 1, page + 1))}
                      disabled={page >= totalPages - 1}
                      className={`flex items-center gap-1.5 px-4 py-2 rounded-lg border text-sm font-medium transition-all disabled:opacity-30 ${btnOutline}`}
                    >
                      Next
                      <ChevronRight className="w-4 h-4" />
                    </button>
                  </div>
                )}
              </>
            )}
          </>
        )}
      </div>

      {/* Overlay on mobile when panel is open */}
      <AnimatePresence>
        {activeObject && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 z-40 bg-black/40 sm:hidden"
              onClick={() => setActiveObject(null)}
            />
            <ImagePanel obj={activeObject} onClose={() => setActiveObject(null)} dark={dark} currentPage={page} />
          </>
        )}
      </AnimatePresence>
    </div>
  );
}