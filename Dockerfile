# Thin BinderHub wrapper around the published ml-platform-gpu image, so
# BinderHub launches it without rebuilding ml_platform from source.
#
# On main this tracks :latest (the HEAD of ml_platform main) and Renovate
# updates the digest whenever :latest moves. Release tags pin a CalVer tag
# instead (see README.md). The digest is always present because BinderHub
# caches builds by commit: a FROM line naming only a moving tag would never
# be rebuilt.
FROM hub.opensciencegrid.org/usatlas/ml-platform-gpu:latest@sha256:49fd28d706e767f74a37d70fd6b451c16101896f5bfba3f3dafbfe422df02de9
