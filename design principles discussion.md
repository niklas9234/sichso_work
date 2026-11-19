# Design Principles Discussion – FinSec

## Ausgangspunkt und Sicherheitsarchitektur

In der [funktionalen Architektur aus Übung 2, Aufgabe 4](docs/functional%20architecture.md) greifen Authentifizierung, Kontoverwaltung, Zahlungsverwaltung, Finanzdatenverarbeitung und Bankanbindung auf eine gemeinsame Datenbank zu. Das Ausgangsdiagramm weist für diese Zugriffe keine separaten Rechte aus.

### Vorher – funktionale Architektur

```mermaid
flowchart TB
    subgraph FE["Frontend"]
        FAuth["Authentifizierung: Anmeldung und Abmeldung"]
        FAccount["Bankkonto verknüpfen; Kontostand und Transaktionen anzeigen"]
        FPayment["Überweisung erfassen und Status anzeigen"]
        FAnalysis["Auswertungen und Sparhinweise anzeigen"]
    end

    subgraph BE["Backend"]
        BAuth["Authentifizierung: Zugangsdaten und Sitzung prüfen"]
        BAccount["Kontoverwaltung: Konten zuordnen und Finanzdaten abrufen"]
        BPayment["Zahlungsverwaltung: Aufträge prüfen und weiterleiten"]
        BAnalysis["Finanzdatenverarbeitung: klassifizieren, aggregieren, analysieren; Sparhinweise erstellen"]
        BBank["Bankanbindung: Autorisierung, Tokens und Bank-API"]
        DB[("Datenbank: Nutzer und Passworthashes, Bankverbindungen und Finanzdaten")]
    end

    Bank["EuroTrust / weitere Banken (extern)"]

    FAuth <--> BAuth
    FAccount <--> BAccount
    FPayment <--> BPayment
    FAnalysis <--> BAnalysis
    BAuth <-->|"FinSec-Login-Daten"| DB
    BAuth -.->|"Sitzung und Berechtigung prüfen"| BAccount
    BAuth -.->|"Sitzung und Berechtigung prüfen"| BPayment
    BAuth -.->|"Sitzung und Berechtigung prüfen"| BAnalysis
    BAccount <--> BBank
    BPayment <--> BBank
    BAccount <--> DB
    BPayment <--> DB
    BAnalysis <--> DB
    BBank <--> DB
    BBank <--> Bank
```

### Nachher – Sicherheitsarchitektur

Die Sicherheitsarchitektur zeigt die getrennten Speicherbereiche und markiert die Prüfungen, die Zugriffe oder Bankaufrufe freigeben.

```mermaid
flowchart LR
    Browser["Browser / FinSec-Frontend"]
    Bank["EuroTrust – Bank-Login und TOTP"]
    subgraph Backend["FinSec-Backend"]
        Auth["FinSec-Authentifizierung"]
        Accounts["Kontoverwaltung"]
        Payments["Zahlungsverwaltung"]
        Analysis["Finanzdatenverarbeitung"]
        Adapter["Bankanbindung – Company Token und Customer Token im Arbeitsspeicher"]
        Callback["Backend-Callback – Authorization Code und state prüfen"]
    end
    subgraph Storage["Getrennte Zugriffsbereiche"]
        Users[("FinSec-Nutzerdaten")]
        Login[("FinSec-Auth – Passworthashes und Sitzungen")]
        Consents[("Bankverbindungen und Einwilligungen")]
        Finance[("Kontostände und Transaktionen")]
        Orders[("Zahlungsaufträge und Status")]
        Results[("Auswertungen und Sparhinweise")]
        Config[("Secret-Speicher – Client-ID und Client-Secret")]
        Refresh[("Token-Speicher – Customer Refresh Token")]
        Pending[("Kurzlebiger SCA-Vorgang – state, Sitzung, Vorgang")]
    end
    Browser -->|"FinSec-Login"| Auth
    Browser -->|"Sitzungsnachweis und Anfrage"| Accounts & Payments & Analysis
    Accounts & Payments & Analysis -.->|"Sitzung prüfen"| Auth
    Auth --> Users & Login
    Accounts -->|"Verbindungen verwalten"| Consents
    Payments -->|"Kontozuordnung lesen"| Consents
    Accounts -->|"Bankdaten abrufen"| Adapter
    Payments -->|"Zahlung auslösen / Status abfragen"| Adapter
    Accounts -->|"Lesen und schreiben"| Finance
    Finance -->|"Freigegebene Daten lesen"| Analysis
    Payments --> Orders
    Analysis --> Results
    Adapter --> Config & Refresh & Pending
    Adapter -.->|"scaRedirect mit state über die Fachkomponente"| Browser
    Browser -->|"Weiterleitung, Bank-Login direkt bei EuroTrust"| Bank
    Bank -.->|"Redirect über Browser mit Authorization Code und state"| Callback
    Callback -->|"Einmaligen Vorgang prüfen"| Pending
    Callback -.->|"FinSec-Sitzung prüfen"| Auth
    Callback -->|"Code nach erfolgreicher Prüfung weitergeben"| Adapter
    Adapter <-->|"Token-Endpunkt und zweckgebundene Bankaufrufe"| Bank
```

