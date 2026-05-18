# Grenzen und sichere Nutzung von Automatisierungsplattformen und KI-Agenten im Unternehmen

## Executive Summary für Führungskräfte

Automatisierungsplattformen und KI-Agenten können Unternehmen entlasten, Prozesse beschleunigen und Informationen besser nutzbar machen. Aus Sicht der Systemadministration gilt jedoch ein nüchterner Grundsatz:

> **Ein Agent kann nur das tun, wofür er Zugriff, Berechtigungen, Schnittstellen, Netzwerkwege und vertrauenswürdige Datenquellen besitzt.**

Daraus folgt: Ein KI-Agent ist kein „magisches“ System, sondern ein technischer Akteur mit Identität, Rechten, Datenzugriffen, Netzwerkverbindungen, Protokollierungspflichten und Betriebsrisiken.

Für Unternehmen ist deshalb nicht die Frage entscheidend, ob Automatisierung technisch möglich ist. Entscheidend ist:

* Ist sie **organisatorisch freigegeben**?
* Ist sie **technisch sauber betreibbar**?
* Ist sie **sicher begrenzt**?
* Ist sie **auditierbar**?
* Ist sie **datenschutzrechtlich bewertet**?
* Ist klar, **wer verantwortlich ist**, wenn etwas falsch läuft?

Aktuelle Sicherheitsrahmenwerke unterstützen genau diese Sichtweise. ISO/IEC 27001 beschreibt Informationssicherheitsmanagement als risikobasierten Prozess, der zur Größe, Struktur und Zielsetzung einer Organisation passen muss. ([ISO][1]) Der BSI IT-Grundschutz bietet dafür praxisorientierte Bausteine und Anforderungen für Informationssicherheit. ([BSI][2]) Zero Trust verschiebt den Fokus weg vom reinen Netzwerkperimeter hin zu Benutzern, Ressourcen, Geräten und kontinuierlicher Prüfung. ([NIST Computer Security Resource Center][3]) Für KI-Systeme sind zusätzlich Risiken wie Prompt Injection, unsichere Tool-Nutzung und Datenabfluss relevant, wie sie unter anderem in den OWASP-Empfehlungen zu LLM- und Agentensicherheit beschrieben werden. ([OWASP Foundation][4])

Die wichtigste Empfehlung für KI-Manager lautet:

> **Der sichere Einstieg ist häufig ein Nur-Lese- oder Vorschlagsmodus mit menschlicher Freigabe. Produktivzugriffe sollten erst nach Tests, Dokumentation, Berechtigungskonzept, Logging, Datenschutzbewertung und Notfallabschaltung erfolgen.**

---

# 1. Einleitung

Automatisierungsplattformen wie **n8n**, **Make**, **Zapier** und **Microsoft Power Automate** ermöglichen es Unternehmen, wiederkehrende Aufgaben zwischen Anwendungen zu verbinden. Typische Beispiele sind:

* Tickets automatisch klassifizieren
* E-Mails auswerten
* Daten aus Formularen übernehmen
* CRM-Daten aktualisieren
* Berichte erzeugen
* Dokumente zusammenfassen
* Genehmigungsprozesse starten
* Benachrichtigungen versenden

KI-Agenten erweitern diese Idee. Sie können nicht nur starre Wenn-dann-Abläufe ausführen, sondern Informationen interpretieren, Werkzeuge verwenden, Texte erzeugen, Daten abrufen oder Entscheidungsvorschläge vorbereiten.

Aus Sicht eines Systemadministrators ist dabei entscheidend:

> **Ein Agent handelt nicht im luftleeren Raum. Er benötigt Identität, Berechtigungen, Netzwerkzugang, Schnittstellen, Zertifikate, Datenquellen, Protokollierung und eine kontrollierte Betriebsumgebung.**

Ein Agent ohne Zugriff auf ein Ticketsystem kann keine Tickets aktualisieren. Ein Workflow ohne DNS-Auflösung erreicht keine API. Ein Container ohne interne Zertifikatskette kann interne HTTPS-Endpunkte nicht vertrauenswürdig aufrufen. Ein lokales LLM ohne Zugriff auf Dokumente kann keine unternehmensspezifischen Fragen beantworten.

Gleichzeitig bedeutet Zugriff immer Risiko. Je mehr ein Agent darf, desto größer wird der mögliche Schaden bei Fehlkonfiguration, Missbrauch, kompromittierten Tokens, fehlerhaften Prompts oder manipulierten Datenquellen.

## Kernaussage

Automatisierung und KI-Agenten sind nur dann sinnvoll, wenn technische Möglichkeit, organisatorische Freigabe und sicherer Betrieb zusammenpassen.

---

# 2. Grundprinzip: Linke und rechte Grenzen

## 2.1 Bedeutung des Begriffs

Mit „linken und rechten Grenzen“ ist gemeint:

* **Linke Grenze:** Was mindestens vorhanden sein muss, damit eine Automatisierung überhaupt funktionieren kann.
* **Rechte Grenze:** Was eine Automatisierung maximal dürfen sollte, damit der Betrieb sicher bleibt.

Dieses Denken hilft besonders bei Beratungen. Fachbereiche sehen oft nur den gewünschten Prozess. Die IT muss zusätzlich prüfen, welche Voraussetzungen fehlen und wo Sicherheitsgrenzen gesetzt werden müssen.

---

## 2.2 Linke Grenze

Die linke Grenze beschreibt die Mindestvoraussetzungen.

| Mindestvoraussetzung                          | Bedeutung                                                            |
| --------------------------------------------- | -------------------------------------------------------------------- |
| Benutzerkonto oder Servicekonto               | Der Workflow braucht eine technische Identität.                      |
| API-Zugang                                    | Systeme müssen maschinenlesbar erreichbar sein.                      |
| Netzwerkzugriff                               | Quelle und Ziel müssen sich erreichen können.                        |
| DNS-Auflösung                                 | Namen wie `crm.intern.local` müssen auflösbar sein.                  |
| Zertifikate                                   | HTTPS-Verbindungen müssen vertrauenswürdig sein.                     |
| Berechtigungen                                | Lesen, Schreiben, Löschen oder Ausführen müssen geregelt sein.       |
| Rollen                                        | Der Zugriff muss zum Zweck passen.                                   |
| Skriptausführung                              | Für Systemaktionen werden oft PowerShell, Bash oder Python benötigt. |
| Logging                                       | Aktionen müssen nachvollziehbar sein.                                |
| Monitoring                                    | Fehler müssen erkannt werden.                                        |
| Backup                                        | Workflows, Konfigurationen und Daten müssen wiederherstellbar sein.  |
| Freigabe durch IT oder Informationssicherheit | Produktivbetrieb benötigt Kontrolle und Verantwortung.               |

### Praxisbeispiel

Ein Fachbereich möchte, dass ein KI-Agent neue Benutzer im Active Directory anlegt.

**Linke Grenze:**

* Zugriff auf AD oder Microsoft Graph
* Servicekonto
* Berechtigungen zum Anlegen von Benutzern
* definierter Namensstandard
* Logging
* Freigabeprozess
* Testumgebung
* Genehmigung durch HR oder IT

Fehlt eines davon, kann der Agent den Prozess nicht sauber und sicher ausführen.

---

## 2.3 Rechte Grenze

Die rechte Grenze beschreibt, was maximal erlaubt sein sollte.

| Nicht empfehlenswerte Maximalfreiheit | Sichere Begrenzung                                         |
| ------------------------------------- | ---------------------------------------------------------- |
| Domänenadmin-Rechte für Agenten       | Delegierte Rechte auf genau benötigte OU oder API-Funktion |
| Freier Internetzugriff                | Whitelist, Proxy, Protokollierung                          |
| Freie PowerShell auf Produktivservern | Signierte Skripte, JEA, Runbooks                           |
| Unkontrollierte E-Mail-Versendung     | Entwurfsmodus oder Versand nach Freigabe                   |
| Direkte Änderung kritischer Systeme   | Genehmigungsworkflow                                       |
| Speicherung von API-Keys im Klartext  | Secret Management                                          |
| Zugriff auf alle Datenräume           | Rollenbasierter Zugriff                                    |
| Autonomes Löschen von Daten           | Nur Vorschlag oder Papierkorb mit Freigabe                 |

### Praxisbeispiel

Ein Agent soll Rechnungen vorprüfen.

**Sinnvolle rechte Grenze:**

* Er darf Rechnungen lesen.
* Er darf Beträge extrahieren.
* Er darf Auffälligkeiten markieren.
* Er darf einen Prüfbericht erstellen.
* Er darf keine Zahlung auslösen.
* Er darf keine Lieferantenstammdaten ändern.
* Er darf keine Bankverbindungen überschreiben.

---

## Kapitelzusammenfassung

Linke Grenzen verhindern unrealistische Erwartungen. Rechte Grenzen verhindern unsicheren Betrieb. Gute KI-Beratung erklärt beides gleichzeitig.

---

# 3. Technische Grundvoraussetzungen für Automatisierung und Agenten

| Voraussetzung                 | Warum sie benötigt wird                                     | Beispiel                                         | Was passiert, wenn sie fehlt?                | Mögliche Alternative                           |
| ----------------------------- | ----------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------- | ---------------------------------------------- |
| Netzwerkzugriff               | Systeme müssen erreichbar sein.                             | n8n ruft interne REST-API auf.                   | API-Aufruf schlägt fehl.                     | Integration Server im gleichen Netzsegment     |
| Internetzugriff               | Cloud-APIs und SaaS-Dienste benötigen externe Verbindung.   | Make ruft Cloud-CRM auf.                         | Cloud-Dienst ist nicht erreichbar.           | On-Prem-Plattform oder Proxy                   |
| DNS-Auflösung                 | Dienste werden meist per Name adressiert.                   | `ticketsystem.intern.local`                      | Verbindung scheitert trotz offener Firewall. | Hosts-Eintrag, interner DNS, Service Discovery |
| Proxy-Konfiguration           | Viele Unternehmen erzwingen ausgehenden Traffic über Proxy. | Power Automate Gateway oder Skript ruft API auf. | Verbindung nach außen wird blockiert.        | Proxy in Plattform konfigurieren               |
| Firewall-Regeln               | Verbindungen müssen erlaubt sein.                           | n8n zu Datenbank auf Port 5432                   | Timeout oder Verbindungsfehler               | Dedizierte Firewall-Freigabe                   |
| TLS-/SSL-Zertifikate          | Sichere Verbindungen benötigen Vertrauen.                   | Interne HTTPS-API                                | TLS-Fehler                                   | Interne CA verteilen                           |
| Interne Zertifizierungsstelle | Interne Systeme nutzen oft eigene Zertifikate.              | AD CS oder Unternehmens-CA                       | Container oder Agent vertrauen API nicht.    | CA-Bundle in Trust Store importieren           |
| Servicekonten                 | Automatisierungen brauchen technische Identität.            | `svc_n8n_ticketing`                              | Persönliche Konten werden missbraucht.       | Managed Identity oder dediziertes Servicekonto |
| API-Keys                      | Einfache technische Authentifizierung.                      | Zugriff auf SaaS-API                             | Workflow kann sich nicht authentifizieren.   | OAuth, Zertifikat, Token Broker                |
| OAuth                         | Delegierte und kontrollierte Zugriffe.                      | Microsoft Graph                                  | Keine Freigabe, kein Zugriff.                | Service Principal mit definierten Rechten      |
| Rollen- und Rechtekonzept     | Rechte müssen begrenzt werden.                              | Nur Ticket lesen und kommentieren                | Zu viele oder zu wenige Rechte               | RBAC-Modell definieren                         |
| Zugriff auf Datenbanken       | Strukturierte Daten müssen abrufbar sein.                   | SQL-Abfrage für Bericht                          | Keine automatisierte Datenauswertung         | API oder Exportdatei                           |
| Zugriff auf Dateifreigaben    | Viele KMU speichern Daten auf Fileservern.                  | Eingangsordner für Rechnungen                    | Agent sieht Dokumente nicht.                 | DMS, SharePoint, kontrollierter Import         |
| Zugriff auf E-Mail-Systeme    | E-Mail ist häufig Prozessauslöser.                          | Rechnungseingang per Mail                        | Keine automatische Auswertung                | Shared Mailbox mit Graph API                   |
| Zugriff auf Ticketsysteme     | Workflows sollen Tickets lesen oder schreiben.              | Jira, ServiceNow, OTRS, Zammad                   | Keine Ticketautomatisierung                  | CSV-Import, E-Mail-Schnittstelle               |
| Zugriff auf ERP-/CRM-Systeme  | Geschäftsprozesse liegen dort.                              | SAP, Dynamics, Salesforce                        | Keine Stammdaten- oder Prozessintegration    | API-Gateway, Export, Middleware                |
| Zugriff auf DMS               | Dokumente müssen auffindbar sein.                           | SharePoint, ELO, DocuWare                        | Kein RAG oder Dokumentenworkflow             | Geplanter Export in sicheren Datenraum         |
| PowerShell-Ausführung         | Windows-Verwaltung erfolgt häufig über PowerShell.          | AD-Abfrage, Exchange-Online                      | Viele Admin-Aktionen nicht möglich           | Graph API, signierte Runbooks                  |
| Skript-Ausführung unter Linux | Linux-Automatisierung nutzt Bash, Python, systemd.          | Logrotation prüfen                               | Keine lokale Automatisierung                 | REST-Agent, Ansible, Monitoring-API            |
| Container-Ausführung          | Viele Plattformen laufen containerisiert.                   | n8n, OpenWebUI, RAGFlow                          | Betrieb wird erschwert                       | VM-Installation, Managed Service               |
| Zugriff auf lokale LLMs       | Datenschutzfreundliche KI-Nutzung.                          | Ollama, vLLM                                     | Keine lokale Inferenz                        | Cloud-LLM mit Datenschutzprüfung               |
| Zugriff auf Cloud-LLMs        | Leistungsfähige Modelle und APIs.                           | ChatGPT API, Claude API, Gemini API              | Cloud-Agenten eingeschränkt                  | Lokale Modelle, Hybridmodell                   |
| Logging                       | Nachvollziehbarkeit und Fehleranalyse.                      | Workflow-Protokoll                               | Fehler und Missbrauch bleiben unklar.        | Zentrales Logsystem                            |
| Monitoring                    | Betriebszustand muss überwacht werden.                      | Container down, Token abgelaufen                 | Ausfälle werden spät erkannt.                | Prometheus, Grafana, SIEM                      |
| Backup                        | Wiederherstellung nach Fehlern.                             | n8n-Workflows, DB, Secrets                       | Verlust von Workflows oder Historie          | Snapshot, Datenbankbackup                      |
| Freigabeprozesse              | Produktivänderungen brauchen Kontrolle.                     | Workflow versendet Kundenmails                   | Schatten-IT und Risiko                       | Change-Prozess, Vier-Augen-Prinzip             |

