__author__ = 'kgulliks'

from libs.products import ProductDB, PipelineStorage
from libs.path_info import IGRINSPath
import astropy.io.fits as pyfits

from libs.products import PipelineProducts
import glob
import json
import numpy as np



def blaze_correct(utdate, refdate="20140316", bands="HK",
                  starting_obsids=None,
                  config_file="recipe.config"):

    if bands=="HK":
        bandlist = ["H", "K"]
    elif bands=="H":
        bandlist = ["H"]
    elif bands=="K":
        bandlist==["K"]
    else:
        raise ValueError

    for band in bandlist:
        pattern = "calib/primary/{0:s}/ORDERFLAT_SDC{1:s}_{0:s}*.json".format(utdate, band)
        filename = glob.glob(pattern)[0]

        #Read the json file
        infile = open(filename)
        data = json.load(infile)
        infile.close()

        blazes = np.array([np.array(b) for b in data['fitted_responses']]).T

        np.savetxt("../{:s}/{:s}_BLAZE.DAT".format(utdate, band), blazes)




