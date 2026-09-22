#!/usr/bin/env python3
"""Generate .github/ISSUE_TEMPLATE/*.md and *_form.yml from .github/templates/source/*.yaml.

Usage:
    python .github/templates/generate_issue_templates.py --check   # CI用: 生成物が最新か検証
    python .github/templates/generate_issue_templates.py --write   # ローカル用: 生成物を書き出す
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path
from typing import Any

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR / "source"
OUTPUT_DIR = SCRIPT_DIR.parent / "ISSUE_TEMPLATE"

AUTOGEN_NOTICE = (
    ".github/templates/source/{id}.yaml から自動生成されています。"
    "このファイルを直接編集しないでください。"
    "ソースを編集し、`python .github/templates/generate_issue_templates.py --write` を実行してください。"
)


def yaml_str(value: str) -> str:
    """Render a Python string as a double-quoted YAML scalar."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def render_md(tpl: dict[str, Any]) -> str:
    lines: list[str] = [f"<!-- {AUTOGEN_NOTICE.format(id=tpl['id'])} -->", ""]
    lines += [
        "---",
        f'name: "{tpl["name"]}"',
        f'about: "{tpl["description"]}"',
        f'title: "{tpl["title_prefix"]}"',
        f'labels: "{", ".join(tpl["labels"])}"',
        "---",
        "",
    ]

    for sec in tpl["sections"]:
        lines.append(f"## {sec['heading']}")
        description = sec.get("md_description", sec.get("description"))
        if description:
            lines.append(f"<!-- {description} -->")

        kind = sec["kind"]
        if kind == "checkboxes":
            for item in sec["items"]:
                lines.append(f"- [ ] {item}")
        elif kind == "dropdown":
            opts = " / ".join(f"[ ] {o}" for o in sec["options"])
            lines.append(f"- {opts}")
        elif kind in ("textarea", "input"):
            if sec.get("sub_labels"):
                for label in sec["sub_labels"]:
                    lines.append(f"- **{label}:**")
            elif sec.get("example_lines"):
                for label, _example in sec["example_lines"]:
                    lines.append(f"- {label}: #")
            elif sec.get("value"):
                for item in sec["value"]:
                    lines.append(f"- [ ] {item}")
            elif sec.get("md_body") is not None:
                lines.append(sec["md_body"].rstrip("\n"))
        lines.append("")

    return "\n".join(lines).rstrip("\n") + "\n"


def render_yml(tpl: dict[str, Any]) -> str:
    lines: list[str] = [f"# {AUTOGEN_NOTICE.format(id=tpl['id'])}", ""]
    lines += [
        f'name: {yaml_str(tpl["name"] + " [フォーム版]")}',
        f'description: {yaml_str(tpl["description"])}',
        f'title: {yaml_str(tpl["title_prefix"])}',
        "labels:",
    ]
    for label in tpl["labels"]:
        lines.append(f"  - {yaml_str(label)}")
    lines.append("body:")

    for sec in tpl["sections"]:
        kind = sec["kind"]
        lines.append(f"  - type: {kind}")
        lines.append(f"    id: {sec['id']}")
        lines.append("    attributes:")
        lines.append(f"      label: {yaml_str(sec['heading'])}")

        description = sec.get("yml_description", sec.get("description"))
        if description:
            lines.append(f"      description: {yaml_str(description)}")

        if kind == "dropdown":
            lines.append("      options:")
            for opt in sec["options"]:
                lines.append(f"        - {yaml_str(opt)}")
        elif kind == "checkboxes":
            lines.append("      options:")
            for item in sec["items"]:
                lines.append(f"        - label: {yaml_str(item)}")
        elif kind in ("textarea", "input"):
            if sec.get("sub_labels"):
                placeholder = "\n".join(f"{label}:" for label in sec["sub_labels"])
                lines.append(f"      placeholder: {yaml_str(placeholder)}")
            elif sec.get("example_lines"):
                placeholder = "\n".join(
                    f"{label}: #{example}" if example else f"{label}: #"
                    for label, example in sec["example_lines"]
                )
                lines.append(f"      placeholder: {yaml_str(placeholder)}")
            elif sec.get("placeholder"):
                lines.append(f"      placeholder: {yaml_str(sec['placeholder'])}")

            if sec.get("value"):
                lines.append("      value: |")
                for item in sec["value"]:
                    lines.append(f"        - [ ] {item}")

        if sec.get("required"):
            lines.append("    validations:")
            lines.append("      required: true")
        lines.append("")

    return "\n".join(lines).rstrip("\n") + "\n"


def load_templates() -> list[dict[str, Any]]:
    templates = []
    for path in sorted(SOURCE_DIR.glob("*.yaml")):
        with path.open(encoding="utf-8") as f:
            templates.append(yaml.safe_load(f))
    return templates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="生成物が最新かを検証する（CI用）")
    group.add_argument("--write", action="store_true", help="生成物を書き出す（ローカル用）")
    args = parser.parse_args()

    up_to_date = True
    for tpl in load_templates():
        outputs = {
            OUTPUT_DIR / f"{tpl['id']}.md": render_md(tpl),
            OUTPUT_DIR / f"{tpl['id']}_form.yml": render_yml(tpl),
        }
        for path, content in outputs.items():
            if args.write:
                path.write_text(content, encoding="utf-8")
                print(f"wrote {path.relative_to(SCRIPT_DIR.parent.parent)}")
                continue

            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current != content:
                up_to_date = False
                rel = path.relative_to(SCRIPT_DIR.parent.parent)
                print(f"OUT OF DATE: {rel}")
                diff = difflib.unified_diff(
                    current.splitlines(keepends=True),
                    content.splitlines(keepends=True),
                    fromfile=f"{rel} (committed)",
                    tofile=f"{rel} (generated)",
                )
                sys.stdout.writelines(diff)

    if args.check and not up_to_date:
        print(
            "\n生成物がソースと一致していません。"
            "`python .github/templates/generate_issue_templates.py --write` を実行してコミットしてください。"
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
