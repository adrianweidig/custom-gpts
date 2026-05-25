# Dokumentation

Sprachen: [Deutsch](index.md) | [English](../en/index.md)

Dies ist die deutsche Standarddokumentation für das Repository `custom-gpts`.

## Einstieg

- [Repository-Startseite](../../README.md)
- [FAQ](FAQ.md)
- [Internationalisierung](I18N.md)
- [Release-Prozess](RELEASE_PROCESS.md)
- [Maintainer-Checkliste](MAINTAINER_CHECKLIST.md)

## Sprachstandard

Deutsch ist die Standardsprache des Repositorys. Englisch ist die wichtigste Alternativsprache. GitHub schaltet die normale Repository-Ansicht nicht automatisch nach Besuchersprache um; deshalb werden Sprachversionen über sichtbare Links und parallele Dateien gepflegt.

## Repository-Art

Dieses Repository ist eine Markdown-/Prompt-Artefaktsammlung. Es gibt keinen zentralen Dev-Server, kein Anwendungspaket und keine Runtime, die eine technische Locale-Erkennung für UI oder CLI ausführen könnte.

## Prüfungen

Relevante lokale Prüfungen:

```powershell
git diff --check
python scripts/validate_repository_i18n.py
git status --short --branch
```
