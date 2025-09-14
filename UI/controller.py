import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        years, countries= self._model.fillDD()
        for anno in years:
            self._view.ddyear.options = [ft.dropdown.Option(str(anno)) for anno in years]
        for c in countries :
            self._view.ddcountry.options = [ft.dropdown.Option(str(c)) for c in countries]
        self._view.update_page()


    def handle_graph(self, e):
        country = self._view.ddcountry.value
        year = self._view.ddyear.value
        self._model.crea_grafo(year, country)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("grafo creato con succeso!"))
        nNodi,nArchi = self._model.get_graph_details()
        self._view.txt_result.controls.append(ft.Text(f"numero di nodi : {nNodi}  , numero di archi {nArchi}"))
        self._view.update_page()



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
