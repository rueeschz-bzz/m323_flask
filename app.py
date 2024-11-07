from flask import Flask, jsonify, request
from dataclasses import dataclass, field
from typing import List, Dict, Callable

app = Flask(__name__)

# Definition einer unveränderlichen Klasse für Event-Optionen
@dataclass(frozen=True)
class EventOption:
    name: str
    cost: float

# Unveränderliche Event-Optionen
basic_option = EventOption(name="Standard", cost=0.0)
premium_option = EventOption(name="Premium", cost=25.0)

# Pure function zur Berechnung der Gesamtkosten
def calculate_total_cost(participants: int, options: List[EventOption]) -> float:
    """Berechnet die Gesamtkosten basierend auf Teilnehmerzahl und Event-Optionen."""
    base_cost = participants * 20  # Basispreis pro Teilnehmer
    options_cost = sum(option.cost for option in options)  # Zusatzoptionen summieren
    return base_cost + options_cost

# Lambda-Funktion zum Erhöhen der Teilnehmerzahl
increase_participant = lambda participants, increment: participants + increment

# Funktion zum Filtern der Premium-Optionen
filter_premium_options = lambda options: list(filter(lambda x: x.cost > 10, options))

# Map-Funktion zur Umwandlung von Event-Optionen in String-Darstellung
map_option_names = lambda options: list(map(lambda x: x.name, options))

# Beispiel-Daten für Teilnehmer und Event-Optionen
participants = 100
selected_options = [basic_option, premium_option]

@app.route('/')
def index():
    return "Willkommen im Event-Planungstool!"

@app.route('/total_cost', methods=['GET'])
def total_cost():
    """Berechnet die Gesamtkosten basierend auf den Event-Optionen und der Teilnehmerzahl."""
    total = calculate_total_cost(participants, selected_options)
    return jsonify({"total_cost": total})

@app.route('/increase_participants', methods=['POST'])
def increase_participants_view():
    """Erhöht die Teilnehmerzahl und gibt die neue Zahl zurück."""
    increment = request.json.get("increment", 1)  # Standardwert für Erhöhung ist 1
    global participants
    participants = increase_participant(participants, increment)
    return jsonify({"new_participants": participants})

@app.route('/filter_options', methods=['GET'])
def filter_options_view():
    """Filtert Event-Optionen basierend auf dem Preis und gibt nur Premium-Optionen zurück."""
    premium_options = filter_premium_options(selected_options)
    return jsonify({"premium_options": [option.name for option in premium_options]})

@app.route('/map_option_names', methods=['GET'])
def map_options_view():
    """Mappt Event-Optionen auf ihre Namen und gibt sie zurück."""
    option_names = map_option_names(selected_options)
    return jsonify({"option_names": option_names})

if __name__ == '__main__':
    app.run(debug=True)
