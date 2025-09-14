from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def fillDD(self):
        anni= DAO.get_years()
        countries = DAO.get_countries()
        return anni, countries