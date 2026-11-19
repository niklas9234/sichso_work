# 2.1 Security Impact Analysis

## Schritt 1: Drei schützenswerte Assets

| ID | Asset | Warum schützenswert? |
| --- | --- | --- |
| A1 | FinSec-Benutzerkonten mit Anmeldedaten und Berechtigungen | Sie bestimmen, wer auf ein Konto und dessen Funktionen zugreifen darf. |
| A2 | Finanzdaten: Kontostände und Transaktionshistorie | Sie enthalten private Informationen und bilden die Grundlage für Auswertungen. |
| A3 | Zahlungsaufträge | Manipulierte oder unberechtigte Aufträge können einen finanziellen Schaden verursachen. |

## Schritte 2 und 3: Misuse Cases und Schaden

| STRIDE-Bedrohung / verletztes Schutzziel | Asset | Misuse Case | Schadensklasse und Begründung |
| --- | --- | --- | --- |
| **S – Spoofing / Authentizität** | A1 | Ein Angreifer meldet sich mit gestohlenen Zugangsdaten als ein anderer Nutzer bei FinSec an. | **High:** Übernahme eines Benutzerkontos mit Zugriff auf dessen Finanzdaten und Funktionen. |
| **T – Tampering / Integrität** | A3 | Ein Angreifer verändert bei einem einzelnen Zahlungsauftrag die Empfänger-IBAN. Dadurch werden 100 € an den falschen Empfänger überwiesen; der Betrag kann zurückgeholt werden. | **Medium:** Einzelne unberechtigte Aktion und begrenzter, wiederherstellbarer finanzieller Schaden. |
| **R – Repudiation / Nachweisbarkeit** | A3 | Ein Nutzer bestreitet einen von ihm ausgelösten Zahlungsauftrag. Ohne verlässliche Aufzeichnung kann FinSec den Auftrag nicht zuordnen und erstattet die Zahlung irrtümlich. | **Medium:** Begrenzter finanzieller Verlust durch einen einzelnen strittigen Auftrag. |
| **I – Information Disclosure / Vertraulichkeit** | A2 | Ein Angreifer liest über einen ungeschützten Datenzugriff die Transaktionshistorien mehrerer Nutzer aus. | **High:** Offenlegung sensibler Finanzdaten mehrerer Konten. |
| **D – Denial of Service / Verfügbarkeit** | A2 | Ein Angreifer überlastet die Auswertungsfunktion. Die Ausgabenübersicht ist kurzzeitig nicht verfügbar; gespeicherte Daten und Zahlungsfunktionen bleiben verfügbar. | **Low:** Vorübergehende Unannehmlichkeit ohne finanziellen Verlust oder Datenoffenlegung; schnelle Wiederherstellung. |
| **E – Elevation of Privilege / Autorisierung** | A1 | Ein normaler Nutzer erhält durch eine fehlende Rechteprüfung Verwaltungsrechte und kann fremde Benutzerkonten übernehmen. | **High:** Übernahme mehrerer Konten und Zugriff auf fremde Finanzdaten. |

## Schritt 4: Sicherheitsziele ab Schadensklasse Medium

| Bezug | Sicherheitsziel |
| --- | --- |
| S | FinSec muss die Identität des Nutzers vor dem Kontozugriff zuverlässig prüfen und Sitzungen gegen Übernahme schützen. |
| T | Empfänger und Betrag eines Zahlungsauftrags müssen unverändert der vom Nutzer freigegebenen Zahlung entsprechen. Eine Änderung muss eine erneute Freigabe erfordern. |
| R | FinSec muss Zahlungsaufträge mit Nutzerzuordnung, Zeitpunkt, Auftragsdaten und Freigabestatus nachvollziehbar und gegen nachträgliche Veränderung geschützt aufzeichnen. |
| I | Finanzdaten dürfen nur vom jeweils berechtigten Nutzer und den für die Verarbeitung benötigten FinSec-Komponenten gelesen werden. |
| E | FinSec muss Berechtigungen im Backend prüfen und verhindern, dass Nutzer ihre Rechte selbst erweitern oder fremde Konten verwalten. |
