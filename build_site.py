from pathlib import Path
import shutil


ROOT = Path("/Volumes/Extreme SSD/プロラボサウナ/lp-wireframes-site")
PAGE_DIR = ROOT / "pages" / "magma-secret-ticket"
ASSETS_DIR = PAGE_DIR / "assets"
SOURCE_HTML = Path(
    "/Users/meguro/Library/Application Support/Claude/local-agent-mode-sessions/"
    "6cbd687b-c7d9-45b0-a208-b88a065d6b84/"
    "c9217f13-4c8b-44e4-afe8-1fbf6200541c/"
    "local_13fb8575-5252-4cf4-bbb1-e837fb1c7a69/outputs/MAGMA_LP構成案.html"
)


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    copies = {
        Path("/Users/meguro/Downloads/20220831prolabosauna4516.jpg"): ASSETS_DIR / "hero-bg.jpg",
        Path("/Users/meguro/Downloads/20220831prolabosauna4342.jpg"): ASSETS_DIR / "magma-bg.jpg",
        Path("/Users/meguro/Downloads/PLH_prolabo-sauna_logo_220207.jpg"): ASSETS_DIR / "prolabo-sauna-logo.jpg",
        Path("/Users/meguro/Downloads/変換画像/EPL_mainlogo_lp.png"): ASSETS_DIR / "esthe-pro-labo-logo.png",
        Path(
            "/Users/meguro/Library/Application Support/Claude/local-agent-mode-sessions/"
            "6cbd687b-c7d9-45b0-a208-b88a065d6b84/"
            "c9217f13-4c8b-44e4-afe8-1fbf6200541c/"
            "local_13fb8575-5252-4cf4-bbb1-e837fb1c7a69/outputs/room-floor-map-v2.jpg"
        ): ASSETS_DIR / "room-floor-map-v2.jpg",
        Path(
            "/Users/meguro/Library/Application Support/Claude/local-agent-mode-sessions/"
            "6cbd687b-c7d9-45b0-a208-b88a065d6b84/"
            "c9217f13-4c8b-44e4-afe8-1fbf6200541c/"
            "local_13fb8575-5252-4cf4-bbb1-e837fb1c7a69/outputs/sauna-room-photo.jpg"
        ): ASSETS_DIR / "sauna-room-photo.jpg",
        Path(
            "/Users/meguro/Library/Application Support/Claude/local-agent-mode-sessions/"
            "6cbd687b-c7d9-45b0-a208-b88a065d6b84/"
            "c9217f13-4c8b-44e4-afe8-1fbf6200541c/"
            "local_13fb8575-5252-4cf4-bbb1-e837fb1c7a69/outputs/cold-bath-photo.png"
        ): ASSETS_DIR / "cold-bath-photo.png",
        Path(
            "/Users/meguro/Library/Application Support/Claude/local-agent-mode-sessions/"
            "6cbd687b-c7d9-45b0-a208-b88a065d6b84/"
            "c9217f13-4c8b-44e4-afe8-1fbf6200541c/"
            "local_13fb8575-5252-4cf4-bbb1-e837fb1c7a69/outputs/private-shower-room.jpg"
        ): ASSETS_DIR / "private-shower-room.jpg",
        Path(
            "/Users/meguro/Library/Application Support/Claude/local-agent-mode-sessions/"
            "6cbd687b-c7d9-45b0-a208-b88a065d6b84/"
            "c9217f13-4c8b-44e4-afe8-1fbf6200541c/"
            "local_13fb8575-5252-4cf4-bbb1-e837fb1c7a69/outputs/premium-ticket-system.jpg"
        ): ASSETS_DIR / "premium-ticket-system.jpg",
    }
    for src, dest in copies.items():
        shutil.copy2(src, dest)

    html = SOURCE_HTML.read_text(encoding="utf-8")
    replacements = {
        "file:///Users/meguro/Downloads/20220831prolabosauna4516.jpg": "assets/hero-bg.jpg",
        "file:///Users/meguro/Downloads/20220831prolabosauna4342.jpg": "assets/magma-bg.jpg",
        "file:///Users/meguro/Downloads/PLH_prolabo-sauna_logo_220207.jpg": "assets/prolabo-sauna-logo.jpg",
        "file:///Users/meguro/Downloads/%E5%A4%89%E6%8F%9B%E7%94%BB%E5%83%8F/EPL_mainlogo_lp.png": "assets/esthe-pro-labo-logo.png",
        "room-floor-map-v2.jpg": "assets/room-floor-map-v2.jpg",
        "sauna-room-photo.jpg": "assets/sauna-room-photo.jpg",
        "cold-bath-photo.png": "assets/cold-bath-photo.png",
        "private-shower-room.jpg": "assets/private-shower-room.jpg",
        "premium-ticket-system.jpg": "assets/premium-ticket-system.jpg",
    }
    for old, new in replacements.items():
        html = html.replace(old, new)

    (PAGE_DIR / "index.html").write_text(html, encoding="utf-8")
    print(PAGE_DIR / "index.html")


if __name__ == "__main__":
    main()
