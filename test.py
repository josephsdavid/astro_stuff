import scratch as nasa
import molecules as m
import os

molecules = m.construct_mega_query

for f in os.listdir("Titan/Titan/"):
    sf = nasa.SpectralFile(f"Titan/Titan/{f}")
    sd = nasa.read(sf)
    sd = nasa.convert_units(sd, 'GHz')
    sd_stats = nasa.get_stats(sd)
    print(sd_stats)
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    nasa.plot_spikes(nasa.identify_spikes(sd))
    # use these spikes + splatalogue to query JPL
    # given that that works, figure out optimal choice

import pdb; pdb.set_trace()  # XXX BREAKPOINT

sf = nasa.SpectralFile(f"Titan/Titan/Win0.clean1.contsub_Jy.rest.scom.c.txt")
sd = nasa.read(sf)

print()