## Empfehlung

| Variante                 | Beschreibung                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------ |
| Minimalvariante          | Einzelner Workflow mit Testdaten, Leserechten und manueller Freigabe.                      |
| Sichere Standardvariante | Servicekonto, RBAC, Logging, Backup, Proxy, Zertifikate, Dokumentation.                    |
| Erweiterte Variante      | IAM-Integration, SIEM, API-Gateway, Secret Vault, Change Management, getrennte Umgebungen. |
| Nicht empfehlenswert     | Persönlicher Admin-Account, Klartext-Secrets, keine Logs, direkter Produktivzugriff.       |

---

# 4. Berechtigungen und Identitäten

Berechtigungen sind der zentrale Sicherheitsfaktor. Ein Agent ist aus Administrationssicht ein technischer Benutzer. Er kann nur innerhalb seiner Rechte handeln. Sind diese Rechte zu hoch, entsteht ein Sicherheitsrisiko. Sind sie zu niedrig, funktioniert der Prozess nicht.

Microsoft beschreibt Least Privilege als Ansatz, bei dem Benutzer und Gruppen nur Zugriff auf Ressourcen, Daten und Aktionen erhalten, die für ihre Rolle relevant sind, und nicht darüber hinaus. ([Microsoft Learn][5]) Privileged Identity Management unterstützt zusätzlich zeitlich begrenzte privilegierte Zugriffe, Genehmigungen, MFA, Begründungen und Access Reviews. ([Microsoft Learn][6])

---

## 4.1 Benutzerkonto vs. Servicekonto

| Kontoart                              | Beschreibung                               | Typischer Einsatz            | Risiko                                                  |
| ------------------------------------- | ------------------------------------------ | ---------------------------- | ------------------------------------------------------- |
| Persönliches Benutzerkonto            | Konto einer realen Person                  | Manuelle Arbeit              | Passwortwechsel, Austritt, fehlende Nachvollziehbarkeit |
| Servicekonto                          | Technisches Konto für Dienst oder Workflow | n8n-Zugriff auf Ticketsystem | Zu hohe Rechte, vergessene Nutzung                      |
| Managed Identity                      | Plattformverwaltete Identität              | Azure, Microsoft Cloud       | Abhängigkeit von Plattform und korrekter Rollenvergabe  |
| API-Key                               | Einfaches Geheimnis für API-Zugriff        | SaaS-Integration             | Kann kopiert oder geleakt werden                        |
| OAuth-Token                           | Delegierter Zugriff mit Scopes             | Microsoft Graph, Google APIs | Zu breite Scopes, Token-Missbrauch                      |
| Zertifikatsbasierte Authentifizierung | Authentifizierung über Zertifikat          | mTLS, Service-to-Service     | Zertifikatsmanagement erforderlich                      |

---

## 4.2 Berechtigungsmodelle

| Berechtigungsmodell                   | Vorteil                               | Risiko                                                  | Empfehlung für Unternehmen                                                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Persönliches Konto                    | Schnell verfügbar                     | Schlechte Nachvollziehbarkeit, abhängig von Mitarbeiter | Nur für Tests, nicht für produktive Automatisierung                                 |
| Dediziertes Servicekonto              | Saubere technische Identität          | Muss dokumentiert und überwacht werden                  | Standard für On-Prem-Workflows                                                      |
| Managed Identity                      | Kein manuelles Secret nötig           | Stark plattformabhängig                                 | Sehr geeignet in Cloud-Umgebungen                                                   |
| API-Key                               | Einfach einzurichten                  | Häufig zu breit und lange gültig                        | Nur mit Vault, Rotation und minimalem Scope                                         |
| OAuth mit Scopes                      | Rechte können begrenzt werden         | Falsch konfigurierte Scopes geben zu viel Zugriff       | Für SaaS und M365 bevorzugt                                                         |
| Zertifikatsbasierte Authentifizierung | Stark für Service-to-Service          | Ablauf, Rotation und Trust Store müssen gepflegt werden | Geeignet für interne APIs und mTLS                                                  |
| RBAC                                  | Rollen statt Einzelrechte             | Rollen können zu grob sein                              | Standardmodell für größere Umgebungen                                               |
| Just-in-Time Access                   | Rechte nur zeitlich begrenzt          | Komplexer Betrieb                                       | Für kritische Aktionen sinnvoll                                                     |
| Just Enough Administration            | Nur definierte Admin-Aktionen erlaubt | Initialer Aufwand                                       | Für PowerShell- und Windows-Admin-Szenarien geeignet                                |
| Vier-Augen-Prinzip                    | Reduziert Fehlbedienung               | Verlangsamt Prozesse                                    | Pflichtnah bei kritischen Aktionen, auch wenn nicht gesetzlich immer vorgeschrieben |

---

## 4.3 Warum Agenten keine pauschalen Adminrechte erhalten sollten

Adminrechte sind für Agenten besonders kritisch, weil Agenten:

* Prompts falsch interpretieren können
* manipulierte Eingaben verarbeiten können
* externe Inhalte falsch bewerten können
* Tools versehentlich in falscher Reihenfolge nutzen können
* bei kompromittierten Zugangsdaten großen Schaden verursachen können

OWASP beschreibt bei KI-Agenten unter anderem Risiken wie Prompt Injection, Tool Abuse, Privilege Escalation und Datenabfluss durch Tool-Aufrufe oder Agentenausgaben. ([OWASP Cheat Sheet Series][7])

### Admin-Bewertung

| Zugriff      | Bewertung                                                  |
| ------------ | ---------------------------------------------------------- |
| Leserecht    | Meist kontrollierbar, wenn Datenklassifizierung passt      |
| Schreibrecht | Deutlich kritischer, da Daten verändert werden             |
| Löschrecht   | Sehr kritisch, nur mit Freigabe oder Papierkorbmechanismus |
| Adminrecht   | Für Agenten grundsätzlich zu vermeiden                     |
| Domänenadmin | Für Agenten praktisch nie angemessen                       |

---

## 4.4 Schreibrechte sind gefährlicher als Leserechte

Leserechte können Datenabfluss verursachen. Schreibrechte können zusätzlich Daten verändern, Prozesse auslösen oder Systeme beschädigen.

Beispiele:

| Recht               | Möglicher Schaden                                     |
| ------------------- | ----------------------------------------------------- |
| Ticket lesen        | Vertrauliche Informationen können offengelegt werden. |
| Ticket kommentieren | Falsche Informationen können dokumentiert werden.     |
| Ticket schließen    | Bearbeitung kann fälschlich beendet werden.           |
| Benutzer anlegen    | Unberechtigte Konten können entstehen.                |
| Gruppen ändern      | Rechteausweitung möglich.                             |
| Dateien löschen     | Datenverlust möglich.                                 |
| E-Mails versenden   | Reputations- und Datenschutzrisiko.                   |

---

## Kapitelzusammenfassung

Berechtigungen entscheiden, ob Automatisierung sicher ist. Die beste technische Plattform hilft wenig, wenn Identitäten, Rechte, Secrets und Verantwortlichkeiten unsauber geregelt sind.

---

# 5. Wenn bestimmte Dinge gesperrt sind: Was geht dann nicht?

## 5.1 Netzwerk und Internet

| Gesperrte oder fehlende Funktion             | Direkte Auswirkung                     | Was funktioniert dadurch nicht?        | Sicherheitsgrund für die Sperre            | Mögliche Alternative                        | Bewertung aus Admin-Sicht          |
| -------------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------------ | ------------------------------------------- | ---------------------------------- |
| Kein Internetzugriff                         | Externe Dienste sind nicht erreichbar. | Cloud-LLMs, Make, Zapier, externe APIs | Schutz vor Datenabfluss und Malware        | On-Prem n8n, lokales LLM, Offline-Import    | Sicher, aber integrationsarm       |
| Kein ausgehender HTTPS-Zugriff               | APIs über 443 nicht erreichbar         | SaaS-Integrationen, Cloud-KI           | Kontrolle über externe Kommunikation       | Egress Proxy mit Whitelist                  | Sinnvoll, wenn sauber dokumentiert |
| Kein DNS                                     | Namen können nicht aufgelöst werden    | API-Aufrufe per Hostname               | Verhindert unkontrollierte Namensauflösung | Interner DNS, statische Einträge            | Betrieblich oft problematisch      |
| Nur Proxy-Zugriff                            | Direkter Internetverkehr blockiert     | Tools ohne Proxy-Support               | Zentrale Kontrolle und Logging             | Plattform proxyfähig konfigurieren          | Gute Standardmaßnahme              |
| Keine Webhooks von außen erreichbar          | Externe Systeme können nichts anstoßen | Make/Zapier zu internem n8n            | Schutz interner Systeme                    | Polling, API-Gateway, Message Queue         | Meist sinnvoll                     |
| Keine eingehenden Verbindungen erlaubt       | Interne Dienste bleiben abgeschottet   | Externe Trigger, Callback-URLs         | Reduzierung Angriffsfläche                 | Outbound Polling                            | Sicherer Standard                  |
| Keine Verbindung zu Cloud-KI-Diensten        | Externe Modelle nicht nutzbar          | ChatGPT API, Claude API, Gemini API    | Datenschutz, Compliance, Geheimnisschutz   | Lokale LLMs, freigegebene KI-Gateways       | In regulierten Umgebungen typisch  |
| Keine Verbindung zu Make/Zapier              | SaaS-Automatisierung eingeschränkt     | Cloud-Workflows mit internen Systemen  | Datenabfluss- und Zugriffskontrolle        | n8n self-hosted, Power Automate mit Gateway | Für interne Prozesse oft besser    |
| Keine Verbindung zu GitHub oder Paketquellen | Updates und Abhängigkeiten fehlen      | Container Pulls, npm, pip              | Supply-Chain-Schutz                        | Interner Paketmirror, geprüfte Images       | Sicher, aber wartungsintensiv      |

---

## 5.2 Zertifikate und Verschlüsselung

| Gesperrte oder fehlende Funktion                | Direkte Auswirkung                        | Was funktioniert dadurch nicht?            | Sicherheitsgrund                   | Mögliche Alternative               | Admin-Bewertung            |
| ----------------------------------------------- | ----------------------------------------- | ------------------------------------------ | ---------------------------------- | ---------------------------------- | -------------------------- |
| Interne TLS-Zertifikate fehlen                  | Verbindungen sind unsicher oder scheitern | Interne APIs über HTTPS                    | Verhindert unsichere Kommunikation | Interne CA einführen               | Grundvoraussetzung         |
| Zertifikatskette wird nicht vertraut            | TLS-Fehler                                | Container ruft interne API nicht auf       | Schutz vor Man-in-the-Middle       | CA in Trust Store importieren      | Sauber lösbar              |
| Self-signed Zertifikate werden nicht akzeptiert | Verbindungsabbruch                        | Agent erreicht interne Weboberfläche nicht | Verhindert unsichere Ausnahmen     | CA-signiertes Zertifikat           | Richtig so                 |
| Zertifikate sind abgelaufen                     | Dienste werden blockiert                  | API, Webhook, Login                        | Integrität der Verbindung          | Monitoring und Rotation            | Klassischer Betriebsfehler |
| Kein Zugriff auf interne CA                     | Neue Dienste erhalten keine Zertifikate   | Neue Automatisierungsplattform             | Schutz der CA                      | Zertifikatsantragsprozess          | Organisatorisch lösen      |
| Kein mTLS möglich                               | Gegenseitige Authentifizierung fehlt      | Hochsichere Service-Kommunikation          | mTLS nicht überall nötig           | OAuth, API-Gateway, IP-Restriktion | Kontextabhängig            |

