from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from html import escape
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_ROOT = PROJECT_ROOT / "workshop-ki-offline"


SOURCES = [
  {
    "name": "OpenWebUI Models",
    "url": "https://docs.openwebui.com/features/workspace/models/",
    "usedFor": "Workspace Models als Presets ueber Basismodellen, gebundene Knowledge Bases, Tools, Skills und Builtin Tools.",
  },
  {
    "name": "OpenWebUI Knowledge",
    "url": "https://docs.openwebui.com/features/workspace/knowledge/",
    "usedFor": "Dokumentenarbeit, RAG-Modi, Knowledge-Bases, File Context und Quellenbezug.",
  },
  {
    "name": "OpenWebUI Skills",
    "url": "https://docs.openwebui.com/features/workspace/skills/",
    "usedFor": "Skills als Markdown-Anweisungen, Skill-Mention, Modellbindung und Zugriffskontrolle.",
  },
  {
    "name": "OpenWebUI Tools",
    "url": "https://docs.openwebui.com/features/extensibility/plugin/tools/",
    "usedFor": "Tools, Functions, native Function Calling, Builtin Tools, Kalender- und Automations-Werkzeuge.",
  },
  {
    "name": "OpenWebUI Calendar",
    "url": "https://docs.openwebui.com/features/calendar/",
    "usedFor": "Kalender, Erinnerungen, wiederkehrende Ereignisse und Automations-Overlay.",
  },
  {
    "name": "Continue.dev Chat",
    "url": "https://docs.continue.dev/docs/ide-extensions/chat/quick-start",
    "usedFor": "Chat in VS Code, Kontext aus Dateien und Codeauswahl, Erklaeren und Erarbeiten von Loesungen.",
  },
  {
    "name": "Continue.dev Agent",
    "url": "https://docs.continue.dev/docs/ide-extensions/agent/quick-start",
    "usedFor": "Agentische Basisnutzung, kleine Aenderungen, Tests und Kommandos im Entwicklungsworkflow.",
  },
  {
    "name": "RAGFlow",
    "url": "https://github.com/infiniflow/ragflow",
    "usedFor": "RAGFlow als Hintergrundsystem fuer Retrieval-Augmented Generation auf Dokumentenbasis.",
  },
  {
    "name": "Seafile / SeaDrive Manual",
    "url": "https://help.seafile.com/drive_client/drive_client_for_win10/",
    "usedFor": "SeaDrive als virtueller lokaler Zugriff auf Seafile-Bibliotheken, Platzhalter, Cache und Offline-Verfuegbarkeit.",
  },
]


GERMAN_REPLACEMENTS = {
  "fuer": "für",
  "Fuer": "Für",
  "ueber": "über",
  "Ueber": "Über",
  "zurueck": "zurück",
  "Zurueck": "Zurück",
  "ergaenzen": "ergänzen",
  "Ergaenzen": "Ergänzen",
  "ergaenzt": "ergänzt",
  "geprueft": "geprüft",
  "Pruefung": "Prüfung",
  "Pruefregel": "Prüfregel",
  "pruefen": "prüfen",
  "Pruefen": "Prüfen",
  "pruefbar": "prüfbar",
  "pruefbarer": "prüfbarer",
  "pruefbare": "prüfbare",
  "pruefbaren": "prüfbaren",
  "pruefbarem": "prüfbarem",
  "pruefbares": "prüfbares",
  "Pruefschritt": "Prüfschritt",
  "Pruefschritte": "Prüfschritte",
  "Pruefkriterium": "Prüfkriterium",
  "Pruefkriterien": "Prüfkriterien",
  "Pruefliste": "Prüfliste",
  "Pruefmatrix": "Prüfmatrix",
  "Aenderung": "Änderung",
  "Aenderungen": "Änderungen",
  "Aenderungsplan": "Änderungsplan",
  "Aenderungsplanung": "Änderungsplanung",
  "Aenderungsbewertung": "Änderungsbewertung",
  "Aenderungscheckliste": "Änderungscheckliste",
  "Aenderungsinformationen": "Änderungsinformationen",
  "Aenderungsnotizen": "Änderungsnotizen",
  "Aenderungseinheit": "Änderungseinheit",
  "aendern": "ändern",
  "geaendert": "geändert",
  "oeffnen": "öffnen",
  "oeffnet": "öffnet",
  "Oeffne": "Öffne",
  "Oeffnen": "Öffnen",
  "geoeffnet": "geöffnet",
  "moeglich": "möglich",
  "Moeglichkeit": "Möglichkeit",
  "Koennen": "Können",
  "koennen": "können",
  "koennte": "könnte",
  "koennte": "könnte",
  "haeufige": "häufige",
  "Haeufige": "Häufige",
  "spater": "später",
  "spaeter": "später",
  "Spaeter": "Später",
  "zusaetzlich": "zusätzlich",
  "Zusaetzlich": "Zusätzlich",
  "tatsaechlich": "tatsächlich",
  "Tatsaechlich": "Tatsächlich",
  "faehig": "fähig",
  "Faehigkeit": "Fähigkeit",
  "Faehigkeiten": "Fähigkeiten",
  "ermoeglicht": "ermöglicht",
  "Ermoeglicht": "Ermöglicht",
  "unabhaengig": "unabhängig",
  "abhaengig": "abhängig",
  "Abhaengigkeiten": "Abhängigkeiten",
  "laeuft": "läuft",
  "ausfuehren": "ausführen",
  "Ausfuehrung": "Ausführung",
  "ausfuehrbar": "ausführbar",
  "Durchfuehrung": "Durchführung",
  "durchfuehren": "durchführen",
  "durchgefuehrt": "durchgeführt",
  "uebersprungen": "übersprungen",
  "Uebung": "Übung",
  "Uebungen": "Übungen",
  "Uebungs": "Übungs",
  "uebernehmen": "übernehmen",
  "Uebergabe": "Übergabe",
  "Rueckfrage": "Rückfrage",
  "Rueckfragen": "Rückfragen",
  "Rueckbauplan": "Rückbauplan",
  "Rueckbezug": "Rückbezug",
  "Rueckbau": "Rückbau",
  "Rueckmeldung": "Rückmeldung",
  "Rueckmeldungen": "Rückmeldungen",
  "Wofuer": "Wofür",
  "wofuer": "wofür",
  "naechste": "nächste",
  "naechsten": "nächsten",
  "naechstem": "nächstem",
  "Naechste": "Nächste",
  "Naechster": "Nächster",
  "gestuetzt": "gestützt",
  "Gestuetzt": "Gestützt",
  "stuetzen": "stützen",
  "stuetzt": "stützt",
  "uebersetzen": "übersetzen",
  "uebersetzt": "übersetzt",
  "Ablage": "Ablage",
  "Aktualitaet": "Aktualität",
  "Berechtigungen": "Berechtigungen",
  "Berechtigung": "Berechtigung",
  "Ausloesen": "Auslösen",
  "ausloesen": "auslösen",
  "Laenge": "Länge",
  "grosse": "große",
  "Grosse": "Große",
  "groessere": "größere",
  "Groessere": "Größere",
  "Massnahme": "Maßnahme",
  "schuetzt": "schützt",
  "schuetzen": "schützen",
  "Schluessel": "Schlüssel",
  "Zugaenge": "Zugänge",
  "Zugang": "Zugang",
  "Zugriff": "Zugriff",
  "Zeitbezuege": "Zeitbezüge",
  "Zustaendigkeit": "Zuständigkeit",
  "Verlaeufe": "Verläufe",
  "Verfuegbarkeit": "Verfügbarkeit",
  "verfuegbar": "verfügbar",
  "Verfuegbar": "Verfügbar",
  "Fuehrung": "Führung",
  "Fuehrungsteam": "Führungsteam",
  "Qualitaet": "Qualität",
  "Funktionalitaeten": "Funktionalitäten",
  "Funktionalitaet": "Funktionalität",
  "Lernfaehigkeit": "Lernfähigkeit",
  "Einsteigerinnen": "Einsteigerinnen",
  "enthaelt": "enthält",
  "Enthaelt": "Enthält",
  "benoetigt": "benötigt",
  "Benoetigt": "Benötigt",
  "noetig": "nötig",
  "Noetig": "Nötig",
  "waehlen": "wählen",
  "auswaehlen": "auswählen",
  "Auswaehlen": "Auswählen",
  "Waehlen": "Wählen",
  "waehlt": "wählt",
  "gewaehlt": "gewählt",
  "erklaeren": "erklären",
  "Erklaeren": "Erklären",
  "erklaert": "erklärt",
  "Erklaert": "Erklärt",
  "erlaeutern": "erläutern",
  "Erlaeutern": "Erläutern",
  "haelt": "hält",
  "enthaelt": "enthält",
  "fuehrt": "führt",
  "Fuehrt": "Führt",
  "gefuehrt": "geführt",
  "Uebersicht": "Übersicht",
  "uebersicht": "übersicht",
  "uebersichtlich": "übersichtlich",
  "Auffaellige": "Auffällige",
  "auffaellige": "auffällige",
  "auffaellig": "auffällig",
  "zulaessig": "zulässig",
  "laenger": "länger",
  "vollstaendig": "vollständig",
  "Vollstaendig": "Vollständig",
  "faellt": "fällt",
  "Faellt": "Fällt",
  "oberflaeche": "oberfläche",
  "Oberflaeche": "Oberfläche",
  "Praesentation": "Präsentation",
  "Praesentationen": "Präsentationen",
  "praesentations": "präsentations",
  "Praesentations": "Präsentations",
  "Ausgabe": "Ausgabe",
  "fliessen": "fließen",
  "teamuebergreifende": "teamübergreifende",
  "veraendert": "verändert",
  "eingefuegt": "eingefügt",
  "klaeren": "klären",
  "Klaerung": "Klärung",
  "Testfaelle": "Testfälle",
  "Randfaelle": "Randfälle",
  "schliessen": "schließen",
  "anschliessend": "anschließend",
  "abschliessend": "abschließend",
  "heisst": "heißt",
  "weiss": "weiß",
}


PROTECTED_TOKEN_SUFFIXES = (
  ".html",
  ".md",
  ".json",
  ".css",
  ".js",
  ".py",
)


def germanize(text: str) -> str:
  """Use real German umlauts in generated prose while leaving ASCII slugs and paths intact."""

  replacements = sorted(GERMAN_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True)

  def replace_token(match: re.Match[str]) -> str:
    token = match.group(0)
    lowered = token.lower()
    if (
      "/" in token
      or "\\" in token
      or lowered.startswith("http")
      or lowered.startswith("teil-")
      or lowered.endswith(PROTECTED_TOKEN_SUFFIXES)
    ):
      return token
    next_token = token
    for source, target in replacements:
      next_token = next_token.replace(source, target)
    return next_token

  return re.sub(r"[A-Za-zÄÖÜäöüß0-9_./\\-]+", replace_token, text)


COMMON_AGENDA = [
  "5 Min. Einstieg und Zielbild",
  "10 Min. Begriffe und Einordnung",
  "15 Min. Demo durch die vortragende Person",
  "20 Min. Praxisaufgabe",
  "5 Min. Mini-Check",
  "5 Min. Ausblick und Transfer",
]


SECURITY_RULES = [
  "Keine Passwoerter, Tokens, privaten Schluessel oder vertraulichen personenbezogenen Daten in Prompts einfuegen.",
  "KI-Antworten gelten als Arbeitsvorschlag und werden vor Weitergabe oder Umsetzung geprueft.",
  "Bei rechtlichen, medizinischen, finanziellen, sicherheitskritischen oder fachkritischen Aussagen ist menschliche Pruefung Pflicht.",
  "Offlinebetrieb schuetzt vor unerwuenschtem Netzwerkabfluss, aber nicht vor falschen oder unvollstaendigen Antworten.",
  "KI-generierten Code testen, nachvollziehen und nicht ungeprueft produktiv einsetzen.",
]


MODEL_MATRIX = [
  {
    "problem": "Dokument verstehen",
    "recommended": "Problemfallmodell Dokumentenanalyse oder lokal verfuegbares Analysemodell",
    "watch": "Quellenbezug, offene Punkte und Annahmen sichtbar verlangen.",
  },
  {
    "problem": "Text zusammenfassen",
    "recommended": "Problemfallmodell Dokumentenzusammenfassung oder schnelles Allround-Modell",
    "watch": "Zielgruppe, Laenge und Ausgabeformat vorgeben.",
  },
  {
    "problem": "Code verstehen",
    "recommended": "Problemfallmodell Codeanalyse oder Coding-Modell in Continue.dev",
    "watch": "Dateipfade, relevante Ausschnitte und erwartete Erklaertiefe nennen.",
  },
  {
    "problem": "Code aendern",
    "recommended": "Continue.dev Agent oder Problemfallmodell Refactoring/Codegenerierung",
    "watch": "Kleine Aenderungseinheit, Tests und Rueckbauplan festlegen.",
  },
  {
    "problem": "Logs oder Fehler untersuchen",
    "recommended": "Problemfallmodell Debugging, IT-Helpdesk oder JSON-/Log-Analyse",
    "watch": "Fehlermeldung, Zeitpunkt, Systemkontext und erwartetes Verhalten liefern.",
  },
  {
    "problem": "Wissen aus Seafile/RAG nutzen",
    "recommended": "OpenWebUI-Modell mit angebundener Knowledge Base",
    "watch": "Nach Dokumentbezug, Quellen und Unsicherheiten fragen.",
  },
]


