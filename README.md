# One Million Checkboxes Clicker - Selenium Script

## Projektbeschreibung

Dieses Projekt ist ein Lernprojekt, das die Bibliothek **Selenium** verwendet, um eine Website zu automatisieren. Es besucht die Seite [One Million Checkboxes](https://onemillioncheckboxes.com) und klickt automatisch auf die Checkboxes. 

Das Projekt wurde entwickelt, um praktische Erfahrung mit **Selenium** zu sammeln, einer populären Bibliothek zur Automatisierung von Webanwendungen, und um **Logging** in Python besser zu verstehen. 

## Funktionen

- Automatisches Klicken auf Checkboxen auf der Seite [onemillioncheckboxes.com](https://onemillioncheckboxes.com)
- Integrierte **Logging**-Mechanismen, um Aktionen und Fehler zu protokollieren
- Geeignet als Lernprojekt für Einsteiger, die Selenium und Logging näher kennenlernen möchten

## Voraussetzungen

Stelle sicher, dass folgende Programme und Bibliotheken auf deinem System installiert sind:

- **Python 3.x**
- **Selenium**
- Ein Webdriver für deinen bevorzugten Browser (z.B. ChromeDriver für Chrome)

## Installation

1. **Klone das Repository**:

   ```bash
   git clone https://github.com/dein-benutzername/dein-repository.git

2. **Erstelle eine virtuelle Umgebung (optional, aber empfohlen):**

    python -m venv venv
    source venv/bin/activate    # Für Linux/macOS
    # oder 
    venv\Scripts\activate       # Für Windows

3. **Installiere die benötigten Bibliotheken:**

    pip install -r requirements.txt


## Verwendung

1. **Starte das Script**:

    ```bash
    python omcb_checker.py

2. **Das Script öffnet automatisch die Seite onemillioncheckboxes.com und beginnt mit dem Klicken auf die Checkboxen.**

3. **Logs: Alle Aktionen werden im Log-File protokolliert, das dir eine Übersicht über die durchgeführten Klicks und mögliche Fehler gibt.**

## Logging

Das Projekt verwendet das Python-Logging-Modul, um Informationen über den Status des Scripts zu erfassen. Die Log-Daten werden in einer Datei gespeichert, die du in der Datei omcb_checker.py konfigurieren kannst.

Wenn du das Logging nutzen willst, achte darauf eine oder beide Booleans auf True zu setzen.
ENABLE_CONSOLE_LOGGING = False
ENABLE_FILE_LOGGING = False


Die Logs enthalten:

- Info-Meldungen: Zu erfolgreichen Aktionen
- Warnungen: Falls eine Checkbox nicht angeklickt werden konnte
- Fehler: Falls die Seite nicht geladen werden kann oder andere Probleme auftreten

## Lizenz

Dieses Projekt ist lizenziert unter der MIT License - siehe die LICENSE Datei für Details.


## Danksagungen

    Selenium für die großartige Bibliothek zur Webautomatisierung
    One Million Checkboxes für die Seite als Übungsobjekt


### Erklärung der Abschnitte:
- **Projektbeschreibung**: Eine kurze Einführung, was das Projekt macht und warum es entwickelt wurde.
- **Funktionen**: Eine Übersicht der Kernfunktionen des Scripts.
- **Voraussetzungen**: Notwendige Software und Bibliotheken, die vor dem Ausführen installiert werden müssen.
- **Installation**: Anweisungen zum Klonen des Repositories und zum Installieren der Abhängigkeiten.
- **Verwendung**: Einfache Anleitung, wie man das Script startet und was es tut.
- **Logging**: Ein kurzer Abschnitt, der erklärt, wie Logging im Projekt funktioniert.
- **Lizenz**: Eine allgemeine Erwähnung der MIT-Lizenz.

Du kannst diese Vorlage weiter anpassen, wenn du noch spezifische Informationen hinzufügen möchtest oder wenn sich das Projekt in Zukunft weiterentwickelt.

Wenn du möchtest, kann ich noch bestimmte Details ergänzen, wenn du sie mir mitteilst!