---

## 5.3 Identität und Berechtigungen

| Gesperrte oder fehlende Funktion        | Direkte Auswirkung                      | Was funktioniert dadurch nicht?         | Sicherheitsgrund                   | Mögliche Alternative                   | Admin-Bewertung                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ---------------------------------- | -------------------------------------- | ------------------------------- |
| Kein Servicekonto verfügbar             | Kein sauberer technischer Akteur        | Produktivworkflow                       | Vermeidung unkontrollierter Konten | Antrag mit Zweck und Owner             | Servicekonto ist Standardbedarf |
| Keine API-Keys erlaubt                  | Key-basierte Integration nicht möglich  | Viele SaaS-APIs                         | Schutz vor Key-Leaks               | OAuth, Zertifikate, Managed Identity   | Oft sinnvoll                    |
| OAuth nicht freigegeben                 | Delegierte API-Zugriffe blockiert       | Microsoft Graph, Google APIs            | Schutz vor zu breiten Scopes       | Admin Consent mit Review               | Freigabeprozess nötig           |
| Keine Schreibrechte                     | Agent kann nicht ändern                 | CRM-Update, Ticketabschluss             | Schutz vor Fehländerungen          | Vorschlagsmodus, Genehmigung           | Sehr guter Startpunkt           |
| Nur Leserechte vorhanden                | Analyse möglich, Aktion nicht           | Auto-Korrektur, Auto-Versand            | Begrenzung des Schadens            | Human-in-the-loop                      | Für Einstieg ideal              |
| Keine Adminrechte                       | Systemänderungen nicht möglich          | Benutzerverwaltung, Serveraktionen      | Schutz kritischer Systeme          | Delegierte Rechte, JEA                 | Richtig und erwünscht           |
| Kein Zugriff auf Abteilungsdaten        | Datenraum bleibt getrennt               | HR-, Finanz-, Rechtsdatenanalyse        | Datenschutz und Need-to-know       | Bereichsspezifische Freigabe           | Notwendig                       |
| Keine Benutzerimitation oder Delegation | Aktionen im Namen anderer nicht möglich | Persönliche Kalender- oder Mailaktionen | Schutz vor Identitätsmissbrauch    | Shared Mailbox, Servicekonto, Freigabe | Meist sinnvoll                  |

---

## 5.4 Skripting und Automatisierung

| Gesperrte oder fehlende Funktion   | Direkte Auswirkung                     | Was funktioniert dadurch nicht? | Sicherheitsgrund                         | Mögliche Alternative                      | Admin-Bewertung                   |
| ---------------------------------- | -------------------------------------- | ------------------------------- | ---------------------------------------- | ----------------------------------------- | --------------------------------- |
| PowerShell deaktiviert             | Windows-Automatisierung stark begrenzt | AD, Exchange, Serververwaltung  | Schutz vor Missbrauch                    | Graph API, signierte Runbooks             | Verständlich, aber einschränkend  |
| Execution Policy blockiert Skripte | Unsigned Scripts laufen nicht          | Lokale Automatisierung          | Schutz vor ungeprüften Skripten          | Signierte Skripte                         | Gute Kontrollmaßnahme             |
| Remote PowerShell deaktiviert      | Keine Fernadministration               | Serveraktionen aus Workflow     | Reduktion lateraler Bewegung             | JEA, Management-Server                    | Sicherer Standard                 |
| WinRM gesperrt                     | PowerShell Remoting blockiert          | Remote-Kommandos                | Angriffsflächenreduktion                 | Endpoint Management, API                  | Oft sinnvoll                      |
| SSH gesperrt                       | Linux-Remotezugriff nicht möglich      | Serverstatus, Deployments       | Schutz vor Fernzugriff                   | Agent-basierte Tools, Ansible Tower       | Kontextabhängig                   |
| Linux-Shell nicht erlaubt          | Keine direkten Systembefehle           | Logs auslesen, Dienste prüfen   | Schutz produktiver Systeme               | Monitoring-API                            | Für Fachbereich richtig           |
| Keine lokalen Skripte erlaubt      | Keine individuelle Logik               | Spezialprozesse                 | Change- und Malware-Schutz               | Freigegebene Skriptbibliothek             | Gut, wenn Alternativen existieren |
| Keine Container erlaubt            | Moderne Plattformen schwer betreibbar  | n8n, RAGFlow, OpenWebUI         | Betriebsstandard oder Sicherheitsvorgabe | VM-Betrieb, Managed Service               | Erhöht Aufwand                    |
| Keine geplanten Tasks erlaubt      | Keine lokalen Zeitpläne                | Batch-Verarbeitung              | Schatten-IT vermeiden                    | Zentrale Orchestrierung                   | Sinnvoll                          |
| Keine Cronjobs erlaubt             | Linux-Zeitsteuerung blockiert          | periodische Importe             | Kontrolle über Jobs                      | n8n-Scheduler, systemd Timer mit Freigabe | Organisatorisch lösen             |

---

## 5.5 Datenzugriff

| Gesperrte oder fehlende Funktion   | Direkte Auswirkung                | Was funktioniert dadurch nicht? | Sicherheitsgrund                   | Mögliche Alternative                      | Admin-Bewertung                   |
| ---------------------------------- | --------------------------------- | ------------------------------- | ---------------------------------- | ----------------------------------------- | --------------------------------- |
| Kein Datenbankzugriff              | Keine direkte Datenanalyse        | SQL-Berichte, RAG-Import        | Schutz produktiver Datenbanken     | Read Replica, API, Export                 | Sehr sinnvoll                     |
| Keine direkte SQL-Verbindung       | Tabellen nicht direkt nutzbar     | CRM/ERP-Auswertung              | Vermeidung fehlerhafter Queries    | Reporting-API                             | Besser als Direktzugriff          |
| Kein Zugriff auf Dateifreigaben    | Dokumente unsichtbar              | Dokumentenanalyse               | Schutz interner Ablagen            | DMS-Export, dedizierter Ordner            | Saubere Datenräume nötig          |
| Kein Zugriff auf SharePoint        | M365-Dokumente nicht erreichbar   | Wissenssuche, Zusammenfassung   | Schutz von Berechtigungen          | Graph API mit Scopes                      | Kontrolliert möglich              |
| Kein Zugriff auf E-Mail-Postfächer | Mails nicht auswertbar            | Rechnungseingang, Support       | Datenschutz und Vertraulichkeit    | Shared Mailbox, definierte Ordner         | Besser als persönliche Postfächer |
| Kein Zugriff auf Ticketsystem      | Keine Ticketautomatisierung       | Klassifizierung, Eskalation     | Schutz von Kundendaten             | E-Mail-Schnittstelle, API mit Leserechten | Integration prüfen                |
| Kein Zugriff auf ERP oder CRM      | Keine Geschäftsprozessintegration | Stammdaten, Angebote            | Schutz kritischer Geschäftsdaten   | Middleware, API-Gateway                   | Direkter Zugriff kritisch         |
| Keine Exportfunktion               | Daten bleiben im System           | Analyse, Migration              | Hersteller- oder Sicherheitsgründe | Datenbank-Read-Only, API-Anfrage          | Kann Projekt blockieren           |
| Keine API verfügbar                | Keine saubere Integration         | Echtzeit-Automation             | Legacy-System                      | RPA, Dateiimport, manuelle Schnittstelle  | Wartungsintensiv                  |
| Nur manuelle Exporte möglich       | Kein Echtzeitprozess              | Live-Automation                 | Kontrolle über Datenabgabe         | Geplanter Import mit Freigabe             | Für Einstieg möglich              |

---

## 5.6 KI-spezifische Einschränkungen

| Gesperrte oder fehlende Funktion      | Direkte Auswirkung                  | Was funktioniert dadurch nicht?      | Sicherheitsgrund                             | Mögliche Alternative                          | Admin-Bewertung                  |
| ------------------------------------- | ----------------------------------- | ------------------------------------ | -------------------------------------------- | --------------------------------------------- | -------------------------------- |
| Keine Cloud-LLMs erlaubt              | Externe KI-APIs nicht nutzbar       | SaaS-Agenten, Cloud-Chatbots         | Datenschutz, Geheimnisschutz                 | Lokale LLMs                                   | In regulierten Bereichen häufig  |
| Keine lokalen GPUs vorhanden          | Lokale Modelle langsam              | Große Modelle on-prem                | Kosten, Energie, Hardware                    | Kleine Modelle, CPU, Hybrid                   | Technische Leistungsgrenze       |
| Keine lokalen Modelle freigegeben     | Kein lokaler KI-Betrieb             | Offline-Agent                        | Lizenz- und Sicherheitsprüfung fehlt         | Modellfreigabeprozess                         | Governance nötig                 |
| Keine Vektordatenbank erlaubt         | RAG erschwert                       | Semantische Suche                    | Datenhaltung unklar                          | Volltextsuche, DB mit pgvector                | Kontextabhängig                  |
| Keine Embeddings erlaubt              | Semantische Indizes fehlen          | RAG, Ähnlichkeitssuche               | Schutz abgeleiteter Daten                    | Lokale Embeddings, Hashing nicht gleichwertig | Muss bewertet werden             |
| Keine Speicherung von Prompts erlaubt | Verlauf und Audit begrenzt          | Qualitätsprüfung, Debugging          | Datenschutz                                  | Redaction, kurze Aufbewahrung                 | Abwägung nötig                   |
| Keine personenbezogenen Daten erlaubt | Viele HR/CRM-Fälle entfallen        | Bewerber-, Kunden-, Mitarbeiterdaten | DSGVO-Risiko                                 | Anonymisierung, Pseudonymisierung, Freigabe   | Richtig vor Produktivstart       |
| Keine RAG-Architektur erlaubt         | Kein dokumentenbasierter KI-Kontext | Wissenschatbot                       | Datenabfluss oder Rechteproblem              | Manuelle Dokumentenauswahl                    | Stark einschränkend              |
| Kein Webzugriff für Agenten           | Keine Live-Recherche                | Marktanalyse, externe Prüfung        | Schutz vor Prompt Injection und Datenabfluss | Kuratierte Quellen, Proxy                     | Sehr oft sinnvoll                |
| Keine Tool-Nutzung durch Agenten      | Agent kann nur Text erzeugen        | Keine Aktionen                       | Schutz vor Fehlaktionen                      | Vorschlagsmodus                               | Sicherer Einstieg                |
| Kein autonomes Ausführen              | Keine End-to-End-Automation         | Auto-Löschen, Auto-Buchen            | Schutz vor Fehlentscheidungen                | Human-in-the-loop                             | Für kritische Prozesse empfohlen |

---

# 6. Beispiele für sichere Alternativen

## 6.1 Fall 1: Kein direkter Internetzugriff

### Ausgangslage

Ein Unternehmen erlaubt Servern und internen Anwendungen keinen direkten Internetzugriff.

### Auswirkung

* Cloud-Agenten funktionieren nur eingeschränkt oder gar nicht.
* Make und Zapier können interne Systeme nicht direkt erreichen.
* Webhooks von außen sind problematisch.
* Externe KI-APIs sind nicht nutzbar.
* Paketinstallationen aus GitHub, Docker Hub, npm oder PyPI sind nicht direkt möglich.

### Sichere Alternativen

| Alternative                  | Beschreibung                                 | Bewertung                              |
| ---------------------------- | -------------------------------------------- | -------------------------------------- |
| On-Prem n8n                  | Workflow-Plattform im internen Netz          | Sehr geeignet für interne Prozesse     |
| Lokales LLM                  | Modelle laufen intern                        | Gut für Datenschutz, benötigt Hardware |
| Interner Reverse Proxy       | Kontrollierter Zugriff auf interne Dienste   | Nur mit Authentifizierung und Logging  |
| Dedizierter Egress Proxy     | Ausgehender Zugriff über Whitelist           | Gute Standardlösung                    |
| Whitelisting einzelner Ziele | Nur definierte Domains und APIs              | Sicherer als freier Internetzugriff    |
| Offline-Importe              | Daten werden manuell oder geplant importiert | Einfach, aber nicht echtzeitfähig      |
| Manuelle Freigabeschritte    | Mensch prüft vor externer Übermittlung       | Gut bei sensiblen Daten                |
| DMZ-Architektur              | Zwischenzone für externe Kommunikation       | Geeignet für größere Organisationen    |
| API-Gateway                  | Zentral kontrollierte Schnittstellen         | Sehr empfehlenswert                    |

