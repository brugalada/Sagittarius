# created by: Pau Ramos (p.ramos@unistra.fr)
# Date: 19/10/2020

# main

try:
    import cPickle as pickle
except ImportError:
    import pickle

import string
import os

__mypath = os.path.dirname(os.path.abspath(__file__))

filename = __mypath+'pickles/sgr_interpolator'

def get_dist(Lambda,source):
    """ Query the distance for a given Lambda vector and source (strip or ngc3) """
    with open(filename+'_{}_{}.pkl'.format(source,'dist'), 'rb') as f:
        dist_interpol = pickle.load(f)
        dist_vec = dist_interpol(Lambda)
    return dist_vec
            
def get_scale(Lambda):
    """ Query the distance scale for a given Lambda vector and source (strip or ngc3) """
    with open(filename+'_{}_{}.pkl'.format(source,'scale'), 'rb') as f:
        scale_interpol = pickle.load(f)
        scale_vec = scale_interpol(Lambda)
    return scale_vec

def get_pm(Lambda):
    """ Query the proper motions for a given Lambda vector, source (a20, strip or ngc) and frame (gal or icrs)"""
    with open(filename+'_{}_{}_{}.pkl'.format(source,frame,'pmlong'), 'rb') as f:
        pmlong_interpol = pickle.load(f)
        pmlong_vec = pmlong_interpol(Lambda)

    with open(filename+'_{}_{}_{}.pkl'.format(source,frame,'pmlat'), 'rb') as f:
        pmlat_interpol = pickle.load(f)
        pmlat_vec = pmlat_interpol(Lambda)
        
    return np.vstack((pmlong_vec,pmlat_vec))


def sagittarius_properties(Lambda,
                           distance=False,scale=False,proper_motion=True,frame='icrs',source='strip'):
    """
    Obtain the properties of the Sagittarius stream at different Lambdas (defined as in Antoja et al. 2020 & Ramos et al. 2020).
    
    Input:
        - Lambda: float or iterable (ndarray, list or tuple). Values of the Longitude (in the Sagittarius reference frame.) in degrees
        - distance: boolean. True to query the distance to the stream [kpc]. Only available for Strip and nGC3 (based on RR Lyrae, see Ramos20).
        - scale: boolean. True to query the depth of the stream [kpc]. Only available for Strip and nGC3 (based on RR Lyrae, see Ramos20).
        - proper_motion: boolean. True to query the proper motions of the stream [mas/yr]. If frame='ICRS' or 'C', the proper motions are pmra and pmdec. If frame='Galactic' or 'G', the proper motions are mul and mub.
        - frame: string. ICRS or C for ICRS proper motions. Galactic or G for Galactic proper motions.
        - source: string. A20 for the proper motions obtained in Antoja+20. Strip or nGC3 for the proper motions obtained in Ramos+20, respectively, with the Strip or nGC3 sample.
        
    Output:
        Array of values at each given Lambda. The number of columns varies depending on the requested properties (distance, scale and/or proper_motions)
    """
    
    if string.lower(source) not in ['a20','strip','ngc3']:
        raise ValueError("The source requested does not exist. Available options are: A20, Strip, nGC3.")
        
    if string.lower(source) not in ['g','c','icrs','galactic']:
        raise ValueError("The requested reference frame does not exist. The available celestial frames are ICRS (or 'C') and Galactic (or 'G').")
    else:
        if string.lower(source) in ['g','galactic']:
            source='gal'
        elif string.lower(source) in ['c','icrs']:
            source='icrs'
        
    if not (isinstance(Lambda,np.ndarrray) or isinstance(Lambda,list) or isinstance(Lambda,tuple)):
        raise ValueError("The input must be an valid iterable (list, tuple or array).")
        
    if not isinstance(Lambda,np.ndarrray):
        Lambda = np.array(Lambda)
            
    
    if (distance) or (scale) or (proper_motion):
        if distance:
            dist_vec=get_dist(Lambda)            
            if scale:
                scale_vec=get_scale(Lambda)
                if proper_motion:
                    pm_vec=get_pm(Lambda)
                    return np.vstack((dist_vec,scale_vec,pm_vec))
                else:
                    return np.vstack((dist_vec,scale_vec))
            else:
                if proper_motion:
                    pm_vec=get_pm(Lambda)
                    return np.vstack((dist_vec,pm_vec))
                else:
                    return dist_vec
        elif scale:
            scale_vec=get_scale(Lambda)
            if proper_motion:
                pm_vec=get_pm(Lambda)
                return np.vstack((scale_vec,pm_vec))
            else:
                return scale_vec
            
        elif proper_motion:
            pm_vec=get_pm(Lambda)
            return pm_vec
            
    else:
        return none


