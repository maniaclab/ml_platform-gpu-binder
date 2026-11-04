"""Pin the Dockerfile's base image to a tag of the ml-platform image and that tag's current digest.

Usage: python scripts/pin_base.py <tag>   (e.g. ``latest`` or ``2026.8.17``)

The digest is part of the FROM line so that every change to the base image is a
new commit: BinderHub caches builds by commit, so a FROM line that only names a
moving tag would never be rebuilt.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

DOCKERFILE = Path(__file__).resolve().parent.parent / "Dockerfile"
FROM_RE = re.compile(
    r"^FROM (?P<registry>[^/\s]+)/(?P<repository>[^:@\s]+):[^@\s]+@sha256:[0-9a-f]{64}$",
    re.MULTILINE,
)
MANIFEST_TYPES = ", ".join(
    [
        "application/vnd.oci.image.index.v1+json",
        "application/vnd.docker.distribution.manifest.list.v2+json",
        "application/vnd.oci.image.manifest.v1+json",
        "application/vnd.docker.distribution.manifest.v2+json",
    ]
)


def resolve_digest(registry: str, repository: str, tag: str) -> str:
    """Return the digest the registry currently serves for ``repository:tag`` (anonymous pull)."""
    token_url = (
        f"https://{registry}/service/token?service=harbor-registry"
        f"&scope=repository:{repository}:pull"
    )
    with urllib.request.urlopen(token_url, timeout=30) as resp:
        token = json.load(resp)["token"]
    request = urllib.request.Request(
        f"https://{registry}/v2/{repository}/manifests/{tag}",
        method="HEAD",
        headers={"Authorization": f"Bearer {token}", "Accept": MANIFEST_TYPES},
    )
    with urllib.request.urlopen(request, timeout=30) as resp:
        return resp.headers["Docker-Content-Digest"]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    tag = sys.argv[1]
    text = DOCKERFILE.read_text()
    match = FROM_RE.search(text)
    if match is None:
        print(f"no pinned FROM line found in {DOCKERFILE}", file=sys.stderr)
        return 1
    registry, repository = match["registry"], match["repository"]
    try:
        digest = resolve_digest(registry, repository, tag)
    except urllib.error.HTTPError as exc:
        print(f"cannot resolve {registry}/{repository}:{tag}: {exc}", file=sys.stderr)
        return 1
    new_from = f"FROM {registry}/{repository}:{tag}@{digest}"
    DOCKERFILE.write_text(text[: match.start()] + new_from + text[match.end() :])
    print(new_from)
    return 0


if __name__ == "__main__":
    sys.exit(main())
