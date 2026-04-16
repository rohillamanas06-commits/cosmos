import { jsx, jsxs } from "react/jsx-runtime";
import { createRootRoute, Link, Outlet, HeadContent, Scripts, createFileRoute, lazyRouteComponent, createRouter, useRouter } from "@tanstack/react-router";
const appCss = "/assets/styles-DAB8t7dq.css";
function NotFoundComponent() {
  return /* @__PURE__ */ jsx("div", { className: "flex min-h-screen items-center justify-center bg-background px-4", children: /* @__PURE__ */ jsxs("div", { className: "max-w-md text-center", children: [
    /* @__PURE__ */ jsx("h1", { className: "text-7xl font-bold text-foreground", children: "404" }),
    /* @__PURE__ */ jsx("h2", { className: "mt-4 text-xl font-semibold text-foreground", children: "Page not found" }),
    /* @__PURE__ */ jsx("p", { className: "mt-2 text-sm text-muted-foreground", children: "The page you're looking for doesn't exist or has been moved." }),
    /* @__PURE__ */ jsx("div", { className: "mt-6", children: /* @__PURE__ */ jsx(
      Link,
      {
        to: "/",
        className: "inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90",
        children: "Go home"
      }
    ) })
  ] }) });
}
const Route$a = createRootRoute({
  head: () => ({
    meta: [
      { charSet: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { title: "Cosmos — Explore the Universe" },
      { name: "description", content: "An interactive encyclopedia of 169 cosmic objects from galaxies to black holes." },
      { name: "author", content: "Cosmos" },
      { property: "og:title", content: "Cosmos — Explore the Universe" },
      { property: "og:description", content: "An interactive encyclopedia of 169 cosmic objects." },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary" }
    ],
    links: [
      { rel: "icon", href: "/nasa-Yj1M5riCKk4-unsplash.ico" },
      { rel: "preconnect", href: "https://fonts.googleapis.com" },
      { rel: "preconnect", href: "https://fonts.gstatic.com", crossOrigin: "anonymous" },
      { rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" },
      { rel: "stylesheet", href: appCss }
    ]
  }),
  shellComponent: RootShell,
  component: RootComponent,
  notFoundComponent: NotFoundComponent
});
function RootShell({ children }) {
  return /* @__PURE__ */ jsxs("html", { lang: "en", children: [
    /* @__PURE__ */ jsx("head", { children: /* @__PURE__ */ jsx(HeadContent, {}) }),
    /* @__PURE__ */ jsxs("body", { children: [
      children,
      /* @__PURE__ */ jsx(Scripts, {})
    ] })
  ] });
}
function RootComponent() {
  return /* @__PURE__ */ jsx(Outlet, {});
}
const $$splitComponentImporter$9 = () => import("./terms-CRHi78SJ.js");
const Route$9 = createFileRoute("/terms")({
  head: () => ({
    meta: [{
      title: "Terms of Service - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$9, "component")
});
const $$splitComponentImporter$8 = () => import("./privacy-CJXltCsh.js");
const Route$8 = createFileRoute("/privacy")({
  head: () => ({
    meta: [{
      title: "Privacy Policy - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$8, "component")
});
const $$splitComponentImporter$7 = () => import("./license-B8GYro4z.js");
const Route$7 = createFileRoute("/license")({
  head: () => ({
    meta: [{
      title: "License - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$7, "component")
});
const $$splitComponentImporter$6 = () => import("./faq-BrKgVwCD.js");
const Route$6 = createFileRoute("/faq")({
  head: () => ({
    meta: [{
      title: "FAQ - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$6, "component")
});
const $$splitComponentImporter$5 = () => import("./cookies-jkvezjTX.js");
const Route$5 = createFileRoute("/cookies")({
  head: () => ({
    meta: [{
      title: "Cookie Policy - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$5, "component")
});
const $$splitComponentImporter$4 = () => import("./contact-PN9TOxSr.js");
const Route$4 = createFileRoute("/contact")({
  head: () => ({
    meta: [{
      title: "Contact - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$4, "component")
});
const $$splitComponentImporter$3 = () => import("./about-DEHI62h1.js");
const Route$3 = createFileRoute("/about")({
  head: () => ({
    meta: [{
      title: "About - Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$3, "component")
});
const $$splitComponentImporter$2 = () => import("./index-C7LRQ2p_.js");
const Route$2 = createFileRoute("/")({
  head: () => ({
    meta: [{
      title: "Cosmos"
    }]
  }),
  component: lazyRouteComponent($$splitComponentImporter$2, "component")
});
const $$splitComponentImporter$1 = () => import("./explore.index-CPxogS2y.js");
const Route$1 = createFileRoute("/explore/")({
  head: () => ({
    meta: [{
      title: "Explore — Cosmos"
    }, {
      name: "description",
      content: "Browse and search 169 cosmic objects with filters by category and difficulty."
    }, {
      property: "og:title",
      content: "Explore — Cosmos"
    }, {
      property: "og:description",
      content: "Browse and search 169 cosmic objects."
    }]
  }),
  validateSearch: (search) => ({
    page: search.page ? Number(search.page) : 0,
    category: search.category || null
  }),
  component: lazyRouteComponent($$splitComponentImporter$1, "component")
});
const $$splitComponentImporter = () => import("./explore._objectId-CaAMhaLP.js");
const Route = createFileRoute("/explore/$objectId")({
  head: () => ({
    meta: [{
      title: "Object Detail — Cosmos"
    }, {
      name: "description",
      content: "Detailed view of a cosmic object."
    }]
  }),
  validateSearch: (search) => ({
    page: search.page ? Number(search.page) : 0,
    category: search.category || null
  }),
  component: lazyRouteComponent($$splitComponentImporter, "component")
});
const TermsRoute = Route$9.update({
  id: "/terms",
  path: "/terms",
  getParentRoute: () => Route$a
});
const PrivacyRoute = Route$8.update({
  id: "/privacy",
  path: "/privacy",
  getParentRoute: () => Route$a
});
const LicenseRoute = Route$7.update({
  id: "/license",
  path: "/license",
  getParentRoute: () => Route$a
});
const FaqRoute = Route$6.update({
  id: "/faq",
  path: "/faq",
  getParentRoute: () => Route$a
});
const CookiesRoute = Route$5.update({
  id: "/cookies",
  path: "/cookies",
  getParentRoute: () => Route$a
});
const ContactRoute = Route$4.update({
  id: "/contact",
  path: "/contact",
  getParentRoute: () => Route$a
});
const AboutRoute = Route$3.update({
  id: "/about",
  path: "/about",
  getParentRoute: () => Route$a
});
const IndexRoute = Route$2.update({
  id: "/",
  path: "/",
  getParentRoute: () => Route$a
});
const ExploreIndexRoute = Route$1.update({
  id: "/explore/",
  path: "/explore/",
  getParentRoute: () => Route$a
});
const ExploreObjectIdRoute = Route.update({
  id: "/explore/$objectId",
  path: "/explore/$objectId",
  getParentRoute: () => Route$a
});
const rootRouteChildren = {
  IndexRoute,
  AboutRoute,
  ContactRoute,
  CookiesRoute,
  FaqRoute,
  LicenseRoute,
  PrivacyRoute,
  TermsRoute,
  ExploreObjectIdRoute,
  ExploreIndexRoute
};
const routeTree = Route$a._addFileChildren(rootRouteChildren)._addFileTypes();
function DefaultErrorComponent({ error, reset }) {
  const router2 = useRouter();
  return /* @__PURE__ */ jsx("div", { className: "flex min-h-screen items-center justify-center bg-background px-4", children: /* @__PURE__ */ jsxs("div", { className: "max-w-md text-center", children: [
    /* @__PURE__ */ jsx("div", { className: "mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-full bg-destructive/10", children: /* @__PURE__ */ jsx(
      "svg",
      {
        xmlns: "http://www.w3.org/2000/svg",
        className: "h-8 w-8 text-destructive",
        fill: "none",
        viewBox: "0 0 24 24",
        stroke: "currentColor",
        strokeWidth: 2,
        children: /* @__PURE__ */ jsx(
          "path",
          {
            strokeLinecap: "round",
            strokeLinejoin: "round",
            d: "M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z"
          }
        )
      }
    ) }),
    /* @__PURE__ */ jsx("h1", { className: "text-2xl font-bold tracking-tight text-foreground", children: "Something went wrong" }),
    /* @__PURE__ */ jsx("p", { className: "mt-2 text-sm text-muted-foreground", children: "An unexpected error occurred. Please try again." }),
    false,
    /* @__PURE__ */ jsxs("div", { className: "mt-6 flex items-center justify-center gap-3", children: [
      /* @__PURE__ */ jsx(
        "button",
        {
          onClick: () => {
            router2.invalidate();
            reset();
          },
          className: "inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90",
          children: "Try again"
        }
      ),
      /* @__PURE__ */ jsx(
        "a",
        {
          href: "/",
          className: "inline-flex items-center justify-center rounded-md border border-input bg-background px-4 py-2 text-sm font-medium text-foreground transition-colors hover:bg-accent",
          children: "Go home"
        }
      )
    ] })
  ] }) });
}
const getRouter = () => {
  const router2 = createRouter({
    routeTree,
    context: {},
    scrollRestoration: true,
    defaultPreloadStaleTime: 0,
    defaultErrorComponent: DefaultErrorComponent
  });
  return router2;
};
const router = getRouter();
const router$1 = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  getRouter,
  router
}, Symbol.toStringTag, { value: "Module" }));
export {
  Route$1 as R,
  Route as a,
  router$1 as r
};
