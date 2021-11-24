# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import sqlite3

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionSimpanNama(Action):

    def name(self) -> Text:
        return "action_simpan_nama"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connect = sqlite3.connect('example.db')

        prediction = tracker.latest_message
        entity = prediction['entities']
        nama = ""

        for x in entity:
            if x['entity'] == 'nama':
                nama = x['value']

        mycursor = connect.cursor()

        sql = "INSERT INTO pengguna (nama) VALUES (?)"
        mycursor.execute(sql, (nama,))
        connect.commit()

        dispatcher.utter_message(text="Data berhasil disimpan!")

        return []

class ActionAmbilNama(Action):

    def name(self) -> Text:
        return "action_ambil_nama"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connect = sqlite3.connect('example.db')

        mycursor = connect.cursor()
        mycursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pengguna'");
        
        if (len(mycursor.fetchall()) == 0):
            mycursor.execute("CREATE TABLE pengguna (nama text)")
            connect.commit()

        mycursor.execute("SELECT nama FROM pengguna")
        myresult = mycursor.fetchall()
        nama = "".join(myresult[-1])

        dispatcher.utter_message(
            template="utter_jawabnama",
            nama=nama
        )

        return []