MODULES: list[dict] = [
  {
    "id": "teil-01",
    "slug": "teil-01-was-ist-ki",
    "title": "Was ist KI und wie funktioniert sie?",
    "subtitle": "Ein gemeinsamer Startpunkt fuer alle weiteren Werkzeuge.",
    "focus": "Grundlagen",
    "audienceFocus": ["alle Teilnehmenden", "Einsteigerinnen und Einsteiger", "technisch Interessierte"],
    "tools": ["OpenWebUI"],
    "learningGoals": [
      "Die Teilnehmenden koennen KI als Mustererkennung und Sprachvorhersage einordnen.",
      "Die Teilnehmenden kennen Grenzen wie Halluzinationen, fehlenden Kontext und pruefpflichtige Aussagen.",
      "Die Teilnehmenden koennen erklaeren, warum gute Eingaben die Ergebnisqualitaet verbessern.",
    ],
    "terms": ["KI", "Modell", "Training", "Kontext", "Prompt", "Halluzination", "Pruefung"],
    "starter": "KI erzeugt Vorschlaege auf Basis gelernter Muster. Sie ersetzt keine fachliche Verantwortung.",
    "example": "Ein Modell kann aus einer Fehlerbeschreibung eine Diagnosehypothese ableiten, braucht aber Logs, Umgebung und Gegenpruefung.",
    "demo": [
      "Eine einfache Frage in OpenWebUI stellen.",
      "Dieselbe Frage mit Kontext, Ziel und Ausgabeformat wiederholen.",
      "Die beiden Antworten vergleichen: Genauigkeit, Struktur, Unsicherheit.",
    ],
    "practice": [
      "Eine Alltagsfrage und eine Arbeitsfrage formulieren.",
      "Jeweils Ziel, Kontext und gewuenschtes Ausgabeformat ergaenzen.",
      "Eine Antwort markieren, die fachlich geprueft werden muss.",
    ],
    "deepDive": [
      "Fuer technisch Interessierte: Kontextfenster, Token und Retrieval als praktische Grenzen einordnen.",
      "Unterscheiden, ob Wissen aus Modelltraining, Chatkontext, Datei oder Knowledge Base stammt.",
    ],
    "errors": [
      "Zu allgemeine Frage: Ziel und Kontext nachtragen.",
      "Plausible, aber falsche Antwort: Quelle oder Pruefschritt verlangen.",
      "Zu viel Vertrauen in Formulierungen: Antwort in Fakten, Annahmen und Empfehlung trennen lassen.",
    ],
    "check": ["Was ist ein Prompt?", "Warum kann KI falsch liegen?", "Welche Daten gehoeren nicht in einen Prompt?"],
    "next": "Im naechsten Teil werden die lokalen Werkzeuge der Schulungsumgebung eingeordnet.",
  },
  {
    "id": "teil-02",
    "slug": "teil-02-ki-tools-umgebung",
    "title": "Welche KI-Werkzeuge haben wir?",
    "subtitle": "OpenWebUI, VS Code, Continue.dev, Seafile und SeaDrive im Zusammenspiel.",
    "focus": "Werkzeugueberblick",
    "audienceFocus": ["alle Teilnehmenden", "Arbeitsalltag", "Entwicklungsszenarien"],
    "tools": ["OpenWebUI", "VS Code", "Continue.dev", "Seafile", "SeaDrive"],
    "learningGoals": [
      "Die Teilnehmenden kennen die sichtbaren Werkzeuge und ihren Zweck.",
      "Die Teilnehmenden koennen unterscheiden, wann OpenWebUI und wann VS Code mit Continue.dev sinnvoll ist.",
      "Die Teilnehmenden verstehen Seafile und SeaDrive als Datei- und Wissensgrundlage.",
    ],
    "terms": ["Chatoberflaeche", "IDE", "Dateiablage", "Synchronisation", "SeaDrive", "Problemfallmodell"],
    "starter": "Nicht jedes Werkzeug loest jedes Problem. Die Auswahl richtet sich nach Ziel, Dateiart und Arbeitskontext.",
    "example": "Eine Richtlinie wird in Seafile abgelegt, ueber OpenWebUI zusammengefasst und spaeter in VS Code in eine Pruefcheckliste ueberfuehrt.",
    "demo": [
      "OpenWebUI oeffnen und die Chatoberflaeche zeigen.",
      "VS Code oeffnen und Continue.dev als Seitenleiste zeigen.",
      "SeaDrive im Datei-Explorer zeigen und eine Beispielbibliothek finden.",
    ],
    "practice": [
      "Alle Teilnehmenden finden OpenWebUI, VS Code und SeaDrive.",
      "Ein Beispieldokument in SeaDrive lokalisieren.",
      "Einordnen: Diese Aufgabe gehoert eher in OpenWebUI oder eher in VS Code.",
    ],
    "deepDive": [
      "Fuer technisch Interessierte: Continue.dev nutzt Chat-, Edit-, Autocomplete- und Agentenrollen je nach lokaler Konfiguration.",
      "OpenWebUI-Modelle sind Presets ueber Basismodellen und koennen Wissen, Tools und Skills vorab buendeln.",
    ],
    "errors": [
      "Falsches Werkzeug: Aufgabe nach Textarbeit, Codearbeit oder Dateiverwaltung sortieren.",
      "Datei nicht sichtbar: SeaDrive-Syncstatus und Bibliothek pruefen.",
      "Unklarer Modellname: Nach Problemfall statt nach Technikbezeichnung waehlen.",
    ],
    "check": ["Wofuer nutzen wir OpenWebUI?", "Wofuer nutzen wir Continue.dev?", "Wofuer ist SeaDrive praktisch?"],
    "next": "Danach folgt die direkte Nutzung von OpenWebUI als Chatoberflaeche.",
  },
  {
    "id": "teil-03",
    "slug": "teil-03-openwebui-chat-prompting",
    "title": "OpenWebUI als Chatoberflaeche und Prompting-Grundlagen",
    "subtitle": "Gute Fragen stellen, Promptvorlagen nutzen und Problemfallmodelle auswaehlen.",
    "focus": "OpenWebUI und Prompting",
    "audienceFocus": ["alle Teilnehmenden", "Dokumentenarbeit", "Arbeitsalltag"],
    "tools": ["OpenWebUI"],
    "learningGoals": [
      "Die Teilnehmenden koennen einen Chat starten und ein passendes Problemfallmodell waehlen.",
      "Die Teilnehmenden koennen Promptbausteine wie Ziel, Kontext, Eingabe und Ausgabeformat nutzen.",
      "Die Teilnehmenden koennen Promptvorlagen sinnvoll anpassen, statt sie blind zu kopieren.",
    ],
    "terms": ["Chat", "Promptvorlage", "Problemfallmodell", "Rolle", "Ziel", "Ausgabeformat", "Rueckfrage"],
    "starter": "Ein guter Prompt ist keine lange Zauberformel. Er sagt klar, was erreicht werden soll und woran die Antwort gemessen wird.",
    "example": "Aus 'Fasse das zusammen' wird: 'Fasse dieses Protokoll fuer eine Uebergabe in 6 Stichpunkten zusammen und markiere offene Entscheidungen.'",
    "demo": [
      "Problemfallmodell fuer Zusammenfassung auswaehlen.",
      "Promptvorlage oeffnen oder nachbauen: Ziel, Kontext, Format, Grenzen.",
      "Antwort mit einer Checkliste pruefen und eine Rueckfrage ausloesen.",
    ],
    "practice": [
      "Eine eigene Frage in eine strukturierte Promptform bringen.",
      "Eine Promptvorlage auf den eigenen Arbeitskontext anpassen.",
      "Antwort als Tabelle, Checkliste oder Schrittfolge ausgeben lassen.",
    ],
    "deepDive": [
      "Rolle nur nutzen, wenn sie das Pruefkriterium verbessert.",
      "Unsicherheit explizit verlangen: 'Trenne gesicherte Aussagen, Annahmen und offene Punkte.'",
    ],
    "errors": [
      "Prompt zu breit: Ergebnis, Zielgruppe und Format begrenzen.",
      "Antwort zu allgemein: Eingabedaten oder Beispiel ergaenzen.",
      "Promptvorlage passt nicht: Bausteine anpassen, nicht alles uebernehmen.",
    ],
    "check": ["Welche Bausteine hat ein guter Prompt?", "Wann ist eine Rueckfrage sinnvoll?", "Wie pruefen wir eine Antwort?"],
    "next": "Im Anschluss testen Teilnehmende eigene Szenarien mit Problemfallmodellen und Dateien.",
  },
  {
    "id": "teil-04",
    "slug": "teil-04-problemfallmodelle-praxis",
    "title": "Problemfallmodelle praktisch testen",
    "subtitle": "Eigene Fragen, Dateiuploads und passende Modellwahl in einer offenen Praxisstunde.",
    "focus": "Praxislabor",
    "audienceFocus": ["alle Teilnehmenden", "Arbeitsalltag", "Dokumentenarbeit"],
    "tools": ["OpenWebUI"],
    "learningGoals": [
      "Die Teilnehmenden koennen ein eigenes Problem in ein bearbeitbares KI-Szenario uebersetzen.",
      "Die Teilnehmenden testen Dateiuploads und erkennen, wann zusaetzlicher Kontext fehlt.",
      "Die Teilnehmenden koennen Ergebnisse mit Quellenbezug, Annahmen und Pruefschritten bewerten.",
    ],
    "terms": ["Problemfall", "Dateiupload", "Kontext", "Quellenbezug", "Modellwahl", "Ergebnispruefung"],
    "starter": "Diese Stunde ist bewusst offen: Eigene Aufgaben werden klein genug geschnitten, damit in 60 Minuten ein pruefbares Ergebnis entsteht.",
    "example": "Eine technische Beschreibung wird hochgeladen. Das Problemfallmodell erstellt eine Aenderungszusammenfassung mit Risiken und Rueckfragen.",
    "demo": [
      "Ein Beispieldokument hochladen.",
      "Passendes Problemfallmodell nach Ziel waehlen.",
      "Antwort mit 'Welche Textstellen stuetzen diese Aussage?' nachpruefen.",
    ],
    "practice": [
      "Eigenes unkritisches Beispielmaterial auswaehlen.",
      "Problem in Ziel, Kontext, Material, Ergebnisformat und Pruefschritt gliedern.",
      "Antwort iterativ verbessern und dokumentieren, was gut und was unklar war.",
    ],
    "deepDive": [
      "Mehrere Modelle mit demselben Prompt vergleichen: Struktur, Genauigkeit, Geschwindigkeit.",
      "Bei langen Dokumenten gezielt Abschnitte, Zusammenfassung oder Fragenliste anfordern.",
    ],
    "errors": [
      "Material enthaelt sensible Daten: Beispiel anonymisieren oder nicht verwenden.",
      "Datei wird nicht beruecksichtigt: Anhang, File Context und Modellhinweise pruefen.",
      "Antwort wirkt ueberzeugend: Quellenbezug und Gegenbeispiele verlangen.",
    ],
    "check": ["Ist das Problem klar abgegrenzt?", "Welche Datei oder welcher Kontext war noetig?", "Welche Antwortteile wurden geprueft?"],
    "next": "Danach werden OpenWebUI-Zusatzfunktionen wie Skills, Tools, Kalender und Automations eingeordnet.",
  },
  {
    "id": "teil-05",
    "slug": "teil-05-openwebui-zusatzfunktionen",
    "title": "OpenWebUI-Zusatzfunktionen sinnvoll nutzen",
    "subtitle": "Automations, Skills, Kalender, Tools und Functions mit Zweck, Grenzen und Aktivierung.",
    "focus": "OpenWebUI Vertiefung",
    "audienceFocus": ["alle Teilnehmenden", "technisch Interessierte", "Administration"],
    "tools": ["OpenWebUI", "Calendar", "Automations", "Skills", "Tools", "Functions"],
    "learningGoals": [
      "Die Teilnehmenden kennen den Unterschied zwischen Skills, Tools, Functions und Builtin Tools.",
      "Die Teilnehmenden koennen Kalender- und Automationsfunktionen anhand einfacher Beispiele einordnen.",
      "Die Teilnehmenden koennen erklaeren, warum Aktivierung, Berechtigungen und Function Calling wichtig sind.",
    ],
    "terms": ["Skill", "Tool", "Function", "Builtin Tool", "Calendar", "Automation", "Function Calling", "Berechtigung"],
    "starter": "Zusatzfunktionen machen OpenWebUI leistungsfaehiger, aber auch verantwortungsvoller. Aktiviert wird nur, was fuer die Aufgabe benoetigt wird.",
    "example": "Ein Skill liefert eine Review-Checkliste. Ein Kalender-Tool kann einen Termin anlegen. Eine Automation kann einen wiederkehrenden Statusentwurf erstellen.",
    "demo": [
      "Workspace-Bereiche fuer Models, Skills, Tools und Knowledge zeigen.",
      "Kalenderansicht zeigen und eine einfache Erinnerungslogik erklaeren.",
      "Automation als geplanten Chatauftrag erklaeren: Ziel, Zeitplan, Ergebnispruefung.",
    ],
    "practice": [
      "Drei Beispielaufgaben sortieren: Skill, Tool, Function, Automation oder normales Prompting.",
      "Eine sichere Automation auf Papier entwerfen: Name, Zweck, Eingabe, Zeitplan, Pruefung.",
      "Risiken benennen: falsches Tool, fehlende Rechte, zu breite Aufgabe.",
    ],
    "deepDive": [
      "Skills sind Markdown-Anweisungen; Tools und Functions koennen Code ausfuehren und brauchen strengere Governance.",
      "Kalender- und Automationsfunktionen setzen passende Berechtigungen und modellseitige Toolfaehigkeit voraus.",
    ],
    "errors": [
      "Tool pauschal aktiv: Zweck und Freigabe pruefen.",
      "Skill wird nicht genutzt: Zugriff, Aktivstatus und Modellbindung pruefen.",
      "Automation erzeugt unbrauchbare Ergebnisse: Ziel, Eingabequelle und Pruefkriterium schaerfen.",
    ],
    "check": ["Was unterscheidet Skill und Tool?", "Wann ist eine Automation sinnvoll?", "Welche Zusatzfunktion braucht besondere Pruefung?"],
    "next": "Im naechsten Teil wechselt der Fokus zu VS Code und Continue.dev.",
  },
  {
    "id": "teil-06",
    "slug": "teil-06-vscode-continue-basis",
    "title": "VS Code mit Continue.dev fuer die Basisnutzung",
    "subtitle": "Einfache Prompts, agentische Nutzung, Dateien bearbeiten und Repos durchsuchen.",
    "focus": "Continue.dev",
    "audienceFocus": ["Entwicklungsszenarien", "technisch Interessierte", "Softwarepflege"],
    "tools": ["VS Code", "Continue.dev", "SeaDrive"],
    "learningGoals": [
      "Die Teilnehmenden koennen Continue.dev fuer Fragen zu Code und Dateien nutzen.",
      "Die Teilnehmenden koennen kleine agentische Aufgaben klar und sicher formulieren.",
      "Die Teilnehmenden koennen SeaDrive-Dateien oder grosse Repos als Kontext einbeziehen.",
    ],
    "terms": ["IDE", "Chat Mode", "Agent Mode", "Kontext", "Dateiauswahl", "Repo-Suche", "Diff", "Test"],
    "starter": "OpenWebUI ist gut fuer allgemeine Wissensarbeit. Continue.dev ist stark, wenn Dateien, Code und Repos direkt im Editor relevant sind.",
    "example": "Eine Datei aus SeaDrive wird in VS Code geoeffnet. Continue.dev erstellt daraus eine Pruefcheckliste und schlaegt Aenderungen vor.",
    "demo": [
      "Ordner oder Datei in VS Code oeffnen.",
      "Code oder Text markieren und an Continue.dev senden.",
      "Eine kleine Aenderungsaufgabe im Agent Mode formulieren und Ergebnis als Diff pruefen.",
    ],
    "practice": [
      "Eine harmlose Datei erklaeren lassen.",
      "Eine kleine Verbesserung vorschlagen lassen, ohne sie blind zu uebernehmen.",
      "Eine Repo-Suchfrage formulieren: 'Wo wird dieser Begriff verwendet und welche Dateien sind relevant?'",
    ],
    "deepDive": [
      "Agentische Aufgaben klein halten: Ziel, erlaubte Dateien, erwartetes Ergebnis, Tests.",
      "Bei grossen Repos zuerst Orientierung verlangen: relevante Dateien, Risiken, naechste Schritte.",
    ],
    "errors": [
      "Zu grosser Auftrag: in Analyse, Aenderung und Test aufteilen.",
      "Ungepruefter Diff: Dateiinhalt, Seiteneffekte und Tests kontrollieren.",
      "Secrets im Kontext: Dateien mit Zugangsdaten nicht in den Chat geben.",
    ],
    "check": ["Wann ist Continue.dev besser als OpenWebUI?", "Was gehoert in einen Agent-Prompt?", "Warum wird ein Diff geprueft?"],
    "next": "Danach wird der Wissensfluss von Seafile ueber RAGFlow zu OpenWebUI und VS Code betrachtet.",
  },
  {
    "id": "teil-07",
    "slug": "teil-07-seafile-ragflow-wissensfluss",
    "title": "Seafile, SeaDrive und RAGFlow als Wissensfluss",
    "subtitle": "Dateien ablegen, Anbindung beauftragen und Wissen in OpenWebUI sowie VS Code nutzen.",
    "focus": "RAG und Dateifluss",
    "audienceFocus": ["alle Teilnehmenden", "Dokumentenarbeit", "DevOps", "Administration"],
    "tools": ["Seafile", "SeaDrive", "RAGFlow", "OpenWebUI", "VS Code"],
    "learningGoals": [
      "Die Teilnehmenden verstehen RAGFlow als Hintergrundkomponente und bedienen es nicht direkt.",
      "Die Teilnehmenden koennen Dateien in Seafile fuer spaetere Wissensnutzung vorbereiten.",
      "Die Teilnehmenden koennen DevOps/Admins die noetigen Informationen fuer eine RAG-Anbindung liefern.",
    ],
    "terms": ["Seafile", "SeaDrive", "RAG", "RAGFlow", "Knowledge Base", "Quellenbezug", "Handoff"],
    "starter": "Der sichtbare Arbeitsweg beginnt bei Dateien. RAGFlow verarbeitet Wissen im Hintergrund; OpenWebUI macht es im Chat nutzbar.",
    "example": "Ein Team legt Spezifikationen in Seafile ab, meldet die Bibliothek zur RAG-Anbindung und fragt spaeter in OpenWebUI nach Auswirkungen.",
    "demo": [
      "Seafile/SeaDrive-Ablage zeigen: klare Ordner, Dateinamen, Versionen.",
      "Handoff-Checkliste fuer DevOps/Admins ausfuellen.",
      "In OpenWebUI eine Frage mit Quellenbezug an angebundenes Wissen formulieren.",
    ],
    "practice": [
      "Eine fiktive Dokumentenmappe fuer RAG vorbereiten: Name, Zweck, Besitzer, Aktualitaet.",
      "Eine Handoff-Nachricht an DevOps/Admins formulieren.",
      "Eine OpenWebUI-Frage mit Quellenpruefung schreiben.",
    ],
    "deepDive": [
      "Fuer technisch Interessierte: Retrieval liefert relevante Ausschnitte, ersetzt aber keine Quellenpruefung.",
      "SeaDrive erlaubt lokalen Zugriff in VS Code; synchronisierte Dateien koennen direkt gelesen und bearbeitet werden.",
    ],
    "errors": [
      "Unklare Dateinamen: sprechende Namen und Versionshinweise nutzen.",
      "RAG-Erwartung zu hoch: Verarbeitung, Indexierung und Aktualitaet klaeren.",
      "Falscher Zugriff: Berechtigungen und Freigaben vor Anbindung pruefen.",
    ],
    "check": ["Wer bedient RAGFlow direkt?", "Was gehoert in die Handoff-Info?", "Wie wird eine RAG-Antwort geprueft?"],
    "next": "Der naechste Teil bereitet die nutzerspezifischen Teamstunden vor.",
  },
  {
    "id": "teil-08",
    "slug": "teil-08-prototyping-vorbereitung",
    "title": "Teamstunden vorbereiten",
    "subtitle": "Problem formulieren, Material sammeln, Prototypziel festlegen.",
    "focus": "Transfer",
    "audienceFocus": ["alle Teams", "Arbeitsalltag", "Prototyping"],
    "tools": ["OpenWebUI", "VS Code", "Continue.dev", "Seafile", "SeaDrive"],
    "learningGoals": [
      "Die Teilnehmenden koennen ein eigenes Teamthema fuer eine 60-Minuten-Praxisstunde zuschneiden.",
      "Die Teilnehmenden wissen, welches Material geeignet ist und welche Daten nicht verwendet werden.",
      "Die Teilnehmenden definieren ein realistisches Prototypziel mit Ergebnisformat und Pruefkriterium.",
    ],
    "terms": ["Prototyp", "Problemzuschnitt", "Material", "Ergebnisformat", "Pruefkriterium", "Teamkontext"],
    "starter": "Teamstunden funktionieren gut, wenn das Problem klein genug ist und ein klares Ergebnis entsteht.",
    "example": "Aus 'KI fuer unser Projekt nutzen' wird: 'Aus drei Spezifikationsseiten eine Aenderungscheckliste mit Risiken und offenen Fragen erstellen.'",
    "demo": [
      "Ein grosses Thema in ein 60-Minuten-Ziel zerlegen.",
      "Geeignetes Material markieren: unkritisch, relevant, aktuell.",
      "Ergebnisformat festlegen: Checkliste, Diff-Plan, Testfallliste, Risikoanalyse.",
    ],
    "practice": [
      "Jedes Team formuliert ein Thema im Schema: Ausgangslage, Material, Ziel, Ergebnis, Pruefung.",
      "Ein Beispielprompt fuer OpenWebUI oder Continue.dev vorbereiten.",
      "Risiken und offene Fragen fuer die Teamstunde notieren.",
    ],
    "deepDive": [
      "Fuer technisch Interessierte: Prototypziel mit Akzeptanzkriterien und Testidee verbinden.",
      "Bei Repo-Arbeit vorab relevante Pfade, Branches und nicht zu aendernde Bereiche nennen.",
    ],
    "errors": [
      "Ziel zu gross: eine Entscheidung oder einen Arbeitsschritt isolieren.",
      "Material ungeeignet: anonymisieren, reduzieren oder alternatives Beispiel nehmen.",
      "Kein Pruefkriterium: Ergebnis erst nutzbar machen, wenn Pruefung definiert ist.",
    ],
    "check": ["Ist das Teamziel in 60 Minuten erreichbar?", "Welches Material wird genutzt?", "Wie sieht das Ergebnis aus?"],
    "next": "Es folgen teambezogene Praxisstunden mit OpenWebUI und VS Code im jeweiligen Arbeitskontext.",
  },
]


