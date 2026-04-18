# 🌌 Cosmos - Explore the Universe

An interactive encyclopedia for exploring and understanding the cosmos. Discover 169+ cosmic objects including galaxies, nebulae, stars, black holes, and more with rich scientific data and beautiful visualizations.

## 🌟 About Cosmos

Cosmos is a cutting-edge web application that brings the universe to your fingertips. Built with modern web technologies and powered by comprehensive astronomical data, Cosmos makes cosmic exploration accessible to everyone—from casual stargazers to serious astronomers.

## 📸 Screenshots

![ss 1](public/taneli-lahtinen-3G8p__Lv8iM-unsplash.jpg)
![ss 2](public/Ring%20Galaxy.jpg)
![ss 3](public/Neptune.jpg)
![ss 4](public/milky%20way%20galaxy.jpg)

### Why Cosmos?

- 🚀 **Instant Discovery** - Browse 169+ cosmic objects with rich data
- 🔬 **Scientific Accuracy** - Curated information from astronomical databases
- 🎯 **Smart Filtering** - Search by category, difficulty level, and more
- 🔒 **Seamless Experience** - Smooth animations and responsive design
- 📱 **Accessible Everywhere** - Works perfectly on desktop, tablet, and mobile
- 🌍 **Beautiful Dark Theme** - Glassmorphism design with cosmic aesthetics

### Core Functionality

#### 🔍 Cosmic Object Database
- **169+ Cosmic Objects** - Comprehensive collection including:
  - 🌀 Galaxies
  - ⚫ Black Holes
  - ⭐ Stars & Variable Stars
  - 🌫️ Nebulae & Planetary Nebulae
  - 💫 Pulsars & Neutron Stars
  - ✨ Quasars & Blazars
  - 🪐 Exoplanets & Planets
  - 🛸 Space Missions
  - 🌠 Supernova Remnants
  - 🌌 Galaxy Clusters & More
- **Detailed Information** - Each object includes:
  - Scientific description
  - Physical properties (distance, size, mass, temperature)
  - Formation and evolution data
  - Related cosmic objects
  - Did you know facts
  - NASA references

#### 🔎 Advanced Search & Filtering
- **Real-time Search** - Instantly search across all cosmic objects
- **Category Filtering** - Browse by 35+ astronomical categories
- **Difficulty Levels** - Content organized by learning difficulty:
  - Beginner - Perfect for newcomers
  - Intermediate - For enthusiasts
  - Advanced - For serious astronomers
  - Expert - Deep scientific knowledge
- **Pagination** - Smooth browsing with organized pagination
- **Visual Badges** - Color-coded categories and difficulty indicators

#### 🖼️ Rich Visualizations
- **Curated Imagery** - High-quality images for each cosmic object category
- **Responsive Gallery** - Beautiful grid layout with hover animations
- **Smooth Animations** - Framer Motion powered transitions and interactions
- **Dark Theme** - Eye-friendly cosmos-inspired color scheme

#### 📊 Detailed Object Exploration
- **Complete Profile** - Comprehensive data pages for each cosmic object
- **Related Objects** - Discover connections between cosmic entities
- **Spatial Information** - Distance, coordinates, and spatial relationships
- **Physical Properties** - Mass, size, temperature, composition, and more
- **Evolution Timeline** - Formation process and future evolution
- **Scientific Facts** - Fascinating insights and "Did You Know" sections

#### 🌐 Multi-Page Experience
- **Home/Landing Page** - Beautiful introduction to Cosmos
- **Explore Page** - Interactive cosmic object browser
- **About Page** - Learn about Cosmos and its mission
- **Object Details** - Deep dives into individual cosmic objects
- **Legal Pages** - Privacy, Terms, Cookies, and License information
- **Contact Page** - Get in touch with the team

### Additional Features

- ✅ **Responsive Design** - Perfectly adapted for all screen sizes
- ✅ **Fast Performance** - Optimized with Vite for lightning-fast loads
- ✅ **Type-Safe** - Full TypeScript support
- ✅ **Modern UI** - Shadcn/ui components with Tailwind CSS
- ✅ **Client-Side Routing** - TanStack Router for seamless navigation
- ✅ **Data Caching** - Efficient data loading and caching strategies
- ✅ **SEO Optimized** - Meta tags for better search visibility

## 🛠️ Tech Stack

### Frontend

- **React 18** - Modern UI library
- **TypeScript** - Type-safe development
- **Vite** - Lightning-fast build tool and dev server
- **Tailwind CSS** - Utility-first styling
- **TanStack Router** - Modern routing solution
- **Framer Motion** - Smooth animations and transitions
- **Shadcn/ui** - High-quality React components
- **Lucide Icons** - Beautiful SVG icons
- **Radix UI** - Accessible component primitives

### Styling & UI

- **Tailwind CSS v4** - Advanced utility styling with VitePlugin
- **PostCSS** - CSS transformation
- **Class Variance Authority** - Component variant management
- **CLSX** - Conditional className utility

### Data & API

- **TanStack React Query** - Server state management
- **Dynamic Data Loading** - Efficient pagination and caching
- **Backend API** - RESTful API for cosmic object data

## 📁 Project Structure

```
Cosmos/
├── public/                     # Static assets
│   ├── cosmic_data.json       # Cosmic object database
│   └── *.jpg                  # Curated space imagery
├── src/                        # Frontend Application
│   ├── assets/                # Images, icons, and styles
│   ├── components/            # Reusable React components
│   │   ├── ui/               # Shadcn UI primitives (30+ components)
│   │   ├── CosmicCard.tsx    # Cosmic object card component
│   │   ├── StarField.tsx     # Animated starfield background
│   │   └── ThemeToggle.tsx   # Theme switcher
│   ├── hooks/                # Custom React hooks
│   │   └── use-mobile.tsx    # Mobile detection hook
│   ├── lib/                  # Utilities and helpers
│   │   ├── cosmic-data.ts    # Data loading and categories
│   │   └── utils.ts          # Utility functions
│   ├── routes/               # Page components
│   │   ├── __root.tsx        # Root layout
│   │   ├── index.tsx         # Home/Landing page
│   │   ├── explore.index.tsx # Cosmic objects explorer
│   │   ├── explore.$objectId.tsx  # Object detail page
│   │   ├── about.tsx         # About page
│   │   ├── contact.tsx       # Contact page
│   │   ├── privacy.tsx       # Privacy policy
│   │   ├── terms.tsx         # Terms of service
│   │   ├── cookies.tsx       # Cookie policy
│   │   ├── license.tsx       # License information
│   │   ├── faq.tsx           # FAQ page
│   │   └── routeTree.gen.ts  # Auto-generated router
│   ├── styles.css            # Global styles & Tailwind directives
│   ├── entry.client.tsx      # Client entry point
│   ├── router.tsx            # Router configuration
│   └── main.tsx              # Application bootstrap
├── scripts/                    # Utility scripts
├── components.json           # Shadcn UI configuration
├── tsconfig.json             # TypeScript configuration
├── vite.config.ts            # Vite configuration
├── tailwind.config.ts        # Tailwind CSS configuration
├── postcss.config.js         # PostCSS configuration
├── eslint.config.js          # ESLint rules
├── package.json              # NPM dependencies and scripts
├── bunfig.toml               # Bun configuration
├── vercel.json               # Vercel deployment config
└── README.md                 # This file
```

Made with ❤️ By Manas Rohilla

