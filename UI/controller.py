import flet as ft
from flet.core.dropdown import Dropdown

from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None


    # POPOLA DROPDOWN
    # TODO

    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()
        self._view.ddmuseo.options = [ft.dropdown.Option("Nessun filtro")]
        for museo in musei:
            self._view.ddmuseo.options.append(ft.dropdown.Option(museo.nome))
        self._view.ddepoca.options = [ft.dropdown.Option("Nessun filtro")]
        for epoca in epoche:
            self._view.ddepoca.options.append(ft.dropdown.Option(epoca))
        self._view.ddepoca.value = "Nessun filtro"
        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def handler_dropdown_change_museo(self, e: ft.ControlEvent):
        self.museo_selezionato = e.control.value
        print(f"Museo selezionato: {self.museo_selezionato}")

    def handler_dropdown_change_epoca(self, e):
        self.epoca_selezionata = e.control.value
        print(f"Epoca selezionata: {self.epoca_selezionata}")

    # AZIONE: MOSTRA ARTEFATTI
    # TODO

    def mostra_artefatti(self,e):
        lista_artefatti = []
        museo = self._view.ddmuseo.value
        epoca = self._view.ddepoca.value
        artefatti = self._model.get_artefatti_filtrati(museo,epoca)

        if not artefatti:
            self._view.lista_artefatti.controls.append(ft.Text("Nessun artefatto trovato"))

        #self._view.lista_artefatti.controls.clear()
        else:
            for a in artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(a))

        self._view.update()
