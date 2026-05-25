# n8n Workflow Architect

Languages: [Deutsch](README.md) | [English](README.en.md)

Local project folder for the public GPT `n8n Workflow Architect`.

## ChatGPT Link

https://chatgpt.com/g/g-6a06f5d8d0ac81918ce368d8db8a9bf5-n8n-workflow-architect

## Purpose

This GPT converts natural-language requirements into importable n8n workflow JSON. It considers operating model, services, credentials, safety boundaries, testability and documentation needs.

## Included Files

| File | Purpose |
|---|---|
| `customgpt_infos.md` | GPT metadata and configuration notes |
| `systemprompt.md` | Workflow generation rules and safety boundaries |
| `fachwissen.md` | n8n workflow and integration knowledge |
| `bootloader.md` | Compact GPT setup text |
| `beispiel.md` | Example workflow output |

## Typical Use

Use this package to create or review n8n workflows, especially when credentials, dry runs and import safety must be handled explicitly.

## Internationalization

German is the default language. User-facing explanations can follow the user's language, but JSON node fields, credential names, expressions and n8n-specific identifiers are not translated unless n8n itself requires it.
