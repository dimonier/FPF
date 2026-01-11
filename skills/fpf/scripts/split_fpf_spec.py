"""Split FPF-Spec.md into domain-organized files with 4-level progressive disclosure.

This script:
1. Reads the large FPF-Spec.md file
2. Splits it into individual .md files by pattern (## A.1, ## B.3, etc.)
3. Organizes files into semantic domain directories (foundations, reasoning, etc.)
4. Generates index.md per domain with pattern TOC and "Load when..." guidance

Usage:
    uv run skills/fpf/scripts/split_fpf_spec.py
"""

import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Paths
SCRIPT_DIR = Path(__file__).parent
FPF_SKILL_DIR = SCRIPT_DIR.parent
FPF_CORE_DIR = FPF_SKILL_DIR / "fpf-core"
FPF_SPEC_PATH = Path(__file__).parents[3] / "FPF" / "FPF-Spec.md"

# Domain definitions with descriptions and "Load when..." guidance
DOMAINS = {
    "foundations": {
        "description": "Core ontological concepts: holons, entities, roles, and fundamental distinctions.",
        "load_when": "understanding what entities ARE, modeling basics, identity vs structure",
    },
    "transformation": {
        "description": "Action and change patterns: methods, work, execution, and evolution cycles.",
        "load_when": "planning tasks, executing work, understanding plan vs reality",
    },
    "reasoning": {
        "description": "Problem-solving and thinking patterns: reasoning cycles, abduction, exploration.",
        "load_when": "problem-solving, hypothesis generation, creative thinking",
    },
    "trust-evidence": {
        "description": "Trust, reliability, and evidence patterns: F-G-R calculus, assurance, provenance.",
        "load_when": "evaluating claims, checking reliability, evidence chains",
    },
    "aggregation": {
        "description": "Composition and emergence patterns: Gamma operator, meta-holon transitions, mereology.",
        "load_when": "combining parts, understanding emergence, holarchy",
    },
    "signature": {
        "description": "Interface and boundary patterns: signature stack, boundary norms, epistemic morphing.",
        "load_when": "interface design, boundary discipline, type systems",
    },
    "architheories": {
        "description": "Domain-specific calculi and characterizations: Sys-CAL, Kind-CAL, Method-CAL, etc.",
        "load_when": "domain-specific modeling, specialized calculi",
    },
    "constitution": {
        "description": "FPF core principles, pillars, authoring guides, and governance patterns.",
        "load_when": "understanding FPF rules, constraints, authoring",
    },
    "unification": {
        "description": "Cross-domain integration patterns: bridges, mappings, universal structures.",
        "load_when": "integrating across domains, building bridges",
    },
    "ethics": {
        "description": "Multi-scale ethics, conflict resolution, and axiological patterns.",
        "load_when": "ethical considerations, conflict resolution, values",
    },
    "sota": {
        "description": "State-of-the-art patterns: discipline packs, benchmarks, telemetry.",
        "load_when": "advanced usage, benchmarking, discipline-specific packs",
    },
}

