# Project Sync Process

## Overview

Project content is managed in two repos:

1. **projectSummaries** (private) - Source of truth for content
   - Location: `/Users/pearseaudio/StephenPearseProfile/projectSummaries/portfolio-web/`
   - Plain markdown files
   - No Jekyll formatting

2. **portfolio** (public) - Published website
   - Location: `/Users/pearseaudio/StephenPearseProfile/portfolio/projects/`
   - Jekyll-formatted with front matter
   - Visual formatting (highlight boxes, metrics, etc.)

## Automated Sync (GitHub Actions)

The sync happens automatically via `.github/workflows/sync.yml`:

- **Trigger**: Manual workflow dispatch or weekly schedule (Mondays 9am UTC)
- **What it does**:
  1. Copies files from projectSummaries repo
  2. Adds Jekyll front matter
  3. Commits with note about visual formatting

**Currently synced files:**
- `density-copilot.md` → `01-Density-Copilot.md`
- `density-daw.md` → `02-Density-DAW.md`
- `density-fullstack.md` → `05-Density-Web-Platform.md`

**Not synced** (manually maintained):
- `03-Compose-with-Sounds.md` (not in projectSummaries yet)
- `04-CLaMP3-Audio-Semantic-Search.md` (not in projectSummaries yet)

## After Sync: Apply Visual Formatting

The GitHub Action only copies content - **visual formatting must be applied manually**.

### Using Claude Code

After the sync runs and creates a commit, use Claude Code:

```
"The GitHub sync just ran and updated project pages from projectSummaries.
Apply the visual formatting from projects/02-Density-DAW.md to the updated files.

Include:
- Highlight box with key achievements (🎯)
- Metrics box with 4 key numbers
- Two-column layouts for challenges
- Visual breaks with highlight boxes
- Reduce length by ~30-40%"
```

### Visual Elements Reference

See `projects/02-Density-DAW.md` for the template. Key components:

#### 1. Highlight Box (Key Achievements)
```html
<div class="highlight-box">

### 🎯 Key Achievements

- **Achievement 1** with bold emphasis
- **Achievement 2** with context

</div>
```

#### 2. Metrics Box
```html
<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">40%</span>
    <span class="metric-label">Crash Reduction<br>(5% → 3%)</span>
  </div>
  <!-- 3-4 total metrics -->
</div>
```

#### 3. Two-Column Layout
```html
<div class="two-col">
  <div class="col-box">
    <h4>Problem</h4>
    <ul>
      <li>Point 1</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>Solution</h4>
    <ul>
      <li>Point 1</li>
    </ul>
  </div>
</div>
```

## Manual Sync (if needed)

If you need to sync manually before the workflow runs:

```bash
cd /Users/pearseaudio/StephenPearseProfile/portfolio

# Example: sync density-copilot
cat > projects/01-Density-Copilot.md <<EOF
---
layout: default
title: Density Copilot
permalink: /projects/01-Density-Copilot.html
---

EOF

cat ../projectSummaries/portfolio-web/density-copilot.md >> projects/01-Density-Copilot.md

# Then use Claude Code to apply visual formatting
```

## Adding New Projects to Sync

To add a new project to automated sync:

1. **Create the source file** in projectSummaries/portfolio-web/
   ```bash
   cd /Users/pearseaudio/StephenPearseProfile/projectSummaries/portfolio-web
   # Create new-project.md
   ```

2. **Update the workflow** in portfolio/.github/workflows/sync.yml:
   ```bash
   # Add to the mappings array:
   ["new-project.md"]="06-New-Project.md"
   ```

3. **Run the workflow** (or wait for next scheduled run)
   - GitHub → Actions → "Sync Approved Summaries" → Run workflow

4. **Apply visual formatting** using Claude Code

## CSS Classes Available

All visual elements are styled in `assets/css/site.css`:

- `.highlight-box` - Gradient box with left accent
- `.metrics-box` - Grid of metric cards
- `.metric`, `.metric-value`, `.metric-label` - Individual metric styling
- `.two-col`, `.col-box` - Two-column responsive layout

## Troubleshooting

**Sync not working?**
- Check GitHub Actions logs
- Verify `PRIVATE_REPO_PAT` secret is set
- Confirm file names match workflow mappings

**Visual formatting not applied?**
- Check that CSS classes are available in `assets/css/site.css`
- Reference `projects/02-Density-DAW.md` as template
- Use Claude Code to apply transformations

**New file not syncing?**
- Add mapping to `.github/workflows/sync.yml`
- Verify source file exists in projectSummaries/portfolio-web/
- Trigger workflow manually to test
