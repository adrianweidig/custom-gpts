# Codex Project Readiness

Languages: [Deutsch](CODEX_PROJECT_READINESS.md) | [English](CODEX_PROJECT_READINESS.en.md)

## Summary

The project has been reviewed in the current work context. It is a usable Markdown and prompt artifact repository without a central software application, package manager or domain test framework. Git and GitHub are configured. Public use is supported by community documentation, issue and pull request templates, a Repository Health workflow and an explicit German/English documentation structure.

## Project Root

`E:\Codex_Workspace\repos\custom-gpts`

Determined via `git rev-parse --show-toplevel`.

## Project Type

Documentation and prompt artifact repository for multiple Custom GPT configurations.

Important contents:

- central German project documentation in `README.md`
- English landing page in `README.en.md`
- project-specific Codex rules in `AGENTS.md`
- GPT subfolders with `README.md`, `README.en.md`, `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` and sometimes assets
- new GPT subfolders can additionally include `beispiel.md` or suitable `beispiel.*` files as sample artifacts
- problem briefings under `OpenWebUI Model Builder/Problemfälle/`
- explicit documentation routes under `docs/de/` and `docs/en/`

## Dependencies

No central dependencies are present.

Not found:

- `package.json`
- JavaScript or Node lockfiles
- `pyproject.toml`
- `requirements.txt`
- `Cargo.toml`
- `go.mod`
- Docker or Compose manifests

No installation is required.

## Tests and Builds

There is no central build, domain test, lint or typecheck process. Suitable local checks are:

```powershell
git diff --check
python scripts/validate_repository_i18n.py
git status --short --branch
```

The Repository Health workflow checks required files, i18n structure, local Markdown links, referenced images, UTF-8, German umlaut spelling and Unicode fixtures.

## Internationalization State

- German is the repository default language.
- English is the primary alternative language.
- GitHub's normal repository view does not automatically switch by visitor language; visible language links and parallel files provide navigation.
- GPT source artifacts remain German unless a domain-reviewed translation exists.
- Technical IDs, filenames, URLs, JSON keys, model parameters and import formats are not translated.
- If no reliable language is available in future runtime code, German is the documented fallback.

## Startability

There is no development server and no central application. The project is usable directly through Markdown and asset files.

## Codex Usability

Codex can work on the project effectively:

- `AGENTS.md` contains clear project rules.
- `README.md` and `README.en.md` describe structure, usage, workflow and community processes.
- `.gitignore` excludes typical local artifacts, caches, logs and `.env` files.
- `.github/` contains issue and pull request templates and a Repository Health workflow.
- `docs/de/` and `docs/en/` contain explicit multilingual documentation routes.

## Security and Sensitive Files

- `.gitignore` ignores `.env`, `.env.*`, logs, temporary files and common cache directories.
- No versioned files with sensitive filenames such as `.env`, private keys, credential, token or password files were found in the prior readiness review.
- Examples should use obvious placeholders such as `YOUR_API_KEY` only.

## Manual Tasks

- Upload the social preview from `docs/assets/social-preview.png` through the GitHub web UI if desired.
- Check whether Wiki and Projects are still needed.
- Perform domain and legal review before production publication of individual GPT artifacts.

## End State

The project is directly usable and better prepared for public German and English navigation. The changes affect documentation, GitHub collaboration and repository hygiene; the domain core of the GPT artifacts remains intentionally stable.
