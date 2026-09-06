---
name: Website Design (Screenshot to Code)
description: Converts screenshots, UI mockups, sketches, and visual designs into clean, semantic, responsive HTML/CSS/JS and modern component frameworks. Based on the Screenshot-to-Code architecture.
---

# Website Design: Screenshot-to-Code Skill

This skill guides the translation of visual screenshots, design mockups, wireframes, and UI sketches into high-fidelity, production-ready, responsive front-end code. It incorporates principles from the **Screenshot-to-Code** architecture (Emil Wallner / pix2code).

---

## 🎯 Core Objectives

1. **Visual Fidelity**: Faithfully reproduce layout, typography, color palettes, spacing, and micro-interactions from any reference image or mockup.
2. **Semantic Structure**: Generate clean, modern, accessible HTML5, CSS3, and JavaScript rather than rigid absolute positioning.
3. **Responsive Adaptation**: Ensure designs generalize seamlessly across desktop, tablet, and mobile screen viewports.
4. **Component Modularization**: Break down complex interfaces into reusable, decoupled components and design tokens.

---

## 🧠 The 3-Tier Screenshot-to-Code Architecture

Inspired by the `Screenshot-to-code` pipeline:

```
[ Visual Input / Screenshot / Mockup ]
                  │
                  ▼
   1. Visual Decomposition & Tokenization
   (Grid, Hierarchy, Spacing, Typography, Color Palette)
                  │
                  ▼
   2. Structural Layout Synthesis
   (Container -> Grid/Flexbox -> Elements -> Media)
                  │
                  ▼
   3. Compilation & High-Fidelity Styling
   (Modern CSS / Tailwind / Bootstrap / Framework Components)
                  │
                  ▼
   4. Validation & Browser Visual Comparison
```

---

## 📋 Step-by-Step Implementation Workflow

### Step 1: Visual Decomposition & Token Extraction
Before writing any code, systematically extract the visual tokens from the screenshot:

1. **Color Palette & Design Tokens**:
   - Background colors (primary, secondary, surface, card backgrounds)
   - Text colors (heading `#1a1a2e`, body `#4a4a68`, muted `#888888`)
   - Accent / Brand colors (primary gradient, CTA highlight, border accents)
   - Border radii (`rounded-sm`: 4px, `rounded-md`: 8px, `pill`: 30px+)
   - Shadows (`box-shadow: 0 4px 15px rgba(0,0,0,0.08)`)

2. **Typography System**:
   - Heading font family, weight (600/700/800), and relative sizing (h1: 2.5rem, h2: 1.8rem, etc.)
   - Body copy line-height (1.5 - 1.7) and letter-spacing

3. **Layout Hierarchy (Domain Tokens)**:
   - Identify header / navigation bars
   - Hero / Headline sections
   - Grid / Multi-column card containers (`repeat(auto-fit, minmax(280px, 1fr))`)
   - Call-to-action blocks
   - Footer / Contact blocks

---

### Step 2: Semantic HTML Structure

Translate the visual tokens into semantic HTML tags:

```html
<!-- Navigation / Header -->
<header class="site-header">
  <div class="container nav-wrapper">
    <a href="#" class="brand-logo">...</a>
    <nav class="nav-menu">...</nav>
    <a href="#contact" class="cta-button">...</a>
  </div>
</header>

<!-- Hero Section -->
<section class="hero-section">
  <div class="container hero-content">
    <h1 class="hero-title">...</h1>
    <p class="hero-subtitle">...</p>
    <div class="hero-actions">...</div>
  </div>
</section>

<!-- Content Grid / Cards -->
<section class="features-section">
  <div class="container card-grid">
    <article class="card">...</article>
  </div>
</section>
```

---

### Step 3: Layout & Responsive Styling

Apply modern CSS standards:
- **CSS Grid & Flexbox**: Always prioritize dynamic flexbox and CSS grid over fixed widths or absolute coordinates.
- **Fluid Sizing**: Use `clamp()`, `rem`, and percentage units for adaptive typography and fluid containers.
- **Mobile-First Breakpoints**:
  - `@media (max-width: 768px)`: Stack multi-column grids into single-column flows.
  - `@media (max-width: 480px)`: Compact padding and adjust font scales for small mobile displays.

---

### Step 4: Visual Polish & Micro-Interactions

Add the details that make mockups feel alive:
- **Button Hover States**: Subtle transform (`transform: translateY(-2px)`), enhanced shadow, and smooth bezier transition (`transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`).
- **Card Depth**: Soft borders (`border: 1px solid rgba(0,0,0,0.08)`) or layered drop-shadows.
- **Interactive States**: Focus rings for accessibility (`:focus-visible`), active press effects.

---

### Step 5: Verification & Visual Comparison

1. **DOM & Viewport Audit**: Test the generated layout in real viewport dimensions (Desktop 1440px, Tablet 768px, Mobile 375px).
2. **Contrast & Legibility**: Verify WCAG AA contrast ratio compliance on all text against its background.
3. **No Overlaps / Overflow**: Check for horizontal scrollbars (`overflow-x: hidden`) and text clipping.

---

## 🛠️ Reference: Screenshot-to-Code Domain-Specific Token Dictionary

When compiling designs using intermediate tokenization (as in pix2code):

| Token Category | Tokens | HTML/CSS Equivalent |
|---|---|---|
| **Structural** | `header`, `footer`, `section`, `container` | `<header>`, `<footer>`, `<div class="container">` |
| **Grid** | `row`, `col-12`, `col-6`, `col-4`, `col-3` | Flex row / CSS grid column fraction (`1fr`) |
| **Components** | `card`, `navbar`, `media-object`, `badge` | Card component with header, body, and image |
| **Controls** | `btn-primary`, `btn-secondary`, `input-text` | Styled `<button>`, `<input type="text">` |
| **Typography** | `title`, `subtitle`, `paragraph`, `list` | `<h1>-<h3>`, `<p class="lead">`, `<ul><li>` |

---

## 💡 Quick Rules
- Never hardcode screen-specific pixel widths (`width: 1240px;`); use `max-width: 1200px; width: 100%;`.
- Ensure images utilize `max-width: 100%; height: auto; display: block;` to prevent layout breaking.
- Preserve accessibility attributes (`alt` on images, `aria-label` on icon-only buttons).
