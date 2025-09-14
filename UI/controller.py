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
        years, countries = self._model.fillDD()
        self._view.ddyear.options = [
            ft.dropdown.Option(key=str(anno), text=str(anno)) for anno in years
        ]
        self._view.ddcountry.options = [
            ft.dropdown.Option(key=c, text=c) for c in countries
        ]
        self._view.ddyear.value = None
        self._view.ddcountry.value = None
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
        volume = self._model.get_volume()  # correggi nome variabile
        self._view.txtOut2.controls.clear()  # pulisci l’area corretta
        volume2 = sorted(volume.items(), key=lambda item: item[1], reverse=True)
        for nodo, vol in volume2:  # ottieni nodo e volume
            self._view.txtOut2.controls.append(
                ft.Text(f"nodo {nodo}  volume totale {vol}")
            )
        self._view.update_page()


    def handle_path(self, e):
        N = self._view.txtN.value
        pesoM, cammino = self._model.get_cammino(N)
        self._view.txtOut3.controls.clear()
        self._view.txtOut3.controls.append(ft.Text(f"peso massimo {pesoM}"))
        for c in cammino :
            self._view.txtOut3.controls.append(ft.Text(f"{c}"))
        self._view.update_page()
