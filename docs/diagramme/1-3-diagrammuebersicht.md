# Architektur und Diagramme

| Ebene | Diagramm | Aufgabe |
| --- | --- | --- |
| Systemkontext | [Übersicht im System-Context-README](../1.1-1.2-README.md) | Übung 1. Zeigt die FinSec-Systemgrenze, externe Beteiligte und Datenflüsse. |
| Funktionale Architektur | [Grunddiagramm und Erläuterung](../2.4-functional-architecture.md) | Übung 2. Zeigt die Komponenten innerhalb von FinSec und ihre Schnittstellen. |
| Sicherheitsarchitektur | [Sicherheitsansicht in der Discussion](../3.1-design-principles-discussion.md#nachher--sicherheitsarchitektur) | Übung 3. Verfeinert das Grunddiagramm mit Datenbankrechten und EuroTrust-Zugangsmitteln. |
| Vorher/Nachher | [Design Principles Discussion](../3.1-design-principles-discussion.md) | Zeigt beide Architekturstände nebeneinander im selben Dokument und begründet die Änderungen. |

Die Sequenzdiagramme zeigen den zeitlichen Ablauf konkreter Anwendungsfälle derselben Architektur. [Konto verknüpfen](../2.3-user-account-link.md) · [Kontostand abrufen](../2.3-user-balance.md) · [Überweisen](../2.3-user-transfer.md)

## Architekturdiagramme pflegen

`2.4-functional-architecture.dot` ist die Quelle für das Grunddiagramm, `3.1-security-architecture.dot` für seine Sicherheitsverfeinerung. Beide verwenden dieselben Komponenten und Schnittstellen. Bei einer Änderung der gemeinsamen Architektur beide DOT-Dateien prüfen. Die Markdown-Dokumente binden dieselben SVG-Dateien ein.

Die SVGs lassen sich im Browser direkt öffnen und mit der Browser-Tastatursteuerung vergrößern. Die Begleittexte beschreiben die wesentlichen Verbindungen und Zugriffsrechte auch ohne Grafik.

Aus dem Repository-Stamm mit Graphviz erzeugen:

```bash
dot -Tsvg docs/diagramme/1.1-system-context.dot -o docs/diagramme/1.1-system-context.svg
dot -Tsvg docs/diagramme/2.4-functional-architecture.dot -o docs/diagramme/2.4-functional-architecture.svg
dot -Tsvg docs/diagramme/3.1-security-architecture.dot -o docs/diagramme/3.1-security-architecture.svg
```

Für den ursprünglichen Systemkontext liegen [DOT-Quelle](1.1-system-context.dot), [SVG](1.1-system-context.svg) und [HTML-Ansicht](../material/1.1-system-context.html) unter `docs`. Eine frühere Ausgestaltung des Systemkontexts liegt im [Archiv](archiv/1.1-system-context-variant.dot).
