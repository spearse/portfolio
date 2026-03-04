#!/usr/bin/env python3
"""
Transform plain markdown project pages into visually enhanced format.
Used when syncing from projectSummaries repo to portfolio.

Usage:
    python scripts/transform-project-page.py <input.md> <output.md>

Example:
    python scripts/transform-project-page.py \
        ../projectSummaries/portfolio-web/density-copilot.md \
        projects/01-Density-Copilot.md
"""

import re
import sys
from typing import List, Dict, Tuple

def extract_metrics(content: str) -> List[Dict[str, str]]:
    """
    Extract key metrics from content.

    Looks for patterns like:
    - X% improvement
    - X months/weeks/years
    - X users/files/tests
    - <Xms latency
    """
    metrics = []

    # Pattern: percentage improvements
    percent_pattern = r'(\d+%)\s+(?:improvement|reduction|increase|faster|slower)'
    for match in re.finditer(percent_pattern, content, re.IGNORECASE):
        metrics.append({
            'value': match.group(1),
            'context': match.group(0)
        })

    # Pattern: time periods (X months, X years, etc.)
    time_pattern = r'(\d+\s+(?:month|week|year|day)s?)'
    for match in re.finditer(time_pattern, content, re.IGNORECASE):
        metrics.append({
            'value': match.group(1),
            'context': match.group(0)
        })

    # Pattern: quantities (X users, X files, X tests)
    quantity_pattern = r'(\d+[,\d]*\+?)\s+(?:users|files|tests|languages|platforms)'
    for match in re.finditer(quantity_pattern, content, re.IGNORECASE):
        metrics.append({
            'value': match.group(1),
            'context': match.group(0)
        })

    # Pattern: latency (<Xms)
    latency_pattern = r'(<\d+ms)'
    for match in re.finditer(latency_pattern, content, re.IGNORECASE):
        metrics.append({
            'value': match.group(1),
            'context': match.group(0)
        })

    return metrics[:4]  # Return top 4 metrics


def create_highlight_box(content: str) -> str:
    """Create a highlight box div."""
    return f'''<div class="highlight-box">

{content}

</div>
'''


def create_metrics_box(metrics: List[Tuple[str, str]]) -> str:
    """
    Create a metrics box with up to 4 metrics.

    Args:
        metrics: List of (value, label) tuples
    """
    if not metrics:
        return ""

    metric_divs = []
    for value, label in metrics:
        metric_divs.append(f'''  <div class="metric">
    <span class="metric-value">{value}</span>
    <span class="metric-label">{label}</span>
  </div>''')

    return f'''<div class="metrics-box">
{chr(10).join(metric_divs)}
</div>
'''


def create_two_col_box(items: List[Tuple[str, List[str]]]) -> str:
    """
    Create a two-column layout with col-box elements.

    Args:
        items: List of (heading, bullet_points) tuples
    """
    col_boxes = []
    for heading, points in items:
        bullets = '\n'.join(f'      <li>{point}</li>' for point in points)
        col_boxes.append(f'''  <div class="col-box">
    <h4>{heading}</h4>
    <ul>
{bullets}
    </ul>
  </div>''')

    return f'''<div class="two-col">
{chr(10).join(col_boxes)}
</div>
'''


def add_front_matter(content: str, title: str, number: str) -> str:
    """Add Jekyll front matter to the content."""
    permalink = f"/projects/{number}-{title.replace(' ', '-')}.html"

    return f'''---
layout: default
title: {title}
permalink: {permalink}
---

{content}'''


def transform_markdown(content: str, project_number: str) -> str:
    """
    Transform plain markdown into visually enhanced format.

    This is a helper that suggests transformations but requires manual
    refinement. The transformations include:
    - Adding front matter
    - Identifying sections that could be highlight boxes
    - Suggesting metrics to highlight

    Args:
        content: Input markdown content
        project_number: Project number (e.g., "01", "02")

    Returns:
        Transformed markdown with suggestions
    """

    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+?)(?:\s+-\s+.*)?$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Project"

    # Extract metrics for suggestion
    metrics = extract_metrics(content)

    # Add front matter
    result = add_front_matter(content, title, project_number)

    # Add a comment suggesting where to add visual elements
    suggestions = f"""
<!--
TRANSFORMATION SUGGESTIONS:
==========================

1. Add a highlight box near the top with key achievements using 🎯 emoji

2. Suggested metrics found in content:
{chr(10).join(f"   - {m['value']}: {m['context']}" for m in metrics[:4])}

   Create a metrics-box like:
   <div class="metrics-box">
     <div class="metric">
       <span class="metric-value">VALUE</span>
       <span class="metric-label">LABEL</span>
     </div>
     <!-- repeat for 3-4 key metrics -->
   </div>

3. Convert "Challenge" or "Problem" sections to two-col with col-box elements

4. Add highlight-box elements to break up dense technical sections

5. Reduce length by ~30-40% by condensing while keeping essential details

Reference: projects/02-Density-DAW.md for the template
-->
"""

    return result + suggestions


def main():
    """Main entry point."""
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Extract project number from output filename
    match = re.search(r'(\d+)-', output_file)
    project_number = match.group(1) if match else "01"

    # Read input
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Transform
    transformed = transform_markdown(content, project_number)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transformed)

    print(f"✅ Transformed {input_file} -> {output_file}")
    print(f"⚠️  Manual refinement needed! Check the TRANSFORMATION SUGGESTIONS comment.")
    print(f"📖 Reference: projects/02-Density-DAW.md for visual formatting examples")


if __name__ == '__main__':
    main()
