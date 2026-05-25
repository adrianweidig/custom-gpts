# OpenWebUI Model Builder

Languages: [Deutsch](README.md) | [English](README.en.md)

Local project folder for the public GPT `OpenWebUI Model Builder`.

## ChatGPT Link

https://chatgpt.com/g/g-6a070eda8fdc81918ab61d4c4f1aa136-openwebui-model-builder

## Purpose

This GPT creates complete OpenWebUI model packages for concrete task models. In addition to a plausible `model.json`, it generates the associated prompt and knowledge files for reproducible model configurations.

## Included Files

| File | Purpose |
|---|---|
| `customgpt_infos.md` | GPT metadata and configuration notes |
| `systemprompt.md` | Package generation logic and output rules |
| `fachwissen.md` | OpenWebUI model and artifact knowledge |
| `bootloader.md` | Compact GPT setup text |
| `beispiel.md` | Example package output |
| `Problemfälle/` | Offline-first task briefings |

## Typical Use

Use this package to create OpenWebUI task models, model packages and knowledge files that can be reviewed before import.

## Internationalization

German is the default. The generated model descriptions can follow the user's language, but model IDs, filenames, JSON keys and import formats remain stable.
