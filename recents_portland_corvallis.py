import pycraigslist, sched, time
from prettytable import PrettyTable

free_portland = pycraigslist.forsale.zip(site="portland")

queue_length = 20

data = []

s = sched.scheduler(time.time, time.sleep)
p = PrettyTable()
p.field_names = ["Title", "City", "Neighborhood", "Updated"]

def run_search():
	for free in free_portland.search(limit=queue_length):
		p.add_row([free["title"],free["site"],free["neighborhood"],free["last_updated"]])
	p.align = "l"
	print(p)
	p.clear_rows()
	s.enter(60,1,run_search)
run_search()
s.enter(60,1,run_search)
s.run()