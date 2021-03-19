import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def main():
	filename = ''

	if (len(sys.argv) != 2):
		print("usage: python3 filename")
		exit()
	else:
		filename = sys.argv[1]

	#Constants
	DSIZE = 15360
	TSTEP = 0.0000002000 #Secpnds
	waveform = np.zeros((DSIZE+1), dtype=np.float)
	time = np.arange(0, DSIZE*TSTEP, TSTEP)


	



	fig, ax = plt.subplots(1)
	fig.set_size_inches(10,6)
	ax.plot(time[0:(DSIZE//3)], waveform[0:(DSIZE//3)], linewidth=0.75)
	ax.set_xlabel("Time (s)")
	ax.set_ylabel("Voltage (v)")
	ax.set_title(title)
	print("./images/" + filename[7:-4]+".png")
	# plt.savefig("./images/" + filename[7:-4]+".png", dpi=250)
	plt.show()

if __name__ == "__main__":
	main()
