# Operation Data Analyst · UK South East Roadmap

An interactive, responsive Single Page Application (SPA) designed to build job-ready analytics skills alongside work and commitments. Features a gamified *Solo Leveling* training arc system, live checkpoint tracking, UK South East employer market intel, curated courses, 5 portfolio project briefs, and interview preparation.

## Features

- **8 Dedicated App Screens**:
  - 🎯 **Roadmap**: 142 interactive skill checkpoints across 9 arcs (Excel, SQL, Power BI, Python, Stats, Capstone, Jobs) with horizontal skill filter chips.
  - 📊 **Market Intelligence**: UK South East job market data, salaries, and stack signals.
  - 👔 **Roles Audit**: Specifications from local employers (NHS Trusts, MetLife, Hastings Direct) and coverage matrix.
  - 🎓 **Courses**: Audited free curriculum with direct YouTube and documentation links.
  - 💼 **Portfolio Projects**: 5 employer-grade portfolio projects with clear business questions.
  - 🚀 **Job Hunt**: Application playbook, CV strategy, and LinkedIn outreach guidance.
  - 🎙️ **Interview Q&A**: 40+ practice questions spanning technical, behavioral, and commercial topics.
  - ⚡ **Shortcuts**: Quick-reference cheatsheets and downloadable PDF summaries.
- **Native Mobile App View**:
  - Floating bottom dock with high-res SVG icons.
  - Slide-up bottom sheet drawer with Hunter Rank leveling progress (`E-Rank` → `S-Rank`).
  - 50px thumb-friendly touch targets.
- **Offline & Persistence**:
  - Automatically saves all progress in `localStorage`.
  - Export and restore backup features for migrating progress across devices.

## Local Development

Serve locally using any static web server:

```bash
# Python
python3 -m http.server 8085

# Or Node / npx
npx serve .
```

Open [http://localhost:8085](http://localhost:8085) in your browser.

## Deployment to Vercel

Configured for automatic zero-config deployment on [Vercel](https://vercel.com) via `vercel.json` and `index.html`.
