# Thin BinderHub wrapper around the published ml-platform-gpu image, so
# BinderHub launches it without rebuilding ml_platform from source.
#
# On main this tracks :latest (the HEAD of ml_platform main) and Renovate
# updates the digest whenever :latest moves. Release tags pin a CalVer tag
# instead (see README.md). The digest is always present because BinderHub
# caches builds by commit: a FROM line naming only a moving tag would never
# be rebuilt.
FROM hub.opensciencegrid.org/usatlas/ml-platform-gpu:latest@sha256:1c07508a71197458c6e13792ec0c17a1573e865f5fd99e82f08feed13f019b01