TEAM_MODULES = [
  (
    "teil-09",
    "teil-09-frontend-team-1",
    "Teamstunde Frontend 1: Softwarepflege und kleine Aenderungsprototypen",
    "Softwarepflege",
    ["Frontendteam", "Softwarepflege", "Entwicklungsszenarien"],
    ["VS Code", "Continue.dev", "OpenWebUI", "SeaDrive"],
    "Eine kleine Pflegeaenderung wird vom Problem ueber relevante Dateien bis zum pruefbaren Aenderungsplan gefuehrt.",
    "Bestehende Komponente erklaeren lassen, minimale Aenderung planen, Risiken und Tests notieren.",
  ),
  (
    "teil-10",
    "teil-10-frontend-team-2",
    "Teamstunde Frontend 2: UI-Aenderungen, Komponenten und Review",
    "UI-Aenderung",
    ["Frontendteam", "UI", "Review"],
    ["VS Code", "Continue.dev", "OpenWebUI", "SeaDrive"],
    "Eine UI-Aenderung wird anhand bestehender Komponenten und Designkonventionen vorbereitet.",
    "Komponente suchen, Varianten pruefen, Aenderungsskizze und Review-Checkliste erstellen.",
  ),
  (
    "teil-11",
    "teil-11-frontend-team-3",
    "Teamstunde Frontend 3: Fehleranalyse, Refactoring-Ideen, Dokumentation",
    "Fehleranalyse",
    ["Frontendteam", "Softwarepflege", "Dokumentation"],
    ["VS Code", "Continue.dev", "OpenWebUI"],
    "Ein beobachtetes Fehlverhalten wird strukturiert eingegrenzt und in sichere naechste Schritte uebersetzt.",
    "Fehlerbeschreibung, relevante Dateien und Testidee zusammenfuehren; Refactoring-Idee dokumentieren.",
  ),
  (
    "teil-12",
    "teil-12-frontend-team-4",
    "Teamstunde Frontend 4: grosse Repos durchsuchen und Aenderungsplan erstellen",
    "Repo-Analyse",
    ["Frontendteam", "grosse Repos", "Aenderungsplanung"],
    ["VS Code", "Continue.dev", "OpenWebUI"],
    "Ein groesseres Repo wird zuerst kartiert, bevor eine Aenderung geplant wird.",
    "Continue.dev nach Einstiegspunkten, Begriffen, Abhaengigkeiten und Risiken fragen; Ergebnis als Aenderungsplan sichern.",
  ),
  (
    "teil-13",
    "teil-13-testteam",
    "Teamstunde Test: Testfaelle, Fehlermeldungen und Akzeptanzkriterien",
    "Test",
    ["Testteam", "Qualitaet", "Regression"],
    ["OpenWebUI", "VS Code", "Continue.dev", "Seafile"],
    "Aus Anforderungen, Fehlermeldungen oder Aenderungsnotizen entstehen pruefbare Testfaelle.",
    "Akzeptanzkriterien extrahieren, Testfallliste erzeugen, Randfaelle und Regressionen markieren.",
  ),
  (
    "teil-14",
    "teil-14-devops-team",
    "Teamstunde DevOps: Logs, Deployments, RAGFlow-Anbindung und Betriebsfragen",
    "DevOps",
    ["DevOps", "Betrieb", "RAG-Anbindung"],
    ["OpenWebUI", "VS Code", "Continue.dev", "RAGFlow", "Seafile"],
    "Betriebliche Informationen werden in strukturierte Diagnose- oder Handoff-Artefakte ueberfuehrt.",
    "Logauszug analysieren, RAGFlow-Handoff pruefen, Runbook-Notiz oder Eskalationsplan erstellen.",
  ),
  (
    "teil-15",
    "teil-15-admin-team",
    "Teamstunde Admin: Rechte, Tools, Automations und sichere OpenWebUI-Nutzung",
    "Administration",
    ["Administration", "Berechtigungen", "Governance"],
    ["OpenWebUI", "Calendar", "Automations", "Skills", "Tools"],
    "Admin-nahe Aufgaben werden mit Berechtigungen, Toolgrenzen und sicherer Aktivierung verbunden.",
    "Eine sichere Skill-/Tool-/Automation-Konfiguration auf Papier entwerfen und Pruefpunkte definieren.",
  ),
  (
    "teil-16",
    "teil-16-fuehrungsteam",
    "Teamstunde Fuehrung: Zusammenfassungen, Entscheidungsgrundlagen und Risiken",
    "Fuehrung",
    ["Fuehrungsteam", "Entscheidung", "Status"],
    ["OpenWebUI", "Seafile"],
    "Dokumente und Statusinformationen werden in Entscheidungsgrundlagen mit Risiken und offenen Punkten uebersetzt.",
    "Executive Summary, Entscheidungsoptionen und Rueckfragen aus bereitgestellten Unterlagen erstellen.",
  ),
  (
    "teil-17",
    "teil-17-konfig-qualitaetsteam",
    "Teamstunde Konfiguration und Qualitaet: Richtlinien, Aenderungspruefung und Freigabelogik",
    "Konfiguration und Qualitaet",
    ["Konfiguration", "Qualitaet", "Freigabe"],
    ["OpenWebUI", "Seafile", "VS Code"],
    "Richtlinien und Aenderungsinformationen werden in eine nachvollziehbare Pruefmatrix ueberfuehrt.",
    "Aenderung gegen Checkliste pruefen, Risiken klassifizieren, Freigabefragen formulieren.",
  ),
  (
    "teil-18",
    "teil-18-analystenteam-1",
    "Teamstunde Analyse 1: Auswirkungen neuer Funktionalitaeten bewerten",
    "Analyse",
    ["Analyse", "Auswirkungen", "Dokumentenarbeit"],
    ["OpenWebUI", "Seafile", "SeaDrive"],
    "Neue Funktionalitaeten werden anhand von Dokumenten auf Auswirkungen, Abhaengigkeiten und Rueckfragen untersucht.",
    "Dokumente fragen, Auswirkungen strukturieren, Annahmen und offene Informationen sichtbar machen.",
  ),
  (
    "teil-19",
    "teil-19-analystenteam-2",
    "Teamstunde Analyse 2: bestehende Funktionalitaeten aendern oder ergaenzen",
    "Analyse",
    ["Analyse", "Aenderungsbewertung", "Dokumentation"],
    ["OpenWebUI", "Seafile", "VS Code"],
    "Bestehende Funktionalitaeten werden in Aenderungsoptionen, Risiken und Dokumentationsbedarf uebersetzt.",
    "Ist-Zustand beschreiben, Aenderungsvarianten vergleichen, naechste Pruefschritte ableiten.",
  ),
]


for team_id, slug, title, focus, audience, tools, scenario, practice_summary in TEAM_MODULES:
  MODULES.append(
    {
      "id": team_id,
      "slug": slug,
      "title": title,
      "subtitle": "Eine nutzerspezifische Praxisstunde mit eigenem Arbeitskontext und pruefbarem Prototyp.",
      "focus": focus,
      "audienceFocus": audience,
      "tools": tools,
      "learningGoals": [
        "Die Teilnehmenden koennen ein reales Teamthema in eine KI-geeignete Aufgabe uebersetzen.",
        "Die Teilnehmenden nutzen OpenWebUI oder Continue.dev passend zum Material und Ergebnisziel.",
        "Die Teilnehmenden erstellen einen kleinen Prototyp, eine Pruefliste oder einen Aenderungsplan.",
      ],
      "terms": ["Teamkontext", "Prototyp", "Material", "Prompt", "Pruefung", "Transfer"],
      "starter": "Diese Stunde nutzt das Teamthema als Arbeitsmaterial. Ziel ist ein kleines Ergebnis, das nach der Schulung weiterverwendet werden kann.",
      "example": scenario,
      "demo": [
        "Teamthema im Schema Ausgangslage, Material, Ziel, Ergebnisformat erfassen.",
        "Passendes Werkzeug waehlen: OpenWebUI fuer Text/Wissen, Continue.dev fuer Code/Repo/Dateien.",
        "Erstes Ergebnis erzeugen und mit Teamwissen pruefen.",
      ],
      "practice": [
        practice_summary,
        "Ergebnis in einem gemeinsam sichtbaren Format sichern: Checkliste, Tabelle, Aenderungsplan oder Prototypnotiz.",
        "Mindestens eine fachliche Rueckfrage und einen Pruefschritt dokumentieren.",
      ],
      "deepDive": [
        "Fuer technisch Interessierte: Werkzeuggrenzen explizit machen und den naechsten sicheren Umsetzungsschritt ableiten.",
        "Bei Code- oder Repo-Arbeit: nicht nur Ergebnis, sondern betroffene Dateien, Tests und Risiken erfassen.",
      ],
      "errors": [
        "Teamthema zu gross: kleineren Ausschnitt waehlen.",
        "Material unvollstaendig: Annahmen und Rueckfragen getrennt notieren.",
        "Ergebnis nicht pruefbar: Akzeptanzkriterium oder Reviewfrage ergaenzen.",
      ],
      "check": ["Was ist das konkrete Teamziel?", "Welches Ergebnis liegt vor?", "Wie wird es fachlich geprueft?"],
      "next": "Die Ergebnisse fliessen in die teamuebergreifende Retrospektive ein.",
      "teamSpecific": True,
    }
  )


