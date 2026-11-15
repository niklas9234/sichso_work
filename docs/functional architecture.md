# 2.4 Funktionale Architektur

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

Die Authentifizierung liegt in beiden Teilen: Das Frontend nimmt die Anmeldung entgegen, das Backend prüft Zugangsdaten und Sitzungen. In der Datenbank werden die FinSec-Nutzerkennung und der Passworthash gespeichert. Die Bankanmeldung erfolgt bei der Bank; FinSec verwaltet dafür die erhaltenen Tokens.
