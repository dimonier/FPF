"""FPF Tool Functions for Progressive Disclosure.

These tools provide access to the FPF specification without context overflow:
- fpf_search_index: Low token cost keyword search across patterns
- fpf_read_pattern: Load specific pattern content on demand

Index structure (single folder):
- references/fpf-patterns/introduction.md — title, TOC, preface
- references/fpf-patterns/index.md — single table (ID, title, domain, status, link)
- references/fpf-patterns/{pattern_id}_{title}.md — individual pattern files
"""

import logging
import re
from pathlib import Path

from pydantic_ai import RunContext

logger = logging.getLogger(__name__)

# Path to fpf-patterns directory (relative to this script)
FPF_PATTERNS_PATH = Path(__file__).parent.parent / "references" / "fpf-patterns"

# Domain definitions for search routing
DOMAINS = [
    "foundations",
    "transformation",
    "reasoning",
    "trust-evidence",
    "aggregation",
    "signature",
    "architheories",
    "constitution",
    "unification",
    "ethics",
    "sota",
]

# Cache for parsed single index
_all_patterns_cache: list[dict] | None = None


def _normalize_search_text(text: str) -> str:
    """Normalize text for keyword search."""
    normalized = text.lower().replace("*", " ").replace("`", " ")
    return re.sub(r"\s+", " ", normalized).strip()


def _parse_single_index() -> list[dict]:
    """Parse references/fpf-patterns/index.md (single table: ID | Title | Domain | Status | Link)."""
    global _all_patterns_cache
    if _all_patterns_cache is not None:
        return _all_patterns_cache

    index_path = FPF_PATTERNS_PATH / "index.md"
    if not index_path.exists():
        _all_patterns_cache = []
        return []

    content = index_path.read_text(encoding="utf-8")
    patterns = []
    # Table: | ID | Title | Domain | Status | Link |
    link_re = re.compile(r"\]\(([^)]+)\)")

    for line in content.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 5:
            continue
        pattern_id = cells[0].strip()
        if not re.match(r"^[A-G]\.[A-Za-z0-9.]+$", pattern_id):
            continue
        title = cells[1].strip()
        domain = cells[2].strip() if len(cells) > 2 else ""
        link_match = link_re.search(cells[4])
        filename = link_match.group(1).strip() if link_match else ""
        if not filename:
            continue
        patterns.append({
            "id": pattern_id,
            "title": title,
            "filename": filename,
            "keywords": "",
            "domain": domain,
        })

    _all_patterns_cache = patterns
    return patterns


def _parse_domain_index(domain: str) -> list[dict]:
    """Return patterns in the given domain (filter from single index)."""
    return [p for p in _parse_single_index() if p.get("domain") == domain]


def _get_all_patterns() -> list[dict]:
    """Get all patterns from the single index."""
    return _parse_single_index()


def _search_patterns(keyword: str) -> list[dict]:
    """Search for patterns matching keyword in ID, title, or keywords."""
    keyword_lower = _normalize_search_text(keyword)
    results = []
    
    for pattern in _get_all_patterns():
        searchable = " ".join([
            pattern.get("id", ""),
            pattern.get("title", ""),
            pattern.get("keywords", ""),
        ])
        searchable = _normalize_search_text(searchable)
        if keyword_lower and keyword_lower in searchable:
            results.append(pattern)
    
    return results


def _find_pattern_file(pattern_id: str) -> Path | None:
    """Find the file path for a specific pattern ID (single folder)."""
    raw_id = pattern_id.strip()
    if raw_id and raw_id[0].isalpha():
        pattern_id_norm = raw_id[0].upper() + raw_id[1:]
    else:
        pattern_id_norm = raw_id

    for p in _parse_single_index():
        if p["id"].upper() == pattern_id_norm.upper():
            return FPF_PATTERNS_PATH / p["filename"]

    # Fallback: exact ID.md or legacy ID_slug.md
    if not FPF_PATTERNS_PATH.exists():
        return None
    exact = FPF_PATTERNS_PATH / f"{pattern_id_norm}.md"
    if exact.exists():
        return exact
    for f in FPF_PATTERNS_PATH.glob(f"{pattern_id_norm}_*.md"):
        return f
    for f in FPF_PATTERNS_PATH.glob("*.md"):
        if f.name.lower().startswith(pattern_id_norm.lower() + "_"):
            return f
    return None


