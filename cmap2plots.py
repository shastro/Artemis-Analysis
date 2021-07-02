import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
import random



def create_arg_parser():
	parser = argparse.ArgumentParser(description="Tool for converting a txt file with a list of hit names to a set of plots with those hit names in a specified folder")
	parser.add_argument("cmap", help="Path to .txt file which contains only a list of hitnumbers")
	parser.add_argument("sourcedir", help="Path to folder where the waveforms data is stored")
	parser.add_argument("outdir", help="Path to output directory for waveform plots will be saved")
	parser.add_argument("rand", help="Use Random Selection of Elements with <rand> probability. 1 Says not to use rand")
	parser.add_argument("maxToGen", help="Maximum number of elements of each cluster to generate plots for")
	return parser



def parse_dense(filename, ndarray):
	with open(filename) as f:
		i = 0
		for l in f:
			if ("HIT NUMBER" in l):
				title = l
			try:
				lsplits = l.split(",")
				ndarray[i] = float(lsplits[-1].rstrip())
				i += 1
			except ValueError:
				i -= 1
				pass

		return title 


def save_plot(filename, dirname,  fig, ax):
	DSIZE = 15360
	TSTEP = 0.0000002000 #Secpnds
	waveform = np.zeros((DSIZE+1), dtype=np.float)
	time = np.arange(0, DSIZE*TSTEP, TSTEP)
	title = parse_dense(filename, waveform)

	
	fig.set_size_inches(10,6)
	ax.plot(time[0:(DSIZE//3)], waveform[0:(DSIZE//3)], linewidth=0.75)
	ax.set_xlabel("Time (s)")
	ax.set_ylabel("Voltage (v)")
	ax.set_title(title)
	f_name = dirname + "/" + title.replace(" ", "").rstrip() +".png"
	print("Saving " + f_name)
	plt.savefig(f_name, dpi=100)
	ax.clear()

def main():

	random.seed()
	filename = None
	dirname = None
	sourcedir = None

	arg_parser = create_arg_parser()
	parsed_args = arg_parser.parse_args(sys.argv[1:])


	if os.path.exists(parsed_args.cmap):
		filename = parsed_args.cmap
	if os.path.exists(parsed_args.sourcedir):
		sourcedir = parsed_args.sourcedir
	if os.path.exists(parsed_args.outdir):
		dirname = parsed_args.outdir	

	useRand = float(parsed_args.rand)
	maxToGen = int(parsed_args.maxToGen)

	if(maxToGen == -1):
		maxToGen = 1000000000

	f = open(filename)
	hits = []
	for l in f:
		hits.append(int(l))

	fig, ax = plt.subplots(1)

	hitTotal = 0
	hitNum = 0
	for fname in os.listdir(sourcedir):
		# splits = fname.split("_")
		# hit_num = int(splits[2])
		if hitNum in hits:
			p = random.random()
			if (p <= useRand):
				if(hitTotal < maxToGen):
					save_plot(sourcedir + fname, dirname, fig, ax)
					hitTotal += 1
					print(hitTotal)
		hitNum += 1

	#Constants

	# plt.show()

if __name__ == "__main__":
	main()
