# Contributing

Languages: [Deutsch](CONTRIBUTING.md) | [English](CONTRIBUTING.en.md)

Thank you for your interest in this repository. Since 24 May 2026, this repository is no longer actively developed. Contributions can still help make the existing GPT artifacts more precise, consistent or easier to understand, but review, merge and support are not guaranteed.

## Suitable Contributions

- fixes for README files, links, tables, headings or spelling
- well-founded improvements to `systemprompt.md`, `fachwissen.md`, `bootloader.md` or `customgpt_infos.md`
- new or improved example artifacts such as `beispiel.md`, `beispiel.py`, `beispiel.html`, `beispiel.json` or suitable test files
- new or improved problem briefings for the OpenWebUI Model Builder
- notes about unclear security, privacy, license or usage boundaries
- improvements to GitHub templates, repository hygiene or documentation navigation
- English language variants for central repository, community or package overview files

## Before Changing Files

1. Read the central [`README.en.md`](README.en.md) and the README of the affected GPT folder.
2. Check which artifacts belong together. For one GPT, this usually includes `README.md`, `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` and existing `beispiel.*` files.
3. Open an issue first for larger changes so that goal, scope and risks are clear. Issues are handled without a guaranteed response.

## Local Checks

This repository has no package manager, development server or central build.

Safe standard checks:

```powershell
git status --short --branch
git diff --check
python scripts/validate_repository_i18n.py
```

Also check manually:

- local Markdown links and image paths
- tables and headings
- UTF-8 text and Unicode characters
- consistent language links in `README.md`, `README.en.md`, package READMEs and `docs/de`/`docs/en`
- unchanged technical slugs, model IDs, filenames and URLs
- no real secrets, tokens, passwords, API keys, customer data or personal data

## Pull Request Process

1. Keep the diff small and focused on one topic.
2. Explain which GPT package or documentation area is affected.
3. Describe domain impact if prompt behavior changes.
4. List the checks you ran.
5. Link related issues where available.

Pull requests are reviewed best-effort. For active development or custom variants, a fork is the more reliable path.

## Style Rules

- Write clear and concrete documentation.
- Keep German as the default language and add English alternatives for central repository and community files.
- Use real UTF-8 characters in prose.
- Change technical IDs, slugs, filenames, URLs and model parameters only deliberately.
- Avoid broad rewrites without a domain reason.
- Delete icons, export artifacts, special documents or problem briefings only when it is clearly established that they are no longer needed.

## Security

Do not report security issues publicly as issues. Follow [`SECURITY.en.md`](SECURITY.en.md).

## Conduct

Collaboration follows [`CODE_OF_CONDUCT.en.md`](CODE_OF_CONDUCT.en.md). Feedback should be specific, respectful and focused on the repository.
