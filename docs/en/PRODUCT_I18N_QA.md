# Product i18n Quality Review

Languages: [Deutsch](../de/PRODUCT_I18N_QA.md) | [English](PRODUCT_I18N_QA.md)

## Result

The product language packs were reviewed and corrected again on 25 May 2026. No DeepL connector or DeepL MCP server was available in this Codex instance; the review therefore used local generator validation, structured spot checks, UTF-8 and Unicode validation, and targeted searches for remaining English boilerplate.

## Reviewed Scope

- 11 central GPT product folders
- 10 product languages: `en`, `es`, `fr`, `pt-BR`, `it`, `nl`, `pl`, `tr`, `zh-Hans`, `ja`
- 660 localized Markdown components
- 110 localized `systemprompt.md` files

## Corrections

- Localized section headings in product language packs.
- Localized language-link rows.
- Localized component titles, for example system prompt, knowledge file and example.
- Localized locale rules for each language.
- Extended validation so non-English product packs must not contain English boilerplate headings such as `Languages:`, `Canonical Source Files` or `Locale Rules`, or an untranslated `fallback` residue.

## Review Boundaries

The language packs are intentionally localized product overlays, not legally or domain-certified full translations of all German source artifacts. The German sources remain canonical. Security, privacy, medical and legal statements remain subject to human review before production use.

## Checks Run

```powershell
python scripts/generate_product_i18n.py
python scripts/validate_repository_i18n.py
git diff --check
```

Spanish, Chinese Simplified and Japanese samples were additionally checked manually against the generator logic. A targeted `rg` search for English boilerplate in non-English product packs returned no matches.
