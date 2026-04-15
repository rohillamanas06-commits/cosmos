import { createFileRoute, Link } from "@tanstack/react-router";
import { useState, useEffect, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, Filter, X, ChevronLeft, ChevronRight } from "lucide-react";
import { loadCosmicData, CATEGORIES, DIFFICULTIES, getCategoryBadgeClass } from "@/lib/cosmic-data";
import type { CosmicObject } from "@/lib/cosmic-data";
import { CosmicCard } from "@/components/CosmicCard";
import { ThemeToggle } from "@/components/ThemeToggle";

export const Route = createFileRoute("/explore/")({
  head: () => ({
    meta: [
      { title: "Explore — Cosmos" },
      { name: "description", content: "Browse and search 169 cosmic objects with filters by category and difficulty." },
      { property: "og:title", content: "Explore — Cosmos" },
      { property: "og:description", content: "Browse and search 169 cosmic objects." },
    ],
  }),
  component: ExplorePage,
});

const PAGE_SIZE = 24;

function ExplorePage() {
  const [objects, setObjects] = useState<CosmicObject[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [selectedDifficulty, setSelectedDifficulty] = useState<string | null>(null);
  const [showFilters, setShowFilters] = useState(false);
  const [page, setPage] = useState(0);

  useEffect(() => {
    loadCosmicData().then((data) => {
      setObjects(data);
      setLoading(false);
    });
  }, []);

  // Apply dark by default for explorer
  useEffect(() => {
    document.documentElement.classList.add("dark");
  }, []);

  const filtered = useMemo(() => {
    let result = objects;
    if (search) {
      const q = search.toLowerCase();
      result = result.filter(
        (o) =>
          o.name.toLowerCase().includes(q) ||
          o.category.toLowerCase().includes(q) ||
          (o.tags && o.tags.some((t) => t.toLowerCase().includes(q)))
      );
    }
    if (selectedCategory) {
      result = result.filter((o) => o.category === selectedCategory);
    }
    if (selectedDifficulty) {
      result = result.filter((o) => o.difficulty_level === selectedDifficulty);
    }
    return result;
  }, [objects, search, selectedCategory, selectedDifficulty]);

  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginated = filtered.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);

  // Reset page when filters change
  useEffect(() => {
    setPage(0);
  }, [search, selectedCategory, selectedDifficulty]);

  const activeCategories = useMemo(() => {
    const cats = new Set(objects.map((o) => o.category));
    return CATEGORIES.filter((c) => cats.has(c));
  }, [objects]);

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-background">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent" />
          <p className="mt-4 text-muted-foreground">Loading cosmic data...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur-xl">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 md:px-6">
          <div className="flex items-center gap-4">
            <Link to="/" className="flex items-center gap-2">
              <div className="w-7 h-7 rounded-full bg-gradient-to-br from-purple-500 to-pink-500" />
              <span className="font-display text-lg font-bold text-foreground">Cosmos</span>
            </Link>
            <span className="hidden sm:inline text-sm text-muted-foreground">
              {filtered.length} objects
            </span>
          </div>

          <div className="flex items-center gap-3">
            <ThemeToggle />
          </div>
        </div>
      </header>

      <div className="mx-auto max-w-7xl px-4 py-6 md:px-6">
        {/* Search & Filter bar */}
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:gap-3 mb-6">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search objects, categories, tags..."
              className="w-full rounded-xl border border-border bg-card pl-10 pr-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/50"
            />
            {search && (
              <button
                onClick={() => setSearch("")}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-muted-foreground hover:text-foreground"
              >
                <X className="h-4 w-4" />
              </button>
            )}
          </div>
          <button
            onClick={() => setShowFilters(!showFilters)}
            className={`flex items-center gap-2 rounded-xl border px-4 py-2.5 text-sm font-medium transition-all ${
              showFilters || selectedCategory || selectedDifficulty
                ? "border-primary bg-primary/10 text-primary"
                : "border-border bg-card text-foreground hover:bg-accent"
            }`}
          >
            <Filter className="h-4 w-4" />
            Filters
            {(selectedCategory || selectedDifficulty) && (
              <span className="rounded-full bg-primary px-1.5 py-0.5 text-xs text-primary-foreground">
                {(selectedCategory ? 1 : 0) + (selectedDifficulty ? 1 : 0)}
              </span>
            )}
          </button>
        </div>

        {/* Filter panel */}
        <AnimatePresence>
          {showFilters && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: "auto", opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              className="overflow-hidden mb-6"
            >
              <div className="rounded-xl border border-border bg-card p-5">
                <div className="mb-4">
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="text-sm font-semibold text-foreground">Category</h3>
                    {selectedCategory && (
                      <button onClick={() => setSelectedCategory(null)} className="text-xs text-primary hover:underline">
                        Clear
                      </button>
                    )}
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {activeCategories.map((cat) => (
                      <button
                        key={cat}
                        onClick={() => setSelectedCategory(selectedCategory === cat ? null : cat)}
                        className={`rounded-full px-3 py-1 text-xs font-medium transition-all ${
                          selectedCategory === cat
                            ? "bg-primary text-primary-foreground"
                            : `${getCategoryBadgeClass(cat)} hover:opacity-80`
                        }`}
                      >
                        {cat}
                      </button>
                    ))}
                  </div>
                </div>
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="text-sm font-semibold text-foreground">Difficulty</h3>
                    {selectedDifficulty && (
                      <button onClick={() => setSelectedDifficulty(null)} className="text-xs text-primary hover:underline">
                        Clear
                      </button>
                    )}
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {DIFFICULTIES.map((d) => (
                      <button
                        key={d}
                        onClick={() => setSelectedDifficulty(selectedDifficulty === d ? null : d)}
                        className={`rounded-full px-3 py-1 text-xs font-medium capitalize transition-all ${
                          selectedDifficulty === d
                            ? "bg-primary text-primary-foreground"
                            : "bg-muted text-muted-foreground hover:bg-accent"
                        }`}
                      >
                        {d}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Results */}
        {paginated.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-20 text-center">
            <p className="text-lg font-medium text-foreground">No objects found</p>
            <p className="mt-1 text-sm text-muted-foreground">Try adjusting your search or filters</p>
            <button
              onClick={() => { setSearch(""); setSelectedCategory(null); setSelectedDifficulty(null); }}
              className="mt-4 text-sm text-primary hover:underline"
            >
              Clear all filters
            </button>
          </div>
        ) : (
          <>
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {paginated.map((obj, i) => (
                <CosmicCard key={obj.id} obj={obj} index={i} />
              ))}
            </div>

            {/* Pagination */}
            {totalPages > 1 && (
              <div className="mt-8 flex items-center justify-center gap-3">
                <button
                  onClick={() => setPage(Math.max(0, page - 1))}
                  disabled={page === 0}
                  className="flex items-center gap-1 rounded-lg border border-border bg-card px-3 py-2 text-sm font-medium text-foreground disabled:opacity-40 hover:bg-accent transition-colors"
                >
                  <ChevronLeft className="h-4 w-4" />
                  Prev
                </button>
                <span className="text-sm text-muted-foreground">
                  Page {page + 1} of {totalPages}
                </span>
                <button
                  onClick={() => setPage(Math.min(totalPages - 1, page + 1))}
                  disabled={page >= totalPages - 1}
                  className="flex items-center gap-1 rounded-lg border border-border bg-card px-3 py-2 text-sm font-medium text-foreground disabled:opacity-40 hover:bg-accent transition-colors"
                >
                  Next
                  <ChevronRight className="h-4 w-4" />
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
