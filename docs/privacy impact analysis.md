# 2.2 Privacy Impact Analysis

## 1. FinSec-Benutzerdaten

- **Daten:** Benutzerkennung, E-Mail-Adresse und Passwort-Hash. Das eingegebene Passwort wird nur zur Anmeldung verarbeitet und nicht im Klartext gespeichert.
- **Übermittlung:** Vom Nutzer über das Web-Frontend bzw. die geplante App an die Authentisierung im Backend. FinSec-Anmeldedaten werden nicht an die Bank weitergegeben.
- **Speicherung:** Benutzerkennung, E-Mail-Adresse und Passwort-Hash in der FinSec-Datenbank.
- **Zweck:** Benutzerkonto anlegen, anmelden und die Daten dem richtigen Nutzer zuordnen.
- **Funktionale DSGVO-Anforderungen:** Bei der Registrierung über Zweck und Verarbeitung informieren (Art. 13); nur erforderliche Angaben abfragen (Art. 5 Abs. 1 lit. c); Auskunft und Berichtigung der Kontaktdaten ermöglichen (Art. 15, 16); beim Löschen des Benutzerkontos die Daten löschen, soweit keine Aufbewahrungspflicht entgegensteht (Art. 17).

## 2. Bankverbindungs- und Berechtigungsdaten

- **Daten:** Kontoinhaber, IBAN, Bankzuordnung und dem Nutzer zugeordnete Zugriffs- und Refresh-Tokens.
- **Übermittlung:** Zwischen Bank und FinSec-Bankanbindung; Kontozuordnung an die Anwendungslogik und zur Anzeige an das Frontend. Bank-Tokens bleiben im Backend und werden nur an die zugehörige Bank gesendet.
- **Speicherung:** Kontozuordnung und benötigte Tokens geschützt in der FinSec-Datenbank.
- **Zweck:** Bankkonten verknüpfen und die vom Nutzer erlaubten Bankzugriffe ausführen.
- **Funktionale DSGVO-Anforderungen:** Nutzer über Datenumfang und Empfänger informieren (Art. 13); nur die erforderlichen Konten und Berechtigungen verwenden (Art. 5, 25); eine Funktion zum Trennen der Bankverbindung vorsehen und danach nicht mehr benötigte Tokens löschen (Art. 5 Abs. 1 lit. e, Art. 17). Wird die Verarbeitung auf Einwilligung gestützt, muss sie widerrufbar sein (Art. 7 Abs. 3).

## 3. Finanz- und Transaktionsdaten

- **Daten:** Kontostände, Umsätze mit Betrag, Datum, Zahlungspartner und Verwendungszweck sowie daraus abgeleitete Ausgabenkategorien.
- **Übermittlung:** Von der Bank über die Bankanbindung an Anwendungslogik, Finanzdatenverarbeitung und Datenbank; Kontostände und Auswertungen zurück an das Frontend. Bei einer Überweisung gehen die erforderlichen Zahlungsdaten an die Bank.
- **Speicherung:** In der FinSec-Datenbank; während der Analyse zusätzlich vorübergehend in der Finanzdatenverarbeitung.
- **Zweck:** Kontostände und Umsätze anzeigen, Überweisungen ausführen, Ausgaben auswerten und Sparhinweise erstellen.
- **Funktionale DSGVO-Anforderungen:** Nur Daten für diese Zwecke abrufen und verarbeiten (Art. 5 Abs. 1 lit. b, c); dem Nutzer Auskunft und einen Export ermöglichen, bei erfüllten Voraussetzungen auch in einem übertragbaren Format (Art. 15, 20); falsche Zuordnungen bzw. Auswertungskategorien korrigierbar machen (Art. 16); nicht mehr benötigte Daten nach festgelegten Fristen löschen, soweit keine Aufbewahrungspflicht besteht (Art. 5 Abs. 1 lit. e, Art. 17).
