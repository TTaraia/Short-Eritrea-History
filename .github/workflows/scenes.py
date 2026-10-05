"""Parses scenes_<lang>.txt.  Header:  Title | Date label | map spec (English file only)
map spec:  view=eritrea|horn; style=ancient|coast|italian|british|federation|province|war|independent; mark=Assab,Massawa; note=analysis
Scenes are separated by a line of ----- ; lines starting with # are ignored."""
import re, sys

def parse_spec(s):
    spec = {}
    for part in s.split(";"):
        if "=" in part:
            k, v = part.split("=", 1); spec[k.strip()] = v.strip()
    spec["mark"] = [m.strip() for m in spec.get("mark", "").split(",") if m.strip()]
    return spec

def parse(path):
    text = "\n".join(l for l in open(path, encoding="utf-8").read().splitlines() if not l.lstrip().startswith("#"))
    out = []
    for block in re.split(r"^\s*-{3,}\s*$", text, flags=re.M):
        block = block.strip()
        if not block: continue
        head, _, body = block.partition("\n")
        parts = [p.strip() for p in head.split("|")]
        if len(parts) < 2 or not body.strip():
            sys.exit(f"{path}: bad scene (need 'Title | Date' then narration): {head[:70]}")
        spoken = re.sub(r"([a-z0-9][.!?])([A-Z])", r"\1 \2", " ".join(body.split()))
        out.append({"title": parts[0], "date": parts[1], "spec": parse_spec(parts[2]) if len(parts) > 2 else {}, "spoken": spoken})
    return out
