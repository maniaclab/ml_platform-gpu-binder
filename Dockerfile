# Thin BinderHub wrapper around the published ml-platform-gpu image, so
# BinderHub launches it without rebuilding ml_platform from source.
#
# On main this tracks :latest (the HEAD of ml_platform main) and Renovate
# updates the digest whenever :latest moves. Release tags pin a CalVer tag
# instead (see README.md). The digest is always present because BinderHub
# caches builds by commit: a FROM line naming only a moving tag would never
# be rebuilt.
FROM hub.opensciencegrid.org/usatlas/ml-platform-gpu:2026.11.4@sha256:3534859c71bbfff6f60c44c599cd63ece6e0f09f2becb8b13a9e26e61bebdd49