## 1.1 Zugangsmittel nach EuroTrust-Spezifikation

| Zugangsmittel | Wer braucht es und wofür? | Speicherort und Lebensdauer |
| --- | --- | --- |
| Client-ID und Client-Secret | Die Bankanbindung weist damit FinSec gegenüber dem EuroTrust-Token-Endpunkt aus. Das Paar wird beim Company-Token-Abruf, beim Code-Austausch und beim Refresh verwendet. | Langlebig in serverseitiger Konfiguration mit Zugriff für die Bankanbindung. Das Client-Secret liegt im Secret-Speicher und wird nur an den Token-Endpunkt gesendet. |
| Company Token | Die Bankanbindung erstellt damit eine Anfrage zur Kontoverknüpfung bei EuroTrust. | Kurzzeitig im Arbeitsspeicher der Bankanbindung, laut Spezifikation etwa 10 Minuten gültig. |
| Bankzugangsdaten der Kund:innen | Kund:innen geben Bank-Benutzername, Passwort und TOTP auf der EuroTrust-Seite ein. EuroTrust prüft sie. | Die Zugangsdaten bleiben bei Kund:innen und EuroTrust. FinSec speichert sie nicht. |
| Authorization Code | EuroTrust leitet den Browser mit einem einmaligen Code an die registrierte FinSec-Rückkehr-URL weiter. Der Backend-Callback prüft die Zuordnung zur Sitzung und zum Vorgang. Die Bankanbindung tauscht den Code anschließend am Token-Endpunkt ein. | Nur während der Verarbeitung im Backend, laut Spezifikation etwa 60 Sekunden gültig. Callback-Parameter werden von der Protokollierung ausgenommen. |
| Customer Refresh Token | Die Bankanbindung fordert damit und mit Client-ID und Client-Secret einen neuen Customer Token an. | Langlebig und verschlüsselt im getrennten Token-Speicher, einer konkreten Bankverbindung zugeordnet. Bei erfolgreicher Erneuerung ersetzt der neue Refresh Token den bisherigen. Parallele Erneuerungen derselben Verbindung werden serialisiert. |
| Customer Token | Die Bankanbindung ruft damit Kontodaten zusammen mit der Consent-ID ab und führt die vorgesehenen Zahlungsaufrufe aus. | Kurzzeitig im Arbeitsspeicher der Bankanbindung, laut Spezifikation etwa 30 Minuten gültig. Kontoverwaltung und Zahlungsverwaltung erhalten nur die fachlichen API-Ergebnisse. |

Die Consent-ID gehört zu den Verbindungsdaten. `scaRedirect` führt den Browser zur Bank, und der zufällige `state` ordnet die Rückkehr dem ursprünglichen FinSec-Vorgang zu.

## 1.2 Segmentation and Least Privilege

Die Datenbereiche folgen den Zugriffsrechten der Komponenten. Sie können technisch als getrennte Bereiche einer Datenbank mit eigenen Dienstrollen umgesetzt werden. Anfragen von Kund:innen werden zusätzlich auf die eigene Nutzer-ID und die zugeordnete Bankverbindung eingeschränkt.

