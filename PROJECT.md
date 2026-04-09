# PROJECT.md - Complete Knowledge Base for tasnimalam.com

> **Read this file first in every new session.** It contains everything needed to understand, edit, and extend this website.

---

## Owner

**Mir Md Tasnim Alam** - Geospatial Data Scientist & AI Specialist
- Email: tasnim966937@gmail.com, tasnimalam@ou.edu
- GitHub: https://github.com/tasnim966937/website.git
- Live site: https://tasnimalam.com

---

## Quick Start

```powershell
# Install dependencies (first time only)
npm install                       # Node.js dependencies
pip install -r requirements.txt   # Python dependencies

# Start local dev server
node serve.mjs
# Serves at http://localhost:3000

# Take a full-page screenshot
node screenshot.mjs http://localhost:3000
# Saved to ./temporary screenshots/screenshot-N.png

# Screenshot a specific page with label
node screenshot.mjs http://localhost:3000/blog.html blog
# Saved to ./temporary screenshots/screenshot-N-blog.png

# Convert photos for a new album
python scripts/convert-images.py "C:/Photos/MyAlbum" album-slug
# Creates photography/album-slug/ with WebP images + thumbs/
```

**Shell: PowerShell** - no `&&` chaining, no heredocs. Use `$msg` variable for git commit messages:
```powershell
$msg = "Your commit message here"
git commit -m $msg
git push
```

---

## File Structure

```
ai_automation/
|
|-- index.html               # Production home page (edit directly)
|-- ai-automation.html        # AI & Web Solutions service page
|-- research.html             # Publications & Research (15 cards, filter pills, animated stats)
|-- remote-sensing.html       # Remote Sensing & AI project showcase + published research cards
|-- gis-mapping.html          # GIS & Mapping project showcase
|-- photography.html          # Photography gallery (masonry grid, 5 albums, lightbox, map view)
|-- blog.html                 # Blog listing page with filter pills
|-- paper-chl.html            # Paper: Canopy Chlorophyll (ML vs RTM)
|-- paper-nitrogen.html       # Paper: Chlorophyll & Nitrogen from EnMAP
|-- paper-phosphorus.html     # Paper: CCC/CNC/CPC from Google Satellite Embeddings
|
|-- blog/                     # Individual blog posts (5 HTML files)
|   |-- crypto-bangladesh.html
|   |-- debunking-myths-bengal.html
|   |-- ngos-save-or-exploit.html
|   |-- sticks-cant-tell.html
|   |-- trade-deal-bangladesh-us.html
|
|-- frames/                   # 145 WebP frames (frame_0001 to frame_0145) for planet scroll animation
|-- photography/              # Optimized WebP images + thumbs/ subfolders per album
|   |-- dc/                   # 44 photos + thumbs/ (Washington DC)
|   |-- yosemite/             # 49 photos + thumbs/
|   |-- death-valley/         # 20 photos + thumbs/
|   |-- miami/                # 19 photos + thumbs/
|   |-- kitch-iti-kipi/       # 30 photos + thumbs/
|
|-- scripts/                  # Utility scripts
|   |-- convert-images.py     # Convert JPG/PNG to WebP for albums
|
|-- research/                 # Media for remote-sensing.html & gis-mapping.html
|   |-- BD_3d.png, India_3d.png, eq_ohio.jpg, ship_routes.jpg
|   |-- poster_sst.jpg, poster_chlorophyll.jpg
|   |-- river_timelapse.mp4, nightlight_bd.mp4
|   |-- papers/
|       |-- chl/              # 5 figures for paper-chl.html
|       |-- nitrogen/         # 5 figures for paper-nitrogen.html
|       |-- phosphorus/       # 9 figures for paper-phosphorus.html
|
|-- ref/                      # Reviewer profile images (zach.jfif, jeff.webp, ifran.jfif)
|-- brand_assets/             # Mir.png logo, Mir Brand Guideline.png, reference designs
|
|-- serve.mjs                 # Local dev server (Node.js, port 3000)
|-- screenshot.mjs            # Puppeteer full-page screenshot utility
|-- CLAUDE.md                 # Frontend design rules for AI coding sessions
|-- SKILL.md                  # Cursor agent skill: frontend-design
|-- PROJECT.md                # This file
|-- package.json              # Dependencies: puppeteer, sharp, mammoth
|-- .gitignore                # See "Git" section below
```

