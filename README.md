# ml_platform-gpu-binder

Thin [BinderHub](https://binderhub.af.uchicago.edu/) repository for the
`hub.opensciencegrid.org/usatlas/ml-platform-gpu` image built by
[maniaclab/ml_platform](https://github.com/maniaclab/ml_platform). The
`Dockerfile` is a single `FROM` line, so BinderHub launches the published image
instead of rebuilding ml_platform from source.

Launch:
<https://binderhub.af.uchicago.edu/v2/gh/maniaclab/ml_platform-gpu-binder/main>

## Refs

| Ref         | Base image                                             | Updated by                                                          |
| ----------- | ------------------------------------------------------ | ------------------------------------------------------------------- |
| `main`      | `ml-platform-gpu:latest@sha256:…` (ml_platform `main`) | Renovate, which merges each new `:latest` digest straight to `main` |
| `vYYYY.M.D` | `ml-platform-gpu:YYYY.M.D@sha256:…`                    | `tbump`, run on a `release/vYYYY.M.D` branch (below)                |

The `FROM` line always carries the digest. BinderHub caches builds by commit, so
a `FROM` line that only names a moving tag like `:latest` would never be
rebuilt.

## Releasing

Tag a release after ml_platform has published the matching CalVer image. The
release commit never goes to `main`, which keeps following `:latest`:

```bash
git switch -c release/v2026.8.17 origin/main
git push -u origin release/v2026.8.17
pixi run -e dev tbump 2026.8.17
```

`tbump` bumps the version, pins the `FROM` line to `:2026.8.17` and its digest
(`scripts/pin_base.py`), then commits, tags `v2026.8.17` and pushes.

To re-pin `main` by hand (Renovate normally does this):

```bash
pixi run -e dev pin-base latest
```

## Development

```bash
pixi run -e dev pre-commit
```