# Pattern ID -> Domain mapping
# Uses prefix matching: "A.1" matches "A.1", "A.1.1", "A.1.2", etc.
DOMAIN_MAPPING = {
    # Foundations: A.1, A.1.1, A.2-A.2.9, A.7-A.11
    "A.0": "foundations",
    "A.1": "foundations",
    "A.2": "foundations",
    "A.7": "foundations",
    "A.8": "foundations",
    "A.9": "foundations",
    "A.11": "foundations",
    "A.12": "foundations",
    "A.13": "foundations",
    
    # Transformation: A.3, A.3.x, A.4, A.15, A.15.x, B.4, B.4.x
    "A.3": "transformation",
    "A.4": "transformation",
    "A.15": "transformation",
    "B.4": "transformation",
    
    # Reasoning: B.5, B.5.x, B.6, B.7
    "B.5": "reasoning",
    "B.6": "reasoning",
    "B.7": "reasoning",
    
    # Trust-Evidence: A.10, B.3, B.3.x, C.2, C.2.x
    "A.10": "trust-evidence",
    "B.3": "trust-evidence",
    "C.2": "trust-evidence",
    
    # Aggregation: B.1, B.1.x, B.2, B.2.x, A.14
    "A.14": "aggregation",
    "B.1": "aggregation",
    "B.2": "aggregation",
    
    # Signature: A.6, A.6.x (all A.6.* patterns)
    "A.6": "signature",
    
    # Architheories: All Part C except C.2
    "C.1": "architheories",
    "C.3": "architheories",
    "C.4": "architheories",
    "C.5": "architheories",
    "C.6": "architheories",
    "C.7": "architheories",
    "C.9": "architheories",
    "C.10": "architheories",
    "C.11": "architheories",
    "C.12": "architheories",
    "C.13": "architheories",
    "C.14": "architheories",
    "C.15": "architheories",
    "C.16": "architheories",
    "C.17": "architheories",
    "C.18": "architheories",
    "C.19": "architheories",
    "C.20": "architheories",
    "C.21": "architheories",
    "C.22": "architheories",
    "C.23": "architheories",
    "C.24": "architheories",
    "C.25": "architheories",
    
    # Constitution: Part E
    "E": "constitution",
    
    # Unification: Part F
    "F": "unification",
    
    # Ethics: Part D
    "D": "ethics",
    
    # SOTA: Part G
    "G": "sota",
    
    # Characteristics (A.17-A.21) -> foundations (measurement/state concepts)
    "A.17": "foundations",
    "A.18": "foundations",
    "A.19": "foundations",
    "A.20": "foundations",
    "A.21": "foundations",
}


def get_domain_for_pattern(pattern_id: str) -> str:
    """Get domain for a pattern ID using prefix matching."""
    # Try exact match first
    if pattern_id in DOMAIN_MAPPING:
        return DOMAIN_MAPPING[pattern_id]
    
    # Try progressively shorter prefixes
    # E.g., for "A.6.B", try "A.6.B", "A.6", "A"
    parts = pattern_id.split(".")
    for i in range(len(parts) - 1, 0, -1):
        prefix = ".".join(parts[:i])
        if prefix in DOMAIN_MAPPING:
            return DOMAIN_MAPPING[prefix]
    
    # Try just the letter
    if parts[0] in DOMAIN_MAPPING:
        return DOMAIN_MAPPING[parts[0]]
    
    # Default fallback
    logger.warning(f"No domain mapping for {pattern_id}, using 'foundations'")
    return "foundations"


def sanitize_filename(title: str) -> str:
    """Convert title to safe filename."""
    safe = re.sub(r"[^\w\s-]", "", title)
    safe = re.sub(r"\s+", "_", safe.strip())
    return safe.lower()[:50]


# Pattern regex: matches ## A.1, ## A.1.1, ## B.3.4, ## A.6.B, etc.
PATTERN_REGEX = re.compile(r"^## ([A-G])\.(\d+(?:\.\d+)?(?:\.[A-Z0-9]+)?)\s*[-–—]?\s*(.*)$")