| Datenbereich | Inhalt und Zugriff |
| --- | --- |
| FinSec-Nutzerdaten | Nutzer-ID, E-Mail und ggf. Profil. Die Authentifizierung verwaltet die Login-Zuordnung. Fachkomponenten erhalten die geprüfte Nutzer-ID. |
| FinSec-Authentifizierung | Passworthashes und Sitzungsdaten. Die Authentifizierung prüft das beim Login eingegebene Passwort und stellt die Sitzung aus. Das Frontend verwendet den Sitzungsnachweis. Die Fachkomponenten prüfen im Backend, ob die Sitzung und die fachliche Berechtigung für den jeweiligen Vorgang vorliegen. |
| Bankverbindungen und Einwilligungen | Nutzer-ID, Bank, Konto- bzw. Ressourcen-ID, Consent-ID und Einwilligungsstatus. Die Kontoverwaltung pflegt die Zuordnung. Die Zahlungsverwaltung liest die benötigte Zuordnung für das Zahlungskonto. Die Bankanbindung erhält die geprüften Verbindungsdaten für den jeweiligen Aufruf. |
| Finanzdaten | Kontostände und Transaktionen. Die Kontoverwaltung liest und schreibt sie. Die Finanzdatenverarbeitung liest nur die für die Auswertung freigegebenen Daten. |
| Zahlungsdaten | Zahlungskonto, Empfänger-IBAN, Betrag, Währung, Zahlungs-ID und Status. Die Zahlungsverwaltung liest und schreibt sie. Die Bankanbindung erhält die Daten, die der konkrete Bankaufruf benötigt. |
| Analyseergebnisse | Klassifikationen, Auswertungen und Sparhinweise. Die Finanzdatenverarbeitung erstellt sie und liefert der Oberfläche nur die Ergebnisse des angemeldeten Nutzers. |
| Bank-API-Zugangsmittel | Die Bankanbindung allein erhält Zugriff auf die TPP-Konfiguration und den Token-Speicher. Fachkomponenten rufen bei ihr getrennte Operationen für Kontodaten und Zahlungen auf. EuroTrust erlaubt mit demselben Customer Token beide Arten von Aufrufen. Die Trennung dieser Rechte wird daher innerhalb von FinSec durchgesetzt. |

**Vorteile.** Ein kompromittierter Analysedienst hat über seine Rolle keinen Zugriff auf Refresh Tokens, Passworthashes oder Zahlungsaufträge. Fehler in der Kontoverwaltung eröffnen über deren Schnittstelle keine Zahlungsoperationen.

**Nachteile.** Mehr Dienstrollen und Schnittstellen erhöhen Konfigurations- und Testaufwand. Bei Änderungen an Bankverbindungen oder Token-Rotation müssen Einwilligung, Zuordnung und Token-Speicher konsistent bleiben.

## 1.2 Fail Secure

Die funktionale Architektur sieht Sitzungs- und Berechtigungsprüfungen vor. In der Sicherheitsarchitektur wird ihr Ergebnis zur Voraussetzung für den Bankaufruf. Kontoverwaltung und Zahlungsverwaltung prüfen die gültige Sitzung und Kontozuordnung. Die Bankanbindung prüft die Berechtigung der aufrufenden Komponente für die konkrete Operation. Fehlt eine Voraussetzung oder schlägt die Prüfung fehl, wird die Anfrage abgelehnt.

Vor einer SCA-Weiterleitung bindet FinSec einen zufälligen, kurzlebigen `state` serverseitig an die Sitzung und die konkrete Verknüpfung oder Zahlung. Der Callback prüft diese Bindung und verbraucht den Vorgang einmalig, bevor er den Authorization Code weitergibt. Bei fehlendem, falschem, abgelaufenem oder bereits verwendetem `state` endet der Vorgang ohne Code-Austausch oder Übernahme neuer Tokens. Zahlungen mit unbekanntem Bankstatus bleiben ungeklärt. FinSec fragt bei vorhandener Zahlungs-ID den Status ab und zeigt eine erfolgreiche Zahlung erst nach bestätigtem Bankstatus an. Bei unklarem Ausgang löst FinSec die Zahlung nicht automatisch erneut aus.

**Vorteile.** Eine falsche Callback-Zuordnung kann keine Tokens mit einem anderen FinSec-Konto verknüpfen. Bei einem Timeout verhindert die Statusabfrage, dass FinSec vorschnell Erfolg meldet oder dieselbe Zahlung erneut auslöst.

**Nachteile.** Sind Sitzungsprüfung, Vorgangsspeicher oder Bank zeitweise unerreichbar, können auch berechtigte Vorgänge abgebrochen werden oder ungeklärt bleiben. Abgelaufene Freigaben müssen neu gestartet werden. Für ungeklärte Zahlungen braucht die Oberfläche eine verständliche Statusanzeige.

Grundlagen sind [Übung 3](Aufgabenblätter/Uebung_3_Design_Principles.pdf) und die [EuroTrust-API-Spezifikation, Abschnitte 3 bis 5](Aufgabenblätter/FinSec_Banking_API_for_Students_EN.pdf).
