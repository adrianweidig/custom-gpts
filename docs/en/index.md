# Documentation

Languages: [Deutsch](../de/index.md) | [English](index.md)

This is the English documentation route for the `custom-gpts` repository.

## Start

- [Repository landing page](../../README.en.md)
- [FAQ](FAQ.md)
- [Internationalization](I18N.md)
- [Release process](RELEASE_PROCESS.md)
- [Maintainer checklist](MAINTAINER_CHECKLIST.md)

## Language Default

German is the repository default language. English is the most important alternative language. GitHub does not automatically switch the normal repository view based on a visitor's language, so language versions are maintained through visible links and parallel files.

## Repository Type

This repository is a Markdown and prompt artifact collection. It has no central development server, application package or runtime that could perform technical locale detection for UI or CLI output.

## Checks

Relevant local checks:

```powershell
git diff --check
python scripts/validate_repository_i18n.py
git status --short --branch
```
