from database.DB_connect import DBConnect
from model.retailers import Retailers


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_years():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct YEAR(date) as year  from go_daily_sales ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_countries():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinct country
                    from go_retailers 
                    order by country asc"""

        cursor.execute(query)

        for row in cursor:
            results.append(row["country"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_nodes( country ):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
                   from go_retailers
                   where country = "%s" """

        cursor.execute(query,(country,))

        for row in cursor:
            results.append(Retailers(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_edges(year,country, idMap):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select r1.retailer_code as ret1, r2.retailer_code as ret2, count(*) as weight
                    from go_retailers as r1, go_retailers as r2, go_daily_sales as s1, go_daily_sales as s2
                    where r1.country = "%s"
                    and r1.country = r2.Country
                    and YEAR(s1.date ) = %s
                    and year(s2.date) = year(s2.date)
                    and r1.retailer_code = s1.Retailer_code 
                    and r2.retailer_code = s2.Retailer_code
                    and r1.Retailer_code < r2.Retailer_code
                    and s1.Product_number = s2.Product_number
                    group by ret1, ret2 
                    order by ret1 asc"""

        cursor.execute(query, (country , year,))

        for row in cursor:
            results.append((idMap[row["ret1"]], idMap[row["ret2"]], row["weight"]))

        cursor.close()
        conn.close()
        return results


