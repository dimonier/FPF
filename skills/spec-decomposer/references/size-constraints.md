# Size Constraints

## Limits

| Level | Max Size | Max Lines | Purpose |
|-------|----------|-----------|---------|
| L2 SKILL.md body | 50 KB | ~500 | Core workflow + navigation |
| L3 index.md | 20 KB | ~200 | Domain overview + TOC |
| L4 unit files | 50 KB | ~500 | Individual content units |

## Rationale

### Why 50KB?

- Fits comfortably in context with other content
- Leaves room for conversation, other skills, tool results
- Practical limit for "one concept" depth

### Why 20KB for Indexes?

- Indexes are navigation, not content
- Should be scannable, not read in full
- Larger index = too many items = needs sub-domains

## Measuring Size

```python
import os

def check_file_size(path: str, limit_kb: int = 50) -> bool:
    size_kb = os.path.getsize(path) / 1024
    return size_kb <= limit_kb
```

## When Limits Exceeded

### L4 Unit Too Large (>50KB)

**Solution**: Create sub-index

```
domain/
├── index.md
├── large_unit/
│   ├── index.md      # Sub-index for this unit
│   ├── part_1.md
│   └── part_2.md
└── normal_unit.md
```

Parent index references `large_unit/index.md` instead of single file.

### L3 Index Too Large (>20KB)

**Solution**: Split domain into sub-domains

```
# Before
architheories/
├── index.md (25KB - too large!)
└── [50 files]

# After
architheories/
├── index.md (5KB - overview + sub-domain links)
├── core-cals/
│   ├── index.md
│   └── [files]
└── domain-cals/
    ├── index.md
    └── [files]
```

### L2 SKILL.md Too Large (>50KB)

**Solution**: Move content to L3 references

- Keep only essential workflow in SKILL.md
- Move detailed explanations to reference files
- Add "See [reference.md] for details" links

## TOC Requirement

Files over 100 lines MUST have table of contents at top:

```markdown
# Domain Name

## Contents

- [Section 1](#section-1)
- [Section 2](#section-2)
- [Section 3](#section-3)

## Section 1
...
```

## Validation Script Pattern

```python
def validate_skill_sizes(skill_path: Path) -> list[str]:
    """Return list of size violations."""
    violations = []
    
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        size = skill_md.stat().st_size / 1024
        if size > 50:
            violations.append(f"SKILL.md: {size:.1f}KB > 50KB limit")
    
    for index_file in skill_path.rglob("index.md"):
        size = index_file.stat().st_size / 1024
        if size > 20:
            violations.append(f"{index_file}: {size:.1f}KB > 20KB limit")
    
    for md_file in skill_path.rglob("*.md"):
        if md_file.name == "index.md":
            continue
        size = md_file.stat().st_size / 1024
        if size > 50:
            violations.append(f"{md_file}: {size:.1f}KB > 50KB limit")
    
    return violations
```
