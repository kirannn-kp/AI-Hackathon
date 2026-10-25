"""Rebuild the local review page and HackboxConsole content; never deploys."""
import html
import shutil
from pathlib import Path

import markdown


def build(root: Path) -> None:
    pages = [
        ("brief", "docs/START_HERE.md"), ("architecture", "docs/architecture.md"),
        ("setup", "README.md"),
        *((f"mission-{number:02}", f"docs/mission-{number:02}.md") for number in range(1, 5)),
        ("bonus", "docs/bonus.md"),
    ]
    sources = {name: (root / path).read_text(encoding="utf-8") for name, path in pages}
    links = {path: f"#{name}" for name, path in pages}
    links["/challenges"] = "#mission-01"
    sections = []
    for name, _ in pages:
        body = markdown.markdown(sources[name], extensions=["fenced_code", "tables"])
        for target, replacement in links.items():
            body = body.replace(f'href="{target}"', f'href="{replacement}"')
        sections.append(f'<section id="{html.escape(name)}" class="review-card" hidden>{body}</section>')
    theme = (root / "web" / "theme.css").read_text(encoding="utf-8")
    template = (root / "web" / "review.html").read_text(encoding="utf-8")
    preview = template.replace("{{THEME}}", theme).replace("{{CONTENT}}", "\n".join(sections))
    (root / "index.html").write_text(preview, encoding="utf-8", newline="\n")
    destination = root / "console" / "challenges"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "workshop-home.md").write_text(sources["brief"], encoding="utf-8", newline="\n")
    (destination / "workshop-theme.css").write_text(theme, encoding="utf-8", newline="\n")
    shutil.copyfile(root / "README.md", destination / "README.md")
    (destination / "docs").mkdir(exist_ok=True)
    for _, relative in pages:
        if relative.startswith("docs/"):
            shutil.copyfile(root / relative, destination / relative)
    for number in range(1, 5):
        (destination / f"challenge-{number:02}.md").write_text(
            sources[f"mission-{number:02}"], encoding="utf-8", newline="\n",
        )


if __name__ == "__main__":
    build(Path(__file__).resolve().parents[1])
    print("Built index.html and console/challenges. Nothing was published or deployed.")