---

## Design System

### CSS Variables (defined in `:root` on every page)

```css
--cosmic-black: #000000;    /* Global background, MUST be pitch black */
--cosmic-dark: #080808;
--cosmic-surface: #161616;
--accent-teal: #1E8289;     /* Primary accent */
--accent-gold: #DAA520;     /* Secondary accent */
--cosmic-blue: #1a3a5c;
--cosmic-purple: #2a1a4a;
```

### Typography

- **Headings**: `'Montserrat', sans-serif` - weight 700 to 900, letter-spacing `-0.02em` to `-0.04em`
- **Body**: `'Instrument Sans', sans-serif` (or `'Plus Jakarta Sans'` on some pages) - color `rgba(255,255,255,0.3)` to `0.5`
- **Fonts loaded via Google Fonts CDN**
- Tailwind CSS loaded via CDN `<script src="https://cdn.tailwindcss.com"></script>`

### Color Philosophy

- Background is always pitch black (`#000000` or `#0d0d0d`)
- Text is low-opacity white: `rgba(255,255,255,0.3)` for body, `rgba(255,255,255,0.55)` for secondary, full white for headings
- Teal (`#1E8289`) is the primary accent, gold (`#DAA520`) is secondary
- Cards alternate teal/gold glow on hover

---

## Shared Components (identical across all pages)

### Navigation

Fixed transparent nav bar at top. Must include:
- **Logo**: `Mır` using dotless `ı` (Unicode U+0131) with `.mir-i` and `.mir-dot` CSS classes for the animated dot
- **Links**: Home, About, Services, Blog, Photography
- **"Get in Touch" button**: `.moving-border-btn` with animated `.glow-orb` SVG border that orbits the button perimeter

```html
<nav class="fixed top-0 left-0 right-0 z-50 px-[5vw] py-5" style="background: rgba(13,13,13,0.92); backdrop-filter: blur(16px); border-bottom: 1px solid rgba(255,255,255,0.04);">
  <div class="max-w-[1400px] mx-auto flex items-center justify-between">
    <a href="index.html" class="group flex items-center gap-3">
      <span class="text-white font-extrabold text-3xl" style="font-family: 'Montserrat', sans-serif; letter-spacing: -0.03em; text-shadow: 0 0 20px rgba(30,130,137,0.3);">M<span class="mir-i">ı<span class="mir-dot"></span></span>r</span>
    </a>
    <div class="hidden sm:flex items-center gap-8 text-sm font-medium">
      <a href="index.html" class="nav-link-dark">Home</a>
      <a href="index.html#about" class="nav-link-dark">About</a>
      <a href="index.html#services" class="nav-link-dark">Services</a>
      <a href="blog.html" class="nav-link-dark">Blog</a>
      <a href="photography.html" class="nav-link-dark">Photography</a>
    </div>
    <!-- Get in Touch button with moving border -->
    <a href="mailto:info@tasnimalam.com,tasnimpksf@gmail.com" class="hidden sm:inline-flex moving-border-btn">
      ...
    </a>
  </div>
</nav>
```

### Footer

```html
<footer class="px-[7vw] py-14 border-t border-white/[0.04]">
  <div class="max-w-[1200px] mx-auto flex flex-col sm:flex-row items-center justify-between gap-6">
    <div class="flex items-center gap-3">
      <span class="text-white font-bold text-lg" style="font-family: 'Montserrat';">Mır</span>
      <span class="text-white/20 text-xs">|</span>
      <span class="text-white/30 text-xs font-medium tracking-wide" style="font-family: 'Montserrat';">Mir Md Tasnim Alam</span>
    </div>
    <div class="flex items-center gap-6 text-xs text-white/25">
      <!-- Same nav links as header -->
    </div>
    <p class="text-white/15 text-xs">&copy; 2026 Mir Md Tasnim Alam</p>
  </div>
</footer>
```

### Starfield Canvas

Some pages (index.html, research.html) use `<canvas id="starfield">` with a JS twinkling star animation as background.

### Scroll Reveal

All pages use Intersection Observer for entrance animations:
```javascript
var obs = new IntersectionObserver(function(entries) {
  entries.forEach(function(e) { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
}, { threshold: 0.1 });
document.querySelectorAll('.scroll-reveal').forEach(function(el) { obs.observe(el); });
```