### Empfehlung

* **Minimalvariante:** Kein direkter Zugriff, manuelle Exporte.
* **Sichere Standardvariante:** On-Prem n8n plus Proxy-Whitelist.
* **Erweiterte Variante:** DMZ, API-Gateway, SIEM-Anbindung, Secret Vault.
* **Nicht empfehlenswert:** Firewall pauschal öffnen, damit ein Workflow funktioniert.

---

## 6.2 Fall 2: PowerShell gesperrt

### Ausgangslage

PowerShell oder Remote PowerShell ist deaktiviert.

### Auswirkung

* Windows-Automatisierungen sind eingeschränkt.
* AD-Abfragen, Exchange-Verwaltung oder Serveraktionen können nicht direkt automatisiert werden.
* Agenten können keine lokalen Systemänderungen ausführen.

### Alternativen

| Alternative               | Beschreibung                                      |
| ------------------------- | ------------------------------------------------- |
| Microsoft Graph API       | Für M365- und Entra-ID-Aktionen                   |
| REST-APIs                 | Wenn Zielsysteme APIs anbieten                    |
| Administrative Middleware | Kontrollierter Dienst führt geprüfte Aktionen aus |
| Signierte Skripte         | Nur geprüfte Skripte werden ausgeführt            |
| Runbooks                  | Skripte laufen in kontrollierter Umgebung         |
| Endpoint Management       | Intune, SCCM oder RMM-Systeme                     |
| Manuelle Freigabeprozesse | Agent erstellt Vorschlag oder Ticket              |

### Admin-Bewertung

PowerShell pauschal freizugeben ist selten sinnvoll. Besser sind signierte Skripte, JEA, Logging und klar definierte Ausführungsumgebungen.

---

## 6.3 Fall 3: Keine Schreibrechte

### Ausgangslage

Ein Agent darf Daten lesen, aber keine Änderungen durchführen.

### Auswirkung

* Der Agent kann analysieren.
* Der Agent kann Vorschläge erstellen.
* Der Agent kann keine Systeme verändern.
* Workflows enden bei Entwürfen, Tickets oder Handlungsempfehlungen.

### Alternativen

| Alternative                      | Beschreibung                                        |
| -------------------------------- | --------------------------------------------------- |
| Human-in-the-loop                | Mensch genehmigt Aktion                             |
| Ticket-Erstellung                | Agent erstellt Ticket statt Änderung                |
| Genehmigungsworkflow             | Freigabe vor Ausführung                             |
| Vorschlagsmodus                  | Agent erstellt konkrete Empfehlung                  |
| Nur-Lese-Dashboard               | Ergebnisse sichtbar, aber nicht automatisch wirksam |
| Export von Handlungsempfehlungen | Fachbereich oder IT setzt um                        |

### Admin-Bewertung

Nur-Lese- und Vorschlagsmodi sind für Pilotprojekte oft der beste Einstieg.

---

## 6.4 Fall 4: Keine Cloud-KI erlaubt

### Ausgangslage

Externe KI-Dienste sind untersagt.

### Auswirkung

* ChatGPT API, Claude API, Gemini API oder andere externe Modelle sind nicht nutzbar.
* SaaS-Agenten sind stark eingeschränkt.
* Make oder Zapier können keine Cloud-KI für interne Daten verwenden.

### Alternativen

| Alternative                | Beschreibung                        |
| -------------------------- | ----------------------------------- |
| Lokale LLMs                | Modelle laufen im eigenen Netz      |
| Ollama                     | Einfacher lokaler Modellbetrieb     |
| vLLM                       | Performante Modellbereitstellung    |
| OpenWebUI                  | Lokale Chat-Oberfläche              |
| RAGFlow                    | Dokumentenbasierte RAG-Plattform    |
| Lokale Embedding-Modelle   | Keine externen Embedding-APIs       |
| Lokale Vektordatenbank     | Qdrant, PostgreSQL/pgvector, Milvus |
| Isolierte KI-Infrastruktur | Separates Netzsegment               |
| Offline-Betrieb            | Keine externe Kommunikation         |

### Admin-Bewertung

Lokale KI reduziert Datenabflussrisiken, löst aber nicht automatisch Berechtigungs-, Logging-, Backup- und Governance-Fragen.

---

## 6.5 Fall 5: Keine Webhooks von außen

### Ausgangslage

Interne Systeme dürfen von außen nicht direkt erreicht werden.

### Auswirkung

* Externe Systeme können interne Workflows nicht direkt anstoßen.
* Make/Zapier können keinen internen n8n-Webhook aufrufen.
* Callback-Mechanismen funktionieren nicht.

### Alternativen

| Alternative                         | Beschreibung                                        |
| ----------------------------------- | --------------------------------------------------- |
| Polling                             | Internes System fragt regelmäßig externen Status ab |
| Message Queue                       | Entkoppelte Nachrichtenverarbeitung                 |
| API-Gateway                         | Kontrollierter Eingangspunkt                        |
| Reverse Proxy mit Authentifizierung | Nur definierte Endpunkte erreichbar                 |
| VPN                                 | Geschützter Verbindungskanal                        |
| Dedizierter Integration Server      | Vermittler in DMZ                                   |
| Periodischer Import                 | Zeitgesteuerte Datenübernahme                       |

### Admin-Bewertung

Keine eingehenden Verbindungen zu internen Workflows zuzulassen ist sicherheitstechnisch nachvollziehbar. Für Integration sind kontrollierte Zwischeninstanzen besser als direkte Freigaben.

---

# 7. Vergleich: n8n, Make, Zapier, Power Automate und eigene Agenten

| Plattform                                 | Typische Betriebsform           | Stärken                                                 | Grenzen                                            | Sicherheitsaspekte                             | Geeignet für                                | Weniger geeignet für                       |
| ----------------------------------------- | ------------------------------- | ------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| n8n self-hosted                           | On-Prem, Cloud-VM, Container    | Hohe Kontrolle, interne Systeme erreichbar, flexibel    | Betrieb, Updates, Backup selbst verantworten       | Secrets, RBAC, Netzwerksegmentierung, Logging  | Interne Workflows, KMU, technische Teams    | Unternehmen ohne Betriebsverantwortung     |
| n8n cloud                                 | SaaS                            | Kein eigener Betrieb, schnelle Einrichtung              | Interne Systeme nur über sichere Anbindung         | Datenabfluss, Webhooks, API-Keys               | SaaS-nahe Prozesse                          | Streng isolierte Netze                     |
| Make                                      | SaaS                            | Viele Konnektoren, schnelle Prozessautomatisierung      | Interne Systeme schwer erreichbar                  | Externe Datenverarbeitung, Token-Schutz        | Marketing, Vertrieb, einfache SaaS-Prozesse | Hochsensible interne Prozesse              |
| Zapier                                    | SaaS                            | Sehr einfache Bedienung, viele Apps                     | Begrenzte komplexe Logik, Cloud-Fokus              | Datenschutz, App-Berechtigungen                | Kleine Automatisierungen                    | Kritische Kernprozesse                     |
| Power Automate                            | Microsoft Cloud, teils Gateway  | Gute M365-Integration, Governance in Microsoft-Umgebung | Abhängigkeit von Lizenzen und Tenant-Konfiguration | DLP Policies, Connector-Kontrolle, Entra ID    | M365-Unternehmen                            | Nicht-Microsoft-lastige On-Prem-Umgebungen |
| Eigene Python-/PowerShell-Automatisierung | On-Prem, Server, Task, Pipeline | Maximale Kontrolle, sehr flexibel                       | Wartbarkeit, Know-how, Fehlerhandling              | Code Review, Signierung, Secrets, Logging      | Admin-nahe Aufgaben                         | Fachbereich ohne technische Betreuung      |
| KI-Agenten mit Tool-Zugriff               | Cloud oder On-Prem              | Dynamische Aufgaben, Sprache, Tool-Nutzung              | Schwerer vorhersagbar als feste Workflows          | Prompt Injection, Tool Abuse, Rechtebegrenzung | Vorschläge, Analysen, Assistenz             | Autonome kritische Aktionen                |
| Lokale KI-Agenten im Unternehmensnetz     | On-Prem, isoliert               | Datenschutzfreundlicher, interne Daten nutzbar          | Hardware, Modellqualität, Betrieb                  | Datenräume, RAG-Rechte, Logging                | Regulierte oder sensible Umgebungen         | Kleine Firmen ohne Betriebsressourcen      |

## Bewertung

| Kriterium                   | Cloud-Plattformen | On-Prem-Plattformen  | Hybrid                     |
| --------------------------- | ----------------- | -------------------- | -------------------------- |
| Schneller Start             | Hoch              | Mittel               | Mittel                     |
| Kontrolle über Daten        | Niedriger         | Hoch                 | Mittel bis hoch            |
| Zugriff auf interne Systeme | Eingeschränkt     | Hoch                 | Hoch mit Gateway           |
| Betriebsaufwand             | Niedrig           | Hoch                 | Mittel                     |
| Datenschutzprüfung          | Wichtig           | Ebenfalls wichtig    | Besonders wichtig          |
| Anbieterabhängigkeit        | Höher             | Niedriger            | Mittel                     |
| Skalierbarkeit              | Hoch              | Abhängig von Betrieb | Hoch bei guter Architektur |

---

# 8. Webzugriff von Agenten

Webzugriff bedeutet nicht nur, dass ein Agent „ins Internet darf“. Es gibt verschiedene Stufen.

| Stufe                         | Beschreibung                         | Beispiel                 | Bewertung                              |
| ----------------------------- | ------------------------------------ | ------------------------ | -------------------------------------- |
| Kein Webzugriff               | Agent nutzt nur lokale Daten         | Interne Wissensdatenbank | Sehr kontrollierbar                    |
| Nur interne Webseiten         | Agent darf Intranet lesen            | Wiki, DMS, Ticketsystem  | Gut, wenn Rechte beachtet werden       |
| Definierte externe Domains    | Nur Whitelist                        | Herstellerdokumentation  | Sinnvoll für Recherche                 |
| Zugriff über Proxy            | Zentral kontrolliert                 | HTTP(S)-Proxy mit Logs   | Standard in Unternehmen                |
| Freier Internetzugriff        | Agent kann beliebige Seiten aufrufen | Web-Agent                | Hohes Risiko                           |
| Zugriff mit Benutzeranmeldung | Agent nutzt Benutzerkontext          | Intranet oder SaaS       | Kritisch, wenn nicht begrenzt          |
| Zugriff mit Servicekonto      | Technischer Zugriff                  | API oder Portal          | Besser kontrollierbar                  |
| API statt Webseite            | Strukturierter Zugriff               | REST API                 | Bevorzugt gegenüber Browser-Automation |

## Risiken

| Risiko                                 | Erklärung                                                                                                                                                                                                                                                                    |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Datenabfluss                           | Agent kann interne Inhalte an externe Seiten oder APIs senden.                                                                                                                                                                                                               |
| Prompt Injection durch Webseiten       | Eine Webseite kann versteckte Anweisungen enthalten, die Agentenverhalten beeinflussen. OWASP beschreibt Prompt Injection als Manipulation von Modellantworten durch Eingaben, einschließlich indirekter Angriffe über externe Inhalte. ([OWASP Gen AI Security Project][8]) |
| Falsche Informationen                  | Webseiten können veraltet, manipuliert oder unvollständig sein.                                                                                                                                                                                                              |
| Unkontrolliertes Crawling              | Agent ruft mehr Inhalte ab als vorgesehen.                                                                                                                                                                                                                                   |
| Zugriff auf nicht freigegebene Inhalte | Agent nutzt Berechtigungen breiter als fachlich nötig.                                                                                                                                                                                                                       |
| Rechtliche Risiken                     | Urheberrecht, Datenschutz und Nutzungsbedingungen können relevant sein.                                                                                                                                                                                                      |
| Authentifizierungsrisiken              | Cookies, Tokens oder Sessions können missbraucht werden.                                                                                                                                                                                                                     |
| Umgehung von Sicherheitskontrollen     | Browser-Agenten können technische Grenzen verwischen.                                                                                                                                                                                                                        |

## Empfehlungen

| Empfehlung                                      | Begründung                                                          |
| ----------------------------------------------- | ------------------------------------------------------------------- |
| Whitelisting                                    | Agent darf nur definierte Ziele aufrufen.                           |
| Proxy mit Logging                               | Zugriffe sind nachvollziehbar.                                      |
| API-first statt Browser-Automation              | APIs sind stabiler, kontrollierbarer und auditierbarer.             |
| Keine freien Browser-Agenten auf Produktivdaten | Risiko durch Prompt Injection und Datenabfluss zu hoch.             |
| Trennung zwischen Recherche und Aktion          | Webinformationen dürfen nicht ungeprüft Produktivaktionen auslösen. |
| Human-in-the-loop                               | Kritische Entscheidungen benötigen menschliche Freigabe.            |
| Protokollierung aller Abfragen                  | Notwendig für Fehleranalyse und Audit.                              |

