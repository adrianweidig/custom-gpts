# Produkt-i18n-Qualitätsprüfung

Sprachen: [Deutsch](PRODUCT_I18N_QA.md) | [English](../en/PRODUCT_I18N_QA.md)

## Ergebnis

Die Produkt-Sprachpakete wurden am 25. Mai 2026 erneut geprüft und korrigiert. Ein DeepL-Connector oder DeepL-MCP war in dieser Codex-Instanz nicht verfügbar; die Prüfung erfolgte deshalb lokal über Generatorprüfung, strukturierte Stichproben, UTF-8-/Unicode-Validierung und eine gezielte Suche nach verbliebenem englischem Boilerplate.

## Geprüfter Umfang

- 11 zentrale GPT-Produktordner
- 10 Produktsprachen: `en`, `es`, `fr`, `pt-BR`, `it`, `nl`, `pl`, `tr`, `zh-Hans`, `ja`
- 660 lokalisierte Markdown-Komponenten
- 110 lokalisierte `systemprompt.md`-Dateien

## Korrekturen

- Abschnittsüberschriften der Produkt-Sprachpakete lokalisiert.
- Sprachlink-Zeilen lokalisiert.
- Komponententitel lokalisiert, zum Beispiel Systemprompt, Wissensdatei und Beispiel.
- Locale-Regeln pro Sprache lokalisiert.
- Validierung erweitert, damit nicht-englische Produktpakete keine englischen Boilerplate-Überschriften wie `Languages:`, `Canonical Source Files` oder `Locale Rules` und keinen unübersetzten `fallback`-Restbegriff enthalten dürfen.

## Prüfgrenzen

Die Sprachpakete sind bewusst lokalisierte Produkt-Overlays, keine vollständigen juristisch oder fachlich zertifizierten Übersetzungen der gesamten deutschen Quellartefakte. Die deutschen Quellen bleiben kanonisch. Sicherheits-, Datenschutz-, medizinische und rechtliche Aussagen bleiben vor produktiver Nutzung menschlich prüfpflichtig.

## Ausgeführte Prüfungen

```powershell
python scripts/generate_product_i18n.py
python scripts/validate_repository_i18n.py
git diff --check
```

Zusätzlich wurden Stichproben in Spanisch, vereinfachtem Chinesisch und Japanisch manuell gegen die Generatorlogik geprüft. Eine gezielte `rg`-Suche nach englischem Boilerplate in nicht-englischen Produktpaketen lieferte keine Treffer.
