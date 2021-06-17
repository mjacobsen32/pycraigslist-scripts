import sched, time
from helpers.search_class import Search
from helpers.args import Args

def run(sites,repeater):
	for site in sites:
		s = Search(site,queue)
		r = s.run_search()
		s.print(r)
	repeater.enter(60,1,run)
	

if __name__ == "__main__":
	repeater = sched.scheduler(time.time, time.sleep)
	a = Args()
	queue = a.get_size()
	sites = a.get_sites()
	run(sites,repeater)
	repeater.run()