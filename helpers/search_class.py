import pycraigslist
from prettytable import PrettyTable
from helpers.colors import Colors

class Search:
    def __init__(self,site,queue):
        self.site = site
        self.limit = int(queue)
    def run_search(self):
        search_criteria = pycraigslist.forsale.zip(site=self.site)
        return(search_criteria.search(limit=self.limit))
    def print(self,results):
        p = PrettyTable()
        c = Colors()
        p.field_names = ["Title", "City", "Neighborhood", "Updated"]
        for r in results:
            p.add_row([c.G+str(r["title"])+c.N,c.B+str(r["site"])+c.N,c.Y+str(r["neighborhood"])+c.N,c.R+str(r["last_updated"])+c.N])
        p.align = "l"
        print(p)
        p.clear_rows()