---

# 9. PowerShell, Skripte und Systemzugriffe

PowerShell ist in Windows-Umgebungen eines der mächtigsten Administrationswerkzeuge. Genau deshalb ist sie sicherheitskritisch.

PowerShell kann:

* Benutzer anlegen
* Gruppenmitgliedschaften ändern
* Exchange und Microsoft 365 verwalten
* Dienste starten oder stoppen
* Dateien verschieben oder löschen
* Registry ändern
* Server remote verwalten
* Sicherheitskonfigurationen beeinflussen

Microsoft Security Baselines sind empfohlene Konfigurationseinstellungen, die Sicherheitsauswirkungen erklären und auf Erfahrungen von Microsoft-Sicherheitsteams, Produktgruppen, Partnern und Kunden beruhen. ([Microsoft Learn][9]) Solche Baselines sind ein sinnvoller Bezugspunkt, wenn Unternehmen PowerShell, Windows Server, Clients und administrative Funktionen härten.

---

## 9.1 Wichtige Begriffe

| Begriff                    | Erklärung                                                    |
| -------------------------- | ------------------------------------------------------------ |
| Lokale PowerShell          | Ausführung auf demselben System                              |
| Remote PowerShell          | Ausführung auf entfernten Systemen                           |
| WinRM                      | Windows Remote Management, Grundlage für PowerShell Remoting |
| Signierte Skripte          | Skripte mit digitaler Signatur                               |
| Execution Policy           | Richtlinie, welche Skripte ausgeführt werden dürfen          |
| Constrained Language Mode  | Eingeschränkter PowerShell-Sprachmodus                       |
| Just Enough Administration | Benutzer dürfen nur definierte Admin-Aufgaben ausführen      |
| Script Block Logging       | Protokolliert ausgeführte PowerShell-Blöcke                  |
| Transcription              | Zeichnet PowerShell-Sitzungen auf                            |

---

## 9.2 Tabelle: Automatisierungswünsche

| Automatisierungswunsch         | Benötigte technische Fähigkeit | Risiko                            | Sichere Umsetzung                 | Alternative bei Sperre      |
| ------------------------------ | ------------------------------ | --------------------------------- | --------------------------------- | --------------------------- |
| Benutzer anlegen               | AD/Graph-Schreibrecht          | Falsche oder unberechtigte Konten | Genehmigter Onboarding-Workflow   | Ticket an IT                |
| Gruppenmitgliedschaften prüfen | AD/Graph-Leserecht             | Offenlegung von Berechtigungen    | Read-only Servicekonto            | Export aus IAM              |
| Gruppenmitgliedschaft ändern   | AD/Graph-Schreibrecht          | Rechteausweitung                  | JIT, Vier-Augen-Prinzip           | Freigabe durch IAM-Team     |
| Dateien verschieben            | Fileserver-Rechte              | Datenverlust                      | Dedizierter Ordner, Logging       | Manuelle Prüfung            |
| Dienste neustarten             | Serverzugriff                  | Ausfall                           | Runbook mit Freigabe              | Monitoring löst Ticket aus  |
| Serverstatus prüfen            | Monitoring/API/SSH/WinRM       | Gering, wenn read-only            | Monitoring-Integration            | Agent liest Monitoringdaten |
| Updates auslösen               | Endpoint Management            | Betriebsunterbrechung             | Wartungsfenster, Freigabe         | Patchmanagement-System      |
| Tickets erstellen              | Ticketsystem-API               | Ticketflut                        | Rate Limits, Pflichtfelder        | E-Mail an Service Desk      |
| E-Mails auswerten              | Mailbox-Zugriff                | Datenschutz                       | Shared Mailbox, definierte Ordner | Manuelle Weiterleitung      |
| Logdateien analysieren         | Zugriff auf Logs               | Sensible Inhalte in Logs          | SIEM, Rollen, Redaction           | Export mit Maskierung       |

## Empfehlung

| Variante                 | Beschreibung                                                 |
| ------------------------ | ------------------------------------------------------------ |
| Minimalvariante          | Agent erstellt PowerShell-Vorschläge, Mensch führt aus.      |
| Sichere Standardvariante | Signierte Skripte, Runbook, Logging, Servicekonto, Freigabe. |
| Erweiterte Variante      | JEA, PIM, SIEM, Code Review, getrennte Admin-Workstations.   |
| Nicht empfehlenswert     | Agent führt beliebige PowerShell mit Adminrechten aus.       |

---

# 10. Zertifikate, TLS und interne Systeme

Zertifikate sind für Automatisierung zentral, weil moderne Systeme meist über HTTPS oder mTLS kommunizieren.

## 10.1 Warum Zertifikate wichtig sind

| Thema                   | Bedeutung                                           |
| ----------------------- | --------------------------------------------------- |
| HTTPS                   | Verschlüsselte und authentisierte Verbindung        |
| Interne CA              | Vertrauensanker für interne Systeme                 |
| Zertifikatskette        | Muss vollständig und vertrauenswürdig sein          |
| Trust Store             | System oder Container muss CA kennen                |
| Self-signed Zertifikate | Häufig problematisch, weil nicht vertrauenswürdig   |
| mTLS                    | Client und Server authentifizieren sich gegenseitig |
| Ablaufdatum             | Abgelaufene Zertifikate blockieren Verbindungen     |
| Container               | Haben eigene Trust Stores                           |
| Interne APIs            | Brauchen passende Zertifikate für Hostnamen         |

---

## 10.2 Typische Probleme

| Problem                              | Ursache                             | Auswirkung                          | Sichere Lösung                      |
| ------------------------------------ | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| Agent vertraut internem System nicht | Interne CA fehlt im Trust Store     | API-Aufruf scheitert                | CA-Bundle verteilen                 |
| TLS-Fehler in n8n                    | Zertifikatskette unvollständig      | Workflow bricht ab                  | Vollständige Chain konfigurieren    |
| Container kennt interne CA nicht     | Container nutzt eigenen Trust Store | HTTPS zu internen APIs schlägt fehl | CA in Image oder Volume einbinden   |
| Zertifikat passt nicht zum Hostnamen | CN/SAN falsch                       | TLS-Validierung schlägt fehl        | Zertifikat korrekt ausstellen       |
| Proxy bricht TLS auf                 | TLS Inspection                      | Zertifikat wird vom Proxy ersetzt   | Proxy-CA vertrauenswürdig verteilen |
| Zertifikatsrotation vergessen        | Ablauf nicht überwacht              | Plötzlicher Ausfall                 | Monitoring und Kalenderwarnung      |
| Prüfung wird deaktiviert             | Schnelle Fehlersuche                | Man-in-the-Middle-Risiko            | Niemals dauerhaft deaktivieren      |

## Admin-Empfehlungen

* Interne CA sauber verteilen.
* Zertifikate dokumentieren.
* Ablaufdaten überwachen.
* Zertifikatsrotation testen.
* Keine pauschale Deaktivierung der Zertifikatsprüfung.
* Eigene Trust Stores für Container pflegen.
* Test- und Produktionszertifikate trennen.

---

# 11. Datenklassifizierung und Datenschutz

Datenklassifizierung ist vor KI- und Automatisierungsprojekten notwendig, weil nicht alle Daten gleich behandelt werden dürfen.

Die DSGVO nennt unter anderem Grundsätze wie Rechtmäßigkeit, Transparenz, Zweckbindung, Datenminimierung, Richtigkeit, Speicherbegrenzung, Integrität und Vertraulichkeit für personenbezogene Daten. ([DSGVO][10]) Der EU AI Act verfolgt einen risikobasierten Ansatz für KI-Systeme. ([Digitalstrategie Europa][11]) Daraus folgt praktisch: Ein KI-Manager sollte Datenart, Zweck, Zugriff, Speicherung und Risiko klären, bevor Agenten produktiv eingesetzt werden.

---

## 11.1 Datenarten

| Datenart                                     | Beispiel                   | Darf ein Agent darauf zugreifen? | Bedingungen                         | Empfehlung                      |
| -------------------------------------------- | -------------------------- | -------------------------------- | ----------------------------------- | ------------------------------- |
| Öffentliche Daten                            | Produktflyer               | Ja                               | Quelle prüfen                       | Unkritischer Einstieg           |
| Interne Daten                                | Prozessbeschreibung        | Ja, eingeschränkt                | Interner Zweck, Rollen              | Gut für Wissenssuche            |
| Vertrauliche Daten                           | Angebote, Kalkulationen    | Nur kontrolliert                 | Berechtigung, Logging               | Datenraum trennen               |
| Personenbezogene Daten                       | Kundenname, E-Mail         | Nur nach Prüfung                 | Rechtsgrundlage, Zweck, Minimierung | Datenschutz einbinden           |
| Besondere Kategorien personenbezogener Daten | Gesundheitsdaten           | Nur sehr streng                  | Spezielle Prüfung                   | Meist nicht für Pilot           |
| Geschäftsgeheimnisse                         | Strategie, Preise          | Nur streng begrenzt              | Need-to-know                        | Kein Cloud-Upload ohne Freigabe |
| Zugangsdaten                                 | Passwörter, Tokens         | Nein                             | Nur Secret Vault                    | Nie in Prompts                  |
| Kundendaten                                  | Verträge, Tickets          | Kontrolliert                     | Rollen, Zweck                       | Mandantentrennung               |
| Finanzdaten                                  | Rechnungen, Bankdaten      | Kontrolliert                     | Vier-Augen-Prinzip                  | Kein autonomes Buchen           |
| HR-Daten                                     | Bewerbungen, Personalakten | Sehr eingeschränkt               | Datenschutz, HR-Freigabe            | Höchste Vorsicht                |
| Technische Betriebsdaten                     | Logs, Metriken             | Ja, aber prüfen                  | Redaction, Rollen                   | Gut für Monitoring-Agenten      |
| Logs                                         | Fehler, IPs, Benutzernamen | Kontrolliert                     | Keine Secrets, Aufbewahrung         | SIEM-Regeln beachten            |

---

## 11.2 Wichtige Grundsätze

| Grundsatz                                         | Bedeutung für Agenten                                                  |
| ------------------------------------------------- | ---------------------------------------------------------------------- |
| Nicht jeder Agent darf auf alle Daten zugreifen   | Datenräume müssen getrennt bleiben.                                    |
| RAG muss Berechtigungen respektieren              | Ein Benutzer darf über RAG nicht mehr sehen als direkt im Quellsystem. |
| Embeddings können schützenswert sein              | Sie sind abgeleitete Repräsentationen vertraulicher Inhalte.           |
| Logs dürfen keine sensiblen Inhalte enthalten     | Prompts, Antworten und API-Fehler können Daten enthalten.              |
| Prompt- und Antwortspeicherung muss geregelt sein | Aufbewahrung, Zugriff und Löschung müssen definiert sein.              |

---

# 12. Betriebsmodelle

| Betriebsmodell                     | Vorteile                                 | Nachteile                                 | Sicherheitsniveau                    | Administrativer Aufwand | Geeignete Unternehmenstypen                      |
| ---------------------------------- | ---------------------------------------- | ----------------------------------------- | ------------------------------------ | ----------------------- | ------------------------------------------------ |
| Vollständig cloudbasiert           | Schnell, skalierbar, wenig Betrieb       | Datenabflussprüfung, Anbieterabhängigkeit | Mittel bis hoch bei guter Governance | Niedrig bis mittel      | Kleine Unternehmen, SaaS-lastige Organisationen  |
| Hybrid                             | Balance aus Kontrolle und Cloud-Leistung | Komplexe Schnittstellen                   | Hoch, wenn sauber geplant            | Mittel bis hoch         | Mittelstand, M365-Umgebungen                     |
| Vollständig On-Prem                | Hohe Datenkontrolle                      | Betrieb, Updates, Hardware                | Hoch bei guter Administration        | Hoch                    | Regulierte oder sensible Umgebungen              |
| Air-gapped                         | Maximale Abschottung                     | Kein Cloud-Zugriff, Updates schwierig     | Sehr hoch gegen externe Abflüsse     | Sehr hoch               | Kritische Infrastruktur, Forschung, Geheimschutz |
| Testumgebung                       | Sicheres Ausprobieren                    | Nicht produktiv                           | Hoch für Experimente                 | Mittel                  | Alle Unternehmen                                 |
| Produktivumgebung                  | Realer Nutzen                            | Höchstes Risiko                           | Abhängig von Kontrollen              | Hoch                    | Nach Freigabe                                    |
| Isolierte Automatisierungsumgebung | Begrenzter Schaden                       | Zusätzliche Infrastruktur                 | Hoch                                 | Mittel                  | Admin-nahe Workflows                             |
| DMZ-Modell                         | Kontrollierte externe Kommunikation      | Architekturaufwand                        | Hoch                                 | Hoch                    | Unternehmen mit externen Integrationen           |
| Jump-Host-Modell                   | Kontrollierter Admin-Zugriff             | Bedienaufwand                             | Hoch                                 | Mittel                  | Serveradministration                             |
| API-Gateway-Modell                 | Zentrale Kontrolle von APIs              | Initialer Aufwand                         | Hoch                                 | Mittel bis hoch         | Größere Organisationen                           |

