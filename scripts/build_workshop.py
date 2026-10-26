"""Rebuild the local review page and HackboxConsole content; never deploys."""
import html
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown


def rebase_links(text: str, source: str, destination: str) -> str:
    def replace(match: re.Match[str]) -> str:
        target = urlsplit(match[2])
        if target.scheme or target.netloc or not target.path or target.path.startswith("/"):
            return match[0]
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), target.path))
        relative = posixpath.relpath(resolved, posixpath.dirname(destination) or ".")
        return match[1] + urlunsplit(("", "", relative, target.query, target.fragment)) + match[3]
    return re.sub(r"(!?\[[^\]]*\]\()([^\s)]+)(\))", replace, text)


def build(root: Path) -> None:
    pages = [
        ("brief", "docs/START_HERE.md"), ("architecture", "docs/architecture.md"),
        ("setup", "docs/environment-setup.md"), ("repository", "README.md"),
        *((f"mission-{number:02}", f"docs/mission-{number:02}.md") for number in range(1, 5)),
        ("bonus", "docs/bonus.md"),
        ("code-setup", "docs/code-extension/setup.md"),
        *((f"code-{number:02}", f"docs/code-extension/mission-{number:02}.md") for number in range(1, 5)),
    ]
    sources = {name: (root / path).read_text(encoding="utf-8") for name, path in pages}
    links = {path: f"#{name}" for name, path in pages}
    links["/challenges"] = "#mission-01"
    sections = []
    for name, source in pages:
        body = markdown.markdown(rebase_links(sources[name], source, "index.html"),
                                 extensions=["fenced_code", "tables"])
        for target, replacement in links.items():
            body = body.replace(f'href="{target}"', f'href="{replacement}"')
        sections.append(f'<section id="{html.escape(name)}" class="review-card" hidden>{body}</section>')
    theme = (root / "web" / "theme.css").read_text(encoding="utf-8")
    template = (root / "web" / "review.html").read_text(encoding="utf-8")
    preview = template.replace("{{THEME}}", theme).replace("{{CONTENT}}", "\n".join(sections))
    (root / "index.html").write_text(preview, encoding="utf-8", newline="\n")
    destination = root / "console" / "challenges"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "workshop-home.md").write_text(
        rebase_links(sources["brief"], "docs/START_HERE.md", "workshop-home.md"),
        encoding="utf-8", newline="\n",
    )
    (destination / "workshop-theme.css").write_text(theme, encoding="utf-8", newline="\n")
    shutil.copyfile(root / "README.md", destination / "README.md")
    (destination / "examples").mkdir(exist_ok=True)
    shutil.copyfile(root / "examples" / "agent_blueprint.py", destination / "examples" / "agent_blueprint.py")
    (destination / "docs").mkdir(exist_ok=True)
    for _, relative in pages:
        if relative.startswith("docs/"):
            (destination / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / relative, destination / relative)
    assets = destination / "docs" / "assets"
    assets.mkdir(exist_ok=True)
    shutil.copyfile(root / "docs" / "assets" / "github-join.png", assets / "github-join.png")
    for number in range(1, 5):
        (destination / f"challenge-{number:02}.md").write_text(
            rebase_links(sources[f"mission-{number:02}"], f"docs/mission-{number:02}.md", f"challenge-{number:02}.md"),
            encoding="utf-8", newline="\n",
        )


if __name__ == "__main__":
    build(Path(__file__).resolve().parents[1])
    print("Built index.html and console/challenges. Nothing was published or deployed.")
