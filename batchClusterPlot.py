import os
import subprocess

for clusterFname in os.listdir("wtaClusterMaps"):
	process = subprocess.run(['python3', 'cmap2plots.py', f'./wtaClusterMaps/{clusterFname}', "/mnt/Art_Wind_Tunnel/WTA_3_18_21_25Hz_10min/WTA_3_18_21_25Hz_10min_WFs/", f"./wtaClusterWavePlots/{clusterFname[:-4]}", "0.5", "1000"])
	