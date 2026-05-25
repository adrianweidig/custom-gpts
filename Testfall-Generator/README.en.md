# Testfall-Generator

Languages: [Deutsch](README.md) | [English](README.en.md)

Local project folder for a Custom GPT that derives structured test cases from requirements, user stories, bug reports and acceptance criteria.

## Status

Prepared GPT package without a public ChatGPT link.

## Purpose

This GPT creates traceable test case collections with preconditions, test data, steps, expected results, edge cases and risk notes. It is suitable for manual tests, regression tests and preparation of automated tests.

## Included Files

| File | Purpose |
|---|---|
| `customgpt_infos.md` | GPT metadata and usage framing |
| `systemprompt.md` | Test design logic and output rules |
| `fachwissen.md` | QA, test case and risk-based testing knowledge |
| `bootloader.md` | Compact GPT setup text |
| `beispiel.md` | Example test case set |

## Typical Use

Use this package when requirements or bug reports must be converted into clear, executable and reviewable test cases.

## Internationalization

German is the default language. Test titles and steps can follow the user's language, while issue IDs, requirement IDs, field names and automation selectors stay unchanged.