Elements use classes: `.scroll-reveal`, `.sr-d1`, `.sr-d2` for staggered delays.

---

## Interactive Effects

### Cursor-Following Glow (used on most card types)

Cards across the site have a dynamic glow that follows the cursor. The pattern:

1. Create a `.card-glow` div inside each card
2. On `mousemove`, set a `radial-gradient` on the glow div centered at cursor position
3. Also set `box-shadow` with directional offset based on cursor position
4. On `mouseleave`, reset both
5. Colors alternate between teal and gold per card index (`i % 2`)

This pattern is applied to: `.svc-card`, `.blog-card`, `.blog-card-ft`, `.pub-card`, `.stat-card`, `.album-card-wrap`, `.card-wrap` (bento grid), `.paper-card`, `.fig-card`

### Moving Border Button

The "Get in Touch" button has an SVG rect path, and a JS animation that moves a glowing orb along the path perimeter using `getPointAtLength()`.

---

## Page-Specific Details

### index.html (Home Page)

- Planet scroll animation: 145 WebP frames in `frames/`, drawn on a `<canvas>` controlled by GSAP ScrollTrigger
- Lenis smooth scrolling
- Service cards (`.svc-card`) in a 4-column grid with cursor-following glow
- Blog feature cards (`.blog-card-ft`) linking to latest posts
- Section anchors: `#about` (planet entry), `#services`
- **Title must be**: "Mir Md Tasnim Alam - Geospatial Data Scientist & AI Specialist"

### photography.html

- Albums defined in a JS array (around line 418):
  ```javascript
  var albums = [
    { slug: 'yosemite', title: '...', subtitle: '...', date: '...', cover: '...', images: [...] },
    ...
  ];
  ```
- Images follow the pattern: `photography/{slug}/{name}.webp` (full) and `photography/{slug}/thumbs/{name}.webp` (thumbnail)
- To add a new album: create folder in `photography/`, add WebP images + `thumbs/`, add entry to the albums array

### blog.html

- Blog cards are hardcoded HTML `<a class="blog-card ...">` blocks
- Filter pills for categories (All, Geology, Economics, Analysis)
- Each card has `data-category` attribute for filtering
- To add a blog post: create `blog/new-post.html`, add a card block to `blog.html`

### remote-sensing.html

- Two sections: "Published Research" (top, 3 paper cards linking to paper-*.html) and "Project Visualizations" (bento grid)
- Bento grid items defined in JS array with title, description, media path, type (image/video)
- Gold accent color for glow

### gis-mapping.html

- Same bento grid pattern as remote-sensing.html
- Teal accent color for glow

### paper-chl.html, paper-nitrogen.html, paper-phosphorus.html

- Each has: hero (title, journal badge, DOI link), stat cards, abstract, key findings, key visualizations (at bottom)
- Figures stored in `research/papers/{chl|nitrogen|phosphorus}/`
- Gallery grid: `grid-template-columns: repeat(3, 1fr); grid-auto-rows: 340px;`
- Each figure card has click-to-expand fullscreen modal

### research.html

- 15 publication cards from Google Scholar
- Filter pills by category
- Animated stat counters

### ai-automation.html

- Service offerings page (voice agents, website creation, AI integration, etc.)

---

## How to Add Content

### New Photography Album

1. Convert images using the script:
   ```powershell
   python scripts/convert-images.py "C:/path/to/source/photos" album-slug
   # Optional flags: --quality 70 --max-width 2000 --thumb-width 800
   ```
   This creates `photography/album-slug/` with WebP images and `thumbs/` subfolder.

2. In `photography.html`, add to the `albums` array (~line 633):
   ```javascript
   {
     slug: 'album-slug',
     title: 'Location Name',
     subtitle: 'State/Country',
     date: 'Month Year',
     lat: 40.7128, lng: -74.0060,  // coordinates for map view
     cover: 'photography/album-slug/COVER_IMAGE.webp',
     description: 'Optional description.',
     images: ['IMG_001', 'IMG_002', 'IMG_003']
   }
   ```

