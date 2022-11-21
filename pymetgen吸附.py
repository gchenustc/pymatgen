# from pymatgen.core import structure
# from pymatgen import Lattice, MPRester, Molecule
# from pymatgen.analysis.adsorption import *
# from pymatgen.core.surface import generate_all_slabs
# from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
# from matplotlib import pyplot as plt
# from pymatgen.ext.matproj import MPRester
# from pymatgen.io.vasp.inputs import Poscar
# print(dir(structure))

# from_spacegroup(199, Lattice.cubic(3.765), ["N"], [[0.085, 0.085, 0.085]])

# slabs = generate_all_slabs(fcc_ni, max_index=1, min_slab_size=6.0, min_vacuum_size=15.0)
# cgN_100 = [slab for slab in slabs if slab.miller_index==(1,0,0)][0]

# asf_ni_111 = AdsorbateSiteFinder(ni_111)
# ads_sites = asf_ni_111.find_adsorption_sites()
# print(ads_sites)
# assert len(ads_sites) == 4


# fig = plt.figure()
# ax = fig.add_subplot(111)
# plot_slab(ni_111, ax, adsorption_sites=True)
# plt.savefig('111.png', img_format='png')