---

# 13. Governance und Freigabeprozesse

Technische Sicherheit reicht nicht aus. Unternehmen benötigen klare Regeln.

## 13.1 Zu klärende Fragen

| Frage                                | Warum wichtig?                                |
| ------------------------------------ | --------------------------------------------- |
| Wer darf Workflows erstellen?        | Verhindert unkontrollierte Schatten-IT        |
| Wer darf Workflows produktiv setzen? | Produktivbetrieb benötigt Freigabe            |
| Wer verwaltet Secrets?               | API-Keys und Tokens sind kritisch             |
| Wer genehmigt neue API-Zugriffe?     | Schnittstellen öffnen Datenwege               |
| Wer prüft Datenschutz?               | Personenbezogene Daten müssen bewertet werden |
| Wer prüft Informationssicherheit?    | Risiken müssen dokumentiert werden            |
| Wer dokumentiert Änderungen?         | Nachvollziehbarkeit                           |
| Wer reagiert bei Fehlern?            | Betriebsverantwortung                         |
| Wer ist fachlicher Owner?            | Prozessverantwortung                          |
| Wer ist technischer Owner?           | Plattform- und Betriebsverantwortung          |
| Wer prüft Logs?                      | Missbrauch und Fehler erkennen                |
| Wer deaktiviert alte Workflows?      | Verhindert verwaiste Automatisierungen        |

---

## 13.2 Empfehlungen

| Bereich               | Empfehlung                                                                        |
| --------------------- | --------------------------------------------------------------------------------- |
| Rollenmodell          | Fachlicher Owner, technischer Owner, Datenschutz, Informationssicherheit, Betrieb |
| Freigabeprozess       | Test, Review, Datenschutzprüfung, technische Freigabe, Produktivsetzung           |
| Dokumentationspflicht | Zweck, Daten, Systeme, Rechte, Owner, Notfallkontakt                              |
| Change Management     | Änderungen versionieren und freigeben                                             |
| Notfallabschaltung    | Workflows müssen schnell deaktivierbar sein                                       |
| Auditierbarkeit       | Logs, Versionen und Freigaben aufbewahren                                         |
| Review-Zyklen         | Rechte und Workflows regelmäßig prüfen                                            |
| Schatten-IT           | Niedrigschwellige, aber kontrollierte Plattform anbieten                          |

NIS2 legt auf EU-Ebene einen Rahmen für Cybersicherheit in kritischen Sektoren fest. ([Digitalstrategie Europa][12]) ENISA stellt technische Umsetzungshinweise zu Cybersicherheits-Risikomanagementmaßnahmen bereit, inklusive praktischer Hinweise und Nachweisen. ([enisa.europa.eu][13]) Auch wenn nicht jedes Unternehmen direkt betroffen ist, sind diese Anforderungen als Orientierung für Governance, Risikomanagement, Lieferkettensicherheit, Incident Handling und Business Continuity relevant.

---

# 14. Typische Fehlannahmen von Fachbereichen

| Fehlannahme                                                                      | Korrektur aus Admin-Sicht                                                                                                                    |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. „Der Agent kann doch einfach auf alles zugreifen.“                            | Nur wenn Zugänge, Rechte, Schnittstellen und Freigaben vorhanden sind. Genau das sollte aus Sicherheitsgründen meistens nicht der Fall sein. |
| 2. „Wir geben dem Agenten einfach Adminrechte.“                                  | Das erhöht den möglichen Schaden massiv. Besser sind minimale Rechte und Freigabeschritte.                                                   |
| 3. „Wenn PowerShell gesperrt ist, kann der Agent trotzdem alles automatisieren.“ | Ohne Skriptzugriff oder alternative APIs sind viele Systemaktionen nicht möglich.                                                            |
| 4. „Wenn kein Internet erlaubt ist, nutzen wir einfach Make oder Zapier.“        | Cloudplattformen benötigen externe Verbindungen. Für interne Systeme braucht man On-Prem oder Gateways.                                      |
| 5. „Ein lokales LLM löst automatisch alle Datenschutzprobleme.“                  | Lokaler Betrieb reduziert Datenabfluss, ersetzt aber kein Rechte-, Logging- und Governance-Konzept.                                          |
| 6. „Leserechte sind unkritisch.“                                                 | Leserechte können vertrauliche Daten offenlegen.                                                                                             |
| 7. „Der Agent entscheidet schon richtig.“                                        | KI-Ausgaben können falsch, unvollständig oder manipuliert sein.                                                                              |
| 8. „Wir speichern API-Keys einfach im Workflow.“                                 | Secrets im Klartext sind ein erhebliches Risiko.                                                                                             |
| 9. „Ein Test mit echten Kundendaten ist schneller.“                              | Testdaten sollten anonymisiert oder synthetisch sein.                                                                                        |
| 10. „Wenn es technisch geht, ist es auch erlaubt.“                               | Technische Machbarkeit ersetzt keine organisatorische, rechtliche oder Sicherheitsfreigabe.                                                  |
| 11. „Webzugriff ist nur Recherche.“                                              | Webzugriff kann Prompt Injection, Datenabfluss und falsche Entscheidungen verursachen.                                                       |
| 12. „Ein Workflow braucht keine Dokumentation.“                                  | Ohne Dokumentation sind Betrieb, Audit und Fehlerbehebung unsicher.                                                                          |
| 13. „Einmal eingerichtet läuft das dauerhaft.“                                   | Tokens laufen ab, APIs ändern sich, Zertifikate verfallen, Rechte ändern sich.                                                               |
| 14. „Ein Agent kann direkt produktiv starten.“                                   | Produktivbetrieb benötigt Test, Freigabe, Monitoring und Notfallabschaltung.                                                                 |
| 15. „Cloud ist immer unsicher, On-Prem ist immer sicher.“                        | Beide Modelle haben Risiken. Entscheidend sind Architektur, Rechte, Betrieb und Kontrolle.                                                   |
| 16. „Wenn ein Tool beliebt ist, ist es automatisch sicher.“                      | Beliebtheit ersetzt keine Sicherheitsprüfung.                                                                                                |
| 17. „RAG zeigt nur erlaubte Dokumente.“                                          | Nur, wenn Berechtigungen technisch durchgesetzt werden.                                                                                      |
| 18. „Logs sind unproblematisch.“                                                 | Logs können personenbezogene Daten, Tokens oder vertrauliche Inhalte enthalten.                                                              |

---

# 15. Konkrete Beratungsempfehlungen für KI-Manager

## 15.1 Technische Fragen

* Welche Systeme sollen angebunden werden?
* Gibt es APIs?
* Gibt es Testsysteme?
* Gibt es Servicekonten?
* Gibt es Netzwerkfreigaben?
* Ist Internetzugriff erlaubt?
* Gibt es Proxy-Vorgaben?
* Gibt es Zertifikatsanforderungen?
* Sind Webhooks erlaubt?
* Sind Skripte erlaubt?
* Sind Container erlaubt?
* Gibt es Monitoring?
* Gibt es Backups?
* Gibt es eine Update-Strategie?
* Gibt es eine Rollback-Möglichkeit?

## 15.2 Sicherheitsfragen

* Welche Daten werden verarbeitet?
* Welche Berechtigungen werden benötigt?
* Sind Leserechte ausreichend?
* Sind Schreibrechte wirklich nötig?
* Gibt es Least-Privilege-Konzepte?
* Wie werden Secrets gespeichert?
* Wer darf Workflows ändern?
* Gibt es Logging?
* Gibt es Audit Trails?
* Gibt es Datenschutzfreigaben?
* Gibt es eine Notfallabschaltung?
* Gibt es eine Trennung zwischen Test und Produktion?

## 15.3 Organisatorische Fragen

* Wer ist fachlicher Owner?
* Wer ist technischer Owner?
* Wer wartet die Workflows?
* Wer reagiert bei Fehlern?
* Wer prüft Änderungen?
* Wie werden Workflows dokumentiert?
* Wie wird verhindert, dass Schatten-IT entsteht?
* Wie werden alte Workflows deaktiviert?
* Wie werden Berechtigungen regelmäßig geprüft?

---

# 16. Ampelmodell für Automatisierungen und Agenten

## 16.1 Grün: unkritisch oder gut kontrollierbar

| Beispiel                                | Empfehlung                         |
| --------------------------------------- | ---------------------------------- |
| Nur-Lese-Zugriffe                       | Geeignet für Pilot                 |
| Interne Wissenssuche                    | Mit Berechtigungskonzept           |
| Zusammenfassung freigegebener Dokumente | Keine sensiblen Daten ohne Prüfung |
| Ticketvorschläge                        | Mensch entscheidet                 |
| E-Mail-Entwürfe                         | Versand nur manuell                |
| Testumgebung                            | Sehr geeignet                      |
| Keine personenbezogenen Daten           | Niedrigeres Risiko                 |

## 16.2 Gelb: kontrolliert möglich, aber mit Prüfung

| Beispiel                               | Empfehlung                           |
| -------------------------------------- | ------------------------------------ |
| Verarbeitung interner Daten            | Datenklassifizierung durchführen     |
| API-Zugriffe mit Schreibrechten        | Freigabe und Logging                 |
| E-Mail-Automatisierung                 | Versandbegrenzung und Review         |
| Zugriff auf CRM                        | Rollen und Zweckbindung              |
| Zugriff auf SharePoint                 | Berechtigungen technisch durchsetzen |
| Webhooks                               | Authentifizierung und Rate Limits    |
| PowerShell mit eingeschränkten Rechten | Signierung, JEA, Logging             |
| RAG mit vertraulichen Dokumenten       | Datenräume und Zugriffskontrolle     |

## 16.3 Rot: nur mit strenger Kontrolle oder nicht empfehlenswert

| Beispiel                                  | Empfehlung                             |
| ----------------------------------------- | -------------------------------------- |
| Domänenadmin-Rechte                       | Für Agenten nicht verwenden            |
| Freier Internetzugriff mit Produktivdaten | Vermeiden                              |
| Autonomes Löschen von Daten               | Nur mit Freigabe oder gar nicht        |
| Autonome Benutzerverwaltung               | Nur mit Genehmigungsworkflow           |
| Beliebige Skriptausführung                | Nicht zulassen                         |
| Hochsensible Daten ohne Freigabe          | Nicht starten                          |
| Secrets im Klartext                       | Nicht zulässig als Betriebsstandard    |
| Agent mit Zugriff auf mehrere Kernsysteme | Sehr strenge Architektur und Kontrolle |

---

# 17. Beispielarchitekturen

## 17.1 Architektur 1: Sicheres On-Prem-n8n für interne Workflows

| Aspekt             | Beschreibung                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Ziel               | Interne Prozesse automatisieren, ohne Daten an SaaS-Plattformen zu übertragen                                      |
| Komponenten        | n8n self-hosted, Reverse Proxy, interne Datenbank, Servicekonten, Secret Management, Logging, Backup, Rollenmodell |
| Vorteile           | Hohe Kontrolle, gute Integration interner Systeme                                                                  |
| Risiken            | Betriebsaufwand, Fehlkonfiguration, Secret-Verwaltung                                                              |
| Admin-Empfehlung   | Containerbetrieb mit Backup, Monitoring, TLS, Rollen, getrennten Umgebungen                                        |
| Geeignet für       | Mittelstand, interne IT, sensible Prozesse                                                                         |
| Nicht geeignet für | Unternehmen ohne Betriebsressourcen                                                                                |

---

## 17.2 Architektur 2: Cloud-Automatisierung mit Make für unkritische Prozesse

| Aspekt             | Beschreibung                                            |
| ------------------ | ------------------------------------------------------- |
| Ziel               | Schnelle Automatisierung zwischen SaaS-Anwendungen      |
| Komponenten        | Make, SaaS-Apps, API-Keys, OAuth, begrenzte Daten       |
| Vorteile           | Schneller Start, viele Konnektoren                      |
| Risiken            | Datenabfluss, Token-Missbrauch, Anbieterabhängigkeit    |
| Admin-Empfehlung   | Nur für freigegebene Daten und definierte SaaS-Prozesse |
| Geeignet für       | Marketing, Vertrieb, einfache Meldungen                 |
| Nicht geeignet für | HR-Akten, Finanzfreigaben, interne Admin-Aufgaben       |

---

## 17.3 Architektur 3: Lokaler KI-Agent ohne Internetzugriff

| Aspekt             | Beschreibung                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Ziel               | Interne Dokumente analysieren, ohne externe KI-Dienste                                        |
| Komponenten        | Lokales LLM, lokale Vektordatenbank, interne Dokumente, kein Internetzugriff, Freigabeprozess |
| Vorteile           | Reduzierter Datenabfluss, kontrollierbare Umgebung                                            |
| Risiken            | Modellqualität, Hardwarebedarf, Berechtigungskonzept                                          |
| Admin-Empfehlung   | Datenräume, RBAC, Logging und Testdaten konsequent einführen                                  |
| Geeignet für       | Regulierte Umgebungen, interne Wissenssuche                                                   |
| Nicht geeignet für | Echtzeit-Webrecherche, sehr große Modelle ohne Hardware                                       |

