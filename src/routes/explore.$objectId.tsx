import { createFileRoute, Link } from "@tanstack/react-router";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ArrowLeft, ExternalLink, Sparkles, Info, Atom, BookOpen } from "lucide-react";
import { loadCosmicObjectById, getCategoryBadgeClass, getDifficultyColor } from "@/lib/cosmic-data";
import type { CosmicObject } from "@/lib/cosmic-data";
import { ThemeToggle } from "@/components/ThemeToggle";

export const Route = createFileRoute("/explore/$objectId")({
  head: () => ({
    meta: [
      { title: "Object Detail — Cosmos" },
      { name: "description", content: "Detailed view of a cosmic object." },
    ],
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
      <div className="flex min-h-screen items-center justify-center bg-background">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent" />
      </div>
    );
  }

  if (!obj) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-background">
        <h1 className="font-display text-2xl font-bold text-foreground">Object not found</h1>
        <Link to="/explore" className="mt-4 text-primary hover:underline">Back to explorer</Link>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur-xl">
        <div className="mx-auto flex max-w-5xl items-center justify-between px-4 py-3 md:px-6">
          <Link
            to="/explore"
            className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
            Back to Explorer
          </Link>
          <ThemeToggle />
        </div>
      </header>

      <div className="mx-auto max-w-5xl px-4 py-8 md:px-6">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }}>
          {/* Title area */}
          <div className="mb-8">
            <div className="flex flex-wrap items-center gap-3 mb-3">
              <span className={`rounded-full px-3 py-1 text-xs font-medium ${getCategoryBadgeClass(obj.category)}`}>
                {obj.category}
              </span>
              {obj.difficulty_level && (
                <span className={`text-xs font-medium capitalize ${getDifficultyColor(obj.difficulty_level)}`}>
                  {obj.difficulty_level}
                </span>
              )}
            </div>
            <h1 className="font-display text-4xl font-bold text-foreground md:text-5xl">{obj.name}</h1>
            {obj.subtype && (
              <p className="mt-2 text-lg text-muted-foreground">{obj.subtype}</p>
            )}
            {obj.tags && (
              <div className="mt-3 flex flex-wrap gap-2">
                {obj.tags.map((tag) => (
                  <span key={tag} className="text-xs text-muted-foreground/70">#{tag}</span>
                ))}
              </div>
            )}
          </div>

          {/* Description */}
          {obj.detailed_description && (
            <Section icon={BookOpen} title="Description">
              <p className="text-foreground/80 leading-relaxed">{obj.detailed_description}</p>
            </Section>
          )}

          {/* Physical & Spatial data */}
          <div className="grid gap-6 md:grid-cols-2 mt-6">
            {obj.physical && Object.keys(obj.physical).length > 0 && (
              <Section icon={Atom} title="Physical Properties">
                <DataTable data={obj.physical} />
              </Section>
            )}
            {obj.spatial && Object.keys(obj.spatial).length > 0 && (
              <Section icon={Info} title="Spatial Data">
                <DataTable data={obj.spatial} />
              </Section>
            )}
          </div>

          {/* Scientific Facts */}
          {obj.scientific_facts && obj.scientific_facts.length > 0 && (
            <Section icon={Sparkles} title="Scientific Facts" className="mt-6">
              <ul className="space-y-2">
                {obj.scientific_facts.map((fact, i) => (
                  <li key={i} className="flex gap-2 text-sm text-foreground/80">
                    <span className="shrink-0 mt-1 h-1.5 w-1.5 rounded-full bg-primary" />
                    {fact}
                  </li>
                ))}
              </ul>
            </Section>
          )}

          {/* Did you know */}
          {obj.did_you_know && obj.did_you_know.length > 0 && (
            <Section icon={Sparkles} title="Did You Know?" className="mt-6">
              <ul className="space-y-2">
                {obj.did_you_know.map((fact, i) => (
                  <li key={i} className="flex gap-2 text-sm text-foreground/80">
                    <span className="shrink-0 mt-1 text-cosmos-solar">💡</span>
                    {fact}
                  </li>
                ))}
              </ul>
            </Section>
          )}

          {/* Formation */}
          {obj.formation_process && (
            <Section icon={Info} title="Formation Process" className="mt-6">
              <p className="text-foreground/80 leading-relaxed text-sm">{obj.formation_process}</p>
            </Section>
          )}

          {/* Future evolution */}
          {obj.future_evolution && (
            <Section icon={Info} title="Future Evolution" className="mt-6">
              <p className="text-foreground/80 leading-relaxed text-sm">{obj.future_evolution}</p>
            </Section>
          )}

          {/* Related */}
          {obj.related_objects && obj.related_objects.length > 0 && (
            <Section icon={Info} title="Related Objects" className="mt-6">
              <div className="flex flex-wrap gap-2">
                {obj.related_objects.map((r) => (
                  <span key={r} className="rounded-full bg-muted px-3 py-1 text-xs font-medium text-muted-foreground">
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
                className="inline-flex items-center gap-2 text-sm text-primary hover:underline"
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
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div className={`rounded-xl border border-border bg-card p-5 ${className}`}>
      <div className="flex items-center gap-2 mb-3">
        <Icon className="h-4 w-4 text-primary" />
        <h2 className="font-display text-sm font-semibold text-foreground uppercase tracking-wider">{title}</h2>
      </div>
      {children}
    </div>
  );
}

function DataTable({ data }: { data: Record<string, any> }) {
  return (
    <div className="space-y-2">
      {Object.entries(data).map(([key, value]) => (
        <div key={key} className="flex justify-between gap-4 text-sm border-b border-border/50 pb-1.5 last:border-0">
          <span className="text-muted-foreground capitalize">{key.replace(/_/g, " ")}</span>
          <span className="text-foreground/80 text-right font-mono text-xs max-w-[60%] break-words">
            {formatValue(value)}
          </span>
        </div>
      ))}
    </div>
  );
}