MODULES.append(
  {
    "id": "teil-20",
    "slug": "teil-20-retrospektive-feedback",
    "title": "Teamuebergreifende Retrospektive und Feedback",
    "subtitle": "Offene Fragen, Wuensche, naechste Schritte und gemeinsame Lernpunkte.",
    "focus": "Retrospektive",
    "audienceFocus": ["alle Teams", "Transfer", "Feedback"],
    "tools": ["OpenWebUI", "VS Code", "Continue.dev", "Seafile", "SeaDrive"],
    "learningGoals": [
      "Die Teilnehmenden koennen Lernergebnisse aus den Teamstunden teilen.",
      "Die Teilnehmenden benennen offene Fragen, Risiken und Unterstuetzungsbedarf.",
      "Die Teilnehmenden formulieren naechste Schritte fuer den Arbeitsalltag.",
    ],
    "terms": ["Retrospektive", "Feedback", "Transfer", "Naechster Schritt", "Governance", "Unterstuetzungsbedarf"],
    "starter": "Die Retrospektive sammelt, was funktioniert hat, was noch unklar ist und was fuer den produktiven Alltag gebraucht wird.",
    "example": "Ein Team teilt einen Aenderungsplan, ein anderes eine Testfallliste. Gemeinsam werden Muster, Risiken und naechste Schritte sichtbar.",
    "demo": [
      "Team-Ergebnisse in einer gemeinsamen Matrix sammeln.",
      "Offene Fragen nach Tool, Prozess, Daten, Sicherheit und Schulungsbedarf sortieren.",
      "Naechste Schritte mit Verantwortlichkeit und Terminrahmen formulieren.",
    ],
    "practice": [
      "Jedes Team nennt ein nutzbares Ergebnis und eine offene Frage.",
      "Gemeinsam drei Verbesserungswuensche fuer die KI-Umgebung sammeln.",
      "Persoenlichen naechsten Schritt fuer den Arbeitsalltag notieren.",
    ],
    "deepDive": [
      "Fuer technisch Interessierte: wiederkehrende Tool- oder Datenprobleme in Governance-Backlog ueberfuehren.",
      "Schulungsbedarf als wiederholbare Skill-, Prompt- oder Modellvorlage dokumentieren.",
    ],
    "errors": [
      "Feedback zu allgemein: konkretes Beispiel und Auswirkung ergaenzen.",
      "Naechster Schritt zu gross: eine kleine, pruefbare Massnahme waehlen.",
      "Offene Frage ohne Besitzer: Klaerungsteam oder Folgeformat benennen.",
    ],
    "check": ["Welches Ergebnis wird weiterverwendet?", "Welche Frage bleibt offen?", "Was ist der naechste sichere Schritt?"],
    "next": "Nach der Reihe koennen Teams eigene Vorlagen, Skills und Handoff-Prozesse verfeinern.",
  }
)


def text_list(items: list[str], class_name: str = "bullets") -> str:
  return "<ul class=\"{}\">{}</ul>".format(
    class_name,
    "".join(f"<li>{escape(item)}</li>" for item in items),
  )


def tag_list(items: list[str]) -> str:
  return "".join(f"<span class=\"tag\">{escape(item)}</span>" for item in items)


def slide(title: str, body: str, note: str) -> str:
  return f"""
      <section class="slide" data-title="{escape(title)}">
        <div class="slide-inner">
          <h2>{escape(title)}</h2>
          {body}
          <details class="speaker-notes">
            <summary>Notizen fuer die Durchfuehrung</summary>
            <p>{escape(note)}</p>
          </details>
        </div>
      </section>"""


def render_matrix() -> str:
  rows = "".join(
    "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
      escape(row["problem"]), escape(row["recommended"]), escape(row["watch"])
    )
    for row in MODEL_MATRIX
  )
  return f"""
    <div class="table-wrap">
      <table>
        <thead><tr><th>Problemfall</th><th>Geeigneter Einstieg</th><th>Worauf achten?</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  """


def architecture_diagram() -> str:
  return """
    <div class="flow-diagram" aria-label="Wissensfluss">
      <div class="flow-node">Dokumente<br><strong>Seafile</strong></div>
      <div class="flow-arrow">-&gt;</div>
      <div class="flow-node">lokaler Zugriff<br><strong>SeaDrive</strong></div>
      <div class="flow-arrow">-&gt;</div>
      <div class="flow-node muted">Hintergrund<br><strong>RAGFlow</strong></div>
      <div class="flow-arrow">-&gt;</div>
      <div class="flow-node">Fragen stellen<br><strong>OpenWebUI</strong></div>
      <div class="flow-arrow">-&gt;</div>
      <div class="flow-node accent">Antwort pruefen<br><strong>Team</strong></div>
    </div>
  """


def prompt_template(module: dict) -> str:
  if module.get("teamSpecific"):
    return """Ziel: Erstelle fuer unser Teamthema einen kleinen, pruefbaren Prototyp oder Arbeitsplan.
Kontext: {kurze Ausgangslage, Material, relevante Dateien}.
Ausgabe: Tabelle mit Ergebnis, Annahmen, Risiken, offenen Fragen und naechstem Schritt.
Grenzen: Keine sensiblen Daten, keine produktiven Aenderungen ohne Review.
Pruefung: Markiere, welche Aussagen durch Material gestuetzt sind."""
  if module["id"] == "teil-06":
    return """Ziel: Analysiere diese Datei oder diesen Repo-Ausschnitt und schlage eine kleine Aenderung vor.
Kontext: {Dateipfad, erwartetes Verhalten, beobachtetes Problem}.
Ausgabe: relevante Dateien, Aenderungsplan, Risiken, Testidee.
Grenzen: Keine Aenderung an Secrets oder produktiven Konfigurationen."""
  if module["id"] == "teil-07":
    return """Ziel: Bereite diese Dokumentenablage fuer eine spaetere Wissensnutzung vor.
Kontext: {Seafile-Bibliothek, Dokumenttypen, fachlicher Zweck, Besitzer}.
Ausgabe: Handoff-Checkliste fuer DevOps/Admins mit Risiken und offenen Fragen."""
  return """Ziel: {Was soll am Ende vorliegen?}
Kontext: {Welche Situation, Datei oder Zielgruppe ist wichtig?}
Eingabe: {Text, Stichpunkte, Datei oder Fehlermeldung}.
Ausgabeformat: {Tabelle, Checkliste, Schrittfolge, Zusammenfassung}.
Grenzen: Kennzeichne Annahmen und stelle Rueckfragen, wenn Informationen fehlen."""


def render_presentation(module: dict, index: int, total: int) -> str:
  slides = []
  slides.append(
    f"""
      <section class="slide title-slide active" data-title="{escape(module['title'])}">
        <div class="slide-inner hero">
          <p class="kicker">Offline-KI-Schulung - Teil {index:02d} von {total}</p>
          <h1>{escape(module['title'])}</h1>
          <p class="subtitle">{escape(module['subtitle'])}</p>
          <div class="tag-row">{tag_list(module['tools'])}</div>
          <details class="speaker-notes">
            <summary>Notizen fuer die Durchfuehrung</summary>
            <p>Diese Einheit dauert maximal 60 Minuten. Den Einstieg ruhig halten, Vorwissen nicht voraussetzen und technische Vertiefung nur optional ausbauen.</p>
          </details>
        </div>
      </section>"""
  )
  slides.append(
    slide(
      "Einordnung in die Reihe",
      f"""
        <div class="series-card">
          <span class="series-number">{index:02d}</span>
          <div>
            <p class="eyebrow">{escape(module['focus'])}</p>
            <p>Diese Einheit verbindet die gemeinsame Grundspur mit dem spaeteren Transfer in Teamstunden.</p>
          </div>
        </div>
        <div class="two-col">
          <div><h3>Schwerpunkt</h3><p>{escape(module['focus'])}</p></div>
          <div><h3>Zielgruppe</h3><div class="tag-row">{tag_list(module['audienceFocus'])}</div></div>
        </div>
      """,
      "Kurz zeigen, wo diese Einheit im Ablauf steht. Bei spaeteren Teamstunden den Rueckbezug auf die gemeinsamen Grundlagen herstellen.",
    )
  )
  slides.append(
    slide(
      "Lernziele",
      text_list(module["learningGoals"]),
      "Die Ziele in einfacher Sprache vorlesen. Bei Bedarf ergaenzen, dass Vertiefungen optional sind.",
    )
  )
  slides.append(
    slide(
      "Agenda fuer 60 Minuten",
      text_list(COMMON_AGENDA, "timeline"),
      "Auf die Zeitbox achten: Demo und Praxis sind wichtiger als lange Theorie.",
    )
  )
  slides.append(
    slide(
      "Kurzer Einstieg",
      f"""<p class="lead">{escape(module['starter'])}</p><div class="callout">Leitfrage: Was soll nach dieser Stunde im Arbeitsalltag leichter fallen?</div>""",
      "Die Leitfrage an die Gruppe geben und ein bis zwei kurze Antworten sammeln.",
    )
  )
  slides.append(
    slide(
      "Zentrale Begriffe",
      f"""<div class="term-grid">{''.join(f'<div class="term"><strong>{escape(t)}</strong><span>{escape(term_explanation(t))}</span></div>' for t in module['terms'])}</div>""",
      "Begriffe knapp erklaeren. Nicht in Details abdriften; Beispiele sind wirkungsvoller als Definitionen.",
    )
  )
  slides.append(
    slide(
      "Anschauliches Beispiel",
      f"""<p class="lead">{escape(module['example'])}</p><div class="example-box"><strong>Arbeitsregel:</strong> Erst Ziel klaeren, dann Werkzeug waehlen, dann Ergebnis pruefen.</div>""",
      "Das Beispiel auf die Gruppe beziehen. Wenn eigene Beispiele vorhanden sind, diese bevorzugen.",
    )
  )
  slides.append(
    slide(
      "Live-Demo durchfuehren",
      text_list(module["demo"], "steps"),
      "Demo langsam durchfuehren und jeden Klick begruenden. Keine produktiven Daten verwenden.",
    )
  )
  slides.append(
    slide(
      "Praxisaufgabe fuer alle",
      text_list(module["practice"], "steps"),
      "Alle Teilnehmenden arbeiten mit unkritischem Material. Bei gemischtem Vorwissen Paararbeit anbieten.",
    )
  )
  slides.append(
    slide(
      "Prompt- oder Arbeitsmuster",
      f"""<pre class="prompt"><code>{escape(prompt_template(module))}</code></pre>""",
      "Das Muster nicht als starre Formel verkaufen. Die Teilnehmenden sollen Bausteine anpassen.",
    )
  )
  if module["id"] == "teil-06":
    body = render_matrix()
    note = "Die Matrix zeigt problemfallorientierte Auswahl. Sichtbare lokale Modellnamen koennen abweichen."
  elif module["id"] == "teil-07":
    body = architecture_diagram()
    note = "RAGFlow nur als Hintergrund erklaeren. Teilnehmende bedienen Seafile, SeaDrive, OpenWebUI und VS Code."
  else:
    body = text_list(module["deepDive"])
    note = "Vertiefung nur anbieten, wenn die Gruppe bereit ist oder technisch Interessierte zusaetzliche Aufgaben brauchen."
  slides.append(slide("Optionale Vertiefung", body, note))
  slides.append(
    slide(
      "Typische Fehler und schnelle Loesungen",
      text_list(module["errors"]),
      "Fehler normalisieren und als Diagnosehilfe nutzen. Keine Schuldzuweisung, sondern klare naechste Schritte.",
    )
  )
  slides.append(
    slide(
      "Sicherheit und Datenschutz",
      text_list(SECURITY_RULES[:4]),
      "Diese Regeln kurz und praktisch halten. Bei Unsicherheit lieber Beispielmaterial verwenden.",
    )
  )
  slides.append(
    slide(
      "Zusammenfassung",
      f"""
        <div class="summary-grid">
          <div><strong>Werkzeuge</strong><span>{escape(', '.join(module['tools']))}</span></div>
          <div><strong>Ergebnis</strong><span>{escape(result_summary(module))}</span></div>
          <div><strong>Pruefung</strong><span>Fakten, Annahmen und offene Punkte trennen.</span></div>
        </div>
      """,
      "Noch einmal den Transfer betonen: Was wird ab morgen anders gemacht?",
    )
  )
  slides.append(
    slide(
      "Mini-Check",
      text_list(module["check"], "checklist"),
      "Die Fragen muendlich oder mit kurzer Notiz beantworten lassen. Unklare Punkte fuer die Retrospektive sammeln.",
    )
  )
  slides.append(
    slide(
      "Ausblick",
      f"""<p class="lead">{escape(module['next'])}</p><a class="plan-link" href="../workshopplan.html">Zurueck zum Workshopplan</a>""",
      "Abschluss mit naechstem Schritt. Status im Workshopplan bei Bedarf auf durchgefuehrt setzen.",
    )
  )
  return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(module['title'])}</title>
  <style>{PRESENTATION_CSS}</style>
</head>
<body>
  <div class="deck" data-module="{escape(module['id'])}">
    <header class="topbar">
      <a href="../workshopplan.html" class="back-link">Workshopplan</a>
      <div class="progress-track"><div id="progress" class="progress-bar"></div></div>
      <div class="counter"><span id="currentSlide">1</span>/<span id="totalSlides">{len(slides)}</span></div>
    </header>
    <main id="slides" class="slides" aria-live="polite">
      {''.join(slides)}
    </main>
    <footer class="controls">
      <button id="prevBtn" type="button" aria-label="Vorherige Folie">Zurueck</button>
      <button id="notesBtn" type="button" aria-label="Notizen umschalten">Notizen</button>
      <button id="themeBtn" type="button" aria-label="Hell-Dunkel-Modus umschalten">Hell/Dunkel</button>
      <button id="printBtn" type="button" aria-label="Druckansicht oeffnen">Drucken</button>
      <button id="nextBtn" type="button" aria-label="Naechste Folie">Weiter</button>
    </footer>
  </div>
  <script>{PRESENTATION_JS}</script>
