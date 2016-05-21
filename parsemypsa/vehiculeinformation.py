#!/usr/bin/env python

from peewee import *


sqlite_db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = sqlite_db

class VehiculeInformation(BaseModel):
    updatedon = IntegerField()
    mileage = IntegerField()
    endlatitude = DoubleField()
    endlongitude = DoubleField()
    destlatitude = DoubleField()
    destlongitude = DoubleField()
    distancetonextmaintenance = IntegerField()
    daysuntilnextmaintenance = IntegerField()
    maintenancepassed = IntegerField()
    fuellevel = FloatField()
    fuelautonomy = IntegerField()
    endpositionaddrtext = CharField()
    destinationpositionaddrtext = CharField()
    #alerts


def create_tables():
    sqlite_db.connect()
    sqlite_db.create_tables([Alert], True)

class Alert(BaseModel):
    id = SmallIntegerField()
    date = IntegerField()
    is_solved = SmallIntegerField(null=True)


alert_mapping = {
    10: "Front left door open",
    11: "Porte avant droite ouverte",
    12: "Porte arrière gauche ouverte",
    13: "Porte arrière droite ouverte",
    15: "Coffre ouvert",
    22: "Niveau carburant faible",
    39: "Batterie faible",
    107: "Risque de verglas",
    108: "Porte avant droite ouverte(à l'arrêt, moteur en marche)",
    109: "Porte avant gauche ouverte(à l'arrêt, moteur en marche)",
    110: "Porte arrière droite ouverte(à l'arrêt, moteur en marche)",
    111: "Porte arrière gauche ouverte(à l'arrêt, moteur en marche)",
    112: "Coffre ouvert(à l'arrêt, moteur en marche)",
    125: "Défaut système freinage automatique",
    141: "Défaut moteur: faites réparer le véhicule"
}