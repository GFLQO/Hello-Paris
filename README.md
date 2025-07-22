# Hello-Paris Home Assistant Interface

Ce dépôt contient une petite application Flask pouvant servir d'interface simple pour piloter des appareils connectés à un Raspberry Pi.

## Installation

Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Lancez l'application :

```bash
python app.py
```

Ouvrez ensuite votre navigateur sur `http://adresse-ip-du-pi:5000` pour accéder à l'interface.

Par défaut deux appareils fictifs sont déclarés (`light` et `fan`). Sur un Raspberry Pi, ils utiliseront les pins GPIO 17 et 27 via `gpiozero`. Sur une autre plateforme, des objets factices sont utilisés pour permettre des tests sans matériel.
