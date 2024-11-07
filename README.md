Event-Planungstool

Eine Flask-Anwendung zur Event-Planung, die funktionale Programmierung nutzt. Sie berechnet Gesamtkosten, erhöht die Teilnehmerzahl und filtert Event-Optionen.
Features

    Berechnung der Gesamtkosten für ein Event.
    Teilnehmerzahl erhöhen.
    Filterung von Premium-Event-Optionen.
    Umwandlung von Event-Optionen in Namen.

Installation

    Klone das Repository:

git clone https://github.com/rueeschz-bzz/m323_flask

Installiere Flask:

pip install flask

Starte die Anwendung:

    python app.py

API-Endpunkte

    GET /total_cost: Berechnet und gibt die Gesamtkosten zurück.
    POST /increase_participants: Erhöht die Teilnehmerzahl.
    GET /filter_options: Gibt Premium-Optionen zurück.
    GET /map_option_names: Gibt die Namen der Event-Optionen zurück.