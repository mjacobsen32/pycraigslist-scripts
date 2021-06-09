import pycraigslist, sched, time, sys
from prettytable import PrettyTable

#Color
R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset

queue_length = 58

data = []

s = sched.scheduler(time.time, time.sleep)
p = PrettyTable()
p.field_names = ["Title", "City", "Neighborhood", "Updated"]

def run_search():
	free_portland = pycraigslist.forsale.zip(site="corvallis")
	for free in free_portland.search(limit=queue_length):
		p.add_row([G+str(free["title"])+N,B+str(free["site"])+N,Y+str(free["neighborhood"])+N,R+str(free["last_updated"])+N])
	p.align = "l"
	print(p)
	p.clear_rows()
	s.enter(60,1,run_search)
run_search()
s.enter(60,1,run_search)
s.run()
