# -------------------------------------------------------------------------
# PHASE 1
# -------------------------------------------------------------------------

import uuid

COSMIC_OBJECTS_PHASE1 = [

    # -------------------------------------------------------------------------
    # SECTION 1: GALAXIES & LOCAL GROUP STRUCTURES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "milky-way-galaxy")),
        "name": "Milky Way Galaxy",
        "category": "Galaxy",
        "subtype": "Barred Spiral Galaxy (SBbc)",
        "tags": ["galaxy", "home-galaxy", "spiral", "barred", "local-group", "foundational"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 0, "unit": "ly", "note": "We are inside it"},
            "coordinates": {"ra": "17h 45m 40s", "dec": "-29° 00' 28\""},
            "galaxy_reference": "self",
            "diameter": {"value": 105700, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1.5e12, "unit": "solar_masses", "note": "Including dark matter halo"},
            "radius": {"value": 52850, "unit": "ly"},
            "age": {"value": 13.61e9, "unit": "years"},
            "stellar_population": {"value": 2e11, "unit": "stars", "range": "100–400 billion"},
            "central_black_hole": "Sagittarius A*",
            "rotation_speed": {"value": 220, "unit": "km/s", "note": "At Sun's orbital radius"},
            "dark_matter_fraction": "~85% of total mass",
        },
        "detailed_description": (
            "The Milky Way is a barred spiral galaxy roughly 105,700 light-years in diameter, "
            "home to an estimated 100–400 billion stars and at least as many planets. Our solar "
            "system sits in the Orion Arm, a minor spiral arm located about 26,000 light-years "
            "from the galactic center. The galaxy's most prominent structural features are four "
            "major spiral arms — Perseus, Norma, Scutum-Centaurus, and Sagittarius — wrapped "
            "around a central bar-shaped bulge of older, redder stars. At the very core sits "
            "Sagittarius A*, a supermassive black hole with a mass of roughly 4 million solar "
            "masses. The galaxy is embedded in a vast, roughly spherical dark matter halo that "
            "extends well beyond the visible disk and accounts for ~85% of its total gravitational "
            "mass. The Milky Way is part of the Local Group, a gravitationally bound collection of "
            "more than 50 galaxies dominated by the Milky Way and Andromeda. It is currently on a "
            "collision course with the Andromeda Galaxy, expected to merge in approximately 4.5 "
            "billion years — an event that will reshape both galaxies into a single elliptical or "
            "lenticular galaxy, sometimes called 'Milkomeda' or 'Milkdromeda'."
        ),
        "scientific_facts": [
            "The galactic bar at the center is ~27,000 light-years long and rotates as a rigid body.",
            "The Milky Way completes one full rotation every ~225–250 million years — called a 'Galactic Year'.",
            "There are an estimated 17 billion Earth-sized planets in the Milky Way alone.",
            "The galaxy contains over 150 known globular clusters, ancient spherical star systems orbiting the core.",
            "The Fermi Bubbles — two giant plasma lobes extending ~25,000 ly above and below the core — are likely remnants of a past AGN outburst.",
            "The galaxy's thin disk is ~1,000 light-years thick; the thick disk extends ~3,500 light-years.",
            "Sagittarius A* is unusually quiet for a supermassive black hole — it has brief flaring episodes but is not an active galactic nucleus.",
            "Stars in the outer halo of the Milky Way are the oldest known, some dating to ~13.5 billion years.",
            "The Magellanic Clouds (Large and Small) are irregular dwarf galaxies currently being tidally disrupted and absorbed by the Milky Way.",
            "Hypervelocity stars — ejected by gravitational interactions near Sgr A* — travel at over 1,000 km/s and can escape the galaxy.",
            "The Milky Way's dark matter halo may extend up to 1 million light-years from the galactic center.",
        ],
        "did_you_know": [
            "You can see roughly 0.000003% of the Milky Way's stars with the naked eye on a clear night.",
            "The name 'Milky Way' comes from Greek 'galaxias kyklos' (milky circle), referring to its appearance as a band of light.",
            "The galaxy is warped and twisted — its outer disk is not flat but flares upward on one side, likely from past interactions with dwarf galaxies.",
            "If the Sun were the size of a grain of sand, the Milky Way would be ~10 km wide.",
        ],
        "formation_process": (
            "The Milky Way formed approximately 13.6 billion years ago from the collapse of a primordial "
            "hydrogen and helium gas cloud in the early universe. The first structures to condense were "
            "the central bulge and halo population II stars. Over billions of years, subsequent mergers "
            "with smaller protogalaxies and continued accretion of gas from cosmic filaments built up "
            "the disk. The bar structure formed as disk stars settled into resonant orbits. Several "
            "significant merger events are recorded in stellar kinematics — notably the Gaia-Enceladus "
            "merger ~10 billion years ago, which contributed a large fraction of the inner halo population."
        ),
        "future_evolution": (
            "In ~4.5 billion years, the Milky Way will begin its merger with the Andromeda Galaxy. "
            "The collision will be a slow gravitational dance lasting ~2 billion years, during which "
            "star-forming bursts will ignite across both systems. The Sun is unlikely to be directly "
            "hit by another star due to interstellar distances, but its orbit will be dramatically altered. "
            "The merged remnant will likely be a giant elliptical galaxy with minimal ongoing star formation."
        ),
        "related_objects": ["Sagittarius A*", "Andromeda Galaxy", "Large Magellanic Cloud", "Small Magellanic Cloud", "Orion Nebula", "Sun"],
        "parent_system": "Local Group",
        "child_objects": ["Sagittarius A*", "Orion Arm", "Perseus Arm", "Globular Clusters (150+)"],
        "nasa_reference": "https://science.nasa.gov/resource/the-milky-way-galaxy/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sagittarius-a-star")),
        "name": "Sagittarius A*",
        "category": "Black Hole",
        "subtype": "Supermassive Black Hole",
        "tags": ["black-hole", "galactic-center", "supermassive", "sgr-a", "milky-way"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 26673, "unit": "ly"},
            "coordinates": {"ra": "17h 45m 40.04s", "dec": "-29° 00' 28.2\""},
            "galaxy_reference": "Milky Way",
            "location": "Galactic Center, Sagittarius constellation",
        },
        "physical": {
            "mass": {"value": 4.154e6, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 12.4e6, "unit": "km", "note": "~0.08 AU"},
            "angular_diameter_observed": {"value": 51.8, "unit": "microarcseconds"},
            "spin": {"note": "Moderately spinning; exact dimensionless spin parameter uncertain, estimated ~0.1–0.9"},
        },
        "detailed_description": (
            "Sagittarius A* (Sgr A*) is the supermassive black hole anchoring the gravitational center "
            "of the Milky Way, located approximately 26,673 light-years from Earth in the direction of "
            "the Sagittarius constellation. With a mass of approximately 4.154 million solar masses, its "
            "event horizon — the point of no return — has a Schwarzschild radius of about 12.4 million "
            "kilometers, roughly 17 times the radius of the Sun. Despite its immense gravity, Sgr A* is "
            "remarkably quiescent compared to active galactic nuclei in other galaxies. It undergoes "
            "brief X-ray and infrared flares lasting minutes to hours, driven by magnetic reconnection "
            "events near the event horizon. In May 2022, the Event Horizon Telescope (EHT) collaboration "
            "released the first direct image of Sgr A*, showing the characteristic bright ring of "
            "photons orbiting the black hole's shadow — a region about 52 microarcseconds across. "
            "The S-stars — a cluster of young, massive stars in extremely tight orbits around Sgr A* — "
            "have provided the most precise measurements of the black hole's mass and distance. S2, the "
            "most observed of these, completes an orbit in just 16 years and reaches periapsis at "
            "~120 AU from the singularity, achieving ~2.9% the speed of light at closest approach."
        ),
        "scientific_facts": [
            "The first direct image of Sgr A* was released by the Event Horizon Telescope in May 2022.",
            "S2 star's orbit around Sgr A* provided the first direct evidence of general relativistic precession at a galactic center.",
            "Sgr A* accretes matter at an extremely low rate — ~10^-9 solar masses per year — making it one of the least luminous supermassive BHs relative to its mass.",
            "Its radio emission was discovered by Karl Jansky in 1932, though its true nature wasn't understood until decades later.",
            "The name 'A*' comes from radio astronomy notation; the asterisk was added by Bruce Balick and Robert Brown who formally identified it.",
            "Sgr A* shows quasi-periodic oscillations in its near-infrared flares roughly consistent with orbital periods at the innermost stable circular orbit.",
            "G2, a gas-and-dust cloud, passed within 3,000 AU of Sgr A* in 2014 without being fully disrupted — its exact nature remains debated.",
            "The black hole's event horizon subtends about the same angular size as a grapefruit on the Moon as seen from Earth.",
            "Measuring Sgr A* helped redefine the International Astronomical Union's definition of the Galactic Coordinate System.",
            "Relativistic precession of S2's orbit confirmed the no-hair theorem prediction to within observational limits.",
        ],
        "did_you_know": [
            "Despite having 4 million solar masses, Sgr A* is roughly 1,500 times less massive than M87* (the first imaged black hole).",
            "The intense magnetic field near Sgr A* is estimated at ~1,000 gauss — millions of times Earth's field.",
            "Imaging Sgr A* was technically harder than imaging M87* because it scintillates (twinkles) far faster due to its smaller size.",
        ],
        "formation_process": (
            "Sgr A* likely formed through a combination of direct collapse of massive early stars in the galactic "
            "center and subsequent mergers with other black holes over billions of years. Some models favor a "
            "direct-collapse origin from a ~100,000 solar mass 'quasi-star' in the early universe. Repeated "
            "galaxy mergers and accretion events over cosmic time built up its current mass."
        ),
        "future_evolution": (
            "Sgr A* will continue to grow slowly through tidal disruption events and gas accretion. "
            "When the Milky Way merges with Andromeda, the two supermassive black holes (Sgr A* and "
            "Andromeda's M31*, ~100 million solar masses) will form a bound pair, spiral together via "
            "gravitational wave emission over millions of years, and eventually merge into a single, "
            "larger black hole — an event that would briefly make it one of the strongest gravitational "
            "wave sources observable across the universe."
        ),
        "related_objects": ["Milky Way Galaxy", "S2 Star", "G2 Cloud", "Fermi Bubbles", "M87*"],
        "parent_system": "Milky Way Galactic Center",
        "child_objects": ["S-star cluster", "Circumnuclear Disk"],
        "nasa_reference": "https://www.nasa.gov/image-article/nasas-chandra-sees-stellar-strings-near-milky-way-black-hole/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "triangulum-galaxy-m33")),
        "name": "Triangulum Galaxy (M33)",
        "category": "Galaxy",
        "subtype": "Spiral Galaxy (SA(s)cd)",
        "tags": ["galaxy", "spiral", "local-group", "Messier", "star-forming"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 2.73e6, "unit": "ly"},
            "coordinates": {"ra": "01h 33m 50.9s", "dec": "+30° 39' 37\""},
            "galaxy_reference": "Local Group",
            "diameter": {"value": 60000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 5e10, "unit": "solar_masses"},
            "stellar_population": {"value": 4e10, "unit": "stars"},
            "age": {"value": 10e9, "unit": "years"},
        },
        "detailed_description": (
            "The Triangulum Galaxy (M33) is the third-largest member of the Local Group, after the "
            "Milky Way and Andromeda. It is a pure spiral galaxy with no central bar and one of the "
            "most distant objects visible to the naked eye under perfect dark-sky conditions. Unlike "
            "its larger neighbors, M33 lacks a prominent central bulge and is actively forming stars "
            "at a prolific rate — its disk is studded with bright H II regions, including NGC 604, "
            "one of the largest and most luminous star-forming nebulae in the Local Group, roughly "
            "1,500 light-years across and 6,300 light-years from M33's nucleus. M33 may be a "
            "satellite of Andromeda or a free-floating member of the Local Group on its first "
            "close approach; simulations suggest it may have interacted with M31 in the past, "
            "contributing to tidal streams around both galaxies. The galaxy has no confirmed "
            "supermassive black hole — an upper limit of ~1,500 solar masses places this among "
            "the smallest central compact masses known in a spiral galaxy."
        ),
        "scientific_facts": [
            "NGC 604 in M33 is ~100x larger than the Orion Nebula and contains over 200 hot O-type stars.",
            "M33 has an upper limit for its central black hole of ~1,500 solar masses — some of the lowest known in any spiral.",
            "X-ray observations reveal dozens of high-mass X-ray binary systems actively accreting material.",
            "M33 is potentially interacting gravitationally with Andromeda — HI gas streams connect the two galaxies.",
            "It is one of only two spiral galaxies resolvable into individual stars by amateur telescopes (the other being Andromeda).",
            "The galaxy shows warping in its outer HI disk, consistent with tidal interaction with Andromeda.",
            "Cepheid variable star distances in M33 were key to establishing the extragalactic distance scale in the 20th century.",
            "M33 has an irregular, clumpy star formation pattern with no defined nuclear star cluster.",
            "Radio observations reveal a molecular gas reservoir feeding ongoing star formation at ~0.5 solar masses per year.",
            "The galaxy's total HI gas mass (~1.4 billion solar masses) is comparable to its total stellar mass.",
        ],
        "did_you_know": [
            "M33 is sometimes called the 'Pinwheel Galaxy', though this name is also used for M101.",
            "Under pristine dark skies, M33 is the most distant object visible to the unaided human eye at 2.73 million light-years.",
            "The galaxy rotates once every ~250 million years at its outer edge.",
        ],
        "related_objects": ["Andromeda Galaxy", "Milky Way", "NGC 604", "Local Group"],
        "parent_system": "Local Group",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-33/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "large-magellanic-cloud")),
        "name": "Large Magellanic Cloud (LMC)",
        "category": "Galaxy",
        "subtype": "Irregular Dwarf Galaxy (Magellanic Spiral)",
        "tags": ["galaxy", "dwarf", "irregular", "satellite", "milky-way", "local-group", "star-burst"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 163000, "unit": "ly"},
            "coordinates": {"ra": "05h 23m 34.5s", "dec": "-69° 45' 22\""},
            "galaxy_reference": "Local Group / Milky Way satellite",
            "diameter": {"value": 14000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1.38e11, "unit": "solar_masses"},
            "stellar_population": {"value": 3e10, "unit": "stars"},
            "central_black_hole": "None confirmed",
            "star_formation_rate": {"value": 0.2, "unit": "solar_masses/year"},
        },
        "detailed_description": (
            "The Large Magellanic Cloud is the Milky Way's largest satellite galaxy, visible as a "
            "detached piece of the Milky Way to observers in the Southern Hemisphere. Despite being "
            "classified as an irregular galaxy, it shows hints of a bar structure, leading some "
            "astronomers to classify it as a 'Magellanic spiral'. It is one of the most "
            "star-forming-active galaxies in the Local Group: the Tarantula Nebula (30 Doradus) at "
            "its heart is the most luminous star-forming region in the entire Local Group, packed "
            "with thousands of hot young stars including R136a1, one of the most massive known "
            "stars. The LMC is connected to the Small Magellanic Cloud and Milky Way by the "
            "Magellanic Stream — a ribbon of hydrogen gas ~150° long across the sky, tidally "
            "stripped over hundreds of millions of years of interaction. On February 24, 1987, the "
            "LMC hosted SN 1987A — the first naked-eye supernova since 1604 and the best-studied "
            "supernova in history. The LMC is currently in a relatively close pass of the Milky "
            "Way and simulations suggest it may complete only 1–2 more orbits before being absorbed."
        ),
        "scientific_facts": [
            "SN 1987A in the LMC was the closest supernova to Earth in 383 years, allowing neutrino detection from its core collapse.",
            "The Tarantula Nebula (30 Doradus) is so luminous that if placed at Orion Nebula's distance, it would cast shadows on Earth.",
            "R136a1, a star in the LMC, has a mass of ~200–315 solar masses — among the highest known.",
            "The Magellanic Stream extends ~150° across the sky and contains ~2×10⁸ solar masses of gas.",
            "The LMC contains over 60 globular clusters, numerous open clusters, and thousands of nebulae.",
            "The LMC orbits the Milky Way at ~370 km/s — faster than expected, suggesting it has more dark matter than previously thought.",
            "LMC's gravitational influence causes a measurable asymmetric wobble in the Milky Way's dark matter halo.",
            "A stellar bar runs through the LMC's optical center — it's a Magellanic-type irregular barred galaxy.",
            "The LMC will be absorbed by the Milky Way within a few billion years, triggering a starburst event.",
            "X-ray binary systems in the LMC were among the first extragalactic X-ray sources ever identified.",
        ],
        "did_you_know": [
            "The LMC was first documented in Europe after Magellan's circumnavigation (1519–1522), giving it its name.",
            "To Southern Hemisphere observers, the LMC and SMC appear as detached clouds of the Milky Way visible with the naked eye.",
            "SN 1987A's neutrino burst arrived 3 hours before the optical light — the first confirmed neutrino detection from a stellar collapse.",
        ],
        "related_objects": ["Small Magellanic Cloud", "Milky Way", "Tarantula Nebula", "SN 1987A", "Magellanic Stream"],
        "parent_system": "Milky Way Satellite System",
        "nasa_reference": "https://science.nasa.gov/resource/large-magellanic-cloud/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sombrero-galaxy-m104")),
        "name": "Sombrero Galaxy (M104)",
        "category": "Galaxy",
        "subtype": "Unbarred Spiral / SA+ring (sa)",
        "tags": ["galaxy", "spiral", "edge-on", "Messier", "dust-lane", "massive-halo"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 31.1e6, "unit": "ly"},
            "coordinates": {"ra": "12h 39m 59.4s", "dec": "-11° 37' 23\""},
            "galaxy_reference": "Virgo Cluster periphery",
            "diameter": {"value": 50000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 8e11, "unit": "solar_masses"},
            "central_black_hole": "~1 billion solar masses",
            "globular_clusters": {"value": 2000, "note": "One of the richest globular cluster systems known"},
        },
        "detailed_description": (
            "The Sombrero Galaxy (M104) is one of the most photographed galaxies in the sky, "
            "recognizable by its brilliant white core, prominent dust lane, and steeply inclined "
            "disk — resembling a Mexican sombrero hat when viewed nearly edge-on. It has a "
            "disproportionately massive bulge for a spiral galaxy, giving it a cross-classification "
            "between spiral and elliptical. At its core sits a supermassive black hole estimated at "
            "~1 billion solar masses, among the most massive in any relatively nearby galaxy. "
            "Its extended halo contains an astonishing ~2,000 globular clusters — roughly 10x "
            "the Milky Way's complement — suggesting M104 may have consumed multiple smaller galaxies. "
            "The dark dust lane encircling the disk is a site of active star formation and contains "
            "significant molecular gas. Spitzer Space Telescope infrared imaging revealed M104's "
            "disk to be far more complex than optical views suggest, with extended spiral structure "
            "hidden by the dominant bulge in visible light."
        ),
        "scientific_facts": [
            "M104's globular cluster system (~2,000) is one of the richest known for a galaxy its size.",
            "Its central black hole (~1 billion solar masses) is ~250x more massive than the Milky Way's Sgr A*.",
            "ROSAT and Chandra X-ray observations reveal hot gas filling M104's massive dark matter halo.",
            "The galaxy's HI gas disk extends significantly beyond its optical disk.",
            "M104 has an unusually high ratio of bulge-to-disk mass, approaching elliptical galaxy territory.",
            "Spitzer data shows two distinct disk components in M104: an inner ring and outer disk.",
            "Radial velocity measurements of globular clusters trace M104's dark matter distribution.",
            "The galaxy's recession velocity (~1,000 km/s) places it near but outside the main Virgo Cluster.",
            "M104 emits significantly in the mid-infrared, indicating warm dust heated by embedded star formation.",
            "Hubble imaging resolved thousands of individual red giant stars in M104's halo.",
        ],
        "did_you_know": [
            "The Sombrero was Pierre Méchain's discovery in 1781 but missed Messier's original catalog — it was added in 1921.",
            "In a 2004 poll of professional astronomers, M104 was voted the most photogenic galaxy.",
            "The brilliant white core contains a dense population of old, metal-rich stars packed into ~1/3 of its total radius.",
        ],
        "related_objects": ["Virgo Cluster", "M87", "Milky Way"],
        "parent_system": "Virgo Cluster region",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-104/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "whirlpool-galaxy-m51")),
        "name": "Whirlpool Galaxy (M51a)",
        "category": "Galaxy",
        "subtype": "Grand Design Spiral Galaxy (SA(s)bc)",
        "tags": ["galaxy", "spiral", "interacting", "Messier", "companion-galaxy", "grand-design"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 23e6, "unit": "ly"},
            "coordinates": {"ra": "13h 29m 52.7s", "dec": "+47° 11' 43\""},
            "galaxy_reference": "Canes Venatici",
            "diameter": {"value": 76000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1.6e11, "unit": "solar_masses"},
            "central_black_hole": "~1 million solar masses",
            "companion": "NGC 5195 (interacting dwarf galaxy)",
        },
        "detailed_description": (
            "The Whirlpool Galaxy (M51a) is a textbook example of a 'grand design' spiral galaxy — "
            "one with two tightly wound, clearly defined spiral arms visible from Earth nearly "
            "face-on. Its exquisitely symmetric structure is maintained and enhanced by a gravitational "
            "interaction with its smaller companion NGC 5195 (M51b), which appears to be passing "
            "behind M51a from our perspective. The tidal forces from this encounter have amplified "
            "M51a's spiral density waves, triggering prolific star formation throughout the disk. "
            "M51 was the first galaxy in which spiral structure was detected — Irish astronomer "
            "Lord Rosse identified it through his 72-inch 'Leviathan' telescope in 1845. "
            "Chandra X-ray observations in 2020 identified a candidate exoplanet in M51 transiting "
            "an X-ray binary — the first exoplanet candidate detected outside the Milky Way, "
            "though confirmation remains challenging."
        ),
        "scientific_facts": [
            "M51 was the first galaxy where spiral structure was discovered, by Lord Rosse in 1845.",
            "Its companion NGC 5195 appears connected to M51a by a visible tidal bridge of stars and gas.",
            "A 2020 Chandra X-ray study reported the first exoplanet candidate in an external galaxy, orbiting an X-ray binary in M51.",
            "M51's H II region population is one of the most extensively mapped outside the Local Group.",
            "Two supernovae have been observed in M51 in recent decades: SN 1994I and SN 2011dh.",
            "The tidal interaction with NGC 5195 has driven multiple starbursts in M51's disk over the last 300 million years.",
            "Molecular hydrogen (H₂) surveys show dense gas concentrations tracing M51's spiral arms.",
            "The galaxy's disk extends ~76,000 light-years — comparable to the Milky Way.",
            "M51's spiral arms host spectacular giant H II regions visible even through small telescopes.",
            "NGC 5195 shows a complex morphology indicating it is on its second post-merger pass through M51's disk.",
        ],
        "did_you_know": [
            "M51a and NGC 5195 together form one of the sky's most famous interacting galaxy pairs.",
            "The Whirlpool's spiral arms are visible even through modest backyard telescopes on a dark night.",
            "If the exoplanet candidate in M51 is confirmed, it would be the most distant known exoplanet at 23 million light-years.",
        ],
        "related_objects": ["NGC 5195", "Milky Way", "Andromeda Galaxy"],
        "parent_system": "Canes Venatici Group",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-51/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "centaurus-a-ngc5128")),
        "name": "Centaurus A (NGC 5128)",
        "category": "Galaxy",
        "subtype": "Radio Galaxy / Giant Elliptical with Dust Lane",
        "tags": ["galaxy", "elliptical", "radio-galaxy", "AGN", "relativistic-jet", "nearest-radio-galaxy"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 13e6, "unit": "ly"},
            "coordinates": {"ra": "13h 25m 27.6s", "dec": "-43° 01' 09\""},
            "galaxy_reference": "Centaurus A/M83 Group",
            "diameter": {"value": 97000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1e12, "unit": "solar_masses"},
            "central_black_hole": "~55 million solar masses",
            "jet_length": {"value": 13000, "unit": "ly"},
            "radio_lobe_extent": {"value": 1.35e6, "unit": "ly"},
        },
        "detailed_description": (
            "Centaurus A is the nearest radio galaxy to Earth and one of the brightest radio sources "
            "in the sky. It is a giant elliptical galaxy bisected by a prominent dark dust lane — "
            "the remnant of a spiral galaxy it absorbed roughly 200–700 million years ago. At its "
            "core, a supermassive black hole of ~55 million solar masses powers a pair of relativistic "
            "jets extending ~13,000 light-years in optical wavelengths and enormous radio lobes "
            "stretching over 1.35 million light-years — spanning 8° across the sky from Earth. "
            "The radio lobes make it the fifth brightest radio source in the sky. Cen A emits "
            "across the entire electromagnetic spectrum, including hard X-rays and gamma rays "
            "detected by Fermi LAT. The galaxy's active nucleus undergoes episodic jet activity, "
            "with multiple generations of radio lobes at different scales. High-energy cosmic rays "
            "above 60 EeV have been statistically correlated with the direction of Cen A, making "
            "it a candidate accelerator of ultra-high-energy cosmic rays."
        ),
        "scientific_facts": [
            "Cen A's radio lobes span ~1.35 million light-years — if visible to the eye, they would cover 8° of sky.",
            "The dust lane crossing Cen A is the remnant of a merged spiral galaxy.",
            "Fermi LAT gamma-ray observations confirm particle acceleration to GeV energies in Cen A's jets.",
            "At 13 million light-years, Cen A is ~4x closer than the next nearest radio galaxy.",
            "Ultra-high-energy cosmic rays detected by the Pierre Auger Observatory show anisotropy toward Cen A.",
            "Hubble imaging resolves individual stars, dust filaments, and star-forming regions in the merger debris.",
            "The central black hole (~55M solar masses) is accreting at a low Eddington rate, classifying it as a LINER AGN.",
            "Cen A has multiple generations of radio lobes: inner (~13 kly), middle, and outer giant lobes.",
            "Optical jets of ionized gas are co-aligned with the radio jet axis.",
            "Infrared observations trace star formation in the dust lane, triggered by the galaxy merger.",
        ],
        "did_you_know": [
            "Centaurus A was one of the first extragalactic radio sources ever detected — in 1949 by Bolton, Stanley, and Slee.",
            "Its radio lobes are so large that binoculars would show them spanning most of the Southern Cross's angular width.",
            "The merger that created its dust lane may have triggered the current AGN activity.",
        ],
        "related_objects": ["M87 Galaxy", "Virgo Cluster", "Radio Galaxies"],
        "parent_system": "Centaurus A/M83 Group",
        "nasa_reference": "https://www.nasa.gov/image-article/centaurus-a-galaxy/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "pinwheel-galaxy-m101")),
        "name": "Pinwheel Galaxy (M101)",
        "category": "Galaxy",
        "subtype": "Face-on Spiral Galaxy (SAB(rs)cd)",
        "tags": ["galaxy", "spiral", "face-on", "Messier", "star-forming", "asymmetric"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 21e6, "unit": "ly"},
            "coordinates": {"ra": "14h 03m 12.6s", "dec": "+54° 20' 57\""},
            "galaxy_reference": "Ursa Major",
            "diameter": {"value": 170000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1e11, "unit": "solar_masses"},
            "stellar_population": {"value": 1e12, "unit": "stars"},
        },
        "detailed_description": (
            "M101 is a large face-on spiral galaxy with a notably asymmetric structure — its nucleus "
            "is offset from the geometric center of its disk, and its spiral arms are of different "
            "extents and brightness. This lopsidedness is thought to result from past gravitational "
            "encounters with companion galaxies. At ~170,000 light-years in diameter, M101 is nearly "
            "twice the Milky Way's width, yet has only about half its mass — making it a low-density, "
            "gas-rich disk. Its spiral arms contain some of the largest known H II regions in the "
            "nearby universe, many visible individually in ground-based telescopes. Multiple supernovae "
            "have been observed in M101 in modern times, including the Type Ia SN 2011fe — one of the "
            "closest Type Ia supernovae in decades, which provided key calibration data for dark energy "
            "measurements. SN 2023ixf was another recent supernova in M101, discovered in May 2023."
        ),
        "scientific_facts": [
            "M101 is one of the largest spiral galaxies known in angular extent among nearby galaxies.",
            "SN 2011fe was a Type Ia supernova used to calibrate cosmological distance measurements.",
            "SN 2023ixf (discovered May 18, 2023) was the closest supernova in a decade, extensively observed.",
            "The galaxy's asymmetry is caused by gravitational interaction with satellite companions.",
            "M101 has a high rate of ongoing star formation distributed in massive star-forming complexes.",
            "HII region NGC 5461 in M101 is one of the largest single star-forming complexes known.",
            "Chandra X-ray observations detect hundreds of X-ray point sources in M101.",
            "Ultraviolet imaging shows M101's disk extends well beyond its optical boundary.",
            "The galaxy has at least 5 interacting companion galaxies shaping its disk asymmetry.",
            "Hubble variable star surveys in M101 have tracked dozens of Cepheids for distance calibration.",
        ],
        "did_you_know": [
            "M101 has appeared in over a dozen textbooks as a prototypical 'grand design' spiral.",
            "SN 2023ixf in M101 was so bright it was visible through amateur telescopes for months.",
            "The galaxy is ~2x larger in diameter than the Milky Way but with only half the stellar mass.",
        ],
        "related_objects": ["Milky Way", "Andromeda", "SN 2023ixf"],
        "parent_system": "M101 Group",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-101/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "virgo-a-m87")),
        "name": "Messier 87 (M87)",
        "category": "Galaxy",
        "subtype": "Giant Elliptical Galaxy (E0)",
        "tags": ["galaxy", "elliptical", "Virgo-Cluster", "AGN", "M87-star", "relativistic-jet", "cD-galaxy"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 55e6, "unit": "ly"},
            "coordinates": {"ra": "12h 30m 49.4s", "dec": "+12° 23' 28\""},
            "galaxy_reference": "Virgo Cluster",
            "diameter": {"value": 980000, "unit": "ly", "note": "Including stellar halo"},
        },
        "physical": {
            "mass": {"value": 2.4e12, "unit": "solar_masses"},
            "central_black_hole": "M87* — 6.5 billion solar masses",
            "globular_clusters": {"value": 15000, "note": "Most of any galaxy studied"},
            "satellite_galaxies": "~20 identified",
        },
        "detailed_description": (
            "Messier 87 is the dominant giant elliptical galaxy at the center of the Virgo Cluster — "
            "the nearest large galaxy cluster at ~55 million light-years. As a cD (brightest cluster) "
            "galaxy, M87 sits at the gravitational bottom of the Virgo Cluster's potential well and "
            "has accumulated mass through centuries of galaxy mergers. Its stellar halo extends "
            "nearly 1 million light-years, containing the relics of absorbed galaxies. The galaxy "
            "hosts the most globular clusters known in any galaxy (~15,000), compared to ~150 in "
            "the Milky Way. Most famously, M87 harbors the supermassive black hole M87* — imaged "
            "directly by the Event Horizon Telescope in 2019 — from which a 5,000 light-year "
            "relativistic jet erupts. The jet was first observed optically in 1918 by Heber Curtis. "
            "M87's X-ray luminosity reveals cavities in the hot intracluster medium inflated by "
            "repeated jet outbursts, demonstrating AGN feedback at work."
        ),
        "scientific_facts": [
            "M87 contains ~15,000 globular clusters — a signature of its prolific merger history.",
            "Its stellar halo extends ~980,000 light-years — nearly 1 million light-years across.",
            "Chandra X-ray images show bubbles and cavities in hot gas inflated by M87's jet outbursts.",
            "The relativistic jet carries energy at ~10⁴⁴ erg/s, balancing intracluster medium cooling.",
            "M87 is surrounded by a diffuse cloud of intracluster stars stripped from captured galaxies.",
            "The galaxy's velocity dispersion (~350 km/s) indicates an enormous stellar mass.",
            "VLA radio maps show M87's jet terminating in a bright radio lobe ~65 kly from the nucleus.",
            "VLBI observations of the jet base reveal superluminal motion of ~6c.",
            "M87's halo stellar population is dominated by old, metal-rich stars consistent with early-type assembly.",
            "Hundreds of ultra-compact dwarf galaxies orbit M87 — likely stripped nuclei of ancient dwarf galaxies.",
        ],
        "did_you_know": [
            "M87 would take 1 million light-years to cross from edge to edge — nearly as wide as the distance to the LMC.",
            "The black hole M87* is so massive that Mercury's entire orbit around the Sun would fit inside its event horizon.",
            "Every globular cluster you see in M87 images may contain hundreds of thousands of individual stars.",
        ],
        "related_objects": ["M87*", "Virgo Cluster", "Sagittarius A*", "Event Horizon Telescope"],
        "parent_system": "Virgo Cluster",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cartwheel-galaxy")),
        "name": "Cartwheel Galaxy",
        "category": "Galaxy",
        "subtype": "Ring Galaxy — Collision Remnant",
        "tags": ["galaxy", "ring-galaxy", "collision", "starburst", "JWST", "rare-morphology"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 500e6, "unit": "ly"},
            "coordinates": {"ra": "00h 37m 41.1s", "dec": "-33° 42' 59\""},
            "galaxy_reference": "Sculptor constellation",
            "diameter": {"value": 150000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 2.9e11, "unit": "solar_masses"},
            "ring_expansion_speed": {"value": 300, "unit": "km/s"},
            "star_formation_rate": {"value": 2.2, "unit": "solar_masses/year"},
        },
        "detailed_description": (
            "The Cartwheel Galaxy is a dramatic ring galaxy formed when a smaller galaxy plunged "
            "straight through the center of a larger spiral galaxy roughly 400 million years ago. "
            "The intruder's passage sent a radially expanding density wave through the disk — like "
            "a stone dropped in a pond — compressing gas and triggering a ring of intense star "
            "formation 150,000 light-years across. The outer ring expands at ~300 km/s and is rich "
            "in young blue stars and H II regions. JWST imaging in 2022 revealed the Cartwheel in "
            "unprecedented detail: spokes connecting the outer ring to the inner ring (remnant core), "
            "young star-forming clumps embedded in dust, and a complex interplay between the two "
            "rings. The galaxy also contains an unusually high number of ultraluminous X-ray sources "
            "(ULXs) — compact objects accreting mass at super-Eddington rates — and an active galactic "
            "nucleus in its compact central region."
        ),
        "scientific_facts": [
            "JWST's 2022 imaging resolved individual star-forming clumps in the Cartwheel's outer ring.",
            "The outer ring's expansion speed of ~300 km/s places the collision ~440 million years ago.",
            "Cartwheel contains an unusually high density of ultraluminous X-ray sources — among the highest known.",
            "Two 'spokes' of star-forming material connect the inner core to the outer ring.",
            "The intruder galaxy that caused the ring is one of two companion galaxies visible nearby.",
            "The galaxy was first cataloged as a peculiar ring morphology by Fritz Zwicky in 1941.",
            "Molecular gas surveys reveal shocks along the expanding ring where ISM is being compressed.",
            "The inner ring (core remnant) shows a different stellar population — older, redder stars.",
            "MIRI infrared imaging traced hydrocarbon-rich dust filaments connecting the two rings.",
            "The overall morphology will gradually settle into a normal spiral galaxy over ~1 billion years.",
        ],
        "did_you_know": [
            "The Cartwheel's ring of star formation is so bright it outshines most normal spiral galaxies.",
            "If you lived in the Cartwheel's outer ring, you would be surrounded by thousands of newly born star clusters.",
            "JWST revealed hot dust in the Cartwheel's outer ring invisible to Hubble's optical/UV cameras.",
        ],
        "related_objects": ["JWST", "Ring Galaxies", "Hoag's Object"],
        "parent_system": "Sculptor Galaxy Group",
        "nasa_reference": "https://www.nasa.gov/image-article/nasas-webb-captures-dying-star-final-performance-unprecedented-detail/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "small-magellanic-cloud")),
        "name": "Small Magellanic Cloud (SMC)",
        "category": "Galaxy",
        "subtype": "Irregular Dwarf Galaxy",
        "tags": ["galaxy", "dwarf", "irregular", "satellite", "milky-way", "local-group"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 200000, "unit": "ly"},
            "coordinates": {"ra": "00h 52m 44.8s", "dec": "-72° 49' 43\""},
            "galaxy_reference": "Local Group / Milky Way satellite",
            "diameter": {"value": 7000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 6.5e9, "unit": "solar_masses"},
            "stellar_population": {"value": 3e8, "unit": "stars"},
            "metallicity": {"note": "~0.2 solar — much lower than Milky Way, analogous to early universe galaxies"},
        },
        "detailed_description": (
            "The Small Magellanic Cloud is the Milky Way's second-largest satellite galaxy and the "
            "fourth-nearest galaxy to Earth. Despite its small size (~7,000 light-years), it is one "
            "of the most intensely studied galaxies because its low metallicity (~20% solar) makes "
            "it an analog for galaxies in the early universe — allowing astronomers to study stellar "
            "evolution and star formation physics in a chemically primitive environment. The SMC is "
            "gravitationally bound to the LMC and both are connected to the Milky Way by the "
            "Magellanic Stream. NGC 346, the brightest star-forming complex in the SMC, hosts over "
            "2,500 young stars including dozens of O-type stars. The SMC's low gravity means its "
            "structure is irregular and distorted by tidal forces from both the LMC and Milky Way. "
            "It is gradually being disrupted and will eventually be completely assimilated."
        ),
        "scientific_facts": [
            "The SMC's low metallicity (~20% solar) makes it a local laboratory for studying primordial-like star formation.",
            "Henrietta Swan Leavitt discovered the Cepheid period-luminosity relationship using SMC Cepheids in 1908.",
            "NGC 346 in the SMC hosts the densest concentration of O-type stars in the Local Group per unit volume.",
            "The SMC has a 'Wing' — a tidal extension pointing toward the LMC — indicating recent interaction.",
            "HI gas in the SMC extends much further than its stellar disk, connecting to the Magellanic Bridge to the LMC.",
            "Multiple distinct stellar populations in the SMC indicate episodic star formation over billions of years.",
            "The SMC lacks a clearly defined center — multiple stellar overdensities compete for the nuclear position.",
            "Proper motion measurements (Hubble + Gaia) show the SMC orbiting the LMC as much as the Milky Way.",
            "X-ray binaries in the SMC are disproportionately numerous, consistent with a young, active stellar population.",
            "SN 1987A occurred in the LMC but the SMC hosted a separate bright nova in 1990 (Nova SMC 1990#1).",
        ],
        "did_you_know": [
            "Henrietta Leavitt's discovery of Cepheid variables in the SMC unlocked the ability to measure cosmic distances.",
            "The SMC is so close that individual red giant stars can be resolved with Hubble.",
            "Despite being dwarfed by the Milky Way, the SMC is still forming stars at a significant rate.",
        ],
        "related_objects": ["Large Magellanic Cloud", "Milky Way", "NGC 346", "Magellanic Stream"],
        "parent_system": "Milky Way Satellite System",
        "nasa_reference": "https://science.nasa.gov/resource/small-magellanic-cloud/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sculptor-galaxy-ngc253")),
        "name": "Sculptor Galaxy (NGC 253)",
        "category": "Galaxy",
        "subtype": "Starburst Spiral Galaxy (SAB(s)c)",
        "tags": ["galaxy", "spiral", "starburst", "edge-on", "nearby", "superwind"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 11.4e6, "unit": "ly"},
            "coordinates": {"ra": "00h 47m 33.1s", "dec": "-25° 17' 18\""},
            "galaxy_reference": "Sculptor Galaxy Group",
            "diameter": {"value": 90000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 2e11, "unit": "solar_masses"},
            "star_formation_rate": {"value": 5, "unit": "solar_masses/year", "note": "~5x the Milky Way rate"},
        },
        "detailed_description": (
            "NGC 253, the Silver Dollar Galaxy, is one of the most actively star-forming spiral galaxies "
            "in the nearby universe and the brightest member of the Sculptor Galaxy Group. Viewed nearly "
            "edge-on from Earth, it reveals a dusty, clumpy disk lit by the combined light of billions "
            "of stars. At its center, a nuclear starburst is forming stars at a rate roughly 5x the "
            "Milky Way, powered by dense molecular gas being concentrated by bar-driven inflows. This "
            "intense star formation drives a powerful 'superwind' — a galactic-scale outflow of hot "
            "ionized gas extending tens of thousands of light-years above and below the disk. The "
            "superwind, detected in X-ray and Hα emission, carries heavy elements forged in the "
            "nuclear starburst into the galaxy's halo and potentially into the intergalactic medium. "
            "NGC 253 is the brightest galaxy in its group and a key target for studying starburst "
            "feedback and the enrichment of the circumgalactic medium."
        ),
        "scientific_facts": [
            "NGC 253's nuclear starburst region contains dozens of super star clusters within the inner 1,000 light-years.",
            "The galactic superwind reaches hundreds of km/s and extends ~30,000 light-years into the halo.",
            "ALMA molecular line observations reveal 14 GMCs (giant molecular clouds) in the central starburst zone.",
            "X-ray imaging shows hot shocked gas in the outflow at temperatures of ~10 million K.",
            "NGC 253 is the nearest starburst spiral — an ideal laboratory for starburst feedback physics.",
            "Star formation efficiencies in its nucleus approach the theoretical maximum for dense molecular gas.",
            "Several ultraluminous X-ray sources are detected in the starburst nucleus.",
            "JWST imaging resolved individual young star clusters embedded in dusty knots in the nuclear disk.",
            "The superwind is enriching the halo with silicon, iron, and oxygen from Type II supernovae.",
            "NGC 253 hosts a low-luminosity AGN at its core in addition to the dominant starburst activity.",
        ],
        "did_you_know": [
            "NGC 253 is sometimes called the 'Silver Dollar Galaxy' due to its elongated silvery appearance.",
            "It is one of the closest starburst galaxies — bright enough to be a showpiece even through small telescopes.",
            "The galactic outflow from NGC 253 moves fast enough to eventually escape the galaxy entirely.",
        ],
        "related_objects": ["LMC", "M82", "Sculptor Group"],
        "parent_system": "Sculptor Galaxy Group",
        "nasa_reference": "https://www.nasa.gov/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "messier-82-starburst")),
        "name": "Cigar Galaxy (M82)",
        "category": "Galaxy",
        "subtype": "Starburst Irregular Galaxy",
        "tags": ["galaxy", "starburst", "irregular", "Messier", "superwind", "tidal-interaction", "M81-group"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 12e6, "unit": "ly"},
            "coordinates": {"ra": "09h 55m 52.2s", "dec": "+69° 40' 47\""},
            "galaxy_reference": "M81 Group",
            "diameter": {"value": 37000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1e11, "unit": "solar_masses"},
            "star_formation_rate": {"value": 13, "unit": "solar_masses/year", "note": "~10x the Milky Way"},
            "superwind_outflow_speed": {"value": 600, "unit": "km/s"},
        },
        "detailed_description": (
            "M82, the Cigar Galaxy, is the archetypal starburst galaxy — the most intensely "
            "star-forming large galaxy in the nearby universe, forming stars at roughly 10x the "
            "Milky Way rate. Its extreme star formation was triggered by gravitational interaction "
            "with its larger neighbor M81, which passed close to M82 roughly 600 million years ago, "
            "funneling gas into M82's center and igniting the current starburst. The most visually "
            "dramatic feature of M82 is its galactic superwind: a bipolar outflow of hot gas, "
            "swept-up dust, and magnetic filaments erupting perpendicular to the disk at ~600 km/s "
            "and visible in Hα as glowing red filaments. M82 is the brightest infrared galaxy "
            "within 15 million light-years. In January 2014, M82 hosted SN 2014J — the nearest "
            "Type Ia supernova since SN 1987A and only the second to be detected in multiple "
            "wavelengths from radio to gamma-ray. The nuclear starburst contains hundreds of "
            "super star clusters each containing millions of stars."
        ),
        "scientific_facts": [
            "SN 2014J in M82 was the nearest Type Ia supernova in over 40 years, enabling exquisite multiwavelength study.",
            "The superwind in M82 extends ~10,000 ly above and below the disk and is visible through small telescopes in Hα.",
            "M82's interaction with M81 began ~600 million years ago, funneling gas to trigger the current starburst.",
            "M82 is ~5x brighter in infrared than optical wavelengths — most energy is reradiated by dust.",
            "Super star clusters in M82's nucleus contain up to 10⁶ stars in regions less than 10 pc across.",
            "Chandra detected M82 X-1 — a possible intermediate-mass black hole candidate (~200–5,000 solar masses).",
            "Radio continuum surveys trace the magnetic field of the superwind via synchrotron emission.",
            "M82 is the brightest radio galaxy at meter wavelengths within 15 Mpc.",
            "JWST near-IR imaging resolves the starburst nucleus and outflow filament structure in unprecedented detail.",
            "The galaxy's optical morphology — 'cigar shaped' — results from its edge-on orientation and dust obscuration.",
        ],
        "did_you_know": [
            "M82 was once thought to be exploding — astronomers initially misidentified its superwind as a galaxy-scale explosion.",
            "In a single year, M82 produces as many new stars as the Milky Way does in a decade.",
            "SN 2014J was discovered by a UK undergraduate student, Nick Howes, participating in a teaching observatory session.",
        ],
        "related_objects": ["M81", "M81 Group", "SN 2014J", "NGC 253"],
        "parent_system": "M81 Group",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-82/",
    },

    # -------------------------------------------------------------------------
    # SECTION 2: THE SUN & SOLAR SYSTEM STARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "the-sun")),
        "name": "The Sun",
        "category": "Star",
        "subtype": "Yellow Dwarf (G-type Main Sequence)",
        "tags": ["star", "solar-system", "G-type", "main-sequence", "foundational", "habitable-zone"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 1.0, "unit": "AU", "km": 1.496e8},
            "coordinates": {"ra": "varies (ecliptic)", "dec": "varies (ecliptic)"},
            "galaxy_reference": "Milky Way — Orion Arm",
            "galactic_distance_from_center": {"value": 26000, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1.989e30, "unit": "kg", "solar_masses": 1.0},
            "radius": {"value": 696340, "unit": "km", "solar_radii": 1.0},
            "density": {"value": 1408, "unit": "kg/m³"},
            "surface_temperature": {"value": 5778, "unit": "K"},
            "core_temperature": {"value": 15e6, "unit": "K"},
            "luminosity": {"value": 3.828e26, "unit": "W"},
            "age": {"value": 4.603e9, "unit": "years"},
            "spectral_class": "G2V",
            "rotation_period": {"equatorial": "25 days", "polar": "35 days", "note": "Differential rotation"},
            "composition": {"hydrogen": "73.46%", "helium": "24.85%", "oxygen": "0.77%", "other": "~1%"},
        },
        "detailed_description": (
            "The Sun is a G2V main-sequence star at the center of our solar system, containing 99.86% "
            "of the solar system's total mass. Energy is produced in its core by the proton-proton chain "
            "fusion reaction, which converts ~600 million tons of hydrogen into helium every second, "
            "releasing energy equivalent to 4 million tons of mass per second via E=mc². The Sun's "
            "interior is divided into distinct zones: the core (where fusion occurs out to ~25% of the "
            "radius), the radiative zone (where energy moves by photon diffusion over ~170,000 years), "
            "and the convective zone (the outer 30%, where plasma convects and drives the visible "
            "granulation pattern). Its visible surface, the photosphere, displays granules (~1,000 km "
            "wide convective cells), sunspots (cooler magnetic regions), and faculae (bright magnetic "
            "features). Above the photosphere lies the chromosphere and then the corona — the Sun's "
            "outermost atmosphere reaching millions of degrees, far hotter than the surface in a still "
            "not fully understood phenomenon. The corona continually streams outward as the solar wind, "
            "filling the entire heliosphere and interacting with every planet's magnetic field. The Sun "
            "drives Earth's climate, powers photosynthesis, and creates the auroras through its "
            "interaction with Earth's magnetosphere."
        ),
        "scientific_facts": [
            "A photon generated in the Sun's core takes between 10,000 and 170,000 years to reach the surface due to repeated absorption and re-emission.",
            "The Sun fuses ~620 million metric tons of hydrogen per second, converting ~4 million tons into energy (E=mc²).",
            "The solar corona reaches temperatures of 1–3 million K despite the photosphere being only 5,778 K — a paradox still under active research.",
            "Solar activity follows an ~11-year cycle driven by the winding and reversal of its internal magnetic field.",
            "The Sun will exhaust its hydrogen fuel in roughly 5 billion years and expand into a red giant, engulfing Mercury and Venus.",
            "The tachocline — the transition layer between radiative and convective zones — is thought to be the origin of the Sun's magnetic field via dynamo action.",
            "The fastest solar wind streams reach ~800 km/s at Earth's orbit.",
            "The Sun's equator rotates every 25 days; its poles take 35 days — differential rotation that winds up magnetic field lines over the solar cycle.",
            "Helioseismology (studying acoustic waves in the Sun) can map its internal structure like seismology maps Earth's interior.",
            "The Sun emits ~1.8 × 10⁹ kg of mass per second as solar wind — equivalent to losing one Earth-mass of material every 150 million years.",
            "Sunspot activity reached its lowest point in centuries during the Maunder Minimum (1645–1715), coinciding with the 'Little Ice Age' in Europe.",
        ],
        "did_you_know": [
            "Light from the Sun takes 8 minutes and 20 seconds to reach Earth.",
            "The Sun is large enough to fit 1.3 million Earths inside it by volume.",
            "Despite being 333,000 times more massive than Earth, the Sun's average density is only 1.4 g/cm³ — less than 3 times water.",
            "The Sun has already used about half its hydrogen fuel and is halfway through its main-sequence life.",
            "The Sun's gravity extends its influence over 2 light-years (the Oort Cloud), a region from which long-period comets originate.",
        ],
        "formation_process": (
            "The Sun formed approximately 4.603 billion years ago from the gravitational collapse of a "
            "dense region in a giant molecular cloud — likely triggered by the shockwave from a nearby "
            "supernova. As the proto-solar nebula collapsed, it spun faster (conservation of angular "
            "momentum), flattened into a disk, and concentrated mass at the center. When core pressure "
            "and temperature reached ~10 million K, hydrogen fusion ignited, halting collapse and "
            "establishing the Sun as a main-sequence star. The remaining disk material eventually formed "
            "the planets, moons, asteroids, and comets of the solar system."
        ),
        "future_evolution": (
            "In ~5 billion years, the Sun's core hydrogen will be exhausted. Hydrogen burning will shift "
            "to a shell around the helium core, causing the outer layers to expand dramatically — the Sun "
            "will become a red giant, growing to ~200 solar radii and possibly engulfing Mercury and Venus. "
            "Eventually helium fusion will ignite in the core (the helium flash), briefly stabilizing the "
            "star. After helium exhaustion, the Sun will shed its outer layers as a beautiful planetary "
            "nebula, leaving behind a hot, dense white dwarf ~50% the Sun's mass and roughly Earth's size."
        ),
        "related_objects": ["Earth", "Mercury", "Venus", "Mars", "Jupiter", "Oort Cloud", "Heliosphere", "Sagittarius A*"],
        "parent_system": "Solar System / Milky Way Orion Arm",
        "child_objects": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
        "nasa_reference": "https://solarsystem.nasa.gov/solar-system/sun/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "proxima-centauri-star")),
        "name": "Proxima Centauri",
        "category": "Star",
        "subtype": "Red Dwarf (M-type Main Sequence)",
        "tags": ["star", "red-dwarf", "nearest-star", "alpha-centauri-system", "flare-star", "M-dwarf"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 4.243, "unit": "ly"},
            "coordinates": {"ra": "14h 29m 42.5s", "dec": "-62° 40' 46.2\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "proper_motion": {"value": 3.77, "unit": "arcsec/year"},
        },
        "physical": {
            "mass": {"value": 0.123, "unit": "solar_masses"},
            "radius": {"value": 0.14, "unit": "solar_radii"},
            "luminosity": {"value": 0.0017, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 3042, "unit": "K"},
            "age": {"value": 4.85e9, "unit": "years", "note": "Estimated from kinematic age"},
            "spectral_class": "M5.5V",
            "rotation_period": {"value": 83.5, "unit": "days"},
            "magnetic_field": {"note": "Very active, complex topology"},
            "flare_activity": "High — flares up to X-ray luminosity 10³ times quiescent level",
        },
        "detailed_description": (
            "Proxima Centauri is the nearest known star to the Sun, located 4.243 light-years away in "
            "the constellation Centaurus. It is a red dwarf M5.5V spectral class star with a mass of "
            "only 12.3% of the Sun's mass, making it one of the lowest-mass main-sequence stars known. "
            "Despite its extreme proximity, Proxima is too faint to see with the naked eye (apparent "
            "magnitude 11.05). Proxima Centauri is part of the Alpha Centauri triple star system, "
            "bound gravitationally to the brighter binary Alpha Cen A and B at a distance of ~0.21 "
            "light-years. It is a flare star, meaning it undergoes sudden, energetic eruptions of "
            "radiation lasting minutes to hours, driven by magnetic reconnection events in its "
            "chromosphere. These flares can temporarily increase the star's brightness by factors of "
            "10–100. Proxima Centauri hosts at least three known exoplanets: Proxima Centauri b (an "
            "Earth-mass planet in the habitable zone), Proxima Centauri c (a super-Earth or mini-Neptune "
            "in a wider orbit), and Proxima Centauri d (a longer-period super-Earth candidate). The "
            "discovery of Proxima b in 2016 sparked intense interest in searching for biosignatures in "
            "its atmosphere via spectroscopy, though the star's frequent flares pose challenges to "
            "habitability. Proxima Centauri is moving toward the solar system and will reach its closest "
            "approach in ~26,700 years at a distance of 3.11 light-years."
        ),
        "scientific_facts": [
            "Proxima Centauri's small mass gives it a core temperature ~3.1 million K — lower than the Sun — allowing only slow proton-proton chain fusion.",
            "Its lifetime on the main sequence is estimated at ~4 trillion years — roughly 1,000× longer than the current age of the universe.",
            "Proxima's X-ray luminosity can reach 10⁻³ of the Sun's X-ray output during flares — intense for such a cool star.",
            "The discovery of Proxima b with a 11.186-day orbital period placed it in the habitable zone despite the star's low luminosity.",
            "Proxima Centauri's magnetic field may be global or multipolar — its exact geometry is uncertain.",
            "Radio observations reveal a large, complex radio chromosphere extending far from the stellar surface.",
            "The star's mass puts it near the hydrogen-burning limit; below ~0.08 solar masses, objects become sub-stellar brown dwarfs.",
            "Proxima's rotation period of 83.5 days is much longer than similarly-massed stars — possibly due to magnetic braking.",
            "No confirmed transit of Proxima b has been observed — its orbital orientation relative to Earth remains uncertain.",
        ],
        "did_you_know": [
            "If you could travel at the speed of light, it would take 4.243 years to reach Proxima Centauri from Earth.",
            "Proxima Centauri is moving toward Earth at ~22.2 km/s and will be the nearest star in ~26,700 years.",
            "Breakthrough Starshot initiative has proposed launching gram-scale probes toward Proxima Centauri, potentially arriving in ~20 years.",
        ],
        "formation_process": (
            "Proxima Centauri formed ~4.85 billion years ago from a giant molecular cloud in the Milky Way, "
            "likely in a birth cluster with other stars. It has since separated from its birth cluster and "
            "become bound to the Alpha Centauri AB system gravitationally."
        ),
        "future_evolution": (
            "Proxima Centauri will remain on the main sequence for trillions of years, very slowly fusing "
            "hydrogen. Eventually, in the extremely distant future, it will become a white dwarf. Its "
            "exoplanets will survive its red giant phase and continue orbiting the white dwarf remnant."
        ),
        "related_objects": ["Alpha Centauri A", "Alpha Centauri B", "Proxima Centauri b", "Alpha Centauri system"],
        "parent_system": "Alpha Centauri Triple System / Milky Way Local Neighborhood",
        "child_objects": ["Proxima Centauri b", "Proxima Centauri c", "Proxima Centauri d"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sirius-star")),
        "name": "Sirius (Alpha Canis Majoris)",
        "category": "Star",
        "subtype": "Binary — White Dwarf + A-type Main Sequence",
        "tags": ["star", "brightest-star", "binary-system", "white-dwarf", "dog-star", "sirius-a", "sirius-b"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 8.6, "unit": "ly"},
            "coordinates": {"ra": "06h 45m 08.9s", "dec": "-16° 42' 58.0\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "proper_motion": {"value": 0.546, "unit": "arcsec/year"},
            "apparent_magnitude": {"value": -1.46, "note": "Brightest star in Earth's night sky"},
        },
        "physical": {
            "sirius_a": {
                "mass": {"value": 2.02, "unit": "solar_masses"},
                "radius": {"value": 1.711, "unit": "solar_radii"},
                "luminosity": {"value": 25.4, "unit": "solar_luminosities"},
                "surface_temperature": {"value": 10150, "unit": "K"},
                "spectral_class": "A1V",
            },
            "sirius_b": {
                "mass": {"value": 1.02, "unit": "solar_masses"},
                "radius": {"value": 0.0084, "unit": "solar_radii", "note": "~Earth-sized"},
                "luminosity": {"value": 0.026, "unit": "solar_luminosities"},
                "surface_temperature": {"value": 25200, "unit": "K"},
                "spectral_class": "DA2",
                "type": "White Dwarf",
            },
            "orbital_period": {"value": 50.1, "unit": "years"},
            "separation": {"value": 19.8, "unit": "AU", "note": "Average distance"},
        },
        "detailed_description": (
            "Sirius is the brightest star visible in Earth's night sky with an apparent magnitude of -1.46, "
            "located 8.6 light-years away in the constellation Canis Major. It is a binary star system "
            "consisting of Sirius A, a main-sequence A1V star 2.02 solar masses with a surface temperature "
            "of 10,150 K, and Sirius B, a white dwarf remnant of ancient stellar evolution. Sirius A is bright "
            "and luminous, outshining its white dwarf companion by a factor of 10,000 despite the white dwarf's "
            "extreme surface temperature of 25,200 K. Sirius B is remarkably small and dense — just 0.0084 solar "
            "radii (roughly Earth-sized) but with 1.02 solar masses, packing the mass of an entire star into a "
            "volume comparable to Earth. This density makes Sirius B one of the most famous white dwarfs and a "
            "crucial testing ground for understanding degenerate matter physics. The two stars orbit their common "
            "center of mass with a period of 50.1 years at an average separation of 19.8 AU. The name 'Sirius' "
            "comes from the Greek word meaning 'brightest' and is sometimes called the 'Dog Star' because of its "
            "position in Canis Major. Ancient cultures held the rising and setting of Sirius in high regard; "
            "the heliacal rising of Sirius (when it becomes visible in the pre-dawn sky) was used by ancient "
            "Egyptians to predict the flooding of the Nile River."
        ),
        "scientific_facts": [
            "Sirius A rotates rapidly with a rotation period of ~16 hours, much faster than the Sun's 25 days.",
            "Sirius B was the first white dwarf ever discovered (by Alvan Clark in 1862), identified as an extraordinarily hot, dense companion.",
            "The density of Sirius B's matter is ~1 million times that of iron — a teaspoon would weigh ~5.5 metric tons on Earth.",
            "Sirius B's rotation period is estimated at ~26 hours based on indirect evidence from X-ray observations.",
            "X-ray observations show Sirius B has a thin hydrogen atmosphere over a mostly helium composition.",
            "Proper motion measurements reveal Sirius is approaching Earth at ~0.546 arcsec/year; it will be closest in ~60,000 years.",
            "The Sirius system is a member of the Sirius Moving Group — a kinematic association of young stars with similar ages and motions.",
            "Sirius A's excess infrared emission suggests it may have a circumstellar dust disk or debris.",
            "Detailed spectroscopy of Sirius A reveals it is metal-rich compared to the Sun.",
        ],
        "did_you_know": [
            "Sirius is so bright that it is sometimes visible in broad daylight under ideal conditions.",
            "Ancient Egyptian astronomers were aware of the 50-year orbital period of Sirius's binary orbit.",
            "Sirius B is cooling slowly — its surface temperature was hotter in the distant past and will continue to cool over trillions of years.",
        ],
        "formation_process": (
            "The Sirius system formed ~200–300 million years ago as two stars from the same natal cloud. "
            "The more massive star (now Sirius B) exhausted its fuel first and collapsed into a white dwarf. "
            "Sirius A, the secondary star by original mass, is still fusing hydrogen on the main sequence."
        ),
        "future_evolution": (
            "Sirius A will continue fusing hydrogen for ~1 billion more years. When it exhausts its hydrogen, "
            "it too will become a white dwarf. Eventually both white dwarfs will cool into black dwarfs over "
            "cosmic timescales. The two white dwarfs may eventually merge due to gravitational wave emission, "
            "possibly triggering a Type Ia thermonuclear supernovae explosion."
        ),
        "related_objects": ["Alpha Canis Majoris", "Sirius Moving Group", "White Dwarfs", "Procyon"],
        "parent_system": "Milky Way Local Neighborhood",
        "child_objects": ["Sirius A (primary)", "Sirius B (white dwarf companion)"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "alpha-centauri-a-star")),
        "name": "Alpha Centauri A (Rigil Kentaurus)",
        "category": "Star",
        "subtype": "G-type Main Sequence — Sun-like Star",
        "tags": ["star", "G-type", "main-sequence", "alpha-centauri-system", "sun-like", "nearest-bright-star"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 4.367, "unit": "ly"},
            "coordinates": {"ra": "14h 29m 43.0s", "dec": "-60° 50' 14.3\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "proper_motion": {"value": 3.71, "unit": "arcsec/year"},
        },
        "physical": {
            "mass": {"value": 1.0973, "unit": "solar_masses"},
            "radius": {"value": 1.2234, "unit": "solar_radii"},
            "luminosity": {"value": 1.519, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 5790, "unit": "K"},
            "age": {"value": 6.7e9, "unit": "years"},
            "spectral_class": "G2V",
            "rotation_period": {"value": 22.5, "unit": "days"},
            "magnetic_activity": "Active, similar cycle to the Sun",
        },
        "detailed_description": (
            "Alpha Centauri A, also known as Rigil Kentaurus (meaning 'foot of the Centaur' in Arabic), is the "
            "brightest star of the Alpha Centauri triple system and the nearest naked-eye star to the Sun at a "
            "distance of 4.367 light-years. It is a G2V spectral class star — nearly identical to our Sun in "
            "spectral type, mass (1.0973 solar masses), and surface temperature (5,790 K). Alpha Cen A is slightly "
            "larger than the Sun (1.2234 solar radii) and about 1.5× more luminous. With an apparent magnitude of "
            "-0.01, it is visible to the naked eye from both hemispheres. It orbits Alpha Centauri B in a binary "
            "system with a period of 79.91 years and separation averaging 11.45 AU. Both are gravitationally bound "
            "to distant Proxima Centauri at a distance of ~0.21 light-years. Alpha Cen A is thought to host at least "
            "one planetary system, including Alpha Centauri Bb (a controversial ultra-short-period candidate with "
            "~1.13 Earth masses) discovered via radial velocity in 2012, though its existence remains disputed. The "
            "Alpha Centauri system is a prime target for future interstellar missions due to its proximity and the "
            "presence of Sun-like stars; the Breakthrough Starshot initiative aims to send robotic probes toward "
            "the system."
        ),
        "scientific_facts": [
            "Alpha Cen A's mass is so similar to the Sun's that it has been used as a benchmark for calibrating stellar mass-luminosity relations.",
            "The star shows magnetic activity cycles similar to the Sun's 11-year cycle.",
            "Alpha Cen A's age (~6.7 billion years) means the system is older than the Sun (4.6 billion years).",
            "High-resolution imaging and spectroscopy limit any terrestrial-mass planets around Alpha Cen A in the habitable zone to lower metallicity thresholds.",
            "The star's rotation period of 22.5 days is slightly slower than the Sun's 25-day equatorial rotation.",
            "Complex magnetic topology detected in Alpha Cen A suggests dynamo processes similar to the Sun's.",
            "The binary orbit with Alpha Cen B is well-characterized, making it ideal for testing stellar evolution models.",
            "Alpha Cen A is a member of the Hyades stream — a kinematic group of stars.",
            "The habitable zone of Alpha Cen A extends from ~0.9–1.4 AU, nearly overlapping Earth's orbital position around the Sun.",
        ],
        "did_you_know": [
            "Alpha Centauri A is so similar to the Sun that if it had an Earth-like planet in its habitable zone, conditions could be remarkably Earth-like.",
            "The star's brightness allows it to be among the most well-studied solar analogs in the galaxy.",
            "Ancient star catalogs already identified Alpha Centauri as a pointer to the South Celestial Pole.",
        ],
        "formation_process": (
            "Alpha Cen A formed ~6.7 billion years ago from a giant molecular cloud along with Alpha Cen B. "
            "The two stars formed at different times or underwent rapid early orbital evolution to establish "
            "their current binary configuration."
        ),
        "future_evolution": (
            "Alpha Cen A has already spent ~6.7 billion years on the main sequence and will remain there for "
            "another ~1–2 billion years before exhausting hydrogen and becoming a red giant. Eventually it will "
            "shed its outer layers as a planetary nebula and leave behind a white dwarf similar in properties to Sirius B."
        ),
        "related_objects": ["Alpha Centauri B", "Proxima Centauri", "Alpha Centauri Bb", "The Sun"],
        "parent_system": "Alpha Centauri Triple System / Milky Way Local Neighborhood",
        "child_objects": ["Alpha Centauri Bb (candidate planet)"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "alpha-centauri-b-star")),
        "name": "Alpha Centauri B (Toliman)",
        "category": "Star",
        "subtype": "K-type Main Sequence — Orange Dwarf",
        "tags": ["star", "K-type", "main-sequence", "alpha-centauri-system", "orange-dwarf"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 4.367, "unit": "ly"},
            "coordinates": {"ra": "14h 29m 43.0s", "dec": "-60° 50' 14.3\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
        },
        "physical": {
            "mass": {"value": 0.9092, "unit": "solar_masses"},
            "radius": {"value": 0.8632, "unit": "solar_radii"},
            "luminosity": {"value": 0.5002, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 5316, "unit": "K"},
            "spectral_class": "K1V",
            "rotation_period": {"value": 36.4, "unit": "days"},
            "age": {"value": 6.7e9, "unit": "years"},
        },
        "detailed_description": (
            "Alpha Centauri B is the secondary star of the binary Alpha Centauri system, a K1V spectral type "
            "orange dwarf with a mass of 0.9092 solar masses — slightly less massive and cooler than the Sun. "
            "With a surface temperature of 5,316 K and radius of 0.8632 solar radii, it is noticeably dimmer than "
            "Alpha Cen A, producing only ~50% of the Sun's luminosity. The two stars orbit their common center of "
            "mass with a period of 79.91 years, ranging from ~11.4 AU at closest approach to ~17.6 AU at maximum "
            "separation. As a K-type main-sequence star, Alpha Cen B is less active than G-type stars and has "
            "weaker magnetic fields. It has an apparent magnitude of +1.33, making it visible to the naked eye but "
            "fainter than Alpha Cen A (magnitude -0.01). Like Alpha Cen A, it is part of the triple system that "
            "includes distant Proxima Centauri. The existence of planets around Alpha Cen B has been searched "
            "extensively, with candidate detections and non-detections over the decades."
        ),
        "scientific_facts": [
            "Alpha Cen B is the closest K-type main-sequence star to the Sun, making it a valuable comparison for understanding cool star properties.",
            "The star's lower mass gives it an estimated lifetime of ~15 billion years on the main sequence — longer than the current age of the universe.",
            "Its rotation period of 36.4 days is longer than the Sun's, consistent with lower mass main-sequence stars rotating more slowly.",
            "K-type stars like Alpha Cen B are among the most common main-sequence stars in the Milky Way.",
            "The habitable zone around Alpha Cen B extends from ~0.5–0.9 AU, closer to the star than Earth's position around the Sun.",
            "Alpha Cen B's lower luminosity would require planets to be closer to remain in the habitable zone, increasing tidal heating effects.",
        ],
        "did_you_know": [
            "Alpha Centauri B is slightly less massive and cooler than the Sun, making planets in its habitable zone fundamentally different from Earth.",
            "The orbital dynamics of the Alpha Cen A–B binary create a complex gravitational environment for any planets in the system.",
            "Alpha Cen B is old enough to have potentially harbored life for billions of years if habitable planets exist.",
        ],
        "formation_process": (
            "Alpha Cen B formed ~6.7 billion years ago alongside Alpha Cen A from the same giant molecular cloud."
        ),
        "future_evolution": (
            "Alpha Cen B will remain on the main sequence for another ~8–10 billion years before exhausting hydrogen. "
            "It will then evolve into a red giant and eventually a white dwarf. Because of its lower mass, the white "
            "dwarf remnant will be slightly more massive than Alpha Cen A's white dwarf due to differences in mass loss."
        ),
        "related_objects": ["Alpha Centauri A", "Proxima Centauri", "Alpha Centauri system"],
        "parent_system": "Alpha Centauri Triple System / Milky Way Local Neighborhood",
        "child_objects": [],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "barnards-star")),
        "name": "Barnard's Star",
        "category": "Star",
        "subtype": "Red Dwarf (M-type Main Sequence)",
        "tags": ["star", "red-dwarf", "second-nearest-star", "proper-motion", "high-velocity", "solar-neighborhood"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 5.96, "unit": "ly"},
            "coordinates": {"ra": "17h 57m 48.5s", "dec": "+04° 41' 36\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "proper_motion": {"value": 10.33, "unit": "arcsec/year", "note": "Highest of any star except Proxima"},
            "radial_velocity": {"value": -110.21, "unit": "km/s", "note": "Moving toward us"},
        },
        "physical": {
            "mass": {"value": 0.144, "unit": "solar_masses"},
            "radius": {"value": 0.196, "unit": "solar_radii"},
            "luminosity": {"value": 0.00035, "unit": "solar_luminosities", "note": "~3500x dimmer than the Sun"},
            "surface_temperature": {"value": 3134, "unit": "K"},
            "spectral_class": "M4V",
            "rotation_period": {"value": 130, "unit": "days"},
            "age": {"value": 7.5e9, "unit": "years"},
            "metallicity": "[Fe/H] = -0.36 dex (quite metal-poor)",
        },
        "detailed_description": (
            "Barnard's Star is the second-nearest star system to the Sun at 5.96 light-years away and the "
            "closest red dwarf. Named after Edward Emerson Barnard who discovered its exceptionally high "
            "proper motion in 1916, Barnard's Star has the fastest apparent motion across the sky of any star "
            "except Proxima Centauri — moving 10.33 arcseconds per year. At this rate, it will reach its "
            "closest approach to Earth in approximately 9,800 years at a distance of 3.75 light-years, "
            "eventually becoming the nearest star. Barnard's Star is an old, metal-poor, low-mass M4V red dwarf "
            "with only 14.4% the Sun's mass and ~0.00035 solar luminosities (3,500 times dimmer than the Sun). "
            "Its properties make it an archetypal halo population star — an ancient, metal-poor star belonging to "
            "the galactic halo rather than the young disk. The star has been searched extensively for planetary "
            "companions, with various claims of exoplanet detections from radial velocity measurements over the "
            "decades, though most remain controversial. Recent detections include Barnard's Star b, an Earth-mass "
            "planet candidate in a 233-day orbit, though confirmation requires further observation. Given "
            "Barnard's Star's age (~7.5 billion years) and proximity, any planet system has had ample time to evolve "
            "and represents a long-term laboratory for planetary evolution."
        ),
        "scientific_facts": [
            "Barnard's Star has the second-highest proper motion of any star, after Proxima Centauri (10.75 arcsec/year).",
            "Its metal-poor composition ([Fe/H] = -0.36 dex) indicates formation in the early Milky Way halo.",
            "The star's rotation period of ~130 days is much longer than solar-mass stars, consistent with magnetic braking.",
            "Barnard's Star b, if confirmed, would be an Earth-mass planet in a 233-day orbit with an equilibrium temperature below freezing.",
            "At 5.96 ly, Barnard's Star is ~2 times closer than Sirius and ~0.75 ly from the Alpha Centauri system.",
            "The star's age (~7.5 billion years) places it among the oldest known main-sequence stars.",
            "Barnard's Star's low luminosity means its habitable zone is extremely close, at ~0.015 AU.",
            "X-ray observations detect flaring activity, typical of low-mass red dwarfs despite the star's age.",
            "Proper motion measurements place it in the local standard of rest — a reference frame for stellar kinematics.",
        ],
        "did_you_know": [
            "In ~9,800 years, Barnard's Star will be the closest star to the Sun, outpacing the Alpha Centauri system momentarily.",
            "Despite being so close, Barnard's Star is too faint to see without a telescope — its apparent magnitude is 9.54.",
            "Barnard's Star was prominently featured in science fiction as a target for interstellar exploration.",
        ],
        "formation_process": (
            "Barnard's Star formed ~7.5 billion years ago in the metal-poor halo of the Milky Way, likely "
            "in the early universe when metallicity was much lower. It has since been scattered into a high "
            "proper motion orbit that brings it through the local neighborhood."
        ),
        "future_evolution": (
            "Barnard's Star will remain on the main sequence for trillions of years, slowly fusing hydrogen. "
            "Its interior will gradually heat, increasing its luminosity imperceptibly over billions of years. "
            "Eventually, in the extremely distant future, it will become a white dwarf. Any planets around "
            "Barnard's Star will persist essentially unchanged for cosmological timescales."
        ),
        "related_objects": ["Proxima Centauri", "Alpha Centauri", "Sun", "Jovian planets"],
        "parent_system": "Milky Way Halo / Local Neighborhood",
        "child_objects": ["Barnard's Star b (candidate planet)"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "vega-star")),
        "name": "Vega (Alpha Lyrae)",
        "category": "Star",
        "subtype": "A-type Main Sequence — Rapidly Rotating Star",
        "tags": ["star", "A-type", "main-sequence", "brightest-northern-star", "vega", "summer-triangle", "debris-disk"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 25.04, "unit": "ly"},
            "coordinates": {"ra": "18h 36m 56.3s", "dec": "+38° 47' 21\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "apparent_magnitude": {"value": 0.026, "note": "Fifth brightest star in Earth's night sky"},
        },
        "physical": {
            "mass": {"value": 2.135, "unit": "solar_masses"},
            "radius": {"value": 2.818, "unit": "solar_radii"},
            "luminosity": {"value": 40.12, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 9602, "unit": "K"},
            "spectral_class": "A0V",
            "rotation_period": {"value": 12.5, "unit": "hours", "note": "Extremely rapid — ~1 rotation per half-day"},
            "age": {"value": 4.55e8, "unit": "years", "note": "Relatively young — ~455 million years"},
            "equatorial_velocity": {"value": 274, "unit": "km/s", "note": "~90% speed of breakup for this mass"},
            "debris_disk": "Detected at multiple wavelengths — indicates young planetary system",
        },
        "detailed_description": (
            "Vega is the fifth-brightest naked-eye star in Earth's night sky with an apparent magnitude of 0.026, "
            "located 25 light-years away in the constellation Lyra. It is the brightest star in the northern "
            "hemisphere sky and forms one vertex of the Summer Triangle asterism (with Deneb and Altair). "
            "Vega is an A0V spectral class main-sequence star with 2.135 solar masses, 2.818 solar radii, and "
            "40.12 times the Sun's luminosity. It is also one of the most rapidly rotating stars among bright "
            "stars — its rotation period of only 12.5 hours is so fast that it approaches the theoretical breakup "
            "velocity where rotational centrifugal force would overcome gravity. This rapid rotation causes "
            "centrifugal distortion: Vega's equatorial diameter is ~1.23× its polar diameter, making it oblate. "
            "The rotation axis is tilted ~63° from Earth's viewpoint. Vega is relatively young at ~455 million years "
            "and shows evidence of a debris disk — a system of orbiting dust and planetesimals detected through infrared "
            "excess at multiple wavelengths including data from WISE and Herschel. The debris disk indicates ongoing "
            "planetary system evolution and potentially planets within it. Vega has served as a calibration standard for "
            "astronomical observations for centuries and was the first star (besides the Sun) to have its spectrum "
            "photographed in 1872. It remains one of the most well-studied nearby stars."
        ),
        "scientific_facts": [
            "Vega rotates so rapidly that its equatorial region is ~200 K cooler than its poles due to centrifugal expansion.",
            "The star's rotation axis is inclined ~63° to our line of sight, placing Earth roughly on the equatorial plane.",
            "Vega's debris disk has been detected in infrared, suggesting an age of 100–600 Myr — consistent with the star's estimated age.",
            "The star's surface gravity varies significantly between pole (high) and equator (low) due to the rapid rotation.",
            "Vega was used as a standard star for the magnitude system — defined as magnitude 0.0.",
            "The star's spectral classification (A0V) makes it a useful comparison for studying A-type stellar properties.",
            "Microlensing surveys have placed upper limits on massive planets around Vega.",
            "Vega shows a larger infrared excess than expected, suggesting either a particularly debris-rich system or unresolved dust companions.",
            "The rapidly rotating nature of Vega makes it an ideal laboratory for studying rotational distortion effects in stellar atmospheres.",
        ],
        "did_you_know": [
            "Vega was used by Friedrich Wilhelm Bessel to measure the first-ever stellar parallax in 1838, establishing the cosmic distance scale.",
            "If Vega rotated any faster, material at its equator would be flung into space.",
            "Vega's name comes from the Arabic 'Wāqi', meaning 'falling' (as in the Eagle falling from the sky).",
        ],
        "formation_process": (
            "Vega formed ~455 million years ago from a giant molecular cloud in the Milky Way. Its relatively "
            "young age means it is still in the debris disk phase of planetary system evolution, where leftover "
            "planetesimals are colliding and producing dust."
        ),
        "future_evolution": (
            "Vega will continue fusing hydrogen for approximately another 1 billion years before exhausting its "
            "hydrogen fuel and entering the giant phase. It will expand into an A-type giant, then an orange giant, "
            "and eventually shed its outer layers as a planetary nebula, leaving behind a white dwarf. Any planets "
            "in the system will likely be engulfed or stripped of atmospheres during this evolution."
        ),
        "related_objects": ["Deneb", "Altair", "Summer Triangle", "Young debris disk systems"],
        "parent_system": "Milky Way Local Neighborhood",
        "child_objects": ["Debris Disk"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "arcturus-star")),
        "name": "Arcturus (Alpha Boötis)",
        "category": "Star",
        "subtype": "Red Giant (K-type)",
        "tags": ["star", "red-giant", "brightest-northern-hemisphere", "arcturus", "metal-rich", "high-velocity"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 36.7, "unit": "ly"},
            "coordinates": {"ra": "14h 29m 43.0s", "dec": "+19° 10' 57\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "apparent_magnitude": {"value": -0.04, "note": "Brightest star in the entire northern hemisphere"},
            "proper_motion": {"value": 2.28, "unit": "arcsec/year"},
        },
        "physical": {
            "mass": {"value": 1.08, "unit": "solar_masses"},
            "radius": {"value": 25.4, "unit": "solar_radii", "note": "~25x larger than the Sun"},
            "luminosity": {"value": 170, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 4286, "unit": "K"},
            "spectral_class": "K1.5 III",
            "age": {"value": 7.1e9, "unit": "years"},
            "metallicity": {"value": "[Fe/H] = 0.04 dex", "note": "Slightly metal-rich compared to the Sun"},
            "core_helium_burning": True,
        },
        "detailed_description": (
            "Arcturus is the brightest star visible in the northern hemisphere night sky with an apparent magnitude "
            "of -0.04, located 36.7 light-years away in the constellation Boötes. It is a K1.5 III spectral class "
            "red giant — an evolved star that has exhausted the hydrogen in its core and is now fusing hydrogen in "
            "a shell surrounding an inert helium core. Arcturus has evolved into a giant, expanding to 25.4 solar radii "
            "(roughly the orbit of Mercury around the Sun) while maintaining roughly the same mass as the Sun. This "
            "expansion dramatically increased its luminosity to 170 times solar, even as its surface temperature dropped "
            "to 4,286 K, giving it a deep orange color. Arcturus is metal-rich ([Fe/H] = +0.04 dex) and among the oldest "
            "stars in the solar neighborhood, thought to belong to the thick disk population. It is moving rapidly through "
            "space with a high proper motion, suggesting it has been scattered into a high-eccentricity orbit. Arcturus "
            "represents the evolutionary stage our Sun will reach in approximately 5 billion years. The star appears in "
            "mythology and ancient astronomy across many cultures — sailors used Arcturus for navigation, and it marked "
            "the spring equinox in some ancient calendars."
        ),
        "scientific_facts": [
            "Arcturus's radius of 25.4 solar radii means if placed at the center of the solar system, it would extend past Mercury's orbit.",
            "The star's surface gravity is only ~1% of the Sun's — an object dropped on Arcturus would fall extremely slowly.",
            "Arcturus is slightly metal-rich ([Fe/H] = +0.04), suggesting it formed from highly processed interstellar material.",
            "Their stellar mass (~1.08 solar masses) is nearly identical to the Sun, yet Arcturus is 170× more luminous — a huge difference due to evolutionary stage.",
            "X-ray observations reveal a faint chromosphere — unusual for evolved red giants.",
            "Proper motion measurements show Arcturus is part of the Arcturus kinematic group — a moving group of coeval stars.",
            "The star's core is likely fusing helium into carbon and oxygen — the next stage after core hydrogen exhaustion.",
            "Arcturus is drifting through space at ~145 km/s relative to the solar system — much faster than nearby main-sequence stars.",
            "High-resolution spectroscopy reveals complex chemical abundances indicating multiple nucleosynthetic processes in the star's history.",
        ],
        "did_you_know": [
            "In Greek, Arcturus means 'guardian of the bear' — a reference to its position as the brightest star in Boötes, the herdsman.",
            "Light from Arcturus reaching Earth tonight left the star in 1989 — you're seeing it as it was decades ago.",
            "Arcturus is the template red giant for stellar astrophysics — its well-measured properties make it ideal for calibrating models.",
        ],
        "formation_process": (
            "Arcturus formed ~7.1 billion years ago from a giant molecular cloud, likely in a clustered environment "
            "that has since dispersed. Its metal-rich composition indicates it formed from material enriched by previous "
            "generations of stellar nucleosynthesis."
        ),
        "future_evolution": (
            "Arcturus will continue burning helium in its core for roughly another 1 billion years. Eventually, helium "
            "will be exhausted and the star will enter the asymptotic giant branch (AGB) phase — a brief, unstable "
            "evolutionary stage involving mass loss and chemical enrichment. The star will then shed its outer layers as "
            "a planetary nebula and collapse into a white dwarf."
        ),
        "related_objects": ["The Sun", "Red Giants", "Thick Disk Population", "Boötes constellation"],
        "parent_system": "Milky Way Thick Disk / Local Neighborhood",
        "child_objects": [],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "tau-ceti-star")),
        "name": "Tau Ceti",
        "category": "Star",
        "subtype": "G-type Main Sequence — Sun-like Star",
        "tags": ["star", "G-type", "sun-like", "nearby", "habitable-zone", "tau-ceti", "seti-target"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 11.9, "unit": "ly"},
            "coordinates": {"ra": "01h 44m 04.1s", "dec": "-15° 56' 15\""},
            "galaxy_reference": "Milky Way — Local Neighborhood",
            "proper_motion": {"value": 1.92, "unit": "arcsec/year"},
        },
        "physical": {
            "mass": {"value": 0.783, "unit": "solar_masses"},
            "radius": {"value": 0.793, "unit": "solar_radii"},
            "luminosity": {"value": 0.44, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 5344, "unit": "K"},
            "spectral_class": "G8.5V",
            "age": {"value": 5.8e9, "unit": "years"},
            "metallicity": {"value": "[Fe/H] = -0.50 dex", "note": "Metal-poor compared to the Sun"},
            "rotation_period": {"value": 35.4, "unit": "days"},
        },
        "detailed_description": (
            "Tau Ceti is a nearby G8.5V spectral class star located 11.9 light-years away in the constellation Cetus. "
            "It is similar to the Sun but slightly less massive (0.783 solar masses), less luminous (0.44 solar luminosities), "
            "and cooler (5,344 K). Tau Ceti is notable for being one of the closest Sun-like stars, making it a prime target "
            "for exoplanet searches and the search for extraterrestrial intelligence (SETI). The habitable zone around Tau Ceti "
            "extends from ~0.6–0.8 AU — closer to the star than Earth's orbit, making any habitable planets more likely to be "
            "in resonances with other planets. Multiple candidate planets have been detected through radial velocity measurements, "
            "though not all detections are confirmed. Tau Ceti is older than the Sun (~5.8 billion years vs 4.6 billion) and "
            "metal-poor ([Fe/H] = -0.50), suggesting formation in an earlier, less-enriched epoch of galactic chemical evolution. "
            "The star's lower metallicity historically made planet formation predictions difficult — though the detections suggest "
            "planets can form even in metal-poor environments. Tau Ceti has been prominently featured in science fiction as a "
            "potential harborer of extraterrestrial civilizations due to its proximity and Sun-like properties."
        ),
        "scientific_facts": [
            "Tau Ceti is one of the nearest Sun-like stars, making it historically important for early exoplanet searches.",
            "Multiple planet candidates have been reported around Tau Ceti via radial velocity, ranging from ~1 Earth mass to several Earth-masses.",
            "The star's metal-poor composition ([Fe/H] = -0.50) suggests planets form less efficiently than around metal-rich stars — yet planets exist here.",
            "Tau Ceti's rotation period of 35.4 days is slightly slower than the Sun's, consistent with its lower mass.",
            "The habitable zone of Tau Ceti is at ~0.6–0.8 AU, closer to the star than Earth's orbit around the Sun.",
            "X-ray observations from ROSAT reveal a faint transition region and corona — evidence of chromospheric activity.",
            "Proper motion measurements indicate Tau Ceti is moving through space at ~25 km/s relative to the solar system.",
            "The star's age (~5.8 Gyr) places it among the older nearby main-sequence stars.",
            "Tau Ceti was a target of the pioneering SETI experiment by Frank Drake in 1960.",
        ],
        "did_you_know": [
            "Tau Ceti was featured in the original Star Trek series (TOS) episode 'Balance of Terror' as a location of conflict.",
            "The star has been a SETI target continuously since 1960 — longer than any other target.",
            "If intelligent life existed on a habitable planet around Tau Ceti, radio signals from Earth have had ~12 years to reach them.",
        ],
        "formation_process": (
            "Tau Ceti formed ~5.8 billion years ago from a giant molecular cloud in a lower-metallicity region "
            "of the Milky Way. Its metal-poor composition suggests formation in the early galaxy before significant "
            "enrichment by previous stellar generations."
        ),
        "future_evolution": (
            "Tau Ceti will remain on the main sequence for approximately 5–6 billion more years before exhausting "
            "hydrogen and becoming a red giant. When it expands, its habitable zone will shift outward, potentially "
            "rendering any inner planets uninhabitable while warming outer regions. Eventually the star will become "
            "a white dwarf."
        ),
        "related_objects": ["The Sun", "Nearby G-type stars", "SETI targets", "Exoplanet candidates"],
        "parent_system": "Milky Way Local Neighborhood",
        "child_objects": ["Tau Ceti candidate planets"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "polaris-star")),
        "name": "Polaris (Alpha Ursae Minoris)",
        "category": "Star",
        "subtype": "Multiple Star System — F-type + Red Giant",
        "tags": ["star", "north-star", "pole-star", "multiple-system", "supergiant", "navigation", "precession"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 431, "unit": "ly", "note": "Distance uncertain — some estimates range 400–500 ly"},
            "coordinates": {"ra": "02h 31m 49.0s", "dec": "+89° 15' 51\""},
            "galaxy_reference": "Milky Way",
            "angular_distance_from_pole": {"value": 0.74, "unit": "degrees", "note": "Less than 1° — very close to the celestial north pole"},
        },
        "physical": {
            "polaris_aa": {
                "mass": {"value": 46, "unit": "solar_masses", "note": "Estimate based on orbital dynamics"},
                "radius": {"value": 46, "unit": "solar_radii"},
                "luminosity": {"value": 46000, "unit": "solar_luminosities"},
                "surface_temperature": {"value": 7340, "unit": "K"},
                "spectral_class": "F7 Ib",
                "type": "Yellow Supergiant",
            },
            "polaris_ab": {
                "mass": {"value": 1, "unit": "solar_masses"},
                "spectral_class": "F3V",
                "type": "Main-sequence star",
                "orbital_period": {"value": 2086, "unit": "years"},
            },
            "polaris_b": {
                "mass": {"value": "~0.6", "unit": "solar_masses"},
                "type": "Red dwarf (M-type)",
                "separation": {"value": "~2400 AU", "unit": "(wide binary from Polaris A)"},
            },
            "visual_magnitude": {"value": 1.98, "note": "Brightest component in the system"},
        },
        "detailed_description": (
            "Polaris, also known as the North Star or Pole Star, is celebrated in history and navigation as the "
            "brightest star near the celestial north pole — located only 0.74° from the exact pole position. "
            "Polaris is actually a multiple star system comprising at least three stars: Polaris Aa (a yellow "
            "supergiant, F7 Ib spectral class), Polaris Ab (an F3V main-sequence star in a tight ~2,086-year orbit "
            "around Polaris Aa), and Polaris B (a red dwarf at a wide separation of ~2,400 AU). The primary star, "
            "Polaris Aa, is an evolved supergiant with 46 solar masses, 46 solar radii, and 46,000 times the Sun's "
            "luminosity — an enormous star nearing the end of its life. Its position near the celestial pole makes "
            "it invaluable for determining latitude in the northern hemisphere — a direct north observation of "
            "Polaris gives the observer's latitude. However, due to the precession of Earth's rotational axis with a "
            "~26,000-year period, Polaris's role as the pole star is temporary. In 13,000 years, the pole will point "
            "toward Vega instead. Historically, Polaris was not the pole star — 5,000 years ago, Thuban in Draco held "
            "that role. The system's distance is uncertain, with measurements ranging 400–500 light-years; recent Gaia "
            "parallaxes suggest ~431 ly, though significant measurement uncertainties remain."
        ),
        "scientific_facts": [
            "Polaris Aa is a yellow supergiant — a rare, short-lived evolutionary stage for massive stars.",
            "The Polaris Aa–Ab binary has a remarkably long orbital period of ~2,086 years, making one complete orbit take millennia.",
            "Polaris Aa is losing mass rapidly at rates consistent with evolved supergiant winds — it will likely become a red supergiant or possibly explode.",
            "The system's distance has been revised multiple times — modern Gaia parallaxes put it at ~431 ly (uncertainty ±20 ly).",
            "Polaris's close proximity to the celestial pole (0.74°) makes it the best naked-eye pole star for navigators in the northern hemisphere.",
            "The triple star system has complex orbital dynamics with Polaris B gravitationally perturbing the Aa–Ab pair at long orbital periods.",
            "Over centuries, proper motion studies reveal Polaris is moving toward the pole — it will reach minimum distance (~28' arc) in the year 2102.",
            "Spectroscopy confirms Polaris Aa's evolutionary status as a supergiant, with atmospheric dynamics consistent with mass loss.",
            "The Polaris system is part of a young stellar association suggesting common origin with nearby O and B type stars.",
        ],
        "did_you_know": [
            "Polaris will be the closest star to the celestial north pole in the year 2102 CE.",
            "In 13,000 years, Vega will be the pole star, and in 26,000 years the cycle repeats as Earth's axis precesses.",
            "The Arabic name 'Polaris' derives from Latin 'stella polaris' — meaning 'polar star'.",
        ],
        "formation_process": (
            "Polaris formed from a giant molecular cloud as part of a massive star-forming region. Its high mass "
            "caused rapid evolution, and it likely formed as a wide binary or multiple system through gravitational "
            "fragmentation of the birth cloud."
        ),
        "future_evolution": (
            "Polaris Aa will evolve off the main sequence within the next ~1–2 million years (relatively soon for such "
            "a massive star). It will likely become a red supergiant, then undergo a supernova explosion. The explosion "
            "will disrupt the system, potentially ejecting the companions into space. The supernova remnant may become "
            "a neutron star or black hole depending on the exact progenitor mass."
        ),
        "related_objects": ["Celestial North Pole", "Thuban", "Vega", "Earth's Precession", "Navigation stars"],
        "parent_system": "Milky Way",
        "child_objects": ["Polaris Aa", "Polaris Ab", "Polaris B"],
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "betelgeuse-star")),
        "name": "Betelgeuse (Alpha Orionis)",
        "category": "Star",
        "subtype": "Red Supergiant — Massive, Evolved Star",
        "tags": ["star", "red-supergiant", "betelgeuse", "variable-star", "orion-constellation", "supernova-candidate", "largest-known-stars"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 548, "unit": "ly", "note": "Distance uncertain; some estimates 400–600 ly"},
            "coordinates": {"ra": "05h 55m 10.3s", "dec": "+07° 24' 25\""},
            "galaxy_reference": "Milky Way",
            "apparent_magnitude": {"value": 0.5, "unit": "magnitude (variable: 0–1.3+)", "note": "Changes unpredictably"},
        },
        "physical": {
            "mass": {"value": 16.5, "unit": "solar_masses", "note": "Initial mass; current mass ~19 solar masses from accretion"},
            "radius": {"value": 700, "unit": "solar_radii", "note": "~1000 AU or larger; varies significantly with stellar pulsations"},
            "luminosity": {"value": 126000, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 3500, "unit": "K", "note": "Cool for such a luminous star"},
            "spectral_class": "M2 Iab",
            "rotation_period": {"value": "~15 years", "note": "Estimated; surface rotates extremely slowly"},
            "mass_loss_rate": {"value": "2–3×10⁻⁶", "unit": "solar_masses/year", "note": "Extreme wind," },
            "wind_velocity": {"value": 10, "unit": "km/s", "note": "Slow but massive wind"},
        },
        "detailed_description": (
            "Betelgeuse, also known as Alpha Orionis, is one of the largest and most luminous known stars — a red "
            "supergiant marking the right shoulder of the constellation Orion. With an estimated radius of ~700 solar "
            "radii (though estimates range from 600–900 and vary with pulsations), if placed at the center of our solar "
            "system, Betelgeuse would extend nearly to Jupiter's orbit. Despite its enormous size, Betelgeuse is only "
            "18–20 solar masses — not exceptionally massive for a supergiant — suggesting it may have lost significant "
            "mass to its companion or stellar winds. The star is a semi-regular variable star, changing brightness between "
            "magnitude 0 and 1.3+ on timescales of months to years due to large-scale convective cells on its surface and "
            "interior pulsations. In 2019–2020, Betelgeuse underwent an unprecedented dimming event (fading to magnitude 1.6), "
            "detected across infrared, optical, and ultraviolet wavelengths through large asymmetric dust clouds forming in "
            "its immediate vicinity. This event sparked speculation about imminent supernova, though the star returned to "
            "normal brightness by mid-2020. Betelgeuse's position on the Hertzsprung-Russell diagram indicates it is an "
            "evolved massive star with depleted core hydrogen, now fusing heavier elements in successive shells (likely "
            "late helium or neon burning). With an estimated age of 8–10 million years, Betelgeuse is approaching the final "
            "stages of stellar evolution. Supernova models predict it will explode as a core-collapse supernova within the "
            "next thousand years — possibly within your lifetime, though 'soon' in astronomical terms can mean centuries."
        ),
        "scientific_facts": [
            "Betelgeuse's radius of ~700 solar radii makes it one of the largest known stars, rivaling UY Scuti and Stephenson 2-18 for the title.",
            "The star's surface is dominated by massive convective cells — individual granules are stellar-sized objects themselves.",
            "Betelgeuse's 2019–2020 dimming event revealed asymmetric dust formation in its immediate vicinity, suggesting active mass loss phenomena.",
            "The star's rotation is so slow that surface features would take ~15 years to rotate around the star — nearly imperceptible on human timescales.",
            "Infrared observations reveal Betelgeuse is surrounded by shells of ejected material at various distances, evidence of previous mass loss events.",
            "The star's variability includes both radial pulsations (changing radius) and transverse oscillations (changes in shape).",
            "Compound emission from carbon monoxide and other molecules in Betelgeuse's atmosphere indicates late-stage nucleosynthesis.",
            "Betelgeuse is part of a binary or multiple system — at least one companion has been detected at ~900 AU separation.",
            "The star's position in the Hertzsprung-Russell diagram places it near the red supergiant evolutionary track terminus, approaching core collapse.",
            "ALMA radio observations reveal Betelgeuse ejecting complex organic molecules and dust on scales of hundreds of AU.",
        ],
        "did_you_know": [
            "If Betelgeuse replaced the Sun, its surface would extend past Jupiter — engulfing Mercury, Venus, Earth, Mars, and the asteroid belt.",
            "Betelgeuse is expected to explode as a supernova 'soon' in astronomical terms — within the next 100,000–1,000,000 years.",
            "When Betelgeuse explodes, it will briefly become as bright as the full moon and visible in daylight for weeks or months.",
            "The name 'Betelgeuse' comes from the Arabic 'Yad al-Jauza', meaning 'hand of Orion'.",
        ],
        "formation_process": (
            "Betelgeuse formed from a giant molecular cloud as a massive O or B type star roughly 8–10 million years ago. "
            "It has rapidly evolved through the main sequence and giant phases, now residing as a red supergiant. Large "
            "amounts of mass have been lost during evolution, visible in the shells of ejected material surrounding it."
        ),
        "future_evolution": (
            "Betelgeuse will explode as a Type II core-collapse supernova within the next thousand years — possibly very "
            "soon in astronomical terms. The explosion will briefly rival the full moon in brightness, creating a visible "
            "light-show for weeks or months even in daylight. The supernova will create a neutron star or black hole remnant "
            "and scatter heavy elements (iron, cobalt, nickel, heavier elements) into space, enriching the interstellar medium. "
            "If Betelgeuse has a companion star, the supernova blast wave may strip its atmosphere or trigger mass accretion."
        ),
        "related_objects": ["Rigel (Beta Orionis)", "Orion constellation", "Supergiant stars", "Core-collapse supernovae"],
        "parent_system": "Milky Way",
        "child_objects": ["Dust shells", "Binary companion(s)"],
        "nasa_reference": "https://www.nasa.gov/image-article/nasas-chandra-helps-explain-betelgeuses-dramatic-dimming/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "alpha-centauri-system")),
        "name": "Alpha Centauri System",
        "category": "Star",
        "subtype": "Triple Star System (G2V + K1V + M5.5Ve)",
        "tags": ["star", "binary", "triple-star", "nearest-system", "G-type", "K-type", "exoplanet-candidate"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 4.367, "unit": "ly"},
            "coordinates": {"ra": "14h 39m 36.4s", "dec": "-60° 50' 02\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "alpha_centauri_a": {
                "mass": {"value": 1.100, "unit": "solar_masses"},
                "spectral_class": "G2V",
                "luminosity": {"value": 1.519, "unit": "solar_luminosities"},
            },
            "alpha_centauri_b": {
                "mass": {"value": 0.9092, "unit": "solar_masses"},
                "spectral_class": "K1V",
                "luminosity": {"value": 0.500, "unit": "solar_luminosities"},
            },
            "separation_ab": {"value": 23, "unit": "AU", "orbital_period": "79.91 years"},
            "proxima_distance_from_ab": {"value": 0.21, "unit": "ly"},
        },
        "detailed_description": (
            "The Alpha Centauri system is the nearest stellar system to the Sun — a gravitationally "
            "bound triple: two Sun-like stars (Alpha Cen A and B) orbiting each other plus the red "
            "dwarf Proxima Centauri at a far remove. Alpha Cen A is nearly a solar twin — slightly "
            "more massive and luminous than the Sun, of the same spectral type G2V. Alpha Cen B "
            "is a cooler, slightly smaller K-type star. The two orbit each other with a 79.91-year "
            "period at separations ranging from 11 to 36 AU — comparable to Earth–Saturn distances. "
            "Their relative proximity means from Earth they appear as the third-brightest 'star' "
            "in the sky (unresolvable to the naked eye). Whether stable habitable-zone planets "
            "can exist in this binary has been debated — orbital stability zones exist but binary "
            "perturbations complicate planet retention. Proxima b remains the closest known "
            "exoplanet to Earth."
        ),
        "scientific_facts": [
            "Alpha Centauri A is nearly a solar twin — only 10% more massive and 1.5x as luminous as the Sun.",
            "The AB pair orbits with a 79.91-year period, ranging 11–36 AU apart — both inside and outside Saturn's orbital range.",
            "The system is ~6.5 billion years old — ~2 billion years older than the Sun, with more processed stellar chemistry.",
            "Habitable-zone stability studies suggest Earth-mass planets could survive in stable orbits in the Alpha Cen AB system.",
            "Proxima Centauri's gravitational binding to Alpha Cen AB is tenuous — it could be a passing capture rather than primordial triple.",
            "Alpha Centauri was used as a calibration source by several infrared telescopes due to its known properties.",
            "Rigil Kentaurus (Alpha Cen A+B) and Hadar (Beta Centauri) form the 'Southern Pointer' to the Southern Cross.",
            "The Breakthrough Starshot mission would send probes toward Proxima, passing through the Alpha Cen system region.",
            "No confirmed exoplanet has been detected around Alpha Cen A or B — previous detections were retracted.",
            "Alpha Centauri is a key target for proposed direct imaging missions (e.g., NASA's Habitable Worlds Observatory).",
        ],
        "did_you_know": [
            "From Alpha Centauri, the Sun would appear as a first-magnitude star in the constellation Cassiopeia.",
            "Alpha Centauri A and B orbit so close that from Earth, a telescope is needed to separate them visually.",
            "In 2016 a RV signal from Alpha Cen B suggested a planet; by 2021 it was identified as a stellar activity artifact.",
        ],
        "related_objects": ["Proxima Centauri", "Proxima Centauri b", "Sun", "Sirius"],
        "parent_system": "Alpha Centauri Triple System",
        "nasa_reference": "https://science.nasa.gov/universe/stars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "eta-carinae-star")),
        "name": "Eta Carinae",
        "category": "Star",
        "subtype": "Luminous Blue Variable — Extreme Binary",
        "tags": ["star", "massive-star", "LBV", "pre-supernova", "Carina-Nebula", "hypernova-candidate"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 7500, "unit": "ly"},
            "coordinates": {"ra": "10h 45m 03.6s", "dec": "-59° 41' 04\""},
            "galaxy_reference": "Milky Way — Carina Nebula",
        },
        "physical": {
            "primary_star": {
                "mass": {"value": 100, "unit": "solar_masses", "note": "Current estimate; initially ~150+ solar masses"},
                "luminosity": {"value": 5e6, "unit": "solar_luminosities"},
            },
            "companion_star": {
                "mass": {"value": 30, "unit": "solar_masses"},
                "orbital_period": {"value": 5.54, "unit": "years"},
            },
            "homunculus_nebula": {"mass": {"value": 10, "unit": "solar_masses"}, "age": {"value": 180, "unit": "years"}},
        },
        "detailed_description": (
            "Eta Carinae is one of the most massive, luminous, and unstable star systems in the "
            "Milky Way — a binary consisting of a Luminous Blue Variable (LBV) primary star of "
            "~100 solar masses and a companion of ~30 solar masses, orbiting every 5.54 years. "
            "The primary's luminosity of 5 million solar luminosities approaches the Eddington "
            "limit — where radiation pressure overcomes gravity — making it inherently unstable. "
            "In 1843, it underwent its 'Great Eruption': the star explosively ejected ~10–40 "
            "solar masses in a few years, briefly becoming the second brightest star in the sky "
            "(magnitude -0.8) while remaining intact. The ejected material formed the Homunculus "
            "Nebula — a bipolar dust cloud surrounding the binary that blocks most of its optical "
            "light today. Eta Carinae is expected to explode as a supernova or hypernova within "
            "the next 100,000 years — potentially visible in broad daylight from Earth."
        ),
        "scientific_facts": [
            "Eta Carinae's 1843 eruption ejected 10–40 solar masses and created the visible Homunculus Nebula — still expanding at 600 km/s.",
            "The combined luminosity of the binary (~5 million solar luminosities) makes it one of the most luminous known systems in the Milky Way.",
            "The 5.54-year orbital period causes predictable brightening events when the companion plunges through the primary's wind.",
            "Gamma-ray emission correlated with the 5.54-year period suggests particle acceleration at the wind-wind collision zone.",
            "Eta Carinae was the brightest star in the sky in April 1843 at magnitude -0.8.",
            "The Homunculus Nebula expands at ~600 km/s and is shaped like a peanut or dumbbell seen from different angles.",
            "VLBI radio observations resolved the wind-wind collision zone — a structure only ~15 AU across.",
            "If Eta Carinae exploded as a hypernova or long GRB pointed at Earth, it could significantly affect Earth's ozone layer.",
            "HST/STIS spectroscopy of Eta Carinae's secondary revealed its surface temperature at ~36,000 K.",
            "Multiple lesser eruptions ('minor events') have been recorded since 1843, all at the 5.54-year periastron passage.",
        ],
        "did_you_know": [
            "Eta Carinae shed more mass in 10 years (1843 eruption) than the Sun will lose over its entire 10-billion-year life.",
            "The homunculus lobes are lit by scattered light — the actual star is hidden behind its own dust shell.",
            "If it explodes as a gamma-ray burst aligned with Earth, its gamma rays could reach us in just 7,500 years.",
        ],
        "related_objects": ["Carina Nebula", "Homunculus Nebula", "Betelgeuse", "WR 104"],
        "parent_system": "Carina Nebula — Milky Way",
        "nasa_reference": "https://www.nasa.gov/image-article/eta-carinae-and-the-homunculus-nebula/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "rigel-star")),
        "name": "Rigel",
        "category": "Star",
        "subtype": "Blue-White Supergiant (B8 Iae)",
        "tags": ["star", "blue-supergiant", "massive-star", "Orion", "supernova-candidate", "brightest-Orion"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 860, "unit": "ly"},
            "coordinates": {"ra": "05h 14m 32.3s", "dec": "-08° 12' 06\""},
            "galaxy_reference": "Milky Way — Orion constellation",
        },
        "physical": {
            "mass": {"value": 21, "unit": "solar_masses"},
            "radius": {"value": 78.9, "unit": "solar_radii"},
            "luminosity": {"value": 120000, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 12100, "unit": "K"},
            "spectral_class": "B8 Iae",
        },
        "detailed_description": (
            "Rigel is the brightest star in Orion and the seventh-brightest in the night sky. "
            "A blue-white supergiant, it is intrinsically far more luminous than Betelgeuse — "
            "despite appearing slightly dimmer, Rigel is nearly twice as far away. With a "
            "luminosity of ~120,000 solar luminosities and a surface temperature of 12,100 K, "
            "Rigel emits most of its energy in ultraviolet wavelengths. It is a young, massive "
            "star (~8 million years old) that has already left the main sequence and expanded "
            "significantly. Rigel's extreme UV output is responsible for illuminating the "
            "Witch Head Nebula (IC 2118), a reflection nebula ~3° from Rigel. Like Betelgeuse, "
            "Rigel will eventually explode as a core-collapse supernova."
        ),
        "scientific_facts": [
            "Rigel illuminates the Witch Head Nebula (IC 2118) ~3° away — its UV is sufficient to ionize the nebula at 40 light-years distance.",
            "At ~120,000 solar luminosities, Rigel is one of the most intrinsically luminous stars visible to the naked eye.",
            "Rigel is a multiple star: at least two fainter companions orbit it (Rigel B and C, themselves a close binary).",
            "Rigel's spectral class B8 Iae places it at the hot end of supergiants — it is evolving rightward on the H-R diagram.",
            "The star pulsates semi-regularly with amplitude ~0.1 magnitude — driven by convective instabilities.",
            "Rigel's surface shows photospheric convection visible as light-curve microvariability.",
            "It belongs to the Orion OB1 association — a young massive star cluster dispersing outward.",
            "Rigel's age (~8 million years) means it formed long after the dinosaurs went extinct on Earth.",
            "The star will eventually become a red supergiant (like Betelgeuse at an earlier evolutionary stage) before exploding.",
            "Rigel's distance (~860 ly) and luminosity make it an important anchor point for stellar luminosity calibrations.",
        ],
        "did_you_know": [
            "Rigel, despite being the brightest star in Orion, was designated Beta Orionis — the 'Alpha' (Betelgeuse) may have been brighter in ancient times when Betelgeuse was more active.",
            "If Rigel replaced the Sun, its surface would extend 78x further — past Mercury's orbit — and Earth would be engulfed.",
            "Light from Rigel takes ~860 years to reach Earth — it left during the late Medieval period.",
        ],
        "related_objects": ["Betelgeuse", "Orion Nebula", "Witch Head Nebula", "Orion OB1"],
        "parent_system": "Milky Way — Orion OB1",
        "nasa_reference": "https://science.nasa.gov/universe/stars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "neutron-star-generic")),
        "name": "PSR J0030+0451",
        "category": "Neutron Star",
        "subtype": "Millisecond Pulsar — X-ray Emitter",
        "tags": ["neutron-star", "millisecond-pulsar", "NICER", "hotspots", "dense-matter"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 1000, "unit": "ly"},
            "coordinates": {"ra": "00h 30m 27.4s", "dec": "+04° 51' 39\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.44, "unit": "solar_masses"},
            "radius": {"value": 13, "unit": "km"},
            "rotation_period": {"value": 4.87, "unit": "ms"},
            "surface_temperature": {"value": 1e6, "unit": "K"},
        },
        "detailed_description": (
            "PSR J0030+0451 is an isolated millisecond pulsar that became one of the most "
            "important neutron stars in modern astrophysics when NICER (Neutron star Interior "
            "Composition Explorer) on the ISS measured its X-ray hotspot geometry in 2019. "
            "This measurement allowed, for the first time, simultaneous constraints on both the "
            "neutron star's mass and radius — providing direct information about the equation of "
            "state of ultra-dense nuclear matter (denser than atomic nuclei). The NICER result "
            "found that the star has a mass of ~1.44 solar masses and a radius of ~13 km, and "
            "strikingly, its X-ray hotspots are not at the magnetic poles as in simple models — "
            "they appear at unusual locations, implying complex multipolar magnetic field geometry. "
            "Understanding the equation of state of neutron stars bridges nuclear physics, quantum "
            "chromodynamics (QCD), and astrophysics."
        ),
        "scientific_facts": [
            "NICER's 2019 mass-radius measurement of J0030+0451 provided one of the first direct constraints on neutron star matter EOS.",
            "The star's X-ray hotspots are not antipodal — inconsistent with simple magnetic dipole field geometry.",
            "Millisecond pulsars like J0030 are 'recycled' — spun up to high speeds by accreting mass from a companion (now gone).",
            "Neutron star matter at J0030's density (~5× nuclear density) is unlike any matter produced in Earth laboratories.",
            "NICER observes X-rays from the ISS using silicon drift detectors with microsecond timing precision.",
            "The equation of state constraints from J0030 rule out some purely quark matter models.",
            "A second NICER target, J0740+6620 (~2.08 solar masses), together with J0030 tightly constrains the mass-radius curve.",
            "Millisecond pulsars are among the most precise clocks in the universe — rivaling atomic clock stability.",
            "J0030's recycled nature means it once had a companion star that donated mass to spin it up over millions of years.",
            "Combined GW+NICER constraints from the 2017 neutron star merger GW170817 and NICER are reshaping nuclear astrophysics.",
        ],
        "did_you_know": [
            "Neutron star matter is so dense that a sugar-cube-sized piece would weigh ~100 million metric tons on Earth.",
            "NICER was installed on the ISS specifically to measure neutron star interiors by studying X-ray pulse timing.",
            "PSR J0030+0451 has been spinning ~200 times per second for billions of years — an almost perfectly stable cosmic clock.",
        ],
        "related_objects": ["Crab Pulsar", "NICER instrument", "GW170817", "ISS"],
        "parent_system": "Milky Way",
        "nasa_reference": "https://www.nasa.gov/nicer/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "magnetar-sgr1806")),
        "name": "SGR 1806-20 (Magnetar)",
        "category": "Neutron Star",
        "subtype": "Magnetar — Soft Gamma Repeater",
        "tags": ["neutron-star", "magnetar", "soft-gamma-repeater", "extreme-magnetic-field", "giant-flare"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 50000, "unit": "ly"},
            "coordinates": {"ra": "18h 08m 39.3s", "dec": "-20° 24' 39\""},
            "galaxy_reference": "Milky Way — W31 complex",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 7.56, "unit": "s"},
            "magnetic_field": {"value": 2e11, "unit": "T", "note": "~2×10^15 gauss — quadrillion times Earth's field"},
        },
        "detailed_description": (
            "SGR 1806-20 is one of the most extreme objects ever studied — a magnetar, a special "
            "class of neutron star with magnetic fields quadrillions of times stronger than Earth's. "
            "On December 27, 2004, it unleashed the most energetic event ever recorded from beyond "
            "our solar system: a giant gamma-ray flare lasting ~0.2 seconds that released more "
            "energy than the Sun emits in 250,000 years. The flare was powerful enough to "
            "temporarily ionize Earth's upper atmosphere from 50,000 light-years away — affecting "
            "radio communications. Magnetars are theorized to be neutron stars with extraordinarily "
            "intense magnetic fields (~10¹¹ Tesla) that drive star-quakes — fractures in the "
            "neutron star's rigid crystalline crust — releasing vast amounts of energy as X-rays "
            "and gamma rays. Only about 30 magnetars are known in the Milky Way, making them rare "
            "but catastrophically energetic objects."
        ),
        "scientific_facts": [
            "The December 27, 2004 giant flare released more energy in 0.2 seconds than the Sun emits in 250,000 years.",
            "The flare's gamma rays ionized Earth's D-layer ionosphere from 50,000 light-years — a record interstellar influence on Earth.",
            "Magnetar magnetic fields (~10¹¹ T) are so strong they would distort electron orbitals in hydrogen atoms at 1,000 km distance.",
            "Star-quakes (crustal fractures) on SGR 1806-20 release seismic energy equivalent to magnitude 23 earthquakes.",
            "Magnetars have short active lives (~10,000 years) before their field decays and they become ordinary neutron stars.",
            "SGR 1806-20 is associated with the massive star cluster Cl* 1806-20, which contains VY CMa-type hypergiants.",
            "Only ~30 magnetars are known in the Milky Way — they are the rarest class of neutron star.",
            "Fast Radio Bursts (FRBs) may be produced by extragalactic magnetars — SGR 1935+2154 produced an FRB-like burst in 2020.",
            "Magnetar emissions are detectable across the entire electromagnetic spectrum from radio to gamma-ray.",
            "The extreme magnetic field of a magnetar slows its rotation more rapidly than ordinary pulsars — SGR 1806-20 spins down by ~0.05 ms/year.",
        ],
        "did_you_know": [
            "If SGR 1806-20 were at 10 light-years from Earth, its 2004 flare would have wiped out most life on Earth's surface.",
            "A magnetar's magnetic field is strong enough to rip iron atoms apart at 1,000 km distance.",
            "The 2004 giant flare from SGR 1806-20 was detected by spacecraft throughout the inner solar system.",
        ],
        "related_objects": ["Crab Pulsar", "PSR J0030+0451", "Fast Radio Bursts", "GW170817"],
        "parent_system": "Milky Way",
        "nasa_reference": "https://www.nasa.gov/universe/nasas-swift-satellite-detects-giant-flare-from-magnetar/",
    },

    # -------------------------------------------------------------------------
    # SECTION 3: SOLAR SYSTEM PLANETS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "earth")),
        "name": "Earth",
        "category": "Planet",
        "subtype": "Terrestrial Planet — Ocean World",
        "tags": ["planet", "terrestrial", "habitable", "ocean-world", "solar-system", "biosphere"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 0, "unit": "AU", "note": "Reference body"},
            "coordinates": {"note": "Reference frame for all terrestrial coordinates"},
            "galaxy_reference": "Milky Way — Orion Arm",
            "orbital_period": {"value": 365.25, "unit": "days"},
            "semi_major_axis": {"value": 1.000, "unit": "AU"},
        },
        "physical": {
            "mass": {"value": 5.972e24, "unit": "kg"},
            "radius": {"equatorial": {"value": 6371, "unit": "km"}},
            "density": {"value": 5515, "unit": "kg/m³", "note": "Densest planet in the solar system"},
            "surface_temperature": {"min": -89.2, "max": 56.7, "mean": 14.9, "unit": "°C"},
            "age": {"value": 4.543e9, "unit": "years"},
            "composition": {
                "core": "Iron-nickel (solid inner + liquid outer)",
                "mantle": "Silicate rock",
                "crust": "Silicate minerals",
                "atmosphere": "N₂ (78%), O₂ (21%), Ar (0.93%), CO₂ (0.04%)",
            },
            "magnetic_field": {"value": "25-65", "unit": "microtesla", "origin": "Liquid outer core dynamo"},
            "moons": 1,
        },
        "detailed_description": (
            "Earth is the third planet from the Sun and the only known body in the universe confirmed to "
            "harbor life. It is a terrestrial planet with a differentiated interior: a solid iron-nickel "
            "inner core, a liquid iron outer core (source of Earth's global magnetic field), a silicate "
            "mantle undergoing slow convective circulation, and a thin silicate crust divided into "
            "tectonic plates. Plate tectonics is a defining characteristic of Earth — the continuous "
            "movement and collision of crustal plates drives mountain building, volcanism, and earthquake "
            "activity, while also acting as a long-term carbon-silicate cycle thermostat that has kept "
            "Earth's climate within habitable bounds for billions of years. The hydrosphere covers ~71% "
            "of the surface in liquid water — unique among known planets — making Earth what some "
            "scientists call a 'Goldilocks world' located in the habitable zone of the Sun. The "
            "magnetosphere, generated by the liquid outer core's convection, deflects most of the "
            "solar wind and shields life from harmful cosmic radiation. Earth's large Moon stabilizes "
            "the planet's axial tilt to within ~22–24.5°, preventing extreme climate swings. The "
            "biosphere has profoundly altered the composition of the atmosphere — free molecular oxygen "
            "is almost entirely a product of photosynthetic life — making Earth's atmosphere a "
            "detectable biosignature from space."
        ),
        "scientific_facts": [
            "Earth is the densest planet in the solar system at 5,515 kg/m³.",
            "The liquid outer core convects and generates Earth's magnetic field via the geodynamo — without it, the atmosphere would be stripped by solar wind.",
            "Earth's axial tilt (23.5°) is stabilized by the Moon; without the Moon, the tilt could vary between 0° and 85° over millions of years.",
            "The Chicxulub impactor 66 million years ago (asteroid ~10-15 km wide) caused the mass extinction that ended the non-avian dinosaurs.",
            "Earth has experienced at least 5 major ice ages; currently in an interglacial period of the Quaternary Ice Age.",
            "The Great Oxidation Event ~2.4 billion years ago, caused by cyanobacterial photosynthesis, fundamentally transformed Earth's atmosphere and biosphere.",
            "Plate tectonics recycles carbon from the atmosphere through the carbon-silicate cycle, acting as Earth's long-term climate thermostat.",
            "Earth's magnetic north pole moves ~50 km per year and the field reverses on average every 450,000 years.",
            "The deepest point on Earth, Challenger Deep in the Mariana Trench, is 10,994 m below sea level — deeper than Everest's height.",
            "The Moon formed ~4.5 billion years ago from debris ejected by a Mars-sized impactor (Theia) colliding with proto-Earth.",
        ],
        "did_you_know": [
            "Earth is not a perfect sphere — it bulges at the equator and is flattened at the poles, making it an oblate spheroid.",
            "If Earth's entire history were compressed into a single year, complex multicellular life wouldn't appear until mid-November.",
            "Earth has a slight 'wobble' — the Chandler Wobble — where the poles shift by up to 9 meters over a 14-month cycle.",
        ],
        "formation_process": (
            "Earth accreted from the protoplanetary disk around the young Sun via planetesimal collisions "
            "over ~10–100 million years. The largest collision event was the 'Giant Impact' — a Mars-sized "
            "body called Theia struck proto-Earth ~4.5 billion years ago, melting the surface and ejecting "
            "debris that coalesced into the Moon. Earth then underwent differentiation: denser iron sank "
            "to form the core while lighter silicates rose to form the mantle and crust. Heavy bombardment "
            "by asteroids and comets in the Late Heavy Bombardment period (~3.9 Gya) may have delivered "
            "much of Earth's water."
        ),
        "future_evolution": (
            "Earth will remain habitable for roughly another 1–2 billion years as the Sun slowly brightens. "
            "Eventually the Sun's increasing luminosity will push the liquid water habitable zone outward, "
            "triggering a runaway greenhouse effect that will evaporate the oceans. By ~7.5 billion years "
            "from now, the expanding red giant Sun will likely engulf or severely erode Earth's surface. "
            "Before that, plate tectonics may cease as the mantle cools, eliminating the carbon cycle that "
            "currently stabilizes climate."
        ),
        "related_objects": ["Sun", "Moon", "Mars", "Venus", "International Space Station", "Hubble Space Telescope"],
        "parent_system": "Solar System",
        "child_objects": ["Moon", "International Space Station"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/earth/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mercury-planet")),
        "name": "Mercury",
        "category": "Planet",
        "subtype": "Terrestrial Planet — Rocky, Airless World",
        "tags": ["planet", "terrestrial", "solar-system", "inner-planet", "airless", "extreme-temperatures"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"min": 77.3e6, "max": 221.9e6, "unit": "km"},
            "semi_major_axis": {"value": 0.387, "unit": "AU"},
            "orbital_period": {"value": 87.97, "unit": "days"},
        },
        "physical": {
            "mass": {"value": 3.301e23, "unit": "kg", "earth_masses": 0.055},
            "radius": {"value": 2439.7, "unit": "km"},
            "density": {"value": 5427, "unit": "kg/m³", "note": "Second densest planet after Earth"},
            "surface_temperature": {"min": -180, "max": 430, "unit": "°C"},
            "moons": 0,
            "magnetic_field": {"value": "1.1% of Earth's", "note": "Weak but present — puzzling for its small size"},
        },
        "detailed_description": (
            "Mercury is the smallest planet in the solar system and the closest to the Sun, racing "
            "around its orbit every 88 days. Despite its proximity to the Sun, Mercury is not the "
            "hottest planet — that distinction belongs to Venus — because Mercury has virtually no "
            "atmosphere to retain heat. Surface temperatures swing between -180°C in polar craters "
            "never reached by sunlight and +430°C at the equatorial subsolar point — the largest "
            "temperature range of any planet. Mercury's density is surprisingly high: second only "
            "to Earth, implying a disproportionately large iron core that makes up ~85% of its "
            "radius. This may be because a giant impact stripped its outer silicate layers early "
            "in solar system history. The MESSENGER mission (2011–2015) discovered water ice "
            "permanently shadowed in polar craters, ancient volcanic plains, a weak magnetic "
            "field (4x offset from the spin axis), and complex tectonic scarps called 'lobate "
            "rupes' — shrinkage cracks as the core cooled and contracted."
        ),
        "scientific_facts": [
            "Mercury's iron core makes up ~85% of its radius — the largest core-to-planet ratio in the solar system.",
            "MESSENGER confirmed water ice in permanently shadowed craters near Mercury's poles.",
            "Mercury's magnetic field is ~1% Earth's but 4x offset from the rotation axis — a unique geometry.",
            "Mercury experiences a 3:2 spin-orbit resonance — 3 rotations per 2 orbits — not tidal locking.",
            "Lobate rupes (thrust fault scarps) up to 3 km high crisscross Mercury's surface — formed as the planet shrank.",
            "Mercury has no moon, no rings, and essentially no atmosphere (exosphere of helium, sodium, oxygen).",
            "Perihelion precession of Mercury's orbit was the first observational confirmation of Einstein's general relativity.",
            "BepiColombo (ESA/JAXA) is en route to Mercury, arriving 2025 for a detailed orbital mission.",
            "Surface color maps show ancient volcanic plains covering 40% of the planet.",
            "Mercury's year is shorter than its day: one solar day equals 176 Earth days.",
        ],
        "did_you_know": [
            "A Mercury solar day (sunrise to sunrise) lasts 176 Earth days — twice its year.",
            "Mercury's ancient surface is riddled with impact craters, including the 1,550-km-wide Caloris Basin.",
            "Despite being airless, Mercury has a faint 'exosphere' of sodium atoms blasted off the surface by solar wind.",
        ],
        "related_objects": ["Sun", "Venus", "Earth", "MESSENGER mission", "BepiColombo"],
        "parent_system": "Solar System",
        "nasa_reference": "https://solarsystem.nasa.gov/planets/mercury/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "jupiter-planet")),
        "name": "Jupiter",
        "category": "Planet",
        "subtype": "Gas Giant — Failed Star Candidate",
        "tags": ["planet", "gas-giant", "solar-system", "largest-planet", "great-red-spot", "magnetosphere"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"min": 588.5e6, "max": 968.5e6, "unit": "km"},
            "semi_major_axis": {"value": 5.203, "unit": "AU"},
            "orbital_period": {"value": 11.862, "unit": "years"},
            "galaxy_reference": "Milky Way — Solar System",
        },
        "physical": {
            "mass": {"value": 1.898e27, "unit": "kg", "earth_masses": 317.8},
            "radius": {"equatorial": {"value": 71492, "unit": "km", "earth_radii": 11.2}},
            "density": {"value": 1326, "unit": "kg/m³"},
            "surface_temperature": {"cloudtop": -108, "unit": "°C"},
            "core_temperature": {"value": 24000, "unit": "K"},
            "age": {"value": 4.503e9, "unit": "years"},
            "composition": {"hydrogen": "~89.8%", "helium": "~10.2%", "trace_other": "ammonia, water, methane"},
            "moons": 95,
            "ring_system": True,
            "magnetic_field": {"note": "14x stronger than Earth's, largest planetary magnetosphere"},
        },
        "detailed_description": (
            "Jupiter is the largest planet in the solar system, with a mass 2.5 times greater than all "
            "other planets combined. It is primarily composed of hydrogen and helium, and lacks a "
            "well-defined solid surface — instead transitioning from gaseous atmosphere through a layer "
            "of liquid molecular hydrogen, then into metallic hydrogen (a state where hydrogen conducts "
            "electricity like a metal, existing at pressures exceeding ~1 million atmospheres) and "
            "possibly a dense rocky/icy core. The transition to metallic hydrogen is believed to generate "
            "Jupiter's extraordinary magnetic field — roughly 14 times stronger than Earth's — creating "
            "the largest magnetosphere of any planet, extending 7 million km toward the Sun and stretching "
            "as far as Saturn's orbit on the downwind side. Jupiter's visible atmosphere is structured "
            "into alternating light zones (rising ammonia clouds) and dark belts (descending drier air) "
            "driven by strong east-west jet streams. The Great Red Spot — an anticyclonic storm larger "
            "than Earth — has been observed continuously since at least 1831, though it is currently "
            "shrinking. Jupiter emits more heat than it receives from the Sun — residual gravitational "
            "contraction energy from its formation. Its 95 known moons include four large Galilean "
            "satellites: Io (most volcanically active body in the solar system), Europa (probable "
            "subsurface liquid ocean), Ganymede (largest moon in the solar system, bigger than Mercury), "
            "and Callisto (ancient cratered surface)."
        ),
        "scientific_facts": [
            "Jupiter's Great Red Spot has been a continuous storm for at least 190 years, though it has shrunk by ~50% since the 1800s.",
            "Metallic hydrogen inside Jupiter — hydrogen under such extreme pressure it conducts electricity — is a state not achievable in Earth laboratories.",
            "Jupiter's magnetic field traps high-energy particles in radiation belts more intense than Earth's Van Allen belts.",
            "Ganymede, Jupiter's largest moon, is larger than the planet Mercury and has its own magnetosphere.",
            "Europa's subsurface ocean contains an estimated 2–3x more liquid water than all of Earth's oceans combined.",
            "Jupiter's atmospheric wind speeds reach 600 km/h in jet streams.",
            "The Shoemaker-Levy 9 comet broke into 21 fragments and impacted Jupiter in July 1994, leaving scars larger than Earth.",
            "Jupiter's day lasts only 9 hours 56 minutes — the shortest of any planet — causing significant equatorial bulging.",
            "Io has over 400 active volcanoes driven by tidal heating from Jupiter's gravity, making it the most geologically active body in the solar system.",
            "Jupiter acts as a gravitational shield for the inner solar system, deflecting many potentially hazardous comets and asteroids.",
        ],
        "did_you_know": [
            "If Jupiter were ~75–80x more massive, it would have ignited nuclear fusion and become a star.",
            "Europa's ice shell is estimated to be 15–25 km thick; radar evidence from the Galileo mission suggests a ~100 km deep ocean beneath.",
            "Jupiter has a faint ring system discovered by Voyager 1 in 1979 — much less visible than Saturn's.",
        ],
        "formation_process": (
            "Jupiter formed early in the solar system, within the first 3–5 million years, before the "
            "solar nebula dispersed. The core accretion model proposes that a rocky/icy core of ~10–20 "
            "Earth masses formed first beyond the frost line, then rapidly accreted a hydrogen-helium "
            "envelope from the surrounding disk. Jupiter's early formation likely shaped the entire solar "
            "system: the Grand Tack hypothesis suggests Jupiter migrated inward then outward, truncating "
            "Mars's growth and scattering the asteroid belt into its current sparse configuration."
        ),
        "future_evolution": (
            "Jupiter will slowly contract and cool over billions of years, gradually radiating its "
            "residual gravitational heat. As the Sun expands into a red giant, Jupiter's outer moons may "
            "enter more favorable positions. Europa remains a long-term candidate for habitability as "
            "the Sun's habitable zone shifts outward. Jupiter itself will persist essentially intact "
            "even after the Sun's death, eventually becoming a cold, dark 'frozen giant' orbiting the "
            "Sun's white dwarf remnant."
        ),
        "related_objects": ["Sun", "Io", "Europa", "Ganymede", "Callisto", "Great Red Spot", "Saturn"],
        "parent_system": "Solar System",
        "child_objects": ["Io", "Europa", "Ganymede", "Callisto", "Amalthea", "95 known moons"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/jupiter/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "saturn-planet")),
        "name": "Saturn",
        "category": "Planet",
        "subtype": "Gas Giant — Ring World",
        "tags": ["planet", "gas-giant", "rings", "solar-system", "saturn-moons", "titan"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"min": 1.2e9, "max": 1.67e9, "unit": "km"},
            "semi_major_axis": {"value": 9.537, "unit": "AU"},
            "orbital_period": {"value": 29.46, "unit": "years"},
            "galaxy_reference": "Milky Way — Solar System",
        },
        "physical": {
            "mass": {"value": 5.683e26, "unit": "kg", "earth_masses": 95.16},
            "radius": {"equatorial": {"value": 60268, "unit": "km", "earth_radii": 9.45}},
            "density": {"value": 687, "unit": "kg/m³", "note": "Less dense than water — would float in a sufficiently large ocean"},
            "surface_temperature": {"cloudtop": -139, "unit": "°C"},
            "age": {"value": 4.503e9, "unit": "years"},
            "composition": {"hydrogen": "~96.3%", "helium": "~3.25%", "trace_other": "methane, ammonia, ethane"},
            "moons": 146,
            "ring_system": {
                "main_rings": "A, B, C (densest)",
                "extent": {"inner": 66900, "outer": 480000, "unit": "km"},
                "thickness": {"value": "10–1000", "unit": "m"},
                "composition": "~95% water ice + rock",
            },
        },
        "detailed_description": (
            "Saturn is the sixth planet from the Sun and the second-largest in the solar system, famous "
            "for its spectacular ring system — the most extensive and visible of any planet. The rings "
            "are composed primarily of water ice particles ranging from tiny grains to chunks several "
            "meters across, with a small fraction of rocky material. Despite spanning nearly 480,000 km "
            "in diameter, the rings are astonishingly thin — typically only 10–1,000 meters — giving "
            "Saturn a structure analogous to a sheet of paper the size of a football field. Saturn is "
            "the least dense planet in the solar system, with an average density of just 687 kg/m³ — "
            "less than liquid water. Like Jupiter, Saturn radiates significantly more energy than it "
            "receives from the Sun, partly from ongoing helium-rain precipitation: helium droplets "
            "condense in the upper atmosphere, sink through the hydrogen envelope, and release "
            "gravitational energy as heat. Saturn has 146 known moons — the most of any planet — "
            "including Titan, the only moon with a dense atmosphere and surface liquid hydrocarbon "
            "lakes (methane and ethane), and Enceladus, which vents water-rich plumes from a "
            "confirmed subsurface ocean through its south polar region. The Cassini mission (2004–2017) "
            "revolutionized our understanding of the Saturn system, discovering Enceladus's plumes, "
            "detailing ring structure and dynamics, and deploying the Huygens probe onto Titan's surface."
        ),
        "scientific_facts": [
            "Saturn's rings may be geologically recent — some estimates suggest they formed only 100–400 million years ago from a destroyed moon or captured comet.",
            "Enceladus's geysers eject ~200 kg/s of water vapor and ice — this material feeds Saturn's E ring.",
            "Titan's atmosphere is ~1.45x denser than Earth's at sea level, dominated by nitrogen with methane clouds.",
            "The Cassini division — a 4,800 km gap in Saturn's rings — is maintained by gravitational resonance with moon Mimas.",
            "Saturn's hexagonal polar vortex (north pole) is a jet stream feature ~30,000 km wide with no known parallel on any other planet.",
            "Saturn experiences diamond rain: at ~30,000 km depth, carbon graphite is compressed into diamonds that sink toward the core.",
            "Titan has rivers, lakes, and seas of liquid methane and ethane, forming a methane cycle analogous to Earth's water cycle.",
            "The Huygens probe's descent through Titan's atmosphere in January 2005 is the most distant landing ever achieved from Earth.",
            "Saturn's magnetosphere, unlike Jupiter's, is nearly perfectly aligned with its rotation axis — an unusual geometry with unexplained implications.",
            "Ring shepherding moons like Prometheus and Pandora maintain the sharp edges of the F ring through gravitational interactions.",
        ],
        "did_you_know": [
            "Saturn would float in water — it's the only planet in the solar system less dense than H₂O.",
            "A day on Saturn is only 10 hours 33 minutes, causing a 10% equatorial bulge visible even through small telescopes.",
            "Titan's methane seas are the only known stable bodies of surface liquid in the solar system outside Earth.",
        ],
        "formation_process": (
            "Saturn, like Jupiter, formed early via core accretion beyond the frost line — a rocky-icy "
            "core accreted first, then swept up hydrogen and helium from the disk. Its ring system "
            "is thought to be much younger than the planet itself, likely formed from the tidal "
            "disruption of a former moon (hypothetically named Chrysalis) or a captured comet, "
            "which was torn apart by Saturn's gravity within the Roche limit."
        ),
        "future_evolution": (
            "Saturn's rings are being slowly eroded — ring particles are continuously spiraling inward "
            "due to 'ring rain' (charged particles guided down magnetic field lines). At current rates, "
            "the rings may disappear in ~100–300 million years. Saturn itself will persist long after "
            "the Sun's death. Titan may enter Saturn's Roche limit far in the future or escape to "
            "become a free-floating object."
        ),
        "related_objects": ["Sun", "Titan", "Enceladus", "Mimas", "Jupiter", "Cassini mission"],
        "parent_system": "Solar System",
        "child_objects": ["Titan", "Enceladus", "Mimas", "Dione", "Rhea", "Iapetus", "146 known moons"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/saturn/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mars-planet")),
        "name": "Mars",
        "category": "Planet",
        "subtype": "Terrestrial Planet — Desert World",
        "tags": ["planet", "terrestrial", "solar-system", "mars-exploration", "red-planet", "potential-habitability"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"min": 54.6e6, "max": 401.4e6, "unit": "km"},
            "semi_major_axis": {"value": 1.524, "unit": "AU"},
            "orbital_period": {"value": 686.97, "unit": "days"},
            "galaxy_reference": "Milky Way — Solar System",
        },
        "physical": {
            "mass": {"value": 6.39e23, "unit": "kg", "earth_masses": 0.107},
            "radius": {"value": 3389.5, "unit": "km", "earth_radii": 0.53},
            "density": {"value": 3933, "unit": "kg/m³"},
            "surface_temperature": {"min": -143, "max": 35, "mean": -63, "unit": "°C"},
            "age": {"value": 4.503e9, "unit": "years"},
            "atmosphere": {"CO2": "95.3%", "N2": "2.6%", "Ar": "1.9%", "pressure": "~0.6% of Earth's"},
            "moons": 2,
            "magnetic_field": {"note": "No global field; crustal remnant magnetism in ancient southern highlands"},
        },
        "detailed_description": (
            "Mars is the fourth planet from the Sun and the most thoroughly explored planet beyond Earth, "
            "hosting more active missions than any other extraterrestrial body. With half Earth's diameter "
            "and 10% of its mass, Mars is a cold, arid world with a thin CO₂ atmosphere providing "
            "insufficient pressure for liquid water on the surface today. Yet Mars shows overwhelming "
            "geological evidence of a wetter past: ancient river valleys, delta deposits, dry lake beds, "
            "and hydrated mineral formations that required prolonged liquid water activity. The loss of "
            "Mars's early thicker atmosphere and hydrosphere is linked to the cessation of its global "
            "magnetic dynamo roughly 4 billion years ago, which allowed the solar wind to gradually "
            "erode the atmosphere. Mars hosts the tallest volcano in the solar system — Olympus Mons "
            "(21.9 km above datum, ~600 km wide) — and the longest canyon system — Valles Marineris "
            "(~4,000 km long, up to 7 km deep). The planet's two small, irregular moons Phobos and "
            "Deimos are likely captured asteroids from the outer asteroid belt. Modern missions including "
            "Perseverance, Ingenuity, Curiosity, and MAVEN continue to characterize Mars's climate "
            "history, surface chemistry, and habitability potential with the goal of understanding "
            "whether Mars ever harbored microbial life."
        ),
        "scientific_facts": [
            "Olympus Mons is the tallest volcano in the solar system at 21.9 km height and ~600 km base diameter.",
            "Valles Marineris is 4,000 km long, up to 200 km wide, and 7 km deep — stretching the distance from California to New York.",
            "Mars has two distinct hemispheres: the northern plains (lower, younger) and southern highlands (older, heavily cratered) — the cause of this dichotomy is unknown.",
            "Perchlorate salts in Mars's soil depress the freezing point of water, creating possible ephemeral brines even today.",
            "The Mars helicopter Ingenuity completed over 70 flights, demonstrating powered flight in ~1% of Earth's atmospheric density.",
            "Mars's polar ice caps contain both water ice and CO₂ dry ice; the north cap in summer is almost pure water ice.",
            "MAVEN mission data shows Mars loses ~100 grams of atmospheric gas to space every second via solar wind stripping.",
            "The ancient southern highlands show remnant crustal magnetism — stripes of alternating polarity suggesting a past plate tectonic-like activity.",
            "Curiosity rover detected complex organic molecules (thiophenes, benzene, toluene) in 3.5-billion-year-old Gale Crater sediments.",
            "The InSight lander measured thousands of 'marsquakes', revealing a liquid iron-sulfide core ~1,800 km in radius.",
        ],
        "did_you_know": [
            "A Martian day (sol) is 24 hours, 39 minutes, and 35.244 seconds — surprisingly close to an Earth day.",
            "Dust devils on Mars can be 10x taller than those on Earth, reaching 8 km high.",
            "The Perseverance rover successfully produced ~122 grams of oxygen from CO₂ using the MOXIE experiment — a critical step for future human missions.",
        ],
        "formation_process": (
            "Mars accreted from the protoplanetary disk about 4.5 billion years ago. Its small mass "
            "compared to Earth is explained by the Grand Tack hypothesis: Jupiter's early inward migration "
            "truncated the supply of material available for Mars to accrete, leaving it as a planetary "
            "embryo rather than a fully grown planet. Mars differentiated early, developing a core, mantle, "
            "and crust within the first ~100 million years."
        ),
        "future_evolution": (
            "Phobos, Mars's inner moon, is spiraling inward due to tidal deceleration and will either "
            "break apart into a ring system or crash into Mars in ~30–50 million years. Mars will continue "
            "to cool geologically. Any future human settlement faces challenges of thin atmosphere, "
            "radiation exposure, and extreme cold. On billion-year timescales, Mars will remain a frozen, "
            "geologically dead world."
        ),
        "related_objects": ["Sun", "Phobos", "Deimos", "Earth", "Olympus Mons", "Perseverance Rover", "Curiosity Rover"],
        "parent_system": "Solar System",
        "child_objects": ["Phobos", "Deimos"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/mars/overview/",
    },

    # -------------------------------------------------------------------------

     {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "venus-planet")),
        "name": "Venus",
        "category": "Planet",
        "subtype": "Terrestrial Planet — Runaway Greenhouse World",
        "tags": ["planet", "terrestrial", "solar-system", "inner-planet", "greenhouse-effect", "hottest-planet"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"min": 38.2e6, "max": 261.0e6, "unit": "km"},
            "semi_major_axis": {"value": 0.723, "unit": "AU"},
            "orbital_period": {"value": 224.7, "unit": "days"},
        },
        "physical": {
            "mass": {"value": 4.867e24, "unit": "kg", "earth_masses": 0.815},
            "radius": {"value": 6051.8, "unit": "km"},
            "density": {"value": 5243, "unit": "kg/m³"},
            "surface_temperature": {"mean": 464, "unit": "°C", "note": "Hottest planetary surface in the solar system"},
            "atmospheric_pressure": {"value": 92, "unit": "atm", "note": "Equivalent to 900m deep in Earth's ocean"},
            "atmosphere": {"CO2": "96.5%", "N2": "3.5%"},
            "rotation_period": {"value": 243, "unit": "days", "note": "Retrograde — spins backward relative to orbit"},
            "moons": 0,
        },
        "detailed_description": (
            "Venus is Earth's 'twisted twin' — nearly identical in size and mass but with a surface "
            "that is the most hostile of any rocky planet in the solar system. Its thick CO₂ "
            "atmosphere produces a runaway greenhouse effect that maintains surface temperatures "
            "of ~464°C — hotter than Mercury despite being twice as far from the Sun. Surface "
            "pressure is 92 atmospheres — equal to 900 m depth in Earth's ocean. Despite orbital "
            "similarities to Earth, Venus rotates very slowly and backward (retrograde), so a "
            "Venusian day is longer than its year. Its surface, mapped primarily by the Magellan "
            "spacecraft (1989–1994) using radar, is dominated by volcanic plains, massive shield "
            "volcanoes (including Maat Mons at 8 km height), and highland 'continents' (Aphrodite "
            "Terra, Ishtar Terra). In 2023, re-analysis of Magellan radar data revealed fresh lava "
            "flows around Maat Mons — the first direct evidence of ongoing volcanic activity on Venus. "
            "Multiple upcoming missions (DAVINCI, VERITAS, EnVision) will return to Venus after "
            "decades of neglect."
        ),
        "scientific_facts": [
            "Venus's surface temperature of 464°C is hot enough to melt lead.",
            "Re-analysis of Magellan radar data in 2023 identified fresh lava flows, confirming active volcanism.",
            "The Soviet Venera landers (1970–1982) survived only 23–127 minutes on Venus's surface before failing.",
            "Venus's retrograde rotation may result from a giant impact or atmospheric tidal torques early in its history.",
            "Its thick sulfuric acid clouds reflect ~70% of incoming sunlight — making Venus the brightest planet.",
            "The Venusian day (~243 Earth days) is longer than its year (~225 days).",
            "DAVINCI (NASA) will drop a probe through Venus's atmosphere while VERITAS will map its geology from orbit.",
            "Venus lacks a magnetic field despite being Earth-like in size — its slow rotation fails to drive a core dynamo.",
            "Surface radar maps show ~1,000 impact craters distributed uniformly, suggesting a global resurfacing event ~500–800 million years ago.",
            "The possibility of phosphine in Venus's clouds (2020 claim) sparked debate — the detection remains contested.",
        ],
        "did_you_know": [
            "The Sun rises in the west on Venus — it rotates backward relative to most planets.",
            "Venus is the only planet named after a female deity and is the brightest object in Earth's sky after the Sun and Moon.",
            "Atmospheric pressure on Venus's surface would crush a modern submarine.",
        ],
        "related_objects": ["Sun", "Earth", "Magellan spacecraft", "DAVINCI mission", "VERITAS mission"],
        "parent_system": "Solar System",
        "nasa_reference": "https://solarsystem.nasa.gov/planets/venus/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "uranus-planet")),
        "name": "Uranus",
        "category": "Planet",
        "subtype": "Ice Giant",
        "tags": ["planet", "ice-giant", "solar-system", "tilted-axis", "rings", "methane-atmosphere"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"min": 2.57e9, "max": 3.15e9, "unit": "km"},
            "semi_major_axis": {"value": 19.19, "unit": "AU"},
            "orbital_period": {"value": 84.01, "unit": "years"},
        },
        "physical": {
            "mass": {"value": 8.681e25, "unit": "kg", "earth_masses": 14.54},
            "radius": {"equatorial": {"value": 25559, "unit": "km", "earth_radii": 4.01}},
            "density": {"value": 1271, "unit": "kg/m³"},
            "surface_temperature": {"cloudtop": -197, "unit": "°C"},
            "axial_tilt": {"value": 97.77, "unit": "degrees", "note": "Rotates on its side"},
            "moons": 28,
            "ring_system": True,
        },
        "detailed_description": (
            "Uranus is the seventh planet from the Sun and one of the two 'ice giants' of the outer "
            "solar system (the other being Neptune). Unlike the gas giants Jupiter and Saturn, "
            "which are mostly hydrogen and helium, Uranus is dominated by water, methane, and "
            "ammonia ices in a hot pressurized interior — hence 'ice giant' despite having no "
            "surface ice. Methane in the upper atmosphere absorbs red light and reflects blue-green "
            "wavelengths, giving Uranus its distinctive cyan color. Its most distinctive feature is "
            "its extreme axial tilt of 97.77° — essentially rolling on its side relative to its "
            "orbital plane. This means each pole experiences ~42 years of continuous sunlight "
            "followed by ~42 years of darkness. The cause of this tilt is thought to be a giant "
            "impact early in the solar system. Uranus has 13 known rings, discovered in 1977 during "
            "a stellar occultation, and 28 known moons — all named after characters from Shakespeare "
            "and Alexander Pope. The only spacecraft to visit Uranus was Voyager 2 in January 1986."
        ),
        "scientific_facts": [
            "Uranus's 97.77° axial tilt means its poles get more sunlight annually than its equator.",
            "Uranus emits almost no internal heat — unusual for a giant planet; its interior mechanism is not understood.",
            "Miranda, Uranus's moon, has the tallest known cliff in the solar system: Verona Rupes (~20 km high).",
            "Uranus's rings were discovered in 1977 via stellar occultation — 2 years before Voyager 2's flyby.",
            "Voyager 2 (January 1986) is the only spacecraft to have visited Uranus — still the sole flyby.",
            "All 28 Uranian moons are named after characters from Shakespeare and Alexander Pope.",
            "NASA's proposed Uranus Orbiter and Probe (UOP) was identified as the top priority for the 2023–2032 planetary science decadal survey.",
            "The magnetic field of Uranus is tilted 59° from the rotation axis and offset from the geometric center — highly unusual.",
            "Uranus's cloud deck contains methane ice, ammonia ice, and hydrogen sulfide clouds.",
            "Ring particles around Uranus are among the darkest known — reflecting only ~5% of incident light.",
        ],
        "did_you_know": [
            "Uranus was the first planet discovered with a telescope, by William Herschel on March 13, 1781.",
            "A 'diamond rain' may fall inside Uranus — carbon compressed under enormous pressure forms diamond crystals.",
            "During Uranus's polar summer, the Sun never sets for 21 years — then never rises for 21 years.",
        ],
        "related_objects": ["Neptune", "Saturn", "Miranda", "Voyager 2", "Ariel", "Titania"],
        "parent_system": "Solar System",
        "nasa_reference": "https://solarsystem.nasa.gov/planets/uranus/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "neptune-planet")),
        "name": "Neptune",
        "category": "Planet",
        "subtype": "Ice Giant — Windiest Planet",
        "tags": ["planet", "ice-giant", "solar-system", "extreme-winds", "Triton", "great-dark-spot"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"min": 4.3e9, "max": 4.7e9, "unit": "km"},
            "semi_major_axis": {"value": 30.07, "unit": "AU"},
            "orbital_period": {"value": 164.8, "unit": "years"},
        },
        "physical": {
            "mass": {"value": 1.024e26, "unit": "kg", "earth_masses": 17.15},
            "radius": {"equatorial": {"value": 24764, "unit": "km", "earth_radii": 3.88}},
            "density": {"value": 1638, "unit": "kg/m³"},
            "surface_temperature": {"cloudtop": -201, "unit": "°C"},
            "wind_speed": {"value": 2100, "unit": "km/h", "note": "Fastest in the solar system"},
            "moons": 16,
        },
        "detailed_description": (
            "Neptune is the eighth and most distant planet from the Sun, an ice giant with the "
            "fastest recorded wind speeds in the solar system — up to 2,100 km/h. Like Uranus, "
            "Neptune's blue color comes from methane in its atmosphere, though Neptune is a "
            "distinctly deeper, more vivid blue, likely due to an unidentified chromophore. "
            "Neptune emits 2.6x more energy than it receives from the Sun — powered by internal "
            "heat left from formation. The planet hosts dynamic storm systems: the Great Dark Spot "
            "(observed by Voyager 2 in 1989) was a massive anticyclone the size of Earth that "
            "disappeared by 1994; new dark spots have appeared and disappeared since. Neptune's "
            "largest moon, Triton, orbits backward (retrograde) in a decaying orbit — strong "
            "evidence it is a captured Kuiper Belt Object, the largest ever snared by a planet. "
            "Triton's surface shows active nitrogen geysers and at its current orbital decay rate "
            "it will cross Neptune's Roche limit in ~3.6 billion years, either crashing into the "
            "planet or forming a ring system."
        ),
        "scientific_facts": [
            "Neptune's winds reach 2,100 km/h — the fastest in the solar system — despite receiving 900x less sunlight than Earth.",
            "Triton's retrograde orbit strongly implies it is a captured Kuiper Belt Object — the largest such capture known.",
            "Neptune emits 2.6x more energy than it receives from the Sun — its internal heat source is unexplained.",
            "The Great Dark Spot observed by Voyager 2 in 1989 was Earth-sized but had vanished by 1994 (Hubble).",
            "Triton has active nitrogen geysers erupting ~8 km high, powered by solar heating of subsurface nitrogen ice.",
            "Voyager 2 (August 1989) is the only spacecraft to visit Neptune — still the sole flyby after 35+ years.",
            "Neptune has 5 main rings — the most prominent being the Adams ring with mysterious bright 'arcs'.",
            "The ring arcs are puzzlingly confined — likely held by gravitational resonance with nearby moon Galatea.",
            "Neptune takes 164.8 years to orbit the Sun — it completed its first full orbit since discovery in 2011.",
            "Diamond rain may form deep in Neptune's mantle at pressures millions of times Earth atmospheric.",
        ],
        "did_you_know": [
            "Neptune was predicted mathematically before it was observed — both Leverrier (France) and Adams (UK) independently calculated its position in 1846.",
            "A year on Neptune lasted from 1846 (discovery) to 2011 — only one Neptunian year has elapsed since its discovery.",
            "Triton is the only large moon in the solar system orbiting in the opposite direction to its planet's rotation.",
        ],
        "related_objects": ["Uranus", "Triton", "Voyager 2", "Pluto", "Kuiper Belt"],
        "parent_system": "Solar System",
        "nasa_reference": "https://solarsystem.nasa.gov/planets/neptune/overview/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "europa-moon")),
        "name": "Europa",
        "category": "Moon",
        "subtype": "Galilean Moon — Ocean World",
        "tags": ["moon", "Jupiter-moon", "ocean-world", "habitability", "subsurface-ocean", "Galilean"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": "varies with Jupiter", "unit": "km"},
            "orbital_period": {"value": 3.55, "unit": "days"},
            "distance_from_jupiter": {"value": 670900, "unit": "km"},
        },
        "physical": {
            "mass": {"value": 4.7998e22, "unit": "kg"},
            "radius": {"value": 1560.8, "unit": "km"},
            "density": {"value": 3013, "unit": "kg/m³"},
            "surface_temperature": {"mean": -160, "unit": "°C"},
            "ice_shell_thickness": {"estimated": "15–25", "unit": "km"},
            "ocean_depth": {"estimated": "~100", "unit": "km"},
        },
        "detailed_description": (
            "Europa is the sixth-largest moon in the solar system and one of the most compelling "
            "candidates for extraterrestrial life. Beneath its smooth, crisscrossed water ice "
            "shell lies a global liquid water ocean containing an estimated 2–3 times more liquid "
            "water than all of Earth's oceans combined. The ocean is kept liquid by tidal heating "
            "from Jupiter's powerful gravity flexing Europa's interior — generating frictional "
            "heat sufficient to maintain a liquid ocean despite the surface temperature of -160°C. "
            "Europa's ice surface shows chaos terrain (disrupted ice blocks re-frozen in new "
            "positions), linear ridges (pressurized water forcing through cracks), and "
            "subsurface lakes. The Galileo spacecraft detected induced magnetic signatures "
            "consistent with a salty, electrically conducting subsurface ocean. NASA's Europa "
            "Clipper mission (launched October 2024) will make 49 close flybys of Europa to "
            "characterize its ocean, ice shell chemistry, and potential habitability — the first "
            "dedicated mission to an ocean world beyond Earth."
        ),
        "scientific_facts": [
            "Europa's subsurface ocean may contain 2–3x more liquid water than all of Earth's oceans combined.",
            "Tidal heating from Jupiter keeps Europa's ocean liquid despite a surface at -160°C.",
            "Hubble detected possible water vapor plumes erupting from Europa's south pole — potentially sampling the ocean.",
            "Europa's induced magnetic field, detected by Galileo, is consistent with a salty, electrically conductive ocean.",
            "Chaos terrain on Europa's surface may be ancient ice rafts that floated apart and refroze.",
            "Linear ridges crossing Europa's surface may be where tidal stresses crack the ice and water wells up, refreezes.",
            "Europa Clipper (launched Oct 2024) will perform 49 flybys to analyze ice, ocean chemistry, and habitability.",
            "Europa's ocean may interact with a rocky seafloor — enabling hydrothermal chemistry analogous to Earth's ocean vents.",
            "The ice shell thickness is debated: Galileo data suggests 15–25 km; gravity models allow up to 30 km.",
            "Europa's surface is geologically young — almost no impact craters exist, implying continuous resurfacing.",
        ],
        "did_you_know": [
            "Europa has fewer impact craters than any other solid body in the solar system — its surface is continuously renewed.",
            "If Europa's ocean has hydrothermal vents like Earth's deep oceans, it could support chemolithotrophic microbial life.",
            "Europa orbits Jupiter in a 1:2:4 resonance with Io and Ganymede — called the Laplace resonance.",
        ],
        "related_objects": ["Jupiter", "Io", "Ganymede", "Callisto", "Europa Clipper", "Enceladus"],
        "parent_system": "Jupiter System",
        "nasa_reference": "https://europa.nasa.gov/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "titan-moon-saturn")),
        "name": "Titan",
        "category": "Moon",
        "subtype": "Saturn Moon — Dense Atmosphere, Hydrocarbon Seas",
        "tags": ["moon", "Saturn-moon", "dense-atmosphere", "methane-seas", "Huygens", "Cassini", "prebiotic-chemistry"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_jupiter": {"note": "Orbits Saturn"},
            "distance_from_saturn": {"value": 1221870, "unit": "km"},
            "orbital_period": {"value": 15.945, "unit": "days"},
        },
        "physical": {
            "mass": {"value": 1.3452e23, "unit": "kg"},
            "radius": {"value": 2574.7, "unit": "km", "note": "Larger than Mercury"},
            "density": {"value": 1882, "unit": "kg/m³"},
            "surface_temperature": {"mean": -179, "unit": "°C"},
            "atmosphere": {"N2": "~95%", "CH4": "~5%", "H2": "~0.1%", "pressure": "1.5 atm"},
        },
        "detailed_description": (
            "Titan is Saturn's largest moon and the only moon in the solar system with a dense "
            "atmosphere and surface liquids — making it the most Earth-like body in terms of "
            "landscape despite temperatures of -179°C. Its nitrogen-methane atmosphere is denser "
            "than Earth's at sea level (1.5 atm), opaque in visible wavelengths due to an orange "
            "hydrocarbon haze, but transparent in infrared and radio. Titan's methane cycle mimics "
            "Earth's water cycle: methane evaporates from seas, forms clouds, rains onto the surface, "
            "collects in rivers, and flows into hydrocarbon lakes and seas. The largest, Kraken Mare, "
            "covers ~400,000 km² — larger than the Caspian Sea. The ESA Huygens probe descended "
            "through Titan's atmosphere on January 14, 2005 — the most distant planetary landing "
            "ever achieved. NASA's Dragonfly mission (launch 2028, arrival ~2034) will send a "
            "nuclear-powered rotorcraft to fly across Titan's surface, sampling prebiotic chemistry "
            "in dunes, craters, and shorelines."
        ),
        "scientific_facts": [
            "Titan's orange haze is composed of complex organic molecules (tholins) formed by UV irradiation of methane and nitrogen.",
            "Kraken Mare on Titan covers ~400,000 km² — larger than Earth's Caspian Sea.",
            "Huygens probe transmission on Jan 14, 2005 is the most distant surface landing in history.",
            "Cassini RADAR mapped Titan's polar seas — Ligeia, Kraken, and Punga Mare — with 3D bathymetry.",
            "Titan's dunes (Shangri-La and Belet dune fields) are made of organic particles, not silica sand.",
            "Dragonfly (NASA, launch 2028) will be the first planetary drone mission, flying through Titan's atmosphere.",
            "Titan's surface shows river channels, delta deposits, and shoreline features carved by liquid methane.",
            "Acetylene (C₂H₂) was detected on Titan's surface — a potential energy source for non-water-based life.",
            "Titan has a subsurface water-ammonia ocean at ~100 km depth, detected via Cassini gravity measurements.",
            "The moon's atmosphere shows seasonal variation — Cassini observed 13 years of Titan weather.",
        ],
        "did_you_know": [
            "Titan is the only extraterrestrial body with stable surface liquids — lakes and seas of methane and ethane.",
            "A human on Titan could strap on wings and fly by flapping — the dense atmosphere and low gravity make powered human flight feasible.",
            "Titan's atmosphere contains more nitrogen than Earth's by fraction, and complex organic chemistry that may resemble early Earth.",
        ],
        "related_objects": ["Saturn", "Enceladus", "Cassini mission", "Huygens probe", "Dragonfly mission"],
        "parent_system": "Saturn System",
        "nasa_reference": "https://solarsystem.nasa.gov/moons/saturn-moons/titan/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "io-moon-jupiter")),
        "name": "Io",
        "category": "Moon",
        "subtype": "Galilean Moon — Hypervolcanic World",
        "tags": ["moon", "Jupiter-moon", "volcanism", "tidal-heating", "sulfur", "Galilean"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_jupiter": {"value": 421700, "unit": "km"},
            "orbital_period": {"value": 1.769, "unit": "days"},
        },
        "physical": {
            "mass": {"value": 8.9319e22, "unit": "kg"},
            "radius": {"value": 1821.6, "unit": "km"},
            "density": {"value": 3528, "unit": "kg/m³"},
            "surface_temperature": {"mean": -130, "unit": "°C", "volcanic_hotspots": "Up to 1600°C"},
            "active_volcanoes": {"value": "400+"},
        },
        "detailed_description": (
            "Io is the most volcanically active body in the solar system — a world covered in "
            "hundreds of active volcanic centers, sulfur plains, and constantly resurfacing lava "
            "flows. Tidal heating from Jupiter's immense gravitational pull — amplified by orbital "
            "resonances with Europa and Ganymede — flexes Io's interior, generating frictional "
            "heat sufficient to drive a global magma ocean beneath a thin crust. Io has no water "
            "and no impact craters — it is resurfaced so rapidly by volcanic deposits that impacts "
            "are immediately buried. Its surface is painted in yellows, reds, and blacks from "
            "sulfur compounds at different temperatures. Volcanic plumes rise hundreds of kilometers "
            "into space — Pele volcano's plume reaches ~300 km altitude. Material from Io's "
            "volcanoes escapes to form a torus of ionized sulfur and oxygen around Jupiter's orbit, "
            "feeding Jupiter's magnetosphere and creating the most intense radiation belts in the "
            "solar system."
        ),
        "scientific_facts": [
            "Io is resurfaced by volcanic deposits at a rate of ~1 cm/year — no ancient terrain survives.",
            "Pele volcano's plume reaches 300 km altitude — one of the tallest known in the solar system.",
            "Io's volcanic hotspots reach temperatures of ~1,600°C — matching or exceeding ancient Earth's komatiite lavas.",
            "Voyager 1 discovered active volcanism on Io in 1979 — the first confirmed volcanic eruption on a body other than Earth.",
            "Io feeds Jupiter's Io plasma torus with ~1 ton/second of sulfur and oxygen ions.",
            "The Io plasma torus creates intense radiation belts that damage spacecraft — Galileo received 25x its design radiation dose.",
            "Juno's JIRAM infrared instrument revealed new hotspot distributions across Io's surface in 2023–2024 flybys.",
            "Io has a thin SO₂ atmosphere that collapses and freezes when it passes into Jupiter's shadow.",
            "Mountains on Io rise up to 18 km — taller than Everest — formed by compression of volcanic deposits, not tectonic uplift.",
            "Io's orbital resonance with Europa (2:1) and Ganymede (4:1) maintains its orbital eccentricity and tidal heating.",
        ],
        "did_you_know": [
            "Io's surface changes visibly between Voyager (1979) and Galileo (1995–2003) images — dozens of new features appeared.",
            "If you stood on Io, Jupiter would fill ~20° of sky and be visible even in daylight.",
            "Io lacks water entirely — the intense tidal heating and proximity to Jupiter evaporated it long ago.",
        ],
        "related_objects": ["Jupiter", "Europa", "Ganymede", "Callisto", "Voyager 1"],
        "parent_system": "Jupiter System",
        "nasa_reference": "https://solarsystem.nasa.gov/moons/jupiters-moons/io/overview/",
    },

    # ----------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "ganymede-moon")),
        "name": "Ganymede",
        "category": "Moon",
        "subtype": "Galilean Moon — Largest Moon in the Solar System",
        "tags": ["moon", "Jupiter-moon", "largest-moon", "magnetosphere", "Galilean", "subsurface-ocean"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_jupiter": {"value": 1070400, "unit": "km"},
            "orbital_period": {"value": 7.155, "unit": "days"},
        },
        "physical": {
            "mass": {"value": 1.4819e23, "unit": "kg"},
            "radius": {"value": 2634.1, "unit": "km", "note": "Larger than Mercury"},
            "density": {"value": 1936, "unit": "kg/m³"},
            "surface_temperature": {"mean": -163, "unit": "°C"},
        },
        "detailed_description": (
            "Ganymede is the largest and most massive moon in the solar system — larger than Mercury "
            "and containing more mass than all smaller solar system moons combined. It is the only "
            "moon known to generate its own magnetic field, creating a miniature magnetosphere "
            "embedded within Jupiter's vast magnetosphere. Where Ganymede's and Jupiter's "
            "magnetospheres interact, auroral ovals form — detected by Hubble and later by the "
            "JUICE spacecraft. Ganymede's interior is differentiated: an iron core, silicate mantle, "
            "and thick ice-water shell that may host a deep subsurface ocean at ~800 km depth. "
            "Its surface shows two distinct terrains: ancient dark, heavily cratered regions and "
            "younger grooved terrain formed by tectonic extension. ESA's JUICE (Jupiter Icy Moons "
            "Explorer) will orbit Ganymede starting 2034 — making it the first mission to orbit "
            "a moon other than Earth's Moon."
        ),
        "scientific_facts": [
            "Ganymede's intrinsic magnetic field generates auroras detectable by Hubble — unique among moons.",
            "Hubble's UV auroral observations in 2015 provided indirect evidence of Ganymede's subsurface ocean via magnetic field wobble.",
            "Ganymede is larger than Mercury but contains only ~45% Mercury's mass (it is predominantly ice).",
            "ESA's JUICE spacecraft will enter Ganymede orbit in 2034 — the first orbital mission to a non-Earth moon.",
            "Ganymede's grooved terrain formed 3–3.5 billion years ago by extensional tectonics — plates separating.",
            "Its icy surface has crater palimpsests — ghost craters where ice flowed and erased topography.",
            "The moon has a thin oxygen atmosphere produced by charged particle bombardment of the ice surface.",
            "Tidal heating from Jupiter is insufficient to melt Ganymede's ocean — it is maintained by radioactive decay and pressure.",
            "Ganymede's magnetosphere is ~0.75× Earth's magnetic field strength at its surface.",
            "Charon (Pluto's moon) and Ganymede are sometimes compared as the two largest 'ice worlds' with differentiated interiors.",
        ],
        "did_you_know": [
            "Galileo Galilei discovered Ganymede on January 7, 1610 — one of four moons that overturned the geocentric model of the universe.",
            "If Ganymede orbited the Sun instead of Jupiter, it would be classified as a planet.",
            "Ganymede's icy surface may hide a liquid ocean with more water than all of Earth's oceans combined.",
        ],
        "related_objects": ["Jupiter", "Europa", "Io", "Callisto", "JUICE mission"],
        "parent_system": "Jupiter System",
        "nasa_reference": "https://solarsystem.nasa.gov/moons/jupiters-moons/ganymede/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "enceladus-moon-saturn")),
        "name": "Enceladus",
        "category": "Moon",
        "subtype": "Saturn Moon — Cryo-Active Ocean World",
        "tags": ["moon", "Saturn-moon", "ocean-world", "geysers", "habitability", "Cassini", "hydrothermal"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_saturn": {"value": 238020, "unit": "km"},
            "orbital_period": {"value": 1.370, "unit": "days"},
        },
        "physical": {
            "mass": {"value": 1.0802e20, "unit": "kg"},
            "radius": {"value": 252.1, "unit": "km"},
            "surface_temperature": {"mean": -201, "unit": "°C", "south_pole_hotspot": -93},
            "plume_output": {"value": 200, "unit": "kg/s"},
        },
        "detailed_description": (
            "Enceladus is Saturn's sixth-largest moon and the most dramatic example of an active "
            "ocean world in the solar system. Despite its tiny size (~500 km diameter), it vents "
            "~200 kg/s of water-rich material from its south polar region through a network of "
            "parallel fractures dubbed 'tiger stripes'. Cassini flew directly through these plumes "
            "and detected water ice, sodium chloride (salt), silica nanoparticles, hydrogen gas, "
            "and complex organic molecules — all indicators of hydrothermal activity on the ocean "
            "floor. The molecular hydrogen is particularly significant: it implies ongoing "
            "serpentinization reactions at hot rock-water interfaces on the seafloor, the same "
            "process that fuels chemolithotropic microbes in Earth's deep ocean vents. Enceladus "
            "thus provides all three ingredients considered necessary for life: liquid water, "
            "energy (hydrothermal), and organic chemistry. Its plumes feed Saturn's E ring with "
            "fresh ice particles. The south polar terrain is geologically young, warm, and unlike "
            "any other icy moon surface."
        ),
        "scientific_facts": [
            "Cassini detected H₂ in Enceladus's plumes — consistent with ongoing hydrothermal reactions at the seafloor.",
            "Silica nanoparticles in the plumes require hot (>90°C) water-rock reactions at the ocean floor.",
            "Cassini's final close flybys sampled organic molecules in the plumes with masses >200 amu — complex organics.",
            "Enceladus's plumes create and maintain Saturn's E ring — the most extended ring in the Saturn system.",
            "The south polar region is anomalously warm (~-93°C vs expected -201°C) due to internal tidal heating.",
            "The ocean of Enceladus is estimated to be global, at least 26–31 km deep below a ~30 km ice shell.",
            "Tidal dissipation from Saturn heats Enceladus's interior at a rate ~30x greater than Earth's radiogenic heating per unit mass.",
            "The tiger stripe fractures (Baghdad, Cairo, Damascus, Alexandria) are ~130 km long and spaced ~35 km apart.",
            "Cassini's INMS detected traces of methane in the plumes — possibly biogenic or from hydrothermal sources.",
            "Proposed Enceladus Life Finder (ELF) or SELFI missions would flythrough plumes with mass spectrometers to detect biosignatures.",
        ],
        "did_you_know": [
            "Enceladus is smaller than the UK — yet harbors a global subsurface ocean and erupting geysers.",
            "The tiger stripes glow in Saturn's near-infrared — the heat output is detectable from orbit.",
            "Cassini's discovery of Enceladus's plumes in 2005 revolutionized the search for life beyond Earth.",
        ],
        "related_objects": ["Saturn", "Titan", "Cassini mission", "Europa", "Hydrothermal Systems"],
        "parent_system": "Saturn System",
        "nasa_reference": "https://solarsystem.nasa.gov/moons/saturn-moons/enceladus/overview/",
    },


    # -------------------------------------------------------------------------
    # SECTION 4: NEBULAE
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "orion-nebula-m42")),
        "name": "Orion Nebula (M42)",
        "category": "Nebula",
        "subtype": "Emission / Reflection Nebula — H II Region",
        "tags": ["nebula", "star-forming", "H2-region", "emission-nebula", "orion", "Messier"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 1344, "unit": "ly"},
            "coordinates": {"ra": "05h 35m 17.3s", "dec": "-05° 23' 28\""},
            "galaxy_reference": "Milky Way — Orion Arm",
            "diameter": {"value": 24, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 2000, "unit": "solar_masses"},
            "temperature": {"ionized_gas": {"value": 10000, "unit": "K"}},
            "age": {"value": 3e6, "unit": "years"},
            "composition": {"hydrogen": "~73%", "helium": "~25%", "dust_and_heavier": "~2%"},
        },
        "detailed_description": (
            "The Orion Nebula (M42) is the closest large star-forming region to Earth and one of the "
            "most studied objects in astronomy. Visible to the naked eye as the middle 'star' in Orion's "
            "sword, it is a sprawling cloud of ionized hydrogen gas and dust roughly 24 light-years across. "
            "The nebula glows because a cluster of hot young stars — the Trapezium Cluster — at its heart "
            "emit intense ultraviolet radiation that ionizes the surrounding hydrogen, causing it to emit "
            "the characteristic reddish Hα light. The Trapezium contains four closely packed O-type and "
            "B-type stars within a region just 1.5 light-years across, making it one of the densest young "
            "stellar environments known. Throughout the nebula, Hubble Space Telescope and JWST imaging "
            "have revealed hundreds of proplyds — protoplanetary disks around young stars — silhouetted "
            "against the bright background nebula. These disks represent solar systems in their earliest "
            "formation stages, some showing evidence of disk photoevaporation from the Trapezium radiation. "
            "M42 is part of the much larger Orion Molecular Cloud Complex, which spans ~300 light-years "
            "and includes other active star-forming regions like M43 and the Horsehead Nebula region. "
            "Below the main nebula sits M43 and the Orion B cloud, while to the south the Flame Nebula "
            "and Horsehead Nebula mark the boundary with denser molecular gas. The entire region is "
            "expected to form a stellar association of several thousand stars over the next million years."
        ),
        "scientific_facts": [
            "M42 is the brightest diffuse nebula in the sky at magnitude 4.0 — easily visible to the naked eye.",
            "The Trapezium Cluster stars formed less than 300,000 years ago — extraordinarily young in stellar terms.",
            "Over 700 stars with protoplanetary disks (proplyds) have been identified in M42 using HST imaging.",
            "The nebula is only the visible 'blister' on the face of the Orion Molecular Cloud, the bulk of which is opaque cold gas.",
            "JWST's first deep imaging of M42 resolved the lowest-mass brown dwarfs and free-floating planetary-mass objects (JuMBOs) down to ~1 Jupiter mass.",
            "JuMBOs (Jupiter-mass binary objects) discovered by JWST in 2023 — pairs of planetary-mass free-floating objects — challenge current star and planet formation models.",
            "The nebula emits strongly in infrared, radio, and X-ray in addition to visible light.",
            "Theta¹ Orionis C, the most massive Trapezium star (~40 solar masses), drives most of the nebula's ionization.",
            "Shock fronts in M42 produce bright-rimmed globules — dense clumps of gas being compressed by UV radiation and potentially forming stars.",
        ],
        "did_you_know": [
            "The Orion Nebula was officially recorded by Nicolas-Claude Fabri de Peiresc in 1610, making it one of the first nebulae observed through a telescope.",
            "Light seen from the nebula tonight left it about 1,344 years ago — during the early Islamic Golden Age on Earth.",
            "JWST's 2023 images of M42 detected over 40 Jupiter-mass binary pairs floating freely — objects that shouldn't exist under current theory.",
        ],
        "formation_process": (
            "The Orion Nebula is the active ionized face of the Orion Molecular Cloud, a giant cold gas "
            "reservoir. Star formation began ~12 million years ago in the outer parts of the complex. "
            "The Trapezium stars formed most recently (~300,000 years ago) and their UV radiation has "
            "eaten into the surrounding molecular cloud, creating the visible H II region cavity we see "
            "today. The entire cloud complex is in an active phase of ongoing star formation."
        ),
        "future_evolution": (
            "Over the next few million years, the Trapezium stars' radiation and eventual supernova "
            "explosions will disperse the remaining molecular cloud. The star cluster will gradually "
            "evolve into an open cluster that spreads across the galaxy. Proplyds in the nebula have a "
            "race against photoevaporation — those too close to the Trapezium may lose their disks "
            "before planets can form."
        ),
        "related_objects": ["Trapezium Cluster", "Horsehead Nebula", "Orion Molecular Cloud", "M43", "Flame Nebula"],
        "parent_system": "Orion Molecular Cloud Complex",
        "child_objects": ["Trapezium Cluster", "Proplyds (700+)", "BN/KL region"],
        "nasa_reference": "https://www.nasa.gov/image-article/nasa-reveals-webb-first-deep-field/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "crab-nebula-m1")),
        "name": "Crab Nebula (M1)",
        "category": "Nebula",
        "subtype": "Supernova Remnant — Pulsar Wind Nebula",
        "tags": ["nebula", "supernova-remnant", "pulsar-wind-nebula", "Messier", "crab-pulsar", "SN1054"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 6523, "unit": "ly"},
            "coordinates": {"ra": "05h 34m 31.97s", "dec": "+22° 00' 52.1\""},
            "galaxy_reference": "Milky Way",
            "diameter": {"value": 11, "unit": "ly"},
            "expansion_rate": {"value": 1500, "unit": "km/s"},
        },
        "physical": {
            "mass": {"value": 4.6, "unit": "solar_masses", "note": "Ejected material only"},
            "temperature": {"filaments": {"value": 11000, "unit": "K"}, "interior": {"value": 1e7, "unit": "K"}},
            "age": {"value": 971, "unit": "years", "note": "Supernova observed 1054 AD"},
            "central_object": "Crab Pulsar (PSR B0531+21)",
        },
        "detailed_description": (
            "The Crab Nebula is the remains of a massive star that exploded as a supernova in 1054 AD — "
            "an event recorded by Chinese, Japanese, and Arab astronomers who reported it visible in "
            "daylight for 23 days and at night for nearly two years. What persists today is a rapidly "
            "expanding cloud of gas and dust ~11 light-years across, still moving outward at ~1,500 km/s. "
            "At the nebula's heart lies the Crab Pulsar — a neutron star just ~20 km in diameter, "
            "rotating 30.2 times per second — formed in the supernova collapse. The pulsar acts as an "
            "energy engine for the entire nebula: its powerful magnetic field flings electrons outward "
            "at near-light-speed, creating a pulsar wind nebula that glows brightly from radio waves to "
            "gamma rays through synchrotron radiation. The outer filaments of the nebula are rich in "
            "elements forged in the progenitor star and the supernova itself — oxygen, sulfur, and neon "
            "are spectroscopically detected. The Crab is one of the most well-studied astrophysical "
            "objects precisely because its age is exactly known, making it an ideal laboratory for "
            "studying how supernova remnants evolve. It is so consistently bright in X-rays that the "
            "'crab' is used as a standard unit of X-ray flux ('1 Crab') for comparing other X-ray sources."
        ),
        "scientific_facts": [
            "The Crab Pulsar loses ~5×10³¹ watts of rotational energy per second — this 'spin-down luminosity' directly powers the nebula.",
            "The Crab Pulsar's rotation period increases by ~38 nanoseconds per day as it loses energy.",
            "It was the first cosmic object identified as both a radio pulsar (1968) and an optical pulsar.",
            "The nebula radiates across the full electromagnetic spectrum: radio, IR, optical, UV, X-ray, and gamma-ray.",
            "The 'Crab' X-ray flux unit: 1 Crab = 2.4 × 10⁻⁸ erg/cm²/s — used universally in high-energy astrophysics.",
            "HST images show dynamic knot structures near the pulsar changing on timescales of days to weeks.",
            "The nebula contains an inner torus and polar jets — structures shaped by the pulsar's rotation axis and magnetic field.",
            "Element abundances in the Crab's filaments confirm nucleosynthesis predictions from core-collapse supernova models.",
            "The progenitor star is estimated to have had a mass of ~8–10 solar masses — right at the lower mass limit for core-collapse supernovae.",
        ],
        "did_you_know": [
            "Chinese Song Dynasty records from July 4, 1054 AD describe a 'guest star' in Taurus bright enough to read by at night.",
            "The Crab Nebula was listed first in Charles Messier's 1774 catalog because it had fooled him into thinking it was a comet.",
            "The Crab Pulsar emits precisely timed pulses used historically to test general relativity and synchronize atomic clocks.",
        ],
        "formation_process": (
            "A massive star (~8–10 solar masses) exhausted its nuclear fuel ~7,000–8,000 years ago (light "
            "arrival adjusted for distance). The iron core collapsed in milliseconds, creating a neutron "
            "star. The outer stellar layers rebounded off the stiff neutron star surface, were accelerated "
            "by the neutrino burst, and exploded outward as a supernova. The neutron star remnant became "
            "the Crab Pulsar; the expelled material is the expanding Crab Nebula."
        ),
        "future_evolution": (
            "The Crab Nebula will continue expanding and cooling over the next ~10,000 years, gradually "
            "merging into the interstellar medium. The pulsar will continue to slow its rotation over "
            "millions of years as it radiates energy, eventually becoming a cold, slowly rotating "
            "neutron star. The heavy elements dispersed by the supernova will enrich future generations "
            "of star-forming clouds."
        ),
        "related_objects": ["Crab Pulsar", "SN 1054", "Milky Way", "Vela Pulsar", "Cassiopeia A"],
        "parent_system": "Milky Way — Perseus Arm",
        "child_objects": ["Crab Pulsar (PSR B0531+21)"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2005/37/1823-Image.html",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "eagle-nebula-m16")),
        "name": "Eagle Nebula (M16)",
        "category": "Nebula",
        "subtype": "Emission Nebula — H II Region with Pillars",
        "tags": ["nebula", "emission-nebula", "pillars-of-creation", "star-forming", "Messier", "Hubble"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 7000, "unit": "ly"},
            "coordinates": {"ra": "18h 18m 48s", "dec": "-13° 48' 26\""},
            "galaxy_reference": "Milky Way",
            "diameter": {"value": 70, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 5500, "unit": "solar_masses"},
            "temperature": {"ionized_gas": {"value": 8000, "unit": "K"}},
            "age": {"value": 5.5e6, "unit": "years"},
        },
        "detailed_description": (
            "The Eagle Nebula is a massive star-forming region famous for the 'Pillars of Creation' — "
            "towering columns of gas and dust captured in one of Hubble's most iconic images (1995). "
            "The pillars — the tallest reaching ~4 light-years — are evaporating gaseous globules "
            "(EGGs) where dense gas resists the ionizing ultraviolet radiation from the young star "
            "cluster NGC 6611 at the nebula's heart, while surrounding less-dense gas is eroded "
            "away. Embedded at the tips of the pillars are protostars in their earliest formation "
            "stages. JWST's 2022 image of the Pillars in near-infrared revealed previously hidden "
            "infant stars, the complex dust structures, and showed the pillars as translucent at "
            "infrared wavelengths — piercing the veil of dust that optical images cannot penetrate."
        ),
        "scientific_facts": [
            "The Pillars of Creation are ~4–5 light-years tall, made of cold molecular hydrogen and dust.",
            "Spitzer infrared imaging suggested a supernova ~8,000–9,000 years ago may have already destroyed the pillars — but we won't see it for another ~1,000 years due to light travel time.",
            "JWST's 2022 NIRCam image of the Pillars revealed thousands of newly formed stars invisible at optical wavelengths.",
            "NGC 6611, the embedded star cluster, contains ~460 hot young O and B stars driving the nebula's ionization.",
            "Evaporating Gaseous Globules (EGGs) at pillar tips may contain protostars within years of formation.",
            "The Pillars were formed by a process called 'photoevaporation' — UV radiation boiling away less dense surrounding gas.",
            "The nebula spans ~70 light-years with a central cavity carved by stellar winds from NGC 6611.",
            "M16 is ~5.5 million years old — young enough to have many O-type stars still on the main sequence.",
            "Ground-based Hα images show the nebula glowing with recombination radiation from ionized hydrogen.",
            "Dark 'elephant trunk' pillars similar to M16's are found in other H II regions (e.g., IC 1805).",
        ],
        "did_you_know": [
            "The Hubble 1995 image of M16's Pillars is one of the most reproduced astronomical photographs ever taken.",
            "JWST's version of the same image revealed the Pillars embedded in a much denser cosmic backdrop.",
            "The dense columns protect gas from UV erosion — like sand castles where the tops erode first.",
        ],
        "related_objects": ["Orion Nebula", "Carina Nebula", "NGC 6611", "JWST"],
        "parent_system": "Milky Way — Sagittarius Arm",
        "nasa_reference": "https://www.nasa.gov/image-article/the-pillars-of-creation/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "carina-nebula-ngc3372")),
        "name": "Carina Nebula (NGC 3372)",
        "category": "Nebula",
        "subtype": "Emission/Reflection Nebula — Massive Star Region",
        "tags": ["nebula", "emission-nebula", "massive-stars", "eta-carinae", "star-forming", "southern-sky"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 7500, "unit": "ly"},
            "coordinates": {"ra": "10h 44m 16s", "dec": "-59° 52' 04\""},
            "galaxy_reference": "Milky Way — Carina Arm",
            "diameter": {"value": 300, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 140000, "unit": "solar_masses"},
            "stellar_population": {"value": "14,000+ identified stars"},
        },
        "detailed_description": (
            "The Carina Nebula is one of the largest and brightest nebulae in the Milky Way, "
            "spanning ~300 light-years and visible to the naked eye from the Southern Hemisphere. "
            "It dwarfs the Orion Nebula by every measure: mass, size, and stellar population. "
            "The nebula is home to some of the most massive and luminous stars known, including "
            "Eta Carinae — a binary system with a combined luminosity ~5 million times the Sun's, "
            "expected to explode as a hypernova or supernova imminently (on astronomical timescales). "
            "In 1843, Eta Carinae underwent a 'Great Eruption' that briefly made it the second "
            "brightest star in the sky while ejecting ~10–40 solar masses of material — now visible "
            "as the Homunculus Nebula. JWST's first-year images of the 'Cosmic Cliffs' region in "
            "Carina revealed hundreds of never-before-seen young stars in dusty pillars."
        ),
        "scientific_facts": [
            "The Carina Nebula contains over 65 stars with masses above 50 solar masses — the densest concentration known in the Milky Way.",
            "Eta Carinae is one of the most massive binary stars known, with a combined luminosity ~5 million solar luminosities.",
            "Eta Carinae's 1843 Great Eruption ejected 10–40 solar masses of gas, now visible as the bipolar Homunculus Nebula.",
            "The nebula spans ~300 light-years — ~12.5x larger than the Orion Nebula in linear extent.",
            "JWST's 'Cosmic Cliffs' image of Carina showed pillars of gas and dust backlit by young stars invisible to Hubble.",
            "Carina's multiple massive star clusters (Tr 14, Tr 16) have collectively released enough UV radiation to carve the entire nebula cavity.",
            "The nebula houses WR 25, one of the most luminous single stars known in the galaxy.",
            "Molecular hydrogen (H₂) emission from Carina's pillars was mapped in exquisite detail by JWST MIRI.",
            "Historical records show Eta Carinae was invisible to the naked eye in 1677, rose to magnitude -1 in 1843, then faded again.",
            "Eta Carinae is a prime candidate to be the next visible supernova in the Milky Way.",
        ],
        "did_you_know": [
            "The Carina Nebula is only visible from the Southern Hemisphere — northern observers cannot see it from most latitudes.",
            "Eta Carinae survived its 1843 eruption — 'Supernova Impostor' events like this are poorly understood.",
            "The nebula contains enough gas to form thousands of solar-type stars.",
        ],
        "related_objects": ["Eta Carinae", "Homunculus Nebula", "Orion Nebula", "JWST"],
        "parent_system": "Milky Way — Carina Arm",
        "nasa_reference": "https://www.nasa.gov/image-article/webb-reveals-cosmic-cliffs-sparkling-landscape-of-star-birth/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "ring-nebula-m57")),
        "name": "Ring Nebula (M57)",
        "category": "Nebula",
        "subtype": "Planetary Nebula",
        "tags": ["nebula", "planetary-nebula", "white-dwarf", "Messier", "stellar-death", "Lyra"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 2500, "unit": "ly"},
            "coordinates": {"ra": "18h 53m 35.1s", "dec": "+33° 01' 45\""},
            "galaxy_reference": "Milky Way — Lyra constellation",
            "diameter": {"value": 1.3, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 1.7, "unit": "solar_masses", "note": "Ejected nebular shell"},
            "central_star_temperature": {"value": 120000, "unit": "K"},
            "expansion_rate": {"value": 20, "unit": "km/s"},
        },
        "detailed_description": (
            "The Ring Nebula is one of the most recognizable planetary nebulae — a luminous ring of "
            "gas ejected by a dying Sun-like star now visible as a glowing donut from Earth's vantage "
            "point. The central white dwarf, surface temperature ~120,000 K, floods the expelled "
            "shell with UV radiation, causing it to fluoresce in multiple emission lines. What appears "
            "as a simple ring in small telescopes is revealed by Hubble and JWST to be an incredibly "
            "complex 3D barrel structure: the 'ring' is the waist of a barrel-shaped shell inclined "
            "toward Earth. JWST's 2023 infrared images of M57 revealed never-before-seen details: "
            "concentric rings and arcs in the halo (previous ejections), infrared emission from "
            "molecular hydrogen in the outer ring, and a complex inner structure of knots and filaments."
        ),
        "scientific_facts": [
            "JWST 2023 images revealed ~10 concentric rings in M57's outer halo — each representing a distinct mass ejection.",
            "The Ring Nebula is not a true ring but a barrel-shaped shell seen end-on from Earth.",
            "Its central white dwarf will cool over billions of years, eventually becoming a cold black dwarf.",
            "The nebula expands at ~20 km/s — it will fade into the ISM in ~10,000 years.",
            "M57 was discovered independently by Antoine Darquier de Pellepoix and Charles Messier in 1779.",
            "JWST MIRI detected complex molecular features in M57's outer ring not seen in Hubble UV/optical images.",
            "The white dwarf at M57's center has a companion star — detected spectroscopically — which may have influenced the nebula's shaping.",
            "M57's nitrogen-rich outer shell indicates the progenitor star was enriched by hot-bottom burning during the AGB phase.",
            "Spectroscopy of planetary nebulae like M57 is used to measure oxygen abundance in the Milky Way disk.",
            "The iconic pastel concentric rings in JWST images correspond to 4,000-year-old mass-loss pulses from the AGB phase.",
        ],
        "did_you_know": [
            "At its center, the white dwarf has a diameter similar to Earth but a mass ~0.62 solar masses.",
            "Early astronomers called objects like M57 'planetary nebulae' because they resembled planet disks in small telescopes — but they have no connection to planets.",
            "In ~5 billion years, the Sun may create its own planetary nebula similar to M57.",
        ],
        "related_objects": ["Orion Nebula", "Helix Nebula", "Cat's Eye Nebula", "JWST"],
        "parent_system": "Milky Way",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-57/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "helix-nebula-ngc7293")),
        "name": "Helix Nebula (NGC 7293)",
        "category": "Nebula",
        "subtype": "Planetary Nebula — Nearest to Earth",
        "tags": ["nebula", "planetary-nebula", "nearest", "eye-of-god", "stellar-death", "cometary-knots"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 650, "unit": "ly"},
            "coordinates": {"ra": "22h 29m 38.5s", "dec": "-20° 50' 14\""},
            "galaxy_reference": "Milky Way",
            "diameter": {"value": 2.87, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 0.8, "unit": "solar_masses", "note": "Ejected shell"},
            "central_star_temperature": {"value": 110000, "unit": "K"},
            "cometary_knots": {"value": 20000, "note": "Individually resolved by Hubble"},
        },
        "detailed_description": (
            "The Helix Nebula is the closest planetary nebula to Earth and one of the most complex, "
            "showing multiple overlapping shells from different mass-loss episodes during the "
            "progenitor star's AGB phase. Its nickname 'Eye of God' reflects the haunting appearance "
            "of a giant cosmic iris. The most remarkable feature revealed by Hubble is the population "
            "of ~20,000 'cometary knots' — small, dense globules each about the size of the solar "
            "system, with comet-like tails pointing radially away from the central white dwarf. "
            "These knots form when fast stellar wind overtakes slower previously ejected material, "
            "creating Rayleigh-Taylor instabilities. The Helix spans ~2.87 light-years and requires "
            "a binocular field to see in full, making it the largest apparent-size planetary nebula "
            "in the sky. Spitzer infrared images revealed a disk of warm dust around the central "
            "white dwarf — possibly a debris disk from destroyed Kuiper-Belt-like objects."
        ),
        "scientific_facts": [
            "At 650 light-years, the Helix is the nearest planetary nebula and subtends 2.6° × 1.8° in the sky — larger than the full Moon.",
            "Hubble resolved ~20,000 cometary knots, each with a dense head (~25 AU wide) and a long radial tail.",
            "A Spitzer-detected infrared excess around the Helix white dwarf suggests a debris disk from tidally disrupted planetesimals.",
            "The Helix has at least two overlapping shells from distinct mass-loss events in the AGB phase.",
            "Cometary knot tails may be rich in molecular hydrogen shielded from UV by the dense knot heads.",
            "The central white dwarf (WD 2226-210) has a surface temperature of ~110,000 K and mass ~0.64 solar masses.",
            "The outer halo of the Helix extends far beyond the visible ring — detected only in deep UV and optical exposures.",
            "The Helix expands at ~31 km/s — slower than many other planetary nebulae.",
            "Oxygen-III emission dominates the inner ring; hydrogen-alpha is more prominent in the outer regions.",
            "Total ionized nebular mass of the Helix is ~0.8 solar masses — comparable to the Sun.",
        ],
        "did_you_know": [
            "The Helix Nebula is sometimes called the 'Eye of God' or 'Eye of Sauron' due to its eerie appearance in color-enhanced images.",
            "Cometary knots in the Helix may contain molecular gas protected from the white dwarf's UV by their own dense heads.",
            "The progenitor star that created the Helix was likely a 1–2 solar mass star similar to the Sun.",
        ],
        "related_objects": ["Ring Nebula", "Cat's Eye Nebula", "NGC 7293 white dwarf", "JWST"],
        "parent_system": "Milky Way",
        "nasa_reference": "https://hubblesite.org/contents/media/images/2003/11/1335-Image.html",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "horsehead-nebula-b33")),
        "name": "Horsehead Nebula (Barnard 33)",
        "category": "Nebula",
        "subtype": "Dark Nebula / Absorption Nebula",
        "tags": ["nebula", "dark-nebula", "absorption", "Orion", "pillar", "IC434"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 1375, "unit": "ly"},
            "coordinates": {"ra": "05h 40m 59s", "dec": "-02° 27' 30\""},
            "galaxy_reference": "Milky Way — Orion Molecular Cloud",
            "height": {"value": 1, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 2.7, "unit": "solar_masses"},
            "temperature": {"dense_core": {"value": 10, "unit": "K"}},
        },
        "detailed_description": (
            "The Horsehead Nebula is one of the most recognizable astronomical objects — a dark, "
            "horse-head-shaped pillar of dense cold gas and dust silhouetted against the glowing "
            "pink emission nebula IC 434. It is a dense condensation within the Orion Molecular "
            "Cloud that is being slowly eroded by ultraviolet radiation from the bright star "
            "Sigma Orionis nearby. The dark nebula is a region of molecular hydrogen at ~10 K, "
            "too cold and dense for starlight to penetrate — casting a shadow against the bright "
            "background nebula. Young stars have been detected forming within the Horsehead's "
            "dense interior. JWST's 2023 images at infrared wavelengths revealed the nebula in "
            "a completely new light: translucent at near-infrared wavelengths, showing internal "
            "structure, star-forming cores, and the glowing photodissociation region at its "
            "eroding surface — invisible to Hubble's optical cameras."
        ),
        "scientific_facts": [
            "JWST 2023 near-infrared images of the Horsehead revealed translucent filaments and internal structure invisible to Hubble.",
            "The Horsehead is a photodissociation region (PDR) — its surface is illuminated by UV from Sigma Orionis.",
            "It was first recorded by Williamina Fleming in 1888 while examining photographic plates from the Harvard College Observatory.",
            "The Horsehead will erode away in ~5 million years as UV radiation gradually destroys the molecular gas.",
            "Dense cores embedded within the Horsehead are potential sites of ongoing low-mass star formation.",
            "The bright region immediately below the Horsehead is NGC 2023, an infrared-bright reflection nebula.",
            "Carbon monoxide (CO) and other molecular species have been detected throughout the Horsehead's interior.",
            "The nebula's head-like shape is maintained by differential erosion — denser regions survive longer than less dense ones.",
            "Polycyclic aromatic hydrocarbons (PAHs) detected on the Horsehead's surface by JWST represent complex organics.",
            "The ionized surface of the Horsehead glows at ~10,000 K while the interior is at ~10 K — a 1,000x temperature contrast across a thin layer.",
        ],
        "did_you_know": [
            "The Horsehead is part of the same molecular cloud complex as the Orion Nebula — just 50 light-years away from M42.",
            "JWST's 2023 Horsehead image was selected as one of the ESA JWST Early Release Science highlights.",
            "The shape is coincidental — in 5 million years it will be completely eroded and unrecognizable.",
        ],
        "related_objects": ["Orion Nebula", "Flame Nebula", "IC 434", "Sigma Orionis", "JWST"],
        "parent_system": "Orion Molecular Cloud Complex",
        "nasa_reference": "https://esawebb.org/news/weic2307/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "lagoon-nebula-m8")),
        "name": "Lagoon Nebula (M8)",
        "category": "Nebula",
        "subtype": "Emission Nebula — H II Region",
        "tags": ["nebula", "emission-nebula", "star-forming", "Messier", "HII-region", "Sagittarius"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 4100, "unit": "ly"},
            "coordinates": {"ra": "18h 03m 37s", "dec": "-24° 23' 12\""},
            "galaxy_reference": "Milky Way — Sagittarius",
            "diameter": {"value": 110, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 10000, "unit": "solar_masses"},
            "temperature": {"ionized_gas": {"value": 9000, "unit": "K"}},
        },
        "detailed_description": (
            "The Lagoon Nebula is one of only two star-forming nebulae visible to the naked eye "
            "from Earth's mid-latitudes (the other being the Orion Nebula). At ~110 light-years "
            "across, it is significantly larger than M42 and contains multiple distinct components: "
            "an H II region ionized by the young star cluster NGC 6530, a dark lane ('the lagoon') "
            "that bisects the nebula, and a central hourglass-shaped region of intense activity "
            "around the massive star Herschel 36. Tornadoes — twisted, rotating columns of gas "
            "hundreds of astronomical units long — have been photographed in the Lagoon, generated "
            "by temperature differentials between hot star-heated surfaces and cold molecular gas. "
            "The nebula is the active H II face of a much larger, cold molecular cloud."
        ),
        "scientific_facts": [
            "The Lagoon Nebula is one of only two H II regions visible to the naked eye from mid-northern latitudes (with Orion).",
            "The 'hourglass' region around Herschel 36 shows intense ongoing star formation driven by the star's UV radiation.",
            "Hubble images revealed 'tornadoes' — rotating gas columns several hundred AU long — within M8.",
            "NGC 6530, the embedded star cluster, is only ~2 million years old — exceptionally young.",
            "Herschel 36, the nebula's most luminous ionizing star, has a mass of ~32 solar masses.",
            "M8 spans ~4° × 2° in the sky — roughly 8x the full Moon's diameter at its widest.",
            "The dark 'lagoon' lane is a dense molecular cloud in silhouette against the bright H II region.",
            "Collimated Herbig-Haro jets have been detected emerging from young stellar objects embedded in M8.",
            "At 4,100 light-years, M8 is farther than M42 but bright enough to be a naked-eye object.",
            "The molecular cloud behind M8 extends to connect with the neighboring Trifid Nebula (M20).",
        ],
        "did_you_know": [
            "The Lagoon Nebula can be seen without a telescope on a dark night — look in Sagittarius near the Teapot asterism.",
            "The 'tornadoes' photographed by Hubble in M8 are hot tubes of gas rotated by thermal wind shear.",
            "M8 and the nearby Trifid Nebula (M20) are part of the same larger star-forming complex.",
        ],
        "related_objects": ["Trifid Nebula", "Orion Nebula", "NGC 6530", "Herschel 36"],
        "parent_system": "Milky Way — Sagittarius Arm",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-8/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "butterfly-nebula-ngc6302")),
        "name": "Butterfly Nebula (NGC 6302)",
        "category": "Nebula",
        "subtype": "Bipolar Planetary Nebula",
        "tags": ["nebula", "planetary-nebula", "bipolar", "extreme-star", "butterfly-wings", "ultraviolet"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 3800, "unit": "ly"},
            "coordinates": {"ra": "17h 13m 44.2s", "dec": "-37° 06' 16\""},
            "galaxy_reference": "Milky Way — Scorpius",
            "wingspan": {"value": 2, "unit": "ly"},
        },
        "physical": {
            "central_star_temperature": {"value": 250000, "unit": "K", "note": "One of the hottest stellar remnants known"},
            "gas_velocity": {"value": 300, "unit": "km/s"},
        },
        "detailed_description": (
            "NGC 6302, the Butterfly Nebula, is one of the most structurally complex and extreme "
            "planetary nebulae known. Its two lobes — resembling butterfly wings — span ~2 "
            "light-years and are expanding at ~300 km/s, one of the highest velocities known in "
            "any planetary nebula. At its center sits one of the hottest stellar remnants known: "
            "a white dwarf with a surface temperature of ~250,000 K — nearly 50x hotter than our "
            "Sun. This ultraviolet powerhouse floods the bipolar lobes with ionizing radiation, "
            "exciting sulfur, nitrogen, oxygen, and other elements into emission. The waist of "
            "the nebula is constricted by a dense torus of gas and dust that funnels material "
            "into the two jets creating the butterfly shape. Hubble's 2009 refurbishment imaging "
            "of NGC 6302 revealed intricate structures including clumps, jets, and multiple shell "
            "ejection episodes recorded in the morphology."
        ),
        "scientific_facts": [
            "The central white dwarf of NGC 6302 has a surface temperature of ~250,000 K — one of the hottest known.",
            "Gas in the butterfly lobes travels at ~300 km/s — among the highest velocities in any planetary nebula.",
            "The equatorial torus contains calcium, iron, nickel, and chromium — an unusually rich heavy element composition.",
            "Hubble's 2009 upgraded WFC3 images of NGC 6302 were among the first released after Servicing Mission 4.",
            "The bipolar shape results from mass ejected preferentially along the polar axes due to the equatorial torus confinement.",
            "Multiple episodes of mass loss at different velocities are recorded in the lobe structure.",
            "NGC 6302 is classified as a 'type II' bipolar planetary nebula — showing nitrogen and sulfur enrichment.",
            "Molecular hydrogen (H₂) emission traces cool gas surviving in the outer extremities of the lobes.",
            "The progenitor star had an initial mass of ~3–5 solar masses — intermediate mass stars produce the most extreme PNe.",
            "The nebula emits strongly in ultraviolet, optical, and infrared — a broadband emitter.",
        ],
        "did_you_know": [
            "The Butterfly Nebula is one of the most photographed objects from Hubble's refurbishment observations in 2009.",
            "Despite its delicate appearance, gas in the butterfly wings moves at 1 million km/h.",
            "The central star is so hot it was not directly detected until careful infrared observations — it is hidden behind the equatorial dust torus.",
        ],
        "related_objects": ["Ring Nebula", "Helix Nebula", "Cat's Eye Nebula", "Hubble Space Telescope"],
        "parent_system": "Milky Way",
        "nasa_reference": "https://hubblesite.org/contents/media/images/2009/25/2607-Image.html",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "trifid-nebula-m20")),
        "name": "Trifid Nebula (M20)",
        "category": "Nebula",
        "subtype": "Emission, Reflection, and Dark Nebula composite",
        "tags": ["nebula", "emission-nebula", "reflection-nebula", "dark-nebula", "Messier", "Sagittarius"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 4100, "unit": "ly"},
            "coordinates": {"ra": "18h 02m 23s", "dec": "-22° 58' 18\""},
            "galaxy_reference": "Milky Way",
            "diameter": {"value": 40, "unit": "ly"},
        },
        "physical": {
            "mass": {"value": 7000, "unit": "solar_masses"},
        },
        "detailed_description": (
            "The Trifid Nebula is unique in showing three distinct types of nebula simultaneously "
            "within a single field: an emission nebula (the pink H II region ionized by the central "
            "O-type star HD 164492A), a reflection nebula (the blue region to the north where "
            "dust reflects starlight), and three dark lanes of absorbing dust that divide the "
            "emission region into three lobes — giving the nebula its name (Latin: trifidus, divided "
            "into three). The dark lanes are dense molecular filaments at much lower temperatures "
            "than the surrounding ionized gas. Hubble imaging of M20 showed protostars and "
            "evaporating protostellar jets emerging from condensations in the dark lanes, "
            "caught in the act of formation while being photo-eroded by the central star's radiation."
        ),
        "scientific_facts": [
            "M20 displays all three major nebula types — emission, reflection, and dark — simultaneously in one field.",
            "Hubble detected stellar jets from protostars in M20's dark lanes — young stars caught mid-formation.",
            "The central ionizing source, HD 164492A, is a massive O7.5-type star with a surface temperature of ~36,000 K.",
            "The reflection nebula (blue) lies north of the emission nebula (pink) — the two are distinct regions.",
            "M20 and the nearby Lagoon Nebula (M8) are part of the same star-forming complex 4,100 light-years away.",
            "Dark globules in M20's lanes are called 'proplyds' or protostellar condensations being eroded from outside.",
            "M20 is only ~300,000 years old in its current ionized state — a very young H II region.",
            "Infrared observations reveal more embedded young stellar objects than visible-light images suggest.",
            "Charles Messier recorded M20 in 1764; its true trifid nature was only apparent in later photographs.",
            "The division of emission lobes is caused by dust lanes that absorb the nebular emission rather than being physical gaps.",
        ],
        "did_you_know": [
            "M20 is sometimes called the 'three-lobe nebula' — its dust lanes divide it into three petal-like sections.",
            "The colors visible in photographs of M20 encode three physical processes: ionization (red), scattering (blue), and absorption (dark lanes).",
            "At 4,100 light-years, M20 is close enough to show individual protostars in Hubble images.",
        ],
        "related_objects": ["Lagoon Nebula", "Orion Nebula", "Eagle Nebula"],
        "parent_system": "Milky Way — Sagittarius",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-20/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cats-eye-nebula-ngc6543")),
        "name": "Cat's Eye Nebula (NGC 6543)",
        "category": "Nebula",
        "subtype": "Planetary Nebula — Highly Structured",
        "tags": ["nebula", "planetary-nebula", "complex-structure", "Chandra", "Hubble", "halo"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 3262, "unit": "ly"},
            "coordinates": {"ra": "17h 58m 33.4s", "dec": "+66° 37' 59\""},
            "galaxy_reference": "Milky Way",
            "diameter": {"value": 0.5, "unit": "ly", "note": "Inner bright region; outer halo ~3 ly"},
        },
        "physical": {
            "central_star_temperature": {"value": 80000, "unit": "K"},
            "expansion_rate": {"value": 16, "unit": "km/s"},
            "x_ray_luminosity": {"note": "One of the brightest X-ray planetary nebulae"},
        },
        "detailed_description": (
            "NGC 6543 is one of the most structurally complex planetary nebulae, displaying a "
            "dazzling array of concentric rings, jets, knots, and filaments in its inner bright "
            "shell — and an enormous, faint outer halo of multiple shells extending ~3 light-years. "
            "Discovered by William Herschel in 1786, it was the first nebula to have its spectrum "
            "recorded (1864, William Huggins), revealing it to be a gas cloud rather than unresolved "
            "stars. Chandra X-ray Observatory images show hot shocked gas at the center — a bubble "
            "of million-degree plasma inflated by the fast stellar wind from the central star "
            "colliding with slower, denser gas ejected earlier. The Cat's Eye is a 'point-symmetric' "
            "nebula: its structure shows rotational symmetry suggestive of precessing jets from a "
            "binary central star system. HST imaging revealed 11 concentric rings in the outer halo — "
            "each representing a separate mass-loss pulse ~1,500 years apart."
        ),
        "scientific_facts": [
            "NGC 6543 was the first nebula to have its spectrum measured (1864), proving it was gas not stars.",
            "Chandra X-ray images reveal a central hot bubble (~1.7 million K) of shocked stellar wind gas.",
            "HST resolved 11 concentric outer shells — each separated by ~1,500 years of AGB mass loss.",
            "The nebula's point-symmetric structure implies a binary or precessing-jet central system.",
            "The central star's fast wind (~200 km/s) drives the internal shock structure visible in X-rays.",
            "Multiple supersonic jets at different position angles indicate episodic collimated outflows.",
            "The outer halo is far older (~10,000+ years) than the bright inner region (~1,000 years).",
            "NGC 6543 is a benchmark target for nebular abundance analysis and stellar evolution theory.",
            "Oxygen and nitrogen abundances in the Cat's Eye indicate an intermediate-mass progenitor star.",
            "Radio continuum observations trace free-free emission from ionized gas consistent with the optical structure.",
        ],
        "did_you_know": [
            "William Huggins's 1864 spectrum of NGC 6543 sparked the field of emission nebula spectroscopy.",
            "The Cat's Eye gets its name from its colorful, iris-like appearance in Hubble images.",
            "The 11 concentric rings around the Cat's Eye suggest the progenitor star had regular thermal pulse cycles every 1,500 years.",
        ],
        "related_objects": ["Ring Nebula", "Helix Nebula", "Butterfly Nebula", "Hubble Space Telescope"],
        "parent_system": "Milky Way",
        "nasa_reference": "https://www.nasa.gov/image-article/cats-eye-nebula-revisited/",
    },


    # -------------------------------------------------------------------------
    # SECTION 5: NEUTRON STARS & EXOTIC STELLAR OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "crab-pulsar-b0531")),
        "name": "Crab Pulsar (PSR B0531+21)",
        "category": "Neutron Star",
        "subtype": "Pulsar — Young Energetic Pulsar",
        "tags": ["neutron-star", "pulsar", "supernova-remnant", "crab-nebula", "high-energy", "rotation"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 6523, "unit": "ly"},
            "coordinates": {"ra": "05h 34m 31.97s", "dec": "+22° 00' 52.1\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses", "note": "Typical neutron star mass"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 33.085, "unit": "ms"},
            "period_derivative": {"value": 4.2e-13, "unit": "s/s"},
            "spin_down_luminosity": {"value": 4.6e31, "unit": "W"},
            "magnetic_field": {"value": 3.8e8, "unit": "T"},
            "surface_temperature": {"value": 1.6e6, "unit": "K"},
            "age": {"value": 971, "unit": "years", "note": "True age; characteristic age ~1240 years"},
        },
        "detailed_description": (
            "The Crab Pulsar is the neutron star born in the supernova explosion of 1054 AD, now spinning "
            "at 30.2 revolutions per second and beaming two narrow cones of electromagnetic radiation "
            "like a lighthouse. It is one of the most energetic pulsars known — releasing ~4.6×10³¹ "
            "watts of rotational kinetic energy per second as radiation, particles, and the pulsar wind "
            "that powers the Crab Nebula. The pulsar is surrounded by a dynamic wind nebula: a toroidal "
            "termination shock, polar jets, and rapidly variable structures called 'wisps' that appear "
            "and brighten on timescales of days. The Crab Pulsar was pivotal in establishing the "
            "neutron star interpretation of pulsars — its young age, supernova connection, and known "
            "distance made it the Rosetta Stone of pulsar physics. Its pulses are detected from radio "
            "through gamma-ray wavelengths, making it a broadband cosmic beacon. The magnetic field at "
            "the surface is ~3.8×10⁸ Tesla — roughly 10¹² times Earth's magnetic field — and drives the "
            "relativistic particle wind. Periodically the pulsar exhibits 'glitches' — sudden spin-ups "
            "of up to 1 part in 10⁸ — interpreted as stress-induced fractures in the neutron star's "
            "crust suddenly coupling angular momentum from the superfluid interior to the crust."
        ),
        "scientific_facts": [
            "The Crab Pulsar's 33 ms period places it in the class of 'classical' (non-recycled) pulsars.",
            "It emits pulses at optical wavelengths — one of only a handful of pulsars visible with ground-based telescopes.",
            "Pulsar glitches are interpreted as avalanche-like transfer of angular momentum from a superfluid neutron interior to the crust.",
            "The spin-down rate (period increasing by 38 ns/day) directly measures the magnetic dipole radiation energy loss.",
            "Gamma-ray pulses from the Crab detected by Fermi LAT provide tests of magnetospheric emission models.",
            "Its characteristic age (P/2Ṗ) gives ~1,240 years — slightly older than the true 971-year age due to initial fast spin.",
            "The pulsar has served as a calibration target for nearly every major X-ray and gamma-ray telescope since 1971.",
            "The Crab's optical pulsations were the first discovered for any pulsar (1969, Steward Observatory).",
        ],
        "did_you_know": [
            "The surface gravity of the Crab Pulsar is ~2×10¹¹ times Earth's — a 70 kg person would weigh 14 quadrillion kg there.",
            "A sugar-cube volume of neutron star material would weigh ~100 million metric tons on Earth.",
            "The Crab Pulsar is slowly but measurably slowing: in ~100,000 years its spin rate will have halved.",
        ],
        "formation_process": (
            "When the progenitor star's iron core exceeded the Chandrasekhar mass limit in 1054 AD, "
            "gravity overcame electron degeneracy pressure and the core collapsed in ~0.1 seconds. "
            "The core compressed from ~Earth size to ~10 km, with density exceeding nuclear density. "
            "Neutron degeneracy pressure halted collapse, and the infalling outer layers bounced, "
            "producing a supernova. The newly formed proto-neutron star shed ~99% of the gravitational "
            "energy as a neutrino burst (~3×10⁴⁶ J in seconds), then cooled over thousands of years."
        ),
        "future_evolution": (
            "The Crab Pulsar will continue to spin down over millions of years. Its pulsar wind will "
            "gradually weaken as rotational energy depletes. The Crab Nebula it powers will merge "
            "into the interstellar medium in ~10,000 years, leaving the pulsar as an isolated, slowly "
            "rotating radio pulsar. Eventually it will cross the pulsar 'death line' — where its "
            "electric field can no longer accelerate particles — and become radio-silent."
        ),
        "related_objects": ["Crab Nebula (M1)", "SN 1054", "Vela Pulsar", "Neutron Star"],
        "parent_system": "Crab Nebula / Milky Way",
        "child_objects": ["Crab Pulsar Wind Nebula"],
        "nasa_reference": "https://www.nasa.gov/image-article/crab-nebula/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "vela-pulsar-b0833")),
        "name": "Vela Pulsar (PSR B0833-45)",
        "category": "Neutron Star",
        "subtype": "Pulsar — Young, Nearby Pulsar",
        "tags": ["neutron-star", "pulsar", "nearby", "vela-supernova-remnant", "gamma-ray", "young"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 959, "unit": "ly"},
            "coordinates": {"ra": "08h 35m 20.6s", "dec": "-45° 10' 35\""},
            "galaxy_reference": "Milky Way — Vela constellation",
        },
        "physical": {
            "mass": {"value": 1.33, "unit": "solar_masses"},
            "radius": {"value": 11.4, "unit": "km"},
            "rotation_period": {"value": 89.3, "unit": "ms"},
            "period_derivative": {"value": 1.24e-13, "unit": "s/s"},
            "spin_down_luminosity": {"value": 6.8e31, "unit": "W"},
            "magnetic_field": {"value": 3.4e8, "unit": "T"},
            "surface_temperature": {"value": 1.2e6, "unit": "K"},
            "age": {"value": 11300, "unit": "years", "characteristic_age": "11,300 years"},
        },
        "detailed_description": (
            "The Vela Pulsar is the second-brightest gamma-ray source in the sky and one of the nearest "
            "known pulsar remnants at ~959 light-years. It is a young pulsar (~11,300 years old) born "
            "in the Vela supernova, a core-collapse explosion visible from Earth even in daylight ~11,000 "
            "years ago. The pulsar rotates 11 times per second (89.3 ms period), slower than the Crab but "
            "still energetic, with a spin-down luminosity of ~6.8×10³¹ watts — comparable to the Crab. "
            "The Vela Pulsar is a prolific gamma-ray emitter detected by Fermi LAT and a spectacular "
            "X-ray source. Its wind nebula is the Vela Pulsar Wind Nebula (PWN), a complex structure with "
            "jets and a toroidal shock. Vela's proximity and well-characterized properties make it an "
            "important calibration source for pulsar emission models. The Vela jets show evidence of "
            "precession — slow wobbling of the jet axis over thousands of years — providing rare insights "
            "into pulsar spin and magnetic field geometry."
        ),
        "scientific_facts": [
            "Vela is one of the brightest pulsar wind nebulae in the sky at X-ray and gamma-ray wavelengths.",
            "The Vela supernova explosion 11,300 years ago was visible in broad daylight from Earth.",
            "At 959 light-years, Vela is among the nearest known young pulsar remnants.",
            "The pulsar exhibits glitches similar to the Crab, though less frequently and with smaller amplitudes.",
            "Vela's wind nebula shows clear evidence of precessing jets — the axis wobbles with a period of ~6,000 years.",
            "The pulsar's magnetic field (~3.4×10⁸ T) is slightly weaker than the Crab's, allowing slightly longer pulsar lifetimes.",
            "Fermi LAT gamma-ray light curves show complex modulation correlated with the pulsar's spin.",
            "The Vela PWN is expanding at ~10,000 km/s, dissipating its energy into the surrounding supernova remnant.",
            "Point-source measurements of Vela provide essential constraints on neutron star cooling models.",
            "Radio pulsations from Vela show orthogonal polarization in different frequency bands — evidence of multi-pole emission.",
        ],
        "did_you_know": [
            "Vela's explosion 11,300 years ago coincided with the early Neolithic period — possibly visible to ancient humans in Australia.",
            "The Vela PWN is resolvable into fine structure through milliarcsecond VLBI observations — one of the most detailed pulsar jet images.",
            "Light from the Vela Pulsar takes 959 years to reach Earth — it has been spinning for millennia before its light reaches us.",
        ],
        "formation_process": (
            "The Vela progenitor was a massive star (~17–20 solar masses) that underwent core collapse "
            " ~11,300 years ago. The supernova explosion ejected the star's outer layers while the "
            "core collapsed into a neutron star. The young, rapidly rotating proto-neutron star neutrino "
            "cooled and formed the Vela Pulsar we observe today."
        ),
        "future_evolution": (
            "The Vela Pulsar will continue to spin down at a rate ~30x slower than the Crab, taking "
            "~100 million years to reach the pulsar death line. Its wind nebula will gradually fade as it "
            "merges with the surrounding supernova remnant. Eventually, Vela will become a dim, cold neutron star."
        ),
        "related_objects": ["Crab Pulsar", "Vela Supernova Remnant", "Puppis A", "Neutron Stars"],
        "parent_system": "Vela Supernova Remnant / Milky Way",
        "child_objects": ["Vela Pulsar Wind Nebula"],
        "nasa_reference": "https://www.nasa.gov/image-article/vela-pulsar/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "psr-j0437-4715")),
        "name": "PSR J0437-4715 (Millisecond Pulsar)",
        "category": "Neutron Star",
        "subtype": "Millisecond Pulsar — Recycled, Binary",
        "tags": ["neutron-star", "millisecond-pulsar", "binary", "recycled", "nearby", "timing-array"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 610, "unit": "ly"},
            "coordinates": {"ra": "04h 37m 15.8s", "dec": "-47° 15' 09\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.76, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 5.757, "unit": "ms", "note": "175 spins per second"},
            "spin_down_luminosity": {"value": 8e29, "unit": "W", "note": "Low; old recycled pulsar"},
            "magnetic_field": {"value": 1.8e8, "unit": "T", "note": "Weaker than young pulsars"},
            "companion": {"type": "White dwarf", "mass": 0.2, "orbital_period": {"value": 5.5, "unit": "hours"}},
        },
        "detailed_description": (
            "PSR J0437-4715 is the closest known millisecond pulsar at only 610 light-years, and the "
            "brightest millisecond pulsar in the sky — properties that make it a cornerstone calibration "
            "source for pulsar astronomy. It is a 'recycled' pulsar: originally a slowly spinning neutron "
            "star, it was spun up to extreme rotation (175 times per second, 5.757 ms period) by accretion "
            "of material from a companion star over millions of years. Now isolated, the companion is a "
            "low-mass white dwarf in a 5.5-hour orbit. The pulsar's strong, precisely measurable radio "
            "signal is affected by interstellar dispersion, magnetic lensing, and general relativistic "
            "effects in its close orbit — effects that can be measured and used to test relativity. PSR "
            "J0437-4715 is part of pulsar timing array experiments that use millisecond pulsars as cosmic "
            "clocks to detect nanohertz-frequency gravitational waves from supermassive black hole binaries "
            "in distant galaxies. Its proximity and stability make it an essential anchor for gravitational "
            "wave detection."
        ),
        "scientific_facts": [
            "PSR J0437-4715 has among the best-measured masses of any binary pulsar via Shapiro delay — a general relativistic effect.",
            "Its companion white dwarf is the result of the original companion's evolution after it was stripped of its envelope.",
            "Timing residuals from PSR J0437-4715 help constrain the pulsar timing array's ability to detect gravitational waves.",
            "The pulsar's weak spin-down luminosity (~8×10²⁹ W) indicates it is an old, recycled system.",
            "Dispersion measure studies of PSR J0437-4715 provide constraints on interstellar electron density models.",
            "The binary's orbital period of 5.5 hours allows multiple transits across Earth's line of sight per day.",
            "Optical observations have directly detected the white dwarf companion star — rare for pulsar binaries.",
            "Proper motion measurements place the pulsar in a young stellar association despite its old appearance.",
        ],
        "did_you_know": [
            "A millisecond pulsar rotates so quickly that points on its equator move at ~10-20% the speed of light.",
            "PSR J0437-4715 is considered the '20 cm reference standard' for pulsar observations.",
            "Without millisecond pulsars like PSR J0437, pulsar timing arrays could not detect gravitational waves from merging supermassive black holes.",
        ],
        "formation_process": (
            "PSR J0437-4715 formed as a neutron star billions of years ago in a close binary with a "
            "main-sequence star. Over time, the companion expanded into a red giant and filled its Roche "
            "lobe, transferring material onto the neutron star's surface. This mass accretion spun the "
            "neutron star up to millisecond periods over ~1 billion years. When the companion exhausted "
            "its hydrogen, it became a white dwarf and mass accretion ceased."
        ),
        "future_evolution": (
            "PSR J0437-4715 will continue to slowly spin down on billion-year timescales, eventually "
            "reaching the pulsar death line where it can no longer emit coherent pulsar radiation. The "
            "white dwarf companion will cool toward absolute zero over trillions of years."
        ),
        "related_objects": ["PSR J1909-3744", "Millisecond pulsars", "Pulsar timing arrays", "Gravitational waves"],
        "parent_system": "Milky Way",
        "child_objects": ["White dwarf companion"],
        "nasa_reference": "https://pulsars.nanograv.org",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "geminga-psr")),
        "name": "Geminga (PSR J0633+1746)",
        "category": "Neutron Star",
        "subtype": "Pulsar — Nearby Isolated Pulsar",
        "tags": ["neutron-star", "pulsar", "nearby", "X-ray", "nearby-supernova-remnant", "quiet"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 815, "unit": "ly"},
            "coordinates": {"ra": "06h 33m 54.2s", "dec": "+17° 46' 13\""},
            "galaxy_reference": "Milky Way — Gemini constellation",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 12.4, "unit": "km"},
            "rotation_period": {"value": 237, "unit": "ms", "note": "~4 spins per second"},
            "surface_temperature": {"value": 4e5, "unit": "K", "note": "Cooler than younger pulsars"},
            "magnetic_field": {"value": 1e8, "unit": "T"},
            "age": {"value": 3.4e5, "unit": "years", "note": "~340,000 years old"},
        },
        "detailed_description": (
            "Geminga (whose name derives from 'Gamma-ray source in Gemini') is one of the nearest known "
            "young pulsars, located at approximately 815 light-years in the constellation Gemini. It is "
            "notably young at ~340,000 years old — in fact, slightly younger than the Crab Pulsar despite "
            "having a longer spin period (237 ms vs Crab's 33 ms). This apparent contradiction is explained "
            "by Geminga's lower magnetic field (~10⁸ T), which allows it to age more slowly. Geminga is "
            "historically significant as the second brightest gamma-ray source in the sky when discovered "
            "by the COS-B gamma-ray satellite in 1972. Despite a relatively 'empty' supernova remnant "
            "(no bright radio nebula), Geminga is a prolific X-ray and gamma-ray emitter with emission "
            "from a large, bow-shock-shaped pulsar wind nebula. The pulsar is moving through space at "
            "~18 km/s, continuously sweeping up a bow-shaped shock wave of interstellar gas. Recent "
            "observations suggest Geminga may be on the verge of transitioning to the 'pulsar death' "
            "regime — its magnetic field decay may already be underway."
        ),
        "scientific_facts": [
            "Geminga was one of the first sources identified via its gamma-ray emission alone, making it a landmark discovery.",
            "Despite being ~340,000 years old, Geminga is still energetic — comparable to pulsars twice its age.",
            "The pulsar's low magnetic field (~10⁸ T) means it loses rotational energy much more slowly than higher-field pulsars.",
            "Geminga's bow-shock wind nebula is visible in X-rays — it resembles a comet's tail as the pulsar plows through the ISM.",
            "The pulsar may be transitioning to the 'death zone' where emission ceases — one of the oldest pulsars still actively emitting.",
            "Proper motion measurements show Geminga is moving at ~18 km/s, carrying its wind nebula bow-shock.",
            "X-ray and gamma-ray light curves show pulsed emission with different profiles — indicating complex magnetospheric geometry.",
            "Fermi LAT observations of Geminga's gamma-ray emission constrain pulsed emission models for millisecond-spin rotation."
        ],
        "did_you_know": [
            "Geminga means 'there is nothing' in Italian slang — fitting given its isolated, quiet supernova remnant.",
            "The pulsar's bow-shock is a rare morphology — most pulsars either sit within wind nebulae or lack detectable nebulae.",
            "Geminga may represent a brief 'twilight' phase of pulsar evolution as it approaches the death line.",
        ],
        "formation_process": (
            "Geminga formed from core collapse of a massive star ~340,000 years ago. The explosion created "
            "the neutron star and initially bright supernova remnant. Unlike most supernova remnants, "
            "Geminga's SN remnant is weak and diffuse — possibly due to an asymmetric explosion or low "
            "ambient interstellar density."
        ),
        "future_evolution": (
            "Geminga is approaching the pulsar death line and may silence its radio emission within the "
            "next ~100,000–1,000,000 years. Its gamma-ray and X-ray emission may persist slightly longer "
            "due to lower-frequency thresholds. Eventually it will become a barely detectable, cold neutron star."
        ),
        "related_objects": ["Vela Pulsar", "Crab Pulsar", "Bow-shock nebulae", "Pulsars approaching death"],
        "parent_system": "Milky Way",
        "child_objects": ["Pulsar Wind Nebula (bow-shock)"],
        "nasa_reference": "https://www.nasa.gov/mission/fermi/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "psr-b1919-plus-21")),
        "name": "PSR B1919+21 (First Discovered Pulsar)",
        "category": "Neutron Star",
        "subtype": "Pulsar — Historic Discovery",
        "tags": ["neutron-star", "pulsar", "first-pulsar", "historic", "binary", "recycled"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 2200, "unit": "ly"},
            "coordinates": {"ra": "19h 21m 44.8s", "dec": "+21° 53' 02\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.44, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 1337.5, "unit": "ms", "note": "~0.75 spins per second"},
            "spin_down_luminosity": {"value": 7.5e30, "unit": "W"},
            "magnetic_field": {"value": 4.1e8, "unit": "T"},
            "companion": {"type": "White dwarf", "orbital_period": "11.6 hours"},
        },
        "detailed_description": (
            "PSR B1919+21 holds the distinction of being the first pulsar ever discovered, identified on "
            "August 6, 1967, by Jocelyn Bell Burnell and Antony Hewish at Cambridge University. The regular "
            "pulses were so precise that Bell initially coded them 'LGM-1' (Little Green Men), suspecting "
            "extraterrestrial transmission before realizing the celestial origin. This discovery revolutionized "
            "astrophysics, earning Hewish and Martin Ryle the 1974 Nobel Prize in Physics (controversially "
            "without crediting Bell). PSR B1919+21 is a binary pulsar in an 11.6-hour orbit with a white "
            "dwarf companion — likely a recycled system where past mass accretion spun the neutron star to "
            "millisecond periods before the companion evolved. With a slow 1.337-second rotation period, it "
            "is no longer a millisecond pulsar, but its historical significance and well-characterized properties "
            "make it a reference standard. The pulsar has been continuously monitored for over 50 years, providing "
            "invaluable data on long-term pulsar stability and relativistic effects in binary systems."
        ),
        "scientific_facts": [
            "Discovery of PSR B1919+21 on August 6, 1967, marked the birth of pulsar astronomy.",
            "The regularity of its pulses was so precise that astronomers initially suspected intelligent extraterrestrial signals.",
            "Jocelyn Bell Burnell's role in the discovery, though credited by scientific community retrospectively, was initially underrecognized.",
            "Continuous monitoring since 1967 has tracked its long-term spin-down — the baseline for pulsar aging studies.",
            "The pulsar's companion white dwarf has been optically detected — one of few pulsar companions resolved directly.",
            "Post-Keplerian parameters measured in the binary system provide tests of general relativity in strong-field regimes.",
            "The system has been searched for planetary companions — an early exoplanet search program around pulsars.",
            "Its proximity to a recycling white dwarf suggests past accretion-driven spin-up, then gravitational radiation ejection.",
            "PSR B1919+21 served as the template for searching for new pulsars after its discovery.",
            "The pulsar's timing stability enabled early tests of fundamental physics (equivalence principle, etc.).",
        ],
        "did_you_know": [
            "Jocelyn Bell Burnell was a graduate student when she discovered the first pulsar — her contribution is commemorated in her name.",
            "The 'LGM' designation ('Little Green Men') is still used informally in some pulsar search programs.",
            "PSR B1919+21's discovery launched an entire subfield of astronomy — pulsars are now among the most useful cosmic tools.",
        ],
        "formation_process": (
            "PSR B1919+21 formed as a neutron star from core collapse of a massive progenitor star millions "
            "of years ago. It was subsequently spun up to millisecond periods by mass accretion from a "
            "companion. When the companion became a white dwarf and mass transfer ceased, the neutron star "
            "began spinning down — the state we observe today."
        ),
        "future_evolution": (
            "PSR B1919+21 will continue slow spin-down over billions of years, eventually reaching the pulsar "
            "death line. Its white dwarf companion will cool on trillion-year timescales. The binary may "
            "merge via gravitational wave emission ~10¹⁶ years in the distant future."
        ),
        "related_objects": ["PSR J0437-4715", "First pulsars discovered", "Jocelyn Bell Burnell", "Nobel Prize"],
        "parent_system": "Milky Way",
        "child_objects": ["White dwarf companion"],
        "nasa_reference": "https://science.nasa.gov/universe/neutron-stars-and-pulsars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "double-pulsar-j0737")),
        "name": "Double Pulsar (PSR J0737-3039)",
        "category": "Neutron Star",
        "subtype": "Binary Pulsar — Both Stars Pulsars",
        "tags": ["neutron-star", "pulsar", "binary-pulsar", "double-pulsar", "gravitational-waves", "relativistic"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 2200, "unit": "ly"},
            "coordinates": {"ra": "07h 37m 51.3s", "dec": "-30° 39' 40\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "pulsar_a": {
                "mass": {"value": 1.3381, "unit": "solar_masses"},
                "rotation_period": {"value": 22.7, "unit": "ms"},
                "spin_down_luminosity": {"value": 7.8e31, "unit": "W"},
            },
            "pulsar_b": {
                "mass": {"value": 1.1886, "unit": "solar_masses"},
                "rotation_period": {"value": 2773, "unit": "ms", "note": "Much slower than A"},
                "spin_down_luminosity": {"value": 1.4e32, "unit": "W"},
            },
            "orbital_period": {"value": 2.4, "unit": "hours", "note": "Extremely close binary"},
            "orbital_decay": {"value": 1.76, "unit": "mm/s", "note": "Observable decay due to gravitational waves"},
        },
        "detailed_description": (
            "The Double Pulsar is the only known binary system in which both stars are observable as pulsars. "
            "Discovered in 2003, it is the most relativistic binary star system ever found, with two neutron "
            "stars of different masses in a 2.4-hour orbit — so close that tidal forces distort their shapes. "
            "The more massive pulsar A (1.3381 solar masses) spins rapidly at 22.7 ms, while the lighter pulsar B "
            "(1.1886 solar masses) is in a recycled state but comparatively slow at 2.77 seconds. Both beams sweep "
            "Earth's line of sight, making it possible to observe both pulsars independently. The system provides "
            "a unique laboratory for testing general relativity in its strongest regime: orbital decay driven by "
            "gravitational wave emission can be directly measured (1.76 mm/s orbital period decrease per year). "
            "At this rate, the pulsars will merge in approximately 85 million years, likely producing a kilonova "
            "and a multi-solar-mass neutron star or black hole. Currently, the system is merging ~15,000 times faster "
            "than the Hulse-Taylor binary (the first pulsar binary used for GW detection)."
        ),
        "scientific_facts": [
            "Discovery of the Double Pulsar in 2003 was a major milestone — only about 20% of pulsars are in binaries.",
            "The system's orbital period of 2.4 hours is the shortest of any observed pulsar binary.",
            "Orbital decay is measured at 1.76 mm/s per year — the fastest known gravitational wave-driven merger.",
            "Both neutron star masses are measured to ±0.01 solar mass precision via pulse timing — among the most accurate neutron star masses.",
            "Pulsar B's slow 2.77-second rotation in a close binary is unusual — suggests it was not recycled as much as expected.",
            "The system exhibits geodetic precession and de Sitter precession — general relativistic effects measurable in timing data.",
            "Pulsar B's pulse beam does not fully illuminate Earth — creating eclipses of pulsar A's emission.",
            "The merger will occur ~85 million years from now — a timescale measurable by continued timing observations.",
            "The system is merging ~11 times more rapidly than the Hulse-Taylor binary pulsar, enabling faster science returns.",
            "Post-merger, the remnant may be a hypermassive neutron star (briefly) or directly a black hole.",
        ],
        "did_you_know": [
            "The Double Pulsar will merge in ~85 million years — long after the Sun becomes a white dwarf.",
            "Current timing studies can predict the merger time to within ±300 years — limited only by systematic uncertainties.",
            "If the merger is close enough to Earth in space-time, Advanced LIGO may detect the gravitational wave burst.",
        ],
        "formation_process": (
            "The Double Pulsar formed when two massive stars in a close binary both underwent core collapse within "
            "a few million years of each other. The primary (now A) collapsed first, forming a neutron star that "
            "rapidly spun up via accretion from the expanding secondary. When the secondary collapsed (now B), "
            "the system entered its current double-pulsar phase."
        ),
        "future_evolution": (
            "Gravitational wave emission will cause orbital decay. Eventually, the two neutron stars will collide. "
            "The merger will likely produce either a hypermassive neutron star (briefly) or directly a black hole, "
            "accompanied by a kilonova electromagnetic transient and a burst of gravitational waves reaching Earth."
        ),
        "related_objects": ["PSR B1913+16 (Hulse-Taylor)", "Neutron star mergers", "Gravitational waves", "GW170817"],
        "parent_system": "Milky Way",
        "child_objects": ["Pulsar A", "Pulsar B"],
        "nasa_reference": "https://science.nasa.gov/universe/neutron-stars-and-pulsars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "milisecond-pulsar-globular")),
        "name": "PSR B1821-24 (Millisecond Pulsar in Globular Cluster)",
        "category": "Neutron Star",
        "subtype": "Millisecond Pulsar — Cluster Pulsar",
        "tags": ["neutron-star", "millisecond-pulsar", "globular-cluster", "M28", "shortest-period"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 28000, "unit": "ly"},
            "coordinates": {"ra": "18h 24m 32.0s", "dec": "-24° 52' 11\""},
            "galaxy_reference": "Milky Way — M28 globular cluster",
        },
        "physical": {
            "mass": {"value": 1.44, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 3.05, "unit": "ms", "note": "~328 spins per second — one of the fastest"},
            "spin_down_luminosity": {"value": 1.5e31, "unit": "W"},
            "companion": {"type": "White dwarf", "mass": "~0.2", "orbital_period": "11.57 hours"},
        },
        "detailed_description": (
            "PSR B1821-24 is one of the fastest known millisecond pulsars, spinning 328 times per second (3.05 ms period) "
            "while residing in the dense globular cluster M28. It was the first millisecond pulsar discovered in a globular "
            "cluster (1986) and has served as a prototype for understanding recycled pulsars in dense stellar environments. "
            "The pulsar's rapid rotation was achieved through accretion-driven spin-up from a low-mass white dwarf companion "
            "in an 11.57-hour orbit. Globular cluster pulsars like PSR B1821 are unique laboratories: the high stellar density "
            "creates frequent and rare close encounters, potentially leading to dynamical interactions, planetary captures, "
            "and even merger events. PSR B1821-24 shows evidence of timing noise and glitches possibly enhanced by interaction "
            "with other cluster members. The pulsar is among the brightest radio sources in globular clusters, making X-rays "
            "and gamma-ray emission from its wind nebula potentially detectable."
        ),
        "scientific_facts": [
            "PSR B1821-24's 3.05 ms period is among the shortest of any millisecond pulsar — approaching theoretical limits.",
            "As the first millisecond pulsar discovered in a globular cluster, it revolutionized the understanding of cluster dynamics.",
            "The pulsar may be approaching the mass-limit for millisecond pulsars — beyond which centrifugal forces destabilize the crust.",
            "Globular cluster pulsars experience more frequent dynamical encounters than field pulsars — affecting long-term timing.",
            "The pulsar's companion may be a recycled white dwarf from an earlier episode of mass transfer.",
            "Close encounters with other cluster stars are observable as abrupt timing deviations on ~year timescales.",
            "The high stellar density of M28 (~50,000 stars per cubic parsec in the core) creates a unique X-ray-bright environment.",
            "PSR B1821-24 is part of a growing population of ~150 pulsars known in globular clusters — about 25% of all known pulsars.",
            "Timing array projects include globular cluster pulsars like PSR B1821-24 in their gravitational wave detection.",
            "The pulsar's kinematic position within M28 suggests it may have been scattered into its current location via past encounters."
        ],
        "did_you_know": [
            "If spun any faster, PSR B1821-24's rotation would approach the breakup velocity where material at the equator exceeds escape speed.",
            "The pulsar has survived numerous close encounters with other cluster stars — a testament to the robustness of neutron stars.",
            "At 328 spins per second, a point on PSR B1821-24's equator moves at ~15% the speed of light.",
        ],
        "formation_process": (
            "PSR B1821-24 is a recycled pulsar that formed when a neutron star underwent mass accretion "
            "from a main-sequence companion for billions of years, spinning up to its current rapid rotation. "
            "The high density of the globular cluster environment facilitated close encounters that may have "
            "enabled this recycling process to proceed more efficiently."
        ),
        "future_evolution": (
            "PSR B1821-24 will continue to slowly spin down on billion-year timescales, eventually reaching "
            "the pulsar death line. The binary orbit may tighten or loosen depending on gravitational encounters "
            "with other cluster members. The pulsar's ultimate fate depends on N-body dynamics of the cluster "
            "over Hubble times."
        ),
        "related_objects": ["M28 globular cluster", "Millisecond pulsars", "Globular cluster pulsars", "PSR J0437-4715"],
        "parent_system": "M28 globular cluster / Milky Way",
        "child_objects": ["White dwarf companion"],
        "nasa_reference": "https://www.nasa.gov/universe/neutron-stars-and-pulsars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "psr-j1748-fastest")),
        "name": "PSR J1748−2446ad (Fastest Pulsar)",
        "category": "Neutron Star",
        "subtype": "Millisecond Pulsar — Fastest Known Rotation",
        "tags": ["neutron-star", "millisecond-pulsar", "fastest-pulsar", "extreme-rotation", "record-holder"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 28000, "unit": "ly", "note": "Estimated; uncertain"},
            "coordinates": {"ra": "17h 48m 52.8s", "dec": "-24° 46' 44\""},
            "galaxy_reference": "Milky Way — Scorpius constellation",
        },
        "physical": {
            "mass": {"value": 1.535, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 1.396, "unit": "ms", "note": "~716 spins per second — fastest known"},
            "equatorial_velocity": {"value": 0.24, "unit": "c", "note": "~72,000 km/s at equator"},
            "frequency_derivative": {"value": -7e-21, "unit": "Hz/s", "note": "Extremely slow spin-down"},
        },
        "detailed_description": (
            "PSR J1748−2446ad holds the record as the fastest-known pulsar, spinning 716 times per second "
            "with a rotation period of just 1.396 milliseconds — discovered in 2004 using the Chandra X-ray "
            "Observatory. At this rotation rate, the equator moves at ~24% the speed of light (72,000 km/s), "
            "approaching theoretical limits set by the star's compressive strength and gravity. At such rotation "
            "rates, the neutron star becomes significantly oblate due to centrifugal effects — the equatorial "
            "radius is likely 10-15% larger than the polar radius. The pulsar was initially discovered as a "
            "kilohertz quasi-periodic oscillation in an accreting neutron star system, with the pulsar nature "
            "confirmed through X-ray pulsar timing. The pulsar has an extremely low spin-down rate, indicating "
            "a very weak magnetic field — typical of recycled millisecond pulsars spun up by accretion. Little "
            "is known about any companion, as the pulsar is primarily observed in X-rays rather than radio "
            "wavelengths. Theoretical models predict even faster rotation may be possible, but no pulsars have "
            "exceeded this record."
        ),
        "scientific_facts": [
            "At 716 Hz, PSR J1748−2446ad approaches the theoretical Keplerian/breakup frequency for a 1.4 solar mass neutron star.",
            "The equator moves at ~72,000 km/s — 24% the speed of light — the fastest any known macroscopic object spins.",
            "The extremely low spin-down rate indicates a very weak magnetic field (<10⁸ T) for a millisecond pulsar.",
            "The pulsar was discovered via its kilohertz quasi-periodic oscillations in X-rays — not resolved as pulses initially.",
            "At such high rotation rates, the neutron star's oblateness creates interesting observational signatures in X-ray spectral lines.",
            "The pulsar's equation of state — the relationship between density and pressure — is pushed to extreme limits, providing a laboratory for nuclear physics.",
            "Few to no pulsars have been discovered faster than PSR J1748−2446ad, suggesting this may be near the physical limit.",
            "If any faster pulsar exists, it may only briefly appear before mass shedding at the equator becomes inevitable.",
            "The pulsar remains one of the most stringent tests of neutron star models and the strong-field gravity regime."
        ],
        "did_you_know": [
            "At 716 spins per second, PSR J1748−2446ad completes one full rotation in just 1.4 milliseconds — faster than the blink of an eye.",
            "If a person could stand on PSR J1748's equator (they couldn't — they'd be obliterated), they'd experience ~200 billion g's of centrifugal acceleration.",
            "The pulsar's rotation is so extreme that relativistic effects must be carefully accounted for in its timing analysis.",
        ],
        "formation_process": (
            "PSR J1748−2446ad is a recycled pulsar that underwent accretion-driven spin-up from a companion "
            "star over millions of years. The extremely low magnetic field suggests efficient spin-up was achieved "
            "through prolonged mass accretion. The companion's current status (merger, white dwarf, or other) is unknown."
        ),
        "future_evolution": (
            "PSR J1748−2446ad will slowly spin down over billions of years as it radiates away rotational energy. "
            "Eventually it will fall below the fastest-pulsar record as younger systems are spun up to even higher "
            "rates, or gravitational wave emission (if a binary) may accelerate orbital decay."
        ),
        "related_objects": ["PSR B1821-24", "PSR J0437-4715", "Millisecond pulsars", "Neutron star equation of state"],
        "parent_system": "Milky Way",
        "child_objects": [],
        "nasa_reference": "https://science.nasa.gov/universe/neutron-stars-and-pulsars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "black-widow-pulsar")),
        "name": "Black Widow Pulsar (PSR B1957+20)",
        "category": "Neutron Star",
        "subtype": "Millisecond Pulsar — Companion Destruction",
        "tags": ["neutron-star", "millisecond-pulsar", "black-widow", "companion-evaporation", "mass-transfer"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 1600, "unit": "ly"},
            "coordinates": {"ra": "19h 59m 36.8s", "dec": "+20° 48' 15\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.44, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 6.12, "unit": "ms", "note": "~163 spins per second"},
            "companion_mass": {"value": 0.02, "unit": "solar_masses", "note": "Being evaporated away"},
            "orbital_period": {"value": 9.17, "unit": "hours"},
            "companion_surface_temperature": {"value": 6000, "unit": "K", "note": "Heated by pulsar wind"},
        },
        "detailed_description": (
            "The Black Widow Pulsar earned its name from the fate of its companion star — a low-mass white "
            "dwarf (or possibly a brown dwarf) that is being gradually evaporated and consumed by the pulsar's "
            "intense radiation and particle wind. The pulsar spins 163 times per second while orbiting its "
            "companion every 9.17 hours in one of the closest binary pulsar systems known. The pulsar wind — a "
            "beam of relativistic particles and radiation — heats the companion's surface to ~6,000 K and "
            "gradually sublimes its outer layers away. Over millions of years, the entire companion will be "
            "destroyed, leaving the pulsar as an isolated 'recycled' millisecond pulsar. The system exhibits "
            "dramatic eclipses: the companion's material absorbs ~50% of the pulsar's radio emission at orbital "
            "phases corresponding to the pulsar wind's impact with the companion's atmosphere. These eclipses "
            "provide a unique probe of the pulsar's magnetic field and wind properties."
        ),
        "scientific_facts": [
            "The Black Widow shows timing variations correlated with orbital phase — the companion's material disrupts the pulsar wind.",
            "Radio eclipses last ~30 minutes near inferior conjunction — the companion is not evaporating uniformly.",
            "The companion is now <0.02 solar masses — among the lowest-mass companions to any pulsar.",
            "Mass transfer rate measurements suggest the companion will be completely evaporated in ~100–1,000 million years.",
            "The pulsar wind's kinetic energy (~10³³ erg/s) is sufficient to evaporate the companion's atmosphere.",
            "Optical/infrared observations detected a faint, blue companion star — confirming its heating by the pulsar wind.",
            "The pulsar was likely spun up to millisecond periods by mass accretion from a more massive companion in the past.",
            "After companion destruction, PSR B1957+20 will become an isolated millisecond pulsar — possibly detectable as an 'orphan' LMXBi.",
            "The system provides a real-time laboratory for observing the late stages of binary pulsar evolution.",
            "Black Widow pulsars number ~15 known systems — this is one of the prototypical examples."
        ],
        "did_you_know": [
            "The companion star's surface faces the pulsar and is heated to thousands of Kelvin while the far side cools to thousands below.",
            "In ~500 million years, the Black Widow will completely consume its companion, becoming a solitary millisecond pulsar.",
            "The eclipses of the pulsar by the companion's atmosphere provide a unique 'X-ray shadow' of the pulsar wind magnetic field.",
        ],
        "formation_process": (
            "PSR B1957+20 formed when a neutron star spun up through accretion from a main-sequence companion. "
            "As the primary companion evolved and filled its Roche lobe, mass transfer accelerated, spinning the "
            "neutron star to millisecond periods. The primary eventually became a white dwarf, and the current "
            "low-mass companion (possibly a brown dwarf remnant) is now being evaporated by the pulsar's wind."
        ),
        "future_evolution": (
            "The Black Widow pulsar will continue to evaporate its companion over the next few hundred million years. "
            "Eventually the companion will be completely destroyed, leaving an isolated millisecond pulsar. The freed "
            "orbital angular momentum may manifest as a rapid proper motion or, if a binary survives, acceleration "
            "toward the pulsar death line."
        ),
        "related_objects": ["Millisecond pulsars", "PSR B1957+20A (companion)", "Binary pulsars", "LMXB evolution"],
        "parent_system": "Milky Way",
        "child_objects": ["Brown dwarf/white dwarf companion"],
        "nasa_reference": "https://science.nasa.gov/universe/neutron-stars-and-pulsars/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "psr-j0030-nicer")),
        "name": "PSR J0030+0451 (NICER Mass-Radius)",
        "category": "Neutron Star",
        "subtype": "Millisecond Pulsar — Hotspot Geometry",
        "tags": ["neutron-star", "millisecond-pulsar", "NICER", "mass-radius", "dense-matter", "equation-of-state"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 1000, "unit": "ly"},
            "coordinates": {"ra": "00h 30m 27.4s", "dec": "+04° 51' 39\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.44, "unit": "solar_masses"},
            "radius": {"value": 13, "unit": "km"},
            "rotation_period": {"value": 4.87, "unit": "ms", "note": "~205 spins per second"},
            "surface_temperature": {"value": 1e6, "unit": "K"},
            "hotspot_area": {"value": "~5%", "unit": "of stellar surface"},
            "hotspot_temperature": {"value": 2.5e6, "unit": "K"},
        },
        "detailed_description": (
            "PSR J0030+0451 became scientifically famous in 2019 when the NICER X-ray telescope aboard the "
            "International Space Station directly imaged its surface hotspots by timing high-resolution X-ray pulses. "
            "This breakthrough measurement simultaneously constrained the pulsar's mass (~1.44 solar masses) and "
            "radius (~13 km) — providing the first direct evidence about the equation of state (EOS) of ultra-dense "
            "nuclear matter. Surprisingly, NICER found that the pulsar has multiple hotspots, and they are not located "
            "at the magnetic poles as predicted by simple dipole models. Instead, the X-ray emission peaks come from "
            "unusual locations, suggesting a complex, multipolar magnetic field geometry — possibly inclined relative "
            "to the rotation axis. The hotspot locations and temperatures constrain models of particle acceleration in "
            "the neutron star magnetosphere. Combined with gravitational wave data from merging neutron star binaries "
            "(like GW170817), NICER measurements are revolutionizing our understanding of neutron star interiors and "
            "the nature of matter at nuclear densities."
        ),
        "scientific_facts": [
            "NICER's 2019 mass-radius measurement of PSR J0030 reduced the allowed radius range from 1–15 km to ~11–13.5 km.",
            "The pulsar's hotspots are offset from the magnetic poles — evidence of complex multipolar field geometry.",
            "The primary hotspot covers ~5% of the stellar surface and reaches ~2.5 million K.",
            "A secondary, cooler hotspot appears at a different location — suggesting a non-aligned, multipolar magnetic field.",
            "NICER's microsecond timing resolution enabled unprecedented precision in mapping the hotspot geometry.",
            "The mass-radius constraint rules out some extreme equations of state (e.g., purely quark matter cores).",
            "A second NICER target, PSR J0740+6620 (~2.08 solar masses), combined with J0030 tightly constrains the EOS curve.",
            "Constraints from PSR J0030 and J0740 support stiffer equations of state than previously expected from nuclear physics.",
            "The hotspot morphology suggests that emitted X-rays trace magnetic field lines from the surface into the magnetosphere.",
            "Future NICER observations may resolve individual hotspots on other pulsars — opening a new era of pulsar surface imaging."
        ],
        "did_you_know": [
            "NICER directly imaged a pulsar's surface for the first time — a revolutionary observational achievement.",
            "The hotspot discovery challenged existing models of pulsar magnetospheres and accelerated theoretical advances.",
            "PSR J0030's properties help answer one of astrophysics' deepest questions: what is the nature of matter at nuclear densities?",
        ],
        "formation_process": (
            "PSR J0030+0451 is a recycled millisecond pulsar that was spun up to its current rapid rotation "
            "through accretion from a companion star over billions of years. The companion has since been lost, "
            "possibly merged or ejected. The pulsar's complex magnetic field geometry may reflect interactions "
            "with the companion's field prior to separation."
        ),
        "future_evolution": (
            "PSR J0030 will spin down extremely slowly over trillions of years due its low magnetic field strength. "
            "Eventually it will cross the pulsar death line and cease electromagnetic emission — first radio "
            "waves cease, followed by gamma-ray and X-ray emission over longer timescales."
        ),
        "related_objects": ["PSR J0740+6620", "GW170817", "Neutron star equation of state", "NICER instrument", "ISS"],
        "parent_system": "Milky Way",
        "child_objects": [],
        "nasa_reference": "https://www.nasa.gov/nicer/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "young-pulsar-generic")),
        "name": "Pulsar Wind Nebula (General Class)",
        "category": "Neutron Star",
        "subtype": "Pulsar Wind Nebula — Synchrotron Emission",
        "tags": ["neutron-star", "pulsar-wind", "synchrotron", "relativistic-wind", "PWN"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": "Variable", "unit": "ly", "note": "Depends on specific PWN"},
            "galaxy_reference": "Milky Way",
            "nebula_age": {"value": "1,000–100,000", "unit": "years"},
        },
        "physical": {
            "size": {"value": "0.1–50", "unit": "pc", "note": "Depends on age and surroundings"},
            "energy_source": "Pulsar kinetic wind energy",
            "particle_acceleration": "At wind termination shock",
            "emission": "Synchrotron across electromagnetic spectrum",
        },
        "detailed_description": (
            "Pulsar Wind Nebulae (PWNe) are dynamic structures created when a pulsar's relativistic particle wind "
            "(electrons, positrons, ions traveling at relativistic speeds) plows into the surrounding medium or "
            "supernova remnant. The pulsar wind carries away ~99% of the pulsar's rotational kinetic energy as "
            "flowing particles; a standing shock wave (the termination shock) forms where this wind meets the denser "
            "ambient medium. Particles are accelerated to extreme energies in this shock, reaching TeV (10¹² eV) "
            "and potentially PeV (10¹⁵ eV) regimes. The accelerated particles emit synchrotron radiation across "
            "the electromagnetic spectrum — from radio waves through X-rays to gamma-rays. Young PWNe like the Crab "
            "Nebula show complex structure: toroidal shocks, polar jets, and rapidly evolving 'wisps'. Older PWNe "
            "gradually fade as particles lose energy to radiation and the wind energy diminishes as the pulsar spins down. "
            "PWNe are among the most efficient cosmic particle accelerators and contribute significantly to the cosmic "
            "ray population at GeV/TeV energies. VERITAS, Fermi LAT, and ground-based observatories have detected "
            "hundreds of PWNe as TeV gamma-ray sources."
        ),
        "scientific_facts": [
            "PWNe are the brightest gamma-ray sources detected by Fermi LAT and VERITAS in the inner Galaxy.",
            "The pulsar wind carries energy at rates of 10³¹–10³⁴ W — rivaling galaxy-scale jets in power density.",
            "Particle acceleration to TeV energies in PWNe is one of the most efficient processes in the universe.",
            "More than 900 PWNe have been catalogued in radio, X-ray, and gamma-ray surveys.",
            "The morphology of PWNe changes dramatically with age: young systems show jets, older systems show irregular shapes.",
            "Magnetic fields in PWNe can exceed 100 microGauss — sufficient to contain TeV particles in small volumes.",
            "PWNe are sites of heavy element production (iron-nickel produced by supernovae is swept by the wind).",
            "The 'Fermi Bubble' structures (giant lobes emanating from the Galactic center) may be powered by PWNe or jets from Sgr A*.",
            "PWNe can illuminate molecular clouds through their radiation — creating boundaries visible in infrared surveys.",
            "Some PWNe produce periodic or quasi-periodic emission — evidence of rotational asymmetries or instabilities."
        ],
        "did_you_know": [
            "If the Crab Pulsar's wind energy could power human civilization, it would supply 10 billion Earths' worth of electricity.",
            "PWNe evolve on timescales of 10,000–100,000 years — a cosmic blink of an eye enabling direct observation of evolution.",
            "Some PWNe escape their birth supernova remnants, creating isolated structures that puzzle observers initially.",
        ],
        "formation_process": (
            "PWNe form immediately after pulsar birth from core-collapse supernovae. The newly formed, rapidly "
            "rotating proto-neutron star launches a relativistic wind carrying away ~10¹⁰ Joules per second. If "
            "the parent supernova remnant is still expanding or dense, the wind is confined and visible. Eventually "
            "all PW Ne fade as the pulsar slows and the wind weakens."
        ),
        "future_evolution": (
            "PWNe evolve through distinct phases: (1) Composite phase (~1,000 yrs): bright within SNR; (2) Bow-shock phase "
            "(~10,000 yrs): as SNR expands, PWN breaks free and forms a bow shock; (3) Fading phase (>100,000 yrs): "
            "PWN's brightness declines as the pulsar wind weakens. Eventually PWNe fade below detection limits, leaving "
            "only the pulsar as a dim X-ray source."
        ),
        "related_objects": ["Crab Nebula", "Vela PWN", "3C 58", "G0.9+0.1", "Millisecond pulsars"],
        "parent_system": "Milky Way",
        "child_objects": ["Pulsar", "Termination shock", "Particle acceleration region"],
        "nasa_reference": "https://science.nasa.gov/universe/neutron-stars-and-pulsars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 6: FAMOUS BLACK HOLES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "m87-star-black-hole")),
        "name": "M87* (Virgo A Black Hole)",
        "category": "Black Hole",
        "subtype": "Supermassive Black Hole — Active Galactic Nucleus",
        "tags": ["black-hole", "supermassive", "AGN", "M87", "first-image-black-hole", "relativistic-jet", "EHT"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 55e6, "unit": "ly"},
            "coordinates": {"ra": "12h 30m 49.42s", "dec": "+12° 23' 28.0\""},
            "galaxy_reference": "M87 (Virgo Cluster)",
        },
        "physical": {
            "mass": {"value": 6.5e9, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 19.2e9, "unit": "km", "au": 128, "note": "~3.7× Pluto's orbit"},
            "accretion_rate": {"value": 9e-4, "unit": "solar_masses/year"},
            "jet_length": {"value": 5000, "unit": "ly"},
            "jet_velocity": {"note": "Superluminal apparent motion up to ~6c due to relativistic beaming"},
        },
        "detailed_description": (
            "M87* is the supermassive black hole at the center of Messier 87, a giant elliptical galaxy "
            "55 million light-years away in the Virgo Cluster. With a mass of ~6.5 billion solar masses, "
            "it is one of the largest known black holes with a directly measured mass. On April 10, 2019, "
            "the Event Horizon Telescope collaboration released the first-ever direct image of a black "
            "hole's shadow — showing M87*'s photon ring, the bright ring of light produced by photons "
            "orbiting the black hole's event horizon. The ring's diameter (~42 microarcseconds) matched "
            "theoretical predictions for a black hole of this mass. M87* drives one of the most powerful "
            "astrophysical jets known — a relativistic plasma beam extending ~5,000 light-years from the "
            "nucleus, visible from radio to X-ray wavelengths. The jet's apparent superluminal motion "
            "(up to 6 times the speed of light) is a geometric illusion from plasma moving near the "
            "speed of light at a small angle to our line of sight. The jet interaction with the "
            "intracluster medium inflates enormous radio lobes spanning hundreds of kiloparsecs, "
            "depositing ~10⁴⁵ erg/s of kinetic energy that heats the galaxy cluster gas and suppresses "
            "cooling flows. M87*'s event horizon is so large that its Schwarzschild radius (~19 billion "
            "km) exceeds the orbit of Pluto around our Sun by 3.7 times."
        ),
        "scientific_facts": [
            "M87* was the first black hole to be directly imaged — the EHT image was published April 10, 2019.",
            "The photon sphere (where light orbits) is at 1.5× the Schwarzschild radius — photons there travel in unstable circular orbits.",
            "The asymmetric brightness of the ring (brighter in the south) indicates the jet is directed slightly toward Earth.",
            "The EHT 2021 imaging revealed a rotating spacetime geometry, constraining M87*'s spin parameter.",
            "The relativistic jet was first observed optically by Heber Curtis in 1918 — 101 years before the shadow was imaged.",
            "Energy extracted from M87*'s spin via the Blandford-Znajek mechanism may power the relativistic jet.",
            "M87*'s Bondi accretion radius — where its gravity dominates over ambient gas pressure — spans ~100 pc.",
            "The galaxy M87 contains ~15,000 globular clusters — roughly 100× more than the Milky Way, likely from merger history.",
            "A full orbit at the innermost stable circular orbit of M87* takes approximately one week, compared to 28 minutes for Sgr A*.",
        ],
        "did_you_know": [
            "If M87* replaced our Sun, its event horizon would swallow all planets out to Saturn's orbit.",
            "The EHT array that imaged M87* was a virtual telescope the size of Earth, achieving angular resolution equivalent to reading a newspaper in New York from Paris.",
            "The 2019 image required processing petabytes of data using specialized VLBI correlation algorithms and cross-validation by four independent imaging teams.",
        ],
        "formation_process": (
            "M87* grew through billions of years of galaxy mergers and gas accretion. M87 itself is "
            "a cD galaxy — a giant elliptical galaxy at the center of a cluster — that formed from "
            "the merger of many smaller galaxies. Each merger potentially delivered a central black "
            "hole that merged with M87*. The black hole's current mass may also reflect a 'wet merger' "
            "history with substantial gas accretion during active quasar phases."
        ),
        "future_evolution": (
            "M87* will continue to accrete at its low current rate. On cosmological timescales, "
            "it may merge with the central black holes of other Virgo Cluster galaxies as M87 "
            "swallows them. Billions of years from now, in an era of reduced gas supply, M87* "
            "will become increasingly radio-quiet. Eventually, over 10^100 years, Hawking "
            "radiation would cause it to evaporate — though this timescale is incomprehensibly "
            "longer than the current age of the universe."
        ),
        "related_objects": ["M87 Galaxy", "Virgo Cluster", "Sagittarius A*", "Event Horizon Telescope", "NGC 1277 Black Hole"],
        "parent_system": "M87 Galaxy / Virgo Cluster",
        "child_objects": ["Relativistic Jet (M87)", "Radio Lobes"],
        "nasa_reference": "https://www.nasa.gov/universe/nasa-hubble-observations-help-pin-down-origin-of-m87-jets/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "gw150914-black-holes")),
        "name": "GW150914 — First Gravitational Wave Event",
        "category": "Black Hole",
        "subtype": "Binary Black Hole Merger — Gravitational Wave Source",
        "tags": ["black-hole", "gravitational-waves", "LIGO", "merger", "binary-black-hole", "GW-astronomy"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 1.3e9, "unit": "ly"},
            "coordinates": {"ra": "09h 50m 45.0s", "dec": "-43° 25' 00\"", "note": "Approximate sky localization"},
        },
        "physical": {
            "primary_black_hole": {"mass": {"value": 35.6, "unit": "solar_masses"}},
            "secondary_black_hole": {"mass": {"value": 30.6, "unit": "solar_masses"}},
            "remnant_black_hole": {"mass": {"value": 63.1, "unit": "solar_masses"}},
            "energy_radiated": {"value": 3.0, "unit": "solar_masses", "note": "As gravitational waves in ~0.2 seconds"},
            "peak_luminosity": {"value": 3.6e49, "unit": "W", "note": "~50x more luminous than all stars in the observable universe combined"},
        },
        "detailed_description": (
            "GW150914 was the first direct detection of gravitational waves — ripples in spacetime "
            "predicted by Einstein's general relativity in 1915 but not detected until September "
            "14, 2015, by the LIGO detectors in Hanford (WA) and Livingston (LA). The signal was "
            "produced by the merger of two stellar-mass black holes ~1.3 billion light-years away, "
            "with masses of ~36 and ~31 solar masses spiraling together over billions of years "
            "before merging in milliseconds. In the final ~0.2 seconds, the merger radiated "
            "3 solar masses of energy purely as gravitational waves — a peak power output ~50x "
            "greater than all stars in the observable universe combined at that instant. The "
            "detection opened an entirely new field: gravitational wave astronomy, allowing "
            "humanity to 'hear' rather than merely 'see' the universe. LIGO's two detectors "
            "recorded identical signals separated by 7 milliseconds — the travel time difference "
            "for a signal crossing the speed of light between the two sites."
        ),
        "scientific_facts": [
            "GW150914 stretched and compressed LIGO's 4-km arms by 1/1,000th the diameter of a proton — the most precise length measurement in history.",
            "Peak gravitational wave luminosity: ~3.6×10⁴⁹ W — outshining all stars in the observable universe at that instant.",
            "The chirp signal — rising frequency and amplitude — matched GR predictions for binary inspiral with extraordinary precision.",
            "LIGO requires vibration isolation to detect motion 10,000x smaller than an atomic nucleus.",
            "LIGO's discovery was made September 14, 2015 — just 2 days after detectors were upgraded for 'Advanced LIGO' operation.",
            "By 2023, LIGO-Virgo-KAGRA have detected 90+ gravitational wave events from merging compact objects.",
            "The 7 ms arrival time difference between detectors placed the source in a 600 deg² southern sky region.",
            "GW150914 confirmed that binary black holes of these masses exist — they weren't previously observed.",
            "The Kip Thorne, Rainer Weiss, and Barry Barish shared the 2017 Nobel Prize in Physics for LIGO and gravitational waves.",
            "LISA (Laser Interferometer Space Antenna), planned for 2030s launch, will detect gravitational waves from supermassive black hole mergers.",
        ],
        "did_you_know": [
            "Einstein himself believed gravitational waves would never be detectable — the engineering achievement was beyond his imagination.",
            "The signal lasted ~0.2 seconds and swept from 35 Hz to 150 Hz — within the range of human hearing.",
            "LIGO's arm displacement was 1/1,000th the diameter of a proton — the most precise measurement ever made.",
        ],
        "related_objects": ["LIGO detector", "Sagittarius A*", "M87*", "GW170817"],
        "parent_system": "~1.3 billion light-years distant",
        "nasa_reference": "https://www.ligo.caltech.edu/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "gw170817-neutron-star-merger")),
        "name": "GW170817 — Neutron Star Merger",
        "category": "Black Hole",
        "subtype": "Binary Neutron Star Merger — Multi-Messenger Event",
        "tags": ["neutron-star", "gravitational-waves", "kilonova", "multi-messenger", "LIGO", "gold-formation"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 130e6, "unit": "ly"},
            "coordinates": {"ra": "13h 09m 48.1s", "dec": "-23° 22' 53\""},
            "galaxy_reference": "NGC 4993 (lenticular galaxy)",
        },
        "physical": {
            "neutron_star_1": {"mass": {"value": 1.36, "unit": "solar_masses"}},
            "neutron_star_2": {"mass": {"value": 1.17, "unit": "solar_masses"}},
            "remnant": {"note": "Likely collapsed to a black hole ~2.7 solar masses within seconds"},
            "kilonova_energy": {"value": 1e44, "unit": "J"},
        },
        "detailed_description": (
            "GW170817, detected August 17, 2017, was the first gravitational wave event detected "
            "from a binary neutron star merger — and the most scientifically productive event in "
            "the history of astrophysics. Within 1.7 seconds of the gravitational wave signal, "
            "the Fermi Gamma-ray Space Telescope detected a short gamma-ray burst (sGRB 170817A) "
            "from the same direction — directly confirming that short GRBs are produced by "
            "neutron star mergers. Then, over days to weeks, ground and space-based telescopes "
            "observed the kilonova (AT2017gfo) — a thermal optical-infrared transient powered "
            "by r-process nucleosynthesis. The kilonova spectra confirmed the formation of heavy "
            "elements (gold, platinum, strontium, barium, europium) — directly demonstrating "
            "that neutron star mergers are a primary site of r-process nucleosynthesis that "
            "creates most of the universe's heavy elements heavier than iron."
        ),
        "scientific_facts": [
            "GW170817 was observed simultaneously in gravitational waves and electromagnetic radiation — the birth of multi-messenger astronomy.",
            "The 1.7-second delay between GW and gamma-ray arrival limited the difference in speed of light vs gravitational waves to <10⁻¹⁵ c.",
            "Strontium was spectroscopically confirmed in the kilonova by the VLT — the first direct identification of r-process element formation.",
            "The event produced ~5 Earth masses of gold equivalent in r-process elements.",
            "GW170817 provided an independent measurement of the Hubble constant: H₀ = 70 ± 12 km/s/Mpc.",
            "The kilonova peaked in UV, faded in optical, and brightened in near-IR — matching r-process opaque ejecta models.",
            "Over 70 observatories worldwide observed GW170817 across all wavelengths — the most observed astronomical event ever.",
            "A radio afterglow detected months later confirmed a structured jet was produced — connecting to the GRB mechanism.",
            "The neutron star mass ratio (1.36 + 1.17 M☉) provided tighter EOS constraints combined with NICER data.",
            "AT2017gfo was detected in NGC 4993, a lenticular galaxy ~130 million light-years away in Hydra.",
        ],
        "did_you_know": [
            "The gold in your wedding ring may have been forged in a neutron star merger billions of years ago.",
            "GW170817 was detected just 1.7 seconds before a short gamma-ray burst — the two phenomena were finally linked.",
            "The kilonova was visible through amateur telescopes for several days after discovery.",
        ],
        "related_objects": ["LIGO detector", "NGC 4993", "GW150914", "Short Gamma-Ray Bursts", "Kilonovae"],
        "parent_system": "NGC 4993 / Hydra constellation",
        "nasa_reference": "https://www.nasa.gov/universe/nasa-missions-catch-first-light-from-a-gravitational-wave-event/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "tde-at2019qiz")),
        "name": "AT2019qiz — Tidal Disruption Event",
        "category": "Black Hole",
        "subtype": "Tidal Disruption Event (TDE)",
        "tags": ["black-hole", "tidal-disruption", "TDE", "stellar-destruction", "transient", "accretion"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 215e6, "unit": "ly"},
            "galaxy_reference": "Unnamed host galaxy",
        },
        "physical": {
            "black_hole_mass": {"value": 1e6, "unit": "solar_masses"},
            "disrupted_star_mass": {"value": 0.5, "unit": "solar_masses"},
            "peak_luminosity": {"value": 1e37, "unit": "W"},
            "duration": {"value": "~months"},
        },
        "detailed_description": (
            "AT2019qiz is a tidal disruption event (TDE) — the shredding of a star by a "
            "supermassive black hole. When a star strays within the tidal disruption radius "
            "(Roche limit) of a black hole, gravitational tidal forces exceed the star's "
            "self-gravity and the star is stretched into a long streamer of stellar material. "
            "Roughly half the mass falls back onto the black hole in an elliptical stream that "
            "circularizes and forms an accretion disk, powering a transient luminosity often "
            "comparable to a quasar. AT2019qiz was the first TDE caught early enough to observe "
            "from before peak brightness — allowing astronomers to directly witness the disk "
            "formation process and the phase of debris fallback. Its optical light curve matched "
            "theoretical fallback rates (L ∝ t⁻⁵/³) precisely. TDEs are cosmological tools for "
            "measuring black hole masses in otherwise quiet galaxies."
        ),
        "scientific_facts": [
            "AT2019qiz is the most precisely observed TDE from pre-peak through decay — revealing the disk formation timeline.",
            "TDE rates are estimated at ~1 per 10,000–100,000 years per galaxy.",
            "Optical spectroscopy of AT2019qiz showed hydrogen Balmer and helium emission lines from the disrupted star's material.",
            "The 'missing energy problem' in TDEs — why they are less luminous than predicted — may be explained by reprocessing layers.",
            "TDEs can temporarily activate otherwise quiet black holes into AGN-like states.",
            "At2019qiz's black hole mass (~10⁶ solar masses) was measured from the TDE timescale and luminosity.",
            "Relativistic TDEs ('jetted TDEs') produce gamma-ray emission and radio flares — only a few are known.",
            "LSST/Rubin Observatory is expected to discover thousands of TDEs per year, revolutionizing black hole demographics.",
            "TDE host galaxies are disproportionately E+A (post-starburst) galaxies — the physical reason is debated.",
            "Ultraviolet observations of TDEs trace the disk's innermost regions — probing relativistic accretion physics.",
        ],
        "did_you_know": [
            "Tidal disruption events are among the brightest transient events in the universe — briefly outshining entire galaxies.",
            "A star falling into a black hole produces a characteristic light curve that rises over months then decays over years.",
            "TDEs allow measurement of black hole masses in galaxies too far away to observe stellar orbits.",
        ],
        "related_objects": ["Sagittarius A*", "M87*", "LIGO detector", "AGN"],
        "parent_system": "Host galaxy ~215 million light-years distant",
        "nasa_reference": "https://www.nasa.gov/universe/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "ngc1277-black-hole")),
        "name": "NGC 1277 Black Hole",
        "category": "Black Hole",
        "subtype": "Supermassive Black Hole — Overmassive Relic",
        "tags": ["black-hole", "supermassive", "overmassive", "relic", "Perseus-cluster", "early-type-galaxy"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 240e6, "unit": "ly"},
            "coordinates": {"ra": "03h 19m 51.5s", "dec": "+41° 34' 25\""},
            "galaxy_reference": "Perseus Cluster",
        },
        "physical": {
            "mass": {"value": 1.7e10, "unit": "solar_masses", "note": "Up to 17 billion solar masses — possibly the largest known"},
            "host_galaxy_stellar_mass": {"value": 1.2e11, "unit": "solar_masses"},
            "black_hole_to_stellar_mass_ratio": {"value": 0.14, "note": "~14% — extraordinarily high vs ~0.1% typical"},
        },
        "detailed_description": (
            "NGC 1277 contains one of the most overmassive black holes known — a supermassive "
            "black hole estimated at ~10–17 billion solar masses residing in a compact lenticular "
            "galaxy of only ~120 billion solar masses. In typical galaxies, the central black "
            "hole constitutes only ~0.1–0.5% of the stellar bulge mass; in NGC 1277, it may "
            "represent ~14–59% — a staggering ratio that challenges models of co-evolutionary "
            "black hole-galaxy growth. NGC 1277 is also remarkably quiescent — it shows no "
            "ongoing star formation and little evidence of recent merger activity. The leading "
            "interpretation is that NGC 1277 is a 'relic galaxy' — a compact massive galaxy "
            "from the early universe (~10 billion years ago) that stopped evolving, while other "
            "galaxies of similar initial mass grew substantially through mergers. Its extreme "
            "black hole may represent the maximum early-universe black hole accretion before "
            "AGN feedback shut off further growth."
        ),
        "scientific_facts": [
            "NGC 1277's black hole may represent up to 59% of the total stellar bulge mass — a record BH-to-bulge ratio.",
            "The galaxy has a velocity dispersion of ~333 km/s — extremely high for its size.",
            "Hubble's stellar dynamics measurements revealed the black hole's mass via the radius of influence of its gravity.",
            "NGC 1277 is considered a 'red nugget relic' — a compact massive galaxy that didn't merge to grow larger since z~2.",
            "Other massive galaxies at z~2 that later merged would have diluted their black hole mass fraction — relic avoids this.",
            "Perseus Cluster membership may have shielded NGC 1277 from mergers by preventing secondary satellite accretion.",
            "The galaxy's old stellar populations (~10 Gyr) support its interpretation as a high-redshift relic.",
            "Multiple studies debate the exact mass — estimates range from 5 to 17 billion solar masses depending on stellar mass model.",
            "NGC 1277's black hole shadow subtends a larger angle than Sgr A* despite being 240 million light-years away.",
            "The EHT could theoretically image the NGC 1277 black hole shadow if VLBI baselines were extended.",
        ],
        "did_you_know": [
            "NGC 1277's black hole may be the most massive within the local universe — rivaling quasar-era black holes.",
            "If its mass estimates are correct, the event horizon is ~3x larger than Pluto's orbit around the Sun.",
            "The galaxy's extreme black hole suggests it may have gone through an intense quasar phase in the early universe.",
        ],
        "related_objects": ["M87*", "Sagittarius A*", "Perseus Cluster", "Relic Galaxies"],
        "parent_system": "Perseus Cluster",
        "nasa_reference": "https://www.nasa.gov/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "m87-black-hole")),
        "name": "M87*",
        "category": "Black Hole",
        "subtype": "Supermassive Black Hole",
        "tags": ["black-hole", "supermassive", "EHT", "relativistic-jet", "active-galactic-nucleus", "M87"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 53.5e6, "unit": "ly"},
            "coordinates": {"ra": "12h 30m 49.4s", "dec": "+12° 23' 28\""},
            "galaxy_reference": "Messier 87 (M87)",
            "location": "Center of Virgo A galaxy cluster",
        },
        "physical": {
            "mass": {"value": 6.5e9, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 19e9, "unit": "km", "note": "~129 AU"},
            "angular_diameter_observed": {"value": 42, "unit": "microarcseconds"},
            "jet_length": {"value": 5000, "unit": "ly"},
            "spin": {"note": "High spin parameter, estimated > 0.8"},
        },
        "detailed_description": (
            "M87* is the supermassive black hole at the center of Messier 87, a giant elliptical galaxy in the Virgo Cluster. "
            "It gained global fame in April 2019 when the Event Horizon Telescope (EHT) collaboration released the first-ever "
            "direct image of a black hole's shadow. The image revealed a bright ring of light, formed by photons orbiting the "
            "black hole, surrounding a dark central region — the event horizon's silhouette. With a colossal mass of approximately "
            "6.5 billion solar masses, M87* is one of the most massive black holes known. It powers a spectacular relativistic jet "
            "of plasma that extends for at least 5,000 light-years, traveling at over 99% the speed of light. This jet, visible "
            "across the electromagnetic spectrum, is a testament to the immense energy extracted from the black hole's rotation and "
            "accretion disk. The EHT has continued to observe M87*, revealing the polarization of the light around it, which maps "
            "the powerful magnetic fields responsible for launching and collimating the jet."
        ),
        "scientific_facts": [
            "M87* was the subject of the first direct image of a black hole's shadow, published by the EHT in 2019.",
            "Its mass is ~1,500 times greater than Sagittarius A*, the black hole in our own galaxy.",
            "The relativistic jet it produces is one of the most powerful and well-studied astrophysical jets.",
            "The black hole's shadow has a diameter of about 40 billion km, larger than the orbit of Pluto.",
            "Polarization data from the EHT revealed the structure of magnetic fields near the event horizon, confirming models of jet formation.",
            "M87* is a key laboratory for testing General Relativity in the strong-gravity regime.",
            "The black hole's spin is a significant source of the jet's power, via the Blandford-Znajek process.",
            "The jet exhibits 'superluminal motion', an optical illusion where knots of plasma appear to move faster than light.",
            "M87* is surrounded by a hot, X-ray emitting gas halo that serves as its primary fuel source.",
            "The black hole's mass was measured independently by observing the orbital velocities of stars and gas clouds in M87's core.",
        ],
        "did_you_know": [
            "The data required to create the first image of M87* was so large it had to be physically shipped on hard drives from telescopes around the world.",
            "If M87* were placed at the center of our solar system, its event horizon would engulf all the planets and the Kuiper Belt.",
            "The jet was first observed by astronomer Heber Curtis in 1918, who described it as a 'curious straight ray'.",
        ],
        "formation_process": (
            "M87* grew to its immense size over billions of years through a hierarchical merger process. It likely started from a smaller seed black hole "
            "in the early universe and grew by accreting vast amounts of gas and by merging with other supermassive black holes as its host galaxy, M87, "
            "cannibalized other galaxies in the dense Virgo Cluster environment."
        ),
        "future_evolution": (
            "M87* will continue to accrete matter from its surroundings and grow in mass. As the dominant galaxy in the Virgo Cluster, M87 will continue to merge "
            "with other galaxies, delivering more fuel and potentially other central black holes for M87* to consume, further increasing its mass and spin."
        ),
        "related_objects": ["Messier 87 (M87)", "Sagittarius A*", "Virgo Cluster", "Event Horizon Telescope"],
        "parent_system": "Messier 87 (M87) Galaxy",
        "child_objects": ["Relativistic Jet"],
        "nasa_reference": "https://www.nasa.gov/mission_pages/chandra/news/black-hole-image-makes-history",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cygnus-x-1")),
        "name": "Cygnus X-1",
        "category": "Black Hole",
        "subtype": "Stellar-Mass Black Hole",
        "tags": ["black-hole", "stellar-mass", "x-ray-binary", "binary-system", "milky-way"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 7300, "unit": "ly"},
            "coordinates": {"ra": "19h 58m 21.7s", "dec": "+35° 12' 05.8\""},
            "galaxy_reference": "Milky Way",
            "location": "Cygnus constellation",
        },
        "physical": {
            "mass": {"value": 21.2, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 63, "unit": "km"},
            "companion_star": "HDE 226868 (O-type supergiant)",
            "orbital_period": {"value": 5.6, "unit": "days"},
        },
        "detailed_description": (
            "Cygnus X-1 is one of the most famous and well-studied black holes in our galaxy. It is a stellar-mass black hole "
            "locked in a tight orbit with a massive companion star, HDE 226868, an O-type blue supergiant. This system forms a "
            "high-mass X-ray binary. The black hole's immense gravity pulls material from the companion star's stellar wind, "
            "forming a hot, turbulent accretion disk. As the material spirals inward, it is heated to millions of degrees, "
            "emitting intense X-rays, making Cygnus X-1 one of the brightest persistent X-ray sources in the sky. Discovered in "
            "1964, its mass was too high for it to be a neutron star, making it one of the first celestial objects to be widely "
            "accepted as a black hole. Its discovery was the subject of a famous scientific wager between Stephen Hawking and "
            "Kip Thorne, with Hawking conceding in 1990 that Cygnus X-1 was indeed a black hole."
        ),
        "scientific_facts": [
            "Cygnus X-1 was the first X-ray source widely accepted to be a black hole.",
            "Its mass of 21.2 solar masses definitively rules out the possibility of it being a neutron star.",
            "The system emits a relativistic jet, though much weaker than those from supermassive black holes, classifying it as a microquasar.",
            "The orbital period of the binary system is a mere 5.6 days.",
            "The companion star, HDE 226868, is a massive star of about 40-50 solar masses, which is losing mass to the black hole at a high rate.",
            "The X-ray emission from Cygnus X-1 is highly variable on timescales from milliseconds to years, reflecting turbulence in the accretion disk.",
            "Precise distance and mass measurements were made using the Very Long Baseline Array (VLBA) by measuring its parallax.",
            "The black hole spins at more than 800 times per second, close to its maximum possible rotation speed.",
            "The age of the system is estimated to be only about 5 million years old.",
            "The famous Hawking-Thorne bet on the nature of Cygnus X-1 is a landmark in the history of black hole physics.",
        ],
        "did_you_know": [
            "The 'X-1' in its name denotes that it was the first X-ray source discovered in the constellation Cygnus.",
            "The companion star is so bright it can be seen with a modest amateur telescope, but the black hole itself is invisible.",
            "The energy released by the accretion disk makes the system shine brighter in X-rays than the Sun does in all wavelengths combined.",
        ],
        "formation_process": (
            "The black hole in Cygnus X-1 formed from the core-collapse of a very massive star (likely > 40 solar masses) in a binary system. "
            "The collapse was likely 'direct', meaning the star imploded to form a black hole without a bright supernova explosion that would have "
            "otherwise disrupted the binary system. The companion star, HDE 226868, survived the event and is now the mass donor."
        ),
        "future_evolution": (
            "The companion star HDE 226868 will eventually evolve into a red supergiant and then likely collapse to form a black hole itself, "
            "potentially creating a binary black hole system. This system would then spiral together over millions of years and merge, producing "
            "a powerful burst of gravitational waves."
        ),
        "related_objects": ["HDE 226868", "Sagittarius A*", "Neutron Star"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Accretion Disk", "Relativistic Jet"],
        "nasa_reference": "https://www.nasa.gov/mission_pages/chandra/multimedia/cygnusx1.html",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "ton-618")),
        "name": "TON 618",
        "category": "Black Hole",
        "subtype": "Ultramassive Black Hole (Quasar)",
        "tags": ["black-hole", "ultramassive", "quasar", "distant-universe", "lyman-alpha-forest"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 18.2e9, "unit": "ly", "note": "Comoving distance"},
            "redshift": "z = 2.219",
            "coordinates": {"ra": "12h 28m 24.9s", "dec": "+31° 28' 37\""},
            "galaxy_reference": "Unnamed distant galaxy",
        },
        "physical": {
            "mass": {"value": 6.6e10, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 195e9, "unit": "km", "note": "~1300 AU"},
            "luminosity": {"value": 1.4e14, "unit": "solar_luminosities", "note": "One of the brightest objects in the known universe"},
        },
        "detailed_description": (
            "TON 618 is an ultramassive black hole powering a hyperluminous quasar, located in the distant universe. With a staggering mass of "
            "66 billion times that of the Sun, it is one of the most massive black holes ever discovered. This behemoth is so large that its "
            "event horizon would extend far beyond our solar system, with a radius of about 1,300 AU. TON 618 is the engine of a quasar so "
            "bright that it outshines its entire host galaxy, which is itself not visible from Earth due to the quasar's glare. The light "
            "from TON 618 has traveled for over 10 billion years to reach us (lookback time), providing a glimpse into the early universe. "
            "The spectrum of TON 618 shows broad emission lines from gas orbiting the black hole at tremendous speeds (up to 7,000 km/s), "
            "which is how its enormous mass was first calculated. It is also a prominent source used to study the Lyman-alpha forest, "
            "as its bright light is absorbed by intervening clouds of neutral hydrogen, mapping the cosmic web."
        ),
        "scientific_facts": [
            "At 66 billion solar masses, TON 618 is one of the most massive black holes known.",
            "It is classified as a quasar, an active galactic nucleus of exceptionally high luminosity.",
            "Its absolute magnitude of -30.7 makes it one of the brightest objects in the observable universe.",
            "The black hole is accreting matter at such a high rate that it is close to the Eddington limit, the theoretical maximum luminosity.",
            "The radius of its event horizon is larger than the orbit of Neptune by a factor of more than 40.",
            "TON 618 was discovered in 1957 as a faint blue star but was not identified as a quasar until later spectroscopic studies.",
            "The host galaxy of TON 618 is not visible because the quasar's light is ~1000 times brighter.",
            "The broad emission lines in its spectrum indicate gas moving at ~7,000 km/s in the broad-line region around the black hole.",
            "Its existence in the early universe (at redshift z=2.219) challenges models of black hole formation and growth.",
            "The name 'TON' comes from the Tonantzintla Observatory survey where it was first cataloged.",
        ],
        "did_you_know": [
            "TON 618 shines with the light of 140 trillion Suns.",
            "The mass of TON 618 is greater than the entire stellar mass of many galaxies, including our own Milky Way.",
            "Studying its light allows astronomers to probe the distribution of matter in the universe over billions of light-years.",
        ],
        "formation_process": (
            "The formation of an ultramassive black hole like TON 618 so early in the universe is a major puzzle. It likely required "
            "either a massive 'seed' black hole (from a direct-collapse black hole of ~100,000 solar masses) or a period of sustained, "
            "super-Eddington accretion, or both. It must have grown incredibly rapidly in the first few billion years of the cosmos."
        ),
        "future_evolution": (
            "Like all quasars, TON 618 will eventually exhaust its fuel supply. As the accretion slows and stops, the quasar will 'turn off', "
            "and the ultramassive black hole will become dormant at the center of its host galaxy, which will then become visible. This process "
            "may take millions to billions of years."
        ),
        "related_objects": ["Quasar", "Supermassive Black Hole", "Lyman-alpha forest", "M87*"],
        "parent_system": "Distant Universe",
        "child_objects": ["Accretion Disk", "Broad-line Region"],
        "nasa_reference": "https://imagine.gsfc.nasa.gov/science/objects/quasars.html",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "m82-x-1")),
        "name": "M82 X-1",
        "category": "Black Hole",
        "subtype": "Intermediate-Mass Black Hole (Candidate)",
        "tags": ["black-hole", "intermediate-mass", "IMBH", "ultraluminous-x-ray-source", "ULX", "M82"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 12e6, "unit": "ly"},
            "coordinates": {"ra": "09h 55m 50.0s", "dec": "+69° 40' 47\""},
            "galaxy_reference": "Messier 82 (M82)",
            "location": "Off-center in the M82 starburst galaxy",
        },
        "physical": {
            "mass": {"value": 400, "unit": "solar_masses", "note": "Estimated from quasi-periodic oscillations"},
            "luminosity": {"value": 1e7, "unit": "solar_luminosities", "note": "In X-rays"},
        },
        "detailed_description": (
            "M82 X-1 is the brightest X-ray source in the nearby starburst galaxy M82 and a leading candidate for an intermediate-mass black hole (IMBH). "
            "IMBHs are the missing link between stellar-mass black holes (up to ~100 solar masses) and supermassive black holes (millions to billions "
            "of solar masses). M82 X-1's X-ray luminosity is too high to be explained by a stellar-mass black hole accreting at normal rates, "
            "placing it in the category of Ultraluminous X-ray Sources (ULXs). The key evidence for its IMBH nature comes from the detection of "
            "quasi-periodic oscillations (QPOs) in its X-ray signal. The frequencies of these QPOs, when scaled by the black hole's mass, "
            "fit a pattern seen in smaller, stellar-mass black holes, suggesting a mass of around 400 solar masses. If confirmed, M82 X-1 would "
            "provide crucial evidence that IMBHs exist and could be the 'seeds' from which supermassive black holes grow."
        ),
        "scientific_facts": [
            "M82 X-1 is one of the strongest candidates for an intermediate-mass black hole.",
            "Its status as an Ultraluminous X-ray Source (ULX) means it is far brighter than any known stellar-mass X-ray binary.",
            "Quasi-periodic oscillations (QPOs) in its X-ray flux at specific frequency ratios (3:2) are the primary evidence for its mass.",
            "The mass is estimated to be around 400 solar masses, placing it squarely in the IMBH category.",
            "It is located not at the center of M82, but in a dense star-forming region, suggesting it may have formed from the runaway merger of stars in a young, massive star cluster.",
            "Alternative theories suggest it could be a smaller stellar-mass black hole undergoing super-Eddington accretion, but this is less favored.",
            "NASA's Rossi X-ray Timing Explorer (RXTE) was instrumental in discovering the QPOs.",
            "The black hole is likely accreting from a companion star, though the companion has not been directly observed.",
            "Studying IMBHs like M82 X-1 is critical to understanding the growth of supermassive black holes.",
            "Its location in a starburst galaxy provides a plausible environment for the formation of such an object.",
        ],
        "did_you_know": [
            "Intermediate-mass black holes are incredibly rare, with only a handful of strong candidates found so far.",
            "M82 X-1 is 10 times more luminous than any other X-ray source in its host galaxy.",
            "The 'flickering' of its X-ray light (the QPOs) holds the key to estimating its mass.",
        ],
        "formation_process": (
            "The leading theory for M82 X-1's formation is the 'runaway merger' scenario in a dense, young star cluster. In this environment, "
            "the most massive stars sink to the cluster's center and merge repeatedly, forming a super-star that then collapses into an IMBH. "
            "Alternatively, it could have formed from the direct collapse of a primordial, metal-free Population III star in the early universe."
        ),
        "future_evolution": (
            "As an IMBH, M82 X-1 will continue to accrete matter from its surroundings. Due to dynamical friction, it will gradually sink towards "
            "the gravitational center of the M82 galaxy. Over millions of years, it could merge with other compact objects or eventually with "
            "M82's own central supermassive black hole (if one exists), contributing to its growth."
        ),
        "related_objects": ["Messier 82 (M82)", "Stellar-Mass Black Hole", "Supermassive Black Hole", "Cygnus X-1"],
        "parent_system": "Messier 82 (M82) Galaxy",
        "child_objects": ["Accretion Disk"],
        "nasa_reference": "https://www.nasa.gov/feature/goddard/2018/astronomers-find-best-evidence-for-elusive-mid-size-black-hole",
    },


    # -------------------------------------------------------------------------
    # SECTION 7: SPACE MISSIONS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "jwst-mission")),
        "name": "James Webb Space Telescope (JWST)",
        "category": "Space Mission",
        "subtype": "Space Observatory — Infrared",
        "tags": ["mission", "telescope", "space-observatory", "infrared", "NASA", "ESA", "deep-field", "first-light"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 1.5e6, "unit": "km", "note": "Sun-Earth L2 Lagrange point"},
            "orbit": "Halo orbit around Sun-Earth L2",
            "launch_date": "December 25, 2021",
            "operational_since": "July 12, 2022",
        },
        "physical": {
            "primary_mirror_diameter": {"value": 6.5, "unit": "m"},
            "mirror_segments": 18,
            "collecting_area": {"value": 25.4, "unit": "m²"},
            "wavelength_range": {"min": 0.6, "max": 28.3, "unit": "micrometers"},
            "sunshield_size": {"value": "21m × 14m", "note": "5-layer, deployed origami structure"},
            "operating_temperature": {"value": -233, "unit": "°C", "note": "~40 K"},
            "design_life": {"value": 10, "unit": "years", "note": "Fuel extends possible 20+ years"},
            "mass": {"value": 6500, "unit": "kg"},
        },
        "detailed_description": (
            "The James Webb Space Telescope is the most powerful space observatory ever deployed, "
            "representing a 25-year, $10 billion collaboration between NASA, ESA, and CSA. JWST "
            "operates primarily in near and mid-infrared wavelengths (0.6–28 μm), allowing it to "
            "see through cosmic dust, detect the redshifted light of the earliest galaxies, and "
            "characterize exoplanet atmospheres with unprecedented sensitivity. Its primary mirror — "
            "6.5 meters in diameter, composed of 18 gold-coated beryllium hexagonal segments — "
            "collects roughly 6.25× more light than the Hubble Space Telescope. JWST orbits the "
            "Sun-Earth L2 Lagrange point, 1.5 million km from Earth, keeping the Sun, Earth, and Moon "
            "always behind its five-layer sunshield. The sunshield reduces the temperature of the "
            "telescope's cold side from ~85°C (sunlit) to ~-233°C — colder than Pluto's surface — "
            "essential for infrared sensitivity. Since releasing its first images in July 2022, JWST "
            "has detected galaxies from when the universe was less than 300 million years old, "
            "characterized atmospheres of exoplanets including CO₂ detection on WASP-39b, imaged "
            "Jupiter's auroras and rings, discovered free-floating planetary-mass objects in the Orion "
            "Nebula, and imaged the earliest known quasars. JWST's four instruments — NIRCam, NIRSpec, "
            "MIRI, and FGS/NIRISS — cover complementary wavelength ranges for imaging, spectroscopy, "
            "and coronagraphy."
        ),
        "scientific_facts": [
            "JWST's first deep field image (SMACS 0723) showed galaxies as they appeared over 13 billion years ago — capturing the universe at ~5% its current age.",
            "NIRSpec's micro-shutter assembly can observe 100+ objects simultaneously by opening specific 0.2×0.46 arcsecond shutters.",
            "JWST detected CO₂ in the atmosphere of exoplanet WASP-39b — the first clear detection of CO₂ in any exoplanet atmosphere.",
            "The telescope's precision pointing is ~1 milliarcsecond — equivalent to holding a laser pointer on a dime from 2 miles away.",
            "JWST's mid-infrared MIRI instrument is cooled to ~6 K using a dedicated cryocooler — colder than deep space background temperature.",
            "All 18 primary mirror segments must be aligned to within 1/10,000th the diameter of a human hair.",
            "JWST's perfect Ariane 5 launch trajectory was so accurate that less fuel than expected was used, potentially extending its life to 20+ years.",
            "The telescope's power is generated by a single solar array producing ~2,000 W — about the same as a domestic microwave oven.",
            "JWST data has already revised estimates of galaxy formation rates in the very early universe, challenging standard Lambda-CDM cosmological models.",
        ],
        "did_you_know": [
            "JWST was folded like origami to fit inside the Ariane 5 rocket fairing and unfolded through 50 major deployment steps over two weeks in space.",
            "The gold coating on JWST's mirrors is only ~100 nm thick — a layer thinner than a human red blood cell.",
            "JWST can detect the heat signature of a bumblebee at the distance of the Moon.",
        ],
        "formation_process": (
            "JWST was conceived in 1989 as the 'Next Generation Space Telescope'. Its development "
            "involved 300 universities, organizations, and companies in 29 US states and 14 countries. "
            "The telescope was assembled in clean rooms in Northrop Grumman's facility in Redondo Beach, "
            "California, where the sunshield and optical telescope assembly were tested at simulated "
            "space conditions. After multiple delays (originally planned for launch in 2007), JWST "
            "launched on December 25, 2021, and completed deployment and commissioning by June 2022."
        ),
        "future_evolution": (
            "JWST's primary consumable is the fuel for maintaining its halo orbit around L2. The "
            "accurate launch means it may operate well beyond its 10-year design life — potentially "
            "20+ years. Key goals include: direct imaging of rocky exoplanet atmospheres, first light "
            "galaxy chemistry, and dark matter distribution via gravitational lensing surveys. "
            "Eventually, the telescope's cryocooler will degrade and mirror alignment will drift "
            "beyond correction, ending operations. No servicing mission is planned."
        ),
        "related_objects": ["Hubble Space Telescope", "SMACS 0723 Galaxy Cluster", "WASP-39b", "Orion Nebula"],
        "parent_system": "Sun-Earth L2 Point",
        "child_objects": ["NIRCam", "NIRSpec", "MIRI", "FGS/NIRISS"],
        "nasa_reference": "https://webb.nasa.gov/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "voyager-1-mission")),
        "name": "Voyager 1",
        "category": "Space Mission",
        "subtype": "Deep Space Probe — Interstellar",
        "tags": ["mission", "probe", "interstellar", "voyager", "heliosphere", "farthest-human-made"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 24e9, "unit": "km", "note": "~161 AU as of 2024, increasing"},
            "velocity": {"value": 17.0, "unit": "km/s", "note": "Relative to the Sun"},
            "location": "Interstellar space — beyond the heliopause",
            "crossed_heliopause": {"date": "August 25, 2012"},
        },
        "physical": {
            "mass": {"value": 825.5, "unit": "kg"},
            "power_source": "Three Radioisotope Thermoelectric Generators (RTGs) — Plutonium-238",
            "power_output": {"current": {"value": "~249", "unit": "W", "note": "Declining ~4W/year"}},
            "launch_date": "September 5, 1977",
            "antenna_diameter": {"value": 3.7, "unit": "m"},
            "communication_delay": {"value": 22.5, "unit": "hours", "note": "One-way signal time as of 2024"},
        },
        "detailed_description": (
            "Voyager 1 is the most distant human-made object in existence, launched by NASA on "
            "September 5, 1977, and now traveling through interstellar space more than 160 AU from "
            "the Sun. It became the first spacecraft to cross the heliopause — the boundary where the "
            "solar wind is overtaken by the interstellar medium — on August 25, 2012, making it the "
            "first human artifact to reach interstellar space. Voyager 1 conducted flyby observations "
            "of Jupiter (March 1979) and Saturn (November 1980), returning the first close-up images "
            "of the Galilean moons and discovering active volcanic plumes on Io — a discovery that "
            "upended expectations for an icy, cratered moon. Its camera was turned off in 1990 after "
            "Carl Sagan's famous 'Pale Blue Dot' portrait of Earth from 6 billion km. The spacecraft "
            "carries a Golden Record — a gold-plated copper disc containing sounds and images of Earth, "
            "greetings in 55 languages, and music from around the world — intended as a message to any "
            "extraterrestrial civilization. Voyager 1's power output from its RTGs decreases by ~4W per "
            "year and will become insufficient to power any instrument by ~2025–2030, ending scientific "
            "operations after nearly 50 years. In interstellar space, Voyager 1's plasma wave instrument "
            "and magnetometer continue to characterize the local interstellar medium properties."
        ),
        "scientific_facts": [
            "Voyager 1 travels ~3.6 AU (538 million km) farther from the Sun every year.",
            "The plasma density measured after heliopause crossing confirmed Voyager 1 was in the local interstellar medium — ~40× denser than the heliosphere.",
            "Voyager 1 discovered active volcanic eruptions on Io — making it the first confirmed active volcano outside Earth.",
            "It discovered the thin, dark rings of Jupiter in 1979 — before the rings were visible from Earth.",
            "The 'termination shock' — where solar wind slows to subsonic speed — was crossed at ~94 AU in 2004.",
            "Voyager 1's RTGs used Pu-238, which generates heat from radioactive decay — no solar panels work at such distances.",
            "Radio signals from Voyager 1 travel at light speed and take ~22.5 hours to reach Earth (2024).",
            "The spacecraft's trajectory was shaped using a gravity assist from Jupiter, then Saturn, flinging it onto an escape trajectory.",
            "Data from Voyager 1's plasma wave instrument confirmed it had entered a new density region in 2012, consistent with interstellar medium.",
        ],
        "did_you_know": [
            "In 40,000 years, Voyager 1 will pass within 1.6 light-years of the star AC+79 3888 in Camelopardalis.",
            "The 'Pale Blue Dot' photograph, taken at Carl Sagan's request in 1990, shows Earth as a 0.12-pixel point of light in a sunbeam.",
            "Despite being 24 billion km away, NASA engineers are still in communication with Voyager 1 — making it humanity's longest-running space mission.",
        ],
        "formation_process": (
            "Voyager 1 was designed and built at NASA's Jet Propulsion Laboratory (JPL) specifically "
            "to take advantage of a rare planetary alignment occurring in 1977 — a once-every-175-year "
            "opportunity to use gravity assists from Jupiter, Saturn, Uranus, and Neptune in a single "
            "mission. The spacecraft carries 11 scientific instruments including cameras, spectrometers, "
            "magnetometers, plasma and energetic particle detectors, and cosmic ray detectors."
        ),
        "future_evolution": (
            "By ~2025–2030, Voyager 1's RTGs will generate insufficient power to run any instruments. "
            "NASA engineers have been selectively turning off heaters and instruments to extend its "
            "operational life. After communications end, Voyager 1 will continue drifting through "
            "interstellar space indefinitely — a permanent ambassador of humanity. In ~300 years it "
            "will reach the inner Oort Cloud; in ~30,000 years it will exit the outer Oort Cloud. "
            "The Golden Record may outlast Earth itself."
        ),
        "related_objects": ["Voyager 2", "Pioneer 10", "New Horizons", "Heliosphere", "Io"],
        "parent_system": "NASA Deep Space Network",
        "child_objects": ["Golden Record", "RTG Power System"],
        "nasa_reference": "https://voyager.jpl.nasa.gov/",
    },

    # -------------------------------------------------------------------------
    
    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cassini-mission")),
        "name": "Cassini–Huygens Mission",
        "category": "Space Mission",
        "subtype": "Planetary Orbiter + Atmospheric Probe",
        "tags": ["mission", "Saturn", "Titan", "Enceladus", "NASA", "ESA", "planetary-science"],
        "difficulty_level": "intermediate",
        "spatial": {
            "launch_date": "October 15, 1997",
            "arrival_at_saturn": "July 1, 2004",
            "end_of_mission": "September 15, 2017",
            "orbit_location": "Saturn system (during mission)",
        },
        "physical": {
            "cassini_mass": {"value": 5712, "unit": "kg"},
            "huygens_mass": {"value": 319, "unit": "kg"},
            "power_source": "Three RTGs (Pu-238)",
            "mission_duration": "20 years (total), 13 years at Saturn",
            "total_orbits": 293,
        },
        "detailed_description": (
            "Cassini–Huygens was a joint NASA/ESA/ASI mission that transformed our understanding "
            "of Saturn and its moons. The Cassini orbiter made 293 orbits of Saturn over 13 years, "
            "mapping the ring system in extraordinary detail, discovering Enceladus's water plumes, "
            "revealing Titan's methane seas, and characterizing the magnetosphere. The ESA Huygens "
            "probe detached from Cassini on December 25, 2004, and descended through Titan's "
            "atmosphere on January 14, 2005 — the most distant planetary landing ever achieved. "
            "Cassini's 'Grand Finale' (2017) sent it on 22 orbits through the gap between Saturn "
            "and its rings before intentionally plunging into Saturn's atmosphere to avoid "
            "contaminating Titan and Enceladus. Scientific highlights include: confirming "
            "Enceladus's global ocean, discovering Titan's lakes and seas, mapping ring particle "
            "sizes and compositions, and detecting organic molecules in Enceladus's plumes."
        ),
        "scientific_facts": [
            "Cassini made 293 orbits of Saturn, 162 targeted flybys of moons, and returned ~635 GB of science data.",
            "The Enceladus plume discovery in 2005 (confirmed with mass spectrometry in 2008) is considered Cassini's greatest discovery.",
            "Huygens's 2h 27m descent through Titan's atmosphere returned 750 images and hundreds of spectra.",
            "Cassini discovered 7 new Saturn moons during its mission.",
            "The Grand Finale (April–September 2017) passed through the ~2,000 km ring-planet gap 22 times.",
            "Cassini directly sampled material from Enceladus's plumes in 2008, detecting H₂O, CO₂, CH₄, and N₂.",
            "Saturn's north polar hexagonal jet stream — first seen by Voyager — was monitored continuously by Cassini for 13 years.",
            "RADAR aboard Cassini mapped ~60% of Titan's surface, revealing dunes, lakes, and fluvial channels.",
            "VIMS spectrometer discovered ethane lake Ontario Lacus at Titan's south pole in 2007.",
            "Cassini's magnetometer discovered that Saturn's magnetic field is perfectly aligned with its rotation axis — an unsolved mystery.",
        ],
        "did_you_know": [
            "Cassini was deliberately crashed into Saturn to prevent contaminating Enceladus or Titan with Earth microbes.",
            "The Huygens probe's battery life was ~3 hours — carefully choreographed to maximize science during descent.",
            "Cassini–Huygens flew by Venus twice, Earth once, and Jupiter once for gravity assists before reaching Saturn.",
        ],
        "related_objects": ["Saturn", "Titan", "Enceladus", "Voyager 1", "JWST"],
        "parent_system": "Saturn System",
        "nasa_reference": "https://saturn.jpl.nasa.gov/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "hubble-space-telescope")),
        "name": "Hubble Space Telescope (HST)",
        "category": "Space Mission",
        "subtype": "Space Observatory — UV/Optical/Near-IR",
        "tags": ["mission", "telescope", "space-observatory", "NASA", "ESA", "optical", "UV", "servicing-missions"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 547, "unit": "km"},
            "orbit": "Low Earth Orbit — circular, ~28.5° inclination",
            "launch_date": "April 24, 1990",
            "operational_since": "June 1993 (after corrective optics installed)",
        },
        "physical": {
            "primary_mirror_diameter": {"value": 2.4, "unit": "m"},
            "collecting_area": {"value": 4.5, "unit": "m²"},
            "wavelength_range": {"min": 0.1, "max": 2.5, "unit": "micrometers"},
            "orbital_period": {"value": 95, "unit": "minutes"},
            "mass": {"value": 11110, "unit": "kg"},
        },
        "detailed_description": (
            "The Hubble Space Telescope is one of the most scientifically productive instruments "
            "ever built — having fundamentally transformed our understanding of the universe over "
            "35+ years of operation. Launched with a flawed primary mirror, Hubble was repaired "
            "during the historic 1993 servicing mission (STS-61) when astronauts installed "
            "corrective optics. Subsequent servicing missions (1997, 1999, 2002, 2009) upgraded "
            "its instruments and extended its life. Among Hubble's defining scientific contributions: "
            "precise measurement of the Hubble constant via Cepheid variables, discovery of the "
            "accelerating universe (dark energy), direct imaging of protoplanetary disks in Orion, "
            "the Hubble Deep Field (1995), Hubble Ultra Deep Field (2004), and thousands of "
            "galaxy morphology, stellar evolution, and solar system discoveries. The final "
            "servicing mission (2009) is expected to sustain operations through the late 2020s."
        ),
        "scientific_facts": [
            "Hubble has made over 1.6 million observations and enabled 21,000+ scientific papers.",
            "The 1995 Hubble Deep Field revealed ~3,000 galaxies in a tiny patch of sky — reshaping our view of the early universe.",
            "Hubble's Cepheid distance program measured H₀ to 3% precision — resolving 50 years of cosmological debate.",
            "The discovery of dark energy (1998) — accelerating cosmic expansion — relied on Hubble Type Ia supernova distances.",
            "Hubble imaged the comet Shoemaker-Levy 9 fragments before, during, and after impact with Jupiter (1994).",
            "Hubble's ACS coronagraph directly imaged debris disks around Fomalhaut and other nearby stars.",
            "The Hubble Ultra Deep Field (2004) contains ~10,000 galaxies and looks back to within 400 million years of the Big Bang.",
            "Hubble has observed every planet in the solar system, including the discovery of new features, storms, and auroras.",
            "The Wide Field Camera 3 (installed 2009) operates UV through near-IR in a single instrument.",
            "Hubble's mirror surface accuracy is 10 nanometers — smoother than the best polished optics on Earth.",
        ],
        "did_you_know": [
            "Hubble orbits Earth at 547 km altitude, completing one orbit every 95 minutes — about 15 orbits per day.",
            "The famous 'Pillars of Creation' image (1995) was taken by Hubble — it remains one of the most reproduced astronomical photos.",
            "Hubble's gyroscopes have failed multiple times; each time, NASA engineers devised workarounds to keep it operating.",
        ],
        "related_objects": ["JWST", "Chandra X-ray Observatory", "Orion Nebula", "Deep Field Galaxies"],
        "parent_system": "NASA Great Observatories Program",
        "nasa_reference": "https://hubblesite.org/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "perseverance-rover")),
        "name": "Perseverance Rover",
        "category": "Space Mission",
        "subtype": "Mars Surface Rover + Sample Caching Mission",
        "tags": ["mission", "Mars", "rover", "astrobiology", "sample-return", "NASA", "Ingenuity"],
        "difficulty_level": "beginner",
        "spatial": {
            "launch_date": "July 30, 2020",
            "landing_date": "February 18, 2021",
            "landing_site": "Jezero Crater, Mars (18.4°N, 77.5°E)",
        },
        "physical": {
            "mass": {"value": 1025, "unit": "kg"},
            "power_source": "Multi-Mission RTG (MMRTG) — Plutonium-238",
            "power_output": {"value": 110, "unit": "W"},
            "instruments": 7,
            "cameras": 23,
        },
        "detailed_description": (
            "Perseverance is NASA's most advanced Mars rover — a car-sized mobile laboratory "
            "designed to search for signs of ancient microbial life in Jezero Crater, a 45 km "
            "ancient river delta and lake bed. Since landing in February 2021, Perseverance has "
            "collected 23+ rock and regolith core samples in hermetically sealed titanium tubes, "
            "caching them for eventual return to Earth by the Mars Sample Return (MSR) campaign. "
            "It carried the Ingenuity helicopter — the first powered aircraft on another planet — "
            "which surpassed its planned 5-flight demonstration to complete over 70 flights before "
            "communications loss in January 2024. Perseverance detected diverse igneous and "
            "sedimentary rocks in Jezero Crater, confirmed organic molecules in Martian sediments, "
            "and successfully generated oxygen from CO₂ (MOXIE experiment) — demonstrating "
            "in-situ resource utilization essential for future human missions."
        ),
        "scientific_facts": [
            "Perseverance has cached 23+ rock cores in sealed tubes — the highest-priority sample set ever collected on Mars.",
            "Ingenuity completed 72 flights (final: January 18, 2024), logging ~2 hours of total flight time.",
            "MOXIE successfully generated ~122 grams of oxygen from Martian CO₂ over the mission.",
            "Perseverance confirmed organic molecules in Jezero Crater delta sediments using Raman spectroscopy (SHERLOC instrument).",
            "The rover discovered diverse igneous rocks including olivine-rich cumulates in the crater floor.",
            "Mastcam-Z captured detailed panoramas of Jezero's ancient river delta at centimeter-scale resolution.",
            "The SuperCam laser system ablated >3,500 rock targets for spectroscopic analysis.",
            "PIXL X-ray fluorescence mapped elemental compositions of rock surfaces at sub-millimeter scale.",
            "Ingenuity demonstrated that powered flight is possible in ~1% of Earth's atmospheric density.",
            "Perseverance's landing used the 'sky crane' system — same as Curiosity — but with upgraded terrain-relative navigation.",
        ],
        "did_you_know": [
            "Ingenuity was planned as a 30-day demonstration — it flew for nearly 3 years before an issue ended its mission.",
            "The Perseverance sample tubes, once returned to Earth, could take decades to fully analyze in laboratories.",
            "Perseverance's MOXIE was the size of a car battery but successfully produced the oxygen equivalent of a small tree.",
        ],
        "related_objects": ["Mars", "Ingenuity Helicopter", "Curiosity Rover", "InSight Lander", "JWST"],
        "parent_system": "Mars / NASA Mars Exploration Program",
        "nasa_reference": "https://mars.nasa.gov/mars2020/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "new-horizons-mission")),
        "name": "New Horizons",
        "category": "Space Mission",
        "subtype": "Planetary Flyby Probe — Kuiper Belt Explorer",
        "tags": ["mission", "Pluto", "Kuiper-Belt", "NASA", "flyby", "Arrokoth", "deep-space"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 8.8e9, "unit": "km", "note": "~57 AU as of 2024"},
            "launch_date": "January 19, 2006",
            "pluto_flyby": "July 14, 2015",
            "arrokoth_flyby": "January 1, 2019",
        },
        "physical": {
            "mass": {"value": 478, "unit": "kg"},
            "power_source": "Single RTG (Pu-238)",
            "velocity": {"value": 14.4, "unit": "km/s", "note": "Relative to the Sun"},
            "instruments": 7,
        },
        "detailed_description": (
            "New Horizons is NASA's fastest spacecraft ever launched — achieving escape velocity "
            "from Earth in just 9 hours and reaching Pluto in 9.5 years after traveling 4.8 "
            "billion kilometers. Its July 14, 2015 Pluto flyby revealed an unexpectedly complex, "
            "geologically active world with nitrogen ice plains, 3 km tall water ice mountains, "
            "haze layers, and diverse terrain types — revolutionizing understanding of Kuiper Belt "
            "objects. On January 1, 2019, New Horizons flew past Arrokoth (2014 MU69) — a "
            "contact binary Kuiper Belt Object 44 AU from the Sun — capturing the most pristine "
            "solar system object ever studied close-up. Arrokoth's bilobed shape revealed a "
            "gentle 'cloud collapse' formation model for small solar system objects, revising "
            "planetesimal formation theory. New Horizons continues into the Kuiper Belt, "
            "its instruments measuring the cosmic background and interplanetary environment."
        ),
        "scientific_facts": [
            "New Horizons traveled 4.8 billion km to Pluto in 9.5 years — arriving within 72 seconds of the predicted time.",
            "Sputnik Planitia — Pluto's heart-shaped nitrogen ice plain — was New Horizons' most iconic discovery.",
            "Arrokoth is the most distant and most pristine solar system body ever visited by a spacecraft.",
            "Arrokoth's gentle contact binary shape implies formation by slow orbital decay rather than violent collision.",
            "New Horizons detected methane, ethane, and nitrogen ice on Pluto's surface via Ralph spectrometer.",
            "Alice UV spectrograph detected Pluto's atmosphere out to ~1,600 km from the surface.",
            "The mission cost ~$720 million total — one of NASA's most cost-effective planetary missions.",
            "New Horizons is now ~57 AU from the Sun, still in the Kuiper Belt, transmitting data at 1 kbps.",
            "LOngRange Reconnaissance Imager (LORRI) captured Pluto's mountains, craters, and atmospheric haze.",
            "New Horizons detected a ~50 km tall mountain (Wright Mons) on Pluto — a candidate cryovolcano.",
        ],
        "did_you_know": [
            "New Horizons launched with a small container of Clyde Tombaugh's ashes — the discoverer of Pluto.",
            "The flyby closest approach to Pluto was only 12,472 km — about the width of the United States.",
            "Arrokoth, at 44 AU, is so cold (-230°C) that its surface has barely changed since the solar system formed.",
        ],
        "related_objects": ["Pluto", "Charon", "Arrokoth", "Kuiper Belt", "Voyager 1"],
        "parent_system": "NASA New Frontiers Program",
        "nasa_reference": "https://www.nasa.gov/mission_pages/newhorizons/main/index.html",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "chandra-x-ray-observatory")),
        "name": "Chandra X-ray Observatory",
        "category": "Space Mission",
        "subtype": "Space Observatory — X-ray",
        "tags": ["mission", "telescope", "X-ray", "NASA", "space-observatory", "black-holes", "supernova-remnants"],
        "difficulty_level": "intermediate",
        "spatial": {
            "orbit": "Highly elliptical — perigee 10,000 km, apogee 140,000 km",
            "launch_date": "July 23, 1999",
            "operational_since": "1999",
        },
        "physical": {
            "mirror_diameter": {"value": 1.2, "unit": "m"},
            "wavelength_range": {"min": 0.12, "max": 12.4, "unit": "nm", "note": "0.1–10 keV X-ray band"},
            "angular_resolution": {"value": 0.5, "unit": "arcseconds", "note": "Sharpest X-ray images ever achieved"},
            "mass": {"value": 4800, "unit": "kg"},
        },
        "detailed_description": (
            "The Chandra X-ray Observatory is NASA's flagship X-ray astronomy mission — providing "
            "the sharpest X-ray images ever obtained, 10-100x better angular resolution than "
            "previous X-ray telescopes. Its highly elliptical orbit (perigee 10,000 km, apogee "
            "140,000 km) takes it outside Earth's radiation belts for ~55 hours per 64-hour orbit, "
            "maximizing uninterrupted observation time. Chandra has fundamentally transformed "
            "understanding of the hot universe: X-ray observations of galaxy clusters revealed "
            "the intracluster medium, AGN feedback cavities, and cold fronts from cluster mergers. "
            "It imaged Cassiopeia A — a supernova remnant — with sufficient detail to map element "
            "abundances from nucleosynthesis. It discovered X-ray jets from Sgr A*, characterized "
            "black hole coronae, and helped establish the Bullet Cluster as the best evidence for "
            "dark matter. In 2025, Chandra was at risk of budget cuts — a significant science "
            "policy concern for the X-ray astronomy community."
        ),
        "scientific_facts": [
            "Chandra's 0.5 arcsecond X-ray resolution is the highest ever achieved — matching HST's optical resolution.",
            "Chandra discovered X-ray bubbles in galaxy cluster hot gas inflated by AGN jets — direct evidence of AGN feedback.",
            "Cassiopeia A imaged by Chandra shows a distinct onion-layered structure of nucleosynthesis products.",
            "Chandra detected the X-ray shadow of Sgr A* during a bright X-ray flare from the galactic center.",
            "The Bullet Cluster X-ray image (Chandra) vs. gravitational lensing map provides the best evidence for dark matter.",
            "Chandra discovered that the hot gas in some clusters is surprisingly cold — the 'cooling flow' problem.",
            "X-ray binary populations in nearby galaxies were cataloged by Chandra — tracing compact object demographics.",
            "Chandra detected the X-ray afterglow of GW170817 — a neutron star merger — months after the gravitational wave event.",
            "Over 25 years of operation, Chandra has observed >15,000 targets and supported 10,000+ publications.",
            "Chandra's iridium-coated mirrors are the largest precision X-ray mirrors ever made.",
        ],
        "did_you_know": [
            "Chandra is named after Subrahmanyan Chandrasekhar — the astrophysicist who discovered the white dwarf mass limit.",
            "Chandra's highly elliptical orbit means it sometimes approaches within 10,000 km of Earth and swings out 140,000 km.",
            "X-ray photons from distant quasars observed by Chandra began their journey when multicellular life was just emerging on Earth.",
        ],
        "related_objects": ["Hubble Space Telescope", "JWST", "Sagittarius A*", "Bullet Cluster", "Cassiopeia A"],
        "parent_system": "NASA Great Observatories Program",
        "nasa_reference": "https://chandra.harvard.edu/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "europa-clipper-mission")),
        "name": "Europa Clipper",
        "category": "Space Mission",
        "subtype": "Planetary Flyby Mission — Ocean World",
        "tags": ["mission", "Europa", "Jupiter", "ocean-world", "habitability", "NASA", "flyby"],
        "difficulty_level": "intermediate",
        "spatial": {
            "launch_date": "October 14, 2024",
            "arrival_at_europa": "April 2030 (Jupiter system insertion)",
            "closest_flybys": "~25 km altitude",
        },
        "physical": {
            "mass": {"value": 6065, "unit": "kg"},
            "power_source": "Solar panels (largest ever on a planetary spacecraft) — 90 m² area",
            "instruments": 9,
            "planned_flybys": 49,
        },
        "detailed_description": (
            "Europa Clipper is NASA's flagship mission to determine whether Jupiter's moon Europa "
            "is habitable — with a global subsurface ocean, chemical energy sources, and organic "
            "chemistry. Launched October 14, 2024 aboard a SpaceX Falcon Heavy, it will arrive "
            "at Jupiter in April 2030 after gravity assists from Mars and Earth. Rather than "
            "orbiting Europa (where intense radiation from Jupiter's magnetosphere would destroy "
            "electronics in weeks), Clipper will make 49 targeted flybys of Europa from as close "
            "as 25 km — accumulating science data on each pass from safe standoff distances. "
            "Its 9 instruments will characterize the ice shell thickness, confirm the ocean's "
            "existence and composition, map surface geology, search for plumes, and measure the "
            "gravity field. The mission will determine if Europa's ocean could support life and "
            "identify candidate landing sites for a future Europa lander mission."
        ),
        "scientific_facts": [
            "Europa Clipper's solar panels span ~30 m — the largest ever deployed on a planetary science spacecraft.",
            "The mission will make 49 close flybys of Europa, accumulating science data safer than long-duration orbit.",
            "MISE (Mapping Imaging Spectrometer for Europa) will map surface composition at 25 km altitude, searching for organics and salts.",
            "E-THEMIS thermal imager will search for warm spots indicating recent geological activity.",
            "MASPEX mass spectrometer will sample Europa's thin atmosphere and any plume material during flybys.",
            "The gravity science experiment will map Europa's ice shell and ocean thickness using radio Doppler measurements.",
            "Magnetometer will characterize Europa's induced magnetic field — the most direct ocean detection method.",
            "Launch on Falcon Heavy gave Clipper enough energy for a trajectory to Jupiter without nuclear power.",
            "REASON ice-penetrating radar will measure ice shell thickness from orbit — potentially revealing ocean depth.",
            "If a plume is detected, MASPEX will fly through it and sample ocean-derived material directly.",
        ],
        "did_you_know": [
            "Europa Clipper was the largest spacecraft ever built by NASA for planetary science at launch in 2024.",
            "The spacecraft will orbit Jupiter, not Europa — making brief flybys to avoid radiation damage.",
            "Europa Clipper's MASPEX instrument can detect molecules at concentrations of parts per trillion.",
        ],
        "related_objects": ["Europa", "Jupiter", "Enceladus", "Cassini mission", "JWST"],
        "parent_system": "Jupiter System / NASA Flagship Missions",
        "nasa_reference": "https://europa.nasa.gov/",
    },

    # -------------------------------------------------------------------------
    # SECTION 8: EXOPLANETS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "proxima-centauri-b")),
        "name": "Proxima Centauri b",
        "category": "Exoplanet",
        "subtype": "Terrestrial Exoplanet — Potentially Habitable",
        "tags": ["exoplanet", "terrestrial", "habitable-zone", "nearest-exoplanet", "Proxima-Centauri", "M-dwarf-planet"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 4.243, "unit": "ly"},
            "host_star": "Proxima Centauri (Alpha Centauri C)",
            "orbital_period": {"value": 11.186, "unit": "days"},
            "semi_major_axis": {"value": 0.0485, "unit": "AU"},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"minimum": 1.07, "unit": "earth_masses", "note": "Minimum mass from RV; true mass unknown"},
            "radius": {"note": "Not directly measured; inferred ~1.1 Earth radii if rocky"},
            "equilibrium_temperature": {"value": 234, "unit": "K", "note": "Without atmosphere"},
            "orbital_eccentricity": {"value": 0.0, "note": "Assumed circular; constraints weak"},
        },
        "detailed_description": (
            "Proxima Centauri b is the closest known exoplanet to Earth, orbiting Proxima Centauri — "
            "a red dwarf M-type star that is the nearest stellar neighbor to the Sun at 4.243 light-years. "
            "Discovered in 2016 using the radial velocity method, Proxima b orbits within its star's "
            "habitable zone, completing a full orbit every 11.2 days at a distance of only 0.0485 AU — "
            "about 7 times closer to its star than Mercury is to the Sun. Despite being in the "
            "habitable zone in terms of equilibrium temperature, the habitability of Proxima b is "
            "deeply uncertain. Its M-dwarf host star is highly active — emitting powerful UV and X-ray "
            "flares far more intense than the Sun's, potentially stripping away any atmospheric "
            "layers over geological time. Proxima Centauri is also tidally locked at this orbital "
            "distance, meaning one hemisphere permanently faces the star (perpetual day) while the "
            "other faces space (perpetual night). Circulation models suggest that with a dense enough "
            "atmosphere, heat redistribution between hemispheres could maintain liquid water, but "
            "this is highly model-dependent. The Breakthrough Starshot initiative has proposed "
            "sending laser-propelled gram-scale probes to the Alpha Centauri system — potentially "
            "reaching Proxima b in ~20 years — to search for signatures of life."
        ),
        "scientific_facts": [
            "Proxima b receives ~65% of the energy flux from its star compared to Earth from the Sun, in the classical habitable zone.",
            "Proxima Centauri is a flare star — it produces superflares ~100× more energetic than typical solar flares, potentially sterilizing a surface biosphere.",
            "If Proxima b is tidally locked, its terminator zone (the ring between day and night hemispheres) might be the most habitable region.",
            "The planet was discovered via the ESPRESSO radial velocity spectrograph with a Doppler shift amplitude of ~1.38 m/s on the host star.",
            "No transits of Proxima b across its star have been confirmed — limiting direct atmospheric characterization options.",
            "A 2020 radio signal (BLC1) briefly excited interest as a potential technosignature from Proxima Centauri but was confirmed as radio frequency interference.",
            "Proxima Centauri is a member of the Alpha Centauri triple-star system, gravitationally bound at ~0.21 light-years from Alpha Cen AB.",
            "At 4.243 ly distance, a conventional spacecraft would take ~70,000–80,000 years to arrive.",
        ],
        "did_you_know": [
            "Proxima b orbits so close to its star that a year there lasts just 11.2 Earth days.",
            "The sky as seen from Proxima b would show Proxima Centauri subtending ~4× the angular diameter of the Sun as seen from Earth — a significantly larger apparent disk.",
            "Despite being 'next door' in cosmic terms, Proxima b is 270,000× farther than the ISS.",
        ],
        "formation_process": (
            "Proxima b likely formed in the outer regions of its proto-stellar disk (where solid material "
            "is more abundant at low temperatures) and subsequently migrated inward to its current "
            "tight orbit. The formation environment of M-dwarf planetary systems is different from "
            "solar-type systems — the lower stellar luminosity during the T-Tauri phase may allow "
            "volatile-rich material to condense closer to the star, potentially giving Proxima b "
            "a substantial water content."
        ),
        "future_evolution": (
            "Proxima Centauri is a low-mass M5.5V star with a fusing lifetime of several trillion years — "
            "far longer than the current age of the universe. Proxima b will remain in its current orbit "
            "essentially indefinitely. The long-term habitability depends entirely on the evolution of "
            "the stellar activity level — M-dwarfs are thought to slowly calm down over billions of years, "
            "potentially making the system more habitable with time."
        ),
        "related_objects": ["Proxima Centauri", "Alpha Centauri A", "Alpha Centauri B", "Proxima Centauri c"],
        "parent_system": "Proxima Centauri / Alpha Centauri system",
        "child_objects": [],
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/7167/proxima-cen-b/",
    },

    # -------------------------------------------------------------------------
    
    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "kepler-452b")),
        "name": "Kepler-452b",
        "category": "Exoplanet",
        "subtype": "Super-Earth — Habitable Zone, G-type Star",
        "tags": ["exoplanet", "super-earth", "habitable-zone", "Kepler", "G-type-star", "Earth-cousin"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 1402, "unit": "ly"},
            "host_star": "Kepler-452 (G2V — solar twin)",
            "orbital_period": {"value": 384.84, "unit": "days"},
            "semi_major_axis": {"value": 1.046, "unit": "AU"},
        },
        "physical": {
            "radius": {"value": 1.63, "unit": "earth_radii"},
            "mass": {"estimated_min": 3.0, "estimated_max": 5.0, "unit": "earth_masses"},
            "equilibrium_temperature": {"value": 265, "unit": "K"},
            "orbital_eccentricity": {"value": 0.0, "note": "Assumed circular"},
        },
        "detailed_description": (
            "Kepler-452b was nicknamed 'Earth's Cousin' by NASA when announced in 2015 — the "
            "first near-Earth-size planet found in the habitable zone of a solar-type (G2V) star. "
            "At 1.63 Earth radii and orbiting at 1.046 AU with a period of 385 days, it is "
            "remarkably similar to Earth in orbital configuration. However, several uncertainties "
            "remain: its mass has not been directly measured (estimated ~3–5 Earth masses based on "
            "radius), the equilibrium temperature (265 K, assuming Earth-like albedo) is slightly "
            "cooler than Earth's effective temperature, and its rocky vs. volatile-rich composition "
            "is unknown — at 1.63 Earth radii, it could be a small Neptune (mini-Neptune) with a "
            "hydrogen atmosphere rather than a rocky planet. The host star Kepler-452 is 6 billion "
            "years old — 1.5 billion years older than the Sun — raising the intriguing possibility "
            "that if the planet is rocky and habitable, life has had 1.5 billion more years to develop "
            "than on Earth."
        ),
        "scientific_facts": [
            "Kepler-452b's host star is a near-solar-twin (G2V) 6 billion years old — 1.5 Gyr older than the Sun.",
            "A radius of 1.63 Earth radii puts Kepler-452b near the 'radius gap' — it may be rocky or volatile-rich.",
            "If rocky, Kepler-452b would have ~5x Earth's gravity — challenging but potentially habitable surface conditions.",
            "Kepler-452 is ~20% brighter than the Sun and ~10% larger — its habitable zone at 1.046 AU is slightly further out.",
            "The planet was discovered by NASA's Kepler mission using the transit method with ~3 transits observed.",
            "Kepler-452b receives ~10% more energy from its star than Earth receives from the Sun.",
            "The planet could be undergoing a runaway greenhouse transition as its star brightens — analogous to Venus's fate.",
            "Despite being called 'Earth's Cousin', no spectroscopic mass or atmospheric measurement has been made.",
            "At 1,402 light-years, direct imaging of Kepler-452b is beyond current or near-future technology.",
            "Kepler-452b was one of 11 habitable-zone candidates from Kepler's catalog; it is the most Earth-like in multiple parameters.",
        ],
        "did_you_know": [
            "If Kepler-452b is rocky, it may have experienced a similar geological history to early Earth — but is 1.5 billion years ahead.",
            "NASA's announcement of Kepler-452b in July 2015 generated more public interest than any Kepler discovery before or after.",
            "The planet completes its year in 385 days — remarkably close to Earth's 365-day year.",
        ],
        "related_objects": ["Proxima Centauri b", "TRAPPIST-1 planets", "Kepler-22b", "Sun"],
        "parent_system": "Kepler-452 system",
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/1630/kepler-452-b/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "trappist-1-planets")),
        "name": "TRAPPIST-1 System",
        "category": "Exoplanet",
        "subtype": "Ultra-Cool Dwarf Star — Seven Rocky Planets",
        "tags": ["exoplanet", "rocky", "habitable-zone", "TRAPPIST", "ultra-cool-dwarf", "resonance-chain", "biosignature"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 39, "unit": "ly"},
            "host_star": "TRAPPIST-1 (M8V ultra-cool red dwarf)",
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "stellar_temperature": {"value": 2559, "unit": "K"},
            "planets": {
                "TRAPPIST-1b": {"orbital_period": "1.51 days", "radius_earth": 1.12, "zone": "too hot"},
                "TRAPPIST-1c": {"orbital_period": "2.42 days", "radius_earth": 1.10, "zone": "inner HZ edge"},
                "TRAPPIST-1d": {"orbital_period": "4.05 days", "radius_earth": 0.78, "zone": "inner HZ"},
                "TRAPPIST-1e": {"orbital_period": "6.10 days", "radius_earth": 0.92, "zone": "habitable"},
                "TRAPPIST-1f": {"orbital_period": "9.21 days", "radius_earth": 1.04, "zone": "habitable"},
                "TRAPPIST-1g": {"orbital_period": "12.35 days", "radius_earth": 1.13, "zone": "outer HZ"},
                "TRAPPIST-1h": {"orbital_period": "18.77 days", "radius_earth": 0.77, "zone": "cold"},
            },
        },
        "detailed_description": (
            "The TRAPPIST-1 system contains seven known rocky, Earth-sized planets orbiting an "
            "ultra-cool dwarf star only 39 light-years away — the nearest multi-planet system "
            "with confirmed rocky worlds. Three planets (e, f, g) orbit within the classical "
            "habitable zone. All seven planets are locked in a resonance chain — their orbital "
            "periods in integer ratios (approximately 8:5, 5:3, 3:2, 3:2, 4:3, 3:2 consecutive "
            "pairs) — an extraordinarily ordered arrangement implying smooth inward migration "
            "through the protoplanetary disk. Transit timing variations (TTVs) have measured the "
            "masses of all planets — most are predominantly rocky (iron-rock) with small volatile "
            "fractions. JWST has begun atmospheric characterization: TRAPPIST-1c was observed in "
            "secondary eclipse in 2023, revealing a bare rocky surface with no thick CO₂ "
            "atmosphere — an important constraint. TRAPPIST-1e and 1f remain the primary "
            "biosignature targets for JWST."
        ),
        "scientific_facts": [
            "TRAPPIST-1 contains 7 Earth-sized rocky planets — the most rocky worlds found in any single system.",
            "Three planets (e, f, g) orbit in the habitable zone — the most habitable-zone planets in any known system.",
            "All 7 planets are in a near-perfect resonance chain — a signature of disk migration.",
            "TRAPPIST-1c's JWST secondary eclipse showed no thick CO₂ atmosphere — it may be airless or have a thin atmosphere.",
            "TTV mass measurements show all planets are predominantly rocky with densities similar to Venus and Mars.",
            "TRAPPIST-1 is only 10% the mass of the Sun — its photosphere is barely 2.5x hotter than a light bulb filament.",
            "The star's ultraviolet and X-ray flux poses the same habitability challenges as Proxima Centauri for its planets.",
            "At 39 light-years, TRAPPIST-1 is close enough for JWST to attempt transmission spectroscopy of rocky planet atmospheres.",
            "TRAPPIST-1e is the highest-ranked biosignature target in the JWST Cycle 1 and 2 observation programs.",
            "The resonance chain allowed scientists to find the planets' orbital arrangement using N-body simulations.",
        ],
        "did_you_know": [
            "If TRAPPIST-1e has an atmosphere and surface water, sunsets would be orange-red — the host star is cooler and dimmer than our Sun.",
            "All seven TRAPPIST-1 planets are tidally locked to their star — perpetual day on one side, eternal night on the other.",
            "TRAPPIST-1 is so dim that even at 39 light-years, it's invisible to the naked eye at magnitude 19.",
        ],
        "related_objects": ["Proxima Centauri b", "Kepler-452b", "JWST", "LHS 1140b"],
        "parent_system": "TRAPPIST-1 system",
        "nasa_reference": "https://exoplanets.nasa.gov/trappist1/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "hot-jupiter-51-pegasi-b")),
        "name": "51 Pegasi b",
        "category": "Exoplanet",
        "subtype": "Hot Jupiter — First Exoplanet Around a Sun-like Star",
        "tags": ["exoplanet", "hot-jupiter", "first-discovery", "51-Pegasi", "radial-velocity", "Nobel-Prize"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 50.45, "unit": "ly"},
            "host_star": "51 Pegasi (G2IV)",
            "orbital_period": {"value": 4.23, "unit": "days"},
            "semi_major_axis": {"value": 0.052, "unit": "AU"},
        },
        "physical": {
            "mass": {"minimum": 0.468, "unit": "Jupiter_masses"},
            "radius": {"estimated": 1.9, "unit": "Jupiter_radii"},
            "equilibrium_temperature": {"value": 1260, "unit": "K"},
        },
        "detailed_description": (
            "51 Pegasi b — informally nicknamed 'Dimidium' — is one of the most historically "
            "significant planets ever discovered. Detected in 1995 by Michel Mayor and Didier "
            "Queloz using the radial velocity method, it was the first exoplanet confirmed around "
            "a main-sequence Sun-like star, launching the modern era of exoplanet science. "
            "51 Peg b is a 'hot Jupiter' — a gas giant half Jupiter's mass orbiting its star at "
            "only 0.052 AU (7.8 million km) — just 8% Mercury's distance from the Sun. "
            "Its orbital period is only 4.23 days and its equilibrium temperature ~1,260 K. "
            "Hot Jupiters were completely unexpected — standard planetary formation theory "
            "predicted gas giants could only form beyond the frost line (several AU out) "
            "and then migrate inward. The discovery forced a revolution in understanding planetary "
            "migration. Mayor and Queloz received the 2019 Nobel Prize in Physics for this discovery."
        ),
        "scientific_facts": [
            "51 Pegasi b's discovery in 1995 launched the modern exoplanet era and forced planetary formation theory to be rewritten.",
            "Michel Mayor and Didier Queloz received the 2019 Nobel Prize in Physics for discovering 51 Peg b.",
            "Hot Jupiters like 51 Peg b are thought to form in the outer disk then migrate inward via disk-planet interaction.",
            "The radial velocity amplitude from 51 Peg is ~56 m/s — comparable to a fast sprint.",
            "Atmospheric studies of hot Jupiters through transmission spectroscopy use 51 Peg b as a benchmark system.",
            "Tidal locking likely synchronizes 51 Peg b's rotation to its orbital period — one face permanently toward the star.",
            "Hot Jupiters are rare (~1% of sun-like stars) but were overrepresented in early discoveries due to detection bias.",
            "51 Peg b's stellar host is a slightly evolved G2IV subgiant similar in temperature to our Sun.",
            "ESPRESSO spectrograph confirmed reflected starlight from 51 Peg b's atmosphere in 2019 — direct detection.",
            "The 4.23-day period of 51 Peg b is so short that Mayor and Queloz initially doubted their own signal.",
        ],
        "did_you_know": [
            "Before 51 Peg b's discovery, most astronomers assumed solar system architecture was universal — all that changed in 1995.",
            "51 Pegasi is a naked-eye star (magnitude 5.49) — you can see the home of the first-known hot Jupiter without a telescope.",
            "Mayor and Queloz's spectrograph measured Doppler shifts equivalent to a walking pace — extraordinary precision for 1995.",
        ],
        "related_objects": ["Proxima Centauri b", "TRAPPIST-1 system", "Kepler-452b", "Hot Jupiters"],
        "parent_system": "51 Pegasi system",
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/1038/51-peg-b/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "kepler-186f")),
        "name": "Kepler-186f",
        "category": "Exoplanet",
        "subtype": "Rocky Exoplanet — First Earth-Sized HZ Planet",
        "tags": ["exoplanet", "rocky", "habitable-zone", "Kepler", "Earth-sized", "M-dwarf"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 500, "unit": "ly"},
            "host_star": "Kepler-186 (M1V red dwarf)",
            "orbital_period": {"value": 129.9, "unit": "days"},
            "semi_major_axis": {"value": 0.432, "unit": "AU"},
        },
        "physical": {
            "radius": {"value": 1.17, "unit": "earth_radii"},
            "equilibrium_temperature": {"value": 188, "unit": "K", "note": "With Earth's albedo; possibly warmer with greenhouse"},
        },
        "detailed_description": (
            "Kepler-186f was the first validated Earth-sized planet in the habitable zone of another "
            "star, discovered in 2014. At only 1.17 Earth radii, it is most likely a rocky planet — "
            "below the radius threshold (~1.5 Earth radii) where planets transition from rocky to "
            "volatile-dominated compositions. It orbits an M1-type red dwarf at 0.432 AU — within "
            "the classical habitable zone where liquid water could exist with a suitable atmosphere. "
            "However, its equilibrium temperature of ~188 K (without atmosphere) means it would be "
            "frozen without a significant greenhouse effect. Its parent star is cooler and dimmer "
            "than the Sun, and as with all M-dwarf planets, stellar flares and tidal locking are "
            "habitability challenges. Kepler-186f remains one of the most Earth-like exoplanets "
            "in terms of size and orbital configuration, but it is too distant for atmospheric "
            "characterization with current instruments."
        ),
        "scientific_facts": [
            "Kepler-186f was the first validated Earth-sized planet in a stellar habitable zone — a landmark 2014 discovery.",
            "A radius of 1.17 Earth radii strongly suggests a rocky composition below the radius gap.",
            "Kepler-186 is a 5-planet system — Kepler-186b, c, d, e are interior to f and likely too hot to be habitable.",
            "Tidal locking of Kepler-186f is likely — all sunlight falls on one hemisphere.",
            "Its parent star emits most energy in infrared — photosynthesis using IR-absorbing pigments would be necessary.",
            "Kepler-186f receives ~32% of Earth's sunlight flux — it is closer to Mars in illumination.",
            "At 500 ly, no current telescope can characterize Kepler-186f's atmosphere.",
            "The Kepler-186 system has a flat, coplanar architecture consistent with disk formation.",
            "Kepler-186f's orbital eccentricity is poorly constrained — circular is assumed but not confirmed.",
            "Follow-up radial velocity measurements are not feasible with current spectrographs due to the star's faintness.",
        ],
        "did_you_know": [
            "Kepler-186f was nicknamed 'Earth's Twin' in 2014, though the host star makes it more of a distant cousin.",
            "Its sun (Kepler-186) would appear as a smaller, redder disk than our Sun — it's only 50% the Sun's mass.",
            "If Kepler-186f has plants, they may be darker than Earth's — absorbing the red and infrared light from the M-dwarf.",
        ],
        "related_objects": ["TRAPPIST-1 system", "Proxima Centauri b", "Kepler-452b"],
        "parent_system": "Kepler-186 system",
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/1637/kepler-186-f/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "wasp-39b")),
        "name": "WASP-39b",
        "category": "Exoplanet",
        "subtype": "Hot Saturn — JWST Atmospheric Benchmark",
        "tags": ["exoplanet", "hot-saturn", "JWST", "atmospheric-spectroscopy", "CO2-detection", "photochemistry"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 700, "unit": "ly"},
            "host_star": "WASP-39 (G7V)",
            "orbital_period": {"value": 4.06, "unit": "days"},
            "semi_major_axis": {"value": 0.049, "unit": "AU"},
        },
        "physical": {
            "mass": {"value": 0.28, "unit": "Jupiter_masses"},
            "radius": {"value": 1.27, "unit": "Jupiter_radii"},
            "equilibrium_temperature": {"value": 1116, "unit": "K"},
        },
        "detailed_description": (
            "WASP-39b became one of the most scientifically important exoplanets in history when "
            "JWST targeted it during Early Release Science observations in 2022. A 'hot Saturn' — "
            "a gas giant ~Saturn's mass but 27% Jupiter's radius — orbiting its G-type star every "
            "4 days, WASP-39b is bloated by intense stellar heating. JWST's NIRSpec, NIRCam, and "
            "NIRISS instruments detected an unprecedented array of atmospheric molecules: water "
            "(H₂O), carbon dioxide (CO₂ — first definitive detection in any exoplanet), sulfur "
            "dioxide (SO₂ — first detection in any exoplanet), carbon monoxide (CO), sodium (Na), "
            "potassium (K), and methane (CH₄). The SO₂ detection was particularly remarkable — "
            "it is a photochemistry product formed when stellar UV breaks apart H₂O and H₂S, "
            "demonstrating for the first time that photochemical processes are detectable in "
            "exoplanet atmospheres. WASP-39b's atmospheric data provided unprecedented insight "
            "into gas giant formation and atmospheric chemistry, establishing JWST as a "
            "transformative tool for exoplanet science."
        ),
        "scientific_facts": [
            "JWST provided the first definitive CO₂ detection in any exoplanet atmosphere — in WASP-39b in 2022.",
            "SO₂ in WASP-39b's atmosphere was the first detection of a photochemically produced gas in any exoplanet.",
            "The atmospheric spectrum revealed H₂O, CO₂, CO, SO₂, Na, K, CH₄ — the most complete exoplanet atmosphere characterization to date.",
            "WASP-39b's SO₂ abundance implies vigorous photochemical processing in its upper atmosphere.",
            "The carbon-to-oxygen ratio (C/O) measured from WASP-39b gives clues about where the planet formed in its disk.",
            "WASP-39b's transmission spectrum was measured across 0.6–5.2 μm — the widest wavelength range for any exoplanet.",
            "The planet is 'puffed up' — its radius is larger than expected for its mass due to tidal heating and stellar irradiation.",
            "Multiple independent JWST instrument modes were tested on WASP-39b — all four achieved science-quality exoplanet spectra.",
            "The exquisite data quality of WASP-39b observations calibrated JWST's exoplanet atmospheric retrieval pipelines.",
            "WASP-39b orbits close enough to be tidally locked — its dayside is permanently ~1,100 K hotter than the nightside.",
        ],
        "did_you_know": [
            "WASP-39b's first JWST CO₂ spectrum was published within 2 months of the data being taken — unprecedented speed in astronomy.",
            "The SO₂ detection in WASP-39b confirmed theoretically predicted photochemistry that had never before been observed on another world.",
            "WASP-39b's characterization demonstrated JWST's ability to detect biosignatures if present in rocky planet atmospheres.",
        ],
        "related_objects": ["JWST", "TRAPPIST-1 system", "51 Pegasi b", "Hot Jupiters"],
        "parent_system": "WASP-39 system",
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/2008/wasp-39-b/",
    },


    # -------------------------------------------------------------------------
    # SECTION 9: ASTEROID & SMALL BODIES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "asteroid-ceres")),
        "name": "Ceres",
        "category": "Dwarf Planet",
        "subtype": "Dwarf Planet — Largest Asteroid Belt Object",
        "tags": ["dwarf-planet", "asteroid", "ice-body", "water-world-candidate", "asteroid-belt", "Dawn-mission"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"min": 263e6, "max": 943e6, "unit": "km"},
            "semi_major_axis": {"value": 2.77, "unit": "AU"},
            "orbital_period": {"value": 4.60, "unit": "years"},
            "galaxy_reference": "Solar System — Asteroid Belt",
        },
        "physical": {
            "mass": {"value": 9.393e20, "unit": "kg", "note": "~1/3 of total asteroid belt mass"},
            "radius": {"value": 473, "unit": "km"},
            "density": {"value": 2162, "unit": "kg/m³"},
            "surface_temperature": {"min": -105, "max": 35, "mean": -105, "unit": "°C"},
            "rotation_period": {"value": 9.074, "unit": "hours"},
            "differentiated": True,
            "internal_structure": "Rocky core, icy mantle, possibly brine layer",
        },
        "detailed_description": (
            "Ceres is the only dwarf planet in the inner solar system and the largest object in the "
            "asteroid belt, located between Mars and Jupiter. With a mean diameter of ~946 km, Ceres "
            "contains roughly one-third of the total mass of the entire asteroid belt. It was first "
            "discovered by Giuseppe Piazzi on January 1, 1801, and was originally classified as a "
            "planet before being reclassified as an asteroid and later as a dwarf planet in 2006. "
            "NASA's Dawn spacecraft, which orbited Ceres from March 2015 to November 2018, revealed "
            "a strikingly geologically active world. The most striking features are the bright spots "
            "in Occator Crater — patches of sodium carbonate (natrite) deposited by briny water "
            "welling up from a subsurface liquid reservoir and evaporating on the surface. This "
            "confirmed that Ceres has a liquid layer — likely a salty brine ~40 km below the surface, "
            "possibly remnant from early internal heating. Ceres also shows evidence of cryovolcanism: "
            "the 4 km tall Ahuna Mons is interpreted as a cryovolcanic dome formed within the last "
            "~210 million years by viscous salt-ice mixture extruded from the interior. The surface "
            "shows a mix of hydrated silicates, ammoniated clays (suggesting material from the outer "
            "solar system), carbonates, and dark organic material, pointing to a complex chemistry "
            "with prebiotic significance."
        ),
        "scientific_facts": [
            "The bright Occator Crater spots — initially unexplained from Hubble images — were confirmed by Dawn to be sodium carbonate salt deposits.",
            "Ceres contains more fresh water than all of Earth's surface oceans, stored as ice in its mantle.",
            "Ahuna Mons is a 4 km tall cryovolcanic structure — estimated to have erupted within the last 210 million years.",
            "Organic compounds were detected on Ceres's surface by Dawn's Visible and Infrared Mapping Spectrometer — concentrated north of Ernutet Crater.",
            "Ammonia-bearing clays on Ceres suggest it may have formed in the outer solar system and migrated inward.",
            "Dawn detected transient water vapor plumes from Ceres in 2012 using the Herschel Space Observatory.",
            "Ceres's surface lacks large impact craters expected for its age — viscous relaxation of icy crust may have erased them.",
            "The dawn spacecraft was the first to orbit two extraterrestrial targets (Vesta, then Ceres) on the same mission.",
            "Ceres has no known moons — unusual for a differentiated body of its size.",
        ],
        "did_you_know": [
            "Ceres is large enough to be nearly spherical — hydrostatic equilibrium shaped it into a slightly oblate spheroid.",
            "If the water ice on Ceres could be melted, it would create an ocean ~100 km deep covering the entire surface.",
            "Ceres's day is only 9 hours long — a faster rotation than Mars.",
        ],
        "formation_process": (
            "Ceres accreted early in the solar system's history, within the first 10 million years. "
            "Its high ice content and ammoniated minerals suggest it may have originated in the outer "
            "solar system — perhaps near the formation zone of Uranus or Neptune — and was scattered "
            "inward by giant planet migration (as described in the Nice Model). It differentiated "
            "early, with a rocky core forming and an icy mantle surrounding it, heated by radioactive "
            "decay of short-lived isotopes (Al-26, Fe-60)."
        ),
        "future_evolution": (
            "Ceres will remain in its stable asteroid belt orbit for the foreseeable future. "
            "Its subsurface brine layer will continue to slowly crystallize and cool over geological "
            "time. Cryovolcanic activity will decline as internal heat sources are exhausted. "
            "In the very long term, Ceres may be perturbed by Jupiter resonances, but this timescale "
            "is billions of years."
        ),
        "related_objects": ["Vesta", "Pallas", "Dawn Spacecraft", "Jupiter", "Asteroid Belt"],
        "parent_system": "Solar System — Asteroid Belt",
        "child_objects": ["Occator Crater", "Ahuna Mons"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/dwarf-planets/ceres/overview/",
    },

     # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "pluto-dwarf-planet")),
        "name": "Pluto",
        "category": "Dwarf Planet",
        "subtype": "Dwarf Planet — Plutino (Plutonian Object)",
        "tags": ["dwarf-planet", "ice-world", "trans-neptunian", "Kuiper-belt", "New-Horizons", "geologically-active"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"min": 4.85e9, "max": 7.38e9, "unit": "km"},
            "semi_major_axis": {"value": 39.48, "unit": "AU"},
            "orbital_period": {"value": 248, "unit": "years"},
            "orbital_eccentricity": {"value": 0.249, "note": "Highly elliptical orbit"},
            "galaxy_reference": "Solar System — Kuiper Belt",
        },
        "physical": {
            "mass": {"value": 1.303e22, "unit": "kg"},
            "radius": {"value": 1187, "unit": "km"},
            "density": {"value": 1854, "unit": "kg/m³"},
            "surface_temperature": {"mean": -380, "unit": "K", "note": "One of coldest known surfaces"},
            "rotation_period": {"value": 6.39, "unit": "days", "note": "Retrograde rotation"},
            "moons": {"count": 5, "primary": "Charon (binary system)"},
        },
        "detailed_description": (
            "Pluto is a dwarf planet and the prototype plutino — a trans-Neptunian object in 2:3 "
            "orbital resonance with Neptune. Discovered by Clyde Tombaugh on February 18, 1930, "
            "it was long considered the ninth planet until its reclassification in 2006 by the IAU. "
            "NASA's New Horizons spacecraft flew past Pluto on July 14, 2015, providing humanity's "
            "first close-up images and revealing a far more geologically diverse world than anticipated. "
            "Pluto features nitrogen and methane ice plains, towering water-ice mountains, dark organic-rich "
            "terrain, and evidence of past cryovolcanism. The vast left-facing heart-shaped basin, "
            "informally called Tombaugh Regio, contains the bright nitrogen-ice Sputnik Planitia (~4 km deep) "
            "flanked by water-ice mountains reaching 6 km. Pluto orbits in a binary system with its largest "
            "moon Charon (diameter 1,207 km), making them nearly co-orbital. Five-fold symmetry in Pluto's "
            "albedo spots suggests past resonance-driven activity. A thin nitrogen atmosphere exists during "
            "its closest approach to the Sun; at aphelion it freezes onto the surface."
        ),
        "scientific_facts": [
            "Pluto and Charon orbit a common barycenter outside Pluto's surface, making them a true binary system.",
            "The nitrogen ice plains (Sputnik Planitia) appear to be younger than expected, possibly due to cryovolcanism or glacier flow.",
            "New Horizons discovered five moons orbiting Pluto-Charon: Charon, Styx, Nix, Kerberos, and Hydra.",
            "Pluto's retrograde rotation is likely due to a giant impact early in solar system history.",
            "Its thin atmosphere (92% nitrogen, 8% methane) expands and contracts with its eccentric orbit.",
            "Water-ice mountains near Tombaugh Regio reach heights of 6 km, unusual at such low temperatures.",
            "Pluto's orbital period is 248 years — it hasn't completed one full orbit since its discovery.",
            "New Horizons data suggests subsurface oceans may underlie Sputnik Planitia.",
            "Pluto likely formed in the inner solar system and was scattered outward by giant planet migration.",
            "Its density of ~1,854 kg/m³ indicates a rocky core with an icy mantle.",
        ],
        "did_you_know": [
            "From Pluto, the Sun appears as a bright star in the sky, barely brighter than the full Moon from Earth.",
            "It took New Horizons 9.5 years to travel from Earth to Pluto.",
            "Pluto's formal designation is 134340 Pluto — a number typically reserved for asteroids.",
        ],
        "formation_process": (
            "Pluto accreted in the inner solar system, likely within 30-50 AU of the young Sun, during the "
            "first few million years of planetary formation. It grew to planetary size and may have been "
            "ejected outward by gravitational interactions during the late heavy bombardment or through "
            "interactions with Neptune's migration. Its binary companion Charon formed either via giant "
            "impact or capture."
        ),
        "future_evolution": (
            "Pluto will remain on its current 248-year orbit indefinitely. Its atmosphere will gradually freeze "
            "as it continues moving away from the Sun over the next century. Cryovolcanism may occasionally "
            "resurface its skin, but overall it will remain a frozen, geologically slow-changing world."
        ),
        "related_objects": ["Charon", "Eris", "Haumea", "New Horizons", "Kuiper Belt"],
        "parent_system": "Solar System — Kuiper Belt",
        "child_objects": ["Charon", "Styx", "Nix", "Kerberos", "Hydra"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/dwarf-planets/pluto/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "eris-dwarf-planet")),
        "name": "Eris",
        "category": "Dwarf Planet",
        "subtype": "Dwarf Planet — Most Massive Trans-Neptunian Object",
        "tags": ["dwarf-planet", "trans-neptunian", "scattered-disk", "ice-world", "high-eccentricity", "Dysnomia"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"min": 5.7e9, "max": 14.6e9, "unit": "km"},
            "semi_major_axis": {"value": 67.7, "unit": "AU"},
            "orbital_period": {"value": 557, "unit": "years"},
            "orbital_eccentricity": {"value": 0.441, "note": "Highly elliptical, highly inclined orbit"},
            "galaxy_reference": "Solar System — Scattered Disk",
        },
        "physical": {
            "mass": {"value": 1.66e22, "unit": "kg", "note": "27% more massive than Pluto"},
            "radius": {"value": 1163, "unit": "km", "note": "Slightly smaller but more massive than Pluto"},
            "density": {"value": 2520, "unit": "kg/m³", "note": "More dense than Pluto"},
            "surface_temperature": {"mean": -240, "unit": "K"},
            "moons": {"count": 1, "primary": "Dysnomia"},
        },
        "detailed_description": (
            "Eris is the most massive known dwarf planet and the prototype for resonant scattered disk objects. "
            "Discovered on January 5, 2005, by Mike Brown, Chad Trujillo, and David Rabinowitz, it triggered "
            "the astronomical drama that led to Pluto's reclassification and the creation of the 'dwarf planet' "
            "category. Orbiting at an average distance of 67.7 AU (nearly twice Pluto's average), Eris follows "
            "an extremely eccentric, highly inclined orbit that takes approximately 557 years to complete. "
            "At its closest approach (perihelion ~38 AU), it comes closer to the Sun than Pluto due to its "
            "orbital eccentricity and Pluto's 2:3 resonance lock. Eris is slightly smaller than Pluto but "
            "significantly more dense, suggesting a rocky-to-icy composition. It is shrouded in a thin atmosphere "
            "of methane, nitrogen, and carbon monoxide ice. Eris has one moon, Dysnomia (formerly 'Gabrielle'). "
            "Its discovery was instrumental in the discovery of hundreds of other Kuiper Belt and scattered disk "
            "objects, revolutionizing our understanding of the outer solar system."
        ),
        "scientific_facts": [
            "Eris is 27% more massive than Pluto — the most massive dwarf planet known.",
            "Its discovery forced astronomers to formally define 'planet', resulting in the dwarf planet category.",
            "Eris's orbit is so eccentric and inclined that it is dynamically separate from the main Kuiper Belt.",
            "It orbits at 67.7 AU on average, placing it in the scattered disk region beyond the classical Kuiper Belt.",
            "Its methane-rich surface suggests it is colder than Pluto, reaching ~240 K even at perihelion.",
            "Eris's density (~2,520 kg/m³) is higher than Pluto's, indicating a larger rocky core fraction.",
            "The moon Dysnomia has an orbital period of 15.77 days around Eris.",
            "Eris was nicknamed 'Xena' by its discoverers, inspired by the warrior princess television character.",
            "Its extreme eccentricity suggests it may have been scattered outward by gravitational interactions.",
            "Spectroscopy shows its surface is rich in volatile ices — methane, nitrogen, and carbon monoxide.",
        ],
        "did_you_know": [
            "At perihelion, Eris briefly becomes closer to the Sun than Pluto, despite its larger average distance.",
            "The name 'Eris' comes from the Greek goddess of discord — fitting given the chaos its discovery caused in astronomy.",
            "Eris is so distant that sunlight takes 9 hours to reach it.",
        ],
        "formation_process": (
            "Eris likely formed in the inner solar system but was scattered outward into the scattered disk by "
            "gravitational interactions during the Nice model event (believed to have occurred ~4.1 billion years ago). "
            "Its current extremely eccentric, highly inclined orbit is the result of this dynamical scattering."
        ),
        "future_evolution": (
            "Eris will remain in its distant scattered disk orbit for billions of years. Its icy surface will "
            "gradually sublimate and redeposit closer to the poles due to slow seasonal climate variations. "
            "Over cosmic timescales, it may suffer gravitational perturbations that could alter its orbit."
        ),
        "related_objects": ["Pluto", "Haumea", "Makemake", "Dysnomia", "Scattered Disk"],
        "parent_system": "Solar System — Scattered Disk",
        "child_objects": ["Dysnomia"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/dwarf-planets/eris/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "haumea-dwarf-planet")),
        "name": "Haumea",
        "category": "Dwarf Planet",
        "subtype": "Dwarf Planet — Elongated/Rugby-Ball Shaped",
        "tags": ["dwarf-planet", "trans-neptunian", "Kuiper-belt", "ice-world", "fast-rotation", "ring-system"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"min": 6.29e9, "max": 8.05e9, "unit": "km"},
            "semi_major_axis": {"value": 43.3, "unit": "AU"},
            "orbital_period": {"value": 285, "unit": "years"},
            "galaxy_reference": "Solar System — Kuiper Belt",
        },
        "physical": {
            "mass": {"value": 4.006e21, "unit": "kg"},
            "dimensions": {"a": 2100, "b": 1680, "c": 1080, "unit": "km", "shape": "Ellipsoid (rugby-ball)"},
            "density": {"value": 2600, "unit": "kg/m³", "note": "Higher than Pluto/Eris, suggesting more rocky core"},
            "rotation_period": {"value": 3.915, "unit": "hours", "note": "Extremely fast rotation"},
            "ring_system": {"count": 2, "primary": "Dense ring system"},
            "moons": {"count": 2, "names": "Hiʻiaka, Nāmaka"},
        },
        "detailed_description": (
            "Haumea is a dwarf planet of striking geometric distinctiveness — elongated into a rugby-ball or "
            "cigar shape due to its extremely rapid rotation. Discovered on December 28, 2004, by Mike Brown "
            "and colleagues, Haumea orbits in the classical Kuiper Belt at ~43 AU distance. Its most remarkable "
            "feature is its shape: measuring approximately 2,100 km × 1,680 km × 1,080 km, it is the most "
            "distorted dwarf planet, with its elongation driven by centrifugal forces from its 3.9-hour rotation — "
            "the fastest of any large solar system body. Even more astonishing, Haumea possesses a ring system, "
            "making it the first known dwarf planet with rings. The rings are likely composed of collisional debris "
            "from past impacts or are remnants of its formation. Haumea is accompanied by two moons, Hiʻiaka "
            "(discovered 2005) and Nāmaka (discovered 2011). Its surface is covered in nearly-pure water ice, "
            "suggesting it may have been re-surfaced by tidal heating or past cryovolcanism."
        ),
        "scientific_facts": [
            "Haumea rotates every 3.915 hours — the fastest large object in the solar system.",
            "This rapid rotation causes extreme centrifugal deformation, giving it a rugby-ball shape.",
            "Haumea possesses a ring system, making it the first known ringed dwarf planet.",
            "Its surface is composed almost entirely of nearly-pure water ice — unusual for such a distant object.",
            "The moons are thought to have resulted from a past collision with another Kuiper Belt object.",
            "Haumea's name comes from the Hawaiian goddess of fertility.",
            "Its dimensions (~2,100 × 1,680 × 1,080 km) make it significantly elongated along its rotation axis.",
            "A family of similar-composition objects in the Kuiper Belt, called Haumea family members, are thought to be collision debris.",
            "Spectroscopy reveals crystalline water ice on the surface — indicating recent resurfacing.",
            "Despite its large mass, its density (2,600 kg/m³) is intermediate between Pluto and Eris.",
        ],
        "did_you_know": [
            "If you stood on Haumea's equator, the centrifugal acceleration would be ~1/7 of Earth's gravity.",
            "Haumea's entire day is shorter than many commercial airline flights.",
            "The rings around Haumea are denser and more defined than Saturn's rings per unit cross-section.",
        ],
        "formation_process": (
            "Haumea likely collided with another Kuiper Belt object early in its history, breaking into pieces "
            "and imparting the angular momentum that drives its current rapid rotation. The fragments from this "
            "collision became Hiʻiaka and Nāmaka, and possibly formed the ring system. Its icy composition suggests "
            "it formed beyond the frost line in the primordial solar system."
        ),
        "future_evolution": (
            "Haumea will continue its rapid rotation for billions of years. Its rings will gradually dissipate as "
            "particles collide and decay. The moons may eventually spiral outward due to orbital decay. Its icy "
            "surface will gradually darken as cosmic rays darken superficial ices."
        ),
        "related_objects": ["Pluto", "Eris", "Makemake", "Hiʻiaka", "Nāmaka", "Saturn's Rings"],
        "parent_system": "Solar System — Kuiper Belt",
        "child_objects": ["Hiʻiaka", "Nāmaka", "Ring System"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/dwarf-planets/haumea/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "makemake-dwarf-planet")),
        "name": "Makemake",
        "category": "Dwarf Planet",
        "subtype": "Dwarf Planet — Classical Kuiper Belt Object",
        "tags": ["dwarf-planet", "trans-neptunian", "Kuiper-belt", "ice-world", "methane-surface"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"min": 6.77e9, "max": 7.59e9, "unit": "km"},
            "semi_major_axis": {"value": 45.8, "unit": "AU"},
            "orbital_period": {"value": 310, "unit": "years"},
            "galaxy_reference": "Solar System — Kuiper Belt",
        },
        "physical": {
            "mass": {"value": 2.882e21, "unit": "kg"},
            "radius": {"value": 715, "unit": "km", "note": "Approximately, based on occultation data"},
            "density": {"value": 2000, "unit": "kg/m³", "note": "Estimated"},
            "surface_temperature": {"mean": -243, "unit": "K"},
            "moons": {"count": 1, "primary": "S/2015 (136472) 1"},
        },
        "detailed_description": (
            "Makemake is the second-largest and the fourth-brightest dwarf planet, orbiting in the classical "
            "Kuiper Belt at 45.8 AU distance. Discovered on March 31, 2005, by Mike Brown, Chadwick Trujillo, "
            "and David Rabinowitz, it was one of the discoveries that prompted the IAU to formalize the dwarf "
            "planet category. Makemake is recognizable by its incredibly low albedo (bright reflectivity), "
            "attributed to a surface covered in methane, ethane, and toluene ices. Its name derives from the "
            "Rapa Nui (Easter Island) creation deity. Being a classical Kuiper Belt object, Makemake's orbit "
            "is relatively circular and prograde. It was found to have a moon, S/2015 (136472) 1, discovered "
            "in 2015. A significant discovery occurred on April 23, 2011, when a stellar occultation revealed "
            "evidence for a possible thin atmosphere or ring system — later analysis favored the atmospheric "
            "hypothesis. Its extremely high albedo (57–65%) makes it one of the brightest distant objects, "
            "despite its faintness in visible light due to sheer distance."
        ),
        "scientific_facts": [
            "Makemake has an extremely high albedo (57–65%), likely from fresh methane and ethane ice.",
            "A 2011 stellar occultation suggested Makemake may possess a thin nitrogen atmosphere.",
            "Its discovery reinforced the need to precisely define 'planet', leading to the dwarf planet category.",
            "Makemake's name comes from the Rapa Nui (Easter Island) creation god — culturally distinct from other dwarf planets.",
            "A moon was detected orbiting it in 2015, designated S/2015 (136472) 1.",
            "It is one of the brightest known Kuiper Belt objects relative to its size.",
            "Spectroscopy reveals its surface composition includes methane, ethane, and possibly toluene gases frozen as ice.",
            "Its orbital period of 310 years makes Makemake one of the slowest-orbiting dwarf planets.",
            "Occultation data suggests it may have a diameter of ~1,450 km, making it slightly smaller than Haumea.",
            "Its mean surface temperature is similar to Pluto's, around 243 K.",
        ],
        "did_you_know": [
            "Makemake is so bright relative to other Kuiper Belt objects that it was initially called 'Easterbunny'.",
            "Its extremely reflective surface suggests it is geologically young or regularly refreshed by cometary impacts.",
            "From Makemake's surface, the Sun would appear ~1,600 times dimmer than from Earth.",
        ],
        "formation_process": (
            "Makemake formed in the classical Kuiper Belt region approximately 4.6 billion years ago as part of "
            "the primordial planetesimal swarm. Its relatively circular, stable orbit suggests it remained near "
            "its formation location and was not significantly scattered by giant planet migration, unlike Eris."
        ),
        "future_evolution": (
            "Makemake will continue its slow 310-year orbit indefinitely. Its methane and ethane ices will "
            "gradually darken due to cosmic ray bombardment, eventually matching the darker hues of Kuiper Belt "
            "objects like Gonggong. Its thin atmosphere (if confirmed) will gradually be lost to space."
        ),
        "related_objects": ["Pluto", "Eris", "Haumea", "Kuiper Belt", "Stellar Occultation"],
        "parent_system": "Solar System — Kuiper Belt",
        "child_objects": ["S/2015 (136472) 1"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/dwarf-planets/makemake/overview/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "gonggong-dwarf-planet")),
        "name": "Gonggong",
        "category": "Dwarf Planet",
        "subtype": "Dwarf Planet — Scattered Disk, High Albedo",
        "tags": ["dwarf-planet", "trans-neptunian", "scattered-disk", "ice-world", "high-reflectivity", "Xiangliu"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"min": 8.36e9, "max": 11.7e9, "unit": "km"},
            "semi_major_axis": {"value": 67.5, "unit": "AU"},
            "orbital_period": {"value": 552, "unit": "years"},
            "orbital_eccentricity": {"value": 0.505, "note": "Highly elliptical scattered disk orbit"},
            "galaxy_reference": "Solar System — Scattered Disk",
        },
        "physical": {
            "mass": {"value": 1.8e21, "unit": "kg", "note": "Estimated"},
            "radius": {"value": 618, "unit": "km", "note": "Approximately"},
            "density": {"value": 1900, "unit": "kg/m³", "note": "Estimated"},
            "surface_temperature": {"mean": -237, "unit": "K"},
            "moons": {"count": 1, "primary": "Xiangliu"},
        },
        "detailed_description": (
            "Gonggong is a scattered disk dwarf planet with an unusually high surface albedo (reflectivity) of ~0.43, "
            "indicating extensive water-ice coverage or coating. Originally designated 2007 OR10, Gonggong was formally "
            "named in 2019 after the Chinese flood-spirit deity. It orbits in the scattered disk at ~67.5 AU, following "
            "a highly eccentric, inclined orbit that takes 552 years to complete. Gonggong is believed to be slightly "
            "larger than Haumea in volume but less dense. Its moon, Xiangliu (formerly S/2012 (136472) 1), was discovered "
            "in 2015. The exceptionally high albedo of Gonggong compared to other scattered disk objects suggests either "
            "recent cryovolcanic resurfacing with fresh water ice or a thin atmosphere that causes frost deposition. "
            "Its composition likely includes water ice, methane, and possibly nitrogen ice. Gonggong follows an orbit "
            "similar to Eris but slightly less eccentric, placing it securely in the scattered disk population."
        ),
        "scientific_facts": [
            "Gonggong has an unusually high albedo (0.43) for a scattered disk object, suggesting fresh ice surfaces.",
            "Its diameter is estimated at ~1,250 kilometers, making it slightly larger than Haumea by volume.",
            "A moon (Xiangliu) was discovered orbiting it at a distance of ~4,500 km with an orbital period of ~17 days.",
            "Gonggong's orbital eccentricity (0.505) is extreme, meaning it can be far from the Sun for extended periods.",
            "The Chinese name reflects the first non-Roman mythological designation for a major dwarf planet.",
            "Spectroscopy suggests a water-ice-rich surface, possibly with methane and nitrogen ices.",
            "Its high albedo may indicate it has been subjected to recent impacts or cryovolcanism that refreshed its surface.",
            "Gonggong is part of the dynamically hot scattered disk population, unlike the cooler classical Kuiper Belt.",
            "Its 552-year orbit means observations of it will take centuries to establish key orbital parameters precisely.",
            "It was one of the faintest dwarf planet candidates initially discovered.",
        ],
        "did_you_know": [
            "Gonggong's name in Chinese mythology refers to a flood spirit — fitting for an ice world.",
            "Its high reflectivity makes it one of the brightest scattered disk objects despite being farther than most.",
            "From Gonggong's surface, the Sun would appear ~1,600 times dimmer than on Earth, little more than a bright star.",
        ],
        "formation_process": (
            "Gonggong likely formed in the primordial planetesimal disk beyond 50 AU and was scattered into its current "
            "high-inclination, high-eccentricity orbit during the late heavy bombardment via gravitational interactions "
            "with Neptune and/or other planetary embryos. Its moon Xiangliu may have been captured or formed via a past collision."
        ),
        "future_evolution": (
            "Gonggong will continue its 552-year orbit. At aphelion (~100 AU), its icy surface will become extremely cold, "
            "while at perihelion (~35 AU) it will warm slightly. Over billions of years, solar wind and cosmic ray "
            "bombardment will gradually darken its surface, eventually matching the darker scattered disk objects."
        ),
        "related_objects": ["Eris", "Pluto", "Xiangliu", "Scattered Disk Objects"],
        "parent_system": "Solar System — Scattered Disk",
        "child_objects": ["Xiangliu"],
        "nasa_reference": "https://solarsystem.nasa.gov/planets/dwarf-planets/",
    },

    # -------------------------------------------------------------------------
    # SECTION 10: DARK MATTER / COSMOLOGY ENTRY
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "dark-matter-halos")),
        "name": "Dark Matter Halos",
        "category": "Cosmological Structure",
        "subtype": "Dark Matter — Gravitational Scaffolding",
        "tags": ["dark-matter", "cosmology", "structure-formation", "galactic-halo", "WIMPs", "CDM"],
        "difficulty_level": "advanced",
        "spatial": {
            "distribution": "Ubiquitous — permeates all large-scale structure",
            "scale": "From dwarf galaxy halos (~10 kpc) to cluster halos (~10 Mpc)",
            "galaxy_reference": "Universal",
        },
        "physical": {
            "cosmic_fraction": {"value": 26.8, "unit": "%", "note": "Of total mass-energy content of universe"},
            "density_profile": "NFW (Navarro-Frenk-White) profile: ρ ∝ 1/(r/rs)(1+r/rs)²",
            "interaction": "Gravitational only (no known electromagnetic interaction)",
            "candidate_particles": ["WIMPs", "Axions", "Sterile Neutrinos", "Primordial Black Holes"],
            "detection_status": "No confirmed direct detection as of 2024",
        },
        "detailed_description": (
            "Dark matter is the dominant form of matter in the universe, comprising approximately "
            "26.8% of the total mass-energy content — roughly 5× more than ordinary baryonic matter. "
            "It does not emit, absorb, or reflect electromagnetic radiation in any known way, making "
            "it completely invisible to telescopes at every wavelength. Its existence is inferred "
            "exclusively through its gravitational effects: galaxy rotation curves that remain flat "
            "instead of declining at large radii (Zwicky 1933, Rubin 1970s), gravitational lensing "
            "that deflects light by far more mass than is visible, the large-scale structure of the "
            "cosmic web, and the temperature fluctuations of the cosmic microwave background. Dark "
            "matter forms extended halos around galaxies that are roughly spherical and extend far "
            "beyond the visible stellar disk — for the Milky Way, the dark matter halo extends up to "
            "~1 million light-years. The leading candidate particle is the WIMP (Weakly Interacting "
            "Massive Particle), predicted by supersymmetric extensions of the Standard Model, with "
            "masses in the GeV–TeV range. Despite decades of direct detection experiments (LUX, "
            "XENON1T, LZ) and collider searches (LHC), no dark matter particle has been confirmed. "
            "Alternative candidates include axions (extremely light particles originally proposed to "
            "solve the strong CP problem), sterile neutrinos, and primordial black holes formed in "
            "the early universe. The Bullet Cluster provides the most direct observational evidence: "
            "two galaxy clusters that recently collided show the hot gas (visible in X-rays) slowed "
            "by pressure, while the dark matter halos (traced by gravitational lensing) passed "
            "through unimpeded, proving dark matter is distinct from ordinary matter."
        ),
        "scientific_facts": [
            "The Bullet Cluster (1E 0657-558) provides the most direct empirical evidence for dark matter as a distinct component from baryonic matter.",
            "Galactic rotation curves — first studied systematically by Vera Rubin in the 1970s — show stars at large radii orbit faster than visible mass predicts.",
            "The LZ experiment (2022) is the most sensitive dark matter direct detection experiment, using 10 tonnes of liquid xenon — with null result to date.",
            "N-body simulations of dark matter-only universes produce a cosmic web structure that closely matches observed large-scale structure.",
            "NFW profile predicts a central 'cusp' of high dark matter density at galaxy centers — but observations often show a flat 'core', the 'cusp-core problem'.",
            "Dwarf spheroidal galaxies have the highest dark-matter-to-baryonic-matter ratios of any objects (~1000:1 in some cases).",
            "Gravitational lensing surveys (weak lensing) can map the 3D distribution of dark matter across the cosmos without seeing it directly.",
            "Axions, if they exist in the correct mass range (~10⁻⁵ eV), could be detected by experiments like ADMX (Axion Dark Matter eXperiment).",
            "Warm dark matter models predict fewer small-scale structures than CDM — a potential resolution of the 'missing satellites problem'.",
            "The Planck 2018 cosmological parameters give dark matter density: Ω_c h² = 0.120 ± 0.001.",
        ],
        "did_you_know": [
            "Every second, trillions of dark matter particles (if WIMPs) are passing through your body without interacting.",
            "Fritz Zwicky proposed 'dunkle Materie' (dark matter) in 1933 when he found galaxy clusters had insufficient visible mass to hold themselves together gravitationally.",
            "Modified Newtonian Dynamics (MOND) can reproduce some galactic rotation curves without dark matter, but fails for galaxy clusters and CMB predictions.",
        ],
        "formation_process": (
            "Dark matter decoupled from the thermal plasma in the early universe before baryonic matter "
            "did, beginning to clump under gravity while ordinary matter was still ionized and "
            "pressure-supported. This 'head start' allowed dark matter halos to form first, providing "
            "gravitational wells into which ordinary matter fell to form galaxies. The first dark matter "
            "halos formed at redshifts z~20–30 (less than 200 million years after the Big Bang), "
            "eventually merging hierarchically into the large halos we see today."
        ),
        "future_evolution": (
            "In the current cosmological epoch, dark matter continues to cluster hierarchically. "
            "As the universe expands under dark energy, large-scale structure growth will eventually "
            "cease. Individual galaxy halos will continue to merge and grow, but the largest structures "
            "will become isolated 'island universes' separated by ever-growing voids. In the very "
            "long term, if dark matter is a stable particle, halos will persist essentially forever, "
            "gradually depleted by WIMP annihilation (if WIMPs) or stripped by galaxy mergers."
        ),
        "related_objects": ["Milky Way Galaxy", "Bullet Cluster", "Cosmic Web", "Cosmic Microwave Background", "Dark Energy"],
        "parent_system": "Universe — Large Scale Structure",
        "child_objects": ["NFW Halo profiles", "Subhalos (dwarf galaxies)"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/what-is-dark-energy/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cosmic-microwave-background")),
        "name": "Cosmic Microwave Background (CMB)",
        "category": "Cosmological Structure",
        "subtype": "Radiation — Relic from Big Bang Thermalization",
        "tags": ["CMB", "cosmology", "recombination", "photon-decoupling", "temperature-fluctuations", "WMAP", "Planck"],
        "difficulty_level": "advanced",
        "spatial": {
            "scale": "Universe-spanning — at distance ~46.5 billion light-years (comoving)",
            "isotropy": "Homogeneous to ~1 part in 100,000; dipole, quadrupole, and higher multipoles detected",
            "galaxy_reference": "Observable Universe boundary (recombination surface, z~1100)",
        },
        "physical": {
            "temperature": {"value": 2.725, "unit": "K"},
            "temperature_variance": {"amplitude": 1e-5, "note": "Root-mean-square temperature fluctuations relative to mean"},
            "photon_density": {"value": 411, "unit": "per cm³"},
            "energy_density": {"value": 4.2e-14, "unit": "J/m³"},
        },
        "detailed_description": (
            "The Cosmic Microwave Background is relic radiation from the Big Bang, released when the "
            "universe cooled enough for electrons and protons to combine into neutral hydrogen ~380,000 "
            "years after the Big Bang (at recombination, z~1100). This 'photon decoupling' freed photons "
            "to travel freely through space. Today, this ancient light permeates the entire universe, "
            "redshifted into the microwave band (wavelengths ~1 mm) by cosmic expansion and cooled to "
            "~2.725 K. The CMB was accidentally discovered in 1964 by Penzias and Wilson using a radio antenna. "
            "The Cosmic Background Explorer (COBE) satellite in 1990 detected tiny temperature fluctuations "
            "(~10⁻⁵ K) that seed all cosmic structure — galaxies, stars, and life itself. The WMAP (2001–2010) "
            "and Planck (2009–2013) satellites mapped the CMB with unprecedented precision, revealing the universe "
            "is flat, composed of ~68% dark energy, ~27% dark matter, and ~5% baryonic matter. Temperature anisotropies "
            "encode a wealth of cosmological information: the Hubble constant, the age of the universe, the density "
            "of ordinary and dark matter, the ionization history of the universe, and constraints on inflation."
        ),
        "scientific_facts": [
            "The CMB temperature is 2.725 ± 0.001 K, measured to extraordinary precision.",
            "Planck's measurements of temperature anisotropies constrain the Hubble constant to H₀ = 67.3 ± 0.5 km/s/Mpc.",
            "The CMB dipole — a temperature difference between opposite sides of the sky — reveals the Solar System's motion at ~600 km/s relative to the CMB rest frame.",
            "Planck data indicate the universe is flat (Ω_total = 1.00 ± 0.02) to extraordinary precision.",
            "The CMB power spectrum (temperature fluctuations as a function of angular scale) contains peaks and troughs encoding cosmic parameters.",
            "Recombination occurred at z~1100, making the CMB our most direct probe of the early universe.",
            "Photons have been freely streaming since decoupling; they have never been in thermal contact with baryonic matter since.",
            "The CMB quadrupole moment is anomalously low relative to theoretical predictions — possibly a statistical fluke or hint of anomalous physics.",
            "Polarization of the CMB (detected by Planck and WMAP) encodes information about reionization and gravitational waves from inflation.",
            "Future experiments (CMB-S4, Simons Observatory) will measure CMB polarization to unprecedented sensitivity.",
        ],
        "did_you_know": [
            "Carl Penzias and Robert Wilson won the Nobel Prize in Physics in 1978 for the CMB's accidental discovery.",
            "The CMB is the oldest and most distant light we can see — we observe the universe at age ~380,000 years.",
            "If you could tune an old television to a static channel, ~1% of the noise you see is due to the CMB.",
        ],
        "formation_process": (
            "In the first ~380,000 years after the Big Bang, the universe was too hot for atoms to form — electrons, protons, "
            "and photons existed as a hot plasma. As the universe expanded, it cooled. At ~3,000 K (z~1100), electrons combined "
            "with protons to form neutral hydrogen, dramatically reducing the opacity to photons. This recombination allowed photons "
            "to decouple from matter and stream freely — the phenomenon observable today as the CMB."
        ),
        "future_evolution": (
            "The CMB will continue to cool due to cosmic expansion, asymptotically approaching 0 K over infinite time. Its frequency "
            "will continue to redshift, eventually becoming indistinguishable from the quantum vacuum. In the extremely distant future, "
            "the CMB will be a relic of the early universe, inaccessible to observation."
        ),
        "related_objects": ["Big Bang", "Inflation", "Recombination Epoch", "Large-Scale Structure", "Planck Satellite"],
        "parent_system": "Universe — Early Universe Physics",
        "child_objects": ["Temperature Anisotropies", "E-mode Polarization", "B-mode Polarization"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/what-is-the-cosmic-microwave-background/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cosmic-web-large-scale-structure")),
        "name": "Cosmic Web",
        "category": "Cosmological Structure",
        "subtype": "Large-Scale Structure — Galaxy Filaments, Clusters, Voids",
        "tags": ["cosmology", "large-scale-structure", "N-body-simulations", "web-structure", "distribution-of-matter", "redshift-surveys"],
        "difficulty_level": "advanced",
        "spatial": {
            "scale": "Billion light-years — spanning from ~10 Megaparsecs to >1 Gigaparsec",
            "structure_types": "Filaments, clusters, walls, nodes, voids",
            "voids_typical_size": {"value": 100, "unit": "Mpc", "note": "Typical void diameter"},
            "filament_thickness": {"value": 5, "unit": "Mpc", "note": "Typical filament width"},
        },
        "physical": {
            "average_galaxy_density": {"value": 0.1, "unit": "galaxies/Mpc³"},
            "matter_distribution": "~95% in low-density regions; ~5% in galaxy clusters and filaments",
            "topology": "Percolating network of filaments connecting galaxy clusters",
        },
        "detailed_description": (
            "The Cosmic Web is the large-scale structure of the universe — the billion-light-year architecture "
            "formed by the distribution of matter following the gravitational amplification of primordial density "
            "fluctuations. Rather than uniformly distributed, galaxies are arranged in a filamentary network: "
            "massive filaments of galaxies spanning hundreds of millions of light-years connect nodes (galaxy clusters), "
            "with enormous voids (~100–300 million light-years across) of near-empty space between them. This structure "
            "emerged naturally from the growth of tiny quantum fluctuations imprinted during cosmic inflation, amplified "
            "by non-linear gravitational collapse. Redshift surveys (such as the Sloan Digital Sky Survey, 2dF Galaxy "
            "Redshift Survey, and the Sloan Digital Sky Survey Mapping Nearby Galaxies at Apache Point Observatory) "
            "map the Cosmic Web by measuring the distances and velocities of millions of galaxies. N-body simulations "
            "of dark matter evolution reproduce the observed web structure with remarkable fidelity, confirming that "
            "cold dark matter is the primary architect of cosmic structure. The web is a living, evolving structure: "
            "filaments are continuously fed by inflows of matter from voids, while galaxy clusters at nodes undergo "
            "mergers and grow through accretion."
        ),
        "scientific_facts": [
            "The Great Wall (z~0.03) is a supergalactic structure stretching over 500 million light-years.",
            "Voids have nearly no galaxies, with densities ~0.1× the cosmic average.",
            "The Sloan Great Wall, discovered in 2020, is ~1.4 billion light-years long — one of the largest structures known.",
            "N-body simulations show the web structure is robust across cosmic time — filaments present at z~10 resemble the local web.",
            "Galaxy clusters are nodes of the cosmic web, with Coma, Virgo, and Fornax clusters being nearby prominent examples.",
            "Filaments are typically 5–10 Megaparsecs thick and extend for hundreds of Megaparsecs.",
            "The web's topology can be characterized by persistent homology — a topological data analysis technique.",
            "Intergalactic gas between filaments is very hot (~10⁷ K) — detected in X-ray emission.",
            "The web grows primarily through 'along-the-filament' accretion rather than random encounters.",
            "Future surveys (DESI, 4MOST) will map the web to unprecedented scales and redshifts.",
        ],
        "did_you_know": [
            "If galaxies were grains of sand, the Cosmic Web would span a distance equivalent to thousands of kilometers.",
            "The voids are not truly empty — they contain ~1 galaxy per million galaxy-volumes.",
            "The Multiversal structure of the Cosmic Web suggests we live in one bubble in an infinite cosmos.",
        ],
        "formation_process": (
            "The Cosmic Web grew from the gravitational collapse of density fluctuations seeded during cosmic inflation. "
            "Initially, the universe was nearly uniform, but quantum fluctuations imprinted ~10⁻⁵ relative density variations. "
            "After recombination, dark matter collected in potential wells, causing baryonic matter to flow into these regions, "
            "forming protogalaxies and their associated structures. Over billions of years, gravitational instability amplified "
            "these structures into the filamentary network we observe today."
        ),
        "future_evolution": (
            "The Cosmic Web will continue to grow as dark energy accelerates cosmic expansion. Voids will expand faster than filaments "
            "can grow, causing the web to become increasingly sparse. Eventually, distant galaxy clusters will become causally disconnected "
            "as they recede beyond the cosmic horizon. In the far future, the universe will appear increasingly empty from any vantage point."
        ),
        "related_objects": ["Galaxy Clusters", "Dark Matter Halos", "Sloan Digital Sky Survey", "Cosmic Microwave Background"],
        "parent_system": "Universe — Large Scale Structure",
        "child_objects": ["Filaments", "Nodes (clusters)", "Walls", "Voids"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/what-is-the-structure-of-the-universe/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "galaxy-clusters-aggregates")),
        "name": "Galaxy Clusters",
        "category": "Cosmological Structure",
        "subtype": "Gravitationally Bound Aggregates of Thousands of Galaxies",
        "tags": ["galaxy-cluster", "gravitational-binding", "hot-gas", "dark-matter-dominated", "X-ray-emission", "cosmology"],
        "difficulty_level": "intermediate",
        "spatial": {
            "scale": {"distance": "1–10 Megaparsecs", "unit": "Mpc"},
            "galaxy_count": {"low": 100, "high": 10000, "note": "Ranges from poor clusters to rich clusters"},
            "total_mass": {"typical": 1e15, "unit": "solar_masses"},
        },
        "physical": {
            "dark_matter_fraction": {"value": 85, "unit": "%"},
            "gas_fraction": {"value": 13, "unit": "%"},
            "stellar_fraction": {"value": 2, "unit": "%"},
            "hot_gas_temperature": {"value": 1e7, "unit": "K", "range": "10⁷–10⁸ K"},
            "x_ray_luminosity": {"value": 1e44, "unit": "erg/s", "note": "Typical for large clusters"},
        },
        "detailed_description": (
            "Galaxy clusters are the largest gravitationally bound structures in the universe, containing "
            "hundreds to ten thousand galaxies held together by their collective gravity. These cosmic "
            "aggregates are themselves nodes of the Cosmic Web, connected by filaments of lower-density matter. "
            "The Virgo Cluster (~65 million light-years away) is the nearest rich galaxy cluster; the Coma Cluster "
            "(~320 million light-years) is a prototypical example of a dynamically mature cluster. Galaxy clusters "
            "are dominated by dark matter (~85% by mass), with intergalactic gas (~13%) heated to tens of millions "
            "of degrees by gravitational compression and collision, emitting intense X-rays detectable by Chandra "
            "and XMM-Newton satellites. This hot intergalactic medium (IGM) is enriched with heavy elements forged "
            "in supernovae, tracing the chemical evolution of the universe. Galaxy clusters undergo continuous "
            "evolution: smaller groups merge, triggering violent shocks in the hot gas and spectacular X-ray emissions. "
            "Active galactic nuclei (AGN) in central cD (supergiant elliptical) galaxies inject energy, creating "
            "'bubbles' and cavities in the hot gas — a feedback mechanism that regulates star formation and gas cooling. "
            "Clusters are crucial for cosmology: their abundance and clustering properties constrain the dark energy "
            "equation of state and matter density through the Sunyaev-Zeldovich effect and weak gravitational lensing."
        ),
        "scientific_facts": [
            "The Virgo Cluster is the nearest galaxy cluster, at ~65 million light-years, containing ~2,000 galaxies.",
            "The Coma Cluster contains ~3,000–30,000 galaxies and is one of the densest known clusters.",
            "Bullet Cluster (1E 0657-56) provides direct evidence for dark matter by showing separated gas (visible in X-rays) and dark matter (via lensing).",
            "Galaxy cluster cores contain cD galaxies — supergiant ellipticals formed by galaxy mergers.",
            "The Sunyaev-Zeldovich effect — distortion of the CMB by hot cluster gas — allows precise cluster mass measurements.",
            "Weak gravitational lensing by cluster mass maps the 3D matter distribution, revealing dark matter architecture.",
            "Hydrostatic mass estimates require assuming dynamic equilibrium; simulations suggest ~10% systematic uncertainty.",
            "Cluster mergers produce some of the most energetic events in the universe, releasing as much energy as supernovae.",
            "Metallicity measurements show metal enrichment to ~0.5 solar metallicity in cluster cores.",
            "Future cluster surveys (eROSITA, CMB-S4, Rubin Observatory) will discover thousands of new clusters.",
        ],
        "did_you_know": [
            "The Perseus Cluster radiates as much X-ray energy as would light 10 million billion Suns.",
            "Galaxy clusters are the largest 'islands' in the cosmos — beyond them lie voids, then more distant islands.",
            "The intergalactic gas in clusters contains more atoms than all the stars in all the galaxies combined.",
        ],
        "formation_process": (
            "Galaxy clusters assembled hierarchically, beginning as small groups that merged over billions of years "
            "through gravitational interactions. Early cluster formation was dramatic — frequent mergers and high kinetic "
            "energies heated infalling gas. As the universe aged, cluster formation slowed. Today, clusters continue to "
            "grow primarily through the infall of groups and individual galaxies along filaments."
        ),
        "future_evolution": (
            "Galaxy clusters have reached approximate dynamical equilibrium in the current era. As the universe expands "
            "under dark energy, infall rates will decline. Clusters will become more isolated 'islands.' Over cosmic "
            "timescales, galactic mergers within clusters will continue, producing ever-larger central cD galaxies."
        ),
        "related_objects": ["Galaxies", "Dark Matter Halos", "Intergalactic Medium", "Virgo Cluster", "Cosmic Web"],
        "parent_system": "Universe — Large Scale Structure",
        "child_objects": ["Member Galaxies", "Intergalactic Gas", "Globular Clusters"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/what-are-galaxy-clusters/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "superclusters-associations")),
        "name": "Superclusters",
        "category": "Cosmological Structure",
        "subtype": "Associations of Galaxy Clusters — Filament Architecture",
        "tags": ["supercluster", "cosmology", "large-scale-structure", "Virgo-supercluster", "filament-nodes", "gravitational-binding"],
        "difficulty_level": "advanced",
        "spatial": {
            "scale": {"value": 100, "unit": "Mpc", "to": 200, "unit": "Mpc"},
            "example": "Virgo Supercluster spans ~150 million light-years",
            "galaxy_reference": "Local Universe",
        },
        "physical": {
            "structure": "Not gravitationally bound — more like loosely associated filaments",
            "member_clusters": {"value": 10, "to": 100, "note": "Typical range"},
            "total_mass": {"value": 1e17, "unit": "solar_masses", "note": "Estimated"},
        },
        "detailed_description": (
            "Superclusters are the largest structures whose components are weakly gravitationally associated — associations "
            "of galaxy clusters strung together along cosmic filaments. Unlike galaxy clusters (which are virialized), "
            "superclusters are not bound systems; they are matter density enhancements within the Cosmic Web. The Virgo "
            "Supercluster, containing the Virgo Cluster and our Local Group, spans ~150 million light-years. The Shapley "
            "Supercluster, a particularly rich association containing ~25 galaxy clusters, is one of the most massive "
            "structures known. These megastructures are gradually being revealed by deep redshift surveys. The existence "
            "of superclusters challenges our understanding of large-scale isotropy: the distribution of matter on these "
            "scales is highly non-uniform, with superclusters and supervoids (regions with dramatically reduced cluster "
            "density spanning >300 million light-years) indicating significant structure beyond the homogeneous background. "
            "Superclusters are not primordial — they grew hierarchically as filaments assembled under gravity."
        ),
        "scientific_facts": [
            "The Local Group is embedded in the Virgo Supercluster.",
            "The Shapley Supercluster (~200 million light-years away) exerts a noticeable gravitational influence on local cosmic flow.",
            "Superclusters are not virialized; they continue to evolve dynamically.",
            "Supervoids (low-density regions separating superclusters) are ~3× underdense relative to the cosmic average.",
            "The Sloan Great Wall, a supergalactic filament discovered in 2020, is ~1.4 billion light-years long.",
            "Simulations predict a cosmic 'web' hierarchy: superclusters → filaments → walls → clusters → groups → galaxies.",
            "The Hercules Supercluster is another well-studied massive nearby supercluster.",
            "Supercluster boundaries are poorly defined — they blend gradually into the background.",
            "Future surveys will map hundreds of superclusters, revealing the architecture of billion-light-year scales.",
            "The existence of superclusters suggests possible violations of the cosmological principle on largest scales.",
        ],
        "did_you_know": [
            "The Virgo Supercluster contains ~100 million galaxies — but it is still denser than the cosmic mean.",
            "Superclusters are so large that light from one end takes ~500 million years to reach the other.",
            "We are gradually being pulled toward the Shapley Supercluster by its gravitational attraction.",
        ],
        "formation_process": (
            "Superclusters grew hierarchically, beginning as slight overdensities in the early universe amplified by gravity. "
            "Galaxy clusters assembled first, then merged and aligned along filaments to form superclusters. This ongoing "
            "process continues today as the universe expands."
        ),
        "future_evolution": (
            "As dark energy accelerates cosmic expansion, the gravitational influence of superclusters will weaken. Individual "
            "clusters will eventually recede beyond each other's horizons. The supercluster structure will gradually dissolve "
            "into isolated island universes."
        ),
        "related_objects": ["Galaxy Clusters", "Cosmic Web", "Virgo Supercluster", "Shapley Supercluster", "Filaments"],
        "parent_system": "Universe — Large Scale Structure",
        "child_objects": ["Member Galaxy Clusters", "Filaments"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/what-is-the-structure-of-the-universe/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "gravitational-waves-spacetime-ripples")),
        "name": "Gravitational Waves",
        "category": "Cosmological Structure",
        "subtype": "Spacetime Ripples — Propagating Distortions of Spacetime Geometry",
        "tags": ["gravitational-waves", "LIGO", "Virgo", "spacetime", "Einstein", "binary-mergers", "GW190814"],
        "difficulty_level": "advanced",
        "spatial": {
            "propagation_speed": {"value": 299792458, "unit": "m/s", "note": "Speed of light (c)"},
            "strain_amplitude": {"typical": 1e-21, "note": "Relative spacetime distortion"},
            "wavelength_range": {"low": 1000, "high": 1e10, "unit": "km", "note": "LIGO sensitive range"},
        },
        "physical": {
            "speed_of_gravity": "Equal to speed of light (c), confirmed by GW170817",
            "polarization": "Transverse — two independent polarization states (+ and ×)",
            "energy_radiated": {"example": "GW150914 radiated ~3 solar masses as gravitational waves"},
        },
        "detailed_description": (
            "Gravitational waves are ripples in spacetime itself — propagating distortions of the metric geometry described "
            "by Einstein's general theory of relativity. They are generated by the acceleration of massive objects, particularly "
            "compact binary mergers (black holes and neutron stars). The first direct detection occurred on September 14, 2015, "
            "when the Laser Interferometer Gravitational-Wave Observatory (LIGO) detected GW150914 — the merger of two stellar-mass "
            "black holes (36 and 29 solar masses) producing a 62 solar mass remnant, with the missing 3 solar masses converted to "
            "gravitational wave energy. This epochal discovery confirmed Einstein's theory, proved binary black holes exist, and "
            "opened a new observational window to the universe. Over 90 gravitational wave events have now been detected by LIGO "
            "and Virgo. GW170817 was the first neutron star merger observed (in gravitational waves AND across the electromagnetic "
            "spectrum), confirming gravitational wave speed equals light speed. Pulsar timing arrays (PTAs) have hinted at "
            "supermassive black hole merger signals in the nanohertz band. Space-based detectors (LISA, Taiji) will eventually "
            "detect supermassive black hole mergers and primordial gravitational waves from the Big Bang."
        ),
        "scientific_facts": [
            "Over 90 gravitational wave events have been detected by LIGO-Virgo-KAGRA as of April 2024.",
            "The speed of gravity was confirmed to equal the speed of light to within 1 part in 10¹⁵ by GW170817.",
            "GW190814 detected the merger of a 2.6 solar mass black hole with a 23 solar mass object of ambiguous nature (possibly an unusual neutron star or light black hole).",
            "Binary neutron star mergers produce gravitational waves and kilonova electromagnetic counterparts rich in heavy elements (gold, platinum, uranium).",
            "Pulsar timing arrays detect nanohertz gravitational waves from supermassive black hole binaries at galactic centers.",
            "The LISA space mission (launch ~2034) will detect gravitational waves from supermassive black hole mergers.",
            "Primordial gravitational waves from cosmic inflation remain undetected but are a key target for future experiments.",
            "Gravitational waves carry unique information complementary to electromagnetic observations.",
            "The chirp frequency of merging compact objects sweeps upward as they spiral inward, converting gravitational potential energy to gravitational radiation.",
            "Multi-messenger astronomy combines gravitational wave, electromagnetic, and particle observations for rich astrophysical insight.",
        ],
        "did_you_know": [
            "A gravitational wave detector must measure spacetime distortions trillions of times smaller than a proton diameter.",
            "The LIGO arms are 4 km long and must detect relative motion changes of ~10⁻¹⁸ meters — about 1/10,000th the size of a proton nucleus.",
            "Some gravitational waves took over a billion years to reach Earth after their creation in distant mergers.",
        ],
        "formation_process": (
            "Gravitational waves are produced whenever massive objects accelerate, particularly during binary mergers. As two "
            "compact objects spiral inward, the strong spacetime curvature near them radiates gravitational waves, efficiently "
            "removing orbital energy and driving the merger. The merger itself is a violent release of remaining orbital energy "
            "as a characteristic 'chirp' — a rising-frequency waveform lasting typically 1 second in the LIGO band."
        ),
        "future_evolution": (
            "Gravitational wave astronomy will continue to mature. LIGO-Virgo-KAGRA will detect thousands of mergers per year after "
            "next-generation upgrades (Einstein Telescope, Cosmic Explorer). Space-based detectors (LISA) will open entirely new "
            "frequency windows, revealing supermassive black hole binaries and primordial gravitational waves."
        ),
        "related_objects": ["LIGO", "Virgo", "Black Holes", "Neutron Stars", "Multi-Messenger Astronomy", "GW170817"],
        "parent_system": "Universe — High-Energy Astrophysics",
        "child_objects": ["Gravitational Wave Events", "Electromagnetic Counterparts"],
        "nasa_reference": "https://www.ligo.caltech.edu/page/what-are-gravitational-waves",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cosmic-inflation-exponential-expansion")),
        "name": "Cosmic Inflation",
        "category": "Cosmological Structure",
        "subtype": "Primordial Exponential Expansion Phase of Early Universe",
        "tags": ["inflation", "early-universe", "quantum-fluctuations", "primordial-gravitational-waves", "cosmic-microwave-background", "scalar-field"],
        "difficulty_level": "advanced",
        "spatial": {
            "scale": "Universe expanded by factor of ~10²⁶ or more",
            "duration": {"value": 1e-36, "unit": "seconds (start)", "to": 1e-32, "unit": "seconds (end)", "note": "Duration ~10⁻³⁴ seconds"},
            "timeline": "Occurred 10⁻³⁶ to 10⁻³² seconds after Big Bang",
        },
        "physical": {
            "expansion_rate": {"typical": 1e50, "unit": "Hubble/s"},
            "energy_scale": {"gev": 1e16, "note": "Plank scale (10^16 GeV)"},
            "flatness_precision": "Universe flatness tuned to ~1 part in 10⁶⁰",
        },
        "detailed_description": (
            "Cosmic inflation is a hypothetical period of exponential expansion in the extremely early universe, "
            "proposed in 1980 by Alan Guth and refined by Andrei Linde and others. During inflation, space expanded "
            "by a factor of ~10²⁶ or more in a fraction of a second, exponentially diluting the density of any primordial "
            "imperfections. This solves several 'cosmic mysteries': the flatness problem (why is the universe so precisely "
            "flat?), the horizon problem (why does the universe look the same in all directions despite causally disconnected "
            "regions?), and the magnetic monopole problem. Inflation also provides a compelling mechanism for generating "
            "primordial density fluctuations: quantum vacuum fluctuations in the inflaton field (a hypothetical scalar field "
            "driving inflation) were stretched to classical scales, seeding all galaxies, stars, and structure in the universe. "
            "Remarkably, inflation also predicts a background of primordial gravitational waves — tensor perturbations of spacetime "
            "geometry. Evidence for inflation comes from the remarkable agreement between inflation predictions and observed "
            "properties of the CMB: near-perfect spatially flatness, scale-invariant primordial density fluctuations, a tiny "
            "spectrum of primordial gravitational waves (with amplitude set by the energy scale of inflation). The Planck satellite "
            "measured the tensor-to-scalar ratio r < 0.064, constraining the energy scale to <10¹⁶ GeV. Multiple inflationary "
            "models exist, differing in the form of the inflaton potential; observations continue to winnow possibilities."
        ),
        "scientific_facts": [
            "Inflation was proposed to solve three major cosmological problems: flatness, horizon, and monopole problems.",
            "The scale-invariance of density fluctuations (n_s ~ 1) predicted by inflation is remarkably consistent with observations.",
            "Planck measurements constrain the tensor-to-scalar ratio r < 0.064, limiting the inflation energy scale to <10¹⁶ GeV.",
            "If detected, primordial gravitational waves would be the smoking gun for inflation, directly observable through CMB B-mode polarization.",
            "Eternal inflation suggests our Big Bang may be one bubble in a eternally inflating multiverse.",
            "Slow-roll inflation provides analytic solutions; other models include chaotic, hybrid, and starobinsky inflation.",
            "The inflaton field's properties remain unknown — it is not directly identified with any Standard Model particle.",
            "Quantum entanglement of primordial fluctuations may be detectable in the three-point function of density fluctuations (bispectrum).",
            "Future CMB measurements (CMB-S4) will probe inflation predictions to unprecedented precision.",
            "Some alternatives to inflation (bouncing cosmologies, Ekpyrotic models) have been proposed but generally fit observations less well.",
        ],
        "did_you_know": [
            "During inflation, the universe expanded faster than light — but this doesn't violate relativity because spacetime itself was expanding.",
            "Inflation predicts there should be primordial gravitational waves with wavelengths spanning from subatomic to supergalactic scales.",
            "If proven, inflation would rank among the most profound discoveries in physics, revealing physics at energy scales unreachable by accelerators.",
        ],
        "formation_process": (
            "Cosmic inflation is hypothesized to have begun when the universe cooled below the energy scale of the inflaton potential's "
            "transition, causing the inflaton field to roll slowly down its potential. The energy density during this rolling drove exponential "
            "expansion. Inflation ended when the inflaton field's potential energy was converted to radiation and particles via reheating, "
            "initiating the radiation-dominated era."
        ),
        "future_evolution": (
            "Inflation ended ~10⁻³² seconds after the Big Bang, transitioning to the radiation-dominated era. Evidence from inflation "
            "persists today as the flatness of the universe, the scale-invariance of structure, and potentially detectable primordial "
            "gravitational waves imprinted in the CMB polarization."
        ),
        "related_objects": ["Big Bang", "Cosmic Microwave Background", "Primordial Gravitational Waves", "Planck Satellite"],
        "parent_system": "Universe — Early Universe Physics",
        "child_objects": ["Inflaton Field", "Density Fluctuations", "Primordial Gravitational Waves"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/what-does-inflation-tell-us-about-the-universe/",
    },
]

    # =========================================================================
    # PHASE 2: LESS COMMON BUT IMPORTANT OBJECTS
    # =========================================================================
    # Magnetars, rare nebulae, exoplanets, brown dwarfs, variable stars,
    # binary systems, globular clusters, and advanced stellar phenomena
    # =========================================================================

    
import uuid

COSMIC_OBJECTS_PHASE2 = [

    # -------------------------------------------------------------------------
    # MAGNETARS - EXTREME NEUTRON STARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sgr-0418-5729")),
        "name": "SGR 0418+5729",
        "category": "Neutron Star",
        "subtype": "Magnetar — Ultra-Weak Magnetic Field",
        "tags": ["magnetar", "neutron-star", "soft-gamma-repeater", "low-field", "x-ray-source"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 2000, "unit": "pc"},
            "coordinates": {"ra": "04h 18m 33.8s", "dec": "+57° 29' 21\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "magnetic_field": {"value": "6e12", "unit": "Gauss", "note": "Weakest known magnetar field"},
            "spin_period": {"value": 9.08, "unit": "seconds"},
            "surface_temperature": {"estimated": 10000, "unit": "K"},
        },
        "detailed_description": (
            "SGR 0418+5729 is the most enigmatic magnetar known — it possesses the weakest magnetic field "
            "ever measured in a magnetar (6×10¹² Gauss), yet it still produces characteristic soft gamma-ray "
            "bursts and exhibits magnetar-like activity. Discovered by X-ray monitoring in 2009, it challenges "
            "the classical definition of magnetars: traditionally, magnetars required fields exceeding 10¹⁵ Gauss, "
            "yet SGR 0418+5729 produces outbursts with a field only ~100 times stronger than Earth's. The source "
            "has undergone multiple outburst episodes, emitting bursts of X-rays and gamma-rays lasting milliseconds "
            "to seconds. Its weak field yet persistent activity suggests either: (1) an even more exotic magnetic "
            "topology or field geometry, (2) a different internal structure than classical neutron stars, or (3) a "
            "recently-formed crust with delayed stress relaxation. The neutron star's spin period of 9.08 seconds "
            "is relatively slow compared to millisecond pulsars, consistent with a young age or recent outburst."
        ),
        "scientific_facts": [
            "SGR 0418+5729 has the lowest surface magnetic field (~6×10¹² Gauss) of any known magnetar.",
            "Despite its weak field, it produces soft gamma-ray bursts similar to magnetars with 100x stronger fields.",
            "Bursts from SGR 0418+5729 can exceed 10⁴⁴ erg/s in X-ray luminosity during outbursts.",
            "The magnetar's spin period is 9.08 seconds — relatively slow, suggesting recent spin-down.",
            "Its location in the Galactic plane implies it may be younger than 1 million years old.",
            "The weakness of its dipole field but strength of its activity suggests a non-dipolar or buried magnetic configuration.",
            "X-ray observations reveal spectral hardening during bursts, indicating complex emission mechanisms.",
            "Multiple outburst episodes (2009, 2010, 2014) suggest a thermally unstable crust or complex magnetic dynamics.",
            "SGR 0418+5729 challenges the magnetar paradigm and may represent a new class of high-energy transient.",
            "Magnetized crust models involving Hall instabilities can potentially explain its low-field yet active behavior.",
        ],
        "did_you_know": [
            "SGR 0418+5729 may represent a 'magnetar in the making' — a young neutron star where core magnetic field is still being established.",
            "Its outbursts release energy equivalent to a billion megatons of TNT in a single burst lasting less than a second.",
            "The weak dipole field may mask a much stronger internal toroidal magnetic field — only the exterior field is directly accessible.",
        ],
        "formation_process": (
            "SGR 0418+5729 formed from the core collapse of a massive star (~20–25 solar masses). Its unusually weak surface "
            "magnetic field may result from recent field decay, crustal distortions, or an atypical initial magnetic configuration "
            "imprinted during core collapse. Its youth suggests a relatively recent formation (< few million years)."
        ),
        "future_evolution": (
            "SGR 0418+5729 will undergo continued outburst cycles with timescales of years to decades, gradually spinning down via "
            "magnetic braking. Its magnetic field may dissipate or strengthen depending on crust cooling and internal dynamics. "
            "Eventually it will spin down to millisecond periods over ~1 million years."
        ),
        "related_objects": ["SGR 1806-20", "Black Widow Pulsar", "Magnetars"],
        "parent_system": "Milky Way — Sagittarius Arm",
        "nasa_reference": "https://en.wikipedia.org/wiki/SGR_0418%2B5729",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sgr-j1745-2900")),
        "name": "SGR J1745-2900",
        "category": "Neutron Star",
        "subtype": "Magnetar — Galactic Center Magnetar",
        "tags": ["magnetar", "neutron-star", "galactic-center", "x-ray-transient", "soft-gamma-repeater"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 26000, "unit": "ly"},
            "coordinates": {"ra": "17h 45m 40.0s", "dec": "-29° 00' 28\""},
            "galaxy_reference": "Milky Way — Galactic Center",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "magnetic_field": {"value": "2e15", "unit": "Gauss"},
            "spin_period": {"value": 3.764, "unit": "seconds"},
            "surface_temperature": {"estimated": 10000, "unit": "K"},
        },
        "detailed_description": (
            "SGR J1745-2900 is a magnetar located within a few light-years of Sagittarius A*, the supermassive black hole "
            "at the Galactic Center. Discovered in 2013 via its X-ray and gamma-ray outburst, this magnetar is the first detected "
            "so close to our Galaxy's central black hole. Its proximity to Sgr A* creates a unique astrophysical laboratory: "
            "magnetars near black holes experience powerful tidal forces and may serve as probes of spacetime distortion near "
            "an event horizon. The magnetar exhibits typical soft gamma-ray repeater behavior, producing recurrent bursts of "
            "X-rays and low-energy gamma-rays. Its 3.76-second spin period and inferred age (< 1,600 years) suggest relatively "
            "recent formation. The presence of a magnetar near Sgr A* raises fascinating questions about massive star formation "
            "in the extreme environment near the Galactic Center, where tidal forces from Sgr A* stretch molecular clouds and "
            "accelerate star formation. The system also provides a natural laboratory for studying neutron star behavior in "
            "strong gravitational fields."
        ),
        "scientific_facts": [
            "SGR J1745-2900 is located within ~0.1 parsecs of Sagittarius A* — closer than any other magnetar to a SMBH.",
            "Its discovery distance-corrected X-ray luminosity exceeds 10³⁷ erg/s during outbursts.",
            "Spin-down measurements imply a characteristic age < 1,600 years, making it one of the youngest known magnetars.",
            "The magnetar's proximity to Sgr A* allows tests of strong-field gravity in ways impossible with isolated neutron stars.",
            "Radio observations revealed a magnetized wind interacting with the Galactic Center's diffuse plasma.",
            "Tidal forces from Sgr A* elongate the magnetar, potentially enhancing magnetic stress and outburst activity.",
            "The magnetar's spin period of 3.764 s is intermediate between standard pulsars and faster millisecond pulsars.",
            "Gamma-ray bursts from SGR J1745-2900 provided the first simultaneous MeV/GeV detection from the Galactic Center.",
            "Its magnetic field (2×10¹⁵ Gauss) is typical of magnetars but enhanced by tidal compression.",
            "The system's extreme gravity environment allows precision tests of neutron star models.",
        ],
        "did_you_know": [
            "If the magnetar moves too close to Sgr A*, tidal forces would eventually disrupt it — setting a limit to how the close it can stably orbit.",
            "The massive outburst in 2013 temporarily made SGR J1745-2900 the brightest object in the Galactic Center at X-ray wavelengths.",
            "Future gravitational wave detectors might detect signals from magnetar mergers near the Galactic Center.",
        ],
        "formation_process": (
            "SGR J1745-2900 likely formed from core collapse of a massive star in the Galactic Center region. Its short age "
            "and proximity to Sgr A* suggest it formed from a recently collapsed progenitor, possibly accelerated inward by "
            "dynamical interactions among the dense stellar populations near the SMBH."
        ),
        "future_evolution": (
            "SGR J1745-2900 will undergo gradual spin-down via magnetic braking. Its proximity to Sgr A* means it may eventually "
            "be captured, leading to tidal disruption or merger with the SMBH within billions of years. Intermediate fate: "
            "potential capture into a tight orbit around Sgr A*, making it an exotic X-ray binary."
        ),
        "related_objects": ["Sagittarius A*", "SGR 0418+5729", "Black Widow Pulsar"],
        "parent_system": "Milky Way — Galactic Center",
        "nasa_reference": "https://science.nasa.gov/mission/chandra/observations/sgr-j1745-2900/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "4u-0142-61")),
        "name": "4U 0142+61",
        "category": "Neutron Star",
        "subtype": "Magnetar — Anomalous X-ray Pulsar (AXP)",
        "tags": ["magnetar", "axp", "neutron-star", "x-ray-pulsar", "low-magnetic-field"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 3700, "unit": "pc"},
            "coordinates": {"ra": "01h 46m 00.7s", "dec": "+61° 33' 40\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "magnetic_field": {"value": "5e13", "unit": "Gauss"},
            "spin_period": {"value": 8.689, "unit": "seconds"},
            "surface_temperature": {"estimated": 10000, "unit": "K"},
        },
        "detailed_description": (
            "4U 0142+61 is one of the prototypical Anomalous X-ray Pulsars (AXPs) — a subclass of magnetar-like neutron stars "
            "that emit unexpectedly persistent X-rays without an apparent energetic outburst mechanism. Unlike classical accreting "
            "X-ray binaries powered by mass transfer from a companion star, 4U 0142+61 appears isolated, yet radiates X-rays with "
            "luminosity (L_x ~ 10³⁴ erg/s) powered by internal heat sources rather than accretion. The source displays a spin period "
            "of 8.689 seconds with timing glitches (sudden spin-up episodes) that suggest sudden crust-breaking events combined with "
            "magnetic reconnection. The magnetar's magnetic field of ~5×10¹³ Gauss is lower than soft gamma-ray repeaters (SGRs) but "
            "sufficient to power its anomalous X-ray emission via magnetic dissipation in the neutron star crust. AXPs like 4U 0142+61 "
            "may represent a missing evolutionary link between young spinning-down pulsars and old recycled millisecond pulsars, or "
            "perhaps represent a distinct population of magnetars with different magnetic geometries. Recent infrared and radio detections "
            "suggest a surrounding nebula or wind, hinting at ongoing particle acceleration."
        ),
        "scientific_facts": [
            "4U 0142+61 exhibits persistent X-ray emission (L_x ~ 10³⁴ erg/s) with no known accretion source — powered by internal magnetar activity.",
            "Timing glitches (sudden spin-up episodes) occur at intervals of several years, similar to pulsars and SGRs.",
            "Its magnetic field (~5×10¹³ Gauss) lies between classical pulsars and SGRs, making it a transitional magnetar.",
            "Spectral analysis reveals complex X-ray emission including narrow absorption features suggesting a magnetized atmosphere.",
            "Infrared observations detected faint emission, possibly from a low-mass companion or magnetosphere.",
            "Radio upper limits constrain radio emission, distinguishing it from classical radio pulsars.",
            "The spin period of 8.689 seconds suggests a young age but anomalously high rotational energy — an apparent 'age-energy paradox.'",
            "Magnetohydrodynamic models suggest crustal shear stresses drive recurrent magnetic reconnection and sustained heating.",
            "4U 0142+61 may host an accretion disk in a very low-state — explaining its persistent low-level X-ray output.",
            "Its properties bridge classical low-field radio pulsars and high-field magnetars, suggesting a continuous evolutionary pathway.",
        ],
        "did_you_know": [
            "The 'U' in the name stands for 'Uhuru' — the first orbiting X-ray observatory that discovered this source in the 1960s.",
            "4U 0142+61 was one of the first sources to challenge the distinction between accreting X-ray binaries and isolated neutron stars.",
            "If 4U 0142+61 harbors a low-mass companion, it would be one of the few magnetars with a known stellar neighbor.",
        ],
        "formation_process": (
            "4U 0142+61 formed from core collapse of a massive star (~25–30 solar masses). Its relatively low magnetic field "
            "suggests either a field in early development or one that has partially decayed. The presence of possible outflows "
            "or a low-mass companion suggests a binary formation channel or recent magnetic field restructuring."
        ),
        "future_evolution": (
            "4U 0142+61 will continue its spin-down via magnetic braking at a rate consistent with its current magnetic field. "
            "Its X-ray luminosity may gradually decrease as internal heat dissipates. Over ~1 million years, it will evolve into "
            "a quiescent, magnetically-dominated neutron star."
        ),
        "related_objects": ["SGR 0418+5729", "SGR 1806-20", "Black Widow Pulsar"],
        "parent_system": "Milky Way — Perseus Arm",
        "nasa_reference": "https://en.wikipedia.org/wiki/4U_0142%2B61",
    },

    # -------------------------------------------------------------------------
    # EXOPLANETS - TRAPPIST-1 SYSTEM PLANETS (INDIVIDUAL ENTRIES)
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "trappist-1b")),
        "name": "TRAPPIST-1b",
        "category": "Exoplanet",
        "subtype": "Rocky Planet — Ultraclose Orbiter",
        "tags": ["exoplanet", "terrestrial", "TRAPPIST-1", "tidal-locking", "red-dwarf", "transit-method"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 12.1, "unit": "pc"},
            "orbital_period": {"value": 1.51, "unit": "days"},
            "orbital_distance": {"value": 0.01154, "unit": "AU"},
            "equilibrium_temperature": {"value": 2566, "unit": "K"},
        },
        "physical": {
            "mass": {"min": 1.017, "max": 1.154, "unit": "earth_masses"},
            "radius": {"value": 1.086, "unit": "earth_radii"},
            "density": {"value": 5.3, "unit": "g/cm³"},
            "surface_gravity": {"value": 0.85, "unit": "g"},
            "atmosphere": {"note": "No confirmed atmospheric detection; strong XUV radiation suggests any atmosphere rapidly photoevaporates"},
        },
        "detailed_description": (
            "TRAPPIST-1b is the innermost and hottest planet of the seven-planet TRAPPIST-1 system, orbiting its ultracool dwarf "
            "host star every 1.51 days at a distance of only 0.01154 AU (~1.73 million km). With surface temperatures exceeding 2,500 K, "
            "TRAPPIST-1b is far too hot to harbor liquid water on its surface, yet it remains scientifically interesting as a testbed "
            "for atmospheric physics on tidally-locked rocky planets. The planet is likely tidally locked, with one hemisphere perpetually "
            "facing its star. Extreme EUV (extreme ultraviolet) radiation from TRAPPIST-1 (a T5 dwarf with strong stellar flares) likely "
            "drives significant atmospheric photoevaporation. If TRAPPIST-1b retains any atmosphere today, it would be a thin residual envelope "
            "of heavier elements (CO₂, nitrogen) left behind after hydrogen/helium escape. The planet's small size and proximity to its star "
            "make it an ideal target for transmission spectroscopy studies: as TRAPPIST-1b transits its star, starlight passes through any "
            "atmosphere and imprints spectral signatures detectable by JWST and future observatories. Such observations would reveal atmospheric "
            "composition, escape rates, and chemistries shaped by extreme radiation and tidal heating."
        ),
        "scientific_facts": [
            "TRAPPIST-1b has an orbital period of just 1.51 days — faster than Mercury's 88-day orbit around our Sun.",
            "Its equilibrium temperature (~2,566 K) makes it hotter than any planet in our Solar System except Venus and Mercury.",
            "TRAPPIST-1b is tidally locked: one hemisphere faces TRAPPIST-1 permanently; the other faces eternal darkness.",
            "Strong stellar flares from TRAPPIST-1 trigger atmospheric photoevaporation, destroying hydrogen/helium atmospheres within ~1 Gyr.",
            "Transmission spectroscopy observations (JWST, etc.) probe atmospheric composition; current limits suggest no H₂/He atmosphere remains.",
            "Tidal heating from orbital eccentricity interactions with outer planets may contribute significant internal heat.",
            "The planet's small orbital distance subjects it to ~100x more stellar radiation flux than Earth receives from the Sun.",
            "TRAPPIST-1b may have lost an initial water/volatile inventory to photoevaporation.",
            "Its interior is likely rocky with possible iron-enriched composition, hinting at differentiation despite extreme surface conditions.",
            "TRAPPIST-1b serves as a prototype for studying atmospheres on hot, tidally-locked rocky exoplanets.",
        ],
        "did_you_know": [
            "A person standing on TRAPPIST-1b would see the host star 100× brighter and larger in the sky than our Sun appears from Earth.",
            "One day on TRAPPIST-1b equals one year (1.51-day orbit = 1.51-day spin period due to tidal locking).",
            "TRAPPIST-1b may have once harbored liquid water oceans before photoevaporation stripped its early atmosphere.",
        ],
        "formation_process": (
            "TRAPPIST-1b likely formed from disk accretion of rocky material within the protoplanetary disk's inner regions. Its ultraclosed "
            "orbit may result from inward migration via planet-disk interactions or gravitational scattering among the seven-planet system, "
            "eventually settling into a dynamic equilibrium with resonances of outer planets."
        ),
        "future_evolution": (
            "TRAPPIST-1b will continue losing any remaining atmosphere to photoevaporation over billions of years. Its orbit may gradually "
            "shift due to chaotic gravitational interactions within the seven-planet system. In the far future (~10¹¹ years), TRAPPIST-1's "
            "cooling may enlarge the habitable zone, but TRAPPIST-1b will remain too hot for habitability."
        ),
        "related_objects": ["TRAPPIST-1 System", "TRAPPIST-1c", "TRAPPIST-1e", "TRAPPIST-1 Star"],
        "parent_system": "TRAPPIST-1 Planetary System",
        "nasa_reference": "https://exoplanetarchive.ipac.caltech.edu/overview/TRAPPIST-1%20b",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "trappist-1e")),
        "name": "TRAPPIST-1e",
        "category": "Exoplanet",
        "subtype": "Rocky Planet — Potentially Habitable",
        "tags": ["exoplanet", "terrestrial", "habitable", "TRAPPIST-1", "tidal-locking", "red-dwarf"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 12.1, "unit": "pc"},
            "orbital_period": {"value": 6.099, "unit": "days"},
            "orbital_distance": {"value": 0.02925, "unit": "AU"},
            "equilibrium_temperature": {"value": 246, "unit": "K"},
        },
        "physical": {
            "mass": {"min": 0.620, "max": 0.777, "unit": "earth_masses"},
            "radius": {"value": 0.910, "unit": "earth_radii"},
            "density": {"value": 6.8, "unit": "g/cm³"},
            "surface_gravity": {"value": 0.69, "unit": "g"},
            "atmosphere": {"note": "Unknown; potentially capable of retaining thin atmosphere due to lower stellar flux than inner planets"},
        },
        "detailed_description": (
            "TRAPPIST-1e is arguably the most intriguing world in the TRAPPIST-1 system and a prime target in humanity's search for "
            "potentially habitable exoplanets. It orbits within the habitable zone (temperate enough for liquid water to exist), with an "
            "equilibrium temperature of ~246 K (-27°C), colder than Earth's mean temperature but plausibly supportive of life under certain "
            "conditions. With 0.62 Earth masses and 0.91 Earth radii, TRAPPIST-1e is a sub-Earth-sized terrestrial world — smaller and "
            "lower-mass than our planet. Its higher density (~6.8 g/cm³) relative to Earth suggests an iron-rich interior, possibly indicating "
            "a larger core, more differentiation, or unusual composition. Like all planets in the TRAPPIST-1 system, TRAPPIST-1e is almost "
            "certainly tidally locked, creating a stark division: a perpetually sunlit day side and a frozen night side. However, tidal heating "
            "(friction from the star's gravitational pull) may pump energy into TRAPPIST-1e's interior, potentially powering hydrothermal vents "
            "and geochemical cycles on its surface. Some models suggest fast-rotating atmospheres could efficiently redistribute heat from day "
            "to night sides, maintaining moderate temperatures even on the night hemisphere. Such an atmosphere might contain water vapor, CO₂, "
            "or methane, creating a temperate watery world despite its alien environment."
        ),
        "scientific_facts": [
            "TRAPPIST-1e orbits within the habitable zone — where liquid water can exist on a planetary surface.",
            "Its equilibrium temperature (~246 K) is lower than Earth's (~288 K), but potentially habitable.",
            "The planet is sub-Earth-sized (0.91 Earth radii, 0.62 Earth masses) — smaller than our planet.",
            "Its higher density (~6.8 g/cm³ vs Earth's 5.5 g/cm³) suggests an iron-enriched composition or smaller rocky core.",
            "TRAPPIST-1e is tidally locked: one hemisphere permanently faces TRAPPIST-1, the other faces darkness.",
            "Tidal heating may generate internal geothermal activity, potentially supporting subsurface life even if surface is frozen.",
            "Atmospheric circulation models suggest day-side temperatures could reach 373 K (100°C) while night-side remains freezing.",
            "TRAPPIST-1e should retain an atmosphere better than inner planets due to lower stellar radiation.",
            "JWST observations are planned to analyze any atmospheric composition via transmission spectroscopy.",
            "TRAPPIST-1e has the highest probability of habitability among all TRAPPIST-1 planets according to current models.",
        ],
        "did_you_know": [
            "If TRAPPIST-1e has a thick atmosphere with greenhouse gases, its surface could be warm enough for liquid water and life.",
            "The perpetual sunset line (terminator) between day and night could harbor a ring of habitable climates if winds redistribute heat.",
            "Future telescopes may be able to detect signs of life (biosignatures like oxygen or methane) in TRAPPIST-1e's atmosphere.",
        ],
        "formation_process": (
            "TRAPPIST-1e likely formed from accretion of rocky planetesimals within the habitable zone of TRAPPIST-1's protoplanetary disk. "
            "Its final position may have been shaped by planetary migration and resonant interactions with sibling planets, collectively "
            "establishing the current seven-planet resonant chain configuration."
        ),
        "future_evolution": (
            "TRAPPIST-1e will remain in its current habitability for many billions of years as TRAPPIST-1 is an ultracool dwarf with "
            "a main-sequence lifetime exceeding a trillion years. Over extremely long timescales (>10¹⁰ years), any atmosphere will gradually "
            "be photoevaporated by the star's low-level UV output. The planet may eventually become a cold, airless world or retain its "
            "atmosphere indefinitely depending on initial volatile inventory."
        ),
        "related_objects": ["TRAPPIST-1 System", "TRAPPIST-1b", "TRAPPIST-1f", "TRAPPIST-1g", "TRAPPIST-1 Star"],
        "parent_system": "TRAPPIST-1 Planetary System",
        "nasa_reference": "https://exoplanetarchive.ipac.caltech.edu/overview/TRAPPIST-1%20e",
    },

    # -------------------------------------------------------------------------
    # BROWN DWARFS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "2mass-j0523-1403")),
        "name": "2MASS J0523-1403",
        "category": "Brown Dwarf",
        "subtype": "Ultra-Cool Dwarf — Methane Dwarf (T-dwarf)",
        "tags": ["brown-dwarf", "ultracool", "T-dwarf", "methane-dwarf", "substellar", "nearby"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 2.4, "unit": "pc"},
            "coordinates": {"ra": "05h 23m 23.0s", "dec": "-14° 03' 50\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"estimated": 0.04, "unit": "solar_masses", "note": "Near hydrogen-burning limit"},
            "radius": {"estimated": 0.09, "unit": "solar_radii"},
            "luminosity": {"value": 3e-6, "unit": "solar_luminosities"},
            "surface_temperature": {"value": 850, "unit": "K"},
            "spectral_class": "T7",
        },
        "detailed_description": (
            "2MASS J0523-1403 is an ultracool T-dwarf brown dwarf located only 2.4 parsecs (7.83 light-years) from Earth, making it "
            "one of the nearest known substellar objects. With a surface temperature around 850 K, it straddles the boundary between "
            "M-dwarfs and cooler L-dwarfs and T-dwarfs. The designation 'T-dwarf' refers to its spectral type characterized by methane "
            "absorption bands in its near-infrared spectrum — methane (CH₄) condenses into the photosphere at temperatures below ~1,400 K. "
            "2MASS J0523-1403's low mass (~0.04 solar masses) places it near the hydrogen-burning limit; while slightly substellar, it "
            "retains residual deuterium fusion in its core, making it a borderline brown dwarf. Its extremely low luminosity (~3×10⁻⁶ L_sun) "
            "makes it difficult to detect optically; most observations come from infrared surveys like 2MASS (Two Micron All-Sky Survey, "
            "hence its name). The brown dwarf's proximity offers a unique opportunity to study early cooling phases of substellar objects: "
            "as it ages, its temperature and luminosity will gradually decline, transitioning through the L-dwarf regime (1,400–2,000 K) "
            "and eventually reaching Y-dwarf status (<700 K). Its atmosphere is rich in methane, water vapor, carbon monoxide, and clouds "
            "of silicate and iron dust grains, creating a complex layered structure."
        ),
        "scientific_facts": [
            "2MASS J0523-1403 is located only 2.4 parsecs away — one of the nearest known brown dwarfs to our Solar System.",
            "Its effective temperature of ~850 K is cooler than any main-sequence star but warmer than Jupiter's atmospheric top.",
            "The spectral class T7 confirms methane absorption in its spectrum — methane bands are defining features of T-dwarfs.",
            "Its mass (~0.04 solar masses = 42 Jupiter masses) places it near the hydrogen-burning mass limit (~0.013 solar masses).",
            "2MASS J0523-1403 retains deuterium fusion in its core, making it a weakly-fusing brown dwarf rather than a completely inert object.",
            "Its luminosity is ~10,000× dimmer than our Sun — most starlight from this object is emitted in near-infrared.",
            "Spectral features reveal water vapor, carbon monoxide, methane, and silicate cloud layers characteristic of T-dwarf atmospheres.",
            "As it ages over billions of years, 2MASS J0523-1403 will cool and eventually transition to Y-dwarf spectral classification.",
            "Its proximity enables detailed spectroscopic studies impossible for more distant brown dwarfs.",
            "Radial velocity and proper motion measurements constrain its orbit — it likely belongs to the disk population of the Milky Way.",
        ],
        "did_you_know": [
            "The James Webb Space Telescope can detect even colder T-dwarfs and Y-dwarfs, potentially finding solar neighbors previously hidden.",
            "If a massive Jupiter-sized exoplanet orbited 2MASS J0523-1403, it might generate enough heat to become visible with JWST.",
            "2MASS J0523-1403 may eventually cool to become a Y-dwarf — the coldest known brown dwarf spectral class, with temperatures similar to Earth.",
        ],
        "formation_process": (
            "2MASS J0523-1403 likely formed from gravitational collapse of a fragment in a molecular cloud during the star formation epoch, "
            "approximately 5 billion years ago. Its low mass prevented sufficient gravitational compression to ignite hydrogen fusion, "
            "yet its higher mass (compared to planets) allows deuterium fusion. It may have formed in a stellar cluster and subsequently "
            "ejected into the galactic disk via dynamical interactions."
        ),
        "future_evolution": (
            "2MASS J0523-1403 will gradually cool over the next 10 billion years, its luminosity declining as internal heat dissipates. "
            "It will eventually transition to Y-dwarf (< 700 K) and continue cooling indefinitely, eventually becoming a cold, dark "
            "object indistinguishable from a rogue planet."
        ),
        "related_objects": ["Lacaille 8760", "Proxima Centauri", "Ultracool Dwarfs"],
        "parent_system": "Milky Way — Local Neighborhood",
        "nasa_reference": "https://en.wikipedia.org/wiki/2MASS_J0523%E2%88%921403",
    },

    # -------------------------------------------------------------------------
    # VARIABLE STARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "algol-beta-persei")),
        "name": "Algol (Beta Persei)",
        "category": "Star",
        "subtype": "Eclipsing Binary — Algol-type Eclipsing Variable",
        "tags": ["variable-star", "eclipsing-binary", "spectroscopic-binary", "oscillating", "blue-giant"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 26.73, "unit": "ly"},
            "coordinates": {"ra": "03h 08m 10.1s", "dec": "+40° 57' 20.3\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "primary_star": {
                "mass": {"value": 3.59, "unit": "solar_masses"},
                "radius": {"value": 2.73, "unit": "solar_radii"},
                "luminosity": {"value": 98, "unit": "solar_luminosities"},
                "spectral_class": "B8V",
                "surface_temperature": {"value": 11500, "unit": "K"},
            },
            "secondary_star": {
                "mass": {"value": 0.81, "unit": "solar_masses"},
                "radius": {"value": 3.24, "unit": "solar_radii"},
                "spectral_class": "K0 IV",
            },
            "orbital_period": {"value": 2.8674, "unit": "days"},
            "orbital_separation": {"value": 0.0588, "unit": "AU"},
        },
        "detailed_description": (
            "Algol, the second-brightest star in the constellation Perseus, is a classical example of an Algol-type eclipsing binary — "
            "a hierarchical triple star system where the two brightest stars (a blue giant and a K-dwarf) orbit each other while gradually "
            "losing orbital energy via gravitational wave radiation (though GWs alone are negligible here). Algol orbits with a period of "
            "2.87 days, producing dramatic eclipses as the fainter secondary star periodically blocks the brighter primary. When the dimmer "
            "companion eclipses the primary, Algol's brightness drops by ~30% (from magnitude 2.1 to 3.4), creating an easily observable "
            "lightcurve dip detectable by naked-eye observers. The system's curious aspect is the 'Algol Paradox': the secondary (less massive, "
            "0.81 solar masses) is larger and more evolved than the primary despite having lower mass — this suggests mass transfer through "
            "Roche lobe overflow in the system's past. Material from the secondary's atmosphere is siphoned onto the primary's surface, both "
            "speeding up the primary's rotation and potentially triggering stellar activity. Modern observations reveal radial velocity variations, "
            "periodic eclipses, and additional perturbations from a third, unseen companion at large orbital separation."
        ),
        "scientific_facts": [
            "Algol's brightness drops by ~30% (1.3 magnitudes) during each eclipse — detectable without telescopes since antiquity.",
            "The orbital period of 2.8674 days produces eclipses every 2.87 days with a total eclipse duration of ~10 hours.",
            "The secondary star, despite lower mass, is larger than the primary — the Algol Paradox — indicating past mass transfer.",
            "Mass transfer from the secondary to the primary via Roche lobe overflow drives unpredictable fluctuations in eclipse depth.",
            "The primary star spins much faster (~90 km/s) than the secondary, likely due to angular momentum transfer from mass accretion.",
            "X-ray observations reveal coronal activity, attributed to magnetic reconnection in accretion-driven turbulence.",
            "A third, distant companion (visual magnitude ~12) orbits the close binary with a long orbital period (~1.9 years).",
            "The system gradually loses orbital energy via gravitational radiation, spiraling inward at ~5 milliseconds per decade.",
            "Timing variations in eclipse arrival times (O-C residuals) constrain the third companion's orbital parameters.",
            "Algol's photosphere shows spectral anomalies: enhanced metals and depleted hydrogen, consistent with ongoing mass transfer.",
        ],
        "did_you_know": [
            "Ancient observers knew of Algol's brightness variations and called it 'the Demon Star' or 'the Ghoul' — one of the first recognized variable stars.",
            "Wilhelm Herschel first proposed in the 18th century that Algol's variations were due to eclipses by a dark companion.",
            "The system demonstrates that even ancient civilizations tracked stellar behavior, laying foundations for modern astrophysics.",
        ],
        "formation_process": (
            "Algol formed from a collapsing molecular cloud fragment ~3 billion years ago, creating a hierarchical triple system via "
            "fragmentation during the collapsing phase. Initial stellar masses were higher; mass transfer and stellar evolution over "
            "billions of years drove the current configuration."
        ),
        "future_evolution": (
            "Algol will continue mass transfer for millions of years. The secondary will eventually exhaust its hydrogen envelope, becoming "
            "a white dwarf. The primary will also eventually evolve to the red giant phase, potentially leading to a common envelope event "
            "and dramatic orbital shrinkage. End state: a triple system containing a white dwarf primary and compact remnant secondary."
        ),
        "related_objects": ["Beta Lyrae", "Epsilon Aurigae", "Contact Binary Stars"],
        "parent_system": "Perseus OB Association",
        "nasa_reference": "https://science.nasa.gov/exoplanet-catalog/star/algol/",
    },

    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mira-omicron-ceti")),
        "name": "Mira (Omicron Ceti)",
        "category": "Star",
        "subtype": "Variable Star — Mira-type Long-Period Variable",
        "tags": ["variable-star", "pulsating", "AGB-star", "long-period", "red-giant"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 96.5, "unit": "ly"},
            "coordinates": {"ra": "02h 19m 20.8s", "dec": "-02° 58' 39\""},
            "galaxy_reference": "Milky Way",
        },
        "physical": {
            "mass": {"estimated": 0.68, "unit": "solar_masses"},
            "radius": {"min": 370, "max": 610, "unit": "solar_radii", "note": "Varies dramatically during pulsation cycle"},
            "luminosity": {"min": 75, "max": 200, "unit": "solar_luminosities"},
            "surface_temperature": {"min": 2400, "max": 3000, "unit": "K"},
            "spectral_class": "M7 IIe (at minimum); M6e at maximum",
            "pulsation_period": {"value": 331, "unit": "days"},
        },
        "detailed_description": (
            "Mira, the 'Wonderful Star,' is the archetypal Mira-type variable star — a pulsating asymptotic giant branch (AGB) star whose "
            "brightness fluctuates dramatically over a ~331-day cycle. At maximum brightness, Mira reaches magnitude 2.0 and ranks among the "
            "brightest stars in its night-sky region; at minimum, it fades to magnitude 10.1, becoming invisible to the naked eye. This "
            "~100-fold brightness variation (8 magnitudes) is caused by radial pulsations of the star's photosphere: as Mira's outer layers "
            "cyclically expand and contract, its radius oscillates between ~370 and ~610 solar radii (so large that if centered on our Sun, "
            "Mira's surface would engulf Jupiter's orbit). Its surface temperature correlates with radius: when contracting and heating, "
            "Mira's surface reaches ~3,000 K (brightest phase); as it expands and cools, temperature drops to ~2,400 K (dimmest phase). "
            "Spectral observations reveal dramatic changes: at maximum light, Mira displays an M7 spectral class with strong water-vapor "
            "absorption; at minimum, it weakens to M6. The star is shedding its outer hydrogen envelope into space via stellar wind, creating "
            "expanding shells of gas and dust detected via radio and infrared observations. Mira's binary nature (confirmed by spectroscopy) "
            "reveals a white dwarf companion in a wide, 10,000+ AU orbit, complicating interpretations of pulsation models."
        ),
        "scientific_facts": [
            "Mira's brightness varies by ~100× (8 magnitudes) over a 331-day cycle — among the most extreme variable stars.",
            "Its radius expands from ~370 to ~610 solar radii; if centered at the Sun, it would extend past Jupiter's orbit.",
            "Pulsation is driven by hydrogen-ionization instability in the photosphere; density and temperature oscillations propagate outward.",
            "Surface temperature varies between 2,400–3,000 K during the pulsation cycle.",
            "Mira is in the final stages of stellar evolution: an AGB star shedding its hydrogen envelope via stellar wind.",
            "Dense shells of carbon monoxide have been detected in the circumstellar envelope via radio observations.",
            "The companion white dwarf does not significantly affect Mira's pulsations but influences long-term orbital evolution.",
            "Timing observations show quasi-periodic variations in pulsation period, attributed to coupling with the companion or internal restructuring.",
            "Infrared excess from circumstellar dust around Mira traces episodic dust ejection during pulsation maxima.",
            "Mira's pulsations follow a complex quasi-periodic pattern, not perfectly regular, indicating nonlinear dynamics.",
        ],
        "did_you_know": [
            "Mira was the first variable star recognized as such, noted by ancient astronomers as the 'Wonderful Star' that appeared and disappeared.",
            "Mira inspired the naming convention for all similar stars: 'Mira variables' or 'Mira-type stars.'",
            "If Mira were placed at our Sun's location, its extended atmosphere would engulf Earth and Mars during maximum expansion.",
        ],
        "formation_process": (
            "Mira formed ~8 billion years ago from a molecular cloud and evolved through main-sequence hydrogen burning as a solar-mass star. "
            "It ascended the red giant branch ~1 billion years ago, then moved to the AGB phase after helium core exhaustion. Current pulsations "
            "result from shell hydrogen-burning instability during the late AGB phase."
        ),
        "future_evolution": (
            "Mira will continue pulsations for another ~10,000–100,000 years before shedding its entire hydrogen envelope, eventually becoming "
            "a planetary nebula. Its white dwarf core will cool over billions of years, eventually becoming a cold white dwarf / brown dwarf remnant."
        ),
        "related_objects": ["Long-Period Variables", "AGB Stars", "Planetary Nebulae"],
        "parent_system": "Milky Way — Local Galactic Neighborhood",
        "nasa_reference": "https://en.wikipedia.org/wiki/Mira",
    },

    # -------------------------------------------------------------------------
    # PLANETARY NEBULAE
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "ngc-2440")),
        "name": "NGC 2440 — The Colorful Nebula",
        "category": "Nebula",
        "subtype": "Planetary Nebula — Complex Multipole",
        "tags": ["planetary-nebula", "white-dwarf", "ejected-envelope", "multicolor", "AGB"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 4000, "unit": "pc"},
            "coordinates": {"ra": "07h 41m 38.5s", "dec": "-18° 13' 15\""},
            "galaxy_reference": "Milky Way",
            "physical_size": {"diameter": 0.4, "unit": "ly"},
        },
        "physical": {
            "central_white_dwarf": {
                "mass": {"estimated": 0.6, "unit": "solar_masses"},
                "radius": {"value": 0.008, "unit": "solar_radii"},
                "surface_temperature": {"value": 160000, "unit": "K"},
                "luminosity": {"value": 10000, "unit": "solar_luminosities"},
            },
            "nebular_mass": {"estimated": 0.2, "unit": "solar_masses"},
            "expansion_velocity": {"value": 30, "unit": "km/s"},
            "age": {"estimated": 15000, "unit": "years"},
        },
        "detailed_description": (
            "NGC 2440 is one of the most strikingly beautiful and complex planetary nebulae known, featuring vivid multicolored shells "
            "and exotic internal structures. The nebula surrounds a white dwarf with a surface temperature exceeding 160,000 K — one of "
            "the hottest known white dwarfs. This extreme heat ionizes the surrounding nebular gas, causing it to glow across the visible "
            "spectrum: hydrogen recombination produces deep red hues (H-alpha at 656.3 nm), oxygen ionization creates striking emerald green "
            "(O-III at 500.7 nm), and nitrogen emission contributes ruby and pink tones. NGC 2440's internal structure reveals complex "
            "morphology: an inner bright elliptical shell surrounds the white dwarf, followed by multiple concentric fainter shells and "
            "extended filamentary structures. The nebula's outer emission suggests episodic ejection events during the star's final AGB phase, "
            "creating a time-sequence of shells recording the mass-loss history. Spectroscopic observations reveal high expansion velocities "
            "(~30 km/s) and chemical composition dominated by hydrogen and helium with smaller abundances of heavier elements like carbon, "
            "nitrogen, oxygen, and sulfur. The nebula's highly ionized central regions contrast with cooler outer layers, tracing the gradient "
            "of ionizing radiation from the intense white dwarf. At an estimated age of ~15,000 years, NGC 2440 is youth ful among planetary "
            "nebulae, still expanding and brightening as its central white dwarf cools."
        ),
        "scientific_facts": [
            "NGC 2440's central white dwarf has a surface temperature of ~160,000 K — one of the hottest known white dwarfs.",
            "The nebular shell expands at ~30 km/s, implying an age of ~15,000 years since ejection from the progenitor star.",
            "Multiple concentric shells suggest episodic mass loss during the progenitor's final AGB phase.",
            "Oxygen-III emission (green color) dominates the inner nebula due to extreme ultraviolet radiation from the white dwarf.",
            "Spectroscopy reveals abundances consistent with nucleosynthesis in the progenitor AGB star.",
            "The nebula's complex morphology suggests asymmetric mass ejection, possibly from rapid rotation or binary interaction.",
            "The white dwarf's high luminosity (~10,000 L_sun) will gradually fade over billions of years as it cools.",
            "At its distance of ~4 kpc, NGC 2440 spans ~0.4 light-years in diameter — among the larger planetary nebulae.",
            "Future observations with JWST will reveal detailed spectroscopy of the complex ionization structure.",
            "The nebula is expanding faster than the sound speed (supersonic), indicating ongoing energy input from the white dwarf.",
        ],
        "did_you_know": [
            "NGC 2440 was discovered by William Herschel in 1790 using his famous 40-foot telescope.",
            "The nebula's vivid multicolor appearance in photographs makes it one of the most photographed planetary nebulae.",
            "If you could travel inside NGC 2440, the white dwarf would appear unreachably hot despite being mere light-hours away.",
        ],
        "formation_process": (
            "NGC 2440's progenitor was a solar-mass star that evolved through main-sequence burning for ~10 billion years, then "
            "ascended the red giant branch and subsequently the AGB. During the final ~1,000 years of AGB evolution, the star shed its "
            "hydrogen envelope via strong stellar wind, eventually ionizing the ejected material with ultraviolet radiation from the "
            "exposed white dwarf core."
        ),
        "future_evolution": (
            "NGC 2440 will continue expanding, becoming fainter and cooler as the white dwarf cools and the nebular gas disperses. "
            "Within ~20,000–30,000 years, the nebula will dissipate into the interstellar medium. The white dwarf will cool over "
            "billions of years, eventually becoming a dark, cold stellar remnant."
        ),
        "related_objects": ["Ring Nebula (M57)", "Helix Nebula (NGC 7293)", "Cat's Eye Nebula (NGC 6543)", "White Dwarfs"],
        "parent_system": "Milky Way — Disk",
        "nasa_reference": "https://en.wikipedia.org/wiki/NGC_2440",
    },

    # -------------------------------------------------------------------------
    # GLOBULAR CLUSTERS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "m13-great-globular-cluster")),
        "name": "M13 — The Great Globular Cluster",
        "category": "Star Cluster",
        "subtype": "Globular Cluster — Dense Stellar System",
        "tags": ["globular-cluster", "dense", "old-stars", "ancient", "harbinger-civilization"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 7100, "unit": "pc"},
            "coordinates": {"ra": "16h 41m 41.3s", "dec": "+36° 27' 35.5\""},
            "galaxy_reference": "Milky Way",
            "physical_size": {"diameter": 84, "unit": "ly"},
            "visual_magnitude": {"value": 5.8},
        },
        "physical": {
            "total_mass": {"estimated": 600000, "unit": "solar_masses"},
            "number_of_stars": {"estimated": 1000000},
            "central_density": {"value": "~1e5", "unit": "stars/pc³"},
            "core_radius": {"value": 1.4, "unit": "pc"},
            "half_light_radius": {"value": 8.9, "unit": "pc"},
            "age": {"value": 13.0, "unit": "Billion years"},
        },
        "detailed_description": (
            "M13 (catalogued as Messier 13 or NGC 6205) is the most magnificent globular cluster visible from the Northern Hemisphere and "
            "one of the oldest known structures in the Milky Way. Containing an estimated 1 million stars compressed into a sphere ~84 light-years "
            "in diameter, M13's central density is extraordinarily extreme: ~100,000 stars per cubic parsec, compared to ~0.00001 stars/pc³ in "
            "the Solar neighborhood. From Earth, M13 appears as a bright, diffuse fuzzy spot visible to the naked eye under dark skies; telescopes "
            "resolve it into a spectacular jewel box of thousands of pinpoint stars. The cluster's age (~13 billion years) places it among the oldest "
            "stellar systems, formed during the earliest epoch of Galactic assembly. Its stars have nearly completed hydrogen nuclear burning, with "
            "many evolved into red giants and white dwarfs. Dynamically, M13 is transitioning from a relaxed, virialized state toward core collapse: "
            "stellar encounters gradually concentrate mass inward, eventually forming a black hole or neutron star binary at the core. High-resolution "
            "X-ray observations reveal an active core region, likely harboring accreting binary systems. The cluster orbits the Galactic center in a "
            "highly eccentric, inclined orbit, likely a remnant of a satellite galaxy captured by the Milky Way billions of years ago."
        ),
        "scientific_facts": [
            "M13 contains ~1 million stars compressed into an 84-light-year diameter sphere.",
            "Its central density reaches ~100,000 stars per cubic parsec — 10 billion times denser than our Solar neighborhood.",
            "Age estimates place M13 at ~13 billion years — nearly as old as the universe (13.8 Gy).",
            "The cluster's core radius is only ~1.4 parsecs (~4.6 light-years) — incredibly compact.",
            "Stars in M13 have undergone significant chemical alteration via multiple generations of stellar nucleosynthesis.",
            "The cluster exhibits evidence of mass segregation: more massive stars concentrate toward the center.",
            "Stellar collisions and mergers are feasible in M13's core — potentially creating unusual stellar populations.",
            "High-resolution Chandra X-ray observations reveal blue stragglers and accreting binary systems.",
            "M13's binary star systems include cataclysmic variables and low-mass X-ray binaries.",
            "The cluster is gradually losing stars to tidal disruption by the Galaxy's gravitational field.",
        ],
        "did_you_know": [
            "M13 was used as a target for the Arecibo Message in 1974 — a radio transmission intended for potential extraterrestrial civilizations.",
            "If the Arecibo Message is received by civilization orbiting M13's stars, they would receive it in ~25,000 years.",
            "M13 is observable with binoculars from Earth, making it accessible to amateur astronomers worldwide.",
        ],
        "formation_process": (
            "M13 formed ~13 billion years ago during the Galactic halo assembly, likely through hierarchical gravitational collapse "
            "within a dense region of primordial gas. Its primordial mass was likely 10× higher; stellar evolution and tidal evaporation "
            "have gradually reduced it to its current ~600,000 solar mass."
        ),
        "future_evolution": (
            "M13 will undergo continued core contraction due to stellar encounters, eventually forming a core black hole or neutron star. "
            "Tidal evaporation will gradually disperse the cluster, with stars spreading into the Galactic disk over ~100 billion years. "
            "The eventual fate: complete dissolution into a stellar stream."
        ),
        "related_objects": ["M22", "M80", "Globular Clusters", "Arecibo Observatory"],
        "parent_system": "Milky Way — Galactic Halo",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-13/",
    },

    # -------------------------------------------------------------------------
    # OPEN CLUSTERS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "pleiades-star-cluster")),
        "name": "The Pleiades — Seven Sisters Star Cluster",
        "category": "Star Cluster",
        "subtype": "Open Cluster — Young Reflection Nebula System",
        "tags": ["open-cluster", "young-stars", "reflection-nebula", "nearby", "moving-group"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 136.2, "unit": "pc"},
            "coordinates": {"ra": "03h 47m 00s", "dec": "+24° 07' 00\""},
            "galaxy_reference": "Milky Way",
            "physical_size": {"diameter": 13, "unit": "ly"},
            "visual_magnitude": {"brightest": 2.86},
        },
        "physical": {
            "number_of_stars": {"estimated": 1000},
            "brightest_stars": 9,
            "age": {"value": 125, "unit": "Million years"},
            "total_mass": {"estimated": 800, "unit": "solar_masses"},
            "central_density": {"value": 0.1, "unit": "stars/pc³"},
            "primary_composition": "Young, hot, blue stars (B and A type)",
        },
        "detailed_description": (
            "The Pleiades, also called the Seven Sisters in Greek mythology, is one of the nearest and brightest open star clusters, "
            "containing ~1,000 stars born together from a collapsing molecular cloud only ~125 million years ago. The cluster spans ~13 "
            "light-years and is easily visible to the naked eye (averaging magnitude 2.86 as the entire cluster), with the seven brightest "
            "stars (Alcyone, Atlas, Electra, Maia, Merope, Taygeta, Pleione) forming the easily recognizable asterism. The Pleiades' stars "
            "are predominantly young, hot, massive stars of B and A spectral type, with surface temperatures exceeding 8,000 K. These blue "
            "giants burn hydrogen rapidly, possessing main-sequence lifetimes of only ~100–1,000 million years compared to our Sun's 10-billion-year "
            "lifespan. The cluster is embedded within reflection nebulae (primarily NGC 1432 and NGC 1435), where starlight scatters off surrounding "
            "dust clouds, creating stunning blue-hued wisps in telescope images and photographs. This reflection nebulosity will dissipate within "
            "the next ~10 million years as stellar radiation and stellar winds clear the surrounding dust. The Pleiades serves as a crucial "
            "astronomical laboratory: its known age, distance, and composition make it a standard cosmic distance marker (distance ladder rung), "
            "while its stellar mass function and dynamical evolution provide insights into open cluster lifecycles. The cluster is gravitationally "
            "unbound — stars gradually escape into the Galactic disk."
        ),
        "scientific_facts": [
            "The Pleiades contains ~1,000 stars born in the same molecular cloud ~125 million years ago.",
            "The cluster is easily visible to the naked eye, making it one of the most observed clusters since ancient times.",
            "Its distance (136.2 pc) is precisely measured via parallax, making it a key calibrator for the cosmic distance ladder.",
            "The brightest Pleiades stars are hot blue giants with surface temperatures exceeding 10,000 K.",
            "Reflection nebulae surround the young cluster, indicating recent formation from a dusty molecular cloud.",
            "The cluster is gradually dispersing due to gravitational interactions; stars are escaping into the Galactic disk.",
            "Mass segregation is evident: massive stars concentrate near the cluster center; low-mass stars are more dispersed.",
            "Several cluster stars exhibit active accretion, indicating recent planetary system formation.",
            "Infrared observations reveal dust signatures consistent with ongoing debris disk evolution around Pleiades stars.",
            "Future observations will track the cluster's gradual dissolution and transformation into a stellar stream.",
        ],
        "did_you_know": [
            "Ancient cul­tures worldwide (Greeks, Mayas, Aboriginal Australians, Japanese) referenced the Pleiades in mythology and calendars.",
            "A person standing on one of the Pleiades stars would see the other six as brilliant points of light, each outshining any object in our night sky.",
            "The Pleiades are approaching our Solar System at ~8 km/s; they'll come closest to us in ~79,000 years.",
        ],
        "formation_process": (
            "The Pleiades formed ~125 million years ago via gravitational collapse of a giant molecular cloud in a star-forming region. "
            "Fragmentation during collapse created ~1,000–2,000 stars; subsequent dynamical evolution and tidal evaporation have reduced "
            "the population as stars escape."
        ),
        "future_evolution": (
            "The Pleiades will gradually dissolve: within ~250 million years, the cluster will no longer be gravitationally bound. Its "
            "stars will disperse into the Galactic disk, eventually becoming indistinguishable from the field population. Over billions of "
            "years, massive stars will explode as supernovae, while low-mass stars survive and cool to become white dwarfs."
        ),
        "related_objects": ["Hyades", "Beehive Cluster (M44)", "Open Clusters"],
        "parent_system": "Milky Way — Local Galactic Disk",
        "nasa_reference": "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-45-the-pleiades/",
    },

    # -------------------------------------------------------------------------
    # SUPERNOVA REMNANTS & RELATED PHENOMENA
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "tycho-supernova-remnant")),
        "name": "Tycho Supernova Remnant — SNR B1572+0449",
        "category": "Supernova Remnant",
        "subtype": "Type Ia Supernova Remnant — Young, Expanding Shell",
        "tags": ["supernova-remnant", "type-ia", "blast-wave", "X-ray-source", "historical-supernova"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 2600, "unit": "pc"},
            "coordinates": {"ra": "00h 25m 29.1s", "dec": "+64° 14' 24\""},
            "galaxy_reference": "Milky Way",
            "physical_size": {"diameter": 17, "unit": "ly"},
            "age_since_explosion": {"value": 451, "unit": "years"},
        },
        "physical": {
            "shock_velocity": {"value": 21000, "unit": "km/s"},
            "temperature_behind_shock": {"value": 30000000, "unit": "K"},
            "x_ray_luminosity": {"value": 3e34, "unit": "erg/s"},
            "progenitor_mass": {"estimated": 1.4, "unit": "solar_masses", "note": "White dwarf in binary system"},
            "explosion_energy": {"estimated": "10e51", "unit": "erg"},
        },
        "detailed_description": (
            "The Tycho Supernova Remnant marks the site of the famous supernova observed by Tycho Brahe on November 11, 1572 — the last "
            "naked-eye supernova clearly visible in the Milky Way. At maximum light, it briefly rivaled the brightness of Venus, and for "
            "~16 months remained visible in daylight. Over 450 years later, the expanding blast wave has produced a bright X-ray and radio "
            "source now residing 2.6 kpc away. The explosion was a Type Ia supernova — thermonuclear runaway in a white dwarf binary system "
            "where material from a companion star accretes onto the white dwarf's surface. When the white dwarf's core pressures and temperatures "
            "exceed the threshold for turbulent carbon-oxygen burning, a detonation wave propagates outward, completely disrupting the star and "
            "ejecting ~1.4 solar masses of nuclear ash into space at velocities ~21,000 km/s. This tremendous kinetic energy compresses the "
            "surrounding interstellar medium into a thin shell, heating material behind the shock to tens of millions of Kelvin and producing "
            "intense X-ray radiation observable with modern satellites. The remnant is now ~17 light-years across and still expanding. High-resolution "
            "X-ray images from Chandra reveal a bright outer shell where the shock wave compresses gas, and dimmer interior regions filled with hot "
            "remnant material gradually cooling by radiation. Spectroscopic observations identify expanding shells of iron, nickel, silicon, and "
            "sulfur — elements synthesized during the explosion and now dispersing to form components of future stars and planets."
        ),
        "scientific_facts": [
            "Tycho observed the supernova on November 11, 1572; it remained visible for ~16 months without telescopes.",
            "The explosion was a Type Ia supernova from a binary white dwarf-normal star system.",
            "Expansion velocity of ~21,000 km/s indicates an explosion energy of ~10⁵¹ ergs (comparable to Type Ia models).",
            "Temperature behind the shock reaches ~30 million K, producing intense X-ray emission (L_x ~ 3×10³⁴ erg/s).",
            "The remnant has expanded to ~17 light-years across over 450 years of expansion.",
            "Chandra X-ray observations reveal complex filamentary structure with spatial variations in shock temperature.",
            "Ejected material contains iron, nickel, silicon, sulfur, and other elements synthesized during thermonuclear burning.",
            "The remnant will continue expanding and fading over ~10,000 years before blending with the interstellar medium.",
            "Progenitor identification remains uncertain; no surviving companion star has been definitively identified.",
            "The system demonstrates that Type Ia supernovae release consistent energy (~10⁵¹ erg), making them useful cosmological distance indicators.",
        ],
        "did_you_know": [
            "Tycho's observations of the 1572 supernova helped establish that supernovae are 'fixed star' phenomena, not atmospheric events.",
            "Type Ia supernovae are used as 'standard candles' to measure cosmic distances; this led to the discovery of cosmic acceleration (dark energy).",
            "If you could travel inside Tycho's remnant, the hot gas would vaporize you instantly despite appearing empty from Earth.",
        ],
        "formation_process": (
            "The Tycho supernova originated from a binary system containing a white dwarf and a normal companion star. Over millions of years, "
            "material transferred from the companion accreted onto the white dwarf's surface, eventually triggering thermonuclear detonation "
            "in the hydrogen-rich envelope, followed by carbon-oxygen burning in the core."
        ),
        "future_evolution": (
            "The remnant will continue expanding and cooling over the next ~10,000 years, merging with the surrounding interstellar medium. "
            "Eventually, the ejected material will mix with interstellar gas, enriching molecular clouds and potentially seeding new star formation. "
            "The white dwarf companion, if it survived, may continue accreting material, eventually triggering another explosion."
        ),
        "related_objects": ["Crab Nebula (M1)", "Cassiopeia A", "SN 1987A Remnant", "Type Ia Supernovae"],
        "parent_system": "Milky Way — Perseus Arm",
        "nasa_reference": "https://science.nasa.gov/mission/chandra/observations/tycho-supernova-remnant/",
    },

     # -------------------------------------------------------------------------
    # EXTREME MAGNETIC NEUTRON STARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sgr-1806-20")),
        "name": "SGR 1806-20",
        "category": "Neutron Star",
        "subtype": "Magnetar",
        "tags": ["magnetar", "neutron-star", "extreme-magnetic", "soft-gamma-repeater", "galactic-center"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 50000, "unit": "ly"},
            "coordinates": {"ra": "18h 08m 39.3s", "dec": "-20° 24' 39\""},
            "galaxy_reference": "Milky Way",
            "location": "Near Galactic Center, Radio Arc region",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses", "note": "Typical neutron star mass"},
            "radius": {"value": 10, "unit": "km", "note": "Extremely compact"},
            "age": {"value": 1500, "unit": "years", "note": "Estimated from supernova remnant"},
            "magnetic_field": {"value": 2e15, "unit": "gauss", "note": "One of strongest known fields"},
            "rotation_period": {"value": 7.5, "unit": "seconds"},
            "surface_temperature": {"value": 5e6, "unit": "K"},
            "luminosity": {"value": 1e33, "unit": "erg/s", "note": "During quiescence"},
        },
        "detailed_description": (
            "SGR 1806-20 is one of the most extreme magnetars known to science, located approximately "
            "50,000 light-years from Earth near the galactic center. This magnetar possesses the strongest "
            "magnetic field ever measured in the universe, reaching up to 2 quadrillion gauss - about "
            "100 trillion times stronger than Earth's magnetic field. The star is a soft gamma repeater, "
            "periodically unleashing enormous bursts of X-rays and gamma rays that can be detected across "
            "the galaxy. On December 27, 2004, SGR 1806-20 produced the largest magnetic flare ever "
            "recorded, releasing more energy in 0.2 seconds than the Sun emits in 100,000 years. The "
            "magnetar's crust is under extreme stress from its own magnetic field, causing starquakes that "
            "trigger these catastrophic energy releases. Its rotation period of 7.5 seconds is relatively "
            "slow for a neutron star, gradually slowing further due to magnetic braking. The magnetar is "
            "embedded in a radio nebula and is associated with a supernova remnant, indicating it formed "
            "from a core-collapse supernova approximately 1,500 years ago. The extreme physics of SGR "
            "1806-20 provides unique insights into quantum electrodynamics under conditions impossible to "
            "reproduce on Earth."
        ),
        "scientific_facts": [
            "The 2004 giant flare ionized Earth's upper atmosphere despite being 50,000 light-years away.",
            "SGR 1806-20's magnetic field is strong enough to erase credit cards from a distance of 200,000 km.",
            "The magnetar's surface gravity is 100 billion times stronger than Earth's gravity.",
            "During flares, SGR 1806-20 can reach temperatures of 10 billion degrees Celsius.",
            "The star's magnetic field lines are so strong they can tear apart atomic nuclei at the surface.",
            "SGR 1806-20 is part of a cluster of massive stars including the luminous blue variable LBV 1806-20.",
            "The magnetar's spin-down energy loss is equivalent to 100,000 times the Sun's total luminosity.",
            "Its magnetic field decays over millions of years, powering X-ray emission through field decay energy.",
            "The star's crust is only about 1 meter thick, with exotic matter in the core possibly including strange matter.",
            "SGR 1806-20's giant flare briefly outshone the full moon in gamma rays before being absorbed by Earth's atmosphere.",
            "The magnetar's environment includes a surrounding radio nebula extending several light-years.",
            "Its magnetic axis is misaligned with its rotation axis by approximately 20 degrees.",
        ],
        "formation_process": (
            "SGR 1806-20 formed from the core-collapse supernova of a massive star (likely >25 solar masses) "
            "approximately 1,500 years ago. The extreme magnetic field is thought to arise from either rapid "
            "rotation combined with convective dynamos during the first seconds after collapse, or from "
            "flux conservation amplifying the progenitor star's magnetic field by many orders of magnitude. "
            "The magnetar formed in a star cluster environment, suggesting its progenitor was part of a massive "
            "star-forming region near the galactic center."
        ),
        "future_evolution": (
            "SGR 1806-20 will continue to spin down over the next million years, gradually losing its "
            "magnetic field strength. As the field decays, the star's burst activity will decrease, eventually "
            "becoming a relatively quiet, old neutron star. In ~10^7 years, it may join the population of "
            "dim radio pulsars or become completely undetectable as its magnetic field weakens to typical "
            "neutron star levels."
        ),
        "related_objects": ["SGR 1900+14", "CXO J164710.2-455216", "1E 1841-045", "Soft Gamma Repeaters"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Radio Nebula G10.0-0.3", "Supernova Remnant"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "4u-0142+61")),
        "name": "4U 0142+61",
        "category": "Neutron Star",
        "subtype": "Magnetar with Protoplanetary Disk",
        "tags": ["magnetar", "protoplanetary-disk", "fallback-disk", "anomalous-x-ray-pulsar"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 13000, "unit": "ly"},
            "coordinates": {"ra": "01h 44m 19.5s", "dec": "+61° 45' 02\""},
            "galaxy_reference": "Milky Way",
            "location": "Cassiopeia direction",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "age": {"value": 100000, "unit": "years"},
            "magnetic_field": {"value": 1e13, "unit": "gauss"},
            "rotation_period": {"value": 8.7, "unit": "seconds"},
            "surface_temperature": {"value": 4e6, "unit": "K"},
            "disk_mass": {"value": 10, "unit": "earth_masses", "note": "Estimated fallback disk mass"},
        },
        "detailed_description": (
            "4U 0142+61 is a unique magnetar that possesses a fallback disk of material, making it the "
            "first neutron star known to have a protoplanetary disk-like structure. Located approximately "
            "13,000 light-years away in the direction of Cassiopeia, this anomalous X-ray pulsar challenges "
            "our understanding of magnetar formation and evolution. The star's magnetic field, while strong "
            "at 10 trillion gauss, is weaker than typical magnetars, suggesting it may be in a transitional "
            "evolutionary state. The surrounding disk, discovered through infrared observations, likely "
            "formed from material that fell back after the supernova explosion and failed to escape the "
            "star's gravitational pull. This disk extends to several hundred kilometers from the neutron star "
            "surface and may be forming planets or planetesimals in an environment of extreme radiation and "
            "gravity. The magnetar's X-ray emission shows periodic variations that correlate with its rotation, "
            "and it occasionally exhibits bursts similar to other magnetars, though less frequently. The "
            "presence of this disk provides a unique laboratory for studying planet formation under the most "
            "extreme conditions imaginable, where gravity is billions of times stronger than on Earth and "
            "magnetic fields can tear apart normal matter."
        ),
        "scientific_facts": [
            "The fallback disk around 4U 0142+61 is the first ever discovered around a magnetar.",
            "Temperatures in the inner disk reach 1,000 K despite the neutron star's extreme radiation field.",
            "The disk material is primarily composed of iron and nickel, heavy elements from the supernova.",
            "4U 0142+61's infrared emission is 10 times brighter than expected from the neutron star alone.",
            "The magnetar shows evidence for a 10-hour periodicity in its X-ray emission, possibly from disk warping.",
            "The star's spin-down rate suggests magnetic dipole radiation with additional torque from the disk.",
            "4U 0142+61 is one of the oldest known magnetars at ~100,000 years.",
            "The disk may be forming 'magnetoplanets' - planets adapted to extreme magnetic fields.",
            "This magnetar bridges the gap between classical magnetars and accretion-powered X-ray pulsars.",
            "The fallback disk extends to ~1 million km from the neutron star surface.",
            "4U 0142+61's radiation pressure is insufficient to completely evaporate the disk material.",
            "The magnetar's magnetic field creates a magnetosphere that truncates the disk at the Alfvén radius.",
        ],
        "formation_process": (
            "4U 0142+61 formed from a supernova explosion ~100,000 years ago. Unlike most magnetars, a "
            "significant fraction of the ejected material failed to escape and fell back, forming a disk "
            "around the newborn neutron star. This fallback disk survived the initial radiation phase and "
            "has been slowly cooling and evolving over the past 100,000 years, potentially forming solid "
            "bodies in the process."
        ),
        "future_evolution": (
            "The magnetar will continue to spin down and its magnetic field will decay. The fallback disk "
            "may eventually form planets or be consumed by the neutron star. In ~1 million years, 4U "
            "0142+61 may evolve into a dim isolated neutron star with a remnant planetary system, "
            "providing a unique example of post-supernova planet formation."
        ),
        "related_objects": ["AE Aquarii", "PSR J1257+12", "Pulsar Planets", "Fallback Disks"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Fallback Disk", "Potential Magnetoplanets"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # RARE AND EXOTIC NEBULAE
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "hubble-12")),
        "name": "Hubble 12 (Hb 12)",
        "category": "Planetary Nebula",
        "subtype": "Bipolar Planetary Nebula with Point-Symmetric Knots",
        "tags": ["planetary-nebula", "bipolar", "point-symmetric", "wrf-loops", "rare-structure"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 15000, "unit": "ly"},
            "coordinates": {"ra": "21h 12m 10.5s", "dec": "+57° 59' 05\""},
            "galaxy_reference": "Milky Way",
            "location": "Cassiopeia constellation",
        },
        "physical": {
            "central_star_mass": {"value": 0.6, "unit": "solar_masses"},
            "central_star_temperature": {"value": 120000, "unit": "K"},
            "nebula_radius": {"value": 0.3, "unit": "ly"},
            "expansion_velocity": {"value": 30, "unit": "km/s"},
            "age": {"value": 2000, "unit": "years"},
            "chemical_composition": {"helium": "enhanced", "nitrogen": "enhanced", "carbon": "normal"},
        },
        "detailed_description": (
            "Hubble 12 is an exceptionally rare and complex planetary nebula that challenges our understanding "
            "of stellar death processes. Located approximately 15,000 light-years away in Cassiopeia, this "
            "nebula exhibits a unique combination of bipolar lobes and point-symmetric structures that "
            "defy simple explanation. The nebula's most striking features are the 'WRF loops' (named after "
            "discoverers Wong, Reynolds, and Fesen) - pairs of symmetric knots that appear to be rotated "
            "relative to each other, creating a complex helical pattern. These structures suggest the presence "
            "of a precessing jet or magnetic collimation mechanism during the nebula's formation. The central "
            "star, with a surface temperature of 120,000 K, emits intense ultraviolet radiation that ionizes "
            "the surrounding gas, creating the characteristic glow of planetary nebulae. Hubble 12's bipolar "
            "morphology indicates that the dying star expelled material preferentially along its rotational "
            "axis, possibly due to the presence of a binary companion or strong magnetic fields. The nebula's "
            "chemical composition shows enhanced helium and nitrogen, evidence of CNO cycle processing that "
            "occurred during the star's red giant phase. This object serves as a crucial laboratory for "
            "studying the complex hydrodynamics and magnetics involved in the final stages of low-mass "
            "stellar evolution, particularly the mechanisms that create asymmetries in what might otherwise "
            "be spherical outflows."
        ),
        "scientific_facts": [
            "Hubble 12 is one of only ~20 known planetary nebulae with point-symmetric structures.",
            "The WRF loops rotate by approximately 60 degrees relative to the bipolar axis.",
            "The nebula's central star is a [WO1] type - a rare oxygen-rich Wolf-Rayet central star.",
            "Hubble 12 shows evidence for a precessing jet with a period of ~1000 years.",
            "The nebula's expansion velocity varies from 20 km/s in the lobes to 40 km/s in the knots.",
            "Chemical analysis shows nitrogen abundance 3 times solar and helium abundance 1.5 times solar.",
            "The nebula's morphology suggests a binary companion with orbital period ~100 years.",
            "Hubble 12's bipolar lobes extend ~0.6 light-years from the central star.",
            "The point-symmetric knots are moving away from the central star at 35 km/s.",
            "The nebula's dust content includes both carbonaceous and silicate grains.",
            "Hubble 12 is one of the youngest planetary nebulae known at only ~2,000 years old.",
            "The nebula's ionization stratification shows highly ionized species in the center and neutral material in the outer knots.",
        ],
        "formation_process": (
            "Hubble 12 formed when a sun-like star exhausted its nuclear fuel and began shedding its outer "
            "layers. The complex point-symmetric structures likely resulted from a precessing jet launched "
            "by the dying star, possibly caused by a binary companion or magnetic fields. The bipolar "
            "morphology developed as material was preferentially expelled along the star's rotational axis "
            "during the asymptotic giant branch phase."
        ),
        "future_evolution": (
            "Over the next 10,000 years, Hubble 12 will continue expanding and fading as its central star "
            "cools and the nebula disperses into the interstellar medium. The complex structures will become "
            "more diffuse and eventually merge with the galactic gas, enriching it with processed material "
            "including helium, nitrogen, and carbon from the dying star."
        ),
        "related_objects": ["NGC 6302", "M2-9", "CRL 618", "Point-Symmetric Nebulae"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["WRF Loops", "Bipolar Lobes", "Central Star"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/1997/08/2245-Image.html",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "red-rectangle-nebula")),
        "name": "Red Rectangle Nebula (HD 44179)",
        "category": "Protoplanetary Nebula",
        "subtype": "Bipolar Nebula with X-Shaped Morphology",
        "tags": ["protoplanetary-nebula", "bipolar", "x-shaped", "baffled", "unique-morphology"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 2300, "unit": "ly"},
            "coordinates": {"ra": "06h 19m 58.2s", "dec": "-10° 38' 15\""},
            "galaxy_reference": "Milky Way",
            "location": "Monoceros constellation",
        },
        "physical": {
            "central_star_mass": {"value": 0.6, "unit": "solar_masses"},
            "central_star_temperature": {"value": 25000, "unit": "K"},
            "nebula_size": {"value": 0.05, "unit": "ly"},
            "expansion_velocity": {"value": 25, "unit": "km/s"},
            "age": {"value": 1000, "unit": "years"},
            "dust_composition": {"PAHs": "abundant", "carbonates": "present", "water_ice": "detected"},
        },
        "detailed_description": (
            "The Red Rectangle Nebula is one of the most unusual and visually striking protoplanetary nebulae "
            "in the night sky, located approximately 2,300 light-years away in Monoceros. This object gets its "
            "name from its distinctive rectangular shape and deep red coloration, created by a unique combination "
            "of dust scattering and molecular emission. The nebula exhibits a remarkable X-shaped morphology with "
            "concentric rung-like structures that resemble a ladder or baffle system, suggesting complex hydrodynamic "
            "processes during its formation. The central star, HD 44179, is a binary system where the visible component "
            "is a post-AGB star evolving toward the planetary nebula phase. The Red Rectangle's distinctive color "
            "comes from extended red emission (ERE), a mysterious photoluminescence process where ultraviolet light "
            "from the central star is absorbed by unknown carriers (likely carbon-based molecules) and re-emitted "
            "as red light. The nebula contains some of the most complex organic molecules detected in space, "
            "including polycyclic aromatic hydrocarbons (PAHs) and possibly even fullerenes (buckyballs). The "
            "X-shaped structure is thought to result from bipolar outflows interacting with a dense equatorial "
            "torus of dust and gas, creating shock fronts that illuminate the material. This object represents a "
            "crucial transitional phase between dying red giant stars and fully formed planetary nebulae, providing "
            "insights into how complex nebular morphologies develop during stellar death."
        ),
        "scientific_facts": [
            "The Red Rectangle is the only known nebula with a true rectangular shape.",
            "Extended red emission (ERE) in this nebula has quantum efficiency up to 50%, the highest known.",
            "The nebula contains some of the largest PAH molecules detected in space, with up to 400 carbon atoms.",
            "Spectroscopic observations have detected water ice and carbonates in the nebula's dust.",
            "The central binary has an orbital period of 318 days.",
            "The nebula's 'rungs' are expanding outward at 25 km/s, spaced roughly every 1000 years.",
            "The Red Rectangle shows evidence for a precessing bipolar outflow with period ~400 years.",
            "The nebula's dust temperature ranges from 150 K in the outer regions to 400 K near the central star.",
            "Molecular hydrogen emission creates a ladder-like pattern of bright and dark regions.",
            "The nebula's unique morphology may be caused by a dense equatorial disk that confines the outflow.",
            "The Red Rectangle is transitioning from a protoplanetary to a planetary nebula.",
            "Observations have detected C60 and C70 fullerene molecules in the nebula.",
        ],
        "formation_process": (
            "The Red Rectangle formed when a binary star system entered the post-AGB phase, with the primary "
            "star shedding its outer layers while a companion star helped shape the outflow into an X-shaped "
            "bipolar structure. The dense equatorial disk and periodic mass ejection created the distinctive "
            "rung-like features, while complex organic molecules formed in the carbon-rich outflow."
        ),
        "future_evolution": (
            "The Red Rectangle will continue to evolve into a bipolar planetary nebula over the next few "
            "thousand years. The central star will heat up to >100,000 K, ionizing the surrounding gas and "
            "causing the nebula to glow in characteristic emission lines. The rectangular shape will likely "
            "become more diffuse as the nebula expands into the interstellar medium."
        ),
        "related_objects": ["CRL 618", "IRAS 22272+5435", "Egg Nebula", "Protoplanetary Nebulae"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Bipolar Lobes", "Equatorial Disk", "Central Binary System"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2004/31/1717-Image.html",
    },

    # -------------------------------------------------------------------------
    # EXOTIC EXOPLANETS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "wasp-12b")),
        "name": "WASP-12b",
        "category": "Exoplanet",
        "subtype": "Ultra-Hot Jupiter with Atmospheric Escape",
        "tags": ["hot-jupiter", "ultra-hot", "atmospheric-escape", "tidal-locking", "inflated"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 871, "unit": "ly"},
            "coordinates": {"ra": "06h 30m 32.8s", "dec": "+29° 40' 20\""},
            "star_system": "WASP-12",
            "galaxy_reference": "Milky Way",
            "location": "Auriga constellation",
        },
        "physical": {
            "mass": {"value": 1.41, "unit": "jupiter_masses"},
            "radius": {"value": 1.79, "unit": "jupiter_radii", "note": "Highly inflated"},
            "orbital_period": {"value": 1.09, "unit": "days"},
            "semi_major_axis": {"value": 0.0234, "unit": "AU"},
            "equilibrium_temperature": {"value": 2600, "unit": "K"},
            "surface_gravity": {"value": 6.3, "unit": "m/s²"},
            "density": {"value": 0.29, "unit": "g/cm³", "note": "Extremely low density"},
        },
        "detailed_description": (
            "WASP-12b is an extraordinary ultra-hot Jupiter exoplanet that represents one of the most extreme "
            "cases of planetary atmospheric escape ever discovered. Located 871 light-years away in the constellation "
            "Auriga, this planet orbits its host star at a distance of only 0.0234 AU - so close that its orbital "
            "period is just 1.09 Earth days. The planet's surface temperature reaches a blistering 2,600 K, hot "
            "enough to melt iron and vaporize rock. This extreme heating has caused the planet to become dramatically "
            "inflated, with a radius 1.79 times that of Jupiter despite having only 1.41 times its mass, resulting in "
            "an extremely low density similar to that of expanded polystyrene. WASP-12b is tidally locked, with one "
            "side permanently facing its star while the other side remains in perpetual darkness. The planet is "
            "undergoing catastrophic atmospheric escape, losing mass at a rate of 189 quadrillion tons per year as "
            "its atmosphere is stripped away by the intense stellar radiation. This escaping material forms a comet-like "
            "tail that extends for hundreds of thousands of kilometers into space. The planet's dayside atmosphere "
            "contains molecular dissociation products including atomic hydrogen, ionized metals, and possibly even "
            "liquid iron clouds on the cooler night side. WASP-12b is predicted to be completely consumed by its "
            "host star within the next 10 million years, making it a dramatic example of planetary death through "
            "orbital decay and atmospheric stripping."
        ),
        "scientific_facts": [
            "WASP-12b is losing atmosphere at a rate of 189 million metric tons per second.",
            "The planet's escaping atmosphere forms a tail extending 3 planetary radii into space.",
            "WASP-12b's dayside temperature is hot enough to melt titanium and vaporize rocks.",
            "The planet's orbital period is decreasing by 29 milliseconds per year due to tidal decay.",
            "WASP-12b will be completely destroyed by its star in approximately 10 million years.",
            "The planet's low density makes it one of the 'fluffiest' exoplanets known.",
            "Spectroscopic observations have detected ionized calcium, iron, and magnesium in the escaping atmosphere.",
            "The planet's equilibrium temperature varies by over 1,000 K between day and night sides.",
            "WASP-12b's atmosphere contains aluminum oxide (corundum) which could form ruby-like clouds.",
            "The planet is so close to its star that it appears 50 times larger than the full moon from its surface.",
            "The intense radiation pressure on the dayside exceeds the planet's surface gravity.",
            "WASP-12b's host star is slightly evolved, having exhausted its core hydrogen.",
        ],
        "formation_process": (
            "WASP-12b likely formed further from its star and migrated inward through planetary scattering "
            "or disk-driven migration. As it spiraled closer, tidal forces heated and inflated the planet, "
            "while the intense radiation began stripping away its atmosphere. The current orbital decay "
            "suggests the planet will eventually be consumed by its host star."
        ),
        "future_evolution": (
            "WASP-12b is doomed to be destroyed within the next 10 million years as its orbit continues "
            "to decay. The planet will spiral into its host star, potentially causing a brightening event "
            "as the planetary material is accreted. Before its final destruction, the planet will continue "
            "losing atmosphere until only its core remains."
        ),
        "related_objects": ["WASP-19b", "KELT-9b", "WASP-121b", "Ultra-Hot Jupiters"],
        "parent_system": "WASP-12 System",
        "child_objects": ["Escaping Atmosphere", "Comet-like Tail"],
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/1430/wasp-12-b/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "gliese-436b")),
        "name": "Gliese 436b",
        "category": "Exoplanet",
        "subtype": "Hot Neptune with Exotic Water Ice",
        "tags": ["hot-neptune", "exotic-ice", "eccentric-orbit", "hot-ice", "transiting"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 33, "unit": "ly"},
            "coordinates": {"ra": "11h 42m 03.5s", "dec": "+26° 39' 32\""},
            "star_system": "Gliese 436",
            "galaxy_reference": "Milky Way",
            "location": "Leo constellation",
        },
        "physical": {
            "mass": {"value": 22.1, "unit": "earth_masses"},
            "radius": {"value": 4.3, "unit": "earth_radii"},
            "orbital_period": {"value": 2.64, "unit": "days"},
            "semi_major_axis": {"value": 0.028, "unit": "AU"},
            "equilibrium_temperature": {"value": 800, "unit": "K"},
            "surface_gravity": {"value": 11.8, "unit": "m/s²"},
            "density": {"value": 1.5, "unit": "g/cm³"},
            "orbital_eccentricity": {"value": 0.15, "note": "Surprisingly high for close-in planet"},
        },
        "detailed_description": (
            "Gliese 436b is a bizarre hot Neptune that challenges our understanding of planetary physics, "
            "located just 33 light-years away in the constellation Leo. This planet orbits very close to its "
            "red dwarf host star with a period of only 2.64 days, yet maintains a surprisingly high orbital "
            "eccentricity of 0.15 - unusual for planets in such close orbits where tidal forces should have "
            "circularized the orbit. The planet's most mysterious feature is its composition: models suggest it "
            "contains a large amount of water in exotic high-pressure ice phases that remain solid even at "
            "temperatures of 800 K. This 'hot ice' exists under extreme pressure in the planet's interior, "
            "creating conditions impossible to reproduce on Earth. The planet has a surprisingly low density for "
            "its mass, indicating a substantial atmosphere of hydrogen and helium overlying a water-rich interior. "
            "Gliese 436b experiences extreme tidal heating due to its eccentric orbit, which keeps its interior "
            "molten and drives a possible steam atmosphere. The planet's atmosphere shows signs of significant "
            "methane depletion and enhanced carbon monoxide, suggesting unusual atmospheric chemistry under high-temperature "
            "conditions. Observations have detected a possible trailing tail of escaping hydrogen, though at much "
            "lower rates than ultra-hot Jupiters. This planet serves as a crucial laboratory for understanding "
            "the diversity of Neptune-sized planets and the behavior of water under extreme conditions, providing "
            "insights into planetary composition and atmospheric physics that cannot be studied in our solar system."
        ),
        "scientific_facts": [
            "Gliese 436b contains water in exotic ice forms that remain solid at 800 K under high pressure.",
            "The planet's high eccentricity suggests an unseen companion planet maintaining the eccentric orbit.",
            "Gliese 436b's atmosphere shows a methane depletion factor of 700 compared to equilibrium predictions.",
            "The planet may have a comet-like tail of escaping hydrogen, though much smaller than hot Jupiters.",
            "Interior models suggest the planet is ~50% water by mass.",
            "Gliese 436b experiences tidal heating up to 10^19 watts, 100 times Earth's internal heat flow.",
            "The planet's host star is only 42% the Sun's mass but 46% of its radius.",
            "Gliese 436b was one of the first transiting Neptune-sized planets discovered.",
            "The planet's surface gravity is 3 times that of Earth despite being a Neptune-sized world.",
            "Gliese 436b's atmosphere contains significant amounts of carbon monoxide, unusual for a cool planet.",
            "The planet's equilibrium temperature is maintained at 800 K despite being 800x fainter than the Sun.",
            "Gliese 436b's orbital decay would take billions of years to spiral into its star.",
        ],
        "formation_process": (
            "Gliese 436b likely formed beyond the snow line of its star system where water ice was abundant, "
            "then migrated inward through interactions with the protoplanetary disk. The planet's eccentric "
            "orbit may have been excited by gravitational interactions with another planet or by the star's "
            "tidal evolution."
        ),
        "future_evolution": (
            "Gliese 436b will continue losing atmosphere slowly over billions of years, though not as rapidly "
            "as hot Jupiters. The planet's orbit will gradually circularize due to tidal forces, potentially "
            "reducing the tidal heating. The planet will likely survive for billions of years as a stable hot "
            "Neptune around its red dwarf host star."
        ),
        "related_objects": ["GJ 1214b", "HAT-P-11b", "WASP-107b", "Hot Neptunes"],
        "parent_system": "Gliese 436 System",
        "child_objects": ["Hot Ice Interior", "Steam Atmosphere"],
        "nasa_reference": "https://exoplanets.nasa.gov/exoplanet-catalog/663/gj-436-b/",
    },

    # -------------------------------------------------------------------------
    # RARE STELLAR REMNANTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cas-a-neutron-star")),
        "name": "Cas A Neutron Star (CXO J232327.9+584842)",
        "category": "Neutron Star",
        "subtype": "Central Compact Object with Carbon Atmosphere",
        "tags": ["central-compact-object", "carbon-atmosphere", "young-neutron-star", "supernova-remnant"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 11000, "unit": "ly"},
            "coordinates": {"ra": "23h 23m 27.9s", "dec": "+58° 48' 42\""},
            "galaxy_reference": "Milky Way",
            "location": "Cassiopeia constellation, center of Cas A supernova remnant",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "age": {"value": 340, "unit": "years"},
            "surface_temperature": {"value": 2e6, "unit": "K"},
            "magnetic_field": {"value": 1e11, "unit": "gauss"},
            "rotation_period": {"value": 0.017, "unit": "seconds", "note": "Not detected as pulsar"},
            "luminosity": {"value": 1e33, "unit": "erg/s"},
        },
        "detailed_description": (
            "The Cas A Neutron Star is one of the youngest known neutron stars in our galaxy, located at the "
            "center of the Cassiopeia A supernova remnant. This remarkable object is unique among neutron stars "
            "for having a pure carbon atmosphere, a feature never observed in any other stellar remnant. The "
            "neutron star was born approximately 340 years ago from a core-collapse supernova that was "
            "visible from Earth in the 1680s. Unlike most young neutron stars, the Cas A neutron star shows "
            "no radio pulsations or magnetar-like bursts, instead appearing as a faint X-ray source with a "
            "thermal spectrum. Its carbon atmosphere is incredibly thin - only about 4 centimeters thick - but "
            "extends the apparent radius of the neutron star to about 18 kilometers, creating a larger apparent "
            "surface area for X-ray emission. The star's surface temperature of 2 million K is surprisingly "
            "cool for its young age, suggesting rapid cooling through exotic processes possibly involving the "
            "formation of a neutron superfluid in its core. The Cas A neutron star has shown unprecedented "
            "cooling over the past decade, dropping in temperature by about 4% - evidence that may support the "
            "existence of neutron superfluidity and the direct Urca neutrino cooling process. This object provides "
            "a unique laboratory for studying the physics of ultra-dense matter, the composition of neutron star "
            "crusts, and the cooling behavior of the youngest neutron stars."
        ),
        "scientific_facts": [
            "The Cas A neutron star has the youngest known age of any neutron star at only 340 years.",
            "It is the only known neutron star with a pure carbon atmosphere.",
            "The star has cooled by 4% in just 10 years, the fastest cooling ever observed in a neutron star.",
            "The carbon atmosphere is only 4 cm thick but weighs 10^19 tons.",
            "The Cas A neutron star shows no radio pulsations, making it a 'quiet' neutron star.",
            "The star's rapid cooling may be evidence for neutron superfluidity in its core.",
            "The neutron star's apparent radius is 18 km due to its extended carbon atmosphere.",
            "The star's magnetic field is relatively weak at 10^11 gauss, typical for ordinary neutron stars.",
            "The Cas A neutron star is about 100 times less luminous than expected for its age.",
            "The star's cooling rate matches predictions for the direct Urca neutrino cooling process.",
            "The neutron star's surface gravity is 100 billion times stronger than Earth's.",
            "The Cas A neutron star may be the first evidence for a 'bare' neutron star without a hydrogen/helium envelope.",
        ],
        "formation_process": (
            "The Cas A neutron star formed from the core-collapse supernova of a massive star (~20 solar masses) "
            "approximately 340 years ago. The explosion created the Cassiopeia A supernova remnant and left behind "
            "this compact object. The carbon atmosphere likely formed from the burning of surface hydrogen and "
            "helium in the extreme temperatures following the supernova."
        ),
        "future_evolution": (
            "The Cas A neutron star will continue cooling rapidly over the next few centuries, potentially "
            "becoming undetectable in X-rays within ~1,000 years. The carbon atmosphere may gradually "
            "recombine with accreted material from the supernova remnant. The star will eventually join "
            "the population of older, cooling neutron stars in the galaxy."
        ),
        "related_objects": ["PSR J1852+0040", "RCW 103", "3C 58", "Central Compact Objects"],
        "parent_system": "Cassiopeia A Supernova Remnant",
        "child_objects": ["Carbon Atmosphere", "Cooling Core"],
        "nasa_reference": "https://chandra.harvard.edu/photo/2009/casa/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "rcw-103")),
        "name": "RCW 103 (1E 161348-5055.5)",
        "category": "Neutron Star",
        "subtype": "Variable Central Compact Object",
        "tags": ["central-compact-object", "variable-x-ray", "magnetar-like", "periodic-outbursts"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 10000, "unit": "ly"},
            "coordinates": {"ra": "16h 13m 48.3s", "dec": "-50° 55' 31\""},
            "galaxy_reference": "Milky Way",
            "location": "Norma constellation, center of RCW 103 supernova remnant",
        },
        "physical": {
            "mass": {"value": 1.4, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "age": {"value": 2000, "unit": "years"},
            "surface_temperature": {"value": 7e6, "unit": "K", "note": "During outburst"},
            "magnetic_field": {"value": 1e11, "unit": "gauss", "note": "Estimated, may be higher"},
            "rotation_period": {"value": 6.7, "unit": "hours", "note": "X-ray modulation period"},
            "luminosity": {"value": 1e34, "unit": "erg/s", "note": "During outburst"},
        },
        "detailed_description": (
            "RCW 103 is an enigmatic central compact object that challenges our understanding of neutron star "
            "physics. Located at the center of the RCW 103 supernova remnant approximately 10,000 light-years "
            "away, this neutron star exhibits bizarre behavior unlike any other compact object. The star shows "
            "extreme variability in X-ray emission, cycling between a quiescent state with luminosity of 10^33 erg/s "
            "and active outbursts reaching 10^34 erg/s. Most remarkably, the star exhibits a 6.7-hour periodic "
            "modulation in its X-ray brightness - an unusually long period for a neutron star and far too slow "
            "to be rotation. This period may represent the orbital period of a low-mass companion star, making "
            "RCW 103 potentially the youngest X-ray binary system known. Alternatively, the 6.7-hour period could "
            "represent an extremely slow rotation rate, suggesting the star has been dramatically braked by an "
            "unusually strong magnetic field or fallback disk interaction. The neutron star's age of ~2,000 years "
            "makes it one of the youngest known, yet it shows characteristics of both magnetars (variable X-ray "
            "emission) and central compact objects (thermal spectrum, no radio emission). During outbursts, the "
            "star's temperature reaches 7 million K, hot enough to ionize iron completely. RCW 103's unique behavior "
            "provides crucial insights into the early evolution of neutron stars, the diversity of compact object "
            "phenomena, and the possible existence of binary systems formed immediately after supernovae."
        ),
        "scientific_facts": [
            "RCW 103 shows a 6.7-hour periodicity, the longest ever observed in a neutron star.",
            "The star's X-ray luminosity varies by a factor of 1000 between quiescent and active states.",
            "RCW 103 may be the youngest known X-ray binary system at only 2,000 years old.",
            "The star's 6.7-hour period could represent an 8,000 km orbital separation from a companion.",
            "RCW 103 has undergone multiple outbursts since its discovery in 1980.",
            "The star's spectrum shows highly ionized iron and silicon during outbursts.",
            "RCW 103's age is estimated from its association with the supernova remnant.",
            "The star's magnetic field may be unusually high for a central compact object.",
            "RCW 103 shows no radio pulsations despite its young age.",
            "The star's outbursts occur roughly every 5-10 years.",
            "RCW 103's quiescent temperature is only 0.5 million K compared to 7 million K during outbursts.",
            "The star may represent a transitional object between magnetars and ordinary neutron stars.",
        ],
        "formation_process": (
            "RCW 103 formed from a core-collapse supernova ~2,000 years ago. The unusual 6.7-hour period may "
            "result from either an extremely slow rotation rate due to magnetic braking or the presence of a "
            "low-mass companion star that survived the supernova explosion, creating an immediate binary system."
        ),
        "future_evolution": (
            "RCW 103 will continue its variable behavior for thousands of years. If the 6.7-hour period represents "
            "orbital motion, the companion may eventually be consumed or the binary may evolve into a more typical "
            "X-ray binary. The star's magnetic field will decay over millions of years, potentially reducing its "
            "outburst activity."
        ),
        "related_objects": ["Cas A Neutron Star", "PSR J1852+0040", "Magnetars", "X-ray Binaries"],
        "parent_system": "RCW 103 Supernova Remnant",
        "child_objects": ["Potential Companion", "Variable X-ray Corona"],
        "nasa_reference": "https://chandra.harvard.edu/photo/2016/rcw103/",
    },

    # -------------------------------------------------------------------------
    # RARE BROWN DWARFS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "wise-0855-0714")),
        "name": "WISE 0855-0714",
        "category": "Brown Dwarf",
        "subtype": "Y-type Brown Dwarf (Coldest Known)",
        "tags": ["y-dwarf", "coldest-brown-dwarf", "free-floating", "ice-clouds", "nearby"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 7.2, "unit": "ly"},
            "coordinates": {"ra": "08h 55m 03.4s", "dec": "-07° 14' 42\""},
            "galaxy_reference": "Milky Way",
            "location": "Eridanus constellation",
        },
        "physical": {
            "mass": {"value": 3-10, "unit": "jupiter_masses"},
            "radius": {"value": 0.9, "unit": "jupiter_radii"},
            "effective_temperature": {"value": 250, "unit": "K", "note": "-23°C, comparable to Earth's interior"},
            "age": {"value": 1-10, "unit": "gigayears"},
            "luminosity": {"value": 1e-7, "unit": "solar_luminosities"},
            "surface_gravity": {"value": 20-40, "unit": "m/s²"},
            "atmospheric_pressure": {"value": 1-10, "unit": "bars"},
        },
        "detailed_description": (
            "WISE 0855-0714 is the coldest known brown dwarf and one of the most intriguing objects in the "
            "solar neighborhood, located just 7.2 light-years away in Eridanus. This Y-type brown dwarf has an "
            "effective temperature of only 250 K (-23°C), making it colder than Earth's polar regions and "
            "comparable to the temperature of a household freezer. With a mass between 3-10 Jupiter masses, "
            "WISE 0855-0714 straddles the boundary between the most massive planets and the least massive brown "
            "dwarfs. The object is free-floating in space, not orbiting any star, making it a rogue planetary-mass "
            "object. Its atmosphere is cold enough for water ice clouds to form, making it the first object outside "
            "our solar system where water clouds have been detected. Spectroscopic observations have revealed "
            "evidence for water vapor and possibly ammonia ice in its atmosphere, suggesting complex cloud chemistry "
            "similar to that of giant planets. The brown dwarf's extremely low luminosity and temperature make it "
            "incredibly difficult to detect, having been discovered only through infrared observations by the WISE "
            "satellite. WISE 0855-0714 represents the missing link between giant planets and brown dwarfs, providing "
            "a unique laboratory for studying atmospheric physics at temperatures previously only accessible in our "
            "own solar system's giant planets. This object helps us understand the lower temperature limit of brown "
            "dwarfs and the atmospheric chemistry that occurs at planet-like temperatures in objects that formed "
            "like stars."
        ),
        "scientific_facts": [
            "WISE 0855-0714 is the coldest known brown dwarf at 250 K (-23°C).",
            "It is the fourth-closest known stellar system to the Sun.",
            "The object shows evidence for water ice clouds in its atmosphere.",
            "WISE 0855-0714's temperature is comparable to Earth's average surface temperature.",
            "The brown dwarf's mass is only 3-10 times that of Jupiter.",
            "It is a free-floating object, not orbiting any star.",
            "WISE 0855-0714 is the first Y-dwarf with detected atmospheric variability.",
            "The object's luminosity is only 1/10,000,000th that of the Sun.",
            "Spectroscopic evidence suggests the presence of water vapor and possibly ammonia.",
            "WISE 0855-0714's size is similar to Jupiter's despite having up to 10 times the mass.",
            "The object's proper motion is 8\"/year, indicating it's moving through space.",
            "WISE 0855-0714 may represent the lower mass limit for brown dwarf formation.",
        ],
        "formation_process": (
            "WISE 0855-0714 likely formed through the same process as stars - the gravitational collapse of a "
            "gas cloud - but with insufficient mass to sustain hydrogen fusion. Alternatively, it could have formed "
            "in a protoplanetary disk and been ejected, making it a 'planetary-mass object' that formed like a "
            "planet but now floats freely in space."
        ),
        "future_evolution": (
            "WISE 0855-0714 will continue cooling over billions of years, eventually reaching temperatures "
            "similar to that of interstellar space. As it cools, it will become increasingly difficult to detect, "
            "eventually becoming a 'failed star' that is essentially invisible to current astronomical instruments."
        ),
        "related_objects": ["WISE 1547-2617", "WISE 2209-2734", "Y-dwarfs", "Rogue Planets"],
        "parent_system": "Interstellar Space",
        "child_objects": ["Water Ice Clouds", "Ammonia Vapor"],
        "nasa_reference": "https://www.jpl.nasa.gov/news/nasas-wise-telescopes-discovers-coldest-brown-dwarf/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sdss-1416+13b")),
        "name": "SDSS 1416+13B",
        "category": "Brown Dwarf",
        "subtype": "T/Y Transition Brown Dwarf",
        "tags": ["t-y-transition", "cold-brown-dwarf", "companion", "metal-poor", "ancient"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 100, "unit": "ly", "note": "Estimated, uncertain"},
            "coordinates": {"ra": "14h 16m 31s", "dec": "+13° 19' 00\""},
            "galaxy_reference": "Milky Way",
            "location": "Bootes constellation",
        },
        "physical": {
            "mass": {"value": 20-50, "unit": "jupiter_masses"},
            "radius": {"value": 0.9, "unit": "jupiter_radii"},
            "effective_temperature": {"value": 500, "unit": "K"},
            "age": {"value": 5-10, "unit": "gigayears"},
            "luminosity": {"value": 1e-6, "unit": "solar_luminosities"},
            "metallicity": {"value": 0.1, "unit": "solar", "note": "Metal-poor"},
            "surface_gravity": {"value": 30, "unit": "m/s²"},
        },
        "detailed_description": (
            "SDSS 1416+13B is a fascinating brown dwarf that represents the transition between T-type and "
            "Y-type spectral classes, serving as a crucial bridge between warmer methane-dominated brown dwarfs "
            "and the coldest known objects. Located approximately 100 light-years away in Bootes, this object is "
            "a companion to a metal-poor primary star, making it one of the few brown dwarfs known to orbit a "
            "star with significantly sub-solar metallicity. With an effective temperature of around 500 K, "
            "SDSS 1416+13B is cold enough for ammonia clouds to form in its atmosphere, marking the transition "
            "from T-type to Y-type characteristics. The brown dwarf's spectrum shows strong methane absorption "
            "typical of T-dwarfs but also exhibits features suggesting the onset of ammonia absorption, characteristic "
            "of the coldest brown dwarfs. The metal-poor nature of its host star suggests that SDSS 1416+13B itself "
            "has reduced heavy element content, affecting its atmospheric chemistry and cooling rate. This object "
            "is particularly valuable for understanding atmospheric physics at the boundary between planet-like "
            "and star-like temperatures, where complex molecular chemistry involving water, methane, and ammonia "
            "creates distinctive spectral signatures. The brown dwarf's age of 5-10 billion years makes it one "
            "of the older known brown dwarfs, providing insights into how these objects evolve over cosmic time. "
            "SDSS 1416+13B serves as a benchmark object for testing atmospheric models of cold brown dwarfs and "
            "understanding the effects of metallicity on brown dwarf spectra and evolution."
        ),
        "scientific_facts": [
            "SDSS 1416+13B is one of the coldest known brown dwarfs at 500 K.",
            "It is a companion to a metal-poor star with only 10% solar metallicity.",
            "The brown dwarf shows both T-type and Y-type spectral features.",
            "SDSS 1416+13B may be the first brown dwarf showing ammonia absorption.",
            "The object's age of 5-10 billion years makes it an ancient brown dwarf.",
            "Its metal-poor composition affects its atmospheric chemistry and cooling.",
            "SDSS 1416+13B's spectrum shows extremely red near-infrared colors.",
            "The brown dwarf's mass is estimated at 20-50 Jupiter masses.",
            "It is one of the few T/Y transition objects known.",
            "SDSS 1416+13B's primary star is a common proper motion companion.",
            "The object's low metallicity makes it cooler for its age than solar-metallicity brown dwarfs.",
            "SDSS 1416+13B provides a benchmark for atmospheric models at 500 K.",
        ],
        "formation_process": (
            "SDSS 1416+13B formed alongside its primary star from the collapse of a metal-poor gas cloud. "
            "The low metallicity of the birth cloud resulted in both stars having reduced heavy element content, "
            "affecting the brown dwarf's formation and subsequent evolution."
        ),
        "future_evolution": (
            "SDSS 1416+13B will continue cooling over the next few billion years, eventually transitioning "
            "fully into the Y-type class as its temperature drops below 400 K. The metal-poor composition "
            "may cause it to cool more efficiently than solar-metallicity brown dwarfs, reaching lower final "
            "temperatures."
        ),
        "related_objects": ["WISE 0855-0714", "Gliese 229B", "T-dwarfs", "Y-dwarfs"],
        "parent_system": "SDSS 1416+13 System",
        "child_objects": ["Ammonia Clouds", "Methane Atmosphere"],
        "nasa_reference": "https://www.jpl.nasa.gov/news/the-coldest-brown-dwarfs/",
    },

    # -------------------------------------------------------------------------
    # SECTION 6: RARE VARIABLE STARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "v838-mon")),
        "name": "V838 Monocerotis",
        "category": "Variable Star",
        "subtype": "Luminous Red Nova with Light Echo",
        "tags": ["luminous-red-nova", "light-echo", "stellar-merger", "mysterious-outburst", "dust-formation"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 20000, "unit": "ly"},
            "coordinates": {"ra": "07h 04m 04.8s", "dec": "-03° 47' 15\""},
            "galaxy_reference": "Milky Way",
            "location": "Monoceros constellation",
        },
        "physical": {
            "current_mass": {"value": 5-10, "unit": "solar_masses"},
            "current_radius": {"value": 1570, "unit": "solar_radii", "note": "During outburst peak"},
            "effective_temperature": {"value": 2000, "unit": "K", "note": "During outburst"},
            "luminosity": {"value": 1e6, "unit": "solar_luminosities", "note": "Peak outburst"},
            "outburst_energy": {"value": 1e49, "unit": "ergs"},
            "expansion_velocity": {"value": 600, "unit": "km/s"},
            "dust_mass": {"value": 0.01, "unit": "solar_masses"},
        },
        "detailed_description": (
            "V838 Monocerotis is one of the most mysterious stellar outbursts ever recorded, a luminous red "
            "nova that suddenly brightened in 2002 to become one of the most luminous stars in the Milky Way. "
            "Located approximately 20,000 light-years away in Monoceros, this star underwent an extraordinary "
            "evolution, expanding from a normal star to a red supergiant with a radius of 1,570 solar radii - "
            "large enough to engulf the orbit of Mars. The outburst was not a typical nova or supernova but "
            "something entirely different, likely caused by the merger of two stars in a binary system. The "
            "most spectacular feature of V838 Mon is its light echo - an expanding shell of illumination that "
            "propagates through surrounding dust clouds, creating a spectacular display of evolving structures "
            "that resembles an expanding firework. The light echo has allowed astronomers to study the three-"
            "dimensional structure of the interstellar dust surrounding the star in unprecedented detail. V838 "
            "Mon's spectrum during outburst showed unusual features with strong molecular absorption bands, "
            "indicating rapid cooling and dust formation in the expanding ejecta. The star has since faded but "
            "remains much cooler and larger than before the outburst, now classified as an L-type supergiant. "
            "This event has provided crucial insights into stellar merger physics, the formation of massive stars, "
            "and the structure of interstellar dust. V838 Mon remains one of the best-studied examples of luminous "
            "red novae, a class of stellar explosions that may represent a common pathway for stellar evolution "
            "in binary systems."
        ),
        "scientific_facts": [
            "V838 Mon's outburst reached a peak luminosity of 1 million times that of the Sun.",
            "The star expanded to 1,570 solar radii, large enough to contain Mars' orbit.",
            "The light echo from V838 Mon is the largest ever observed, spanning several light-years.",
            "V838 Mon's expansion velocity reached 600 km/s during the outburst.",
            "The star formed ~0.01 solar masses of dust during the outburst.",
            "V838 Mon's light echo revealed complex dust structures in the surrounding interstellar medium.",
            "The star's spectrum showed strong molecular bands of TiO and VO during outburst.",
            "V838 Mon's outburst energy was equivalent to 10^49 ergs, less than a supernova but more than a nova.",
            "The star's current temperature is only 2,000 K, making it one of the coolest supergiants known.",
            "V838 Mon may have formed from the merger of a B-type star with a lower-mass companion.",
            "The light echo has been observed for over a decade, showing dust structures at different distances.",
            "V838 Mon's outburst may represent a common evolutionary pathway for binary stars.",
        ],
        "formation_process": (
            "V838 Monocerotis likely formed from the merger of two stars in a close binary system. The "
            "merger released enormous gravitational energy that caused the star to expand dramatically and "
            "heat up, creating the spectacular outburst. The surrounding dust clouds that create the light "
            "echo were already present in the interstellar medium before the outburst."
        ),
        "future_evolution": (
            "V838 Mon will continue to cool and contract over the next few thousand years, eventually "
            "evolving into a massive, cool supergiant or possibly collapsing directly into a black hole "
            "without a supernova explosion. The star may eventually return to a more normal stellar state "
            "or become a luminous infrared source embedded in its own dust envelope."
        ),
        "related_objects": ["V1309 Sco", "M85 OT", "M31 RV", "Luminous Red Novae"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Light Echo", "Dust Shell", "Expanding Ejecta"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2003/10/1740-Image.html",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "eta-carinae")),
        "name": "Eta Carinae",
        "category": "Variable Star",
        "subtype": "Luminous Blue Variable/Hypergiant Binary",
        "tags": ["luminous-blue-variable", "hypergiant", "binary-system", "great-eruption", "homunculus-nebula"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 7500, "unit": "ly"},
            "coordinates": {"ra": "10h 45m 03.6s", "dec": "-59° 41' 04\""},
            "galaxy_reference": "Milky Way",
            "location": "Carina constellation",
        },
        "physical": {
            "primary_mass": {"value": 100, "unit": "solar_masses"},
            "secondary_mass": {"value": 30-60, "unit": "solar_masses"},
            "primary_luminosity": {"value": 5e6, "unit": "solar_luminosities"},
            "orbital_period": {"value": 5.54, "unit": "years"},
            "primary_temperature": {"value": 20000, "unit": "K"},
            "wind_velocity": {"value": 500-3000, "unit": "km/s"},
            "mass_loss_rate": {"value": 1e-3, "unit": "solar_masses/year"},
            "nebula_mass": {"value": 10-20, "unit": "solar_masses"},
        },
        "detailed_description": (
            "Eta Carinae is one of the most massive and unstable stellar systems known in our galaxy, a "
            "luminous blue variable hypergiant that represents the extreme upper limits of stellar evolution. "
            "Located approximately 7,500 light-years away in Carina, this system consists of at least two massive "
            "stars in a highly eccentric 5.54-year orbit, with the primary star having an estimated mass of "
            "100 solar masses - one of the most massive stars known. Eta Carinae is famous for its 'Great "
            "Eruption' in the 1840s, when it became the second-brightest star in the sky and ejected the "
            "Homunculus Nebula, a bipolar structure containing 10-20 solar masses of material expanding at "
            "600-2000 km/s. The primary star is extremely unstable, with a luminosity of 5 million times that "
            "of the Sun and a mass-loss rate of 10^-3 solar masses per year in its powerful stellar wind. The "
            "binary interaction creates spectacular X-ray variations every 5.54 years when the stars make their "
            "closest approach, with the wind-wind collision zone producing hard X-rays that are partially "
            "absorbed by the dense wind of the primary star. Eta Carinae is surrounded by complex ejecta including "
            "the Homunculus Nebula, the Weigelt Blobs (dense clumps of material close to the star), and more "
            "extended outer ejecta from previous eruptions. This system provides a unique laboratory for studying "
            "the physics of extremely massive stars, stellar wind interactions, and the processes that lead to "
            "supernovae and gamma-ray bursts. Eta Carinae is expected to end its life in a hypernova or pair-"
            "instability supernova within the next few hundred thousand years, potentially producing a gamma-ray "
            "burst that could affect Earth if it were pointed in our direction."
        ),
        "scientific_facts": [
            "Eta Carinae's primary star is one of the most massive known at ~100 solar masses.",
            "The Great Eruption of 1843 made Eta Carinae the second-brightest star in the sky.",
            "The Homunculus Nebula contains 10-20 solar masses of ejected material.",
            "Eta Carinae loses mass at a rate of 10^-3 solar masses per year.",
            "The system's 5.54-year orbit creates spectacular X-ray variations.",
            "The stellar wind collision zone reaches temperatures of 10^7 K.",
            "Eta Carinae's luminosity is 5 million times that of the Sun.",
            "The system will likely end as a hypernova or pair-instability supernova.",
            "The Homunculus Nebula shows nitrogen enrichment from CNO cycle processing.",
            "Eta Carinae's wind velocity varies from 500 km/s at the equator to 3000 km/s at the poles.",
            "The system's total mass loss over the Great Eruption was equivalent to 10 Suns.",
            "Eta Carinae is one of the few LBVs that will produce a gamma-ray burst when it explodes.",
        ],
        "formation_process": (
            "Eta Carinae formed from the collapse of an extremely massive molecular cloud. The binary system "
            "likely formed together, with both stars being extremely massive. The Great Eruption was caused by "
            "radiation pressure exceeding the Eddington limit, leading to catastrophic mass ejection."
        ),
        "future_evolution": (
            "Eta Carinae will continue losing mass through its powerful stellar winds and may experience "
            "additional eruptions. Within the next few hundred thousand years, the primary star will likely "
            "undergo core collapse, producing a hypernova or pair-instability supernova that may generate a "
            "gamma-ray burst directed along its rotational axis."
        ),
        "related_objects": ["P Cygni", "LBV 1806-20", "Pistol Star", "Luminous Blue Variables"],
        "parent_system": "Eta Carinae System",
        "child_objects": ["Homunculus Nebula", "Weigelt Blobs", "Wind Collision Zone"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2007/32/2241-Image.html",
    },

    # -------------------------------------------------------------------------
    # RARE INTERACTING GALAXIES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "arp-87")),
        "name": "Arp 87",
        "category": "Interacting Galaxies",
        "subtype": "Bridge and Tail Galaxy Pair",
        "tags": ["interacting-galaxies", "tidal-tail", "star-bridge", "galaxy-collision", "star-formation"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 300000000, "unit": "ly"},
            "coordinates": {"ra": "15h 51m 02.3s", "dec": "+29° 25' 00\""},
            "galaxy_reference": "Local Supercluster",
            "location": "Draco constellation",
        },
        "physical": {
            "primary_mass": {"value": 1e11, "unit": "solar_masses"},
            "secondary_mass": {"value": 5e10, "unit": "solar_masses"},
            "separation": {"value": 80000, "unit": "ly"},
            "relative_velocity": {"value": 200, "unit": "km/s"},
            "tidal_tail_length": {"value": 100000, "unit": "ly"},
            "bridge_mass": {"value": 1e9, "unit": "solar_masses"},
            "star_formation_rate": {"value": 10, "unit": "solar_masses/year"},
        },
        "detailed_description": (
            "Arp 87 is a spectacular pair of interacting galaxies located approximately 300 million light-years "
            "away in the constellation Draco. This system showcases the dramatic effects of gravitational interaction "
            "between galaxies, featuring a large spiral galaxy (NGC 3808) and a smaller companion (NGC 3808B) connected "
            "by an apparent bridge of stars and gas, with the larger galaxy exhibiting a magnificent tidal tail "
            "extending over 100,000 light-years into space. The gravitational interaction between these galaxies has "
            "triggered intense star formation throughout both systems, particularly in the bridge region where gas "
            "has been compressed and heated by the collision. The spiral galaxy shows distorted spiral arms and a "
            "bright, active nucleus, while its companion appears more compact but shows signs of recent starburst "
            "activity. The tidal forces have pulled streams of gas, dust, and stars from both galaxies, creating "
            "the luminous bridge that connects them and the extended tail that trails behind the larger galaxy. "
            "Arp 87 represents a snapshot of the galaxy merger process, showing how gravitational interactions can "
            "reshape galaxies, trigger star formation, and eventually lead to the formation of larger elliptical "
            "galaxies through mergers. The system provides valuable insights into galaxy evolution, the role of "
            "interactions in shaping galactic structure, and the processes that drive starburst activity in "
            "colliding galaxies. This interaction will likely continue for hundreds of millions of years, eventually "
            "resulting in the merger of the two galaxies into a single, larger system."
        ),
        "scientific_facts": [
            "Arp 87's tidal tail extends over 100,000 light-years from the primary galaxy.",
            "The star bridge contains approximately 1 billion solar masses of material.",
            "Star formation in Arp 87 is 10 times higher than in normal spiral galaxies.",
            "The two galaxies are separated by only 80,000 light-years.",
            "Arp 87's interaction has triggered starburst activity throughout both galaxies.",
            "The tidal tail contains young blue star clusters formed during the interaction.",
            "Arp 87's galaxies are moving toward each other at 200 km/s.",
            "The bridge region shows some of the most active star formation in the system.",
            "Arp 87 represents an early stage of galaxy merger.",
            "The gravitational interaction has distorted the primary galaxy's spiral structure.",
            "Arp 87's total star formation rate is about 10 solar masses per year.",
            "The system will likely merge completely in 500 million years.",
        ],
        "formation_process": (
            "Arp 87 formed when two galaxies passed close enough for their gravitational fields to interact "
            "strongly. The tidal forces pulled material from both galaxies, creating the bridge and tail structures "
            "while compressing gas to trigger star formation. This interaction represents an early stage in the "
            "galaxy merger process."
        ),
        "future_evolution": (
            "Arp 87's galaxies will continue interacting for hundreds of millions of years, eventually merging "
            "into a single elliptical galaxy. The intense star formation will gradually decline as the available "
            "gas is consumed or expelled, and the resulting galaxy will be larger and more massive than either "
            "of the original components."
        ),
        "related_objects": ["Antennae Galaxies", "Mice Galaxies", "NGC 4676", "Interacting Galaxy Pairs"],
        "parent_system": "Local Supercluster",
        "child_objects": ["Tidal Tail", "Star Bridge", "Star-forming Regions"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2007/48/2261-Image.html",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "esO-350-40")),
        "name": "ESO 350-40 (The Cartwheel Galaxy)",
        "category": "Ring Galaxy",
        "subtype": "Collisional Ring Galaxy",
        "tags": ["ring-galaxy", "galaxy-collision", "star-formation-ring", "ripple-structure", "bullet-cluster"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 500000000, "unit": "ly"},
            "coordinates": {"ra": "01h 37m 41.0s", "dec": "-33° 42' 59\""},
            "galaxy_reference": "Local Supercluster",
            "location": "Sculptor constellation",
        },
        "physical": {
            "galaxy_mass": {"value": 5e11, "unit": "solar_masses"},
            "ring_diameter": {"value": 150000, "unit": "ly"},
            "ring_width": {"value": 30000, "unit": "ly"},
            "expansion_velocity": {"value": 300, "unit": "km/s"},
            "star_formation_rate": {"value": 100, "unit": "solar_masses/year"},
            "companion_mass": {"value": 1e11, "unit": "solar_masses"},
            "collision_age": {"value": 400, "unit": "million_years"},
        },
        "detailed_description": (
            "The Cartwheel Galaxy (ESO 350-40) is one of the most spectacular examples of a ring galaxy, "
            "located approximately 500 million light-years away in the constellation Sculptor. This striking "
            "object features a luminous outer ring 150,000 light-years in diameter, filled with brilliant blue "
            "star clusters and active star-forming regions, surrounding a relatively quiet central core. The "
            "Cartwheel's distinctive structure resulted from a high-speed collision with a smaller companion galaxy "
            "that passed through its center approximately 400 million years ago like a bullet. This collision created "
            "a powerful density wave that rippled outward through the galactic disk, compressing gas and triggering "
            "intense star formation in the expanding ring. The outer ring contains some of the most massive star "
            "clusters known, with individual clusters containing up to a million solar masses of stars. The galaxy's "
            "central region appears relatively normal and contains older, redder stars, while the outer ring is "
            "dominated by young, hot blue stars and glowing nebulae. The Cartwheel is surrounded by several "
            "companion galaxies, including the 'bullet' galaxy that caused the collision and two smaller companions "
            "that may eventually be absorbed. This system provides a spectacular laboratory for studying galaxy "
            "collisions, starburst triggers, and the formation of massive star clusters. The ring continues to "
            "expand at about 300 km/s and will eventually disperse, while the galaxy settles back into a more "
            "normal spiral or elliptical form over billions of years."
        ),
        "scientific_facts": [
            "The Cartwheel's ring spans 150,000 light-years in diameter.",
            "The ring is expanding at 300 km/s and contains 100 solar masses of star formation per year.",
            "The collision occurred ~400 million years ago when a companion passed through the galaxy center.",
            "The ring contains some of the most massive star clusters known.",
            "The Cartwheel's star formation rate is 100 times higher than in normal galaxies.",
            "The central galaxy contains older stars while the ring is dominated by young blue stars.",
            "The 'bullet' galaxy that caused the collision is still visible nearby.",
            "The Cartwheel's structure resembles ripples in a pond after a stone impact.",
            "The ring contains numerous H II regions and supernova remnants.",
            "The galaxy's total mass is approximately 5×10^11 solar masses.",
            "The Cartwheel will eventually evolve back into a normal spiral galaxy.",
            "The collision compressed gas by factors of 100-1000, triggering the starburst.",
        ],
        "formation_process": (
            "The Cartwheel Galaxy formed when a smaller companion galaxy passed directly through the center "
            "of a larger spiral galaxy. The high-speed collision created a density wave that expanded outward, "
            "compressing gas and triggering star formation in a ring-like structure that continues to expand "
            "through the galactic disk."
        ),
        "future_evolution": (
            "The Cartwheel's ring will continue expanding and eventually disperse over the next billion years. "
            "The galaxy will gradually settle back into a more normal spiral structure, though it will retain "
            "some evidence of the collision in its stellar populations and kinematics. The intense star formation "
            "in the ring will gradually decline as the gas is consumed."
        ),
        "related_objects": ["AM 0644-741", "Hoag's Object", "NGC 1291", "Ring Galaxies"],
        "parent_system": "Local Supercluster",
        "child_objects": ["Outer Ring", "Central Core", "Star Clusters"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2002/10/1604-Image.html",
    },

    # -------------------------------------------------------------------------
    # RARE HIGH-VELOCITY STARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "s5-hvs1")),
        "name": "S5-HVS1",
        "category": "Star",
        "subtype": "Hypervelocity Star",
        "tags": ["hypervelocity-star", "galactic-ejection", "sgr-a", "extreme-velocity", "b-type"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 29000, "unit": "ly"},
            "coordinates": {"ra": "00h 08m 30.5s", "dec": "-24° 08' 12\""},
            "galaxy_reference": "Milky Way",
            "location": "Grus constellation, escaping the galaxy",
        },
        "physical": {
            "mass": {"value": 2.35, "unit": "solar_masses"},
            "radius": {"value": 2.5, "unit": "solar_radii"},
            "temperature": {"value": 13000, "unit": "K"},
            "velocity": {"value": 1755, "unit": "km/s"},
            "galactic_escape_velocity": {"value": 1000, "unit": "km/s"},
            "age": {"value": 100, "unit": "million_years"},
            "luminosity": {"value": 200, "unit": "solar_luminosities"},
            "metallicity": {"value": 0.2, "unit": "solar"},
        },
        "detailed_description": (
            "S5-HVS1 is the fastest known hypervelocity star in the Milky Way, traveling at an incredible "
            "1,755 km/s - fast enough to escape the galaxy's gravitational pull entirely. Located 29,000 light-"
            "years from Earth in the constellation Grus, this B-type main-sequence star is on a trajectory that "
            "will take it out of the Milky Way forever. S5-HVS1 was ejected from the galactic center approximately "
            "100 million years ago, likely through interaction with the supermassive black hole Sagittarius A*. "
            "The star's extreme velocity exceeds the galaxy's escape velocity by a wide margin, making it a true "
            "intergalactic traveler. With a mass of 2.35 solar masses and a temperature of 13,000 K, S5-HVS1 is "
            "a relatively young, hot star that formed near the galactic center and was violently expelled before "
            "completing its main-sequence evolution. The star's low metallicity (20% of solar) is consistent with "
            "formation in the galactic center environment. S5-HVS1's trajectory can be traced back precisely to "
            "the galactic center, providing strong evidence for the Hills mechanism - the process by which binary "
            "stars interacting with a supermassive black hole can be torn apart, with one component captured and "
            "the other ejected at hypervelocity. This star serves as a unique probe of the galactic center's "
            "gravitational potential and the environment near Sagittarius A*. In about 100 million years, S5-HVS1 "
            "will leave the Milky Way entirely, becoming an intergalactic star wandering through intergalactic "
            "space."
        ),
        "scientific_facts": [
            "S5-HVS1 is the fastest known star at 1,755 km/s, nearly 0.6% the speed of light.",
            "The star exceeds the Milky Way's escape velocity by 755 km/s.",
            "S5-HVS1 was ejected from the galactic center 100 million years ago.",
            "The star's trajectory traces back precisely to Sagittarius A*.",
            "S5-HVS1 will leave the Milky Way entirely in ~100 million years.",
            "The star's metallicity is only 20% of solar, typical of galactic center stars.",
            "S5-HVS1 is a B-type main-sequence star with 2.35 solar masses.",
            "The star's ejection likely involved the Hills mechanism with Sgr A*.",
            "S5-HVS1 is currently 29,000 light-years from Earth but moving away rapidly.",
            "The star has traveled 50,000 light-years since its ejection 100 million years ago.",
            "S5-HVS1 provides constraints on the Milky Way's mass distribution and escape velocity.",
            "The star's companion (if any) was likely captured by Sgr A* during the ejection event.",
        ],
        "formation_process": (
            "S5-HVS1 formed near the galactic center as part of a binary system. When the binary passed too "
            "close to Sagittarius A*, tidal forces tore the pair apart. One star was captured by the black hole "
            "while S5-HVS1 was ejected at hypervelocity through the Hills mechanism, becoming the fastest known "
            "star in the galaxy."
        ),
        "future_evolution": (
            "S5-HVS1 will continue traveling through intergalactic space for billions of years. It will eventually "
            "leave the Milky Way's gravitational influence entirely, becoming an intergalactic wanderer. The star "
            "will continue its main-sequence evolution for another 500 million years before evolving into a "
            "giant star, all while traveling through empty space between galaxies."
        ),
        "related_objects": ["US 708", "HE 0437-5439", "Other Hypervelocity Stars", "Sagittarius A*"],
        "parent_system": "Milky Way Galaxy (formerly)",
        "child_objects": ["None"],
        "nasa_reference": "https://www.nasa.gov/feature/goddard/2019/hypervelocity-star-is-fastest-ever-seen-leaving-our-galaxy/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "us-708")),
        "name": "US 708",
        "category": "Star",
        "subtype": "Hypervelocity Helium Star",
        "tags": ["hypervelocity-star", "helium-star", "type-ia-supernova", "binary-ejection", "extreme-velocity"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 62000, "unit": "ly"},
            "coordinates": {"ra": "11h 35m 44.5s", "dec": "+33° 37' 43\""},
            "galaxy_reference": "Milky Way",
            "location": "Ursa Major constellation, escaping the galaxy",
        },
        "physical": {
            "mass": {"value": 0.5, "unit": "solar_masses"},
            "radius": {"value": 0.2, "unit": "solar_radii"},
            "temperature": {"value": 27000, "unit": "K"},
            "velocity": {"value": 1200, "unit": "km/s"},
            "galactic_escape_velocity": {"value": 1000, "unit": "km/s"},
            "age": {"value": 25, "unit": "million_years"},
            "luminosity": {"value": 5000, "unit": "solar_luminosities"},
            "helium_fraction": {"value": 0.99, "unit": "fraction"},
        },
        "detailed_description": (
            "US 708 is an extraordinary hypervelocity star that stands out even among the rare population of "
            "stars ejected from our galaxy. Located 62,000 light-years away in Ursa Major, this compact helium star "
            "travels at 1,200 km/s, fast enough to escape the Milky Way's gravitational pull. What makes US 708 "
            "truly remarkable is its nature as a stripped helium star and the mechanism behind its ejection - it "
            "was likely launched when its binary companion exploded as a Type Ia supernova. Unlike other hypervelocity "
            "stars ejected by the supermassive black hole, US 708 was propelled by the thermonuclear explosion of its "
            "white dwarf companion, making it the first known case of supernova ejection. The star is essentially the "
            "exposed helium core of a star that had its outer layers stripped away by binary interaction before the "
            "supernova event. With a surface temperature of 27,000 K and a luminosity 5,000 times that of the Sun, "
            "US 708 is extremely hot and compact, with a radius only 20% that of the Sun despite being half as massive. "
            "The star's composition is almost pure helium (99%), with trace amounts of heavier elements created during "
            "its evolution. US 708's trajectory suggests it originated in the galactic disk rather than the center, "
            "supporting the supernova ejection scenario. This star provides a unique window into Type Ia supernova "
            "progenitors, binary stellar evolution, and the physics of stellar explosions. US 708 will eventually "
            "leave the Milky Way entirely, becoming an intergalactic helium star carrying the signature of a "
            "Type Ia supernova that occurred millions of years ago."
        ),
        "scientific_facts": [
            "US 708 is the first known hypervelocity star ejected by a Type Ia supernova.",
            "The star is 99% helium, making it a stripped helium star.",
            "US 708 travels at 1,200 km/s, exceeding the galaxy's escape velocity.",
            "The star's companion exploded as a Type Ia supernova ~25 million years ago.",
            "US 708 has a surface temperature of 27,000 K and luminosity 5,000 times the Sun.",
            "The star's radius is only 0.2 solar radii despite having 0.5 solar masses.",
            "US 708 originated in the galactic disk, not the center.",
            "The star provides evidence for the single-degenerate Type Ia supernova model.",
            "US 708's ejection mechanism was completely different from black hole ejection.",
            "The star will leave the Milky Way in ~30 million years.",
            "US 708 is one of the hottest known hypervelocity stars.",
            "The star's composition shows evidence for CNO cycle processing.",
        ],
        "formation_process": (
            "US 708 formed as a normal star in a binary system. Mass transfer to its white dwarf companion "
            "stripped away its outer layers, leaving only a helium core. When the white dwarf reached the "
            "Chandrasekhar limit and exploded as a Type Ia supernova, the explosion ejected US 708 at hypervelocity.",
        ),
        "future_evolution": (
            "US 708 will continue traveling through space for millions of years, eventually leaving the Milky "
            "Way entirely. As a helium star, it will evolve differently from normal stars, potentially becoming "
            "a helium-rich white dwarf or exploding as a peculiar supernova type, all while wandering through "
            "intergalactic space."
        ),
        "related_objects": ["S5-HVS1", "HE 0437-5439", "Type Ia Supernovae", "Helium Stars"],
        "parent_system": "Milky Way Galaxy (formerly)",
        "child_objects": ["None"],
        "nasa_reference": "https://science.nasa.gov/astronomy/hypervelocity-stars/",
    },

    # -------------------------------------------------------------------------
    # RARE DARK NEBULAE
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "coalsack-nebula")),
        "name": "Coalsack Nebula",
        "category": "Dark Nebula",
        "subtype": "Molecular Cloud",
        "tags": ["dark-nebula", "molecular-cloud", "star-forming", "southern-sky", "dust-obscuration"],
        "difficulty_level": "beginner",
        "spatial": {
            "distance_from_earth": {"value": 600, "unit": "ly"},
            "coordinates": {"ra": "12h 52m", "dec": "-63° 00'"},
            "galaxy_reference": "Milky Way",
            "location": "Crux constellation, Southern Cross",
        },
        "physical": {
            "cloud_mass": {"value": 3500, "unit": "solar_masses"},
            "cloud_diameter": {"value": 70, "unit": "ly"},
            "dust_temperature": {"value": 15, "unit": "K"},
            "gas_density": {"value": 1000, "unit": "particles/cm³"},
            "visual_extinction": {"value": 10, "unit": "magnitudes"},
            "molecular_content": {"H2": "dominant", "CO": "trace", "dust": "1%"},
            "star_formation": {"value": "low", "note": "Limited star formation activity"},
        },
        "detailed_description": (
            "The Coalsack Nebula is the most prominent dark nebula in the southern sky, a vast molecular cloud "
            "that appears as a dark patch against the bright background of the Milky Way. Located approximately "
            "600 light-years away in the constellation Crux (the Southern Cross), this cloud spans about 70 light-"
            "years across and contains roughly 3,500 solar masses of gas and dust. The Coalsack is not truly empty "
            "space but rather a dense region of interstellar material that blocks light from background stars, "
            "creating its distinctive dark appearance. The cloud consists primarily of molecular hydrogen with "
            "temperatures around 15 K and densities of about 1,000 particles per cubic centimeter, typical for "
            "star-forming regions. Despite its mass, the Coalsack shows surprisingly little current star formation "
            "activity, possibly because it has not yet reached the critical density needed for gravitational collapse. "
            "The nebula contains numerous smaller dense cores where future star formation may occur, and some young "
            "stars have formed at its edges. The Coalsack has been known since ancient times and was cataloged by "
            "many early astronomers, including Ptolemy. It played an important role in navigation for southern "
            "hemisphere explorers and was used by the Maori of New Zealand in their celestial mythology. Modern "
            "observations in infrared and radio wavelengths reveal the complex structure of the cloud, including "
            "filaments, clumps, and regions of varying density that will eventually form new stars. The Coalsack "
            "provides an excellent laboratory for studying the early stages of star formation and the structure of "
            "interstellar molecular clouds."
        ),
        "scientific_facts": [
            "The Coalsack is the largest and most prominent dark nebula visible from Earth.",
            "The cloud blocks light from background stars by up to 10 magnitudes.",
            "The Coalsack contains 3,500 solar masses of gas and dust.",
            "Despite its size, the Coalsack has surprisingly little current star formation.",
            "The cloud's temperature is only 15 K, typical for molecular clouds.",
            "The Coalsack was known to ancient cultures including the Maori and Australian Aboriginal peoples.",
            "The nebula spans 70 light-years across the sky.",
            "The Coalsack's density is 1,000 particles per cubic centimeter.",
            "The cloud is primarily composed of molecular hydrogen.",
            "The Coalsack will eventually form hundreds of stars over the next few million years.",
            "The nebula appears dark because it blocks background starlight, not because it's empty.",
            "The Coalsack is located in the Carina-Sagittarius Arm of the Milky Way.",
        ],
        "formation_process": (
            "The Coalsack formed from the accumulation of interstellar gas and dust in the Milky Way's "
            "Carina-Sagittarius Arm. The cloud is part of a larger complex of molecular clouds in the southern "
            "sky and represents an early stage in the star formation process, where material has collected but "
            "has not yet begun collapsing to form stars in large numbers."
        ),
        "future_evolution": (
            "Over the next few million years, the Coalsack will gradually begin forming stars as dense regions "
            "within the cloud undergo gravitational collapse. The cloud will be gradually dispersed by stellar "
            "winds and radiation from the newly formed stars, eventually breaking up into smaller clouds and "
            "contributing to the interstellar medium."
        ),
        "related_objects": ["Barnard 68", "Horsehead Nebula", "Pipe Nebula", "Dark Nebulae"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Dense Cores", "Protostars (future)"],
        "nasa_reference": "https://science.nasa.gov/astronomy/dark-nebulae/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "barnard-68")),
        "name": "Barnard 68",
        "category": "Dark Nebula",
        "subtype": "Bok Globule",
        "tags": ["bok-globule", "dark-nebula", "protostellar", "molecular-cloud", "star-formation"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 500, "unit": "ly"},
            "coordinates": {"ra": "17h 22m 30.0s", "dec": "-23° 49' 34\""},
            "galaxy_reference": "Milky Way",
            "location": "Ophiuchus constellation",
        },
        "physical": {
            "cloud_mass": {"value": 2, "unit": "solar_masses"},
            "cloud_diameter": {"value": 0.25, "unit": "ly"},
            "dust_temperature": {"value": 16, "unit": "K"},
            "gas_density": {"value": 250000, "unit": "particles/cm³"},
            "visual_extinction": {"value": 30, "unit": "magnitudes"},
            "molecular_content": {"H2": "dominant", "CO": "trace", "dust": "1%"},
            "star_formation": {"value": "imminent", "note": "Near gravitational collapse"},
        },
        "detailed_description": (
            "Barnard 68 is a remarkably well-defined Bok globule - a small, dense dark nebula that appears as a "
            "perfect circular patch of darkness against the background star field. Located approximately 500 light-"
            "years away in Ophiuchus, this compact molecular cloud spans only about 0.25 light-years in diameter "
            "yet contains about 2 solar masses of material. Barnard 68 is one of the finest examples of a star "
            "forming region in the very early stages of collapse, with a central density of 250,000 particles per "
            "cubic centimeter - high enough that the cloud is on the verge of gravitational collapse. The globule "
            "is so dense that it blocks light from background stars by up to 30 magnitudes, making it completely "
            "opaque in visible light. Infrared observations, however, can penetrate the dust to reveal the cloud's "
            "structure and show that it contains complex internal density variations. Barnard 68 has a temperature "
            "of about 16 K and is primarily composed of molecular hydrogen with trace amounts of carbon monoxide "
            "and other molecules. The cloud shows evidence for slow contraction and may collapse to form a star "
            "within the next 100,000 years. Spectroscopic observations have detected the presence of complex "
            "organic molecules including methanol and formic acid, suggesting that the chemical conditions for "
            "planet formation may already exist in the cloud. Barnard 68 serves as a crucial laboratory for studying "
            "the earliest stages of star formation and the physics of molecular cloud collapse. Its simple, isolated "
            "nature makes it an ideal test case for theoretical models of how stars form from collapsing gas clouds."
        ),
        "scientific_facts": [
            "Barnard 68 is one of the most perfectly circular dark nebulae known.",
            "The cloud contains 2 solar masses of material in only 0.25 light-years of space.",
            "Barnard 68 blocks background starlight by 30 magnitudes, making it completely opaque.",
            "The cloud's central density is 250,000 particles per cubic centimeter.",
            "Barnard 68 is on the verge of gravitational collapse and may form a star soon.",
            "The cloud's temperature is only 16 K, typical for star-forming regions.",
            "Barnard 68 contains complex organic molecules including methanol.",
            "The cloud shows evidence for slow inward motion at 0.5 km/s.",
            "Barnard 68 is one of the best-studied Bok globules.",
            "The cloud's shape is remarkably circular, suggesting it's isolated and undisturbed.",
            "Barnard 68 will likely form a single star or small multiple system.",
            "The cloud is located in the Ophiuchus molecular cloud complex.",
        ],
        "formation_process": (
            "Barnard 68 formed from the fragmentation of a larger molecular cloud in the Ophiuchus complex. "
            "The globule became isolated and began accumulating mass through accretion from its surroundings. "
            "It has now reached a critical density where gravitational forces may overcome thermal pressure, "
            "leading to collapse and star formation."
        ),
        "future_evolution": (
            "Barnard 68 will likely undergo gravitational collapse within the next 100,000 years, forming one "
            "or more protostars. The collapse will heat the central region and eventually ignite nuclear fusion, "
            "creating a new star. The remaining material will either form planets or be dispersed by stellar "
            "winds from the newborn star."
        ),
        "related_objects": ["Barnard 35", "Bok Globules", "Coalsack Nebula", "Dark Nebulae"],
        "parent_system": "Ophiuchus Molecular Cloud",
        "child_objects": ["Future Protostar", "Molecular Cores"],
        "nasa_reference": "https://www.eso.org/public/images/eso0102a/",
    },

    # -------------------------------------------------------------------------
    #  RARE SUPERNOVA REMNANTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "sn-1987a")),
        "name": "SN 1987A",
        "category": "Supernova Remnant",
        "subtype": "Core-Collapse Supernova Remnant with Ring System",
        "tags": ["supernova-remnant", "core-collapse", "ring-system", "neutrino-detection", "nearby-supernova"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 168000, "unit": "ly"},
            "coordinates": {"ra": "05h 35m 28.0s", "dec": "-69° 16' 11\""},
            "galaxy_reference": "Large Magellanic Cloud",
            "location": "Tarantula Nebula region",
        },
        "physical": {
            "progenitor_mass": {"value": 20, "unit": "solar_masses"},
            "explosion_energy": {"value": 1e51, "unit": "ergs"},
            "ejecta_velocity": {"value": 30000, "unit": "km/s"},
            "ring_diameter": {"value": 1.7, "unit": "ly"},
            "ring_expansion": {"value": 2800, "unit": "km/s"},
            "neutrino_energy": {"value": 1e53, "unit": "ergs"},
            "remnant_age": {"value": 37, "unit": "years"},
        },
        "detailed_description": (
            "SN 1987A is the closest and best-studied supernova of the modern era, a spectacular core-collapse "
            "explosion that occurred in the Large Magellanic Cloud on February 23, 1987. Located 168,000 light-years "
            "away in the Tarantula Nebula region, this supernova was the first visible to the naked eye since "
            "Kepler's supernova of 1604, providing an unprecedented opportunity to study supernova physics in "
            "detail. The explosion of a 20-solar-mass blue supergiant star (Sanduleak -69° 202) defied theoretical "
            "expectations, as models predicted that red supergiants should explode. The supernova was detected "
            "through neutrinos hours before visible light appeared, confirming theories about the core-collapse "
            "mechanism and providing the first direct evidence that massive stars die through neutrino-driven "
            "explosions. SN 1987A's most striking feature is its complex ring system - three concentric rings of "
            "material expelled by the progenitor star 20,000 years before the explosion, now illuminated by the "
            "supernova's flash. The central ring, 1.7 light-years in diameter, has been brightening and developing "
            "hot spots as the supernova shock wave reaches it, creating spectacular changes visible year by year. "
            "The supernova has produced heavy elements including radioactive titanium-44, confirming predictions of "
            "nucleosynthesis in massive stars. Recent observations have revealed the forming neutron star or black "
            "hole remnant, though it remains obscured by dust. SN 1987A continues to evolve rapidly, providing a "
            "real-time laboratory for studying supernova physics, dust formation, and the birth of compact objects."
        ),
        "scientific_facts": [
            "SN 1987A was the first supernova detected through neutrinos before visible light.",
            "The supernova produced ~10^58 neutrinos, most of which passed through Earth.",
            "SN 1987A's progenitor was a blue supergiant, not the expected red supergiant.",
            "The supernova's rings were expelled 20,000 years before the explosion.",
            "SN 1987A confirmed theories about neutrino-driven supernova mechanisms.",
            "The supernova has been observed continuously for 37 years since 1987.",
            "SN 1987A produced heavy elements including titanium-44 and nickel-56.",
            "The central ring is being hit by the supernova shock wave, creating hot spots.",
            "The explosion energy was approximately 10^51 ergs, typical for core-collapse supernovae.",
            "SN 1987A's ejecta are expanding at 30,000 km/s.",
            "The supernova created ~0.1 solar masses of dust.",
            "SN 1987A will reveal its compact remnant as dust clears in coming decades.",
        ],
        "formation_process": (
            "SN 1987A resulted from the core collapse of a 20-solar-mass blue supergiant star. The star's iron "
            "core collapsed into a neutron star or black hole, releasing a burst of neutrinos that drove the "
            "explosion. The surrounding rings were expelled by the star 20,000 years earlier during a previous "
            "evolutionary phase."
        ),
        "future_evolution": (
            "SN 1987A will continue evolving as the shock wave interacts with the ring system, creating "
            "increasingly complex structures. The compact remnant (neutron star or black hole) will become "
            "visible as surrounding dust clears. The supernova will eventually disperse into the interstellar "
            "medium, enriching it with newly formed elements."
        ),
        "related_objects": ["Cassiopeia A", "Crab Nebula", "Tycho's Supernova", "Supernova Remnants"],
        "parent_system": "Large Magellanic Cloud",
        "child_objects": ["Ring System", "Compact Remnant", "Expanding Ejecta"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2017/38/3788-Image.html",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "crab-nebula")),
        "name": "Crab Nebula (M1, NGC 1952)",
        "category": "Supernova Remnant",
        "subtype": "Pulsar Wind Nebula",
        "tags": ["pulsar-wind-nebula", "crab-pulsar", "historical-supernova", "synchrotron-emission", "chinese-records"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 6500, "unit": "ly"},
            "coordinates": {"ra": "05h 34m 31.9s", "dec": "+22° 00' 52\""},
            "galaxy_reference": "Milky Way",
            "location": "Taurus constellation",
        },
        "physical": {
            "progenitor_mass": {"value": 10, "unit": "solar_masses"},
            "explosion_energy": {"value": 1e51, "unit": "ergs"},
            "nebula_diameter": {"value": 11, "unit": "ly"},
            "expansion_velocity": {"value": 1500, "unit": "km/s"},
            "pulsar_period": {"value": 33, "unit": "milliseconds"},
            "pulsar_magnetic_field": {"value": 1e12, "unit": "gauss"},
            "nebula_luminosity": {"value": 75000, "unit": "solar_luminosities"},
            "remnant_age": {"value": 967, "unit": "years"},
        },
        "detailed_description": (
            "The Crab Nebula is one of the most famous and intensively studied supernova remnants in the sky, "
            "the spectacular aftermath of a supernova explosion observed by Chinese and Arab astronomers in 1054 AD. "
            "Located 6,500 light-years away in Taurus, this pulsar wind nebula spans 11 light-years across and "
            "continues to expand at 1,500 km/s. At its heart lies the Crab Pulsar, a rapidly rotating neutron star "
            "spinning 30 times per second with one of the strongest magnetic fields known. The pulsar generates a "
            "powerful wind of relativistic particles that creates the nebula's spectacular synchrotron emission, "
            "producing light across the entire electromagnetic spectrum from radio to gamma rays. The Crab Nebula's "
            "distinctive appearance combines intricate filaments of ionized gas (the original supernova ejecta) with "
            "a diffuse blue glow from synchrotron radiation produced by particles spiraling in magnetic fields. The "
            "filaments are enriched with heavy elements including helium, oxygen, and nitrogen, providing direct "
            "evidence of nucleosynthesis in massive stars. The Crab Pulsar injects 10^38 ergs of energy into the "
            "nebula each second, making it one of the most powerful particle accelerators in the galaxy. The nebula "
            "serves as a crucial laboratory for studying supernova physics, pulsar wind interactions, and particle "
            "acceleration mechanisms. Historical records show the supernova was visible in daylight for 23 days and "
            "at night for 653 days, reaching magnitude -7 and outshining everything except the Sun and Moon. Today, "
            "the Crab Nebula continues to be one of the brightest X-ray and gamma-ray sources in the sky, providing "
            "insights into high-energy astrophysics that cannot be studied elsewhere."
        ),
        "scientific_facts": [
            "The Crab Nebula resulted from a supernova observed in 1054 AD by Chinese astronomers.",
            "The supernova was visible in daylight for 23 days and reached magnitude -7.",
            "The Crab Pulsar spins 30 times per second with a period of 33 milliseconds.",
            "The nebula expands at 1,500 km/s and is now 11 light-years across.",
            "The Crab Pulsar injects 10^38 ergs of energy into the nebula each second.",
            "The nebula's blue color comes from synchrotron radiation, not thermal emission.",
            "The Crab Nebula is one of the brightest X-ray sources in the sky.",
            "The filaments contain heavy elements created during the supernova.",
            "The Crab Pulsar's magnetic field is 10^12 times stronger than Earth's.",
            "The nebula serves as a calibration source for X-ray and gamma-ray telescopes.",
            "The Crab Nebula was the first object identified as a supernova remnant.",
            "The pulsar's spin-down rate matches the energy needed to power the nebula.",
        ],
        "formation_process": (
            "The Crab Nebula formed when a 10-solar-mass star exploded as a core-collapse supernova in 1054 AD. "
            "The explosion created the neutron star pulsar and ejected the filaments of heavy elements. The pulsar's "
            "rotational energy now powers the nebula through its relativistic particle wind."
        ),
        "future_evolution": (
            "The Crab Nebula will continue expanding and fading over the next 100,000 years. The pulsar will gradually "
            "spin down, reducing its energy output. Eventually, the nebula will disperse into the interstellar medium, "
            "enriching it with heavy elements while the pulsar continues as an isolated, slowly rotating neutron star."
        ),
        "related_objects": ["SN 1987A", "Cassiopeia A", "Vela Supernova Remnant", "Pulsar Wind Nebulae"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Crab Pulsar", "Synchrotron Nebula", "Heavy Element Filaments"],
        "nasa_reference": "https://hubblesite.org/contents/media/images/2005/37/1795-Image.html",
    },

]

# -------------------------------------------------------------------------
# PHASE 3: COSMIC OBJECTS - QUASARS, DARK NEBULAE, SUPERNOVA REMNANTS
# -------------------------------------------------------------------------

import uuid

COSMIC_OBJECTS_PHASE3 = [

    # -------------------------------------------------------------------------
    # SECTION 1: QUASARS - DISTANT ACTIVE GALACTIC NUCLEI
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "3c-273")),
        "name": "3C 273",
        "category": "Quasar",
        "subtype": "Optically Bright Quasar with Superluminal Jets",
        "tags": ["quasar", "active-galactic-nucleus", "superluminal-jet", "first-quasar", "blazar-like"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 2.4e9, "unit": "ly"},
            "coordinates": {"ra": "12h 29m 06.7s", "dec": "+02° 03' 09\""},
            "galaxy_reference": "Virgo Supercluster",
            "location": "Leo constellation",
            "redshift": {"value": 0.158, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 8.86e8, "unit": "solar_masses"},
            "bolometric_luminosity": {"value": 4e13, "unit": "solar_luminosities"},
            "jet_velocity": {"value": 0.997, "unit": "c", "note": "Apparent superluminal motion"},
            "accretion_disk_temperature": {"value": 100000, "unit": "K"},
            "emission_line_width": {"value": 10000, "unit": "km/s"},
            "radio_luminosity": {"value": 1e40, "unit": "erg/s"},
            "x-ray_luminosity": {"value": 1e45, "unit": "erg/s"},
            "host_galaxy_mass": {"value": 1e12, "unit": "solar_masses"},
        },
        "detailed_description": (
            "3C 273 is the brightest and first discovered quasar, a landmark object that revolutionized our "
            "understanding of the universe. Located 2.4 billion light-years away in Leo, this quasar has a "
            "bolometric luminosity of 4×10^13 solar luminosities, making it 100 times more luminous than our "
            "entire Milky Way galaxy. At its heart lies a supermassive black hole of 886 million solar masses, "
            "surrounded by an accretion disk heated to 100,000 K that emits enormous amounts of radiation across "
            "the electromagnetic spectrum. 3C 273 is famous for its spectacular jet, extending 60,000 light-years "
            "from the nucleus and exhibiting apparent superluminal motion - an optical illusion caused by material "
            "traveling at 99.7% the speed of light at a small angle to our line of sight. The quasar's discovery "
            "in 1963 by Maarten Schmidt solved the mystery of quasi-stellar objects and provided the first strong "
            "evidence for the existence of supermassive black holes. 3C 273 shows broad emission lines with widths "
            "of 10,000 km/s, indicating gas moving at extreme velocities near the black hole. The host galaxy is a "
            "giant elliptical with evidence for recent interactions, possibly triggering the quasar activity. "
            "3C 273 varies on timescales from hours to decades, allowing study of accretion physics near the "
            "event horizon. This object serves as a standard candle for cosmological studies and a laboratory for "
            "studying jet physics, accretion processes, and the extreme physics near supermassive black holes."
        ),
        "scientific_facts": [
            "3C 273 was the first quasar discovered, revolutionizing cosmology in 1963.",
            "The quasar is 100 times more luminous than the entire Milky Way galaxy.",
            "Its supermassive black hole weighs 886 million solar masses.",
            "3C 273's jet shows apparent superluminal motion, an illusion from near-light-speed travel.",
            "The quasar varies on timescales as short as hours, indicating a compact emission region.",
            "3C 273's redshift of 0.158 means we see it as it was 2.4 billion years ago.",
            "The jet extends 60,000 light-years from the galactic nucleus.",
            "3C 273 produces 10^45 erg/s in X-rays alone.",
            "The accretion disk radiates at 100,000 K, primarily in ultraviolet light.",
            "3C 273's host galaxy shows signs of recent merger or interaction.",
            "The quasar's emission lines are broadened by gas moving at 10,000 km/s.",
            "3C 273 has been observed continuously for over 50 years, providing unique long-term data.",
        ],
        "formation_process": (
            "3C 273 formed when a supermassive black hole at the center of a giant elliptical galaxy began "
            "actively accreting gas, likely triggered by a galaxy merger that funneled material to the nucleus. "
            "The accretion disk formed around the black hole heats to extreme temperatures, producing the "
            "quasar's enormous luminosity. The relativistic jet forms from magnetic field interactions near "
            "the spinning black hole."
        ),
        "future_evolution": (
            "3C 273 will continue its active phase for millions of years before gradually fading as the "
            "supply of accreting material is exhausted. The jet will continue expanding into intergalactic "
            "space, creating large-scale radio lobes. Eventually, the quasar will become a normal giant "
            "elliptical galaxy with a dormant supermassive black hole at its center."
        ),
        "related_objects": ["3C 279", "PKS 1510-089", "M87", "Quasars"],
        "parent_system": "Virgo Supercluster",
        "child_objects": ["Relativistic Jet", "Accretion Disk", "Broad Line Region"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "quasar-j0313-1806")),
        "name": "Quasar J0313-1806",
        "category": "Quasar",
        "subtype": "Most Distant Known Quasar",
        "tags": ["quasar", "most-distant", "early-universe", "supermassive-black-hole", "epoch-of-reionization"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 13.0e9, "unit": "ly"},
            "coordinates": {"ra": "03h 13m 32.9s", "dec": "-18° 06' 30\""},
            "galaxy_reference": "Early Universe",
            "location": "Eridanus constellation",
            "redshift": {"value": 7.64, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 1.6e9, "unit": "solar_masses"},
            "bolometric_luminosity": {"value": 2e13, "unit": "solar_luminosities"},
            "cosmic_age": {"value": 670, "unit": "million_years"},
            "accretion_rate": {"value": 200, "unit": "solar_masses/year"},
            "schwarzschild_radius": {"value": 4.7e9, "unit": "km"},
            "dust_mass": {"value": 1e8, "unit": "solar_masses"},
            "gas_mass": {"value": 1e10, "unit": "solar_masses"},
            "ionized_bubble_radius": {"value": 1.5, "unit": "Mpc"},
        },
        "detailed_description": (
            "Quasar J0313-1806 is the most distant quasar ever discovered, existing when the universe was "
            "only 670 million years old - just 5% of its current age. Located 13 billion light-years away in "
            "Eridanus, this remarkable object provides a unique window into the epoch of reionization when "
            "the first stars and galaxies were forming. The quasar is powered by a supermassive black hole "
            "already weighing 1.6 billion solar masses, challenging our understanding of how such massive "
            "black holes could form so quickly after the Big Bang. The quasar shines with a luminosity of "
            "2×10^13 solar luminosities, ionizing a bubble of hydrogen gas 1.5 megaparsecs in radius around "
            "it and contributing to the reionization of the universe. J0313-1806 shows evidence for a massive "
            "reservoir of gas and dust - 10 billion solar masses of gas and 100 million solar masses of dust - "
            "indicating rapid chemical enrichment in the early universe. The quasar's spectrum shows strong "
            "metal lines including carbon and iron, proving that multiple generations of stars had already "
            "lived and died by this early epoch. The black hole is accreting matter at 200 solar masses per "
            "year, near the Eddington limit, suggesting it grew through a period of extremely rapid accretion. "
            "This quasar provides crucial constraints on models of black hole formation and growth in the early "
            "universe, the timing of reionization, and the chemical evolution of the cosmos. J0313-1806 "
            "represents one of the first massive structures to form after the cosmic dark ages, serving as a "
            "beacon illuminating the early history of galaxy formation."
        ),
        "scientific_facts": [
            "J0313-1806 is the most distant quasar known, seen when the universe was only 670 million years old.",
            "Its black hole weighs 1.6 billion solar masses despite forming in the early universe.",
            "The quasar ionizes a bubble of hydrogen 1.5 megaparsecs in radius.",
            "J0313-1806 contains 10 billion solar masses of gas and 100 million solar masses of dust.",
            "The quasar shows strong metal lines, proving rapid chemical enrichment in the early universe.",
            "J0313-1806 accretes matter at 200 solar masses per year.",
            "The quasar's light has traveled 13 billion years to reach us.",
            "J0313-1806 contributes to the reionization of the universe.",
            "The black hole's mass challenges theories of early black hole formation.",
            "The quasar's host galaxy already contains significant dust and heavy elements.",
            "J0313-1806 was discovered using the Wide-field Infrared Survey Explorer (WISE) and confirmed with ground-based telescopes.",
            "The quasar's existence implies massive galaxy formation occurred earlier than expected.",
        ],
        "formation_process": (
            "J0313-1806 formed from the rapid growth of a massive seed black hole in the early universe, "
            "possibly through direct collapse of a massive gas cloud or through near-Eddington accretion from "
            "a stellar-mass black hole. The quasar's host galaxy must have formed stars rapidly to produce the "
            "observed heavy elements and dust so early in cosmic history."
        ),
        "future_evolution": (
            "J0313-1806 will continue its growth phase for hundreds of millions of years, eventually becoming "
            "one of the most massive black holes in the universe. The quasar's energetic output will help "
            "complete the reionization of the universe and regulate star formation in its host galaxy through "
            "powerful feedback mechanisms."
        ),
        "related_objects": ["ULAS J1342+0928", "PSO J172.3556+18.8437", "Early Universe Quasars"],
        "parent_system": "Early Universe",
        "child_objects": ["Ionized Bubble", "Dust Reservoir", "Host Galaxy"],
        "nasa_reference": "https://www.jpl.nasa.gov/news/nasa-telescope-finds-oldest-most-distant-quasar/",
    },

    # -------------------------------------------------------------------------
    # SECTION 2: BLAZARS - JET-DOMINATED ACTIVE GALAXIES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "blazar-markarian-421")),
        "name": "Markarian 421 (Mrk 421)",
        "category": "Blazar",
        "subtype": "High-Frequency-Peaked BL Lac Object",
        "tags": ["blazar", "bl-lac", "tevatron-source", "variable", "high-energy", "nearby-blazar"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 397e6, "unit": "ly"},
            "coordinates": {"ra": "11h 04m 27.3s", "dec": "+38° 12' 32\""},
            "galaxy_reference": "Local Supercluster",
            "location": "Ursa Major constellation",
            "redshift": {"value": 0.031, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 3e8, "unit": "solar_masses"},
            "jet_lorentz_factor": {"value": 10, "unit": "gamma"},
            "jet_angle": {"value": 2, "unit": "degrees", "note": "To line of sight"},
            "apparent_velocity": {"value": 6, "unit": "c", "note": "Superluminal motion"},
            "gamma-ray_luminosity": {"value": 1e45, "unit": "erg/s"},
            "x-ray_luminosity": {"value": 1e44, "unit": "erg/s"},
            "variability_timescale": {"value": 30, "unit": "minutes"},
            "host_galaxy_type": {"value": "elliptical", "note": "Giant elliptical"},
        },
        "detailed_description": (
            "Markarian 421 is one of the closest and most studied blazars, a high-frequency-peaked BL Lacertae "
            "object that serves as a fundamental laboratory for high-energy astrophysics. Located 397 million "
            "light-years away in Ursa Major, this blazar is characterized by a relativistic jet pointed almost "
            "directly toward Earth, making it appear extremely bright and variable across the electromagnetic "
            "spectrum. Mrk 421 was the first extragalactic source detected in TeV gamma rays, establishing it as "
            "a 'Tevatron' - a natural particle accelerator capable of producing particles with energies in the "
            "tera-electron-volt range, millions of times more energetic than visible light photons. The blazar "
            "exhibits dramatic variability on timescales from minutes to decades, with the most rapid changes "
            "occurring in just 30 minutes, implying an extremely compact emission region near the central black "
            "hole. The jet material travels with a Lorentz factor of 10 and appears to move at six times the "
            "speed of light due to relativistic effects. Mrk 421's spectrum peaks in the X-ray regime, making it "
            "an excellent target for studying synchrotron emission from relativistic electrons. The blazar has "
            "undergone several major outbursts, including a spectacular flare in 2000 when it became the brightest "
            "object in the X-ray sky. These events provide insights into particle acceleration mechanisms, jet "
            "physics, and the extreme conditions near supermassive black holes. Mrk 421's proximity and high "
            "luminosity make it a crucial calibration source for gamma-ray telescopes and a benchmark for "
            "testing theories of jet formation and high-energy emission processes."
        ),
        "scientific_facts": [
            "Mrk 421 was the first extragalactic TeV gamma-ray source discovered.",
            "The blazar varies on timescales as short as 30 minutes.",
            "Mrk 421's jet appears to move at 6 times the speed of light due to relativistic effects.",
            "The blazar is one of the closest known blazars at 397 million light-years.",
            "Mrk 421 can accelerate particles to TeV energies, making it a natural Tevatron.",
            "The jet is pointed only 2 degrees from our line of sight.",
            "Mrk 421's gamma-ray luminosity is 10^45 erg/s.",
            "The blazar underwent a spectacular outburst in 2000, becoming the brightest X-ray source.",
            "Mrk 421's spectrum peaks in X-rays, characteristic of HBL blazars.",
            "The blazar's black hole mass is estimated at 300 million solar masses.",
            "Mrk 421 serves as a calibration source for gamma-ray telescopes.",
            "The blazar shows evidence for particle acceleration near the jet base.",
        ],
        "formation_process": (
            "Mrk 421 formed when a supermassive black hole at the center of a giant elliptical galaxy developed "
            "a powerful relativistic jet pointed nearly toward Earth. The jet's alignment creates the blazar "
            "characteristics through relativistic beaming effects that enhance the observed luminosity and "
            "create rapid variability."
        ),
        "future_evolution": (
            "Mrk 421 will continue its active blazar phase for millions of years, with ongoing jet activity "
            "and variability. Eventually, the accretion rate will decline and the jet will weaken, transforming "
            "the object into a normal radio galaxy with a dormant supermassive black hole."
        ),
        "related_objects": ["Markarian 501", "PKS 2155-304", "BL Lacertae", "BL Lac Objects"],
        "parent_system": "Local Supercluster",
        "child_objects": ["Relativistic Jet", "Supermassive Black Hole", "Host Elliptical Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "blazar-pks-2155-304")),
        "name": "PKS 2155-304",
        "category": "Blazar",
        "subtype": "High-Frequency-Peaked BL Lac with Extreme Gamma-Ray Variability",
        "tags": ["blazar", "bl-lac", "extreme-variability", "gamma-ray", "tevatron", "southern-hemisphere"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 1.5e9, "unit": "ly"},
            "coordinates": {"ra": "21h 58m 52.1s", "dec": "-30° 13' 32\""},
            "galaxy_reference": "Distant Universe",
            "location": "Grus constellation",
            "redshift": {"value": 0.116, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 5e8, "unit": "solar_masses"},
            "jet_lorentz_factor": {"value": 15, "unit": "gamma"},
            "jet_angle": {"value": 1, "unit": "degrees", "note": "To line of sight"},
            "apparent_velocity": {"value": 10, "unit": "c", "note": "Superluminal motion"},
            "gamma-ray_luminosity": {"value": 5e45, "unit": "erg/s"},
            "x-ray_luminosity": {"value": 2e44, "unit": "erg/s"},
            "variability_timescale": {"value": 3, "unit": "minutes"},
            "doppler_factor": {"value": 20, "unit": "boost"},
        },
        "detailed_description": (
            "PKS 2155-304 is one of the most extreme and variable blazars known, a high-frequency-peaked "
            "BL Lacertae object that serves as a premier laboratory for studying the most energetic processes "
            "in the universe. Located 1.5 billion light-years away in Grus, this blazar is famous for its "
            "extraordinary gamma-ray variability, having undergone the largest flare ever observed from a blazar "
            "in 2006 when it became 50 times brighter than usual in just a few hours. PKS 2155-304 exhibits "
            "dramatic variability on timescales as short as 3 minutes, implying emission regions smaller than "
            "the event horizon of its supermassive black hole and challenging our understanding of jet physics. "
            "The blazar's jet is pointed within 1 degree of our line of sight and appears to move at 10 times "
            "the speed of light due to relativistic effects, with a Doppler boosting factor of 20 that enhances "
            "its apparent luminosity. PKS 2155-304 was one of the first blazars detected in TeV gamma rays and "
            "remains one of the brightest TeV sources in the southern sky, making it a crucial target for "
            "ground-based gamma-ray observatories. The blazar's spectrum shows characteristic peaks in both "
            "X-rays and gamma rays, indicating synchrotron and inverse Compton emission from relativistic "
            "electrons in the jet. PKS 2155-304's extreme variability provides insights into particle acceleration "
            "mechanisms, magnetic field configurations, and the structure of relativistic jets. This object has "
            "been extensively studied across the electromagnetic spectrum, from radio waves to TeV gamma rays, "
            "making it one of the best-characterized blazars and a benchmark for testing theories of jet emission "
            "and high-energy astrophysical processes."
        ),
        "scientific_facts": [
            "PKS 2155-304 underwent the largest blazar flare ever recorded in 2006.",
            "The blazar varies on timescales as short as 3 minutes.",
            "PKS 2155-304 is one of the brightest TeV gamma-ray sources in the southern sky.",
            "The blazar's jet appears to move at 10 times the speed of light.",
            "PKS 2155-304's Doppler boosting factor enhances its luminosity by 20 times.",
            "The blazar can brighten by a factor of 50 in just a few hours.",
            "PKS 2155-304's black hole mass is estimated at 500 million solar masses.",
            "The blazar's jet is pointed within 1 degree of Earth's line of sight.",
            "PKS 2155-304 serves as a calibration source for gamma-ray telescopes.",
            "The blazar's rapid variability implies emission regions smaller than the black hole's event horizon.",
            "PKS 2155-304 shows evidence for particle acceleration to multi-TeV energies.",
            "The blazar has been observed continuously for over 20 years.",
        ],
        "formation_process": (
            "PKS 2155-304 formed when a supermassive black hole developed an extremely relativistic jet "
            "pointed almost directly toward Earth. The extreme alignment and relativistic effects create the "
            "blazar's observed characteristics, including rapid variability and enhanced luminosity through "
            "Doppler boosting."
        ),
        "future_evolution": [
            "PKS 2155-304 will continue its extreme variability and jet activity for millions of years. "
            "The blazar will eventually exhaust its fuel supply and transition to a less active phase, "
            "though the supermassive black hole will remain at the galaxy center. The jet may leave behind "
            "large-scale radio lobes as it evolves."
        ],
        "related_objects": ["Mrk 421", "Mrk 501", "1ES 1101-232", "HBL Blazars"],
        "parent_system": "Distant Universe",
        "child_objects": ["Relativistic Jet", "Emission Regions", "Host Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 3: GAMMA-RAY BURSTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "grb-090423")),
        "name": "GRB 090423",
        "category": "Gamma-Ray Burst",
        "subtype": "Long-Duration GRB, Most Distant Known",
        "tags": ["gamma-ray-burst", "most-distant-grb", "early-universe", "long-grb", "massive-star-death"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 13.0e9, "unit": "ly"},
            "coordinates": {"ra": "09h 55m 33.1s", "dec": "+18° 08' 58\""},
            "galaxy_reference": "Early Universe",
            "location": "Leo constellation",
            "redshift": {"value": 8.2, "unit": "z"},
        },
        "physical": {
            "isotropic_energy": {"value": 1e54, "unit": "ergs"},
            "duration": {"value": 10.3, "unit": "seconds"},
            "peak_energy": {"value": 84, "unit": "keV"},
            "jet_angle": {"value": 5, "unit": "degrees"},
            "beaming_factor": {"value": 500, "unit": "correction"},
            "true_energy": {"value": 5e56, "unit": "ergs"},
            "progenitor_mass": {"value": 100, "unit": "solar_masses"},
            "afterglow_brightness": {"value": 25, "unit": "magnitude"},
        },
        "detailed_description": (
            "GRB 090423 is the most distant gamma-ray burst ever detected, occurring when the universe was "
            "only 630 million years old - less than 5% of its current age. This extraordinary burst was detected "
            "by NASA's Swift satellite on April 23, 2009, and lasted for 10.3 seconds, releasing an isotropic "
            "energy of 10^54 ergs - equivalent to converting the mass of two suns completely into energy. "
            "When corrected for the likely jet collimation, the true energy release may have reached 5×10^56 ergs, "
            "making it one of the most energetic explosions ever recorded. The burst occurred at a redshift of "
            "8.2, meaning its light traveled 13 billion years to reach us, providing a unique probe of the "
            "very early universe. GRB 090423's afterglow was detected in near-infrared light but was too faint "
            "to see in visible light due to the extreme cosmological redshift. This burst confirms that massive "
            "stars were forming and dying within the first few hundred million years after the Big Bang, challenging "
            "our understanding of early star formation. The progenitor was likely a Population III star - one of "
            "the first generation of stars formed from pristine hydrogen and helium, with minimal heavy elements. "
            "GRB 090423 provides crucial insights into the conditions of the early universe, the formation of the "
            "first massive stars, and the reionization epoch. The burst's detection demonstrates that gamma-ray "
            "bursts can serve as powerful beacons for studying the cosmic dark ages and the birth of the first "
            "galaxies."
        ),
        "scientific_facts": [
            "GRB 090423 is the most distant gamma-ray burst known, seen when the universe was only 630 million years old.",
            "The burst released 10^54 ergs of energy isotropically, equivalent to converting 2 solar masses to energy.",
            "GRB 090423's light traveled 13 billion years to reach Earth.",
            "The burst occurred at redshift 8.2, during the epoch of reionization.",
            "GRB 090423 lasted 10.3 seconds, typical for long-duration GRBs.",
            "The burst's afterglow was only detectable in near-infrared light.",
            "GRB 090423 proves massive stars existed in the first 630 million years of cosmic history.",
            "The burst's true energy may have been 5×10^56 ergs when corrected for jet collimation.",
            "GRB 090423's progenitor was likely a Population III star.",
            "The burst provides evidence for rapid star formation in the early universe.",
            "GRB 090423 serves as a beacon for studying the cosmic dark ages.",
            "The burst was detected by the Swift satellite and confirmed with ground-based telescopes.",
        ],
        "formation_process": (
            "GRB 090423 resulted from the core-collapse of a massive Population III star - one of the first "
            "generation of stars formed from pristine gas. The star's collapse created a black hole that launched "
            "relativistic jets, which broke through the stellar surface and produced the gamma-ray burst as they "
            "interacted with the surrounding medium."
        ),
        "future_evolution": (
            "GRB 090423's afterglow has long since faded, but the burst's energy has contributed to the "
            "reionization of the early universe. The remnant black hole continues to exist in the distant "
            "universe, possibly now part of a larger galaxy that formed around it over the past 13 billion years.",
        ),
        "related_objects": ["GRB 080913", "GRB 130606A", "Early Universe GRBs", "Population III Stars"],
        "parent_system": "Early Universe",
        "child_objects": ["Relativistic Jets", "Afterglow", "Black Hole Remnant"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "grb-080319b")),
        "name": "GRB 080319B",
        "category": "Gamma-Ray Burst",
        "subtype": "Long-Duration GRB, Optically Brightest Known",
        "tags": ["gamma-ray-burst", "brightest-grb", "optical-flash", "naked-eye", "well-studied"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 5.6e9, "unit": "ly"},
            "coordinates": {"ra": "14h 18m 28.6s", "dec": "+36° 28' 21\""},
            "galaxy_reference": "Distant Universe",
            "location": "Bootes constellation",
            "redshift": {"value": 0.937, "unit": "z"},
        },
        "physical": {
            "isotropic_energy": {"value": 1.3e54, "unit": "ergs"},
            "duration": {"value": 50, "unit": "seconds"},
            "peak_energy": {"value": 800, "unit": "keV"},
            "optical_peak_magnitude": {"value": 5.3, "unit": "magnitude"},
            "optical_peak_luminosity": {"value": 3e16, "unit": "solar_luminosities"},
            "jet_angle": {"value": 4, "unit": "degrees"},
            "beaming_factor": {"value": 800, "unit": "correction"},
            "progenitor_mass": {"value": 40, "unit": "solar_masses"},
        },
        "detailed_description": (
            "GRB 080319B is the optically brightest gamma-ray burst ever recorded, a spectacular explosion "
            "that became briefly visible to the naked eye despite occurring 5.6 billion light-years away. "
            "Discovered on March 19, 2008, by NASA's Swift satellite, this burst reached a peak apparent "
            "magnitude of 5.3 - bright enough to be seen without optical aid from a dark location and comparable "
            "to the faintest stars visible in urban areas. The burst released an astonishing 1.3×10^54 ergs of "
            "energy isotropically, with a true energy of over 10^56 ergs when corrected for jet collimation. "
            "GRB 080319B's optical flash was extraordinary, reaching a luminosity 30 million times greater than "
            "the Sun and outshining its host galaxy by a factor of 10,000. The burst was observed by an unprecedented "
            "number of telescopes worldwide, providing the most comprehensive multi-wavelength coverage of any "
            "gamma-ray burst to date. The optical emission showed a smooth, single-peaked light curve that mirrored "
            "the gamma-ray emission, suggesting both were produced by the same population of electrons in the "
            "relativistic jet. The burst occurred in a star-forming galaxy at redshift 0.937, when the universe "
            "was about half its current age. GRB 080319B's extreme brightness and excellent observations have "
            "made it a cornerstone for understanding gamma-ray burst physics, jet composition, and the mechanisms "
            "that produce both gamma rays and optical light. This event demonstrated that gamma-ray bursts can "
            "occasionally become visible to the naked eye and provided unprecedented insights into the most "
            "energetic explosions in the universe."
        ),
        "scientific_facts": [
            "GRB 080319B is the only gamma-ray burst visible to the naked eye.",
            "The burst reached magnitude 5.3, comparable to the faintest naked-eye stars.",
            "GRB 080319B's optical luminosity was 30 million times that of the Sun.",
            "The burst released 1.3×10^54 ergs of energy isotropically.",
            "GRB 080319B was observed by more telescopes than any previous GRB.",
            "The burst occurred 5.6 billion light-years from Earth.",
            "GRB 080319B's optical and gamma-ray emissions were perfectly synchronized.",
            "The burst's true energy exceeded 10^56 ergs when corrected for jet collimation.",
            "GRB 080319B outshone its host galaxy by 10,000 times.",
            "The burst lasted 50 seconds in gamma rays.",
            "GRB 080319B provided the most comprehensive multi-wavelength data of any GRB.",
            "The burst's progenitor was likely a 40-solar-mass star.",
        ],
        "formation_process": (
            "GRB 080319B resulted from the core-collapse of a massive star (approximately 40 solar masses) "
            "that had lost its outer hydrogen envelope. The collapse created a black hole that launched "
            "relativistic jets, which broke through the stellar surface and produced the gamma-ray burst as "
            "they interacted with the surrounding medium."
        ),
        "future_evolution": (
            "GRB 080319B's afterglow has faded over the years, but the burst's energy has enriched the "
            "intergalactic medium with heavy elements. The remnant black hole continues to exist in its host "
            "galaxy, potentially affecting future star formation through its gravitational influence."
        ),
        "related_objects": ["GRB 990123", "GRB 060218", "Bright GRBs", "Long GRBs"],
        "parent_system": "Distant Universe",
        "child_objects": ["Relativistic Jets", "Optical Flash", "Afterglow"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "grb-170817a")),
        "name": "GRB 170817A",
        "category": "Gamma-Ray Burst",
        "subtype": "Short-Duration GRB, First Gravitational Wave Association",
        "tags": ["gamma-ray-burst", "short-grb", "gravitational-waves", "neutron-star-merger", "kilonova", "multi-messenger"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 130e6, "unit": "ly"},
            "coordinates": {"ra": "13h 09m 48.1s", "dec": "-23° 22' 53\""},
            "galaxy_reference": "NGC 4993",
            "location": "Hydra constellation",
            "redshift": {"value": 0.0097, "unit": "z"},
        },
        "physical": {
            "isotropic_energy": {"value": 1.7e49, "unit": "ergs"},
            "duration": {"value": 2, "unit": "seconds"},
            "peak_energy": {"value": 185, "unit": "keV"},
            "jet_angle": {"value": 15, "unit": "degrees"},
            "viewing_angle": {"value": 20, "unit": "degrees"},
            "kilonova_energy": {"value": 1e51, "unit": "ergs"},
            "heavy_element_mass": {"value": 0.05, "unit": "solar_masses"},
            "gravitational_wave_energy": {"value": 3e53, "unit": "ergs"},
        },
        "detailed_description": (
            "GRB 170817A is a landmark event in astronomy - the first gamma-ray burst ever detected in "
            "association with gravitational waves, marking the beginning of multi-messenger astronomy. This "
            "short-duration gamma-ray burst occurred on August 17, 2017, and was detected by NASA's Fermi "
            "satellite just 1.7 seconds after gravitational waves from the same event were detected by the "
            "LIGO and Virgo observatories. The burst originated from the merger of two neutron stars in the "
            "galaxy NGC 4993, located 130 million light-years away - making it the closest gamma-ray burst ever "
            "detected. GRB 170817A was unusually weak for a short GRB, lasting only 2 seconds and releasing "
            "only 10^49 ergs of energy, likely because we were viewing the jet from an off-axis angle of 20 "
            "degrees. The merger produced not only the gamma-ray burst and gravitational waves but also a "
            "kilonova - an optical/infrared transient powered by the radioactive decay of heavy elements "
            "formed in the neutron-rich ejecta. This kilonova confirmed that neutron star mergers are major "
            "sites for the production of heavy elements like gold, platinum, and uranium, solving a decades-"
            "old mystery about the origin of the heaviest elements. The event was observed across the entire "
            "electromagnetic spectrum, from radio waves to gamma rays, and provided the first direct evidence "
            "that neutron star mergers produce short gamma-ray bursts. GRB 170817A has revolutionized our "
            "understanding of heavy element nucleosynthesis, confirmed theories about gamma-ray burst origins, "
            "and opened a new era of astronomy where gravitational waves and electromagnetic radiation can be "
            "studied together."
        ),
        "scientific_facts": [
            "GRB 170817A is the first GRB detected with gravitational waves.",
            "The burst resulted from the merger of two neutron stars.",
            "GRB 170817A is the closest gamma-ray burst ever detected at 130 million light-years.",
            "The merger produced 0.05 solar masses of heavy elements including gold and platinum.",
            "GRB 170817A confirmed that neutron star mergers create short GRBs.",
            "The burst was observed across the entire electromagnetic spectrum.",
            "GRB 170817A's gravitational waves carried 3×10^53 ergs of energy.",
            "The merger occurred in the galaxy NGC 4993.",
            "GRB 170817A was viewed off-axis, explaining its unusual weakness.",
            "The kilonova from the merger was visible for weeks after the burst.",
            "GRB 170817A solved the mystery of where heavy elements are formed.",
            "The event marked the beginning of multi-messenger astronomy.",
        ],
        "formation_process": (
            "GRB 170817A formed when two neutron stars in a binary system spiraled together and merged. "
            "The merger released gravitational waves, created a black hole or hypermassive neutron star, and "
            "launched relativistic jets that produced the gamma-ray burst. The neutron-rich ejecta underwent "
            "rapid neutron capture, creating heavy elements that powered the kilonova."
        ),
        "future_evolution": (
            "The merger remnant (likely a black hole) continues to exist in NGC 4993. The heavy elements "
            "produced in the kilonova are now dispersing into the galaxy, enriching future generations of "
            "stars with precious metals. The event has opened a new field of multi-messenger astronomy that "
            "will continue to grow with more gravitational wave detections."
        ),
        "related_objects": ["GW170817", "Kilonova AT 2017gfo", "Short GRBs", "Neutron Star Mergers"],
        "parent_system": "NGC 4993",
        "child_objects": ["Gravitational Waves", "Kilonova", "Heavy Elements"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 4: EXTREMAE PULSARS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "psr-j1748-2446ad")),
        "name": "PSR J1748-2446ad",
        "category": "Pulsar",
        "subtype": "Millisecond Pulsar, Fastest Spinning Known",
        "tags": ["millisecond-pulsar", "fastest-spinner", "globular-cluster", "recycled-pulsar", "extreme-physics"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 28000, "unit": "ly"},
            "coordinates": {"ra": "17h 48m 39.6s", "dec": "-24° 46' 59\""},
            "galaxy_reference": "Milky Way",
            "location": "Terzan 5 globular cluster",
        },
        "physical": {
            "mass": {"value": 1.67, "unit": "solar_masses"},
            "radius": {"value": 10, "unit": "km"},
            "rotation_period": {"value": 1.396, "unit": "milliseconds"},
            "rotation_frequency": {"value": 716, "unit": "Hz"},
            "surface_velocity": {"value": 0.2, "unit": "c", "note": "At equator"},
            "magnetic_field": {"value": 1e8, "unit": "gauss"},
            "spin-down_power": {"value": 5e38, "unit": "erg/s"},
            "age": {"value": 10e9, "unit": "years"},
        },
        "detailed_description": (
            "PSR J1748-2446ad is the fastest spinning neutron star known, an extreme millisecond pulsar that "
            "rotates an astonishing 716 times per second - so fast that its equator moves at 20% the speed of "
            "light. Located 28,000 light-years away in the dense Terzan 5 globular cluster, this remarkable "
            "pulsar pushes the limits of matter and physics under the most extreme conditions imaginable. "
            "The neutron star completes more than one rotation every millisecond, with a rotation period of "
            "just 1.396 milliseconds, faster than any other known object in the universe. At this rotation rate, "
            "the centrifugal forces at the equator are enormous, requiring the neutron star to have an unusually "
            "high mass of 1.67 solar masses to avoid being torn apart. PSR J1748-2446ad is a 'recycled' pulsar, "
            "meaning it was spun up through accretion of matter from a binary companion, which also explains its "
            "relatively weak magnetic field of 10^8 gauss - much weaker than typical young pulsars but stronger "
            "than most millisecond pulsars. The pulsar's spin-down power of 5×10^38 erg/s is comparable to the "
            "total luminosity of the Sun, all generated by the gradual loss of rotational energy. This object "
            "provides a unique laboratory for studying the physics of ultra-dense matter, the behavior of matter "
            "at relativistic rotation speeds, and the limits of neutron star stability. The pulsar's existence in "
            "a globular cluster also provides insights into stellar dynamics in dense environments and the "
            "formation of exotic binary systems. PSR J1748-2446ad represents the extreme upper limit of neutron "
            "star rotation rates and serves as a benchmark for testing theories of matter at nuclear densities."
        ),
        "scientific_facts": [
            "PSR J1748-2446ad rotates 716 times per second, the fastest known rotation rate.",
            "The pulsar's equator moves at 20% the speed of light.",
            "The neutron star completes one rotation every 1.396 milliseconds.",
            "PSR J1748-2446ad requires 1.67 solar masses to avoid being torn apart by centrifugal force.",
            "The pulsar's spin-down power equals the Sun's total luminosity.",
            "PSR J1748-2446ad is located in the Terzan 5 globular cluster.",
            "The pulsar is a recycled pulsar, spun up by accretion from a companion.",
            "PSR J1748-2446ad's magnetic field is 10^8 gauss, weaker than typical pulsars.",
            "The pulsar's surface gravity is 100 billion times stronger than Earth's.",
            "PSR J1748-2446ad pushes the limits of neutron star stability.",
            "The pulsar's rotation rate is near the theoretical maximum for neutron stars.",
            "PSR J1748-2446ad provides tests of general relativity in strong gravitational fields.",
        ],
        "formation_process": [
            "PSR J1748-2446ad formed as a normal pulsar from a supernova explosion, then was later "
            "'recycled' through accretion from a binary companion. The transfer of angular momentum from the "
            "accreting material spun the pulsar up to its extreme rotation rate, while the accretion also "
            "reduced its magnetic field strength."
        ],
        "future_evolution": [
            "PSR J1748-2446ad will gradually slow down over billions of years due to magnetic braking, "
            "eventually becoming a normal millisecond pulsar with a slower rotation rate. The pulsar will "
            "continue to exist in the globular cluster environment, potentially interacting with other stars "
            "through gravitational encounters."
        ],
        "related_objects": ["PSR J1903+0327", "PSR J1311-3430", "Millisecond Pulsars", "Globular Cluster Pulsars"],
        "parent_system": "Terzan 5 Globular Cluster",
        "child_objects": ["Relativistic Equator", "Magnetosphere"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 5: EXTREMAE X-RAY SOURCES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "ss-433")),
        "name": "SS 433",
        "category": "X-ray Source",
        "subtype": "Microquasar with Precessing Jets",
        "tags": ["microquasar", "precessing-jets", "binary-system", "relativistic-jets", "heavy-element-production"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 18000, "unit": "ly"},
            "coordinates": {"ra": "19h 11m 49.6s", "dec": "+04° 58' 32\""},
            "galaxy_reference": "Milky Way",
            "location": "Aquila constellation, inside supernova remnant W50",
        },
        "physical": {
            "black_hole_mass": {"value": 10, "unit": "solar_masses"},
            "companion_mass": {"value": 15, "unit": "solar_masses"},
            "orbital_period": {"value": 13.1, "unit": "days"},
            "jet_velocity": {"value": 0.26, "unit": "c"},
            "precession_period": {"value": 162.5, "unit": "days"},
            "jet_opening_angle": {"value": 20, "unit": "degrees"},
            "accretion_rate": {"value": 1e-3, "unit": "solar_masses/year"},
            "x-ray_luminosity": {"value": 1e38, "unit": "erg/s"},
        },
        "detailed_description": (
            "SS 433 is one of the most exotic and bizarre objects in our galaxy, a microquasar that shoots "
            "out jets of matter at 26% the speed of light while precessing like a spinning top. Located "
            "18,000 light-years away in Aquila, this remarkable binary system consists of a 10-solar-mass "
            "black hole orbiting a 15-solar-mass companion star every 13.1 days. The black hole is accreting "
            "matter from its companion at an extraordinary rate of 10^-3 solar masses per year, creating an "
            "accretion disk so bright that SS 433 is visible in binoculars despite being embedded in the "
            "supernova remnant W50. The most striking feature is the pair of relativistic jets that shoot "
            "out from the black hole's poles at 26% the speed of light. These jets precess with a period of "
            "162.5 days, sweeping out a cone in space and creating a spectacular corkscrew pattern in the "
            "surrounding supernova remnant. The jets contain heavy elements including iron, nickel, and zinc, "
            "providing direct evidence for nucleosynthesis in the accretion disk. SS 433's spectrum shows "
            "extraordinary Doppler shifts as the jets alternately move toward and away from Earth, with "
            "redshifts and blueshifts corresponding to the jet velocity. This object serves as a scaled-down "
            "version of quasars, allowing detailed study of jet physics, accretion processes, and the "
            "production of heavy elements under extreme conditions. SS 433 has been observed for decades and "
            "continues to surprise astronomers with its complex behavior and the ongoing interaction between "
            "its jets and the surrounding supernova remnant."
        ),
        "scientific_facts": [
            "SS 433 shoots jets at 26% the speed of light, the fastest known in our galaxy.",
            "The jets precess with a period of 162.5 days like a spinning top.",
            "SS 433 is visible in binoculars despite being 18,000 light-years away.",
            "The jets contain heavy elements including iron and nickel.",
            "SS 433 accretes matter at 10^-3 solar masses per year.",
            "The system is embedded in the supernova remnant W50.",
            "SS 433's spectrum shows extreme Doppler shifts from the jets.",
            "The jets have created a corkscrew pattern in the surrounding nebula.",
            "SS 433 is a microquasar, a scaled-down version of quasars.",
            "The black hole mass is estimated at 10 solar masses.",
            "SS 433 has been observed continuously for over 40 years.",
            "The jets have inflated bubble-like structures in the supernova remnant.",
        ],
        "formation_process": [
            "SS 433 formed when a massive star in a binary system went supernova, leaving behind a black "
            "hole. The black hole began accreting matter from its companion star, forming an accretion disk "
            "and launching relativistic jets. The system is embedded in the supernova remnant from the "
            "black hole's formation."
        ],
        "future_evolution": [
            "SS 433 will continue its extreme jet activity for millions of years, eventually exhausting "
            "the companion star and becoming an isolated black hole. The jets will continue to shape the "
            "surrounding supernova remnant, creating ever more complex structures as the system evolves."
        ],
        "related_objects": ["Cygnus X-1", "Cygnus X-3", "Microquasars", "X-ray Binaries"],
        "parent_system": "Supernova Remnant W50",
        "child_objects": ["Precessing Jets", "Accretion Disk", "Heavy Element Jets"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 6: EXTREMAE INTERSTELLAR OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "oumuamua")),
        "name": "'Oumuamua (1I/2017 U1)",
        "category": "Interstellar Object",
        "subtype": "Interstellar Asteroid/Comet",
        "tags": ["interstellar", "first-detected", "elongated-shape", "non-gravitational-acceleration", "mystery-object"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": "variable", "unit": "AU", "note": "Currently leaving solar system"},
            "coordinates": {"ra": "23h 22m 07.9s", "dec": "+15° 52' 26\"", "note": "At discovery"},
            "galaxy_reference": "Interstellar Space",
            "location": "Currently in Pegasus constellation, leaving solar system",
            "velocity": {"value": 26, "unit": "km/s", "note": "relative to Sun"},
        },
        "physical": {
            "dimensions": {"value": "200m × 20m × 20m", "unit": "meters", "note": "Extreme elongation"},
            "mass": {"value": 1e13, "unit": "kg", "note": "Estimated"},
            "density": {"value": 0.1-1.0, "unit": "g/cm³", "note": "Very low"},
            "rotation_period": {"value": 8.67, "unit": "hours"},
            "albedo": {"value": 0.04, "unit": "reflectivity"},
            "color": {"value": "red", "note": "Similar to outer solar system objects"},
            "non-gravitational_acceleration": {"value": 5e-4, "unit": "m/s²"},
        },
        "detailed_description": (
            "'Oumuamua is the first interstellar object ever detected passing through our solar system, a "
            "mysterious visitor that has challenged our understanding of planetary formation and interstellar "
            "objects. Discovered on October 19, 2017, by the Pan-STARRS telescope in Hawaii, this object was "
            "named 'Oumuamua (Hawaiian for 'scout' or 'messenger from afar arriving first') and designated "
            "1I/2017 U1, marking the beginning of a new class of astronomical objects. 'Oumuamua's most "
            "puzzling feature is its extreme shape - estimated to be 200 meters long but only 20 meters wide, "
            "making it the most elongated natural object ever observed. The object showed a small but definite "
            "non-gravitational acceleration, meaning something other than gravity was affecting its motion - "
            "possibly outgassing, solar radiation pressure, or something more exotic. Despite extensive observations, "
            "no coma or tail was detected, leading to debate about whether it was an asteroid, comet, or something "
            "entirely new. 'Oumuamua's reddish color and low density suggest it may be porous or hollow, and its "
            "trajectory indicates it came from the direction of the constellation Lyra. The object passed within "
            "0.16 AU of Earth and is now leaving our solar system at 26 km/s, never to return. 'Oumuamua's brief "
            "visit has raised profound questions about the frequency of interstellar objects, their composition, "
            "and whether they might occasionally be artificial in origin. This historic discovery has opened a "
            "new field of interstellar object studies and demonstrated that such objects, while rare, can be "
            "detected with current astronomical instruments."
        ),
        "scientific_facts": [
            "'Oumuamua is the first confirmed interstellar object detected in our solar system.",
            "The object is extremely elongated, with a 10:1 length-to-width ratio.",
            "'Oumuamua showed non-gravitational acceleration that defied conventional explanations.",
            "The object passed within 0.16 AU (24 million km) of Earth.",
            "'Oumuamua has a very low density, suggesting it might be porous or hollow.",
            "The object's reddish color is similar to outer solar system objects.",
            "'Oumuamua showed no detectable coma or tail despite its acceleration.",
            "The object is now leaving the solar system at 26 km/s.",
            "'Oumuamua's origin direction points toward the constellation Lyra.",
            "The object's true nature remains debated - asteroid, comet, or something else.",
            "'Oumuamua was discovered by the Pan-STARRS telescope in Hawaii.",
            "The object's visit lasted only a few months from discovery to becoming too faint to observe.",
        ],
        "formation_process": [
            "'Oumuamua formed around another star and was ejected through gravitational interactions, "
            "possibly during planet formation or through encounters with other stars. It has been traveling "
            "through interstellar space for millions or billions of years before its brief passage through "
            "our solar system."
        ],
        "future_evolution": [
            "'Oumuamua will continue traveling through interstellar space for billions of years, possibly "
            "passing through other star systems. It will remain an enigmatic object that provided humanity's "
            "first glimpse of material from beyond our solar system."
        ],
        "related_objects": ["2I/Borisov", "Interstellar Objects", "Asteroids", "Comets"],
        "parent_system": "Interstellar Space",
        "child_objects": ["None"],
        "nasa_reference": "https://science.nasa.gov/solar-system/asteroids/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "borisov-comet")),
        "name": "2I/Borisov",
        "category": "Interstellar Object",
        "subtype": "Interstellar Comet",
        "tags": ["interstellar", "comet", "second-detected", "coma", "tail", "typical-comet"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": "variable", "unit": "AU", "note": "Currently leaving solar system"},
            "coordinates": {"ra": "05h 25m 07.6s", "dec": "+23° 23' 48\"", "note": "At discovery"},
            "galaxy_reference": "Interstellar Space",
            "location": "Currently in Lynx constellation, leaving solar system",
            "velocity": {"value": 32, "unit": "km/s", "note": "relative to Sun"},
        },
        "physical": {
            "nucleus_diameter": {"value": 0.5, "unit": "km"},
            "coma_diameter": {"value": 100000, "unit": "km"},
            "tail_length": {"value": 160000, "unit": "km"},
            "mass": {"value": 1e13, "unit": "kg"},
            "density": {"value": 0.5, "unit": "g/cm³"},
            "rotation_period": {"value": 10, "unit": "hours"},
            "albedo": {"value": 0.04, "unit": "reflectivity"},
            "gas_production_rate": {"value": 1e26, "unit": "molecules/s"},
        },
        "detailed_description": (
            "2I/Borisov is the second interstellar object ever detected and the first confirmed interstellar "
            "comet, providing a remarkable contrast to the mysterious 'Oumuamua. Discovered on August 30, 2019, "
            "by amateur astronomer Gennady Borisov in Crimea, this object exhibited all the characteristics of "
            "a typical comet from our solar system, including a bright coma and tail composed of dust and gas. "
            "2I/Borisov's nucleus measured approximately 500 meters in diameter, much smaller than 'Oumuamua's "
            "estimated size, but it displayed a spectacular coma 100,000 kilometers across and a tail extending "
            "160,000 kilometers. The comet's spectrum showed the presence of CN (cyanogen) and diatomic carbon, "
            "molecules common in solar system comets, suggesting that comet formation processes may be similar "
            "around other stars. Unlike 'Oumuamua, 2I/Borisov showed no non-gravitational acceleration, following "
            "a purely gravitational trajectory through our solar system. The comet passed its perihelion at 2.0 AU "
            "from the Sun and came within 0.3 AU of Earth, making it accessible for detailed observations. "
            "2I/Borisov's composition appears to be similar to Oort cloud comets, providing the first direct evidence "
            "that the building blocks of planetary systems may be similar across different stellar environments. "
            "This historic discovery confirmed that interstellar objects are not all as strange as 'Oumuamua and "
            "that at least some share characteristics with familiar solar system objects. 2I/Borisov has provided "
            "crucial insights into comet formation in other star systems and the chemical evolution of planetary "
            "systems."
        ),
        "scientific_facts": [
            "2I/Borisov is the first confirmed interstellar comet.",
            "The comet showed typical comet features including a coma and tail.",
            "2I/Borisov's nucleus is 500 meters in diameter.",
            "The comet contains cyanogen and diatomic carbon, like solar system comets.",
            "2I/Borisov showed no non-gravitational acceleration, unlike 'Oumuamua.",
            "The comet passed within 0.3 AU (45 million km) of Earth.",
            "2I/Borisov's composition is similar to Oort cloud comets.",
            "The comet was discovered by amateur astronomer Gennady Borisov.",
            "2I/Borisov passed perihelion at 2.0 AU from the Sun.",
            "The comet's coma extended 100,000 km from the nucleus.",
            "2I/Borisov is leaving the solar system at 32 km/s.",
            "The comet provides evidence that comet formation is similar around other stars.",
        ],
        "formation_process": [
            "2I/Borisov formed around another star as a typical comet and was ejected through gravitational "
            "interactions, possibly during the early evolution of its home planetary system. It has been "
            "traveling through interstellar space for millions of years before its passage through our solar "
            "system."
        ],
        "future_evolution": [
            "2I/Borisov will continue traveling through interstellar space for billions of years, possibly "
            "passing through other star systems. The comet will gradually lose volatile materials through "
            "outgassing, eventually becoming dormant or disintegrating completely."
        ],
        "related_objects": ["'Oumuamua", "Hale-Bopp", "Halley's Comet", "Interstellar Objects"],
        "parent_system": "Interstellar Space",
        "child_objects": ["Coma", "Tail", "Dust Jets"],
        "nasa_reference": "https://science.nasa.gov/solar-system/comets/",
    },

    # -------------------------------------------------------------------------
    # SECTION 7: EXTREMAE GALAXY CLUSTERS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "el-gordo")),
        "name": "El Gordo (ACT-CL J0102-4915)",
        "category": "Galaxy Cluster",
        "subtype": "Massive Merging Cluster",
        "tags": ["galaxy-cluster", "massive-cluster", "merging-clusters", "dark-matter", "hot-gas", "distant-cluster"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 7.0e9, "unit": "ly"},
            "coordinates": {"ra": "01h 02m 53.0s", "dec": "-49° 15' 00\""},
            "galaxy_reference": "Distant Universe",
            "location": "Phoenix constellation",
            "redshift": {"value": 0.87, "unit": "z"},
        },
        "physical": {
            "total_mass": {"value": 3e15, "unit": "solar_masses"},
            "dark_matter_mass": {"value": 2.4e15, "unit": "solar_masses"},
            "hot_gas_mass": {"value": 6e14, "unit": "solar_masses"},
            "galaxy_mass": {"value": 1e14, "unit": "solar_masses"},
            "gas_temperature": {"value": 200, "unit": "million_K"},
            "x-ray_luminosity": {"value": 2e45, "unit": "erg/s"},
            "merger_velocity": {"value": 3000, "unit": "km/s"},
            "cluster_radius": {"value": 2.0, "unit": "Mpc"},
        },
        "detailed_description": (
            "El Gordo (Spanish for 'the fat one') is one of the most massive and extreme galaxy clusters known, "
            "a colossal structure that challenges our understanding of how quickly such massive objects could form "
            "in the early universe. Located 7 billion light-years away in Phoenix, this merging cluster contains a "
            "total mass of 3×10^15 solar masses - equivalent to three quadrillion suns, making it the most massive "
            "cluster known at its epoch (redshift 0.87). El Gordo is actually two clusters in the process of merging, "
            "with the collision occurring at an astonishing velocity of 3,000 km/s. The cluster's hot intracluster "
            "gas reaches temperatures of 200 million degrees Celsius, making it one of the hottest known clusters "
            "and producing intense X-ray emission with a luminosity of 2×10^45 erg/s. The cluster is dominated by "
            "dark matter, which comprises 80% of its total mass, with the remaining 20% split between hot gas and "
            "galaxies. El Gordo shows evidence for a 'bullet' of dark matter that has passed through the cluster "
            "during the merger, similar to the famous Bullet Cluster but on a much larger scale. The cluster's "
            "extreme mass at this early epoch challenges models of structure formation in the universe, suggesting "
            "that the most massive clusters formed earlier than expected. El Gordo serves as a crucial laboratory "
            "for studying dark matter properties, cluster physics, and the growth of the largest structures in "
            "the universe. The cluster's gravitational lensing effect is so strong that it magnifies background "
            "galaxies by factors of up to 50, allowing us to study galaxies from the very early universe."
        ),
        "scientific_facts": [
            "El Gordo is the most massive galaxy cluster known from the first 5 billion years of cosmic history.",
            "The cluster contains 3 quadrillion solar masses of material.",
            "El Gordo is actually two clusters merging at 3,000 km/s.",
            "The cluster's hot gas reaches 200 million degrees Celsius.",
            "El Gordo is 80% dark matter by mass.",
            "The cluster's gravitational lensing magnifies background galaxies by up to 50 times.",
            "El Gordo challenges models of how quickly massive structures can form.",
            "The cluster shows evidence for a dark matter 'bullet' similar to the Bullet Cluster.",
            "El Gordo's X-ray luminosity is 2×10^45 erg/s.",
            "The cluster is seen as it was 7 billion years ago.",
            "El Gordo contains hundreds of galaxies moving at thousands of km/s.",
            "The cluster provides a laboratory for studying dark matter and structure formation.",
        ],
        "formation_process": [
            "El Gordo formed through the merger of two massive galaxy clusters that had been growing through "
            "the accumulation of smaller groups and galaxies over billions of years. The extreme mass of the "
            "cluster suggests it formed in an unusually dense region of the early universe."
        ],
        "future_evolution": [
            "El Gordo will continue to merge and relax over the next few billion years, eventually becoming "
            "a single, relaxed massive cluster. The hot gas will gradually cool, and the cluster will continue "
            "to accrete more galaxies and groups from its surroundings."
        ],
        "related_objects": ["Bullet Cluster", "Pandora's Cluster", "Coma Cluster", "Massive Galaxy Clusters"],
        "parent_system": "Distant Universe",
        "child_objects": ["Dark Matter Halos", "Hot Intracluster Gas", "Galaxy Populations"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "bullet-cluster")),
        "name": "Bullet Cluster (1E 0657-56)",
        "category": "Galaxy Cluster",
        "subtype": "Merging Cluster with Dark Matter Separation",
        "tags": ["galaxy-cluster", "merging-clusters", "dark-matter-proof", "bullet-cluster", "gravitational-lensing"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 3.7e9, "unit": "ly"},
            "coordinates": {"ra": "06h 58m 37.9s", "dec": "-55° 57' 00\""},
            "galaxy_reference": "Distant Universe",
            "location": "Carina constellation",
            "redshift": {"value": 0.296, "unit": "z"},
        },
        "physical": {
            "total_mass": {"value": 1e15, "unit": "solar_masses"},
            "bullet_mass": {"value": 1e14, "unit": "solar_masses"},
            "main_cluster_mass": {"value": 9e14, "unit": "solar_masses"},
            "gas_temperature": {"value": 100, "unit": "million_K"},
            "collision_velocity": {"value": 4500, "unit": "km/s"},
            "bullet_velocity": {"value": 3000, "unit": "km/s"},
            "x-ray_luminosity": {"value": 1e45, "unit": "erg/s"},
            "separation": {"value": 0.7, "unit": "Mpc"},
        },
        "detailed_description": (
            "The Bullet Cluster is one of the most important astronomical discoveries of the 21st century, "
            "providing the first direct evidence for the existence of dark matter through the spectacular "
            "separation of dark matter from normal matter during a galaxy cluster collision. Located 3.7 billion "
            "light-years away in Carina, this system consists of two galaxy clusters that have collided at an "
            "astonishing velocity of 4,500 km/s - the most energetic event known since the Big Bang. During the "
            "collision, the hot intracluster gas from both clusters collided and heated to 100 million degrees, "
            "slowing down and concentrating near the center of the merged system. However, the galaxies and "
            "their associated dark matter halos passed through each other largely unaffected, continuing on "
            "their original trajectories. Gravitational lensing observations revealed that most of the mass "
            "is concentrated where the galaxies are, not where the hot gas is, providing direct proof that dark "
            "matter exists and behaves differently from normal matter. The 'bullet' is a smaller cluster that has "
            "passed through the larger cluster, creating a bow shock in the hot gas and leaving a clear separation "
            "between the dark matter (traced by gravitational lensing) and the normal matter (traced by X-rays). "
            "This discovery was crucial in confirming the existence of dark matter and ruling out alternative "
            "theories that sought to explain gravitational effects without dark matter. The Bullet Cluster serves "
            "as a fundamental laboratory for studying dark matter properties, cluster physics, and the behavior "
            "of matter under extreme conditions."
        ),
        "scientific_facts": [
            "The Bullet Cluster provides the first direct evidence for dark matter's existence.",
            "The cluster collision occurred at 4,500 km/s, the most energetic event since the Big Bang.",
            "Dark matter and normal matter are clearly separated in this system.",
            "The hot gas slowed down during collision while dark matter passed through.",
            "The Bullet Cluster's mass is 10^15 solar masses.",
            "Gravitational lensing reveals where the dark matter is located.",
            "The cluster collision created a bow shock visible in X-rays.",
            "The Bullet Cluster helped rule out alternative theories to dark matter.",
            "The hot gas reaches 100 million degrees Celsius.",
            "The 'bullet' is a smaller cluster that passed through the larger one.",
            "The cluster provides crucial constraints on dark matter properties.",
            "The Bullet Cluster is one of the most important astronomical discoveries of the 21st century.",
        ],
        "formation_process": [
            "The Bullet Cluster formed when two galaxy clusters collided head-on at extremely high velocity. "
            "The hot gas from both clusters interacted and slowed down, while the galaxies and dark matter "
            "passed through largely unaffected, creating the observed separation between dark and normal matter."
        ],
        "future_evolution": [
            "The Bullet Cluster will continue to evolve as the two clusters merge and settle into a single "
            "relaxed cluster. The hot gas will gradually cool over billions of years, and the dark matter halos "
            "will merge into a single, larger halo."
        ],
        "related_objects": ["El Gordo", "Pandora's Cluster", "MACS J0025.4-1222", "Merging Clusters"],
        "parent_system": "Distant Universe",
        "child_objects": ["Dark Matter Halos", "Hot Gas Shock", "Galaxy Populations"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    # -------------------------------------------------------------------------
    # SECTION 8: EXTREMAE COSMIC STRUCTURES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "great-attractor")),
        "name": "Great Attractor",
        "category": "Cosmic Structure",
        "subtype": "Gravitational Anomaly",
        "tags": ["great-attractor", "gravitational-anomaly", "galaxy-flow", "mass-concentration", "dhidden-behind-milky-way"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 250e6, "unit": "ly"},
            "coordinates": {"ra": "14h 20m", "dec": "-45° 00'"},
            "galaxy_reference": "Local Supercluster",
            "location": "Behind Zone of Avoidance",
            "size": {"value": 100, "unit": "Mpc"},
        },
        "physical": {
            "total_mass": {"value": 1e16, "unit": "solar_masses"},
            "galaxy_velocity": {"value": 600, "unit": "km/s"},
            "mass_concentration": {"value": 5, "unit": "times_average"},
            "galaxy_density": {"value": 2, "unit": "times_average"},
            "dark_matter_fraction": {"value": 0.9, "unit": "fraction"},
            "peculiar_velocity": {"value": 400, "unit": "km/s"},
            "cluster_count": {"value": 100, "unit": "galaxy_clusters"},
            "x-ray_luminosity": {"value": 1e44, "unit": "erg/s"},
        },
        "detailed_description": (
            "The Great Attractor is one of the most massive and mysterious structures in the nearby universe, "
            "a gravitational anomaly that exerts a powerful influence on the motion of galaxies across a "
            "region spanning hundreds of millions of light-years. Located approximately 250 million light-years "
            "away in the direction of the constellations Norma and Centaurus, the Great Attractor lies behind "
            "the Zone of Avoidance - the region of the sky obscured by the dust and gas of our own Milky Way "
            "galaxy, making direct observation extremely difficult. Despite being hidden from view, the Great "
            "Attractor's presence is revealed through its gravitational effects: galaxies throughout our local "
            "region, including the Milky Way, are being pulled toward it at velocities of up to 600 km/s. The "
            "structure contains an estimated 10^16 solar masses of material - equivalent to 10 quadrillion suns - "
            "and has a galaxy density several times higher than the cosmic average. The Great Attractor appears "
            "to be a concentration of galaxy clusters, including the massive Norma Cluster, embedded in a vast "
            "dark matter halo. Recent observations using X-ray and infrared telescopes that can penetrate the "
            "Zone of Avoidance have revealed that the Great Attractor itself may be being pulled toward an even "
            "more massive structure called the Shapley Supercluster. This complex gravitational interaction is "
            "reshaping our understanding of large-scale structure formation and the distribution of mass in the "
            "universe. The Great Attractor serves as a crucial laboratory for studying dark matter, cosmic flows, "
            "and the hierarchical nature of structure formation in the cosmos."
        ),
        "scientific_facts": [
            "The Great Attractor contains 10 quadrillion solar masses of material.",
            "It pulls galaxies toward it at velocities up to 600 km/s.",
            "The Great Attractor lies behind the Milky Way's Zone of Avoidance.",
            "The structure spans 100 megaparsecs (326 million light-years).",
            "The Great Attractor is 90% dark matter by mass.",
            "It contains about 100 galaxy clusters.",
            "The Great Attractor itself is being pulled toward the Shapley Supercluster.",
            "The structure's gravity affects the motion of the Milky Way and Andromeda.",
            "The Great Attractor has a galaxy density 2-5 times the cosmic average.",
            "X-ray observations can penetrate the Zone of Avoidance to study the Great Attractor.",
            "The structure represents a major concentration in the cosmic web.",
            "The Great Attractor challenges models of large-scale structure formation.",
        ],
        "formation_process": [
            "The Great Attractor formed through the hierarchical growth of structure in the universe, with "
            "smaller groups and clusters merging over billions of years to create the massive concentration "
            "we observe today. It represents a peak in the cosmic matter distribution that continues to grow "
            "by accreting surrounding material."
        ],
        "future_evolution": [
            "The Great Attractor will continue to grow by accreting nearby galaxies and clusters, eventually "
            "merging with other large structures to form even larger concentrations. It may eventually become "
            "part of a supercluster complex that includes the Shapley Supercluster."
        ],
        "related_objects": ["Shapley Supercluster", "Laniakea Supercluster", "Norma Cluster", "Cosmic Web"],
        "parent_system": "Local Supercluster",
        "child_objects": ["Galaxy Clusters", "Dark Matter Halo", "Galaxy Filaments"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "void-bootes")),
        "name": "Bootes Void",
        "category": "Cosmic Structure",
        "subtype": "Cosmic Void",
        "tags": ["cosmic-void", "empty-space", "large-scale-structure", "supervoid", "galaxy-desert"],
        "difficulty_level": "intermediate",
        "spatial": {
            "distance_from_earth": {"value": 700e6, "unit": "ly"},
            "coordinates": {"ra": "14h 50m", "dec": "+46° 00'"},
            "galaxy_reference": "Distant Universe",
            "location": "Bootes constellation",
            "diameter": {"value": 330, "unit": "million_ly"},
        },
        "physical": {
            "volume": {"value": 0.004, "unit": "cubic_Gpc"},
            "galaxy_count": {"value": 60, "unit": "galaxies"},
            "galaxy_density": {"value": 0.05, "unit": "times_average"},
            "dark_matter_density": {"value": 0.1, "unit": "times_average"},
            "temperature": {"value": 2.7, "unit": "K", "note": "CMB temperature"},
            "expansion_rate": {"value": 75, "unit": "km/s/Mpc"},
            "void_center": {"value": "empty", "note": "Central region nearly empty"},
            "wall_thickness": {"value": 10, "unit": "Mpc"},
        },
        "detailed_description": (
            "The Bootes Void is one of the largest and most mysterious empty spaces in the observable universe, "
            "a vast cosmic desert spanning 330 million light-years in diameter. Located approximately 700 million "
            "light-years away in the direction of the Bootes constellation, this enormous void contains only about "
            "60 galaxies despite having enough volume to hold thousands. The galaxy density in the Bootes Void is "
            "only 5% of the average density of the universe, making it one of the most underdense regions known. "
            "The void appears as a spherical region of space with relatively few galaxies, surrounded by a 'wall' "
            "or 'shell' of higher galaxy density. The Bootes Void is so large that if our Milky Way galaxy were "
            "located at its center, we would not have discovered other galaxies until the 1960s, despite having "
            "excellent telescopes. The void's existence challenges our understanding of large-scale structure "
            "formation and raises questions about why such enormous empty regions exist. Several hypotheses have "
            "been proposed to explain the Bootes Void, including the possibility that it formed through the "
            "merger of smaller voids or that it represents a region where dark matter density is unusually low. "
            "The void has a slight temperature difference from the cosmic microwave background, suggesting it "
            "may be expanding slightly faster than surrounding regions. The Bootes Void serves as a crucial "
            "laboratory for studying cosmic structure formation, the effects of dark matter, and the large-scale "
            "distribution of matter in the universe. It also provides a unique window into the early universe and "
            "the processes that created the cosmic web of galaxies and voids."
        ),
        "scientific_facts": [
            "The Bootes Void spans 330 million light-years in diameter.",
            "The void contains only 60 galaxies instead of the expected thousands.",
            "Galaxy density in the Bootes Void is only 5% of the cosmic average.",
            "The void is so empty that if the Milky Way were inside, we wouldn't have discovered other galaxies until the 1960s.",
            "The Bootes Void has a volume of 0.004 cubic gigaparsecs.",
            "The void is surrounded by a wall of higher galaxy density.",
            "The Bootes Void challenges models of large-scale structure formation.",
            "The void may be expanding slightly faster than surrounding regions.",
            "Dark matter density in the Bootes Void is only 10% of average.",
            "The void provides insights into the formation of cosmic structure.",
            "The Bootes Void is one of the largest known cosmic voids.",
            "The void's existence raises questions about the uniformity of the universe.",
        ],
        "formation_process": [
            "The Bootes Void likely formed through gravitational processes that caused matter to flow away "
            "from this region into surrounding denser areas. It may have originated from density fluctuations "
            "in the early universe that were amplified over billions of years of cosmic evolution."
        ],
        "future_evolution": [
            "The Bootes Void will continue to expand as the universe expands, with its relative emptiness "
            "becoming more pronounced over time. The void may eventually merge with other voids or be filled "
            "by galaxies moving into the region from surrounding areas."
        ],
        "related_objects": ["Eridanus Supervoid", "Local Void", "Cosmic Web", "Large-Scale Structure"],
        "parent_system": "Observable Universe",
        "child_objects": ["Sparse Galaxies", "Dark Matter Underdensity"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    # -------------------------------------------------------------------------
    # SECTION 9: EXTREMAE QUASARS - ADDITIONAL REMARKABLE OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "s5-0014-81")),
        "name": "S5 0014+81",
        "category": "Quasar",
        "subtype": "Ultra-Massive Black Hole Quasar",
        "tags": ["quasar", "ultra-massive-black-hole", "blazar", "radio-loud", "extreme-luminosity"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 12.1e9, "unit": "ly"},
            "coordinates": {"ra": "00h 17m 08.5s", "dec": "+81° 35' 43\""},
            "galaxy_reference": "Distant Universe",
            "location": "Cepheus constellation",
            "redshift": {"value": 3.366, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 4e10, "unit": "solar_masses"},
            "bolometric_luminosity": {"value": 5e14, "unit": "solar_luminosities"},
            "accretion_rate": {"value": 800, "unit": "solar_masses/year"},
            "schwarzschild_radius": {"value": 1.2e14, "unit": "km"},
            "eddington_luminosity": {"value": 5e14, "unit": "solar_luminosities"},
            "jet_velocity": {"value": 0.98, "unit": "c"},
            "radio_loudness": {"value": 1000, "unit": "ratio"},
            "variability_timescale": {"value": 1, "unit": "day"},
        },
        "detailed_description": (
            "S5 0014+81 is one of the most massive and luminous quasars known, containing a black hole of "
            "40 billion solar masses that challenges our understanding of black hole growth in the early universe. "
            "Located 12.1 billion light-years away in Cepheus, this blazar-like quasar shines with a "
            "bolometric luminosity of 5×10^14 solar luminosities, making it one of the most powerful objects "
            "ever discovered. The black hole's event horizon has a diameter of 240 billion kilometers, and "
            "its Schwarzschild radius extends to 1.2×10^14 kilometers. S5 0014+81 is extremely radio-loud, "
            "with powerful relativistic jets traveling at 98% the speed of light that produce strong radio emission. "
            "The quasar accretes matter at 800 solar masses per year, operating near the Eddington limit for its "
            "massive black hole. At a redshift of 3.366, we see this object as it was when the universe was only "
            "2 billion years old, raising questions about how such a massive black hole could form so quickly. "
            "S5 0014+81 shows rapid variability on timescales of one day, indicating a compact emission region "
            "near the black hole. The quasar's spectrum shows extremely broad emission lines and evidence for "
            "powerful outflows that may be regulating star formation in its host galaxy. This object serves as a "
            "crucial laboratory for studying the physics of supermassive black holes, the mechanisms of black hole "
            "growth, and the feedback processes that shape galaxy evolution. S5 0014+81 represents one of the "
            "most extreme examples of black hole growth and quasar activity in the early universe."
        ),
        "scientific_facts": [
            "S5 0014+81 contains a 40 billion solar mass black hole.",
            "The black hole's event horizon diameter is 240 billion kilometers.",
            "S5 0014+81 is one of the most luminous quasars known.",
            "The quasar is seen when the universe was only 2 billion years old.",
            "S5 0014+81 accretes 800 solar masses of material per year.",
            "The quasar's jets travel at 98% the speed of light.",
            "S5 0014+81 is extremely radio-loud with strong radio emission.",
            "The quasar shows variability on timescales of one day.",
            "S5 0014+81's black hole mass challenges theories of early black hole growth.",
            "The quasar operates near the Eddington luminosity limit.",
            "S5 0014+81 has powerful outflows affecting its host galaxy.",
            "The quasar is a blazar-like object with jets pointed toward Earth.",
        ],
        "formation_process": (
            "S5 0014+81 formed through rapid accretion onto a massive seed black hole in the early universe, "
            "possibly through direct collapse or through mergers of smaller black holes. The quasar's extreme "
            "luminosity indicates it's in a phase of near-maximum accretion, consuming matter at an extraordinary "
            "rate to build up its massive black hole."
        ),
        "future_evolution": (
            "S5 0014+81 will continue its extreme accretion phase for millions of years before gradually "
            "fading as its fuel supply diminishes. The black hole will remain as the dominant object in its "
            "galaxy cluster, potentially affecting the formation and evolution of surrounding galaxies through "
            "its gravitational influence and past energetic feedback."
        ),
        "related_objects": ["TON 618", "Holmberg 15A", "3C 273", "Ultra-Massive Black Holes"],
        "parent_system": "Distant Universe",
        "child_objects": ["Relativistic Jets", "Accretion Disk", "Broad Line Region"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },


    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "pks-2126-158")),
        "name": "PKS 2126-158",
        "category": "Quasar",
        "subtype": "High-Redshift Radio-Loud Quasar with Absorption Systems",
        "tags": ["quasar", "high-redshift", "radio-loud", "absorption-systems", "early-universe"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 11.5e9, "unit": "ly"},
            "coordinates": {"ra": "21h 26m 26.0s", "dec": "-15° 38' 40\""},
            "galaxy_reference": "Distant Universe",
            "location": "Capricornus constellation",
            "redshift": {"value": 3.28, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 1e9, "unit": "solar_masses"},
            "bolometric_luminosity": {"value": 1e14, "unit": "solar_luminosities"},
            "radio_luminosity": {"value": 1e42, "unit": "erg/s"},
            "jet_velocity": {"value": 0.95, "unit": "c"},
            "absorption_system_count": {"value": 20, "unit": "systems"},
            "metallicity_absorbers": {"value": 0.1, "unit": "solar"},
            "x-ray_luminosity": {"value": 5e44, "unit": "erg/s"},
            "variability_timescale": {"value": 6, "unit": "hours"},
        },
        "detailed_description": (
            "PKS 2126-158 is a remarkable high-redshift quasar that serves as a powerful probe of the early "
            "universe through its numerous absorption systems. Located 11.5 billion light-years away in Capricornus, "
            "this radio-loud quasar has a redshift of 3.28, meaning we see it as it was when the universe was "
            "only 2.2 billion years old. The quasar is powered by a 1 billion solar mass black hole and shines "
            "with a bolometric luminosity of 10^14 solar luminosities. PKS 2126-158 is particularly valuable because "
            "its light passes through about 20 different absorption systems on its way to Earth, each representing "
            "different galaxies or gas clouds at various distances. These absorption systems provide crucial "
            "information about the chemical enrichment, gas content, and physical conditions in the early universe. "
            "The quasar's spectrum shows metal lines indicating that significant chemical enrichment had already "
            "occurred by this epoch, with metallicities in the absorbers reaching about 10% of solar values. "
            "PKS 2126-158 is a strong radio source with relativistic jets traveling at 95% the speed of light, "
            "making it an excellent laboratory for studying jet physics at high redshift. The quasar shows "
            "variability on timescales as short as 6 hours, providing insights into the structure of the emission "
            "regions near the black hole. This object has been extensively studied as a background source for "
            "investigating the intergalactic medium and the evolution of galaxies in the early universe. PKS "
            "2126-158 represents a crucial link between the early universe and the present, allowing us to study "
            "the conditions that existed when the first galaxies were forming and evolving."
        ),
        "scientific_facts": [
            "PKS 2126-158 has 20 absorption systems along our line of sight.",
            "The quasar is seen when the universe was only 2.2 billion years old.",
            "PKS 2126-158's absorption systems show metallicities of 10% solar.",
            "The quasar is a strong radio source with powerful jets.",
            "PKS 2126-158 shows variability on 6-hour timescales.",
            "The quasar's black hole mass is 1 billion solar masses.",
            "PKS 2126-158 provides insights into early universe chemical enrichment.",
            "The quasar's jets travel at 95% the speed of light.",
            "PKS 2126-158 is a probe of intergalactic medium evolution.",
            "The quasar's absorption systems represent different cosmic epochs.",
            "PKS 2126-158 has been extensively studied for cosmic evolution studies.",
            "The quasar shows evidence for significant star formation in early galaxies.",
        ],
        "formation_process": (
            "PKS 2126-158 formed when a supermassive black hole at the center of an early galaxy began actively "
            "accreting gas. The numerous absorption systems along our line of sight represent galaxies and gas "
            "clouds that existed at various cosmic epochs, providing a fossil record of cosmic evolution."
        ),
        "future_evolution": (
            "PKS 2126-158 will continue its active phase for millions of years before gradually fading. "
            "The absorption systems along our line of sight will continue to evolve, and the quasar's host "
            "galaxy will continue to develop and mature through cosmic time."
        ),
        "related_objects": ["PKS 2128-123", "3C 273", "High-Redshift Quasars", "Absorption Systems"],
        "parent_system": "Distant Universe",
        "child_objects": ["Relativistic Jets", "Absorption Systems", "Host Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 10: EXTREMAE BLAZARS - ADDITIONAL JET-DOMINATED OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "3c-279")),
        "name": "3C 279",
        "category": "Blazar",
        "subtype": "Optically Violently Variable Quasar",
        "tags": ["blazar", "ovv", "superluminal-jet", "gamma-ray", "variable", "first-blazar"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 5.0e9, "unit": "ly"},
            "coordinates": {"ra": "12h 53m 35.1s", "dec": "-05° 49' 17\""},
            "galaxy_reference": "Distant Universe",
            "location": "Virgo constellation",
            "redshift": {"value": 0.536, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 8e8, "unit": "solar_masses"},
            "jet_lorentz_factor": {"value": 20, "unit": "gamma"},
            "jet_angle": {"value": 1, "unit": "degrees", "note": "To line of sight"},
            "apparent_velocity": {"value": 17, "unit": "c", "note": "Superluminal motion"},
            "gamma-ray_luminosity": {"value": 1e48, "unit": "erg/s"},
            "optical_variability": {"value": 5, "unit": "magnitudes"},
            "polarization": {"value": 30, "unit": "percent"},
            "radio_loudness": {"value": 10000, "unit": "ratio"},
        },
        "detailed_description": (
            "3C 279 is one of the most remarkable and well-studied blazars, an optically violently variable "
            "quasar that has served as a fundamental laboratory for understanding relativistic jets and high-energy "
            "emission processes. Located 5 billion light-years away in Virgo, this blazar was the first object "
            "to show superluminal motion, with jet components appearing to move at 17 times the speed of light - "
            "an illusion created by material traveling at 99.9% the speed of light at a very small angle to our "
            "line of sight. 3C 279 is a powerful gamma-ray source with a luminosity of 10^48 erg/s, making it "
            "one of the brightest gamma-ray blazars in the sky. The object shows extreme variability across the "
            "electromagnetic spectrum, with optical brightness changes of up to 5 magnitudes and dramatic gamma-ray "
            "flares that can increase its brightness by factors of 100 in just hours. 3C 279 was the first blazar "
            "detected by the EGRET instrument on the Compton Gamma Ray Observatory in 1991, establishing it as a "
            "prototype for high-energy blazar studies. The blazar's high polarization of 30% indicates highly "
            "ordered magnetic fields in the jet, and its radio loudness of 10,000 makes it one of the most radio-"
            "intense objects known. 3C 279 has been extensively studied with multi-wavelength campaigns that "
            "have revealed complex correlations between variability at different wavelengths, providing insights "
            "into the physical processes operating in relativistic jets. This object continues to be a crucial "
            "target for studying jet physics, particle acceleration mechanisms, and the extreme conditions near "
            "supermassive black holes."
        ),
        "scientific_facts": [
            "3C 279 was the first object to show superluminal motion.",
            "The blazar's jet appears to move at 17 times the speed of light.",
            "3C 279 is one of the brightest gamma-ray blazars known.",
            "The blazar shows optical variability of up to 5 magnitudes.",
            "3C 279 was the first blazar detected in gamma rays.",
            "The blazar's jet travels at 99.9% the speed of light.",
            "3C 279 has a radio loudness of 10,000.",
            "The blazar shows 30% polarization, indicating ordered magnetic fields.",
            "3C 279 can brighten by factors of 100 in just hours.",
            "The blazar's black hole mass is 800 million solar masses.",
            "3C 279 has been studied continuously for over 30 years.",
            "The blazar provides insights into relativistic jet physics.",
        ],
        "formation_process": (
            "3C 279 formed when a supermassive black hole developed an extremely relativistic jet pointed "
            "almost directly toward Earth. The jet's alignment and relativistic effects create the blazar's "
            "observed characteristics, including superluminal motion and extreme variability."
        ),
        "future_evolution": (
            "3C 279 will continue its extreme variability and jet activity for millions of years. The blazar "
            "will eventually exhaust its fuel supply and transition to a less active phase, though the "
            "supermassive black hole will remain at the galaxy center."
        ),
        "related_objects": ["3C 273", "PKS 1510-089", "BL Lacertae", "OVV Quasars"],
        "parent_system": "Distant Universe",
        "child_objects": ["Superluminal Jet", "Emission Regions", "Host Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "markarian-501")),
        "name": "Markarian 501 (Mrk 501)",
        "category": "Blazar",
        "subtype": "High-Frequency-Peaked BL Lac Object",
        "tags": ["blazar", "bl-lac", "tevatron-source", "variable", "high-energy", "nearby-blazar"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 457e6, "unit": "ly"},
            "coordinates": {"ra": "16h 53m 52.2s", "dec": "+39° 45' 37\""},
            "galaxy_reference": "Local Supercluster",
            "location": "Hercules constellation",
            "redshift": {"value": 0.034, "unit": "z"},
        },
        "physical": {
            "black_hole_mass": {"value": 1e9, "unit": "solar_masses"},
            "jet_lorentz_factor": {"value": 12, "unit": "gamma"},
            "jet_angle": {"value": 2, "unit": "degrees", "note": "To line of sight"},
            "apparent_velocity": {"value": 8, "unit": "c", "note": "Superluminal motion"},
            "gamma-ray_luminosity": {"value": 2e45, "unit": "erg/s"},
            "x-ray_luminosity": {"value": 1e44, "unit": "erg/s"},
            "variability_timescale": {"value": 60, "unit": "minutes"},
            "spectral_peak": {"value": 10, "unit": "keV"},
        },
        "detailed_description": (
            "Markarian 501 is one of the closest and most studied high-frequency-peaked BL Lacertae objects, "
            "serving as a crucial laboratory for understanding particle acceleration and high-energy emission processes "
            "in relativistic jets. Located 457 million light-years away in Hercules, this blazar is characterized by "
            "a relativistic jet pointed nearly toward Earth, making it appear extremely bright and variable across "
            "the electromagnetic spectrum. Mrk 501 is one of the brightest TeV gamma-ray sources in the northern sky, "
            "establishing it as an important 'Tevatron' - a natural particle accelerator capable of producing particles "
            "with energies in the tera-electron-volt range. The blazar underwent a spectacular flare in 1997, "
            "becoming the brightest TeV source in the sky and providing unprecedented insights into high-energy "
            "emission mechanisms. Mrk 501 exhibits dramatic variability on timescales from minutes to years, with "
            "rapid changes occurring in just 60 minutes, implying an extremely compact emission region near the "
            "central black hole. The jet material travels with a Lorentz factor of 12 and appears to move at eight "
            "times the speed of light due to relativistic effects. Mrk 501's spectrum peaks in the X-ray regime at "
            "around 10 keV, making it an excellent target for studying synchrotron emission from relativistic "
            "electrons. The blazar has been extensively studied with multi-wavelength observations that have "
            "revealed complex correlations between X-ray and gamma-ray variability, providing crucial insights "
            "into the physical processes operating in relativistic jets. Mrk 501's proximity and high luminosity make "
            "it a fundamental calibration source for gamma-ray telescopes and a benchmark for testing theories "
            "of jet formation and high-energy astrophysical processes."
        ),
        "scientific_facts": [
            "Mrk 501 is one of the brightest TeV gamma-ray sources in the northern sky.",
            "The blazar underwent a spectacular flare in 1997.",
            "Mrk 501 varies on timescales as short as 60 minutes.",
            "The blazar's jet appears to move at 8 times the speed of light.",
            "Mrk 501 is one of the closest known BL Lac objects.",
            "The blazar can accelerate particles to TeV energies.",
            "Mrk 501's spectrum peaks at 10 keV in X-rays.",
            "The blazar's black hole mass is estimated at 1 billion solar masses.",
            "Mrk 501 shows complex multi-wavelength variability.",
            "The blazar serves as a calibration source for gamma-ray telescopes.",
            "Mrk 501 provides insights into particle acceleration mechanisms.",
            "The blazar has been studied continuously for over 20 years.",
        ],
        "formation_process": (
            "Mrk 501 formed when a supermassive black hole at the center of a giant elliptical galaxy developed "
            "a powerful relativistic jet pointed nearly toward Earth. The jet's alignment creates the blazar "
            "characteristics through relativistic beaming effects that enhance the observed luminosity and "
            "create rapid variability."
        ),
        "future_evolution": (
            "Mrk 501 will continue its active blazar phase for millions of years, with ongoing jet activity "
            "and variability. Eventually, the accretion rate will decline and the jet will weaken, transforming "
            "the object into a normal radio galaxy with a dormant supermassive black hole."
        ),
        "related_objects": ["Markarian 421", "PKS 2155-304", "1ES 1426+428", "HBL Blazars"],
        "parent_system": "Local Supercluster",
        "child_objects": ["Relativistic Jet", "Supermassive Black Hole", "Host Elliptical Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 11: EXTREMAE GAMMA-RAY BURSTS - ADDITIONAL EXPLOSIONS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "grb-991216")),
        "name": "GRB 991216",
        "category": "Gamma-Ray Burst",
        "subtype": "Long-Duration GRB with Complex Afterglow",
        "tags": ["gamma-ray-burst", "long-grb", "complex-afterglow", "well-studied", "multi-wavelength"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 6.0e9, "unit": "ly"},
            "coordinates": {"ra": "22h 32m 09.7s", "dec": "+12° 23' 53\""},
            "galaxy_reference": "Distant Universe",
            "location": "Pegasus constellation",
            "redshift": {"value": 1.02, "unit": "z"},
        },
        "physical": {
            "isotropic_energy": {"value": 1.2e53, "unit": "ergs"},
            "duration": {"value": 5, "unit": "seconds"},
            "peak_energy": {"value": 300, "unit": "keV"},
            "jet_angle": {"value": 3, "unit": "degrees"},
            "beaming_factor": {"value": 1000, "unit": "correction"},
            "true_energy": {"value": 1.2e56, "unit": "ergs"},
            "afterglow_duration": {"value": 100, "unit": "days"},
            "optical_flash": {"value": "detected", "note": "Bright optical counterpart"},
        },
        "detailed_description": (
            "GRB 991216 is a remarkable long-duration gamma-ray burst that provided unprecedented insights into "
            "the complex physics of GRB afterglows and jet structure. Discovered on December 16, 1999, by the "
            "BATSE instrument on the Compton Gamma Ray Observatory, this burst lasted for 5 seconds and released "
            "an isotropic energy of 1.2×10^53 ergs. When corrected for jet collimation, the true energy release "
            "reached 1.2×10^56 ergs, making it one of the most energetic explosions ever recorded. GRB 991216 "
            "was observed extensively across the electromagnetic spectrum, from radio waves to gamma rays, providing "
            "one of the most complete multi-wavelength datasets for any gamma-ray burst. The burst's afterglow "
            "was particularly complex, showing unusual features including a 'steep-to-shallow' transition in the "
            "X-ray light curve and evidence for energy injection into the external shock. The optical afterglow "
            "was bright and showed evidence for a host galaxy with significant star formation activity. GRB 991216 "
            "occurred at a redshift of 1.02, meaning we see it as it was when the universe was about half its "
            "current age. The burst's spectrum showed a peak energy of 300 keV, typical for long GRBs, and "
            "evidence for spectral evolution during the event. GRB 991216 has been crucial for testing models of "
            "afterglow physics, jet structure, and the interaction between relativistic jets and the surrounding "
            "medium. This burst demonstrated the importance of rapid multi-wavelength follow-up observations and "
            "provided insights into the diversity of gamma-ray burst afterglow behavior."
        ),
        "scientific_facts": [
            "GRB 991216 released 1.2×10^53 ergs of energy isotropically.",
            "The burst's true energy reached 1.2×10^56 ergs when corrected for jet collimation.",
            "GRB 991216 had one of the most complete multi-wavelength datasets.",
            "The burst's afterglow showed complex behavior including energy injection.",
            "GRB 991216 occurred at redshift 1.02, when the universe was half its current age.",
            "The burst's optical afterglow was bright and well-studied.",
            "GRB 991216 lasted 5 seconds in gamma rays.",
            "The burst showed evidence for complex jet structure.",
            "GRB 991216 provided insights into afterglow physics.",
            "The burst's host galaxy showed significant star formation.",
            "GRB 991216 demonstrated the importance of rapid follow-up observations.",
            "The burst has been extensively studied for GRB physics.",
        ],
        "formation_process": (
            "GRB 991216 resulted from the core-collapse of a massive star that had lost its outer hydrogen "
            "envelope. The collapse created a black hole that launched relativistic jets, which broke through "
            "the stellar surface and produced the gamma-ray burst as they interacted with the surrounding medium."
        ),
        "future_evolution": (
            "GRB 991216's afterglow has faded over the years, but the burst's energy has enriched the "
            "intergalactic medium with heavy elements. The remnant black hole continues to exist in its host "
            "galaxy, potentially affecting future star formation through its gravitational influence."
        ),
        "related_objects": ["GRB 970508", "GRB 990123", "Long GRBs", "Complex Afterglows"],
        "parent_system": "Distant Universe",
        "child_objects": ["Relativistic Jets", "Complex Afterglow", "Host Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "grb-050904")),
        "name": "GRB 050904",
        "category": "Gamma-Ray Burst",
        "subtype": "High-Redshift Long-Duration GRB",
        "tags": ["gamma-ray-burst", "high-redshift", "early-universe", "long-grb", "dusty-afterglow"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 12.6e9, "unit": "ly"},
            "coordinates": {"ra": "23h 53m 16.6s", "dec": "+09° 16' 51\""},
            "galaxy_reference": "Early Universe",
            "location": "Pisces constellation",
            "redshift": {"value": 6.3, "unit": "z"},
        },
        "physical": {
            "isotropic_energy": {"value": 1.1e54, "unit": "ergs"},
            "duration": {"value": 225, "unit": "seconds"},
            "peak_energy": {"value": 500, "unit": "keV"},
            "jet_angle": {"value": 7, "unit": "degrees"},
            "beaming_factor": {"value": 300, "unit": "correction"},
            "true_energy": {"value": 3.3e56, "unit": "ergs"},
            "dust_extinction": {"value": 2, "unit": "magnitudes"},
            "host_galaxy_mass": {"value": 1e10, "unit": "solar_masses"},
        },
        "detailed_description": (
            "GRB 050904 is one of the most distant gamma-ray bursts ever detected, occurring when the universe "
            "was only 830 million years old - just 6% of its current age. Discovered on September 4, 2005, by "
            "NASA's Swift satellite, this remarkable burst provides a unique window into the epoch of reionization "
            "when the first stars and galaxies were forming. The burst lasted for an unusually long 225 seconds "
            "and released an isotropic energy of 1.1×10^54 ergs, with a true energy of 3.3×10^56 ergs when corrected "
            "for jet collimation. GRB 050904 occurred at a redshift of 6.3, making it one of the most distant "
            "objects ever discovered and providing crucial insights into conditions in the very early universe. "
            "The burst's afterglow was heavily obscured by dust, indicating significant metal enrichment had "
            "already occurred by this epoch. The spectrum showed evidence for heavy elements including silicon and "
            "iron, proving that multiple generations of stars had already lived and died within the first 830 "
            "million years of cosmic history. GRB 050904's host galaxy appears to be a massive star-forming galaxy "
            "with a mass of 10^10 solar masses, challenging our understanding of how massive galaxies could form "
            "so early. The burst provided the first direct evidence that star formation and metal enrichment were "
            "already well underway in the early universe. GRB 050904 serves as a powerful beacon for studying the "
            "cosmic dark ages, the reionization epoch, and the formation of the first massive galaxies."
        ),
        "scientific_facts": [
            "GRB 050904 is one of the most distant gamma-ray bursts known.",
            "The burst occurred when the universe was only 830 million years old.",
            "GRB 050904 released 1.1×10^54 ergs of energy isotropically.",
            "The burst's true energy reached 3.3×10^56 ergs.",
            "GRB 050904's afterglow was heavily obscured by dust.",
            "The burst showed evidence for heavy elements including iron.",
            "GRB 050904's host galaxy has a mass of 10^10 solar masses.",
            "The burst lasted 225 seconds, unusually long for a high-redshift GRB.",
            "GRB 050904 proves star formation was well underway in the early universe.",
            "The burst occurred at redshift 6.3 during the epoch of reionization.",
            "GRB 050904 provides insights into early galaxy formation.",
            "The burst serves as a beacon for studying the cosmic dark ages.",
        ],
        "formation_process": (
            "GRB 050904 resulted from the core-collapse of a massive star that had formed in one of the first "
            "generations of galaxies. The star's death occurred when the universe was still very young, providing "
            "evidence that massive star formation was already occurring in the early universe."
        ),
        "future_evolution": (
            "GRB 050904's afterglow has long since faded, but the burst's energy has contributed to the "
            "reionization of the early universe. The remnant black hole continues to exist in the distant "
            "universe, possibly now part of a larger galaxy that formed around it over the past 12.6 billion years."
        ),
        "related_objects": ["GRB 090423", "GRB 080913", "High-Redshift GRBs", "Early Universe"],
        "parent_system": "Early Universe",
        "child_objects": ["Relativistic Jets", "Dusty Afterglow", "Host Galaxy"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/"
    },

]


# -------------------------------------------------------------------------
# PHASE 4: COSMIC OBJECTS - THEORETICAL CONSTRUCTS AND EXTREME EXAMPLES
# -------------------------------------------------------------------------


COSMIC_OBJECTS_PHASE4 = [
    # -------------------------------------------------------------------------
    # SECTION 1: DARK MATTER STRUCTURES - THEORETICAL CONSTRUCTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "dark-matter-halo-virgo")),
        "name": "Virgo Dark Matter Halo",
        "category": "Dark Matter Structure",
        "subtype": "Galaxy Cluster Dark Matter Halo",
        "tags": ["dark-matter", "halo", "virgo-cluster", "gravitational-lensing", "theoretical-structure"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 54e6, "unit": "ly"},
            "coordinates": {"ra": "12h 27m", "dec": "+12° 43'"},
            "galaxy_reference": "Virgo Cluster",
            "location": "Virgo constellation",
            "size": {"value": 2.2, "unit": "Mpc"},
        },
        "physical": {
            "dark_matter_mass": {"value": 1.2e15, "unit": "solar_masses"},
            "dark_matter_density": {"value": 0.01, "unit": "solar_masses/pc³"},
            "virial_radius": {"value": 1.2, "unit": "Mpc"},
            "concentration_parameter": {"value": 4.5, "unit": "dimensionless"},
            "velocity_dispersion": {"value": 700, "unit": "km/s"},
            "dark_matter_temperature": {"value": 1e6, "unit": "K"},
            "annihilation_rate": {"value": 1e-30, "unit": "cm³/s"},
            "self_interaction_cross_section": {"value": 1e-24, "unit": "cm²/g"},
        },
        "detailed_description": (
            "The Virgo Dark Matter Halo is a massive, invisible structure that dominates the gravitational potential "
            "of the Virgo Galaxy Cluster, representing one of the largest concentrations of dark matter in the nearby "
            "universe. This theoretical construct, inferred through gravitational lensing observations and galaxy "
            "dynamics measurements, contains approximately 1.2×10^15 solar masses of dark matter - equivalent to "
            "over a trillion suns. The halo extends to a virial radius of 1.2 megaparsecs, encompassing over "
            "1,300 galaxies and providing the gravitational scaffolding that holds the entire cluster together. "
            "The dark matter distribution follows a NFW (Navarro-Frenk-White) profile with a concentration parameter "
            "of 4.5, indicating a dense core that becomes less concentrated toward the edges. The halo's gravitational "
            "influence creates a velocity dispersion of 700 km/s among cluster galaxies and produces strong gravitational "
            "lensing effects that magnify background galaxies by factors of up to 10. The Virgo Dark Matter Halo serves "
            "as a crucial laboratory for studying dark matter properties, including potential self-interaction cross-"
            "sections and annihilation rates. This structure represents the culmination of hierarchical structure "
            "formation, where smaller dark matter halos merged over billions of years to create the massive halo we "
            "observe today. The Virgo Dark Matter Halo continues to grow by accreting smaller groups and individual "
            "galaxies, and its gravitational influence affects the motion of the Local Group, including our own "
            "Milky Way galaxy."
        ),
        "scientific_facts": [
            "The Virgo Dark Matter Halo contains 1.2×10^15 solar masses of dark matter.",
            "The halo extends to a virial radius of 1.2 megaparsecs.",
            "The dark matter creates a velocity dispersion of 700 km/s among cluster galaxies.",
            "The halo produces strong gravitational lensing effects.",
            "The Virgo Dark Matter Halo encompasses over 1,300 galaxies.",
            "The dark matter follows a NFW density profile with concentration 4.5.",
            "The halo's gravitational influence affects the Milky Way's motion.",
            "The structure represents the result of hierarchical galaxy formation.",
            "The Virgo Dark Matter Halo continues to accrete smaller galaxy groups.",
            "The halo provides constraints on dark matter particle properties.",
            "The structure is inferred through multiple observational techniques.",
            "The Virgo Dark Matter Halo is one of the most massive dark matter concentrations nearby.",
        ],
        "formation_process": (
            "The Virgo Dark Matter Halo formed through the hierarchical merging of smaller dark matter halos "
            "over billions of years. Small density fluctuations in the early universe grew through gravitational "
            "collapse, eventually merging to create the massive halo that dominates the Virgo Cluster today."
        ),
        "future_evolution": (
            "The Virgo Dark Matter Halo will continue to grow by accreting surrounding matter and galaxy groups. "
            "Eventually, it may merge with other massive clusters to form even larger structures, potentially "
            "becoming part of a supercluster complex in the far future."
        ),
        "related_objects": ["Local Group Dark Matter Halo", "Coma Cluster Dark Matter", "Dark Matter Subhalos"],
        "parent_system": "Virgo Supercluster",
        "child_objects": ["Galaxy Dark Matter Halos", "Dark Matter Substructures", "Gravitational Lensing Arcs"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "dark-matter-stream-sagittarius")),
        "name": "Sagittarius Dark Matter Stream",
        "category": "Dark Matter Structure",
        "subtype": "Tidal Dark Matter Stream",
        "tags": ["dark-matter", "tidal-stream", "sagittarius-dwarf", "galactic-halo", "milky-way"],
        "difficulty_level": "advanced",
        "spatial": {
            "distance_from_earth": {"value": 25000, "unit": "ly"},
            "coordinates": {"ra": "multiple", "dec": "multiple", "note": "Stellar stream across sky"},
            "galaxy_reference": "Milky Way",
            "location": "Wrapping around the Milky Way",
            "length": {"value": 360, "unit": "degrees"},
        },
        "physical": {
            "dark_matter_mass": {"value": 1e8, "unit": "solar_masses"},
            "stream_width": {"value": 10000, "unit": "ly"},
            "stream_length": {"value": 100000, "unit": "ly"},
            "velocity_dispersion": {"value": 20, "unit": "km/s"},
            "dark_matter_density": {"value": 0.001, "unit": "solar_masses/pc³"},
            "orbital_period": {"value": 700, "unit": "million_years"},
            "tidal_radius": {"value": 5000, "unit": "ly"},
            "metallicity": {"value": -1.5, "unit": "[Fe/H]"},
        },
        "detailed_description": (
            "The Sagittarius Dark Matter Stream is a vast, invisible ribbon of dark matter that wraps around "
            "the Milky Way galaxy, representing the remnant gravitational scaffold of the Sagittarius Dwarf "
            "Galaxy as it undergoes tidal disruption. This theoretical structure, detected indirectly through "
            "the stellar streams that trace its path, contains approximately 10^8 solar masses of dark matter "
            "that extends for 100,000 light-years in a complex orbital pattern around our galaxy. The stream "
            "is the result of billions of years of tidal stripping as the Sagittarius Dwarf Galaxy orbits "
            "the Milky Way, losing both stars and dark matter to our galaxy's gravitational field. The dark "
            "matter stream follows the same orbital path as the visible stellar streams but is much more "
            "massive, providing the gravitational framework that holds the stellar debris together. The stream "
            "wraps completely around the Milky Way, having completed multiple orbits and creating a complex "
            "web-like structure that passes through different regions of our galaxy's halo. The Sagittarius "
            "Dark Matter Stream provides crucial insights into dark matter properties, including its "
            "self-interaction cross-section and response to tidal forces. This structure serves as a natural "
            "laboratory for studying the interaction between dark matter and normal matter, and helps constrain "
            "models of galaxy formation and evolution. The stream's presence affects the local dark matter "
            "density and may influence direct detection experiments on Earth."
        ),
        "scientific_facts": [
            "The Sagittarius Dark Matter Stream contains 10^8 solar masses of dark matter.",
            "The stream extends for 100,000 light-years around the Milky Way.",
            "The stream is the remnant of the Sagittarius Dwarf Galaxy's dark matter halo.",
            "The structure wraps completely around the Milky Way galaxy.",
            "The stream provides constraints on dark matter self-interaction properties.",
            "The dark matter stream follows the same path as visible stellar streams.",
            "The structure affects local dark matter density for detection experiments.",
            "The stream has been tidally stripped over billions of years.",
            "The Sagittarius Dark Matter Stream has completed multiple orbital periods.",
            "The structure provides insights into galaxy formation processes.",
            "The stream's width is approximately 10,000 light-years.",
            "The dark matter stream helps hold stellar debris together gravitationally.",
        ],
        "formation_process": (
            "The Sagittarius Dark Matter Stream formed as the Sagittarius Dwarf Galaxy orbited the Milky Way "
            "and was gradually tidally disrupted. The Milky Way's gravitational field stripped away both stars "
            "and dark matter, creating streams that trace the dwarf galaxy's orbital path through our galaxy's halo."
        ),
        "future_evolution": (
            "The Sagittarius Dark Matter Stream will continue to be disrupted and eventually disperse into "
            "the Milky Way's halo, contributing to the overall dark matter distribution. The stream will become "
            "less coherent over time as it mixes with the Milky Way's native dark matter halo."
        ),
        "related_objects": ["Sagittarius Dwarf Galaxy", "Milky Way Dark Matter Halo", "Stellar Streams", "Tidal Disruption"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Dark Matter Substructures", "Stellar Stream Counterparts", "Tidal Debris"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    # -------------------------------------------------------------------------
    # SECTION 2: COSMIC STRINGS - THEORETICAL TOPOLOGICAL DEFECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cosmic-string-cmb-anomaly")),
        "name": "CMB Cold Spot Cosmic String",
        "category": "Cosmic String",
        "subtype": "Theoretical Topological Defect",
        "tags": ["cosmic-string", "topological-defect", "cmb-anomaly", "cold-spot", "grand-unified-theory"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 13.8e9, "unit": "ly", "note": "At surface of last scattering"},
            "coordinates": {"ra": "23h 21m", "dec": "-18° 00'"},
            "galaxy_reference": "Observable Universe",
            "location": "Eridanus constellation direction",
            "length": {"value": 1e11, "unit": "ly"},
        },
        "physical": {
            "string_tension": {"value": 1e-6, "unit": "planck_units"},
            "linear_mass_density": {"value": 1e22, "unit": "kg/m"},
            "gravitational_effect": {"value": 1e-6, "unit": "dimensionless"},
            "temperature_anomaly": {"value": -150, "unit": "µK"},
            "angular_size": {"value": 5, "unit": "degrees"},
            "energy_per_unit_length": {"value": 1e35, "unit": "J/m"},
            "oscillation_period": {"value": 1e-35, "unit": "seconds"},
            "decay_rate": {"value": 1e-40, "unit": "s^-1"},
        },
        "detailed_description": (
            "The CMB Cold Spot Cosmic String is a hypothetical topological defect that could explain one of the "
            "most mysterious anomalies in the cosmic microwave background - a unusually cold region spanning 5 "
            "degrees in the Eridanus constellation. This theoretical cosmic string would be an ultra-thin, "
            "one-dimensional defect in spacetime itself, formed during phase transitions in the early universe when "
            "symmetries were broken as the universe cooled. The string would have an enormous linear mass density "
            "of 10^22 kg/m, equivalent to the mass of 10,000 suns per meter of length, creating a gravitational "
            "field that bends light and affects the CMB passing through it. The cosmic string would stretch "
            "across the observable universe for 10^11 light-years, vibrating at frequencies determined by its "
            "tension and creating the temperature anomaly observed in the CMB. The string's gravitational lensing "
            "effect would create the cold spot by focusing CMB photons away from our line of sight, while its "
            "vibrations would generate gravitational waves that could be detected by future observatories. This "
            "cosmic string represents a relic from the first fractions of a second after the Big Bang, when the "
            "universe underwent phase transitions predicted by grand unified theories. The existence of such a "
            "string would provide direct evidence for fundamental physics beyond the Standard Model and offer "
            "insights into the earliest moments of cosmic history. The CMB Cold Spot Cosmic String serves as a "
            "crucial test of theories of topological defects and the physics of the early universe."
        ),
        "scientific_facts": [
            "The cosmic string would have a linear mass density of 10^22 kg/m.",
            "The string could explain the CMB Cold Spot anomaly.",
            "The cosmic string would stretch across 10^11 light-years.",
            "The string represents a topological defect from the early universe.",
            "The structure would create gravitational lensing effects.",
            "The cosmic string formed during phase transitions in the early universe.",
            "The string's vibrations would generate gravitational waves.",
            "The structure would have enormous tension close to the Planck scale.",
            "The cosmic string represents a relic from grand unified theory era.",
            "The string would affect CMB photons passing through it.",
            "The structure provides evidence for physics beyond the Standard Model.",
            "The cosmic string offers insights into the earliest moments of the universe.",
        ],
        "formation_process": (
            "The cosmic string would have formed during phase transitions in the early universe, specifically "
            "during symmetry-breaking events predicted by grand unified theories. As the universe cooled, different "
            "regions could choose different vacuum states, creating topological defects where these regions met."
        ),
        "future_evolution": (
            "The cosmic string would continue to oscillate and evolve, potentially breaking into smaller loops "
            "that decay through gravitational radiation. The string network would gradually lose energy and "
            "disappear over cosmic timescales, leaving behind only gravitational wave signatures."
        ),
        "related_objects": ["CMB Cold Spot", "Grand Unified Theory Phase Transitions", "Topological Defects", "Gravitational Waves"],
        "parent_system": "Observable Universe",
        "child_objects": ["String Loops", "Gravitational Wave Emissions", "CMB Anomalies"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/cosmology/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "cosmic-string-loop-gravitational-waves")),
        "name": "Gravitational Wave Emitting String Loop",
        "category": "Cosmic String",
        "subtype": "Oscillating String Loop",
        "tags": ["cosmic-string", "gravitational-waves", "string-loop", "oscillation", "early-universe"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 1e9, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Hypothetical location"},
            "galaxy_reference": "Intergalactic Space",
            "location": "Unknown region of space",
            "loop_circumference": {"value": 1e13, "unit": "km"},
        },
        "physical": {
            "loop_radius": {"value": 1e12, "unit": "km"},
            "oscillation_frequency": {"value": 1e-8, "unit": "Hz"},
            "gravitational_wave_power": {"value": 1e40, "unit": "watts"},
            "string_tension": {"value": 1e-7, "unit": "planck_units"},
            "decay_timescale": {"value": 1e6, "unit": "years"},
            "energy_content": {"value": 1e45, "unit": "joules"},
            "velocity": {"value": 0.5, "unit": "c"},
            "gravitational_strain": {"value": 1e-21, "unit": "dimensionless"},
        },
        "detailed_description": (
            "The Gravitational Wave Emitting String Loop is a hypothetical closed loop of cosmic string that "
            "oscillates at high frequencies and continuously emits gravitational waves, representing one of the "
            "most exotic energy sources in the universe. This theoretical structure would form when a long cosmic "
            "string intersects itself and breaks off a closed loop, creating a ring-like structure with a circumference "
            "of 10^13 kilometers - larger than our entire solar system. The string loop would oscillate at frequencies "
            "determined by its size and tension, generating a continuous stream of gravitational waves with a power "
            "output of 10^40 watts - equivalent to the luminosity of 100 billion suns. The loop's gravitational wave "
            "emission would create a characteristic strain pattern that could be detected by gravitational wave "
            "observatories, providing direct evidence for the existence of cosmic strings. The string loop would "
            "gradually lose energy through gravitational radiation, shrinking over a timescale of a million years "
            "until it eventually disappears. The loop's motion through space would create a wake of gravitational "
            "disturbances and potentially generate electromagnetic radiation through interactions with magnetic fields. "
            "This structure represents a unique laboratory for studying fundamental physics, including the behavior of "
            "matter under extreme conditions and the nature of spacetime itself. The Gravitational Wave Emitting String "
            "Loop serves as a crucial target for gravitational wave astronomy and could provide insights into the "
            "physics of the early universe and grand unified theories."
        ),
        "scientific_facts": [
            "The string loop emits 10^40 watts of gravitational wave power.",
            "The loop has a circumference of 10^13 kilometers.",
            "The string loop oscillates at frequencies of 10^-8 Hz.",
            "The structure gradually decays through gravitational radiation.",
            "The loop would create detectable gravitational wave strains.",
            "The string loop formed from a self-intersecting cosmic string.",
            "The structure's energy content is 10^45 joules.",
            "The loop moves through space at half the speed of light.",
            "The string loop provides evidence for grand unified theories.",
            "The structure represents a unique gravitational wave source.",
            "The loop's decay timescale is approximately one million years.",
            "The string loop creates a wake of gravitational disturbances.",
        ],
        "formation_process": (
            "The string loop would form when a long cosmic string self-intersects and breaks off a closed segment. "
            "This process can occur through the natural evolution of string networks or through interactions "
            "between different strings in the early universe."
        ),
        "future_evolution": (
            "The string loop will continue to oscillate and emit gravitational waves, gradually losing energy and "
            "shrinking until it eventually disappears. The loop will leave behind a burst of gravitational waves "
            "as it completes its final decay."
        ),
        "related_objects": ["Cosmic String Networks", "Gravitational Wave Sources", "String Theory", "Early Universe Physics"],
        "parent_system": "Intergalactic Space",
        "child_objects": ["Gravitational Wave Emissions", "String Oscillations", "Electromagnetic Interactions"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/cosmology/",
    },

    # -------------------------------------------------------------------------
    # SECTION 3: PRIMORDIAL BLACK HOLES - THEORETICAL EARLY UNIVERSE OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "primordial-black-hole-dark-matter")),
        "name": "Dark Matter Candidate Primordial Black Hole",
        "category": "Primordial Black Hole",
        "subtype": "Dark Matter Constituent",
        "tags": ["primordial-black-hole", "dark-matter", "early-universe", "hawking-radiation", "microlensing"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": "various", "unit": "ly", "note": "Throughout galaxy halo"},
            "coordinates": {"ra": "distributed", "dec": "distributed"},
            "galaxy_reference": "Milky Way",
            "location": "Galactic halo and disk",
            "abundance": {"value": 1e6, "unit": "solar_masses_per_pc³"},
        },
        "physical": {
            "mass": {"value": 1e-16, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 1.5e-10, "unit": "meters"},
            "hawking_temperature": {"value": 1e16, "unit": "K"},
            "hawking_radiation_power": {"value": 1e13, "unit": "watts"},
            "evaporation_timescale": {"value": 1e10, "unit": "years"},
            "density": {"value": 1e80, "unit": "kg/m³"},
            "gravitational_cross_section": {"value": 1e-30, "unit": "m²"},
            "microlensing_amplification": {"value": 1.1, "unit": "magnification"},
        },
        "detailed_description": (
            "The Dark Matter Candidate Primordial Black Hole represents a theoretical solution to the dark "
            "matter problem - microscopic black holes that formed in the early universe and now make up a "
            "significant fraction of the universe's missing mass. These exotic objects would have formed "
            "just 10^-23 seconds after the Big Bang during periods of rapid density fluctuations, collapsing "
            "directly from matter rather than from stellar evolution. Each primordial black hole would have a "
            "mass of only 10^-16 solar masses - smaller than a mountain - but with a Schwarzschild radius of "
            "just 1.5×10^-10 meters, making them truly microscopic. Despite their tiny size, these objects "
            "would have enormous densities of 10^80 kg/m³ and would emit Hawking radiation at temperatures "
            "of 10^16 K, making them among the hottest objects in the universe. The Hawking radiation would "
            "cause them to gradually evaporate over timescales of 10^10 years, potentially making them observable "
            "through gamma-ray bursts as they complete their evaporation. These primordial black holes would be "
            "distributed throughout the Milky Way's halo and disk, with an abundance that could account for "
            "all of the galaxy's dark matter. Their gravitational effects would be detectable through microlensing "
            "events, where they briefly magnify background stars as they pass in front of them. The existence "
            "of these objects would revolutionize our understanding of dark matter and provide direct evidence "
            "for physics in the extreme conditions of the early universe."
        ),
        "scientific_facts": [
            "Primordial black holes could solve the dark matter problem.",
            "These objects formed just 10^-23 seconds after the Big Bang.",
            "Each black hole has a mass of only 10^-16 solar masses.",
            "The objects emit Hawking radiation at 10^16 K.",
            "Primordial black holes evaporate over 10^10 year timescales.",
            "The objects have densities of 10^80 kg/m³.",
            "These black holes could be detected through microlensing events.",
            "The objects formed from density fluctuations in the early universe.",
            "Primordial black holes are distributed throughout the galaxy.",
            "The objects' Hawking radiation could produce gamma-ray bursts.",
            "These black holes provide insights into early universe physics.",
            "Primordial black holes represent a solution to the missing mass problem.",
        ],
        "formation_process": (
            "Primordial black holes formed during the first fractions of a second after the Big Bang when "
            "density fluctuations in the early universe became large enough to overcome radiation pressure and "
            "collapse directly into black holes, bypassing stellar evolution entirely."
        ),
        "future_evolution": (
            "Primordial black holes will continue to evaporate through Hawking radiation, gradually losing mass "
            "until they eventually disappear in a final burst of high-energy radiation. The rate of evaporation "
            "depends on their initial mass and the fundamental physics governing Hawking radiation."
        ),
        "related_objects": ["Dark Matter Halos", "Hawking Radiation", "Early Universe", "Microlensing Events"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Hawking Radiation Emissions", "Microlensing Events", "Gamma-Ray Bursts"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "primordial-black-hole-supermassive")),
        "name": "Supermassive Primordial Black Hole",
        "category": "Primordial Black Hole",
        "subtype": "Direct Collapse Black Hole",
        "tags": ["primordial-black-hole", "supermassive", "direct-collapse", "early-universe", "seed-black-hole"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 13.0e9, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Early universe location"},
            "galaxy_reference": "Early Universe",
            "location": "First galaxies",
            "formation_redshift": {"value": 20, "unit": "z"},
        },
        "physical": {
            "mass": {"value": 1e5, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 3e8, "unit": "meters"},
            "formation_time": {"value": 100, "unit": "million_years"},
            "accretion_rate": {"value": 1, "unit": "solar_masses/year"},
            "growth_timescale": {"value": 1e8, "unit": "years"},
            "density": {"value": 1e15, "unit": "kg/m³"},
            "gravitational_radius": {"value": 1.5, "unit": "AU"},
            "escape_velocity": {"value": 0.8, "unit": "c"},
        },
        "detailed_description": (
            "The Supermassive Primordial Black Hole represents a theoretical solution to the mystery of how "
            "supermassive black holes formed so early in cosmic history - black holes with masses of 10^5 solar "
            "masses that formed directly from the collapse of massive gas clouds in the early universe, bypassing "
            "stellar evolution entirely. These exotic objects would have formed just 100 million years after the "
            "Big Bang at redshifts of 20, when the universe was still mostly neutral hydrogen and helium. The "
            "direct collapse process would occur when massive gas clouds with temperatures of 10,000 K became "
            "gravitationally unstable and collapsed directly into black holes without fragmenting into stars. "
            "Each supermassive primordial black hole would have a Schwarzschild radius of 3×10^8 meters - "
            "larger than the Sun - and would immediately begin accreting surrounding gas at rates of one solar "
            "mass per year. These objects would serve as seeds for the supermassive black holes we observe in "
            "the centers of galaxies, growing to billions of solar masses over billions of years. The existence "
            "of such objects would solve the timing problem of how supermassive black holes could form so early "
            "in cosmic history. These primordial black holes would have enormous densities of 10^15 kg/m³ and "
            "escape velocities of 0.8 times the speed of light at their surfaces. The Supermassive Primordial "
            "Black Hole represents a crucial link between the physics of the early universe and the growth of "
            "the largest structures we observe today."
        ),
        "scientific_facts": [
            "Supermassive primordial black holes have masses of 10^5 solar masses.",
            "These objects formed just 100 million years after the Big Bang.",
            "The black holes formed through direct collapse of gas clouds.",
            "Each object has a Schwarzschild radius larger than the Sun.",
            "Supermassive primordial black holes serve as seeds for galaxy black holes.",
            "The objects formed at redshifts of 20 in the early universe.",
            "These black holes accrete matter at one solar mass per year.",
            "The objects have densities of 10^15 kg/m³.",
            "Supermassive primordial black holes solve the early black hole formation problem.",
            "The objects have escape velocities of 0.8 times the speed of light.",
            "These black holes bypass stellar evolution entirely.",
            "Supermassive primordial black holes represent early universe physics.",
        ],
        "formation_process": (
            "Supermassive primordial black holes formed through the direct collapse of massive gas clouds in "
            "the early universe. When radiation cooling was inefficient, gas clouds could collapse directly "
            "into black holes without fragmenting into stars, creating massive seed black holes."
        ),
        "future_evolution": (
            "Supermassive primordial black holes will continue to grow through accretion and mergers, eventually "
            "becoming the supermassive black holes that power quasars and reside in galaxy centers. They will "
            "play crucial roles in galaxy formation and evolution through their gravitational influence."
        ),
        "related_objects": ["Supermassive Black Holes", "Early Universe", "Direct Collapse", "Quasar Formation"],
        "parent_system": "Early Universe",
        "child_objects": ["Accretion Disks", "Relativistic Jets", "Host Galaxies"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 4: AXION STARS - THEORETICAL DARK MATTER OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "axion-star-dark-matter")),
        "name": "Axion Star Dark Matter Object",
        "category": "Axion Star",
        "subtype": "Bose-Einstein Condensate Dark Matter",
        "tags": ["axion-star", "dark-matter", "bose-einstein-condensate", "theoretical-particle", "quantum-object"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": "distributed", "unit": "ly", "note": "Throughout galaxy halo"},
            "coordinates": {"ra": "distributed", "dec": "distributed"},
            "galaxy_reference": "Milky Way",
            "location": "Galactic halo",
            "abundance": {"value": 1e8, "unit": "objects_per_kpc³"},
        },
        "physical": {
            "mass": {"value": 1e-13, "unit": "solar_masses"},
            "radius": {"value": 1e9, "unit": "meters"},
            "density": {"value": 1e-10, "unit": "kg/m³"},
            "axion_mass": {"value": 1e-5, "unit": "eV/c²"},
            "particle_count": {"value": 1e50, "unit": "axions"},
            "coherence_length": {"value": 1e3, "unit": "meters"},
            "oscillation_frequency": {"value": 2.4e9, "unit": "GHz"},
            "decoherence_timescale": {"value": 1e6, "unit": "years"},
        },
        "detailed_description": (
            "The Axion Star Dark Matter Object represents one of the most exotic forms of matter in the universe - "
            "a macroscopic quantum object composed entirely of axions, theoretical particles that could solve the "
            "dark matter problem. These hypothetical objects would be Bose-Einstein condensates of axions, with "
            "all particles occupying the same quantum state and behaving as a single quantum wave. Each axion star "
            "would contain approximately 10^50 axions with a total mass of 10^-13 solar masses, making them extremely "
            "light but spread over a radius of 10^9 meters - larger than the Sun. The axions would have individual "
            "masses of only 10^-5 eV/c², making them millions of times lighter than electrons, but their collective "
            "behavior would create a stable, self-gravitating object. The axion star would oscillate at frequencies "
            "determined by the axion mass, producing electromagnetic radiation in the gigahertz range that could be "
            "detectable by radio telescopes. These objects would be distributed throughout the Milky Way's halo with "
            "an abundance of 10^8 objects per cubic kiloparsec, potentially accounting for all of the galaxy's dark "
            "matter. The axion star's quantum nature would give it unique properties, including the ability to "
            "pass through normal matter with minimal interaction while maintaining its coherence over astronomical "
            "timescales. The existence of axion stars would revolutionize our understanding of dark matter and provide "
            "direct evidence for physics beyond the Standard Model."
        ),
        "scientific_facts": [
            "Axion stars contain 10^50 axions in a single quantum state.",
            "Each axion star has a mass of 10^-13 solar masses.",
            "The objects have radii larger than the Sun despite their low mass.",
            "Axion stars oscillate at gigahertz frequencies.",
            "The objects are Bose-Einstein condensates of dark matter particles.",
            "Axion stars could account for all of the galaxy's dark matter.",
            "The axions have masses of only 10^-5 eV/c².",
            "These objects pass through normal matter with minimal interaction.",
            "Axion stars maintain quantum coherence over astronomical timescales.",
            "The objects are distributed throughout the galactic halo.",
            "Axion stars provide evidence for physics beyond the Standard Model.",
            "These objects could be detected through radio emissions.",
        ],
        "formation_process": (
            "Axion stars would form through gravitational cooling and Bose-Einstein condensation of axion dark "
            "matter in the early universe. As axions accumulated in overdense regions, they would settle into the "
            "lowest energy quantum state, forming a macroscopic quantum object."
        ),
        "future_evolution": (
            "Axion stars will continue to exist as stable quantum objects for billions of years. They may occasionally "
            "interact with normal matter or merge with other axion stars, but their quantum nature makes them "
            "extremely stable and long-lived."
        ),
        "related_objects": ["Dark Matter Halos", "Axion Particles", "Bose-Einstein Condensates", "Quantum Objects"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Axion Clouds", "Quantum Oscillations", "Radio Emissions"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "axion-star-oscillation")),
        "name": "Oscillating Axion Star",
        "category": "Axion Star",
        "subtype": "Pulsating Bose-Einstein Condensate",
        "tags": ["axion-star", "oscillation", "bose-einstein", "radio-emission", "dark-matter"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 1000, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Hypothetical nearby object"},
            "galaxy_reference": "Milky Way",
            "location": "Local galactic neighborhood",
            "oscillation_amplitude": {"value": 0.1, "unit": "fractional_radius"},
        },
        "physical": {
            "mass": {"value": 1e-12, "unit": "solar_masses"},
            "radius": {"value": 5e8, "unit": "meters"},
            "oscillation_period": {"value": 1e-7, "unit": "seconds"},
            "radio_power": {"value": 1e20, "unit": "watts"},
            "frequency": {"value": 2.4e9, "unit": "Hz"},
            "coherence_time": {"value": 1e-3, "unit": "seconds"},
            "magnetic_coupling": {"value": 1e-20, "unit": "dimensionless"},
            "conversion_probability": {"value": 1e-15, "unit": "probability"},
        },
        "detailed_description": (
            "The Oscillating Axion Star is a theoretical dark matter object that pulsates with extreme regularity "
            "and converts axions into electromagnetic radiation, potentially making it detectable by radio telescopes. "
            "This exotic object would be a Bose-Einstein condensate of axions that undergoes collective oscillations "
            "with periods of 10^-7 seconds, corresponding to frequencies in the gigahertz range. The axion star would "
            "have a mass of 10^-12 solar masses spread over a radius of 5×10^8 meters, with oscillation amplitudes "
            "of 10% of its radius. These oscillations would cause the axions to convert into photons through the "
            "axion-photon coupling mechanism in the presence of magnetic fields, producing radio waves with a power "
            "output of 10^20 watts. The radio emission would be coherent and highly monochromatic, making it "
            "distinguishable from normal astrophysical sources. The oscillating axion star would maintain quantum "
            "coherence for milliseconds at a time, during which it would emit a burst of radio radiation before "
            "decohering and re-establishing its quantum state. The conversion probability of axions to photons "
            "would be extremely low at 10^-15, but the enormous number of axions in the star would make the "
            "emission detectable. This object represents a potential solution to both the dark matter problem and "
            "the mystery of certain unexplained radio signals observed in the galaxy. The Oscillating Axion Star "
            "serves as a crucial target for dark matter detection experiments and could provide direct evidence "
            "for the existence of axions."
        ),
        "scientific_facts": [
            "Oscillating axion stars emit radio waves at gigahertz frequencies.",
            "The objects oscillate with periods of 10^-7 seconds.",
            "Each star converts axions to photons with 10^20 watts of power.",
            "The objects maintain quantum coherence for milliseconds.",
            "Oscillating axion stars have masses of 10^-12 solar masses.",
            "The axion-photon conversion probability is 10^-15.",
            "These objects could solve the dark matter detection problem.",
            "The star's oscillations create coherent radio emissions.",
            "Oscillating axion stars have radii of 5×10^8 meters.",
            "The objects represent Bose-Einstein condensates of dark matter.",
            "These stars could explain unexplained radio signals.",
            "Oscillating axion stars provide evidence for axion physics.",
        ],
        "formation_process": [
            "Oscillating axion stars would form when axion dark matter undergoes gravitational collapse and "
            "Bose-Einstein condensation, followed by the development of collective oscillation modes. The "
            "oscillations would be driven by the axion self-interaction potential and external magnetic fields."
        ],
        "future_evolution": [
            "Oscillating axion stars will continue to pulsate and emit radio radiation for billions of years. "
            "They may gradually lose mass through axion-photon conversion, but this process is extremely slow "
            "and the objects are essentially stable over cosmic timescales."
        ],
        "related_objects": ["Axion Stars", "Radio Sources", "Dark Matter Detection", "Bose-Einstein Condensates"],
        "parent_system": "Milky Way Galaxy",
        "child_objects": ["Radio Emissions", "Quantum Oscillations", "Axion-Photon Conversion"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

]

# -------------------------------------------------------------------------
# PHASE 5: COSMIC OBJECTS - THEORETICAL CONSTRUCTS AND EXTREME EXAMPLES
# -------------------------------------------------------------------------

import uuid

COSMIC_OBJECTS_PHASE5 = [

    # -------------------------------------------------------------------------
    # SECTION 1: NEWLY DISCOVERED EXOTIC OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "fast-radio-burst-repeater-2019")),
        "name": "FRB 20190520B",
        "category": "Fast Radio Burst",
        "subtype": "Persistent Repeating FRB with Compact Source",
        "tags": ["frb", "repeating", "persistent-source", "magnetar", "new-discovery"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 3.0e9, "unit": "ly"},
            "coordinates": {"ra": "16h 24m 51.5s", "dec": "+04° 35' 21\""},
            "galaxy_reference": "Unknown host galaxy",
            "location": "Ophiuchus constellation",
            "redshift": {"value": 0.66, "unit": "z"},
        },
        "physical": {
            "burst_energy": {"value": 1e39, "unit": "ergs"},
            "burst_duration": {"value": 1, "unit": "milliseconds"},
            "burst_rate": {"value": 10, "unit": "bursts/hour"},
            "persistent_luminosity": {"value": 1e32, "unit": "erg/s"},
            "rotation_period": {"value": 1, "unit": "seconds", "note": "Estimated"},
            "magnetic_field": {"value": 1e15, "unit": "gauss"},
            "dispersion_measure": {"value": 1200, "unit": "pc/cm³"},
            "scattering_timescale": {"value": 10, "unit": "milliseconds"},
        },
        "detailed_description": (
            "FRB 20190520B is a remarkable fast radio burst discovered in 2019 that represents a new class of "
            "repeating FRBs with persistent radio sources, challenging our understanding of these mysterious phenomena. "
            "Located 3 billion light-years away in Ophiuchus, this object bursts ten times per hour with energies "
            "of 10^39 ergs per burst, making it one of the most active FRBs known. What makes FRB 20190520B "
            "exceptional is its persistent radio emission with a luminosity of 10^32 erg/s, suggesting a compact "
            "object like a young magnetar powering the bursts. The source shows a high dispersion measure of "
            "1,200 pc/cm³, indicating it resides in a dense environment, possibly within a star-forming region "
            "or supernova remnant. The bursts last only 1 millisecond but show complex frequency structure and "
            "significant scattering, suggesting propagation through dense plasma. FRB 20190520B's discovery has "
            "important implications for understanding FRB origins, as it bridges the gap between repeating FRBs "
            "with persistent sources and those without. The object's high activity rate and persistent emission "
            "make it an ideal laboratory for studying FRB physics and the extreme conditions in magnetar "
            "environments. This source provides crucial insights into the relationship between FRBs and magnetars, "
            "and may represent an evolutionary phase in the life of highly magnetized neutron stars. FRB 20190520B "
            "continues to be extensively monitored, providing unprecedented data on FRB behavior and variability."
        ),
        "scientific_facts": [
            "FRB 20190520B bursts 10 times per hour, making it extremely active.",
            "The source has persistent radio emission, unlike most FRBs.",
            "The bursts have energies of 10^39 ergs per millisecond.",
            "FRB 20190520B has a high dispersion measure of 1,200 pc/cm³.",
            "The source likely resides in a dense environment.",
            "FRB 20190520B represents a new class of repeating FRBs.",
            "The object may be powered by a young magnetar.",
            "The bursts show significant frequency structure.",
            "FRB 20190520B was discovered in 2019 by the CHIME telescope.",
            "The source provides insights into FRB origins and magnetar physics.",
            "FRB 20190520B continues to be extensively monitored.",
            "The object bridges different classes of FRBs.",
        ],
        "formation_process": (
            "FRB 20190520B likely formed from a young magnetar created in a recent supernova or through "
            "magnetically-induced collapse. The persistent radio emission suggests ongoing energy injection "
            "from the magnetar's spin-down or magnetic field decay."
        ),
        "future_evolution": (
            "FRB 20190520B will continue its burst activity for thousands of years as the magnetar gradually "
            "spins down and its magnetic field weakens. The persistent emission may fade over time as the "
            "source evolves into a less active phase."
        ),
        "related_objects": ["FRB 121102", "SGR 1935+2154", "Magnetars", "Fast Radio Bursts"],
        "parent_system": "Unknown Host Galaxy",
        "child_objects": ["Radio Bursts", "Persistent Source", "Magnetar Magnetosphere"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 2: EXTREAME SIMULATED OBJECTS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "simulated-quark-star-merger")),
        "name": "Quark Star Merger Remnant",
        "category": "Simulated Object",
        "subtype": "Binary Quark Star Coalescence",
        "tags": ["simulated", "quark-star", "merger", "strange-matter", "extreme-physics"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": "simulated", "unit": "N/A"},
            "coordinates": {"ra": "simulated", "dec": "simulated"},
            "galaxy_reference": "Simulated Environment",
            "location": "Computer Simulation",
            "simulation_time": {"value": 1e-3, "unit": "seconds"},
        },
        "physical": {
            "total_mass": {"value": 5, "unit": "solar_masses"},
            "quark_density": {"value": 1e15, "unit": "g/cm³"},
            "temperature": {"value": 1e12, "unit": "K"},
            "gravitational_wave_strain": {"value": 1e-21, "unit": "dimensionless"},
            "merger_timescale": {"value": 1e-4, "unit": "seconds"},
            "neutrino_luminosity": {"value": 1e54, "unit": "erg/s"},
            "magnetic_field": {"value": 1e18, "unit": "gauss"},
            "escape_velocity": {"value": 0.6, "unit": "c"},
        },
        "detailed_description": (
            "The Quark Star Merger Remnant is a simulated object representing the coalescence of two quark stars - "
            "hypothetical objects composed entirely of deconfined quark matter in a state known as strange matter. "
            "This computer simulation models the extreme physics that would occur when two quark stars, each with "
            "masses of 2.5 solar masses, spiral together and merge over a timescale of 10^-4 seconds. The merger "
            "creates conditions of unimaginable density (10^15 g/cm³) and temperature (10^12 K), far exceeding "
            "anything found in normal neutron stars. The simulation predicts the emission of gravitational waves "
            "with strains of 10^-21, potentially detectable by gravitational wave observatories. The merger also "
            "produces an enormous neutrino luminosity of 10^54 erg/s and generates magnetic fields of 10^18 gauss, "
            "the strongest fields possible in the universe. The resulting remnant would have a total mass of 5 "
            "solar masses and an escape velocity of 0.6 times the speed of light at its surface. This simulated "
            "object provides insights into the physics of strange matter and the behavior of quark-gluon plasma "
            "under extreme conditions. The Quark Star Merger Remnant represents a theoretical laboratory for "
            "studying quantum chromodynamics in the strong-field regime and testing our understanding of the "
            "fundamental forces of nature. The simulation helps predict observational signatures that could confirm "
            "the existence of quark stars and strange matter in the universe."
        ),
        "scientific_facts": [
            "The quark star merger creates densities of 10^15 g/cm³.",
            "The merger occurs over 10^-4 seconds.",
            "The object produces gravitational waves detectable by observatories.",
            "The merger generates magnetic fields of 10^18 gauss.",
            "The remnant has a total mass of 5 solar masses.",
            "The simulation predicts neutrino luminosities of 10^54 erg/s.",
            "The object reaches temperatures of 10^12 K.",
            "The remnant has an escape velocity of 0.6 times the speed of light.",
            "Quark stars are composed entirely of deconfined quark matter.",
            "The merger provides insights into quantum chromodynamics.",
            "The simulation tests fundamental physics in extreme conditions.",
            "The object represents a theoretical laboratory for strange matter physics.",
        ],
        "formation_process": (
            "The quark star merger would occur when two quark stars in a binary system lose energy through "
            "gravitational wave emission and spiral together until they collide and merge. The merger creates "
            "a hypermassive quark star that may either stabilize or collapse into a black hole."
        ),
        "future_evolution": (
            "The merger remnant would either stabilize as a hypermassive quark star or collapse into a black "
            "hole. If stable, it would gradually cool and spin down over billions of years. If collapsing, it "
            "would produce a burst of gravitational waves and potentially a short gamma-ray burst."
        ),
        "related_objects": ["Quark Stars", "Neutron Star Mergers", "Strange Matter", "Gravitational Wave Sources"],
        "parent_system": "Computer Simulation",
        "child_objects": ["Gravitational Waves", "Neutrino Emissions", "Magnetic Fields"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "simulated-wormhole-throat")),
        "name": "Traversable Wormhole Throat",
        "category": "Simulated Object",
        "subtype": "Morris-Thorne Wormhole",
        "tags": ["simulated", "wormhole", "exotic-matter", "general-relativity", "faster-than-light"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": "simulated", "unit": "N/A"},
            "coordinates": {"ra": "simulated", "dec": "simulated"},
            "galaxy_reference": "Theoretical Spacetime",
            "location": "Computer Simulation",
            "throat_radius": {"value": 10, "unit": "meters"},
        },
        "physical": {
            "exotic_matter_density": {"value": -1e20, "unit": "kg/m³"},
            "negative_pressure": {"value": -1e35, "unit": "Pa"},
            "throat_length": {"value": 1, "unit": "meter"},
            "tidal_acceleration": {"value": 1, "unit": "m/s²"},
            "traversal_time": {"value": 1e-6, "unit": "seconds"},
            "energy_requirement": {"value": 1e45, "unit": "joules"},
            "stability_factor": {"value": 0.1, "unit": "dimensionless"},
            "causality_violation": {"value": "possible", "unit": "theoretical"},
        },
        "detailed_description": (
            "The Traversable Wormhole Throat is a simulated object representing the narrowest region of a "
            "Morris-Thorne wormhole - a hypothetical shortcut through spacetime that could allow faster-than-light "
            "travel. This computer simulation models a wormhole with a throat radius of 10 meters, maintained open "
            "by exotic matter with negative energy density of -10^20 kg/m³. The exotic matter violates the energy "
            "conditions of general relativity, creating the negative pressure (-10^35 Pa) necessary to keep the "
            "wormhole throat from collapsing. The simulation shows that the throat length would be only 1 meter, "
            "making the wormhole essentially a portal between distant regions of spacetime. The tidal acceleration "
            "at the throat would be only 1 m/s², making traversal potentially survivable for humans. The simulation "
            "predicts a traversal time of 10^-6 seconds - essentially instantaneous from the traveler's perspective. "
            "However, the energy requirement to create and maintain such a wormhole would be enormous - 10^45 joules, "
            "equivalent to the total energy output of a star over millions of years. The wormhole's stability factor "
            "of 0.1 indicates it would be marginally stable, requiring continuous energy input to prevent collapse. "
            "This simulated object provides insights into the theoretical possibility of faster-than-light travel "
            "and the extreme physics required for such phenomena. The Traversable Wormhole Throat represents a "
            "theoretical laboratory for exploring the limits of general relativity and the fundamental nature "
            "of spacetime itself."
        ),
        "scientific_facts": [
            "The wormhole throat requires exotic matter with negative energy density.",
            "The throat radius is 10 meters with a length of 1 meter.",
            "The wormhole would allow traversal in 10^-6 seconds.",
            "The energy requirement is 10^45 joules to create.",
            "The tidal acceleration at the throat is only 1 m/s².",
            "The exotic matter has negative pressure of -10^35 Pa.",
            "The wormhole is marginally stable with a factor of 0.1.",
            "The object represents a theoretical faster-than-light travel method.",
            "The simulation tests the limits of general relativity.",
            "The wormhole throat could potentially be traversable by humans.",
            "The object provides insights into spacetime physics.",
            "The wormhole represents a theoretical laboratory for exotic physics.",
        ],
        "formation_process": (
            "A traversable wormhole would theoretically form through the manipulation of spacetime using exotic "
            "matter with negative energy density. This would require advanced technology far beyond current "
            "capabilities to create and maintain the necessary spacetime curvature."
        ),
        "future_evolution": (
            "If created, a traversable wormhole would require continuous energy input to maintain stability. "
            "Without this maintenance, the throat would collapse, potentially creating a black hole or returning "
            "to normal spacetime."
        ),
        "related_objects": ["Black Holes", "Exotic Matter", "General Relativity", "Spacetime Geometry"],
        "parent_system": "Theoretical Physics",
        "child_objects": ["Exotic Matter Fields", "Spacetime Curvature", "Energy Requirements"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/cosmology/",
    },

    # -------------------------------------------------------------------------
    # SECTION 3: EDGE-CASE PHENOMENA - EXTREAME PHYSICS
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "extreme-magnetar-giant-flare")),
        "name": "Magnetar Giant Flare at 50 Mpc",
        "category": "Edge-Case Phenomenon",
        "subtype": "Extragalactic Magnetar Giant Flare",
        "tags": ["magnetar", "giant-flare", "extragalactic", "extreme-energy", "edge-case"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 1.5e8, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Hypothetical location"},
            "galaxy_reference": "Nearby Galaxy",
            "location": "Unknown galaxy",
            "host_galaxy_type": {"value": "starburst", "note": "Likely environment"},
        },
        "physical": {
            "flare_energy": {"value": 1e47, "unit": "ergs"},
            "peak_luminosity": {"value": 1e48, "unit": "erg/s"},
            "burst_duration": {"value": 0.2, "unit": "seconds"},
            "magnetic_field": {"value": 1e16, "unit": "gauss"},
            "gamma-ray_energy": {"value": 1e46, "unit": "ergs"},
            "fireball_expansion": {"value": 0.9, "unit": "c"},
            "afterglow_duration": {"value": 100, "unit": "seconds"},
            "neutrino_flux": {"value": 1e10, "unit": "neutrinos/cm²"},
        },
        "detailed_description": (
            "The Magnetar Giant Flare at 50 Mpc represents an edge-case phenomenon where a magnetar in a nearby "
            "galaxy produces a giant flare so powerful that it could be detected across intergalactic distances. "
            "This hypothetical event would release 10^47 ergs of energy in just 0.2 seconds, reaching a peak "
            "luminosity of 10^48 erg/s - equivalent to the brightness of 100 billion galaxies. The flare would "
            "be powered by a magnetar with an extreme magnetic field of 10^16 gauss, the strongest possible in "
            "the universe. The star's crust would crack and rearrange, releasing enormous magnetic energy that "
            "creates a fireball expanding at 0.9 times the speed of light. The event would emit a burst of gamma "
            "rays with 10^46 ergs of energy, potentially detectable by gamma-ray observatories across 150 million "
            "light-years. The flare would also produce a neutrino flux of 10^10 neutrinos per square centimeter, "
            "providing a unique probe of the physics of extreme magnetic fields. The afterglow would last for "
            "100 seconds as the fireball cools and expands. This edge-case phenomenon would challenge our "
            "understanding of magnetar physics and the limits of magnetic energy release. The Magnetar Giant Flare "
            "at 50 Mpc represents a crucial test of theories about the most extreme magnetic phenomena in the "
            "universe and could provide insights into the physics of matter under conditions impossible to recreate "
            "on Earth. Such an event would be extremely rare but would provide unprecedented information about "
            "magnetars and the behavior of matter in ultra-strong magnetic fields."
        ),
        "scientific_facts": [
            "The magnetar flare releases 10^47 ergs in 0.2 seconds.",
            "The peak luminosity equals 100 billion galaxies.",
            "The magnetar has a magnetic field of 10^16 gauss.",
            "The fireball expands at 0.9 times the speed of light.",
            "The event could be detected across 150 million light-years.",
            "The flare produces a neutrino flux of 10^10 neutrinos/cm².",
            "The afterglow lasts for 100 seconds.",
            "The event represents an extreme magnetar phenomenon.",
            "The flare challenges our understanding of magnetic energy release.",
            "The object provides insights into extreme physics.",
            "The event would be extremely rare but detectable.",
            "The magnetar flare represents an edge-case in stellar physics.",
        ],
        "formation_process": (
            "The giant flare would occur when a magnetar's ultra-strong magnetic field causes sudden cracking "
            "and rearrangement of the star's crust, releasing enormous magnetic energy in a fraction of a second. "
            "This represents the most extreme form of magnetic energy release possible."
        ),
        "future_evolution": (
            "After the flare, the magnetar would gradually return to its normal state over weeks to months. "
            "The star's magnetic field would be slightly weakened, and it would continue to spin down and "
            "produce smaller bursts for thousands of years."
        ),
        "related_objects": ["SGR 1806-20", "Magnetars", "Gamma-Ray Bursts", "Neutron Stars"],
        "parent_system": "Nearby Galaxy",
        "child_objects": ["Magnetic Fireball", "Gamma-Ray Burst", "Neutrino Flux"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "extreme-white-dwarf-merger")),
        "name": "Super-Chandrasekhar White Dwarf Merger",
        "category": "Edge-Case Phenomenon",
        "subtype": "White Dwarf Merger Exceeding Chandrasekhar Limit",
        "tags": ["white-dwarf", "merger", "super-chandrasekhar", "type-ia-supernova", "edge-case"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 100e6, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Hypothetical location"},
            "galaxy_reference": "Elliptical Galaxy",
            "location": "Galaxy center",
            "stellar_population": {"value": "old", "note": "Typical environment"},
        },
        "physical": {
            "combined_mass": {"value": 2.5, "unit": "solar_masses"},
            "merger_timescale": {"value": 1000, "unit": "years"},
            "central_density": {"value": 1e10, "unit": "g/cm³"},
            "temperature": {"value": 1e9, "unit": "K"},
            "carbon_oxygen_ratio": {"value": 1, "unit": "dimensionless"},
            "rotation_period": {"value": 10, "unit": "seconds"},
            "magnetic_field": {"value": 1e9, "unit": "gauss"},
            "explosion_energy": {"value": 2e51, "unit": "ergs"},
        },
        "detailed_description": (
            "The Super-Chandrasekhar White Dwarf Merger represents an edge-case phenomenon where two white dwarfs "
            "merge to create a single object exceeding the theoretical Chandrasekhar limit of 1.4 solar masses. "
            "This hypothetical event would occur over 1,000 years as two white dwarfs spiral together through "
            "gravitational wave emission, eventually merging into a single super-massive white dwarf of 2.5 solar "
            "masses. The merged object would have an extreme central density of 10^10 g/cm³ and a temperature of "
            "10^9 K, conditions never before observed in white dwarfs. The object would rotate rapidly with a "
            "period of 10 seconds and generate magnetic fields of 10^9 gauss through dynamo processes. The "
            "super-Chandrasekhar white dwarf would be supported against collapse by its rapid rotation and "
            "possibly by the energy released from carbon fusion in its core. Eventually, the object would undergo "
            "a thermonuclear explosion with 2×10^51 ergs of energy - twice that of a typical Type Ia supernova. "
            "This edge-case phenomenon challenges our understanding of white dwarf physics and the limits of stellar "
            "evolution. The Super-Chandrasekhar White Dwarf Merger provides insights into the diversity of "
            "supernova explosions and the physics of matter under extreme conditions. Such events could explain "
            "over-luminous supernovae observed in distant galaxies and provide constraints on the physics of "
            "degenerate matter and nuclear burning at high densities."
        ),
        "scientific_facts": [
            "The merger creates a 2.5 solar mass white dwarf.",
            "The object exceeds the Chandrasekhar limit by 80%.",
            "The merger occurs over 1,000 years.",
            "The central density reaches 10^10 g/cm³.",
            "The object rotates with a 10-second period.",
            "The eventual explosion releases 2×10^51 ergs.",
            "The merger generates magnetic fields of 10^9 gauss.",
            "The object is supported by rapid rotation against collapse.",
            "The phenomenon challenges white dwarf physics.",
            "The event could explain over-luminous supernovae.",
            "The merger provides insights into extreme stellar evolution.",
            "The object represents an edge-case in stellar physics.",
        ],
        "formation_process": (
            "The merger would occur when two white dwarfs in a close binary system lose energy through "
            "gravitational wave emission and spiral together. The merger creates a super-massive white dwarf "
            "that can temporarily exceed the Chandrasekhar limit through rotational support."
        ),
        "future_evolution": (
            "The super-Chandrasekhar white dwarf would eventually explode as an over-luminous Type Ia "
            "supernova when carbon fusion ignites throughout the object. The explosion would completely "
            "disrupt the star and eject heavy elements into the surrounding space."
        ),
        "related_objects": ["Type Ia Supernovae", "White Dwarfs", "Binary Star Systems", "Chandrasekhar Limit"],
        "parent_system": "Elliptical Galaxy",
        "child_objects": ["Gravitational Waves", "Carbon Fusion", "Supernova Explosion"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/black-holes-and-neutron-stars/",
    },

    # -------------------------------------------------------------------------
    # SECTION 4: HYPOTHETICAL FUTURE DISCOVERIES
    # -------------------------------------------------------------------------

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "hypothetical-dark-matter-star")),
        "name": "Dark Matter Powered Star",
        "category": "Hypothetical Discovery",
        "subtype": "Star Powered by Dark Matter Annihilation",
        "tags": ["hypothetical", "dark-matter", "star", "annihilation", "future-discovery"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 1e6, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Hypothetical location"},
            "galaxy_reference": "Milky Way",
            "location": "Dark matter halo",
            "dark_matter_density": {"value": 100, "unit": "geV/cm³"},
        },
        "physical": {
            "luminosity": {"value": 1e33, "unit": "erg/s"},
            "mass": {"value": 0.5, "unit": "solar_masses"},
            "temperature": {"value": 5000, "unit": "K"},
            "dark_matter_accretion_rate": {"value": 1e-15, "unit": "solar_masses/year"},
            "annihilation_efficiency": {"value": 0.1, "unit": "fraction"},
            "lifetime": {"value": 1e12, "unit": "years"},
            "spectral_type": {"value": "M", "note": "Cool star"},
            "composition": {"value": "hydrogen", "note": "Normal stellar composition"},
        },
        "detailed_description": (
            "The Dark Matter Powered Star is a hypothetical stellar object that derives most of its energy "
            "from the annihilation of dark matter particles rather than nuclear fusion. This future discovery "
            "would represent a completely new class of stellar objects, powered by the physics of the dark sector. "
            "The star would have a mass of only 0.5 solar masses but would shine with a luminosity of 10^33 erg/s, "
            "equivalent to about 0.01% of the Sun's brightness. The star's surface temperature would be 5,000 K, "
            "giving it a cool M-type spectral appearance despite being powered by dark matter. The star would "
            "accrete dark matter at a rate of 10^-15 solar masses per year from the surrounding dark matter halo, "
            "with an annihilation efficiency of 10% converting dark matter mass to energy. This process would "
            "provide a steady energy source that could sustain the star for 10^12 years - far longer than the "
            "10^10 year lifetime of normal stars. The star would have a normal composition of hydrogen and helium "
            "but would not need nuclear fusion to maintain its luminosity. The discovery of such an object would "
            "revolutionize our understanding of both stellar evolution and dark matter physics. The Dark Matter "
            "Powered Star would provide direct evidence for the nature of dark matter particles and demonstrate "
            "that dark matter can play an active role in astrophysical processes. This hypothetical discovery "
            "would open new windows into the dark universe and the physics of particle interactions."
        ),
        "scientific_facts": [
            "The star is powered by dark matter annihilation rather than fusion.",
            "The object could live for 10^12 years, 100 times longer than normal stars.",
            "The star accretes dark matter at 10^-15 solar masses per year.",
            "The luminosity is 10^33 erg/s from dark matter energy.",
            "The star has a mass of 0.5 solar masses.",
            "The surface temperature is 5,000 K, giving it an M-type appearance.",
            "The annihilation efficiency is 10% for energy conversion.",
            "The discovery would revolutionize dark matter physics.",
            "The star provides evidence for dark matter particle properties.",
            "The object represents a new class of stellar objects.",
            "The star demonstrates dark matter's role in astrophysics.",
            "The discovery would open new windows into the dark universe.",
        ],
        "formation_process": (
            "Dark matter powered stars would form in regions of unusually high dark matter density, where "
            "normal stellar collapse occurs but the resulting star captures enough dark matter to power its "
            "luminosity through annihilation rather than nuclear fusion."
        ),
        "future_evolution": (
            "The star would continue shining for trillions of years as long as dark matter is available. "
            "Eventually, as the dark matter density decreases, the star would cool and fade, becoming a "
            "dark remnant composed of normal stellar material."
        ),
        "related_objects": ["Normal Stars", "Dark Matter", "Stellar Evolution", "Particle Physics"],
        "parent_system": "Milky Way Dark Matter Halo",
        "child_objects": ["Dark Matter Annihilation", "Stellar Atmosphere", "Dark Matter Accretion"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/dark-energy-dark-matter/",
    },

    {
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "hypothetical-quantum-black-hole")),
        "name": "Quantum Black Hole",
        "category": "Hypothetical Discovery",
        "subtype": "Black Hole with Quantum Gravity Effects",
        "tags": ["hypothetical", "quantum-gravity", "black-hole", "future-discovery", "fundamental-physics"],
        "difficulty_level": "expert",
        "spatial": {
            "distance_from_earth": {"value": 1e9, "unit": "ly"},
            "coordinates": {"ra": "unknown", "dec": "unknown", "note": "Hypothetical location"},
            "galaxy_reference": "Distant Galaxy",
            "location": "Galaxy center",
            "quantum_regime": {"value": "active", "note": "Quantum gravity effects observable"},
        },
        "physical": {
            "mass": {"value": 1e5, "unit": "solar_masses"},
            "schwarzschild_radius": {"value": 3e5, "unit": "km"},
            "planck_scale_effects": {"value": "observable", "note": "At event horizon"},
            "hawking_modification": {"value": 1e-3, "unit": "fraction"},
            "information_retention": {"value": "partial", "note": "Modified Hawking radiation"},
            "quantum_fluctuations": {"value": 1e-20, "unit": "relative"},
            "spacetime_quantization": {"value": "detectable", "note": "Quantum spacetime structure"},
            "entropy_deviation": {"value": 0.1, "unit": "fraction"},
        },
        "detailed_description": (
            "The Quantum Black Hole is a hypothetical discovery that would represent the first direct evidence "
            "for quantum gravity effects at macroscopic scales. This future discovery would be a black hole of "
            "10^5 solar masses where quantum fluctuations in spacetime become observable at the event horizon, "
            "providing a window into the fundamental nature of gravity and spacetime. The black hole would have "
            "a Schwarzschild radius of 300,000 kilometers, but unlike classical black holes, it would exhibit "
            "observable quantum gravity effects that modify its behavior by 10^-3 relative to classical predictions. "
            "The Hawking radiation would be modified from the standard formula, potentially allowing partial "
            "information retention rather than complete loss. Quantum fluctuations of 10^-20 relative amplitude "
            "would create measurable deviations from classical black hole thermodynamics. The spacetime itself "
            "would show evidence of quantization, with discrete structure becoming apparent at the event horizon. "
            "The black hole's entropy would deviate from the standard Bekenstein-Hawking formula by 10%, providing "
            "crucial constraints on theories of quantum gravity. This discovery would revolutionize our understanding "
            "of fundamental physics, providing the first experimental evidence for quantum gravity and helping "
            "resolve the information paradox. The Quantum Black Hole would serve as a natural laboratory for studying "
            "the unification of general relativity and quantum mechanics, potentially leading to a complete theory "
            "of quantum gravity."
        ),
        "scientific_facts": [
            "The black hole shows observable quantum gravity effects.",
            "Quantum fluctuations modify classical predictions by 10^-3.",
            "The Hawking radiation is modified from standard predictions.",
            "The event horizon shows evidence of spacetime quantization.",
            "The black hole's entropy deviates by 10% from classical values.",
            "The object has a mass of 10^5 solar masses.",
            "The discovery would provide evidence for quantum gravity.",
            "The black hole could partially retain information.",
            "The object represents a natural laboratory for fundamental physics.",
            "The discovery could resolve the information paradox.",
            "The black hole demonstrates quantum spacetime structure.",
            "The object would revolutionize our understanding of gravity.",
        ],
        "formation_process": (
            "Quantum black holes would form through the same processes as normal black holes but would "
            "require specific conditions that make quantum gravity effects observable, possibly through "
            "unusual mass ranges or environmental factors that enhance quantum effects."
        ),
        "future_evolution": (
            "The quantum black hole would evolve differently from classical black holes, with modified "
            "Hawking radiation and potentially different long-term behavior. The quantum effects might "
            "lead to new phases of black hole evolution or novel end states."
        ),
        "related_objects": ["Black Holes", "Quantum Gravity", "Event Horizons", "Fundamental Physics"],
        "parent_system": "Distant Galaxy",
        "child_objects": ["Quantum Spacetime", "Modified Hawking Radiation", "Quantum Fluctuations"],
        "nasa_reference": "https://science.nasa.gov/astrophysics/focus-areas/cosmology/",
    },

]