async def fpf_search_index(ctx: RunContext[None], keyword: str) -> str:
    """
    Search FPF index for patterns matching keyword (ID, title, or keywords/queries).
    
    This is the first tool to use when starting any task.
    Returns a list of pattern IDs with their titles and domains.
    
    Args:
        ctx: Run context (required by pydantic-ai)
        keyword: Search term (e.g., "trust", "evidence", "holon")
        
    Returns:
        Formatted list of matching patterns, or "No patterns found"
        
    Example:
        fpf_search_index("trust")
        # Returns:
        # B.3 - Trust & Assurance Calculus (trust-evidence)
        # B.3.4 - Evidence Decay & Epistemic Debt (trust-evidence)
    """
    results = _search_patterns(keyword)
    
    if results:
        # Deduplicate and format
        unique = {p["id"]: p for p in results}
        formatted = sorted(
            f"{p['id']} - {p['title']} ({p['domain']})"
            for p in unique.values()
        )
        logger.info(f"FPF search '{keyword}': found {len(formatted)} patterns")
        return "\n".join(formatted)
    
    logger.info(f"FPF search '{keyword}': no patterns found")
    return (
        "No patterns found for this keyword.\n"
        "Try different terms like: holon, system, method, work, trust, evidence, role, context\n"
        "Or navigate by domain - see SKILL.md for domain navigation table."
    )


async def fpf_read_pattern(ctx: RunContext[None], pattern_id: str) -> str:
    """
    Load full content of a specific FPF pattern.
    
    Use this after fpf_search_index to load pattern details.
    
    Args:
        ctx: Run context (required by pydantic-ai)
        pattern_id: Pattern identifier (e.g., "A.1", "B.3", "A.15.1")
        
    Returns:
        Full markdown content of the pattern, or error message
        
    Example:
        fpf_read_pattern("A.3")
        # Returns full text of Pattern A.3 - Transformer Constitution (Quartet)
    """
    pattern_id = pattern_id.strip()
    
    if not pattern_id or "." not in pattern_id:
        return f"Invalid pattern ID format: '{pattern_id}'. Expected format: 'A.1', 'B.3', etc."
    
    file_path = _find_pattern_file(pattern_id)
    
    if file_path and file_path.exists():
        logger.info(f"FPF read pattern: {pattern_id} from {file_path.name}")
        return file_path.read_text(encoding="utf-8")
    
    # Pattern not found - provide helpful suggestions
    part_letter = pattern_id[0].upper()
    
    # Find patterns with same prefix
    all_patterns = _get_all_patterns()
    suggestions = [
        p for p in all_patterns 
        if p["id"].startswith(part_letter + ".")
    ][:5]
    
    if suggestions:
        suggestion_str = ", ".join(p["id"] for p in suggestions)
        return (
            f"Pattern '{pattern_id}' not found.\n"
            f"Available patterns starting with {part_letter}: {suggestion_str}...\n"
            "Use fpf_search_index to find patterns."
        )
    
    return (
        f"Pattern '{pattern_id}' not found.\n"
        "Use fpf_search_index to find patterns, or navigate by domain in SKILL.md."
    )


async def fpf_list_domain(ctx: RunContext[None], domain: str) -> str:
    """
    List all patterns in a specific domain.
    
    Use this to explore available patterns in a domain.
    
    Args:
        ctx: Run context (required by pydantic-ai)
        domain: Domain name (e.g., "foundations", "reasoning", "trust-evidence")
        
    Returns:
        List of patterns in the domain, or error if domain not found
        
    Example:
        fpf_list_domain("reasoning")
        # Returns:
        # B.5 - Canonical Reasoning Cycle
        # B.5.1 - Explore → Shape → Evidence → Operate
        # ...
    """
    domain = domain.strip().lower()
    
    if domain not in DOMAINS:
        return (
            f"Domain '{domain}' not found.\n"
            f"Available domains: {', '.join(DOMAINS)}"
        )
    
    patterns = _parse_domain_index(domain)
    
    if not patterns:
        return f"No patterns found in domain '{domain}'."
    
    formatted = [f"{p['id']} - {p['title']}" for p in patterns]
    logger.info(f"FPF list domain '{domain}': {len(formatted)} patterns")
    
    return f"# {domain.replace('-', ' ').title()}\n\n" + "\n".join(formatted)
