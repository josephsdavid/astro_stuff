import spectraldata as nasa
from pprint import pprint
import numpy as np
import sys
import molecules as m
from itertools import chain
import setcover as sc
import os
import joblib

stdout = sys.stdout

# molecules = m.construct_mega_query
PATH = "Titan/Titan/"
files = [f"{PATH}{f}" for f in os.listdir(PATH)]

pp = "Titan/Titan/Win0.clean1.contsub_Jy.rest.scom.c.txt"
data = nasa.read(nasa.SpectralFile(pp))
spikes = nasa.identify_spikes(data)
import joblib; joblib.dump(spikes._asdict(), "parteespike.pkl")
molecules = m.get_molecules_from_spikes(spikes)
cover = sc.SetCovering(spikes, molecules)
joblib.dump(cover.spike_dict, "partee_spike_dict.pkl")
joblib.dump(cover.likeliest_molecules(), "partee_likely_mols.pkl")
joblib.dump(cover.plot_dict, "plot_dict.py")
import pdb; pdb.set_trace()  # XXX BREAKPOINT

for f in files:
    data = nasa.read(nasa.SpectralFile(f))
    spikes = nasa.identify_spikes(data)
    molecules = m.get_molecules_from_spikes(spikes)
    cover = sc.SetCovering(spikes, molecules)
    print("writing results")
    with open("results.txt", 'a') as fi:
        sys.stdout = fi
        print("*"*80, flush=True)
        print(f"Processing: {f}")
        print()
        mols = cover.likeliest_molecules()
        for idx, mol in enumerate(mols[:30]):
            print(f"{idx}. {mol[0]} \t score: {mol[1]}")
    sys.stdout = stdout


