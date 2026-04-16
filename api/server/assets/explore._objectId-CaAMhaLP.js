import { jsx, jsxs } from "react/jsx-runtime";
import { Link } from "@tanstack/react-router";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ArrowLeft, ExternalLink } from "lucide-react";
import { a as loadCosmicObjectById } from "./cosmic-data-CMjh5_z9.js";
import { a as Route } from "./router-C9fNgZ5H.js";
const CATEGORY_IMAGES = {
  "Galaxy": ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg"],
  "Black Hole": ["/Cygnus X-1.jpg", "/M87 (Virgo A Black Hole).jpg", "/M87.jpg", "/Sagittarius A.jpg", "/TON 618.jpg", "/NGC 1277 Black Hole.jpg", "/M82 X-1.jpg", "/AT2019qiz — Tidal Disruption Event.jpg", "/GW150914 — First Gravitational Wave Event.jpg", "/GW170817 — Neutron Star Merge.jpg"],
  "Nebula": ["https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Crab_Nebula.jpg/1200px-Crab_Nebula.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/NGC_604.jpg/1200px-NGC_604.jpg"],
  "Star": ["https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/1200px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg"],
  "Pulsar": ["https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Crab_Nebula.jpg/1200px-Crab_Nebula.jpg"],
  "Quasar": ["https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg"],
  "Supernova": ["https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_nebula_original.jpg/1200px-Crab_nebula_original.jpg"],
  "Exoplanet": ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Exoplanet_Comparison_WASP-17b.png/1200px-Exoplanet_Comparison_WASP-17b.png"],
  "Galaxy Cluster": ["https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg"]
};
const FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hubble_ultra_deep_field.jpg/1200px-Hubble_ultra_deep_field.jpg";
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
    if (val.value !== void 0) {
      parts.push(typeof val.value === "number" ? val.value.toLocaleString() : String(val.value));
    }
    if (val.unit) parts.push(val.unit);
    if (val.note) parts.push(`(${val.note})`);
    if (val.range) parts.push(`[${val.range}]`);
    if (parts.length > 0) return parts.join(" ");
    return Object.entries(val).map(([k, v]) => `${k}: ${formatValue(v)}`).join(", ");
  }
  if (Array.isArray(val)) return val.join(", ");
  return String(val);
}
function ObjectDetailPage() {
  const {
    objectId
  } = Route.useParams();
  const {
    page,
    category
  } = Route.useSearch();
  const [obj, setObj] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    document.documentElement.classList.add("dark");
    loadCosmicObjectById(objectId).then((foundObj) => {
      setObj(foundObj);
      setLoading(false);
    });
  }, [objectId]);
  if (loading) {
    return /* @__PURE__ */ jsx("div", { className: "flex min-h-screen items-center justify-center bg-black/90", children: /* @__PURE__ */ jsx("div", { className: "h-12 w-12 animate-spin rounded-full border-4 border-white/20 border-t-white" }) });
  }
  if (!obj) {
    return /* @__PURE__ */ jsxs("div", { className: "flex min-h-screen flex-col items-center justify-center bg-background", children: [
      /* @__PURE__ */ jsx("h1", { className: "font-display text-2xl font-bold text-foreground", children: "Object not found" }),
      /* @__PURE__ */ jsx(Link, { to: "/explore", search: {
        page,
        ...category && {
          category
        }
      }, className: "mt-4 text-primary hover:underline", children: "Back to explorer" })
    ] });
  }
  return /* @__PURE__ */ jsxs("div", { className: "min-h-screen bg-background", children: [
    /* @__PURE__ */ jsx("header", { className: "sticky top-0 z-40 border-b border-white/10 bg-[#080808]/90 backdrop-blur-xl", children: /* @__PURE__ */ jsx("div", { className: "mx-auto flex max-w-screen-xl items-center justify-between px-4 md:px-8 h-14", children: /* @__PURE__ */ jsxs(Link, { to: "/explore", search: {
      page,
      ...category && {
        category
      }
    }, className: "flex items-center gap-2 text-white hover:text-white/50 transition-colors text-sm font-medium", children: [
      /* @__PURE__ */ jsx(ArrowLeft, { className: "h-4 w-4" }),
      "Back to ",
      category ? category : "Explorer"
    ] }) }) }),
    /* @__PURE__ */ jsx("div", { className: "mx-auto max-w-screen-xl px-4 md:px-8 py-8", children: /* @__PURE__ */ jsxs(motion.div, { initial: {
      opacity: 0,
      y: 20
    }, animate: {
      opacity: 1,
      y: 0
    }, transition: {
      duration: 0.4
    }, children: [
      /* @__PURE__ */ jsx("div", { className: "mb-8 rounded-2xl border border-white/10 bg-gradient-to-r from-white/5 to-transparent p-8 md:p-10", children: /* @__PURE__ */ jsxs("div", { className: "flex flex-col md:flex-row gap-8 items-center md:items-start", children: [
        /* @__PURE__ */ jsx("div", { className: "flex-1", children: /* @__PURE__ */ jsxs("div", { className: "space-y-2", children: [
          /* @__PURE__ */ jsx("h1", { className: "font-display text-3xl md:text-4xl font-bold text-white leading-tight", children: obj.name }),
          obj.subtype && /* @__PURE__ */ jsx("p", { className: "text-sm md:text-base text-white/60 font-light", children: obj.subtype })
        ] }) }),
        /* @__PURE__ */ jsx("div", { className: "w-64 h-64 flex-shrink-0 md:w-72 md:h-72", children: /* @__PURE__ */ jsxs("div", { className: "relative w-full h-full rounded-2xl overflow-hidden border border-white/20 bg-black/40 shadow-2xl", children: [
          /* @__PURE__ */ jsx("img", { src: getImageForObject(obj), alt: obj.name, className: "w-full h-full object-cover", onError: (e) => {
            e.target.src = FALLBACK_IMAGE;
          } }),
          /* @__PURE__ */ jsx("div", { className: "absolute inset-0 bg-gradient-to-t from-black/30 to-transparent" })
        ] }) })
      ] }) }),
      obj.detailed_description && /* @__PURE__ */ jsx(Section, { title: "Description", children: /* @__PURE__ */ jsx("p", { className: "text-white/70 leading-relaxed", children: obj.detailed_description }) }),
      /* @__PURE__ */ jsxs("div", { className: "grid gap-6 md:grid-cols-2 mt-6", children: [
        obj.physical && Object.keys(obj.physical).length > 0 && /* @__PURE__ */ jsx(Section, { title: "Physical Properties", children: /* @__PURE__ */ jsx(DataTable, { data: obj.physical }) }),
        obj.spatial && Object.keys(obj.spatial).length > 0 && /* @__PURE__ */ jsx(Section, { title: "Spatial Data", children: /* @__PURE__ */ jsx(DataTable, { data: obj.spatial }) })
      ] }),
      obj.scientific_facts && obj.scientific_facts.length > 0 && /* @__PURE__ */ jsx(Section, { title: "Scientific Facts", className: "mt-6", children: /* @__PURE__ */ jsx("ul", { className: "space-y-2", children: obj.scientific_facts.map((fact, i) => /* @__PURE__ */ jsxs("li", { className: "flex gap-2 text-sm text-white/70", children: [
        /* @__PURE__ */ jsx("span", { className: "shrink-0 mt-1 h-1.5 w-1.5 rounded-full bg-white/30" }),
        fact
      ] }, i)) }) }),
      obj.did_you_know && obj.did_you_know.length > 0 && /* @__PURE__ */ jsx(Section, { title: "Did You Know?", className: "mt-6", children: /* @__PURE__ */ jsx("ul", { className: "space-y-2", children: obj.did_you_know.map((fact, i) => /* @__PURE__ */ jsxs("li", { className: "flex gap-2 text-sm text-white/70", children: [
        /* @__PURE__ */ jsx("span", { className: "shrink-0 mt-1 text-white/60", children: "💡" }),
        fact
      ] }, i)) }) }),
      obj.formation_process && /* @__PURE__ */ jsx(Section, { title: "Formation Process", className: "mt-6", children: /* @__PURE__ */ jsx("p", { className: "text-white/70 leading-relaxed text-sm", children: obj.formation_process }) }),
      obj.future_evolution && /* @__PURE__ */ jsx(Section, { title: "Future Evolution", className: "mt-6", children: /* @__PURE__ */ jsx("p", { className: "text-white/70 leading-relaxed text-sm", children: obj.future_evolution }) }),
      obj.related_objects && obj.related_objects.length > 0 && /* @__PURE__ */ jsx(Section, { title: "Related Objects", className: "mt-6", children: /* @__PURE__ */ jsx("div", { className: "flex flex-wrap gap-2", children: obj.related_objects.map((r) => /* @__PURE__ */ jsx("span", { className: "rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-white/60", children: r }, r)) }) }),
      obj.nasa_reference && /* @__PURE__ */ jsx("div", { className: "mt-8 text-center", children: /* @__PURE__ */ jsxs("a", { href: obj.nasa_reference, target: "_blank", rel: "noopener noreferrer", className: "inline-flex items-center gap-2 text-sm text-white/60 hover:underline", children: [
        /* @__PURE__ */ jsx(ExternalLink, { className: "h-4 w-4" }),
        "View NASA Reference"
      ] }) })
    ] }) })
  ] });
}
function Section({
  icon: Icon,
  title,
  children,
  className = ""
}) {
  return /* @__PURE__ */ jsxs("div", { className: `rounded-xl border border-white/10 bg-white/5 p-5 ${className}`, children: [
    /* @__PURE__ */ jsxs("div", { className: "flex items-center gap-2 mb-3", children: [
      Icon && /* @__PURE__ */ jsx(Icon, { className: "h-4 w-4 text-white/60" }),
      /* @__PURE__ */ jsx("h2", { className: "font-display text-sm font-semibold text-white/90 uppercase tracking-wider", children: title })
    ] }),
    children
  ] });
}
function DataTable({
  data
}) {
  return /* @__PURE__ */ jsx("div", { className: "space-y-2", children: Object.entries(data).map(([key, value]) => /* @__PURE__ */ jsxs("div", { className: "flex justify-between gap-4 text-sm border-b border-white/8 pb-1.5 last:border-0", children: [
    /* @__PURE__ */ jsx("span", { className: "text-white/50 capitalize", children: key.replace(/_/g, " ") }),
    /* @__PURE__ */ jsx("span", { className: "text-white/70 text-right font-mono text-xs max-w-[60%] break-words", children: formatValue(value) })
  ] }, key)) });
}
export {
  ObjectDetailPage as component
};
