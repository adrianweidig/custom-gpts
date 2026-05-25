# Offline Problem Briefings for the OpenWebUI Model Builder

Languages: [Deutsch](README.md) | [English](README.en.md)

This folder contains Markdown briefings for general OpenWebUI task models. Each file is written as input for the Custom GPT `OpenWebUI Model Builder`.

The briefings are intentionally **offline-first**:

- no web search
- no external RAGFlow or RAG dependency
- no mandatory knowledge bases
- base model always `coder`
- Jupyter/Python code interpreter as the central additional capability

## Use

1. Select a briefing that matches the desired task model.
2. Pass the content to the `OpenWebUI Model Builder`.
3. Review the generated model configuration before importing it into OpenWebUI.

Later, OpenWebUI users should select by problem rather than by base model, for example:

- "I need to analyze a document."
- "I need to create a presentation."
- "I need code generation."
- "I want to evaluate logs."
- "I want to prepare a support ticket."

## Important Files

- `00_INDEX.md`: overview of all problem briefings.
- `01_...` to `25_...`: individual briefings for concrete task models.

## Internationalization

The current briefings are German source artifacts. Additional language versions can be added next to the German files when they are needed. Technical model IDs and filenames intentionally remain slug-compatible and are not translated.