3. Add to the `locations` array (~line 966) for map markers:
   ```javascript
   { idx: N, title: 'Location Name', sub: 'State, Month Year', 
     cover: 'photography/album-slug/COVER.webp', 
     lat: 40.7128, lng: -74.0060,
     anchorLat: 45.0, anchorLng: -65.0, textAnchor: 'left' }
   ```
   - `idx` matches the album's position in the albums array (0-indexed)
   - `anchorLat/anchorLng` is where the label text appears
   - `textAnchor` is 'left' or 'right' depending on which side of the map

### New Blog Post

1. Create `blog/my-new-post.html` (copy structure from an existing post)
2. In `blog.html`, add a new `<a href="blog/my-new-post.html" class="blog-card scroll-reveal block group" data-category="category">` block inside the blog grid section
3. Optionally add a `.blog-card-ft` card on `index.html` to feature it on the home page

### New Research Paper Showcase

1. Extract figures to `research/papers/paper-name/`
2. Create `paper-name.html` (copy structure from paper-chl.html)
3. Add a card linking to it in `remote-sensing.html`'s papers array

### New Project to Remote Sensing or GIS

1. Place optimized media in `research/`
2. Add entry to the items array in the respective page's JavaScript

---

## Animation Libraries

| Library | CDN | Used For |
|---------|-----|----------|
| GSAP 3 + ScrollTrigger | `cdnjs.cloudflare.com/ajax/libs/gsap/` | Planet scroll animation, text overlays, counters |
| Lenis | `cdn.jsdelivr.net/npm/lenis/` | Smooth scrolling on index.html |
| Intersection Observer | Native browser API | `.scroll-reveal` entrance animations on all pages |

---

## Copy Rules

- **Never use em dashes** in any user-facing text, headings, descriptions, or copy. Use commas, periods, or rewrite the sentence instead.

---

## Screenshot & Comparison Workflow

1. Start server: `node serve.mjs` (background, port 3000)
2. Screenshot: `node screenshot.mjs http://localhost:3000/page.html label`
3. Screenshots save to `./temporary screenshots/screenshot-N-label.png` (auto-incremented, never overwritten)
4. Puppeteer is in `node_modules/puppeteer`, Chrome cache at `C:/Users/mir.alam/.cache/puppeteer/`
5. When comparing to a reference image: check spacing, font size/weight, colors (exact hex), alignment, border-radius, shadows, image sizing
6. Do at least 2 comparison rounds before stopping

---

## Frontend Design Principles

- **Background**: Always pitch black
- **Colors**: Never use default Tailwind palette. Use custom brand colors (`--accent-teal`, `--accent-gold`)
- **Shadows**: Layered, color-tinted shadows. Never flat `shadow-md`
- **Typography**: Different fonts for headings (Montserrat) and body (Instrument Sans / Plus Jakarta Sans). Tight tracking on large headings, generous line-height on body
- **Gradients**: Layer multiple radial gradients. Add SVG noise for grain/texture
- **Animations**: Only animate `transform` and `opacity`. Never `transition-all`. Use spring-style easing
- **Interactive states**: Every clickable element needs hover, focus-visible, and active states
- **Depth**: Surfaces have a layering system (base, elevated, floating)
- **Cards**: Glassmorphic style with `rgba(255,255,255,0.015)` bg, subtle border, hover lift, cursor-following glow

---

## Git

- **Repo**: https://github.com/tasnim966937/website.git
- **Branch**: `main`
- **Hosted on**: Vercel (domain from Hostinger, DNS pointed to Vercel)

### .gitignore

```
node_modules/
temporary screenshots/
extract_figs.py
optimize-photos.mjs
globe-picker.html
logo-picker.html
globe_options/
video2web/
index-old.html
balerion-demo.html
CV/
Photography/
media_library_export-*/
ref/paper/*.pdf
ref/paper/fig*.jpg
research/papers/*/page_*.png
```

### Commit Convention (PowerShell)

```powershell
git add -A
$msg = "Describe the change concisely"
git commit -m $msg
git push
```

---

## Dev Dependencies

```json
{
  "puppeteer": "^24.38.0",
  "sharp": "^0.34.5",
  "mammoth": "^1.11.0"
}
```

- **puppeteer**: Headless Chrome for screenshots
- **sharp**: Image optimization (WebP conversion, resizing, thumbnails)
- **mammoth**: DOCX to HTML conversion (utility)
