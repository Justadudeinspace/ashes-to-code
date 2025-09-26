#!/usr/bin/env python3
import sys, os, datetime, textwrap

TEMPLATE = '''# Ashes to Code — {date}

### Opening (Raw State)  
{opening}

### Middle (Anchor & Meaning)  
{anchor}

### Progress (Concrete Wins)  
{progress}

### Philosophy (Signal)  
{signal}

### Closing (Beacon)  
Never give up. That’s the creed.  

(( • ))
'''

def main():
    if len(sys.argv) < 2:
        print("Usage: new_entry.py YYYY-MM-DD [title ignored]")
        sys.exit(1)
    date = sys.argv[1]
    out_dir = os.path.join(os.path.dirname(__file__), "..", "devlog")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{date}.md")

    if os.path.exists(out_path):
        print(f"[SKIP] {out_path} already exists")
        return

    content = TEMPLATE.format(
        date=date,
        opening="(write the truth of where you are)",
        anchor="(why you keep going — daughter, lineage, creed)",
        progress="(one or two concrete wins)",
        signal="(one short truth that heals rather than harms)",
    ).strip() + "\n"

    with open(out_path, "w") as f:
        f.write(content)
    print(f"[OK] created {out_path}")

if __name__ == "__main__":
    main()
