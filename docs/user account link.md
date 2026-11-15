# 2.3 Sequenzdiagramm – Bankkonto verknüpfen

**Voraussetzung:** Der Nutzer ist bei FinSec angemeldet. FinSec besitzt nur die Client-ID und das Client-Secret, noch keine Bank-Tokens.

```mermaid
sequenceDiagram
    actor U as Nutzer
    participant F as FinSec-Frontend
    participant B as FinSec-Backend
    participant E as EuroTrust Bank

    U->>F: EuroTrust-Konto verknüpfen
    F->>B: Verknüpfung für angemeldeten FinSec-Nutzer starten
    B->>E: POST /oauth/token<br/>grant_type=client_credentials, client_id, client_secret
    E-->>B: Company Token
    B->>E: POST /consents<br/>Company Token, gewünschter Kontozugriff
    E-->>B: Consent-ID und scaRedirect
    B->>B: Zufälligen state erzeugen und an Nutzersitzung binden
    B-->>F: scaRedirect mit state
    F-->>U: Browser zur Bank weiterleiten
    U->>E: GET /sca/authorize<br/>über scaRedirect mit state
    E-->>U: Bankseitige Anmeldung und Freigabe anzeigen
    U->>E: POST /sca/authorize<br/>Bank-Benutzername, Passwort, sechsstelliger TOTP, Kontozugriff freigeben
    E-->>U: Redirect zur registrierten FinSec-Rückkehr-URL<br/>Authorization Code und state
    U->>B: Rückkehr-URL aufrufen (Code, state)
    B->>B: state mit Nutzersitzung abgleichen, bei Abweichung abbrechen
    B->>E: POST /oauth/token<br/>grant_type=authorization_code, Code, client_id, client_secret
    E-->>B: Customer Token, Customer Refresh Token und Consent-ID
    B->>B: Bankverbindung, Consent-ID und Tokens dem FinSec-Nutzer zuordnen und speichern
    B-->>F: Konto verknüpft
    F-->>U: Erfolgreiche Verknüpfung anzeigen
```

**Zugangsdaten und Daten:** Client-ID und Client-Secret gehen nur an `/oauth/token`; der Company Token dient zum Anlegen des Consents. Bank-Benutzername, Passwort und TOTP gehen direkt an die Bank. FinSec erhält anschließend die kundenbezogenen Tokens und die Consent-ID. Tokens und Client-Secret bleiben im Backend.

**Quelle:** EuroTrust Bank — API Guide, Abschnitte 3–6. Der Guide nennt keine vollständigen Request-Formate; die Beschriftungen geben die benötigten Informationen an.