def split_spec() -> dict[str, list[dict]]:
    """Split FPF-Spec.md into individual files organized by domain.
    
    Returns:
        Dict mapping domain name to list of pattern info dicts.
    """
    if not FPF_SPEC_PATH.exists():
        logger.error(f"FPF-Spec.md not found at {FPF_SPEC_PATH}")
        return {}
    
    logger.info(f"Reading {FPF_SPEC_PATH}...")
    content = FPF_SPEC_PATH.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    # Create domain directories
    for domain in DOMAINS.keys():
        (FPF_CORE_DIR / domain).mkdir(parents=True, exist_ok=True)
    
    # Collect patterns per domain
    domain_patterns: dict[str, list[dict]] = {domain: [] for domain in DOMAINS.keys()}
    
    current_pattern_id = None
    current_pattern_title = None
    current_content_lines = []
    patterns_found = 0
    
    def save_current_pattern():
        """Save accumulated content to file in appropriate domain."""
        nonlocal patterns_found
        if current_pattern_id and current_content_lines:
            domain = get_domain_for_pattern(current_pattern_id)
            filename = f"{current_pattern_id}_{sanitize_filename(current_pattern_title or 'pattern')}.md"
            filepath = FPF_CORE_DIR / domain / filename
            
            content_text = "\n".join(current_content_lines)
            filepath.write_text(content_text, encoding="utf-8")
            
            # Track pattern info for index generation
            domain_patterns[domain].append({
                "id": current_pattern_id,
                "title": current_pattern_title or current_pattern_id,
                "filename": filename,
                "size_kb": len(content_text.encode("utf-8")) / 1024,
            })
            
            patterns_found += 1
    
    for line in lines:
        match = PATTERN_REGEX.match(line)
        if match:
            # Save previous pattern
            save_current_pattern()
            
            # Start new pattern
            part_letter = match.group(1)
            pattern_num = match.group(2)
            current_pattern_id = f"{part_letter}.{pattern_num}"
            current_pattern_title = match.group(3).strip() if match.group(3) else ""
            current_content_lines = [line]
        elif current_pattern_id:
            current_content_lines.append(line)
    
    # Save last pattern
    save_current_pattern()
    
    logger.info(f"Split into {patterns_found} pattern files")
    
    return domain_patterns


def generate_domain_indexes(domain_patterns: dict[str, list[dict]]):
    """Generate index.md for each domain with pattern TOC."""
    for domain, patterns in domain_patterns.items():
        if not patterns:
            continue
        
        domain_info = DOMAINS[domain]
        
        # Sort patterns by ID
        patterns.sort(key=lambda p: p["id"])
        
        # Build index.md content
        lines = [
            f"# {domain.replace('-', ' ').title()}",
            "",
            domain_info["description"],
            "",
            f"**Load when**: {domain_info['load_when']}",
            "",
            "## Patterns",
            "",
            "| Pattern | Title | Size |",
            "|---------|-------|------|",
        ]
        
        for p in patterns:
            size_str = f"{p['size_kb']:.1f} KB"
            lines.append(f"| [{p['id']}]({p['filename']}) | {p['title']} | {size_str} |")
        
        lines.extend(["", f"Total: {len(patterns)} patterns", ""])
        
        index_path = FPF_CORE_DIR / domain / "index.md"
        index_path.write_text("\n".join(lines), encoding="utf-8")
        
        logger.info(f"  {domain}: {len(patterns)} patterns -> index.md")


def generate_master_index(domain_patterns: dict[str, list[dict]]):
    """Generate master index showing all domains."""
    lines = [
        "# FPF Core Reference",
        "",
        "Progressive disclosure index for FPF patterns.",
        "",
        "## Domains",
        "",
        "| Domain | Patterns | Load when... |",
        "|--------|----------|--------------|",
    ]
    
    for domain, patterns in domain_patterns.items():
        if not patterns:
            continue
        domain_info = DOMAINS[domain]
        count = len(patterns)
        lines.append(f"| [{domain}]({domain}/index.md) | {count} | {domain_info['load_when']} |")
    
    total = sum(len(p) for p in domain_patterns.values())
    lines.extend(["", f"Total: {total} patterns across {len([d for d in domain_patterns.values() if d])} domains", ""])
    
    index_path = FPF_CORE_DIR / "index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    
    logger.info(f"Generated master index: {index_path}")


def main():
    """Main entry point."""
    logger.info("FPF Specification Splitter (4-Level Progressive Disclosure)")
    logger.info("=" * 60)
    
    domain_patterns = split_spec()
    if domain_patterns:
        generate_domain_indexes(domain_patterns)
        generate_master_index(domain_patterns)
        logger.info("Done!")
    else:
        logger.error("Failed to split specification")


if __name__ == "__main__":
    main()
