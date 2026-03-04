#!/bin/bash
#
# Sync project summaries from projectSummaries repo to portfolio
# with visual formatting transformation.
#
# Usage: ./scripts/sync-projects.sh
#

set -e

PORTFOLIO_DIR="/Users/pearseaudio/StephenPearseProfile/portfolio"
SUMMARIES_DIR="/Users/pearseaudio/StephenPearseProfile/projectSummaries/portfolio-web"

echo "🔄 Syncing project summaries..."
echo ""

# Check if directories exist
if [ ! -d "$SUMMARIES_DIR" ]; then
    echo "❌ Error: projectSummaries directory not found at $SUMMARIES_DIR"
    exit 1
fi

# Define mappings: source file -> destination file
declare -A MAPPINGS=(
    ["density-copilot.md"]="01-Density-Copilot.md"
    ["density-daw.md"]="02-Density-DAW.md"
    ["compose-with-sounds.md"]="03-Compose-with-Sounds.md"
    ["clamp3-search.md"]="04-CLaMP3-Audio-Semantic-Search.md"
    ["density-fullstack.md"]="05-Density-Web-Platform.md"
)

echo "📋 Project mappings:"
for source in "${!MAPPINGS[@]}"; do
    dest="${MAPPINGS[$source]}"
    echo "  $source -> $dest"
done
echo ""

# Ask for confirmation
read -p "⚠️  This will OVERWRITE existing project files. Continue? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Sync cancelled"
    exit 1
fi

echo ""
echo "🚀 Starting sync..."
echo ""

# Sync each file
for source in "${!MAPPINGS[@]}"; do
    dest="${MAPPINGS[$source]}"
    source_path="$SUMMARIES_DIR/$source"
    dest_path="$PORTFOLIO_DIR/projects/$dest"

    if [ ! -f "$source_path" ]; then
        echo "⚠️  Skipping $source (not found)"
        continue
    fi

    echo "📝 Processing $source..."

    # For now, just copy the file with a note to manually format
    # In the future, this could use the transform script
    cp "$source_path" "$dest_path.tmp"

    # Extract project number
    number=$(echo "$dest" | grep -oE '^[0-9]+')

    # Use transform script to add front matter and suggestions
    python3 "$PORTFOLIO_DIR/scripts/transform-project-page.py" \
        "$source_path" \
        "$dest_path.tmp2" 2>/dev/null || {
        echo "⚠️  Transform script not working, using simple copy"
        # Simple fallback: just add front matter
        title=$(head -n 1 "$source_path" | sed 's/^# //' | sed 's/ - .*//')
        permalink="/projects/$dest"
        {
            echo "---"
            echo "layout: default"
            echo "title: $title"
            echo "permalink: ${permalink%.md}.html"
            echo "---"
            echo ""
            cat "$source_path"
        } > "$dest_path.tmp2"
    }

    mv "$dest_path.tmp2" "$dest_path"
    rm -f "$dest_path.tmp"

    echo "✅ Synced $dest"
done

echo ""
echo "✅ Sync complete!"
echo ""
echo "⚠️  IMPORTANT: Manual formatting required!"
echo "   Each project page needs visual formatting applied."
echo "   Reference: projects/02-Density-DAW.md"
echo ""
echo "   Required transformations:"
echo "   1. Add highlight-box with 🎯 key achievements"
echo "   2. Add metrics-box with impressive numbers"
echo "   3. Convert challenges to two-col layout"
echo "   4. Add visual breaks with highlight-boxes"
echo "   5. Condense content by ~30-40%"
echo ""
echo "💡 Tip: Use Claude Code to apply the transformations:"
echo "   'Apply the visual formatting from 02-Density-DAW.md to all project pages'"
echo ""