---

## 17.4 Architektur 4: Hybrid-Modell mit API-Gateway

| Aspekt             | Beschreibung                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| Ziel               | Interne Systeme kontrolliert mit Cloud-KI oder SaaS verbinden                                    |
| Komponenten        | Interne Automatisierungsplattform, Proxy, API-Gateway, Whitelisting, Logging, Datenschutzprüfung |
| Vorteile           | Balance aus Kontrolle und Cloud-Funktionalität                                                   |
| Risiken            | Komplexität, Fehlkonfiguration, Schnittstellenabhängigkeit                                       |
| Admin-Empfehlung   | Nur definierte APIs freigeben, keine direkten Datenbankzugriffe                                  |
| Geeignet für       | Unternehmen mit IT-Security und Cloud-Governance                                                 |
| Nicht geeignet für | Unkontrollierte Fachbereichsautomatisierung                                                      |

---

## 17.5 Architektur 5: Analyse-Agent mit Human-in-the-loop

| Aspekt             | Beschreibung                                                      |
| ------------------ | ----------------------------------------------------------------- |
| Ziel               | Agent analysiert und schlägt vor, Mensch entscheidet              |
| Komponenten        | Leserechte, Vorschlagsmodus, Ticket-Erstellung, manuelle Freigabe |
| Vorteile           | Niedrigeres Risiko, guter Einstieg                                |
| Risiken            | Mensch kann Vorschläge ungeprüft übernehmen                       |
| Admin-Empfehlung   | Klare Kennzeichnung als Vorschlag, keine verdeckten Schreibrechte |
| Geeignet für       | Tickets, E-Mails, Rechnungsprüfung, Wissensarbeit                 |
| Nicht geeignet für | Vollautonome kritische Prozesse                                   |

---

# 18. Praxisbeispiele

## 18.1 Automatische Ticketklassifizierung

| Punkt               | Bewertung                                                    |
| ------------------- | ------------------------------------------------------------ |
| Ziel                | Tickets nach Thema, Priorität und Zuständigkeit vorsortieren |
| Benötigte Zugriffe  | Ticketsystem lesen, optional kommentieren                    |
| Benötigte Daten     | Tickettext, Kategorie, SLA                                   |
| Berechtigungen      | Leserecht, optional Schreibrecht für Labels                  |
| Risiken             | Falsche Priorisierung, Datenschutz                           |
| Wenn Rechte fehlen  | Ohne Schreibrecht nur Vorschlag möglich                      |
| Sichere Alternative | Agent erstellt Klassifizierungsvorschlag                     |
| Admin-Bewertung     | Gut als Pilot mit Leserechten                                |

---

## 18.2 E-Mail-Zusammenfassung

| Punkt              | Bewertung                                      |
| ------------------ | ---------------------------------------------- |
| Ziel               | Eingehende Mails zusammenfassen                |
| Benötigte Zugriffe | Shared Mailbox oder definierter Ordner         |
| Daten              | Mailinhalt, Anhänge                            |
| Berechtigungen     | Lesen, kein Löschen                            |
| Risiken            | Personenbezogene Daten, vertrauliche Inhalte   |
| Wenn Rechte fehlen | Keine automatische Auswertung                  |
| Alternative        | Manuelles Weiterleiten an freigegebene Mailbox |
| Admin-Bewertung    | Nur mit klarer Mailbox und Datenschutzprüfung  |

---

## 18.3 Rechnungsvorprüfung

| Punkt                     | Bewertung                                       |
| ------------------------- | ----------------------------------------------- |
| Ziel                      | Rechnungen prüfen und Auffälligkeiten markieren |
| Zugriffe                  | Rechnungseingang, ERP optional lesend           |
| Daten                     | Rechnungsnummer, Betrag, Lieferant              |
| Berechtigungen            | Lesen, Vorschlag erstellen                      |
| Risiken                   | Falsche Bewertung, Zahlungsrisiko               |
| Wenn Schreibrechte fehlen | Keine Buchung möglich                           |
| Alternative               | Prüfbericht für Buchhaltung                     |
| Admin-Bewertung           | Kein autonomes Zahlen                           |

---

## 18.4 SharePoint-Dokumentensuche

| Punkt              | Bewertung                           |
| ------------------ | ----------------------------------- |
| Ziel               | Interne Dokumente auffindbar machen |
| Zugriffe           | SharePoint über Graph API           |
| Daten              | Dokumente, Metadaten                |
| Berechtigungen     | Rollenbasierter Zugriff             |
| Risiken            | Berechtigungsumgehung durch RAG     |
| Wenn Zugriff fehlt | Kein Index möglich                  |
| Alternative        | Freigegebener Dokumentenexport      |
| Admin-Bewertung    | Nur mit Berechtigungsvererbung      |

---

## 18.5 Benutzer-Onboarding

| Punkt                   | Bewertung                                        |
| ----------------------- | ------------------------------------------------ |
| Ziel                    | Benutzeranlage vorbereiten                       |
| Zugriffe                | HR-System, AD oder Entra ID                      |
| Daten                   | Name, Rolle, Abteilung                           |
| Berechtigungen          | Idealerweise zunächst kein direktes Schreibrecht |
| Risiken                 | Falsche Konten, falsche Gruppen                  |
| Wenn Adminrechte fehlen | Keine direkte Anlage                             |
| Alternative             | Ticket mit geprüften Parametern                  |
| Admin-Bewertung         | Schreibaktion nur mit Freigabe                   |

---

## 18.6 Passwort-Reset-Vorbereitung

| Punkt              | Bewertung                                   |
| ------------------ | ------------------------------------------- |
| Ziel               | Identitätsprüfung und Reset vorbereiten     |
| Zugriffe           | Ticketsystem, IAM                           |
| Daten              | Benutzeridentität, Anfrage                  |
| Berechtigungen     | Lesen, optional Reset über sicheren Prozess |
| Risiken            | Account Takeover                            |
| Wenn Rechte fehlen | Nur Empfehlung möglich                      |
| Alternative        | Self-Service Password Reset                 |
| Admin-Bewertung    | Kritisch, starke Kontrolle nötig            |

---

## 18.7 Serverstatus prüfen

| Punkt              | Bewertung                         |
| ------------------ | --------------------------------- |
| Ziel               | Status von Servern zusammenfassen |
| Zugriffe           | Monitoring, Logs                  |
| Daten              | CPU, RAM, Dienste, Fehler         |
| Berechtigungen     | Lesen                             |
| Risiken            | Offenlegung interner Struktur     |
| Wenn Zugriff fehlt | Keine Echtzeitbewertung           |
| Alternative        | Monitoring-Dashboard auswerten    |
| Admin-Bewertung    | Gut geeignet mit Read-only        |

---

## 18.8 Logdateien analysieren

| Punkt              | Bewertung                                   |
| ------------------ | ------------------------------------------- |
| Ziel               | Fehlerursachen finden                       |
| Zugriffe           | Logsystem oder SIEM                         |
| Daten              | Logs, Events                                |
| Berechtigungen     | Lesen, eventuell eingeschränkt              |
| Risiken            | Secrets oder personenbezogene Daten in Logs |
| Wenn Zugriff fehlt | Analyse nur mit Export                      |
| Alternative        | Redacted Log Export                         |
| Admin-Bewertung    | Nur mit Log-Hygiene                         |

---

## 18.9 CRM-Daten anreichern

| Punkt                     | Bewertung                      |
| ------------------------- | ------------------------------ |
| Ziel                      | Kundendaten ergänzen           |
| Zugriffe                  | CRM, externe Quellen           |
| Daten                     | Kundendaten                    |
| Berechtigungen            | Schreibrechte kritisch         |
| Risiken                   | Falsche Daten, Datenschutz     |
| Wenn Schreibrechte fehlen | Nur Vorschlag                  |
| Alternative               | Review durch Vertrieb          |
| Admin-Bewertung           | Schreibrechte nur kontrolliert |

---

## 18.10 Meetingprotokolle verarbeiten

| Punkt              | Bewertung                                          |
| ------------------ | -------------------------------------------------- |
| Ziel               | Protokolle zusammenfassen und Aufgaben extrahieren |
| Zugriffe           | Teams, SharePoint, Kalender                        |
| Daten              | Gesprächsinhalte                                   |
| Berechtigungen     | Lesen, optional Aufgaben erstellen                 |
| Risiken            | Vertraulichkeit, personenbezogene Daten            |
| Wenn Zugriff fehlt | Manuelles Hochladen                                |
| Alternative        | Freigegebener Protokollordner                      |
| Admin-Bewertung    | Gute Schulungsanwendung, aber Datenschutz prüfen   |

---

## 18.11 Sicherheitsmeldungen zusammenfassen

| Punkt              | Bewertung                                              |
| ------------------ | ------------------------------------------------------ |
| Ziel               | Security Alerts priorisieren                           |
| Zugriffe           | SIEM, EDR, Mailbox                                     |
| Daten              | Sicherheitsereignisse                                  |
| Berechtigungen     | Lesen                                                  |
| Risiken            | Falsch negative Bewertung                              |
| Wenn Zugriff fehlt | Keine zentrale Analyse                                 |
| Alternative        | Export aus SIEM                                        |
| Admin-Bewertung    | Agent darf nicht automatisch deaktivieren oder löschen |

---

## 18.12 Daten aus Formularen übernehmen

| Punkt                     | Bewertung                                 |
| ------------------------- | ----------------------------------------- |
| Ziel                      | Formulare in Zielsystem übertragen        |
| Zugriffe                  | Formularsystem, Zielsystem                |
| Daten                     | Eingaben, Anhänge                         |
| Berechtigungen            | Schreiben ins Zielsystem                  |
| Risiken                   | Falsche Übernahme, Injection, Datenschutz |
| Wenn Schreibrechte fehlen | Nur CSV oder Ticket                       |
| Alternative               | Genehmigungsworkflow                      |
| Admin-Bewertung           | Gut mit Validierung und Logging           |

---

# 19. Risiken und Gegenmaßnahmen

| Risiko                         | Beschreibung                                   | Beispiel                              | Auswirkung                        | Gegenmaßnahme              | Verantwortliche Rolle    |
| ------------------------------ | ---------------------------------------------- | ------------------------------------- | --------------------------------- | -------------------------- | ------------------------ |
| Datenabfluss                   | Daten verlassen unkontrolliert das Unternehmen | Prompt enthält Kundendaten            | Datenschutz- und Geheimnisschaden | DLP, Proxy, lokale Modelle | Datenschutz, IT-Security |
| Zu hohe Berechtigungen         | Agent darf mehr als nötig                      | Schreibrechte auf gesamtes CRM        | Großer Schadensradius             | Least Privilege, RBAC      | IAM, IT                  |
| Fehlerhafte Automatisierung    | Workflow handelt falsch                        | Falsches Ticket geschlossen           | Betriebsstörung                   | Test, Review, Rollback     | Workflow Owner           |
| Prompt Injection               | Eingaben manipulieren Agent                    | Webseite enthält versteckte Anweisung | Fehlaktion, Datenabfluss          | Whitelist, Tool-Begrenzung | IT-Security              |
| Unsichere Plugins              | Tool hat zu viele Rechte                       | Plugin darf Dateien löschen           | Kompromittierung                  | Tool Review, Sandbox       | Plattformteam            |
| Unkontrollierte Webzugriffe    | Agent surft frei                               | Ruft unsichere Seite auf              | Malware, Fehlinformation          | Proxy, Whitelist           | Netzwerkteam             |
| Unklare Verantwortlichkeiten   | Niemand fühlt sich zuständig                   | Workflow fällt aus                    | Lange Störung                     | Owner definieren           | Management               |
| Fehlendes Logging              | Aktionen nicht nachvollziehbar                 | API-Key missbraucht                   | Keine Forensik                    | Zentrales Logging          | Betrieb                  |
| Fehlende Notfallabschaltung    | Workflow läuft weiter                          | Massenmailversand                     | Eskalation                        | Kill Switch                | Plattformteam            |
| Schatten-IT                    | Fachbereich baut unkontrolliert                | Zapier mit Kundendaten                | Compliance-Risiko                 | Freigegebene Plattform     | IT-Leitung               |
| Nicht dokumentierte Workflows  | Wissen fehlt                                   | Ersteller verlässt Firma              | Betriebsrisiko                    | Dokumentationspflicht      | Fachlicher Owner         |
| Abgelaufene Zertifikate        | TLS bricht                                     | API nicht erreichbar                  | Ausfall                           | Zertifikatsmonitoring      | Betrieb                  |
| Kompromittierte API-Keys       | Token wird missbraucht                         | Externer Zugriff                      | Datenverlust                      | Vault, Rotation            | IT-Security              |
| Fehlende Testumgebung          | Direkt produktiv getestet                      | Datenfehler                           | Betriebsstörung                   | Dev/Test/Prod trennen      | IT                       |
| Fehlerhafte Datenbasis         | Agent nutzt falsche Daten                      | Alter Preisstand                      | Falsche Entscheidung              | Datenqualität prüfen       | Fachbereich              |
| Halluzinationen                | KI erzeugt falsche Inhalte                     | Falsche Rechtsauskunft                | Fehlentscheidung                  | Quellenpflicht, Review     | Fachbereich              |
| Fehlende menschliche Kontrolle | Agent handelt autonom                          | Löscht Daten                          | Schaden                           | Human-in-the-loop          | Prozessowner             |
| Vendor Lock-in                 | Starke Anbieterbindung                         | Proprietäre Workflows                 | Wechselkosten                     | Exportstrategie            | IT-Leitung               |
| Datenschutzverstöße            | Unzulässige Verarbeitung                       | HR-Daten in Cloud                     | Bußgeld- und Reputationsrisiko    | Datenschutzprüfung         | Datenschutz              |
| Compliance-Probleme            | Vorgaben nicht erfüllt                         | Keine Audit Trails                    | Audit-Feststellung                | Governance                 | Compliance               |

