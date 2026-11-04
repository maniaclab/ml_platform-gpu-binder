# Thin BinderHub wrapper around the published ml-platform-gpu image, so
# BinderHub launches it without rebuilding ml_platform from source.
#
# On main this tracks :latest (the HEAD of ml_platform main) and Renovate
# updates the digest whenever :latest moves. Release tags pin a CalVer tag
# instead (see README.md). The digest is always present because BinderHub
# caches builds by commit: a FROM line naming only a moving tag would never
# be rebuilt.
FROM hub.opensciencegrid.org/usatlas/ml-platform-gpu:2026.8.17@sha256:3c97c6af848fb066f6596ac28b95277c275baf06d1e76240fbfbffacb78e2da1
