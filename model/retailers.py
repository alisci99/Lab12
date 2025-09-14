from dataclasses import dataclass
import datetime
@dataclass
class Retailers:

    Retailer_code:int
    Retailer_name : str
    Type : str
    Country : str

    def __hash__(self):
        return hash(self.Retailer_code)

    def __str__(self):
        return f"{self.Retailer_code} , {self.Retailer_name}"

    def __eq__(self, other):
        return self.Retailer_code== other.Retailer_code

    def __repr__(self):
        return self.__str__()