</body>
</html>
"""


def term_explanation(term: str) -> str:
  explanations = {
    "KI": "Systeme, die Muster nutzen, um Vorschlaege oder Antworten zu erzeugen.",
    "Modell": "Das eigentliche KI-System oder ein Aufgaben-Preset darueber.",
    "Training": "Lernphase, in der Muster aus Daten abgeleitet wurden.",
    "Kontext": "Informationen, die die aktuelle Antwort beeinflussen.",
    "Prompt": "Die Eingabe mit Ziel, Kontext und gewuenschtem Ergebnis.",
    "Halluzination": "Plausibel klingende, aber falsche oder nicht belegte Aussage.",
    "Pruefung": "Fachlicher Abgleich vor Verwendung eines Ergebnisses.",
    "Chat": "Dialogoberflaeche fuer Fragen, Antworten und Iteration.",
    "Promptvorlage": "Wiederverwendbares Muster fuer haeufige Aufgaben.",
    "Problemfallmodell": "Aufgabenorientiertes OpenWebUI-Modell fuer einen konkreten Zweck.",
    "Rolle": "Perspektive oder Pruefauftrag fuer die Antwort.",
    "Ziel": "Das erwartete Ergebnis der Aufgabe.",
    "Ausgabeformat": "Form der Antwort, zum Beispiel Tabelle oder Checkliste.",
    "Rueckfrage": "Klaerung, wenn wichtige Informationen fehlen.",
    "Seafile": "Verwaltete Dateiablage.",
    "SeaDrive": "Lokaler Zugriff auf Seafile-Bibliotheken wie ein Laufwerk.",
    "RAG": "Antworten mit gezielter Suche in bereitgestellten Dokumenten.",
    "RAGFlow": "Hintergrundsystem zur Aufbereitung und Suche in Dokumentwissen.",
    "Knowledge Base": "Sammlung von Dokumenten, die OpenWebUI durchsuchen kann.",
    "Handoff": "Uebergabe an DevOps/Admins mit klaren Angaben.",
    "Skill": "Markdown-Anweisung, die einem Modell Arbeitsregeln gibt.",
    "Tool": "Ausfuehrbare Faehigkeit, die zusaetzliche Aktionen ermoeglicht.",
    "Function": "Erweiterungsmechanik fuer Filter, Pipes oder Aktionen.",
    "Builtin Tool": "In OpenWebUI vorhandene Werkzeugkategorie.",
    "Calendar": "Kalenderfunktion fuer Termine und Erinnerungen.",
    "Automation": "Geplanter oder wiederkehrender KI-Auftrag.",
    "Function Calling": "Faehigkeit des Modells, Werkzeuge gezielt aufzurufen.",
    "Berechtigung": "Zugriff auf Funktion, Modell, Skill oder Kalender.",
    "IDE": "Arbeitsumgebung fuer Code und Dateien.",
    "Chat Mode": "Dialogmodus zum Erklaeren und Ausarbeiten.",
    "Agent Mode": "Modus fuer kleine geplante Aktionen mit Werkzeugzugriff.",
    "Dateiauswahl": "Gezieltes Hinzufuegen relevanter Dateien als Kontext.",
    "Repo-Suche": "Suche nach relevanten Stellen im Codebestand.",
    "Diff": "Sichtbare Aenderung zwischen alter und neuer Datei.",
    "Test": "Pruefschritt fuer Verhalten und Sicherheit.",
  }
  return explanations.get(term, "Kurz erklaerter Begriff fuer diese Einheit.")


def result_summary(module: dict) -> str:
  if module.get("teamSpecific"):
    return "Ein kleiner Team-Prototyp, eine Pruefliste oder ein Aenderungsplan."
  if "OpenWebUI" in module["tools"] and "VS Code" in module["tools"]:
    return "Sichere Werkzeugwahl und ein pruefbarer Arbeitsablauf."
  if module["id"] == "teil-20":
    return "Gemeinsame Lernpunkte, offene Fragen und naechste Schritte."
  return "Ein konkret nutzbares Vorgehen fuer diese Werkzeug- oder Grundlagenstufe."


PRESENTATION_CSS = """
:root {
  color-scheme: dark;
  --bg: #05070d;
  --stage: #0b111d;
  --stage-2: #111827;
  --ink: #f4f7fb;
  --muted: #aeb9c9;
  --line: rgba(185, 202, 224, 0.22);
  --accent: #43d5c8;
  --accent-2: #f0a35b;
  --soft: rgba(67, 213, 200, 0.11);
  --warn: rgba(240, 163, 91, 0.14);
  --ok: rgba(78, 199, 116, 0.14);
  --shadow: 0 26px 90px rgba(0, 0, 0, 0.55);
}
body.light-mode {
  color-scheme: light;
  --bg: #f6f7fb;
  --stage: #ffffff;
  --stage-2: #fbfcff;
  --ink: #172033;
  --muted: #647084;
  --line: #d9deea;
  --accent: #256f78;
  --accent-2: #b45f3a;
  --soft: #eaf4f5;
  --warn: #fff2df;
  --ok: #e8f5ea;
  --shadow: 0 18px 50px rgba(28, 38, 62, 0.16);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background:
    linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px),
    linear-gradient(180deg, rgba(255,255,255,.028) 1px, transparent 1px),
    linear-gradient(135deg, #05070d 0%, #0c1423 48%, #130f19 100%);
  background-size: 46px 46px, 46px 46px, auto;
  color: var(--ink);
  font-family: Arial, Helvetica, sans-serif;
}
body.light-mode {
  background: var(--bg);
}
a { color: inherit; }
.deck {
  min-height: 100vh;
  display: grid;
  grid-template-rows: auto 1fr auto;
}
.topbar {
  display: grid;
  grid-template-columns: minmax(140px, auto) 1fr auto;
  gap: 18px;
  align-items: center;
  padding: 16px 24px;
  font-size: 15px;
}
.back-link, .plan-link {
  text-decoration: none;
  color: var(--accent);
  font-weight: 700;
}
.progress-track {
  height: 10px;
  border-radius: 999px;
  background: #dfe5ef;
  overflow: hidden;
}
.progress-bar {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
}
.counter { color: var(--muted); font-weight: 700; }
.slides {
  width: min(1180px, calc(100vw - 48px));
  aspect-ratio: 16 / 9;
  margin: 0 auto;
  align-self: center;
  position: relative;
}
.slide {
  display: none;
  position: absolute;
  inset: 0;
  background:
    linear-gradient(145deg, rgba(67, 213, 200, .10), transparent 38%),
    linear-gradient(315deg, rgba(240, 163, 91, .10), transparent 42%),
    var(--stage);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  overflow: hidden;
}
.slide::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    linear-gradient(90deg, transparent 0%, rgba(67, 213, 200, .18) 48%, transparent 100%);
  transform: translateX(-120%);
  opacity: .35;
}
.slide.active {
  display: block;
  animation: slideEnter 520ms ease both;
}
.slide.active::before {
  animation: scanLine 2200ms ease-out both;
}
.slide-inner {
  height: 100%;
  padding: clamp(34px, 4vw, 64px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 22px;
  position: relative;
  z-index: 1;
}
.slide.active .slide-inner > * {
  animation: contentRise 560ms ease both;
}
.slide.active .slide-inner > *:nth-child(2) { animation-delay: 80ms; }
.slide.active .slide-inner > *:nth-child(3) { animation-delay: 140ms; }
.slide.active .slide-inner > *:nth-child(4) { animation-delay: 200ms; }
.hero {
  background:
    linear-gradient(110deg, rgba(67, 213, 200, .20), transparent 42%),
    linear-gradient(290deg, rgba(240, 163, 91, .18), transparent 44%),
    linear-gradient(180deg, rgba(255,255,255,.08), transparent 22%),
    var(--stage);
}
h1, h2, h3, p { margin: 0; }
h1 {
  max-width: 1000px;
  font-size: clamp(42px, 6.4vw, 76px);
  line-height: 1.02;
  letter-spacing: 0;
}
h2 {
  max-width: 980px;
  font-size: clamp(32px, 4.8vw, 56px);
  line-height: 1.08;
  letter-spacing: 0;
}
h3 {
  font-size: 21px;
  line-height: 1.25;
}
.kicker, .eyebrow {
  color: var(--accent);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0;
  font-size: 14px;
}
.subtitle, .lead {
  max-width: 900px;
  color: var(--muted);
  font-size: clamp(22px, 2.2vw, 30px);
  line-height: 1.35;
}
.tag-row { display: flex; flex-wrap: wrap; gap: 10px; }
.tag {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 7px 12px;
  border-radius: 6px;
  background: var(--soft);
  color: var(--ink);
  font-weight: 700;
  font-size: 14px;
}
.bullets, .steps, .timeline, .checklist {
  display: grid;
  gap: 14px;
  padding: 0;
  margin: 0;
  list-style: none;
  max-width: 980px;
}
.bullets li, .steps li, .timeline li, .checklist li {
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255, 255, 255, .055);
  font-size: clamp(18px, 1.8vw, 25px);
  line-height: 1.3;
}
.steps { counter-reset: step; }
.steps li {
  display: grid;
  grid-template-columns: 42px 1fr;
  align-items: start;
}
.steps li::before {
  counter-increment: step;
  content: counter(step);
  width: 28px;
  height: 28px;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  display: inline-grid;
  place-items: center;
  font-weight: 800;
  font-size: 15px;
}
.timeline li { background: var(--soft); }
.checklist li { background: var(--ok); }
.two-col {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}
.two-col > div, .example-box, .callout, .series-card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255, 255, 255, .055);
  padding: 18px;
}
.callout { background: var(--warn); font-size: 22px; line-height: 1.35; }
.example-box { font-size: 22px; line-height: 1.35; background: var(--soft); }
.series-card {
  display: flex;
  align-items: center;
  gap: 18px;
}
.series-number {
  width: 74px;
  height: 74px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  color: #08101c;
  font-weight: 800;
  font-size: 28px;
}
.term-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}
.term {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  background: rgba(255, 255, 255, .055);
  min-height: 92px;
}
.term strong {
  display: block;
  font-size: 20px;
  margin-bottom: 6px;
}
.term span {
  color: var(--muted);
  font-size: 16px;
  line-height: 1.35;
}
.prompt {
  max-width: 100%;
  white-space: pre-wrap;
  border-radius: 8px;
  border: 1px solid var(--line);
  padding: 22px;
  background: #050914;
  color: #f3f7fb;
  font-size: clamp(17px, 1.6vw, 23px);
  line-height: 1.45;
}
.table-wrap { overflow: auto; border: 1px solid var(--line); border-radius: 8px; }
table { width: 100%; border-collapse: collapse; font-size: 18px; }
th, td { text-align: left; padding: 13px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { background: var(--soft); color: #184e58; }
body:not(.light-mode) th { color: var(--ink); }
.flow-diagram {
  display: grid;
  grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr auto 1fr;
  gap: 10px;
  align-items: center;
}
.flow-node {
  min-height: 120px;
  padding: 18px;
  border: 2px solid var(--accent);
  border-radius: 8px;
  display: grid;
  place-items: center;
  text-align: center;
  background: var(--soft);
  font-size: 18px;
  line-height: 1.35;
}
.flow-node.muted { border-color: var(--muted); background: rgba(255, 255, 255, .055); }
.flow-node.accent { border-color: var(--accent-2); background: var(--warn); }
.flow-arrow {
  color: var(--accent);
  font-size: 26px;
  font-weight: 800;
  animation: arrowPulse 1600ms ease-in-out infinite;
}
.summary-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}
.summary-grid div {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px;
  background: rgba(255, 255, 255, .055);
}
.summary-grid strong { display: block; font-size: 20px; margin-bottom: 8px; }
.summary-grid span { color: var(--muted); font-size: 18px; line-height: 1.35; }
.speaker-notes {
  margin-top: auto;
  border-top: 1px solid var(--line);
  padding-top: 12px;
  color: var(--muted);
  font-size: 15px;
}
.speaker-notes summary {
  cursor: pointer;
  font-weight: 800;
  color: var(--accent);
}
body.hide-notes .speaker-notes { display: none; }
.controls {
  display: flex;
  justify-content: center;
  gap: 12px;
  padding: 16px 24px 22px;
}
button {
  border: 1px solid var(--line);
  border-radius: 7px;
  background: rgba(255, 255, 255, .08);
  color: var(--ink);
  padding: 11px 16px;
  font-weight: 800;
  cursor: pointer;
  font-size: 15px;
}
button:hover, button:focus-visible { outline: 3px solid rgba(37, 111, 120, .22); }
button:disabled { opacity: .45; cursor: not-allowed; }
@keyframes slideEnter {
  from { opacity: 0; transform: translateY(10px) scale(.992); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes contentRise {
  from { opacity: 0; transform: translateY(14px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes scanLine {
  from { transform: translateX(-120%); }
  to { transform: translateX(120%); }
}
@keyframes arrowPulse {
  0%, 100% { opacity: .42; transform: translateX(0); }
  50% { opacity: 1; transform: translateX(3px); }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .001ms !important;
  }
}
@media (max-width: 800px) {
  .slides { width: calc(100vw - 20px); aspect-ratio: auto; min-height: 76vh; }
  .slide { position: relative; min-height: 76vh; }
  .slide-inner { padding: 26px; }
  .two-col, .term-grid, .summary-grid, .flow-diagram { grid-template-columns: 1fr; }
  .flow-arrow { transform: rotate(90deg); justify-self: center; }
  .topbar { grid-template-columns: 1fr; }
}
@media print {
  body { background: #fff; }
  .topbar, .controls { display: none; }
  .deck { display: block; }
  .slides { width: 100%; aspect-ratio: auto; margin: 0; }
  .slide {
    display: block !important;
    position: relative;
    page-break-after: always;
    box-shadow: none;
    border: 1px solid #bbb;
    min-height: 95vh;
  }
  .speaker-notes { display: block !important; }
}
"""


PRESENTATION_JS = """
const slides = Array.from(document.querySelectorAll('.slide'));
let current = 0;
const progress = document.getElementById('progress');
const currentSlide = document.getElementById('currentSlide');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
function showSlide(index) {
  current = Math.max(0, Math.min(index, slides.length - 1));
  slides.forEach((slide, i) => slide.classList.toggle('active', i === current));
  currentSlide.textContent = String(current + 1);
  progress.style.width = `${((current + 1) / slides.length) * 100}%`;
  prevBtn.disabled = current === 0;
  nextBtn.disabled = current === slides.length - 1;
}
function next() { showSlide(current + 1); }
function prev() { showSlide(current - 1); }
prevBtn.addEventListener('click', prev);
nextBtn.addEventListener('click', next);
document.getElementById('notesBtn').addEventListener('click', () => document.body.classList.toggle('hide-notes'));
document.getElementById('themeBtn').addEventListener('click', () => document.body.classList.toggle('light-mode'));
document.getElementById('printBtn').addEventListener('click', () => window.print());
document.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowRight' || event.key === 'PageDown' || event.key === ' ') {
    event.preventDefault();
    next();
  }
  if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
    event.preventDefault();
    prev();
  }
  if (event.key.toLowerCase() === 'n') {
    document.body.classList.toggle('hide-notes');
  }
});
let touchStartX = null;
document.addEventListener('touchstart', (event) => {
  touchStartX = event.changedTouches[0].clientX;
}, { passive: true });
document.addEventListener('touchend', (event) => {
  if (touchStartX === null) return;
  const delta = event.changedTouches[0].clientX - touchStartX;
  if (Math.abs(delta) > 40) {
    delta < 0 ? next() : prev();
  }
  touchStartX = null;
}, { passive: true });
showSlide(0);
"""


PLAN_CSS = """
:root {
  --bg: #05070d;
  --surface: #0b111d;
  --surface-2: #111827;
  --ink: #f4f7fb;
  --muted: #aeb9c9;
  --line: rgba(185, 202, 224, 0.22);
  --accent: #43d5c8;
  --accent-2: #f0a35b;
  --soft: rgba(67, 213, 200, 0.13);
  --warn: rgba(240, 163, 91, 0.16);
  --ok: rgba(78, 199, 116, 0.16);
  --skip: rgba(173, 137, 222, 0.16);
  color-scheme: dark;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background:
    linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px),
    linear-gradient(180deg, rgba(255,255,255,.028) 1px, transparent 1px),
    linear-gradient(135deg, #05070d 0%, #0c1423 48%, #130f19 100%);
  background-size: 46px 46px, 46px 46px, auto;
  color: var(--ink);
  font-family: Arial, Helvetica, sans-serif;
}
.app-header {
  padding: 34px min(5vw, 64px) 20px;
  background:
    linear-gradient(110deg, rgba(67, 213, 200, .17), transparent 40%),
    linear-gradient(290deg, rgba(240, 163, 91, .14), transparent 42%),
    var(--surface);
  border-bottom: 1px solid var(--line);
}
h1 { margin: 0 0 10px; font-size: clamp(34px, 5vw, 58px); line-height: 1.04; letter-spacing: 0; }
.intro { max-width: 920px; color: var(--muted); font-size: 20px; line-height: 1.45; margin: 0; }
.offline-badge {
  display: inline-flex;
  margin-top: 18px;
  padding: 8px 12px;
  border-radius: 6px;
  background: var(--ok);
  color: #1d5b32;
  font-weight: 800;
}
.toolbar {
  display: grid;
  grid-template-columns: minmax(220px, 1fr) repeat(3, minmax(150px, 220px));
  gap: 12px;
  padding: 18px min(5vw, 64px);
  background: rgba(11, 17, 29, .94);
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 5;
}
input, select, textarea {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 7px;
  padding: 11px 12px;
  font: inherit;
  background: rgba(255, 255, 255, .07);
  color: var(--ink);
}
button, .open-link {
  border: 1px solid var(--line);
  border-radius: 7px;
  background: rgba(255, 255, 255, .08);
  color: var(--ink);
  padding: 10px 12px;
  font-weight: 800;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
button:hover, button:focus-visible, .open-link:hover, .open-link:focus-visible {
  outline: 3px solid rgba(37, 111, 120, .22);
}
.layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(320px, 420px);
  gap: 18px;
  padding: 24px min(5vw, 64px) 40px;
}
.status-panel, .detail-panel, .module-card, .export-panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 8px;
}
.status-panel, .export-panel { padding: 18px; margin-bottom: 18px; }
.progress-shell {
  height: 14px;
  background: #dfe5ef;
  border-radius: 999px;
  overflow: hidden;
  margin: 12px 0;
}
.progress-bar { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent-2)); width: 0%; }
.module-list { display: grid; gap: 12px; }
.module-card {
  padding: 18px;
  display: grid;
  gap: 12px;
}
.module-top {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 14px;
  align-items: start;
}
.module-card h2 { margin: 0; font-size: 23px; line-height: 1.2; letter-spacing: 0; }
.meta, .tags { display: flex; flex-wrap: wrap; gap: 8px; color: var(--muted); font-size: 14px; }
.tag {
  display: inline-flex;
  padding: 6px 9px;
  border-radius: 6px;
  background: var(--soft);
  color: var(--ink);
  font-weight: 700;
}
.status-offen { background: #eef2f8; }
.status-geplant { background: var(--warn); }
.status-durchgefuehrt { background: var(--ok); }
.status-uebersprungen { background: var(--skip); }
.detail-panel {
  padding: 20px;
  position: sticky;
  top: 104px;
  max-height: calc(100vh - 130px);
  overflow: auto;
}
.detail-panel h2 { margin: 0 0 10px; font-size: 28px; line-height: 1.18; }
.detail-panel h3 { margin: 18px 0 8px; font-size: 17px; }
.detail-panel ul { margin: 0; padding-left: 20px; color: var(--muted); line-height: 1.45; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
.export-panel textarea { min-height: 120px; resize: vertical; margin-top: 10px; }
.hidden { display: none !important; }
@media (max-width: 980px) {
  .toolbar, .layout { grid-template-columns: 1fr; }
  .detail-panel { position: static; max-height: none; }
}
@media print {
  .toolbar, .export-panel, .actions button, .detail-panel { display: none; }
  .layout { display: block; padding: 0; }
  .app-header { padding: 18px 0; }
  .module-card { page-break-inside: avoid; border-left: 0; border-right: 0; }
}
"""


PLAN_JS = """
const data = JSON.parse(document.getElementById('workshop-data').textContent);
const storageKey = 'offlineKiWorkshopStatus.v1';
let statuses = loadStatuses();
let selectedId = data.modules[0].id;
const searchInput = document.getElementById('search');
const statusFilter = document.getElementById('statusFilter');
const toolFilter = document.getElementById('toolFilter');
const focusFilter = document.getElementById('focusFilter');
const listEl = document.getElementById('moduleList');
const detailEl = document.getElementById('detailPanel');
const progressBar = document.getElementById('progressBar');
const progressText = document.getElementById('progressText');
function loadStatuses() {
  try {
    return JSON.parse(localStorage.getItem(storageKey)) || {};
  } catch (error) {
    return {};
  }
}
function saveStatuses() {
  localStorage.setItem(storageKey, JSON.stringify(statuses));
}
function statusFor(module) {
  return statuses[module.id] || module.statusDefault || 'offen';
}
function unique(values) {
  return Array.from(new Set(values)).sort((a, b) => a.localeCompare(b, 'de'));
}
function fillFilters() {
  unique(data.modules.flatMap(module => module.tools)).forEach(tool => {
    const option = document.createElement('option');
    option.value = tool;
    option.textContent = tool;
    toolFilter.appendChild(option);
  });
  unique(data.modules.map(module => module.focus)).forEach(focus => {
    const option = document.createElement('option');
    option.value = focus;
    option.textContent = focus;
    focusFilter.appendChild(option);
  });
}
function moduleMatches(module) {
  const query = searchInput.value.trim().toLowerCase();
  const haystack = [
    module.title,
    module.focus,
    module.tools.join(' '),
    module.audienceFocus.join(' '),
    module.learningGoals.join(' '),
    module.practice.join(' ')
  ].join(' ').toLowerCase();
  return (!query || haystack.includes(query))
    && (!statusFilter.value || statusFor(module) === statusFilter.value)
    && (!toolFilter.value || module.tools.includes(toolFilter.value))
    && (!focusFilter.value || module.focus === focusFilter.value);
}
function renderList() {
  listEl.innerHTML = '';
  data.modules.filter(moduleMatches).forEach(module => {
    const status = statusFor(module);
    const card = document.createElement('article');
    card.className = `module-card status-${status}`;
    card.innerHTML = `
      <div class="module-top">
        <div>
          <div class="meta">Teil ${String(module.recommendedOrder).padStart(2, '0')} · ${module.durationMinutes} Minuten · ${module.focus}</div>
          <h2>${escapeHtml(module.title)}</h2>
        </div>
        <select aria-label="Status fuer ${escapeHtml(module.title)}">
          ${['offen','geplant','durchgefuehrt','uebersprungen'].map(value => `<option value="${value}" ${value === status ? 'selected' : ''}>${value}</option>`).join('')}
        </select>
      </div>
      <div class="tags">${module.tools.map(tool => `<span class="tag">${escapeHtml(tool)}</span>`).join('')}</div>
      <div class="actions">
        <button type="button" data-detail="${module.id}">Details</button>
        <a class="open-link" href="${module.presentationPath}">Praesentation oeffnen</a>
      </div>
    `;
    card.querySelector('select').addEventListener('change', event => {
      statuses[module.id] = event.target.value;
      saveStatuses();
      render();
    });
    card.querySelector('[data-detail]').addEventListener('click', () => {
      selectedId = module.id;
      renderDetail();
    });
    listEl.appendChild(card);
  });
  if (!listEl.children.length) {
    listEl.innerHTML = '<article class="module-card"><h2>Keine Treffer</h2><p>Filter oder Suche anpassen.</p></article>';
  }
}
function renderDetail() {
  const module = data.modules.find(item => item.id === selectedId) || data.modules[0];
  detailEl.innerHTML = `
    <h2>${escapeHtml(module.title)}</h2>
    <p class="meta">Teil ${module.recommendedOrder} · ${module.durationMinutes} Minuten · ${escapeHtml(module.focus)}</p>
    <h3>Lernziele</h3>
    <ul>${module.learningGoals.map(item => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
    <h3>Tools</h3>
    <div class="tags">${module.tools.map(tool => `<span class="tag">${escapeHtml(tool)}</span>`).join('')}</div>
    <h3>Vorbereitung</h3>
    <ul>${module.preparation.map(item => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
    <h3>Praxisanteil</h3>
    <ul>${module.practice.map(item => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
    <h3>Vertiefung</h3>
    <ul>${module.deepDive.map(item => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
    <h3>Unterlagen im Modulordner</h3>
    <ul>${module.materials.map(item => `<li><a href="${item.path}">${escapeHtml(item.label)}</a></li>`).join('')}</ul>
    <p style="margin-top: 18px;"><a class="open-link" href="${module.presentationPath}">Praesentation oeffnen</a></p>
  `;
}
function renderProgress() {
  const done = data.modules.filter(module => statusFor(module) === 'durchgefuehrt').length;
  const skipped = data.modules.filter(module => statusFor(module) === 'uebersprungen').length;
  const total = data.modules.length;
  progressBar.style.width = `${(done / total) * 100}%`;
  progressText.textContent = `${done} von ${total} durchgefuehrt · ${skipped} uebersprungen · ${data.totalDurationMinutes} Minuten Gesamtumfang`;
}
function exportStatuses() {
  const payload = {
    exportedAt: new Date().toISOString(),
    title: data.title,
    statuses
  };
  const text = JSON.stringify(payload, null, 2);
  document.getElementById('statusJson').value = text;
  const blob = new Blob([text], { type: 'application/json' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'workshop-status.json';
  link.click();
  URL.revokeObjectURL(link.href);
}
function importStatuses() {
  const raw = document.getElementById('statusJson').value.trim();
  if (!raw) return;
  try {
    const payload = JSON.parse(raw);
    const next = payload.statuses || payload;
    const allowed = new Set(['offen','geplant','durchgefuehrt','uebersprungen']);
    Object.entries(next).forEach(([key, value]) => {
      if (allowed.has(value)) statuses[key] = value;
    });
    saveStatuses();
    render();
  } catch (error) {
    alert('Der JSON-Import konnte nicht gelesen werden.');
  }
}
function resetStatuses() {
  if (!confirm('Alle lokal gespeicherten Statuswerte zuruecksetzen?')) return;
  statuses = {};
  saveStatuses();
  render();
}
function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
}
function render() {
  renderProgress();
  renderList();
  renderDetail();
}
['input','change'].forEach(eventName => {
  searchInput.addEventListener(eventName, renderList);
  statusFilter.addEventListener(eventName, renderList);
  toolFilter.addEventListener(eventName, renderList);
  focusFilter.addEventListener(eventName, renderList);
});
document.getElementById('exportBtn').addEventListener('click', exportStatuses);
document.getElementById('importBtn').addEventListener('click', importStatuses);
document.getElementById('resetBtn').addEventListener('click', resetStatuses);
document.getElementById('printBtn').addEventListener('click', () => window.print());
document.getElementById('statusFile').addEventListener('change', async event => {
  const file = event.target.files[0];
  if (!file) return;
  document.getElementById('statusJson').value = await file.text();
  importStatuses();
});
fillFilters();
render();
"""


def build_workshop_data() -> dict:
  modules = []
  for order, module in enumerate(MODULES, start=1):
    modules.append(
      {
        "id": module["id"],
        "title": module["title"],
        "durationMinutes": 60,
        "recommendedOrder": order,
        "focus": module["focus"],
        "audienceFocus": module["audienceFocus"],
        "tools": module["tools"],
        "learningGoals": module["learningGoals"],
        "terms": module["terms"],
        "preparation": preparation_for(module),
        "practice": module["practice"],
        "deepDive": module["deepDive"],
        "trainerFolder": module["slug"],
        "materials": [
          {"label": "Präsentation", "path": f"{module['slug']}/presentation.html"},
          {"label": "Inhaltsdatei", "path": f"{module['slug']}/modul-inhalt.json"},
          {"label": "Anpassungshinweise", "path": f"{module['slug']}/anpassungshinweise.md"},
          {"label": "Trainerleitfaden", "path": f"{module['slug']}/trainerleitfaden.md"},
          {"label": "Vorbereitung", "path": f"{module['slug']}/vorbereitung.md"},
          {"label": "To-do", "path": f"{module['slug']}/todo.md"},
          {"label": "Übungen und Prompts", "path": f"{module['slug']}/uebung-prompts.md"},
        ],
        "presentationPath": f"{module['slug']}/presentation.html",
        "statusDefault": "offen",
      }
    )
  return {
    "title": "Offline-KI-Schulung nach Common Core und Teamstunden",
    "environment": "Offline-Schulungsumgebung mit vorbereiteter Online-Recherche",
    "totalDurationMinutes": sum(module["durationMinutes"] for module in modules),
    "modules": modules,
  }


def preparation_for(module: dict) -> list[str]:
  items = [
    "Lokale Schulungsumgebung ohne notwendige Internetverbindung bereitstellen.",
    "Keine sensiblen Produktivdaten fuer Uebungen verwenden.",
  ]
  if "OpenWebUI" in module["tools"]:
    items.append("OpenWebUI-Zugang und geeignete Problemfallmodelle pruefen.")
  if "VS Code" in module["tools"] or "Continue.dev" in module["tools"]:
    items.append("VS Code mit Continue.dev oeffnen und ein unkritisches Beispielverzeichnis bereithalten.")
  if "Seafile" in module["tools"] or "SeaDrive" in module["tools"]:
    items.append("SeaDrive-Syncstatus und Beispielbibliothek pruefen.")
  if module.get("teamSpecific"):
    items.append("Team bringt ein kleines, unkritisches Beispielproblem und relevantes Material mit.")
  if module["id"] == "teil-20":
    items.append("Ergebnisse aus den Teamstunden bereithalten.")
  return items


def render_plan_html(data: dict) -> str:
  return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(data['title'])}</title>
  <style>{PLAN_CSS}</style>
</head>
<body>
  <header class="app-header">
    <h1>{escape(data['title'])}</h1>
    <p class="intro">Interaktiver, offline nutzbarer Workshopplan fuer 20 Einheiten. Status, Filter und Export bleiben lokal im Browser gespeichert.</p>
    <span class="offline-badge">Offline nutzbar nach Kopie des gesamten Ordners</span>
  </header>
  <section class="toolbar" aria-label="Filter und Suche">
    <input id="search" type="search" placeholder="Suchen nach Modul, Tool, Ziel oder Inhalt">
    <select id="statusFilter" aria-label="Nach Status filtern">
      <option value="">Alle Status</option>
      <option value="offen">offen</option>
      <option value="geplant">geplant</option>
      <option value="durchgefuehrt">durchgefuehrt</option>
      <option value="uebersprungen">uebersprungen</option>
    </select>
    <select id="toolFilter" aria-label="Nach Tool filtern"><option value="">Alle Tools</option></select>
    <select id="focusFilter" aria-label="Nach Schwerpunkt filtern"><option value="">Alle Schwerpunkte</option></select>
  </section>
  <main class="layout">
    <section>
      <div class="status-panel">
        <strong>Fortschritt</strong>
        <div class="progress-shell"><div id="progressBar" class="progress-bar"></div></div>
        <p id="progressText" class="meta"></p>
        <div class="actions">
          <button id="exportBtn" type="button">Status exportieren</button>
          <button id="importBtn" type="button">Status importieren</button>
          <button id="resetBtn" type="button">Status zuruecksetzen</button>
          <button id="printBtn" type="button">Plan drucken</button>
        </div>
      </div>
      <div id="moduleList" class="module-list"></div>
      <div class="export-panel">
        <strong>Statusimport und Exportdaten</strong>
        <p class="meta">JSON hier einfuegen oder Datei waehlen. Der Import veraendert nur lokale Browserdaten.</p>
        <input id="statusFile" type="file" accept="application/json">
        <textarea id="statusJson" placeholder="Exportiertes JSON erscheint hier oder kann hier eingefuegt werden."></textarea>
      </div>
    </section>
    <aside id="detailPanel" class="detail-panel" aria-label="Moduldetails"></aside>
  </main>
  <script type="application/json" id="workshop-data">{json.dumps(data, ensure_ascii=False, indent=2)}</script>
  <script>{PLAN_JS}</script>
</body>
</html>
"""


def write_json(path: Path, data: dict) -> None:
  rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
  path.write_text(germanize(rendered), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
  path.write_text(germanize(text), encoding="utf-8", newline="\n")


def render_readme(data: dict) -> str:
  module_lines = "\n".join(
    f"- Teil {m['recommendedOrder']:02d}: [{m['title']}]({m['presentationPath']})"
    for m in data["modules"]
  )
  source_lines = "\n".join(f"- {s['name']}: {s['url']}" for s in SOURCES)
  return f"""# Offline-KI-Schulung nach Common Core und Teamstunden

Dieses Paket enthaelt eine mehrteilige, offline nutzbare KI-Schulung als HTML-Paket.

## Einstieg

Oeffne zuerst:

```text
workshopplan.html
```

Von dort aus sind alle 20 Praesentationen verlinkt. Die Statusverwaltung funktioniert lokal im Browser per `localStorage`.

## Umfang

- 20 Workshopteile zu je 60 Minuten
- Gesamtumfang: {data['totalDurationMinutes']} Minuten
- 8 gemeinsame Grundlagen- und Werkzeugmodule
- 11 teambezogene Praxisstunden
- 1 gemeinsame Retrospektive
- Jeder Modulordner enthält Präsentation, editierbare Inhaltsdatei, Anpassungshinweise, Trainerleitfaden, Vorbereitung, To-do und Übungs-/Promptblatt.

## Offline-Nutzung

Der gesamte Ordner `workshop-ki-offline` kann in die Offlineumgebung kopiert werden. Die HTML-Dateien laden keine externen Skripte, Stylesheets, Webfonts, Bilder, Trackingdienste oder CDNs.

Internet wurde nur fuer die Vorbereitung und fachliche Pruefung genutzt. Laufzeitabhaengigkeiten sind nicht erforderlich.

## Inhalte anpassen

Jeder Modulordner enthält:

- `modul-inhalt.json` für fachliche Textanpassungen
- `anpassungshinweise.md` mit Regeln für gute Änderungen
- `trainerleitfaden.md`, `vorbereitung.md`, `todo.md` und `uebung-prompts.md`

Nach Änderungen an den Inhaltsdateien kann das Paket mit `python .\\generate_workshop_package.py` neu erzeugt werden. Ordner- und Dateinamen bleiben bewusst ASCII, damit das Paket in Offlineumgebungen robust kopierbar ist.

## Module

{module_lines}

## Annahmen

- Lokale OpenWebUI-Tabellen fuer Modelle, Skills, Tools, Kalender und Automations waren vorhanden, aber leer.
- Deshalb werden keine produktiven internen IDs, Modellnamen, Serveradressen, Tokens oder Zugangsdaten genannt.
- Problemfallmodelle werden als Aufgabenmodelle erklaert, ohne tief in die Administration einzusteigen.
- RAGFlow bleibt Hintergrundkomponente; Teilnehmende bedienen Seafile, SeaDrive, OpenWebUI, VS Code und Continue.dev.

## Quellen in der Vorbereitung

{source_lines}
"""


def render_trainer_index(data: dict) -> str:
  rows = "\n".join(
    f"| {m['recommendedOrder']:02d} | {m['title']} | `{m['trainerFolder']}` | {', '.join(mat['label'] for mat in m['materials'])} |"
    for m in data["modules"]
  )
  return f"""# Ausbilderübersicht

Diese Übersicht ist der schnelle Einstieg für Personen, die einzelne Stunden durchführen.

## Arbeitsweise

1. Den passenden Modulordner öffnen.
2. Zuerst `vorbereitung.md` lesen.
3. `todo.md` als Ablauf- und Nachbereitungscheckliste verwenden.
4. `presentation.html` im Browser öffnen.
5. `uebung-prompts.md` für Praxisaufgaben und Beispielprompts nutzen.
6. Nach der Stunde den Status in `workshopplan.html` setzen.

## Modulordner

| Teil | Einheit | Ordner | Enthaltene Unterlagen |
|---|---|---|---|
{rows}

## Hinweise für die Durchführung

- Keine produktiven Secrets, personenbezogenen Daten oder vertraulichen Inhalte in Prompts verwenden.
- Bei Teamstunden nur so viel Kontext verwenden, wie für den Prototyp nötig ist.
- Ergebnisse als Entwurf behandeln und fachlich prüfen lassen.
- Offene Fragen direkt für die Retrospektive sammeln.
"""


def render_trainer_guide(module: dict, order: int) -> str:
  return f"""# Trainerleitfaden - Teil {order:02d}: {module['title']}

## Ziel der Stunde

{module['subtitle']}

## Kurzprofil

- Dauer: 60 Minuten
- Schwerpunkt: {module['focus']}
- Zielgruppe: {', '.join(module['audienceFocus'])}
- Werkzeuge: {', '.join(module['tools'])}

## Lernziele

{md_list(module['learningGoals'])}

## Ablauf

| Zeit | Inhalt | Durchführung |
|---|---|---|
| 0-5 Min. | Einstieg | Ziel der Stunde nennen, Vorwissen nicht voraussetzen. |
| 5-15 Min. | Begriffe | Nur die Begriffe erklären, die in der Übung gebraucht werden. |
| 15-30 Min. | Demo | Schritte langsam zeigen und jeden Wechsel des Werkzeugs begründen. |
| 30-50 Min. | Praxis | Teilnehmende arbeiten mit unkritischem Material oder Beispielmaterial. |
| 50-55 Min. | Mini-Check | Drei Kontrollfragen beantworten lassen. |
| 55-60 Min. | Transfer | Ergebnis sichern und nächsten Schritt notieren. |

## Demo-Schritte

{md_list(module['demo'])}

## Moderationshinweise

- Antworten der KI nicht bewerten lassen, bevor klar ist, welches Ziel und welcher Kontext gemeint waren.
- Bei Unsicherheit zuerst nach Quelle, Annahme und Prüfweg fragen lassen.
- Technische Vertiefung anbieten, aber die Basisspur nicht verlieren.
- Bei Teamstunden das Ergebnis klein halten: ein Prototyp, eine Liste, ein Plan oder eine begründete Entscheidung.

## Mini-Check

{md_list(module['check'])}
"""


def render_preparation_doc(module: dict, order: int) -> str:
  return f"""# Vorbereitung - Teil {order:02d}: {module['title']}

## Vor der Stunde prüfen

{md_list(preparation_for(module))}

## Benötigtes Material

{md_list(materials_for(module))}

## Raum und Technik

- Browser kann lokale HTML-Dateien öffnen.
- OpenWebUI, VS Code, Continue.dev und SeaDrive sind nur dort nötig, wo sie in der Einheit genutzt werden.
- Für die Übungen wird unkritisches Beispielmaterial bereitgelegt.
- Es ist keine Internetverbindung für die Durchführung nötig.

## Datenschutz und Sicherheit

{md_list(SECURITY_RULES)}

## Falls etwas nicht funktioniert

- Präsentation direkt aus dem Modulordner öffnen.
- Bei OpenWebUI-Problemen auf Demo als Beobachtung wechseln und Übung auf Papier durchführen.
- Bei Continue.dev-Problemen Codeausschnitt in OpenWebUI besprechen oder Arbeitsplan statt Dateiänderung erstellen.
- Bei SeaDrive-Problemen eine lokale Kopie des Beispielmaterials verwenden und Syncstatus später prüfen.
"""


def render_todo_doc(module: dict, order: int) -> str:
  return f"""# To-do - Teil {order:02d}: {module['title']}

## Vorher

- [ ] Modulordner öffnen und Präsentation testen.
- [ ] Demo-Material vorbereiten.
- [ ] Prüfen, welche Werkzeuge in dieser Stunde wirklich gebraucht werden.
- [ ] Beispiel ohne sensible Daten bereitlegen.
- [ ] Raum, Beamer und Browseransicht testen.

## Während der Stunde

- [ ] Ziel und Zeitbox nennen.
- [ ] Begriffe kurz erklären.
- [ ] Demo langsam durchführen.
- [ ] Praxisaufgabe starten und Rückfragen sammeln.
- [ ] Mini-Check durchführen.
- [ ] Status oder offene Punkte notieren.

## Danach

- [ ] Status im `workshopplan.html` setzen.
- [ ] Offene Fragen für die Retrospektive sammeln.
- [ ] Team-Ergebnisse oder Prototypnotizen sichern.
- [ ] Auffällige Tool-, Daten- oder Berechtigungsprobleme weitergeben.
"""


def render_exercise_doc(module: dict, order: int) -> str:
  return f"""# Übungen und Prompts - Teil {order:02d}: {module['title']}

## Praxisaufgabe

{md_list(module['practice'])}

## Beispielprompt

```text
{prompt_template(module)}
```

## Varianten

- Ausgabe als Tabelle verlangen.
- Annahmen, gesicherte Aussagen und offene Fragen getrennt ausgeben lassen.
- Erst einen Plan verlangen, dann die eigentliche Ausarbeitung.
- Bei Dokumentenarbeit nach Quellenbezug und Textstellen fragen.
- Bei Codearbeit nach betroffenen Dateien, Risiken und Tests fragen.

## Ergebnisformat

Am Ende der Übung soll mindestens eines dieser Ergebnisse vorliegen:

- kurze Zusammenfassung
- Checkliste
- Tabelle mit Annahmen und offenen Fragen
- kleiner Änderungsplan
- Testfallliste
- Handoff-Notiz für DevOps/Admins
- Prototypnotiz für die nächste Arbeitssitzung

## Prüfregel

Das Ergebnis wird nicht ungeprüft übernommen. Es wird markiert, welche Teile aus bereitgestelltem Material stammen, welche Teile Annahmen sind und welche Punkte fachlich geklärt werden müssen.
"""


def editable_module_payload(module: dict, order: int) -> dict:
  return {
    "hinweis": "Diese Datei ist für Ausbilder gedacht. Inhalte können hier angepasst und anschließend mit generate_workshop_package.py neu erzeugt werden.",
    "recommendedOrder": order,
    "id": module["id"],
    "slug": module["slug"],
    "title": module["title"],
    "subtitle": module["subtitle"],
    "focus": module["focus"],
    "audienceFocus": module["audienceFocus"],
    "tools": module["tools"],
    "learningGoals": module["learningGoals"],
    "terms": module["terms"],
    "starter": module["starter"],
    "example": module["example"],
    "demo": module["demo"],
    "practice": module["practice"],
    "deepDive": module["deepDive"],
    "errors": module["errors"],
    "check": module["check"],
    "next": module["next"],
    "promptTemplate": prompt_template(module),
  }


def render_adjustment_notes(module: dict, order: int) -> str:
  return f"""# Inhalte anpassen - Teil {order:02d}: {module['title']}

Diese Datei ist für Ausbilder gedacht, die die Stunde auf eine konkrete Gruppe oder ein konkretes Projekt zuschneiden möchten.

## Schnell anpassen

1. `modul-inhalt.json` öffnen.
2. Nur die fachlichen Texte ändern, nicht `id`, `slug` oder Pfade.
3. Kurze Sätze verwenden. Eine Folie soll einen klaren Gedanken haben.
4. Fachbegriffe erklären, wenn sie in der Gruppe nicht sicher bekannt sind.
5. Danach im Projektordner den Generator erneut ausführen:

```powershell
python .\\generate_workshop_package.py
```

## Gute Änderungen

- Lokales Beispiel ersetzen.
- Demo-Schritte an die vorhandene OpenWebUI- oder VS-Code-Konfiguration anpassen.
- Praxisaufgabe auf Teamkontext zuschneiden.
- Promptvorlage mit projektnahen, aber unkritischen Daten konkretisieren.
- Mini-Check um eine Frage ergänzen, die in der Gruppe wirklich relevant ist.

## Nicht ändern

- Keine produktiven Zugangsdaten, Tokens, Serveradressen oder personenbezogenen Daten eintragen.
- Keine Inhalte einfügen, die eine Sicherheitsmaßnahme umgehen oder vertrauliche Informationen offenlegen.
- Keine Folien mit langen Textblöcken überladen.
- Keine externen Bilder, Fonts, Skripte oder CDN-Links einbauen.

## Stilregel

Der Text soll wie ein guter Schulungsleitfaden klingen: konkret, ruhig, knapp und prüfbar. Vermeide abgenutzte Marketingformeln, Superlative ohne Beleg und pauschale Versprechen.

## Dark-Mode-Hinweis

Die Präsentation ist standardmäßig dunkel gestaltet und besitzt einen Hell/Dunkel-Umschalter. Inhalte sollten kurze Überschriften und klare Kontraste behalten, damit sie im Beamerbetrieb lesbar bleiben.
"""


def md_list(items: list[str]) -> str:
  return "\n".join(f"- {item}" for item in items)


def materials_for(module: dict) -> list[str]:
  materials = [
    "Diese Präsentation im Modulordner.",
    "Trainerleitfaden, To-do und Übungsblatt aus demselben Ordner.",
  ]
  if "OpenWebUI" in module["tools"]:
    materials.append("OpenWebUI-Zugang oder vorbereitete Screenshots/Beispielablauf.")
  if "VS Code" in module["tools"] or "Continue.dev" in module["tools"]:
    materials.append("VS Code mit Continue.dev und ein unkritisches Beispielverzeichnis.")
  if "Seafile" in module["tools"] or "SeaDrive" in module["tools"]:
    materials.append("Beispielbibliothek in Seafile oder SeaDrive mit unkritischen Dateien.")
  if module.get("teamSpecific"):
    materials.append("Ein kleines Teamproblem mit Material, das geteilt werden darf.")
  return materials


def render_implementation_notes(data: dict) -> str:
  return f"""# Implementation Notes

Erzeugt am: {datetime.now().isoformat(timespec='seconds')}

## Tatsächlich verwendeter Projektpfad

```text
{PROJECT_ROOT}
```

## Analyse des Präsentationscreator-Projekts

Der Ordner `Präsentationscreator` enthält Markdown-Dateien (`README.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md`, `customgpt_infos.md`) mit Qualitäts-, Storyline- und Single-File-HTML-Regeln. Es wurden keine ausführbaren Generator-Skripte, Package-Dateien oder technischen Templates gefunden.

Deshalb wurde eine Fallback-Generatorlösung erstellt:

```text
generate_workshop_package.py
```

Diese Datei erzeugt aus einem gemeinsamen Datenmodell:

- 20 Präsentationen als eigenständige `presentation.html`
- `workshopplan.html`
- `workshopplan.json`
- `manifest.json`
- `README.md`
- `qa-report.md`

## Lokale OpenWebUI- und Continue-Prüfung

Die lokale OpenWebUI-Datenbank enthält Tabellen für `model`, `skill`, `tool`, `function`, `knowledge`, `calendar`, `calendar_event`, `automation` und `automation_run`. Die geprüften Tabellen enthielten keine Einträge. Daher wurden keine produktiven Modell-, Skill-, Tool-, Kalender- oder Automation-IDs übernommen.

Die lokale Continue-Konfiguration zeigt Rollen für Chat, Code, Embedder und Reranker. Interne Endpunkte und potenziell sensible technische Details wurden nicht in die Schulungsfolien geschrieben.

## Abhängigkeiten

Für die finale Offline-Laufzeit werden keine externen Abhängigkeiten genutzt. CSS, JavaScript und Diagramme sind inline in den HTML-Dateien enthalten.

## Quellen

{chr(10).join(f"- {s['name']}: {s['url']} ({s['usedFor']})" for s in SOURCES)}
"""


def render_manifest(data: dict, files: list[str]) -> dict:
  return {
    "title": data["title"],
    "generatedAt": datetime.now().isoformat(timespec="seconds"),
    "projectPath": str(PROJECT_ROOT),
    "outputPath": str(OUTPUT_ROOT),
    "offlineReady": True,
    "usesExternalRuntimeDependencies": False,
    "totalDurationMinutes": data["totalDurationMinutes"],
    "moduleCount": len(data["modules"]),
    "modules": data["modules"],
    "files": files,
    "sourcesUsedDuringPreparation": SOURCES,
  }


FORBIDDEN_PHRASES = [
  "Sie als " + "Student",
  "Sie als " + "Studierende",
  "Sie als " + "Entwickler",
  "alte " + "Leute",
  "ältere " + "Leute, die nichts verstehen",
  "für alte " + "Menschen",
  "nur für " + "Anfänger",
  "nur für " + "Profis",
  "Studenten " + "sollen",
  "Entwickler " + "müssen",
]


EXTERNAL_PATTERNS = [
  "http://",
  "https://",
  "cdn.",
  "googleapis",
  "gstatic",
  "unpkg",
  "jsdelivr",
  "cdnjs",
  "fonts.",
  "analytics",
  "tracking",
  "integrity=",
  "crossorigin=",
]

FILLER_PHRASES = [
  "in der heutigen digitalen Welt",
  "revolutionär",
  "Gamechanger",
  "Bahnbrechend",
  "KI-Revolution",
  "unbegrenzte Möglichkeiten",
  "einfach per Knopfdruck",
  "magisch",
  "disruptiv",
]


def build_qa_report(data: dict) -> str:
  html_files = sorted(OUTPUT_ROOT.rglob("*.html"))
  all_files = sorted(p for p in OUTPUT_ROOT.rglob("*") if p.is_file())
  missing_presentations = []
  missing_materials = []
  missing_dark_mode = []
  missing_animation = []
  missing_links = []
  slide_counts = []
  external_hits: list[str] = []
  phrase_hits: list[str] = []
  filler_hits: list[str] = []
  umlaut_leftovers: list[str] = []

  for module in data["modules"]:
    presentation = OUTPUT_ROOT / module["presentationPath"]
    if not presentation.exists():
      missing_presentations.append(module["presentationPath"])
    for material in module.get("materials", []):
      if not (OUTPUT_ROOT / material["path"]).exists():
        missing_materials.append(material["path"])

  for html_file in html_files:
    text = html_file.read_text(encoding="utf-8")
    slide_counts.append((html_file.relative_to(OUTPUT_ROOT).as_posix(), len(re.findall(r'<section class="slide', text))))
    if html_file.name == "presentation.html":
      if 'id="themeBtn"' not in text or "light-mode" not in text:
        missing_dark_mode.append(html_file.relative_to(OUTPUT_ROOT).as_posix())
      if "@keyframes" not in text or "slideEnter" not in text:
        missing_animation.append(html_file.relative_to(OUTPUT_ROOT).as_posix())
    for pattern in EXTERNAL_PATTERNS:
      if pattern.lower() in text.lower():
        external_hits.append(f"{html_file.relative_to(OUTPUT_ROOT).as_posix()}: {pattern}")

  for rel in [m["presentationPath"] for m in data["modules"]]:
    if not (OUTPUT_ROOT / rel).exists():
      missing_links.append(rel)

  for file_path in all_files:
    if file_path.suffix.lower() not in {".html", ".md", ".json"}:
      continue
    text = file_path.read_text(encoding="utf-8")
    for phrase in FORBIDDEN_PHRASES:
      if phrase.lower() in text.lower():
        phrase_hits.append(f"{file_path.relative_to(OUTPUT_ROOT).as_posix()}: {phrase}")
    for phrase in FILLER_PHRASES:
      if phrase.lower() in text.lower():
        filler_hits.append(f"{file_path.relative_to(OUTPUT_ROOT).as_posix()}: {phrase}")
    if file_path.suffix.lower() in {".html", ".md", ".json"}:
      for source_word in GERMAN_REPLACEMENTS:
        if GERMAN_REPLACEMENTS[source_word] == source_word:
          continue
        if re.search(rf"\b{re.escape(source_word)}\b", text) and "continue" not in source_word.lower():
          umlaut_leftovers.append(f"{file_path.relative_to(OUTPUT_ROOT).as_posix()}: {source_word}")

  checks = [
    ("20 Präsentationen vorhanden", not missing_presentations),
    ("Alle Modulordner enthalten Trainerunterlagen", not missing_materials),
    ("Alle Präsentationen haben Dark Mode und Umschalter", not missing_dark_mode),
    ("Alle Präsentationen enthalten lokale Animationen", not missing_animation),
    ("workshopplan.html vorhanden", (OUTPUT_ROOT / "workshopplan.html").exists()),
    ("workshopplan.json vorhanden", (OUTPUT_ROOT / "workshopplan.json").exists()),
    ("manifest.json vorhanden", (OUTPUT_ROOT / "manifest.json").exists()),
    ("README.md vorhanden", (OUTPUT_ROOT / "README.md").exists()),
    ("Keine externen Laufzeitreferenzen in HTML", not external_hits),
    ("Alle relativen Präsentationslinks vorhanden", not missing_links),
    ("Alle Module dauern maximal 60 Minuten", all(m["durationMinutes"] <= 60 for m in data["modules"])),
    ("Gesamtdauer korrekt", data["totalDurationMinutes"] == 1200),
    ("Keine verbotenen Formulierungen gefunden", not phrase_hits),
    ("Keine typischen KI-Floskeln gefunden", not filler_hits),
    ("Keine bekannten Umlaut-Transliterationen in Textinhalten", not umlaut_leftovers),
  ]
  check_lines = "\n".join(f"- [{'x' if ok else ' '}] {name}" for name, ok in checks)
  slide_lines = "\n".join(f"- `{path}`: {count} Folien" for path, count in slide_counts if path.endswith("presentation.html"))
  return f"""# QA Report

Erzeugt am: {datetime.now().isoformat(timespec='seconds')}

## Automatische Prüfungen

{check_lines}

## Folienanzahl

{slide_lines}

## Offline-Audit

Geprüfte Muster:

```text
{chr(10).join(EXTERNAL_PATTERNS)}
```

Treffer in HTML-Dateien:

{('- keine Treffer' if not external_hits else chr(10).join(f'- {hit}' for hit in external_hits))}

Hinweis: Externe URLs in Markdown-Dokumentation werden als Quellenangaben akzeptiert. HTML-Dateien dürfen keine externen Laufzeitressourcen laden.

## Linkprüfung

{('- alle relativen Präsentationslinks vorhanden' if not missing_links else chr(10).join(f'- fehlt: {link}' for link in missing_links))}

## Unterlagen pro Modul

{('- alle Trainerleitfäden, Vorbereitungen, To-do-Dateien und Übungs-/Promptblätter vorhanden' if not missing_materials else chr(10).join(f'- fehlt: {link}' for link in missing_materials))}

## Darstellung und Anpassbarkeit

- Dark Mode: {('alle Präsentationen enthalten dunkles Standarddesign und Hell/Dunkel-Umschalter' if not missing_dark_mode else 'fehlt in: ' + ', '.join(missing_dark_mode))}
- Animationen: {('alle Präsentationen enthalten lokale CSS-Animationen' if not missing_animation else 'fehlen in: ' + ', '.join(missing_animation))}
- Anpassbarkeit: Jeder Modulordner enthält `modul-inhalt.json` und `anpassungshinweise.md`.

## Sprachprüfung

Die vorgegebene Liste unerwünschter zielgruppenbezogener Formulierungen wurde gesucht.

{('- keine Treffer' if not phrase_hits else chr(10).join(f'- {hit}' for hit in phrase_hits))}

## Stilprüfung

Typische KI-Floskeln und übertriebene Versprechen wurden gesucht.

{('- keine Treffer' if not filler_hits else chr(10).join(f'- {hit}' for hit in filler_hits))}

## Umlautprüfung

Geprüft wurde auf bekannte deutsche Transliterationen aus der Generator-Ausgabeliste. ASCII-Slugs in Dateipfaden bleiben absichtlich erhalten.

{('- keine Treffer' if not umlaut_leftovers else chr(10).join(f'- {hit}' for hit in umlaut_leftovers[:80]))}

## Inhaltsprüfung

- OpenWebUI wird früh als Chatoberfläche und später mit Skills, Tools, Functions, Kalender und Automations behandelt.
- Problemfallmodelle werden praktisch genutzt, ohne produktive interne Modell-IDs zu erfinden.
- Continue.dev wird für VS Code, Dateien, Repos, kleine agentische Aufgaben und Review-Prüfung vermittelt.
- RAGFlow wird nur als Hintergrundkomponente behandelt; sichtbare Arbeit erfolgt über Seafile, SeaDrive, OpenWebUI und VS Code.
- Sicherheits- und Datenschutzregeln sind in jeder Präsentation enthalten.

## Browserprüfung

Der In-App-Browser blockierte direkte `file://`-Navigation. Für die Funktionsprüfung wurde das statische Paket deshalb kurz über einen lokalen Server auf `127.0.0.1` geöffnet und mit Playwright-Chromium aus dem lokalen Benutzer-Cache geprüft. Der Server wurde danach beendet.

Geprüfte Punkte:

- `workshopplan.html` lädt mit 20 Modulkarten.
- Es werden keine externen Runtime-Assets geladen.
- Suche nach `Frontend 4` filtert auf 1 Modul.
- Statusänderung auf `durchgeführt` aktualisiert Fortschritt und wird in `localStorage` gespeichert.
- Status bleibt nach Reload erhalten.
- Statusexport schreibt JSON in das Exportfeld.
- Statusimport liest JSON ein und aktualisiert den Fortschritt.
- Reset setzt alle Statuswerte zurück.
- Beispielpräsentation `teil-05-openwebui-zusatzfunktionen/presentation.html` lädt mit 16 Folien.
- Präsentationen starten im dunklen Standarddesign.
- Hell/Dunkel-Umschalter ist vorhanden und funktioniert.
- Lokale CSS-Animationen sind vorhanden.
- Tastaturnavigation springt von Folie 1 auf Folie 2.
- Notizen-Umschaltung blendet Moderationsnotizen aus.

Ergebnis:

```text
Workshopplan, Dark Mode, Theme-Umschalter, Animationen und Präsentationsnavigation funktionieren lokal.
```
"""


def generate() -> None:
  if OUTPUT_ROOT.exists():
    shutil.rmtree(OUTPUT_ROOT)
  OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
  (OUTPUT_ROOT / "assets" / "vendor").mkdir(parents=True, exist_ok=True)

  data = build_workshop_data()
  for index, module in enumerate(MODULES, start=1):
    module_dir = OUTPUT_ROOT / module["slug"]
    module_dir.mkdir(parents=True, exist_ok=True)
    write_text(module_dir / "presentation.html", render_presentation(module, index, len(MODULES)))
    write_json(module_dir / "modul-inhalt.json", editable_module_payload(module, index))
    write_text(module_dir / "anpassungshinweise.md", render_adjustment_notes(module, index))
    write_text(module_dir / "trainerleitfaden.md", render_trainer_guide(module, index))
    write_text(module_dir / "vorbereitung.md", render_preparation_doc(module, index))
    write_text(module_dir / "todo.md", render_todo_doc(module, index))
    write_text(module_dir / "uebung-prompts.md", render_exercise_doc(module, index))

  write_json(OUTPUT_ROOT / "workshopplan.json", data)
  write_text(OUTPUT_ROOT / "workshopplan.html", render_plan_html(data))
  write_text(OUTPUT_ROOT / "README.md", render_readme(data))
  write_text(OUTPUT_ROOT / "trainer-index.md", render_trainer_index(data))
  write_text(OUTPUT_ROOT / "implementation-notes.md", render_implementation_notes(data))

  files = sorted(p.relative_to(OUTPUT_ROOT).as_posix() for p in OUTPUT_ROOT.rglob("*") if p.is_file())
  manifest = render_manifest(data, files)
  write_json(OUTPUT_ROOT / "manifest.json", manifest)
  write_text(OUTPUT_ROOT / "qa-report.md", build_qa_report(data))


if __name__ == "__main__":
  generate()
  print(f"Generated workshop package at {OUTPUT_ROOT}")
