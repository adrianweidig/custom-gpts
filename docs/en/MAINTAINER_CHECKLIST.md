# Maintainer Checklist

Languages: [Deutsch](../de/MAINTAINER_CHECKLIST.md) | [English](MAINTAINER_CHECKLIST.md)

This file documents completed repository settings and remaining steps that require GitHub permissions, UI access or deliberate maintainer decisions.

## Completed on 2026-05-24

- Repository description set: `Curated Custom GPT configurations, system prompts, knowledge files and documentation.`
- Topics set: `custom-gpt`, `prompt-engineering`, `chatgpt`, `openwebui`, `n8n`, `documentation`.
- Discussions enabled.
- Security Policy published.
- Private Vulnerability Reporting enabled.
- Vulnerability Alerts enabled.
- Dependabot Security Updates enabled.
- Secret Scanning and Push Protection enabled.
- Branch Protection configured for `main`:
  - Required Status Check: `Documentation and link health`
  - branch must be up to date before merge
  - one approving review required for pull requests
  - stale reviews are dismissed on new commits
  - conversation resolution required
  - force pushes and branch deletion disabled
- Social preview PNG created: [`docs/assets/social-preview.png`](../assets/social-preview.png)
- Curated snapshot release `public-readiness-2026-05-24` prepared.

## Completed on 2026-05-25

- German default structure with English alternative files added.
- `docs/de/` and `docs/en/` created as explicit documentation routes.
- Repository Health workflow extended with i18n, language-link and Unicode checks.

## GitHub Repository Settings

- Upload the social preview from [`docs/assets/social-preview.png`](../assets/social-preview.png) in the GitHub UI. GitHub documents this through `Settings` -> `Social preview`; no direct REST or GitHub CLI upload was available.
- Check whether Wiki and Projects are still needed. Both features were already enabled and were not disabled to avoid affecting existing external workspaces.
- GitHub Pages is not enabled as new infrastructure. If a project website is added later, German should be the default route and English the first alternative route.

## Security

- Enable Code Scanning only if analyzable application code is added later. No CodeQL workflow is configured for the current Markdown and asset collection.

## Branch Protection

- Branch Protection is configured. If workflow names change later, the required status check must be updated accordingly.

## Releases

- Curated documentation states use the tag schema `public-readiness-YYYY-MM-DD`.
- Introduce SemVer only if package-like artifacts with clear compatibility statements are added later.

## License and External Assets

- The MIT license is present in the repository.
- Published GPT contents, icons, external sources, training data, trademarks and external media should receive additional legal review when needed.
- Do not use copyright-unclear images or logos as social preview assets.
