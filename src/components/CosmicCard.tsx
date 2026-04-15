import { Link } from "@tanstack/react-router";
import { motion } from "framer-motion";
import type { CosmicObject } from "@/lib/cosmic-data";
import { getCategoryBadgeClass, getDifficultyColor } from "@/lib/cosmic-data";

export function CosmicCard({ obj, index }: { obj: CosmicObject; index: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: Math.min(index * 0.03, 0.5) }}
    >
      <Link
        to="/explore/$objectId"
        params={{ objectId: obj.id }}
        className="group block rounded-xl border border-border bg-card p-5 transition-all hover:border-primary/40 hover:shadow-lg hover:shadow-primary/5"
      >
        <div className="flex items-start justify-between gap-3">
          <div className="min-w-0 flex-1">
            <h3 className="font-display text-lg font-semibold text-foreground group-hover:text-primary transition-colors truncate">
              {obj.name}
            </h3>
            {obj.subtype && (
              <p className="mt-0.5 text-sm text-muted-foreground truncate">
                {obj.subtype}
              </p>
            )}
          </div>
          <span className={`shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ${getCategoryBadgeClass(obj.category)}`}>
            {obj.category}
          </span>
        </div>

        {obj.detailed_description && (
          <p className="mt-3 text-sm text-muted-foreground line-clamp-2">
            {obj.detailed_description}
          </p>
        )}

        <div className="mt-3 flex items-center gap-3">
          {obj.difficulty_level && (
            <span className={`text-xs font-medium capitalize ${getDifficultyColor(obj.difficulty_level)}`}>
              {obj.difficulty_level}
            </span>
          )}
          {obj.tags && obj.tags.length > 0 && (
            <div className="flex gap-1.5 overflow-hidden">
              {obj.tags.slice(0, 3).map((tag) => (
                <span key={tag} className="text-xs text-muted-foreground/70">
                  #{tag}
                </span>
              ))}
            </div>
          )}
        </div>
      </Link>
    </motion.div>
  );
}
