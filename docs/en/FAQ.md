# FAQ

Languages: [Deutsch](../de/FAQ.md) | [English](FAQ.md)

## Is This Repository an Installable Application?

No. It is a Markdown and asset collection for multiple Custom GPT configurations.

## How Do I Use a GPT Directly?

Open the matching ChatGPT link in the central [`README.en.md`](../../README.en.md) or in the README of the respective GPT folder.

## How Do I Review a GPT Locally?

Start in the respective folder with `README.md` or `README.en.md`. Then read `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` and any `beispiel.*` files together, because those files jointly describe behavior, positioning and expected output quality.

## What Are `beispiel.md` or `beispiel.*` Files For?

They provide a complete sample result. For advisory, analysis or text GPTs this is usually `beispiel.md`. For coding or file-generator GPTs, concrete artifacts such as `beispiel.py`, `beispiel_test.py`, `beispiel.html` or `beispiel.json` may be used.

## Why Are Some Filenames or IDs Not Translated?

Technical slugs, model IDs, filenames, URLs and parameters intentionally remain stable. They may be referenced by prompt artifacts, exports or target systems.

## How Does Repository Internationalization Work?

German is the default. English alternative files sit next to the German files, for example `README.en.md`, `CONTRIBUTING.en.md` or `docs/en/index.md`. GitHub does not translate the normal repository view automatically; users switch languages through visible links.

## Do the GPTs Detect the System Language Automatically?

The repository itself has no runtime. Many GPT artifacts respond to the language of the user request or explicit language instructions. If no reliable language is available, German is the fallback.

## May I Add Real Credentials to Examples?

No. Real secrets, tokens, passwords, API keys, customer data and personal data do not belong in this repository.

## Are There Automated Tests?

There is no domain-level test run for GPT behavior. The Repository Health workflow checks documentation structure, local Markdown links, referenced images, required i18n files, UTF-8 and Unicode fixtures. Domain prompt changes still require manual review.

## Can I Contribute New GPT Packages?

Yes, if purpose, target group, files, safety boundaries, language behavior and at least one example artifact are clearly documented. For larger additions, open an issue first.
