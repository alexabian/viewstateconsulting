# CLAUDE.md - Viewstate Consulting Website

## Project Overview

Static marketing website for **Viewstate Consulting**, an IT infrastructure consulting and fractional technology leadership firm based in Dubai, UAE.

- **Live site:** [viewstate.co](https://viewstate.co)
- **Hosting:** GitHub Pages with custom domain (configured via `CNAME` file)
- **Founder:** Alejandro Abian, General Manager

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Markup | HTML5 (semantic elements) |
| Styling | Vanilla CSS3 with custom properties |
| Fonts | Google Fonts (Bitter, Roboto Mono) |
| Build system | None — static files served directly |
| Package manager | None |
| JavaScript framework | None |
| Deployment | GitHub Pages (auto-deploy on push to main) |

There is **no build step, no bundler, no package.json, and no node_modules**. Files are deployed as-is.

## Repository Structure

```
/
├── CNAME                    # GitHub Pages custom domain (viewstate.co)
├── index.html               # Main website (~1300 lines, single-page app)
├── brand-guidelines.html    # Brand identity documentation
├── email-signature.html     # Email signature template for the founder
├── favicon.svg              # SVG favicon ("vs" monogram)
└── CLAUDE.md                # This file
```

### File Descriptions

- **`index.html`** — The entire website in one file. Contains all HTML structure, embedded CSS (`<style>` block), and minimal inline behavior. Sections: header, hero, services (5 cards), expertise (6 categories), approach, about, contact form, footer.
- **`brand-guidelines.html`** — Standalone brand identity document covering logo usage, color palette, typography (DM Sans), spacing system, design principles (Dieter Rams-inspired), and voice/tone guidelines.
- **`email-signature.html`** — HTML and plain-text email signature for the founder. Includes contact details and GMT+4 timezone.
- **`favicon.svg`** — 32x32 SVG with dark background (#0a0a0a) and "vs" text in white.
- **`CNAME`** — Contains `viewstate.co` for GitHub Pages domain mapping.

## Design System

### Color Palette (CSS Custom Properties)

```css
--color-dark-navy: #222831    /* Primary text, dark backgrounds */
--color-charcoal: #393E46     /* Secondary text, borders */
--color-taupe: #948979        /* Accent color, highlights */
--color-cream: #DFD0B8        /* Light backgrounds, header */
--color-off-white: #f5f5f5    /* Page background base */
--color-accent: #948979       /* Alias for taupe */
```

### Typography

- **Display font:** `'Bitter', Georgia, serif` — used for headings and logo
- **Body/mono font:** `'Roboto Mono', monospace` — used for body text and UI elements
- Fluid typography using `clamp()` for responsive sizing

### Spacing

- Base unit: `8px` (`--spacing-unit: 8px`)
- Max content width: `1200px` (`--max-width: 1200px`)

### CSS Patterns

- CSS custom properties for theming
- CSS Grid and Flexbox for layouts
- `clamp()` for fluid/responsive sizing
- Gradient backgrounds on sections
- Smooth transitions via `--transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1)`
- `fadeIn` keyframe animation for content reveal
- kebab-case class naming (e.g., `.service-card`, `.hero-title`, `.expertise-category`)

## Development Workflow

### Making Changes

1. Edit HTML/CSS directly in the relevant `.html` file
2. Open in a browser to preview (no build step required)
3. Commit and push — GitHub Pages deploys automatically

### Deployment

Push to `main` branch triggers automatic deployment to GitHub Pages at `viewstate.co`. No CI/CD pipeline, build commands, or deployment scripts exist.

### Testing

There is no automated testing framework. Verify changes manually by:
- Opening HTML files in a browser
- Checking responsive behavior at various viewport widths
- Testing the contact form submission

## Key Conventions

### HTML

- Semantic HTML5 elements: `<header>`, `<main>`, `<section>`, `<footer>`
- Single-file architecture — all CSS is embedded in `<style>` within `<head>`
- Form integrates with Formspree for contact submissions
- WhatsApp link in header for direct contact

### CSS

- All styles live in the `<style>` block within each HTML file (no external stylesheets)
- Use existing CSS custom properties for colors, fonts, spacing, and transitions
- Maintain responsive design — use `clamp()` for fluid sizing, media queries for layout changes
- Follow the existing kebab-case class naming convention
- Keep the design consistent with brand guidelines documented in `brand-guidelines.html`

### Content

- Professional, concise tone — reflects the "precision, not noise" brand voice
- Services focus: IT infrastructure, fractional CTO/CIO, software asset management, AI modernization, project delivery
- Target audience: growing companies in Dubai and internationally

## External Services

| Service | Purpose | Notes |
|---------|---------|-------|
| Google Fonts | Typography (Bitter, Roboto Mono) | Loaded via `<link>` with `preconnect` |
| Formspree | Contact form backend | Form action URL in `index.html` |
| WhatsApp | Direct contact link | Link in header navigation |
| GitHub Pages | Static hosting | Configured via `CNAME` file |

## Known Issues

- Contact form has a placeholder Formspree endpoint (`f/YOUR_FORM_ID`) that may need a real form ID
- Some duplicate CSS blocks exist in `index.html` (form styling appears multiple times)
