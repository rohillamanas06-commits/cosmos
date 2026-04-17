import { jsx, jsxs, Fragment } from "react/jsx-runtime";
import { useNavigate, Link } from "@tanstack/react-router";
import { useState, useCallback, useEffect, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowLeft, Search, X, ChevronLeft, ChevronRight, ExternalLink } from "lucide-react";
import { l as loadCosmicData, C as CATEGORIES, g as getCategoryBadgeClass } from "./cosmic-data-CMjh5_z9.js";
import { R as Route } from "./router-C9fNgZ5H.js";
const PAGE_SIZE = 24;
const CATEGORY_IMAGES = {
  "Galaxy": ["/taneli-lahtinen-3G8p__Lv8iM-unsplash.jpg", "/Whirlpool Galaxy (M51a).jpg", "/Cartwheel Galaxy.jpg", "/Centaurus A (NGC 5128).jpg", "/Cigar Galaxy (M82).jpg", "/Messier 87 (M87).jpg", "/milky way galaxy.jpg", "/Pinwheel Galaxy (M101).jpg", "/Sculptor Galaxy (NGC 253).jpg", "/Triangulum galaxy.jpg", "/Small Magellanic Cloud (SMC).jpg", "/Sombrero Galaxy (M104).jpg", "/Large Magellanic Cloud (LMC).jpg"],
  "Black Hole": ["/primordial black hole.jpg", "/Cygnus X-1.jpg", "/M87 (Virgo A Black Hole).jpg", "/M87.jpg", "/Sagittarius A.jpg", "/TON 618.jpg", "/NGC 1277 Black Hole.jpg", "/M82 X-1.jpg", "/AT2019qiz — Tidal Disruption Event.jpg", "/GW150914 — First Gravitational Wave Event.jpg", "/GW170817 — Neutron Star Merge.jpg"],
  "Nebula": ["/aldebaran-s-qtRF_RxCAo0-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Crab_Nebula.jpg/600px-Crab_Nebula.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/NGC_604.jpg/600px-NGC_604.jpg"],
  "Star": ["/ivana-cajina-IwK0lkENPKY-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/600px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Sirius_A_and_B_Hubble_Photo_-_annotated.full.jpg/600px-Sirius_A_and_B_Hubble_Photo_-_annotated.full.jpg"],
  "Pulsar": ["/nasa-hubble-space-telescope-e_VUMccLu-k-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Crab_Nebula.jpg/600px-Crab_Nebula.jpg"],
  "Quasar": ["/nasa-hubble-space-telescope-gbw_PRLvhJA-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/600px-Hubble_ultra_deep_field.jpg"],
  "Supernova Remnant": ["/tengyart-Q78W18T-dss-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_nebula_original.jpg/600px-Crab_nebula_original.jpg"],
  "Exoplanet": ["/nasa-hubble-space-telescope-hdDjmN0iraw-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Exoplanet_Comparison_WASP-17b.png/600px-Exoplanet_Comparison_WASP-17b.png"],
  "Galaxy Cluster": ["/nasa-hubble-space-telescope-tcgaCmVyueY-unsplash.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/600px-Hubble_ultra_deep_field.jpg"],
  "Brown Dwarf": ["/brown dwarf.jpg"],
  "Moon": ["/moon.jpg"],
  "Neutron Star": ["/neutron star.jpg"],
  "Planet": ["/planet.jpg"],
  "Cosmic String": ["/cosmic string.jpg"],
  "Dark Matter Structure": ["/dark matter.jpg"],
  "Gamma-Ray Burst": ["/gamma ray.jpg"],
  "Primordial Black Hole": ["/primordial black hole.jpg"],
  "Axion Star": ["/axion star.jpg"],
  "Fast Radio Burst": ["/radio burst.jpg"],
  "Variable Star": ["/variable star.jpg"],
  "Blazar": ["/blazer.jpg"],
  "Space Mission": ["/space mission.jpg"],
  "Ring Galaxy": ["/ring galaxies.jpg"],
  "Interacting Galaxies": ["/interacting glaxies.jpg"],
  "X-ray Source": ["/xray source.jpg"],
  "Star Cluster": ["/star cluster.jpg"],
  "Dwarf Planet": ["/dwarf planet.jpg"],
  "Planetary Nebula": ["/planetery nebula.jpg"],
  "Dark Nebula": ["/dark nebula.jpg"],
  "Protoplanetary Nebula": ["/protoplanetry nebula.jpg"],
  "Cosmic Structure": ["/cosmic structure.jpg"],
  "Cosmological Structure": ["/cosmological structure.jpg"],
  "Edge-Case Phenomenon": ["/edge class phenomenon.jpg"],
  "Hypothetical Discovery": ["/hypothetical discovery.jpg"],
  "Simulated Object": ["/simulated object.jpg"],
  "Interstellar Object": ["/interstellar object.jpg"]
};
const FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/600px-Hubble_ultra_deep_field.jpg";
const GALAXY_NAME_MAP = {
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
  "Small Magellanic Cloud": "/Small Magellanic Cloud (SMC).jpg"
};
const PULSAR_NAME_MAP = {
  "PSR J1748-2446ad": "/PSR J1748-2446ad.jpg"
};
const NEBULA_NAME_MAP = {
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
  "NGC 2440 — The Colorful Nebula": "/NGC 2440 — The Colorful Nebula.jpg"
};
const QUASAR_NAME_MAP = {
  "3C 273": "/3C 273.jpg",
  "PKS 2126-158": "/PKS 2126-158.jpg",
  "Quasar J0313-1806": "/Quasar J0313-1806.jpg",
  "S5 0014+81": "/S5 0014+81.jpg"
};
const EXOPLANET_NAME_MAP = {
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
  "WASP-39b": "/WASP-39b.jpg"
};
const SUPERNOVA_NAME_MAP = {
  "SN 1987A": "/SN 1987A.jpg",
  "Crab Nebula (M1, NGC 1952)": "/Crab Nebula (M1, NGC 1952).jpg",
  "Tycho Supernova Remnant — SNR B1572+0449": "/Tycho Supernova Remnant — SNR B1572+0449.jpg"
};
const GALAXY_CLUSTER_NAME_MAP = {
  "El Gordo (ACT-CL J0102-4915)": "/El Gordo (ACT-CL J0102-4915).jpg",
  "Bullet Cluster (1E 0657-56)": "/Bullet Cluster (1E 0657-56).jpg"
};
const PLANET_NAME_MAP = {
  "Mercury": "/mercury.jpg",
  "Venus": "/venus.jpg",
  "Earth": "/earth.jpg",
  "Mars": "/mars.jpg",
  "Jupiter": "/jupiter.jpg",
  "Saturn": "/saturn.jpg",
  "Uranus": "/uranus.jpg",
  "Neptune": "/neptune.jpg"
};
const MOON_NAME_MAP = {
  "Titan": "/titan.jpg",
  "Europa": "/europa.jpg",
  "Io": "/io.jpg",
  "Enceladus": "/Enceladus.jpg",
  "Ganymede": "/Ganymede.jpg"
};
const STAR_NAME_MAP = {
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
  "US 708": "/US 708.jpg"
};
const BLACK_HOLE_NAME_MAP = {
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
  "GW170817 — Neutron Star Merger": "/GW170817 — Neutron Star Merge.jpg"
};
function getImageForObject(obj) {
  const cat = obj.category;
  if (cat === "Galaxy") {
    if (GALAXY_NAME_MAP[obj.name]) {
      return GALAXY_NAME_MAP[obj.name];
    }
    for (const [key, value] of Object.entries(GALAXY_NAME_MAP)) {
      if (obj.name.toLowerCase().includes(key.toLowerCase())) {
        return value;
      }
    }
  }
  if (cat === "Black Hole") {
    if (BLACK_HOLE_NAME_MAP[obj.name]) {
      return BLACK_HOLE_NAME_MAP[obj.name];
    }
  }
  if (cat === "Pulsar") {
    if (PULSAR_NAME_MAP[obj.name]) {
      return PULSAR_NAME_MAP[obj.name];
    }
  }
  if (cat === "Nebula") {
    if (NEBULA_NAME_MAP[obj.name]) {
      return NEBULA_NAME_MAP[obj.name];
    }
  }
  if (cat === "Quasar") {
    if (QUASAR_NAME_MAP[obj.name]) {
      return QUASAR_NAME_MAP[obj.name];
    }
  }
  if (cat === "Exoplanet") {
    if (EXOPLANET_NAME_MAP[obj.name]) {
      return EXOPLANET_NAME_MAP[obj.name];
    }
  }
  if (cat === "Supernova" || cat === "Supernova Remnant") {
    if (SUPERNOVA_NAME_MAP[obj.name]) {
      return SUPERNOVA_NAME_MAP[obj.name];
    }
  }
  if (cat === "Galaxy Cluster") {
    if (GALAXY_CLUSTER_NAME_MAP[obj.name]) {
      return GALAXY_CLUSTER_NAME_MAP[obj.name];
    }
  }
  if (cat === "Planet") {
    if (PLANET_NAME_MAP[obj.name]) {
      return PLANET_NAME_MAP[obj.name];
    }
  }
  if (cat === "Moon") {
    if (MOON_NAME_MAP[obj.name]) {
      return MOON_NAME_MAP[obj.name];
    }
  }
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
function formatValue(val) {
  if (val === null || val === void 0) return "—";
  if (typeof val === "object" && !Array.isArray(val)) {
    const parts = [];
    if (val.value !== void 0) parts.push(String(val.value));
    if (val.unit) parts.push(val.unit);
    if (val.note) parts.push(`(${val.note})`);
    return parts.join(" ") || JSON.stringify(val);
  }
  if (Array.isArray(val)) return val.join(", ");
  return String(val);
}
function ImagePanel({
  obj,
  onClose,
  dark,
  currentPage,
  category
}) {
  const imageUrl = getImageForObject(obj);
  return /* @__PURE__ */ jsxs(motion.div, { initial: {
    x: "100%",
    opacity: 0
  }, animate: {
    x: 0,
    opacity: 1
  }, exit: {
    x: "100%",
    opacity: 0
  }, transition: {
    type: "spring",
    stiffness: 300,
    damping: 30
  }, className: `fixed top-0 right-0 h-full w-full sm:w-[420px] z-50 flex flex-col shadow-2xl border-l ${dark ? "bg-[#0a0a0a] border-white/10 text-white" : "bg-white border-black/10 text-black"}`, children: [
    /* @__PURE__ */ jsxs("div", { className: `flex items-center justify-between px-5 py-4 border-b ${dark ? "border-white/10" : "border-black/10"}`, children: [
      /* @__PURE__ */ jsx("div", { className: "flex items-center gap-2", children: /* @__PURE__ */ jsx("span", { className: `text-xs font-semibold uppercase tracking-widest ${dark ? "text-white/40" : "text-black/40"}`, children: "Object Detail" }) }),
      /* @__PURE__ */ jsx("button", { onClick: onClose, className: `p-1.5 rounded-md transition-colors ${dark ? "hover:bg-white/10 text-white/60 hover:text-white" : "hover:bg-black/5 text-black/40 hover:text-black"}`, children: /* @__PURE__ */ jsx(X, { className: "w-4 h-4" }) })
    ] }),
    /* @__PURE__ */ jsxs("div", { className: "flex-1 overflow-y-auto", children: [
      /* @__PURE__ */ jsxs("div", { className: "relative w-full aspect-video bg-black/20 overflow-hidden", children: [
        /* @__PURE__ */ jsx("img", { src: imageUrl, alt: obj.name, className: "w-full h-full object-cover", onError: (e) => {
          e.target.src = FALLBACK_IMAGE;
        } }),
        /* @__PURE__ */ jsx("div", { className: "absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" })
      ] }),
      /* @__PURE__ */ jsxs("div", { className: "px-5 py-5 space-y-5", children: [
        /* @__PURE__ */ jsxs("div", { children: [
          /* @__PURE__ */ jsx("h2", { className: "text-xl font-bold tracking-tight", children: obj.name }),
          obj.subtype && /* @__PURE__ */ jsx("p", { className: `text-sm mt-0.5 ${dark ? "text-white/50" : "text-black/50"}`, children: obj.subtype })
        ] }),
        obj.detailed_description && /* @__PURE__ */ jsx("p", { className: `text-sm leading-relaxed ${dark ? "text-white/70" : "text-black/70"}`, children: obj.detailed_description }),
        obj.physical && Object.keys(obj.physical).length > 0 && /* @__PURE__ */ jsxs("div", { children: [
          /* @__PURE__ */ jsx("h3", { className: `text-xs font-semibold uppercase tracking-widest mb-2 ${dark ? "text-white/40" : "text-black/40"}`, children: "Physical Properties" }),
          /* @__PURE__ */ jsx("div", { className: `rounded-lg overflow-hidden border ${dark ? "border-white/10" : "border-black/10"}`, children: Object.entries(obj.physical).slice(0, 5).map(([key, val], i) => /* @__PURE__ */ jsxs("div", { className: `flex justify-between items-start px-3 py-2 text-sm ${i % 2 === 0 ? dark ? "bg-white/5" : "bg-black/3" : ""}`, children: [
            /* @__PURE__ */ jsx("span", { className: `capitalize ${dark ? "text-white/50" : "text-black/50"}`, children: key.replace(/_/g, " ") }),
            /* @__PURE__ */ jsx("span", { className: `font-mono text-xs text-right max-w-[55%] ${dark ? "text-white/80" : "text-black/80"}`, children: formatValue(val) })
          ] }, key)) })
        ] }),
        obj.scientific_facts && obj.scientific_facts.length > 0 && /* @__PURE__ */ jsxs("div", { children: [
          /* @__PURE__ */ jsx("h3", { className: `text-xs font-semibold uppercase tracking-widest mb-2 ${dark ? "text-white/40" : "text-black/40"}`, children: "Key Facts" }),
          /* @__PURE__ */ jsx("ul", { className: "space-y-1.5", children: obj.scientific_facts.slice(0, 4).map((fact, i) => /* @__PURE__ */ jsxs("li", { className: `flex gap-2 text-sm ${dark ? "text-white/65" : "text-black/65"}`, children: [
            /* @__PURE__ */ jsx("span", { className: `mt-1.5 w-1 h-1 rounded-full flex-shrink-0 ${dark ? "bg-white/40" : "bg-black/30"}` }),
            fact
          ] }, i)) })
        ] })
      ] })
    ] }),
    /* @__PURE__ */ jsx("div", { className: `px-5 py-4 border-t ${dark ? "border-white/10" : "border-black/10"}`, children: /* @__PURE__ */ jsxs(Link, { to: "/explore/$objectId", params: {
      objectId: obj.id
    }, search: {
      page: currentPage,
      category: category || null
    }, className: `flex items-center justify-center gap-2 w-full py-2.5 rounded-lg text-sm font-medium transition-colors ${dark ? "bg-white text-black hover:bg-white/90" : "bg-black text-white hover:bg-black/90"}`, children: [
      "View Full Details",
      /* @__PURE__ */ jsx(ExternalLink, { className: "w-3.5 h-3.5" })
    ] }) })
  ] });
}
function ObjectCard({
  obj,
  index,
  dark,
  selected,
  onClick
}) {
  const imageUrl = getImageForObject(obj);
  return /* @__PURE__ */ jsxs(motion.div, { initial: {
    opacity: 0,
    y: 8
  }, animate: {
    opacity: 1,
    y: 0
  }, transition: {
    duration: 0.2,
    delay: Math.min(index * 0.02, 0.3)
  }, onClick, className: `group cursor-pointer rounded-xl border overflow-hidden transition-all duration-150 flex flex-col ${selected ? dark ? "border-white/40 bg-white/8" : "border-black/30 bg-black/5" : dark ? "border-white/8 bg-white/3 hover:border-white/20 hover:bg-white/6" : "border-black/8 bg-black/2 hover:border-black/20 hover:bg-black/4"}`, children: [
    /* @__PURE__ */ jsxs("div", { className: "relative w-full aspect-video bg-gradient-to-br from-gray-700 to-gray-900 overflow-hidden", children: [
      /* @__PURE__ */ jsx("img", { src: imageUrl, alt: obj.name, className: "w-full h-full object-cover", loading: "lazy", decoding: "async", onError: (e) => {
        e.target.src = FALLBACK_IMAGE;
      } }),
      /* @__PURE__ */ jsx("div", { className: "absolute inset-0 bg-gradient-to-b from-transparent to-black/40" })
    ] }),
    /* @__PURE__ */ jsxs("div", { className: "px-4 py-3 flex-1 flex flex-col justify-between", children: [
      /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsx("h3", { className: `font-semibold text-sm tracking-tight ${dark ? "text-white" : "text-black"}`, children: obj.name }),
        obj.subtype && /* @__PURE__ */ jsx("p", { className: `text-xs mt-1 ${dark ? "text-white/45" : "text-black/45"}`, children: obj.subtype })
      ] }),
      /* @__PURE__ */ jsx("div", { className: "mt-3", children: /* @__PURE__ */ jsx("span", { className: `inline-block text-xs font-medium px-2.5 py-0.5 rounded-full border ${getCategoryBadgeClass(obj.category)}`, children: obj.category }) })
    ] })
  ] });
}
function ExplorePage() {
  const {
    page: initialPage,
    category: initialCategory
  } = Route.useSearch();
  const navigate = useNavigate({
    from: "/explore/"
  });
  const [objects, setObjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState(initialCategory);
  const [showFilters, setShowFilters] = useState(false);
  const [page, setPage] = useState(initialPage);
  const [dark, setDark] = useState(true);
  const [activeObject, setActiveObject] = useState(null);
  const handlePageChange = useCallback((newPage) => {
    setPage(newPage);
    navigate({
      search: {
        page: newPage,
        category: selectedCategory
      }
    });
  }, [navigate, selectedCategory]);
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
      result = result.filter((o) => o.name.toLowerCase().includes(q) || o.category.toLowerCase().includes(q));
    }
    if (selectedCategory) result = result.filter((o) => o.category === selectedCategory);
    return result;
  }, [objects, search, selectedCategory]);
  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginated = filtered.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);
  useEffect(() => {
    handlePageChange(0);
  }, [search, selectedCategory, handlePageChange]);
  const activeCategories = useMemo(() => {
    const cats = new Set(objects.map((o) => o.category));
    return CATEGORIES.filter((c) => cats.has(c));
  }, [objects]);
  const handleCardClick = useCallback((obj) => {
    setActiveObject((prev) => prev?.id === obj.id ? null : obj);
  }, []);
  const bg = dark ? "bg-[#080808]" : "bg-[#f9f9f7]";
  const textPrimary = dark ? "text-white" : "text-black";
  const textMuted = dark ? "text-white/50" : "text-black/50";
  const borderColor = dark ? "border-white/10" : "border-black/10";
  const headerBg = dark ? "bg-[#080808]/90" : "bg-[#f9f9f7]/90";
  const inputBg = dark ? "bg-white/5 border-white/10 text-white placeholder:text-white/35 focus:border-white/30" : "bg-black/3 border-black/10 text-black placeholder:text-black/35 focus:border-black/30";
  const btnOutline = dark ? "border-white/15 hover:border-white/30 text-white/70 hover:text-white" : "border-black/15 hover:border-black/30 text-black/70 hover:text-black";
  if (loading) {
    return /* @__PURE__ */ jsx("div", { className: `flex min-h-screen items-center justify-center ${bg}`, children: /* @__PURE__ */ jsxs("div", { className: "text-center", children: [
      /* @__PURE__ */ jsx("div", { className: `mx-auto h-8 w-8 animate-spin rounded-full border-2 ${dark ? "border-white/20 border-t-white" : "border-black/20 border-t-black"}` }),
      /* @__PURE__ */ jsx("p", { className: `mt-4 text-sm ${textMuted}`, children: "Loading cosmic data..." })
    ] }) });
  }
  return /* @__PURE__ */ jsxs("div", { className: `min-h-screen ${bg} transition-colors duration-200`, children: [
    /* @__PURE__ */ jsx("header", { className: `sticky top-0 z-40 border-b ${borderColor} ${headerBg} backdrop-blur-xl`, children: /* @__PURE__ */ jsxs("div", { className: "mx-auto flex max-w-screen-xl items-center justify-between px-4 md:px-8 h-14", children: [
      /* @__PURE__ */ jsx("div", { className: "flex items-center gap-6", children: selectedCategory ? /* @__PURE__ */ jsxs("button", { onClick: () => setSelectedCategory(null), className: `flex items-center gap-2 ${textPrimary} hover:${textMuted} transition-colors text-sm font-medium`, children: [
        /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
        "Back to Explorer"
      ] }) : /* @__PURE__ */ jsxs(Link, { to: "/", className: `flex items-center gap-2 ${textPrimary} hover:${textMuted} transition-colors text-sm font-medium`, children: [
        /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
        "Back to Home"
      ] }) }),
      /* @__PURE__ */ jsx("div", { className: "flex items-center gap-2" })
    ] }) }),
    /* @__PURE__ */ jsxs("div", { className: "mx-auto max-w-screen-xl px-4 md:px-8 py-7", children: [
      !selectedCategory && /* @__PURE__ */ jsxs("div", { className: "mb-10", children: [
        /* @__PURE__ */ jsxs("div", { className: "mb-4", children: [
          /* @__PURE__ */ jsx("h2", { className: `text-2xl font-bold ${textPrimary}`, children: "What would you like to explore?" }),
          /* @__PURE__ */ jsx("p", { className: `text-sm ${textMuted} mt-1`, children: "Browse by category or search for specific objects" })
        ] }),
        /* @__PURE__ */ jsx("div", { className: "grid grid-cols-3 gap-3", children: activeCategories.map((cat) => {
          const categoryCount = objects.filter((o) => o.category === cat).length;
          return /* @__PURE__ */ jsxs(motion.button, { onClick: () => setSelectedCategory(cat), initial: {
            opacity: 0,
            y: 8
          }, animate: {
            opacity: 1,
            y: 0
          }, whileHover: {
            y: -4
          }, className: `relative rounded-xl overflow-hidden border transition-all group cursor-pointer h-40 md:h-46 ${dark ? "border-white/10 hover:border-white/30 bg-black/20" : "border-black/10 hover:border-black/30 bg-white/20"}`, children: [
            /* @__PURE__ */ jsx("img", { src: CATEGORY_IMAGES[cat]?.[0] || FALLBACK_IMAGE, alt: cat, className: "w-full h-full object-cover", loading: "lazy", decoding: "async", onError: (e) => {
              e.target.src = FALLBACK_IMAGE;
            } }),
            /* @__PURE__ */ jsx("div", { className: `absolute inset-0 ${dark ? "bg-gradient-to-t from-black/80 via-black/20 to-transparent" : "bg-gradient-to-t from-black/60 via-black/20 to-transparent"}` }),
            /* @__PURE__ */ jsxs("div", { className: "absolute inset-0 flex flex-col items-center justify-end p-3", children: [
              /* @__PURE__ */ jsx("h3", { className: `text-sm md:text-base font-semibold ${dark ? "text-white" : "text-white"}`, children: cat }),
              /* @__PURE__ */ jsxs("p", { className: `text-xs ${dark ? "text-white/60" : "text-white/70"}`, children: [
                categoryCount,
                " objects"
              ] })
            ] })
          ] }, cat);
        }) })
      ] }),
      selectedCategory && /* @__PURE__ */ jsxs("div", { className: "mb-6", children: [
        /* @__PURE__ */ jsxs("div", { className: "mb-4", children: [
          /* @__PURE__ */ jsx("h2", { className: `text-2xl font-bold ${textPrimary}`, children: selectedCategory }),
          /* @__PURE__ */ jsxs("p", { className: `text-sm ${textMuted} mt-1`, children: [
            filtered.length,
            " cosmic objects found"
          ] })
        ] }),
        /* @__PURE__ */ jsxs("div", { className: `relative rounded-lg border transition-all ${inputBg}`, children: [
          /* @__PURE__ */ jsx(Search, { className: `absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 ${dark ? "text-white/40" : "text-black/40"}` }),
          /* @__PURE__ */ jsx("input", { type: "text", placeholder: "Search in this category...", value: search, onChange: (e) => setSearch(e.target.value), className: `w-full pl-12 pr-4 py-3 bg-transparent outline-none text-sm` }),
          search && /* @__PURE__ */ jsx("button", { onClick: () => setSearch(""), className: `absolute right-4 top-1/2 -translate-y-1/2 transition-colors ${dark ? "hover:text-white/60" : "hover:text-black/60"}`, children: /* @__PURE__ */ jsx(X, { className: "w-4 h-4" }) })
        ] })
      ] }),
      selectedCategory && /* @__PURE__ */ jsx(Fragment, { children: paginated.length === 0 ? /* @__PURE__ */ jsxs("div", { className: "flex flex-col items-center justify-center py-24 text-center", children: [
        /* @__PURE__ */ jsx("p", { className: `text-base font-medium ${textPrimary}`, children: "No objects found" }),
        /* @__PURE__ */ jsx("p", { className: `mt-1 text-sm ${textMuted}`, children: "Try adjusting your search or filters" }),
        /* @__PURE__ */ jsx("button", { onClick: () => {
          setSearch("");
          setSelectedCategory(null);
        }, className: `mt-4 text-sm underline ${textMuted}`, children: "Clear all filters" })
      ] }) : /* @__PURE__ */ jsxs(Fragment, { children: [
        /* @__PURE__ */ jsx("div", { className: `grid gap-3 sm:grid-cols-2 lg:grid-cols-3 transition-all duration-300 ${activeObject ? "lg:pr-[440px]" : ""}`, children: paginated.map((obj, i) => /* @__PURE__ */ jsx(ObjectCard, { obj, index: i, dark, selected: activeObject?.id === obj.id, onClick: () => handleCardClick(obj) }, obj.id)) }),
        totalPages > 1 && /* @__PURE__ */ jsxs("div", { className: `mt-8 flex items-center justify-center gap-3 transition-all duration-300 ${activeObject ? "lg:pr-[440px]" : ""}`, children: [
          /* @__PURE__ */ jsxs("button", { onClick: () => handlePageChange(Math.max(0, page - 1)), disabled: page === 0, className: `flex items-center gap-1.5 px-4 py-2 rounded-lg border text-sm font-medium transition-all disabled:opacity-30 ${btnOutline}`, children: [
            /* @__PURE__ */ jsx(ChevronLeft, { className: "w-4 h-4" }),
            "Prev"
          ] }),
          /* @__PURE__ */ jsxs("span", { className: `text-sm ${textMuted}`, children: [
            page + 1,
            " / ",
            totalPages
          ] }),
          /* @__PURE__ */ jsxs("button", { onClick: () => handlePageChange(Math.min(totalPages - 1, page + 1)), disabled: page >= totalPages - 1, className: `flex items-center gap-1.5 px-4 py-2 rounded-lg border text-sm font-medium transition-all disabled:opacity-30 ${btnOutline}`, children: [
            "Next",
            /* @__PURE__ */ jsx(ChevronRight, { className: "w-4 h-4" })
          ] })
        ] })
      ] }) })
    ] }),
    /* @__PURE__ */ jsx(AnimatePresence, { children: activeObject && /* @__PURE__ */ jsxs(Fragment, { children: [
      /* @__PURE__ */ jsx(motion.div, { initial: {
        opacity: 0
      }, animate: {
        opacity: 1
      }, exit: {
        opacity: 0
      }, className: "fixed inset-0 z-40 bg-black/40 sm:hidden", onClick: () => setActiveObject(null) }),
      /* @__PURE__ */ jsx(ImagePanel, { obj: activeObject, onClose: () => setActiveObject(null), dark, currentPage: page, category: selectedCategory })
    ] }) })
  ] });
}
export {
  ExplorePage as component
};