CIS Controls betonen unter anderem Audit Log Management, also Sammeln, Speichern und Auswerten von Audit Logs zur Erkennung, Untersuchung und Wiederherstellung nach Angriffen. ([CIS][14]) Für Agenten und Automatisierung ist das besonders relevant, weil technische Aktionen sonst nicht sauber nachvollzogen werden können.

---

# 20. Abschluss und Kernaussagen

Automatisierung braucht klare Grenzen. KI-Agenten benötigen definierte Identitäten, Berechtigungen, Netzwerkwege, Datenzugriffe, Tool-Rechte und Protokollierung.

Die wichtigsten Erkenntnisse:

* Automatisierung braucht klare linke und rechte Grenzen.
* Agenten brauchen definierte Berechtigungen.
* Nicht alles, was technisch möglich ist, ist betrieblich sinnvoll.
* Gesperrte Funktionen haben oft gute Sicherheitsgründe.
* Alternativen sind möglich, müssen aber bewusst geplant werden.
* On-Prem, Cloud und Hybrid haben unterschiedliche Risiken.
* KI-Manager müssen frühzeitig mit Systemadministration, Datenschutz und Informationssicherheit sprechen.
* Der sicherste Einstieg ist häufig ein Nur-Lese- oder Vorschlagsmodus mit menschlicher Freigabe.
* Produktivzugriffe sollten erst nach Tests, Dokumentation und Freigabe erfolgen.
* Lokale KI reduziert Datenabflussrisiken, ersetzt aber kein Governance- und Betriebskonzept.
* Cloud-Automatisierung ist nicht grundsätzlich falsch, benötigt aber klare Daten- und Zugriffsbewertung.
* Agenten mit Tool-Zugriff sind besonders sorgfältig zu begrenzen.

---

# Zusatzteil A: Admin-Checkliste

| Prüffrage                                                | Ja/Nein | Bemerkung |
| -------------------------------------------------------- | ------: | --------- |
| Gibt es einen technischen Owner?                         |         |           |
| Gibt es einen fachlichen Owner?                          |         |           |
| Gibt es Test, Entwicklung und Produktion getrennt?       |         |           |
| Sind Servicekonten dokumentiert?                         |         |           |
| Sind Rechte minimal vergeben?                            |         |           |
| Sind Schreibrechte begründet?                            |         |           |
| Sind Löschrechte ausgeschlossen oder abgesichert?        |         |           |
| Werden Secrets in einem Vault gespeichert?               |         |           |
| Gibt es Logging?                                         |         |           |
| Gibt es Monitoring?                                      |         |           |
| Gibt es Backups?                                         |         |           |
| Gibt es eine Notfallabschaltung?                         |         |           |
| Sind Zertifikate gültig und überwacht?                   |         |           |
| Ist Proxy/DNS/Firewall geklärt?                          |         |           |
| Gibt es eine Update-Strategie?                           |         |           |
| Gibt es eine Dokumentation des Workflows?                |         |           |
| Sind Datenschutz und Informationssicherheit eingebunden? |         |           |

---

# Zusatzteil B: KI-Manager-Checkliste

| Frage                                            | Zweck                           |
| ------------------------------------------------ | ------------------------------- |
| Welcher Geschäftsprozess soll verbessert werden? | Verhindert Technik ohne Nutzen  |
| Welche Daten werden verarbeitet?                 | Datenschutz und Klassifizierung |
| Welche Systeme sind beteiligt?                   | Schnittstellenanalyse           |
| Gibt es APIs?                                    | Technische Machbarkeit          |
| Welche Aktionen soll der Agent ausführen?        | Rechtebedarf                    |
| Reicht ein Vorschlagsmodus?                      | Risiko reduzieren               |
| Wer genehmigt Aktionen?                          | Human-in-the-loop               |
| Wer ist verantwortlich bei Fehlern?              | Betriebsklarheit                |
| Wie wird Erfolg gemessen?                        | Nutzenbewertung                 |
| Wie wird Missbrauch verhindert?                  | Sicherheitskonzept              |
| Wie wird dokumentiert?                           | Auditierbarkeit                 |
| Wann wird der Workflow abgeschaltet?             | Lebenszyklusmanagement          |

---

# Zusatzteil C: Risiko-Checkliste

| Risiko               | Prüfen                                                  |
| -------------------- | ------------------------------------------------------- |
| Datenabfluss         | Werden Daten extern übertragen?                         |
| Zu hohe Rechte       | Hat der Agent mehr Rechte als nötig?                    |
| Fehlaktion           | Kann der Agent produktive Daten verändern?              |
| Löschung             | Kann der Agent Daten löschen?                           |
| Prompt Injection     | Nutzt der Agent Web, E-Mail oder Dokumente als Eingabe? |
| Secrets              | Werden Tokens sicher gespeichert?                       |
| Logging              | Sind Aktionen nachvollziehbar?                          |
| Datenschutz          | Sind personenbezogene Daten betroffen?                  |
| Betrieb              | Gibt es Monitoring und Backup?                          |
| Verantwortlichkeit   | Gibt es Owner?                                          |
| Anbieterabhängigkeit | Ist ein Wechsel möglich?                                |
| Notfall              | Gibt es Kill Switch und Rollback?                       |

---

# Zusatzteil D: Schnelle Entscheidungshilfe

| Vorhaben                         | Erste Bewertung | Empfehlung                              |
| -------------------------------- | --------------- | --------------------------------------- |
| Interne Dokumente zusammenfassen | Grün bis Gelb   | Mit Leserechten und Datenräumen starten |
| Tickets klassifizieren           | Grün            | Vorschlagsmodus verwenden               |
| E-Mails automatisch beantworten  | Gelb            | Entwürfe statt Direktversand            |
| CRM automatisch ändern           | Gelb bis Rot    | Schreibrechte nur mit Freigabe          |
| Benutzer automatisch anlegen     | Rot             | Genehmigungsworkflow                    |
| Dateien automatisch löschen      | Rot             | Nicht autonom erlauben                  |
| Web-Agent mit Produktivdaten     | Rot             | Vermeiden oder stark begrenzen          |
| Cloud-KI mit Kundendaten         | Gelb bis Rot    | Datenschutz und Vertragsprüfung         |
| Lokales LLM für internes Wissen  | Grün bis Gelb   | Governance nicht vergessen              |
| PowerShell auf Servern           | Gelb bis Rot    | Signierte Runbooks, JEA, Logging        |

---

# Zusatzteil E: Cloud, On-Prem oder Hybrid?

| Kriterium                   | Cloud                              | On-Prem                   | Hybrid                      |
| --------------------------- | ---------------------------------- | ------------------------- | --------------------------- |
| Schneller Start             | Sehr gut                           | Mittel                    | Mittel                      |
| Datenkontrolle              | Eingeschränkt                      | Hoch                      | Hoch, wenn sauber gestaltet |
| Betriebsaufwand             | Niedrig                            | Hoch                      | Mittel                      |
| Zugriff auf interne Systeme | Schwierig                          | Gut                       | Gut über Gateway            |
| Datenschutz                 | Prüfungsintensiv                   | Ebenfalls prüfpflichtig   | Prüfungsintensiv            |
| Skalierung                  | Einfach                            | Hardwareabhängig          | Gut                         |
| Kostenmodell                | Laufende Gebühren                  | Hardware und Betrieb      | Gemischt                    |
| Geeignet für                | SaaS-Prozesse                      | sensible interne Prozesse | kontrollierte Integration   |
| Hauptrisiko                 | Datenabfluss, Anbieterabhängigkeit | Betriebsfehler, Wartung   | Komplexität                 |

---

# Zusatzteil F: Was darf ein Agent niemals ohne Freigabe tun?

| Aktion                                        | Warum kritisch?                            | Sichere Alternative                 |
| --------------------------------------------- | ------------------------------------------ | ----------------------------------- |
| Benutzerkonten anlegen                        | Identitäts- und Rechteproblem              | Genehmigtes Onboarding-Ticket       |
| Gruppenmitgliedschaften ändern                | Rechteausweitung möglich                   | Vier-Augen-Freigabe                 |
| Daten löschen                                 | Datenverlust                               | Papierkorb, Vorschlag, Freigabe     |
| Zahlungen auslösen                            | Finanzschaden                              | Prüfbericht                         |
| Verträge versenden                            | Rechtliche Wirkung                         | Entwurf mit Freigabe                |
| Kunden automatisch anschreiben                | Reputations- und Datenschutzrisiko         | Mailentwurf                         |
| Produktionssysteme ändern                     | Ausfallrisiko                              | Change-Prozess                      |
| Firewall-Regeln ändern                        | Sicherheitsarchitektur betroffen           | Netzwerk-Freigabeprozess            |
| Secrets anzeigen                              | Kompromittierungsrisiko                    | Secret Vault ohne Anzeige           |
| Freien Code ausführen                         | Malware- und Missbrauchsrisiko             | Signierte Skripte                   |
| Externe Webseiten mit internen Daten aufrufen | Datenabfluss                               | Whitelist und Proxy                 |
| RAG über alle Unternehmensdaten ausführen     | Berechtigungsumgehung                      | Datenräume und RBAC                 |
| Logs ungefiltert an KI geben                  | Secrets und personenbezogene Daten möglich | Redaction und SIEM-Auswertung       |
| Tickets endgültig schließen                   | Prozessfehler möglich                      | Vorschlag oder Status „zur Prüfung“ |
| E-Mails massenhaft versenden                  | Missbrauch und Reputationsschaden          | Versandlimits und Freigabe          |

---

# Schlussformel für den KI-Manager-Lehrgang

Ein KI-Agent ist aus Administrationssicht kein autonomer Mitarbeiter, sondern ein technischer Akteur mit begrenzten Rechten. Gute KI- und Automatisierungsberatung bedeutet deshalb nicht, möglichst viele Freiheiten zu schaffen, sondern einen kontrollierten Handlungsrahmen zu definieren:

> **So viel Zugriff wie nötig, so wenig Rechte wie möglich, so viel Protokollierung wie erforderlich und so viel menschliche Freigabe wie für den jeweiligen Prozess angemessen.**

[1]: https://www.iso.org/standard/27001?utm_source=chatgpt.com "ISO/IEC 27001:2022 - Information security management ..."
[2]: https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com "IT-Grundschutz-Kompendium"
[3]: https://csrc.nist.gov/pubs/sp/800/207/final?utm_source=chatgpt.com "SP 800-207, Zero Trust Architecture | CSRC"
[4]: https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com "OWASP Top 10 for Large Language Model Applications"
[5]: https://learn.microsoft.com/de-de/entra/id-governance/scenarios/least-privileged?utm_source=chatgpt.com "Das Prinzip der geringsten Rechte mit Microsoft Entra ID ..."
[6]: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure?utm_source=chatgpt.com "What is Microsoft Entra Privileged Identity Management?"
[7]: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html?utm_source=chatgpt.com "AI Agent Security - OWASP Cheat Sheet Series"
[8]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/?utm_source=chatgpt.com "LLM01:2025 Prompt Injection - OWASP Gen AI Security Project"
[9]: https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines?utm_source=chatgpt.com "Security baselines guide"
[10]: https://gdpr-info.eu/art-5-gdpr/?utm_source=chatgpt.com "Art. 5 GDPR – Principles relating to processing of personal ..."
[11]: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com "AI Act | Shaping Europe's digital future - European Union"
[12]: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive?utm_source=chatgpt.com "NIS2 Directive: securing network and information systems"
[13]: https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance?utm_source=chatgpt.com "NIS2 Technical Implementation Guidance - ENISA"
[14]: https://www.cisecurity.org/controls/cis-controls-navigator/v8?utm_source=chatgpt.com "CIS Critical Security Controls Navigator - v8"
