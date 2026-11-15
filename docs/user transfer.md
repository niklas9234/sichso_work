# 2.3 Sequenzdiagramm – 100 € überweisen

**Voraussetzung:** Der Nutzer ist bei FinSec angemeldet und ein gültiger Customer Token ist vorhanden. Die Überweisung benötigt einen SCARedirect zur starken Kundenauthentifizierung bei der Bank.

```mermaid
sequenceDiagram
    actor U as Nutzer
    participant F as FinSec-Frontend
    participant B as FinSec-Backend
    participant E as EuroTrust Bank

    U->>F: Zahlungskonto, Empfänger und 100 EUR eingeben
    F->>B: Überweisungsauftrag mit Zahlungskonto, Empfänger-IBAN, 100 EUR
    B->>B: Sitzung, Kontoberechtigung und Auftragsdaten prüfen
    B->>E: POST /payments/sepa-credit-transfers<br/>Customer Token, Zahlungskonto, Empfänger-IBAN, 100 EUR
    E-->>B: paymentId und scaRedirect
    B->>B: Zufälligen state erzeugen und an Sitzung und Auftrag binden
    B-->>F: scaRedirect mit state
    F-->>U: Browser zur Bankfreigabe weiterleiten
    U->>E: GET /sca/authorize<br/>über scaRedirect mit state
    E-->>U: Zahlungsdaten und SCA-Seite anzeigen
    U->>E: POST /sca/authorize<br/>Bank-Benutzername, Passwort, sechsstelliger TOTP, Zahlung freigeben
    E-->>U: Redirect zur registrierten FinSec-Rückkehr-URL<br/>Authorization Code und state
    U->>B: Rückkehr-URL aufrufen (Code, state)
    B->>B: state mit Sitzung und Auftrag abgleichen, bei Abweichung abbrechen
    B->>E: POST /oauth/token<br/>grant_type=authorization_code, Code, client_id, client_secret
    E-->>B: Customer Token, Customer Refresh Token und Consent-ID
    B->>B: Tokens und Consent-ID der Bankverbindung aktualisieren
    B->>E: GET /payments/{paymentId}/status<br/>Customer Token
    E-->>B: Aktueller Zahlungsstatus
    B-->>F: Von der Bank bestätigten Zahlungsstatus übermitteln
    F-->>U: Zahlungsstatus anzeigen
```

**Zugangsdaten und Daten:** Der vorhandene Customer Token wird für den Zahlungsauftrag genutzt. Die Zahlung enthält das Zahlungskonto, die Empfänger-IBAN und 100 EUR. Bank-Anmeldedaten und TOTP gehen nur an die Bank. Client-ID und Client-Secret werden nur beim Token-Austausch verwendet; Bank-Tokens bleiben im Backend. FinSec liest den Zahlungsstatus bei der Bank aus, statt die Rückleitung allein als erfolgreiche Zahlung zu behandeln.

**Quelle:** EuroTrust Bank — API Guide, Abschnitte 4–6. Abschnitt 4 beschreibt die Rückkehr mit Code und state sowie den Token-Austausch auch für SCA-pflichtige Zahlungen. Der Ablauf übernimmt diese Schritte. Die Ausnahme für Kleinbeträge unter 30 € greift bei 100 € nicht.
