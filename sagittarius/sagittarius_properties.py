# created by: Pau Ramos (p.ramos@unistra.fr)
# Date: 19/10/2020

# main

try:
    import cPickle as pickle
except ImportError:
    import pickle

codename='sky_20deg'
with open('Sgr_dist_locations_interpolator_{}.pkl'.format(codename), 'rb') as f:
    dist_interpol = pickle.load(f)

