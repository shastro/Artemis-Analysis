import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse



def create_arg_parser():
	parser = argparse.ArgumentParser(description="Tool for converting a txt file with a list of hit names to a set of plots with those hit names in a specified folder")
	parser.add_argument("cmap", help="Path to .txt file which contains only a list of hitnumbers")
	parser.add_argument("sourcedir", help="Path to folder where the waveforms data is stored")
	parser.add_argument("outdir", help="Path to output directory for waveform plots will be saved")
	return parser



def parse_dense(filename, ndarray):
	with open(filename) as f:
		i = 0
		for l in f:
			if ("HIT NUMBER" in l):
				title = l
			try:
				ndarray[i] = float(l.rstrip())
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


	f = open(filename)
	hits = []
	for l in f:
		hits.append(int(l))

	fig, ax = plt.subplots(1)
	for fname in os.listdir(sourcedir):
		splits = fname.split("_")
		hit_num = int(splits[2])
		if hit_num in hits:
			save_plot(sourcedir + fname, dirname, fig, ax)

	#Constants

	# plt.show()

if __name__ == "__main__":
	main()
