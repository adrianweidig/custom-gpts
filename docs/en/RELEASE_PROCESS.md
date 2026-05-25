# Release Process

Languages: [Deutsch](../de/RELEASE_PROCESS.md) | [English](RELEASE_PROCESS.md)

This repository has no package publication. Curated repository states can be published as GitHub Releases with descriptive snapshot tags when needed.

## When a Release Makes Sense

A GitHub Release can make sense when:

- several GPT packages have reached a stable public state
- a curated snapshot should be referenceable for users
- larger structural changes are complete
- external documentation should point to a fixed state

## Recommended Flow

1. Review open pull requests and issues for the planned state.
2. Update `CHANGELOG.md` and `CHANGELOG.en.md`.
3. Run `git diff --check`.
4. Run `python scripts/validate_repository_i18n.py`.
5. Verify that the Repository Health workflow is green on `main`.
6. Manually review critical links, GPT folders and security notes.
7. Create a Git tag with a descriptive name, for example `public-readiness-YYYY-MM-DD` for curated documentation states.
8. Derive GitHub Release notes from the changelog.

## No Automatic Publication

This repository has no release automation. Releases should be created intentionally by maintainers.
