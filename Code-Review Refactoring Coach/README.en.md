# Code-Review Refactoring Coach

Languages: [Deutsch](README.md) | [English](README.en.md)

Local project folder for a Custom GPT focused on structured code review, refactoring and maintainability analysis.

## Status

Prepared GPT package without a public ChatGPT link.

## Purpose

This GPT reviews code changes, individual files or small components for clarity, maintainability, defect risk, testability, security and practical refactoring options. It prioritizes concrete risks and improvements instead of enforcing unnecessary style preferences.

## Included Files

| File | Purpose |
|---|---|
| `customgpt_infos.md` | GPT metadata, positioning and configuration notes |
| `systemprompt.md` | Operating logic, review priorities and output rules |
| `fachwissen.md` | Review, refactoring and testing knowledge |
| `bootloader.md` | Compact instruction text for GPT setup |
| `beispiel.md` and `beispiel.*` | Sample review and test artifacts |

## Typical Use

Use this package when a small code change, component or pull request needs a pragmatic review with findings first, clear severity and concrete improvement options.

## Internationalization

German is the repository default. The GPT can work with code and comments in the project's existing language. Technical identifiers, filenames and APIs are not translated.
