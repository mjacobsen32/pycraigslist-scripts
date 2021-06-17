import argparse
class Args:
    def __init__(self):
        parser = argparse.ArgumentParser(description="input for search")
        parser.add_argument('--site',nargs='+',help="list sites to search from",)
        parser.add_argument('--size',help="size of queue storing recent items")
        self.args = parser.parse_args()
    def get_sites(self):
        return(self.args.site)
    def get_size(self):
        return(self.args.size)