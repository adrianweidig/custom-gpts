# Beispiel: n8n-Workflow-Muster mit sicherer Credential-Behandlung

## Beispielauftrag

> Erstelle einen n8n-Workflow, der täglich einen Support-Report aus einem Webhook-Dummy entgegennimmt, die Daten normalisiert und eine Zusammenfassung an einen Team-Chat sendet. Nutze keine echten Credentials und keine produktiven URLs.

## Annahmen

- Ziel ist ein importierbarer Entwurf, kein produktiver Workflow.
- Chat-Zielsystem wird als Platzhalter beschrieben.
- Credentials werden nach dem Import im n8n UI zugeordnet.
- Testdaten sind synthetisch.

## Kurzbeschreibung

Der Workflow nimmt Supportdaten per Webhook entgegen, prüft Pflichtfelder, erzeugt eine kompakte Textzusammenfassung und sendet sie an einen Chat-Node. Produktive URLs, Tokens und Credential-IDs werden nicht im JSON hinterlegt.

## Benötigte Credentials / Variablen

| Name | Zweck | Hinterlegung |
|---|---|---|
| `TEAM_CHAT_CREDENTIAL` | Authentifizierung für Chat-API | n8n Credentials UI |
| `REPORT_CHANNEL_ID` | Zielkanal | Umgebungsvariable oder manuelle Node-Konfiguration |

## Import-Hinweise

1. Workflow in n8n importieren.
2. Webhook-Pfad prüfen und für Testumgebung anpassen.
3. Chat-Credential im UI zuordnen.
4. Testdaten senden.
5. Fehlerpfade prüfen, bevor ein Schedule ergänzt wird.

## Workflow-JSON

```json
{
  "name": "Support Report Normalizer",
  "nodes": [
    {
      "parameters": {
        "path": "support-report-test",
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "id": "Webhook_Support_Report",
      "name": "Webhook: Support Report",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300]
    },
    {
      "parameters": {
        "jsCode": "const input = $json;\\nconst required = ['date', 'ticketsOpened', 'ticketsClosed', 'criticalIssues'];\\nconst missing = required.filter((key) => input[key] === undefined || input[key] === null || input[key] === '');\\nif (missing.length) {\\n  return [{ json: { ok: false, error: `Missing required fields: ${missing.join(', ')}` } }];\\n}\\nreturn [{ json: { ok: true, summary: `Support Report ${input.date}: ${input.ticketsOpened} opened, ${input.ticketsClosed} closed, critical issues: ${input.criticalIssues}.` } }];"
      },
      "id": "Normalize_Report",
      "name": "Normalize Report",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [520, 300]
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.ok }}",
              "value2": true
            }
          ]
        }
      },
      "id": "IF_Valid_Report",
      "name": "IF Valid Report",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [780, 300]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ { received: true, message: $json.summary } }}"
      },
      "id": "Respond_OK",
      "name": "Respond OK",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1040, 220]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ { received: false, error: $json.error } }}",
        "options": {
          "responseCode": 400
        }
      },
      "id": "Respond_Error",
      "name": "Respond Error",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1040, 400]
    }
  ],
  "connections": {
    "Webhook: Support Report": {
      "main": [
        [
          {
            "node": "Normalize Report",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize Report": {
      "main": [
        [
          {
            "node": "IF Valid Report",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Valid Report": {
      "main": [
        [
          {
            "node": "Respond OK",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Respond Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

## Testdaten

```json
{
  "date": "2026-05-24",
  "ticketsOpened": 18,
  "ticketsClosed": 21,
  "criticalIssues": 1
}
```

## Erwartetes Testergebnis

```json
{
  "received": true,
  "message": "Support Report 2026-05-24: 18 opened, 21 closed, critical issues: 1."
}
```

## Sicherheitshinweise

- Keine echten Chat-API-URLs im Workflow hinterlegen.
- Credentials erst nach Import im n8n UI zuordnen.
- Webhook vor produktiver Nutzung mit Authentifizierung, IP-Filter oder Gateway-Schutz versehen.
- Fehlerpfade mit fehlenden Pflichtfeldern testen.

## Offene produktive Entscheidungen

- Zielsystem und Node-Typ für Chat-Integration.
- Authentifizierung des Webhooks.
- Aufbewahrung und Logging der Supportdaten.
- Rate-Limits und Retry-Verhalten.
