#!/usr/bin/python
from __future__ import print_function
__author__ = "Dr. Dinga Wonanke"
__status__ = "production"
from ccdc import io
import tempfile
import pandas as pd
import csv
import os

def write_crystal(read_crystal, name, format):
    '''
    Function that writes csd structure into one of the many different fileformats
    that is supported by the CSD
    '''
    with io.CrystalWriter(name + '.'+format) as crystal_writer:
        crystal_writer.write(read_crystal)
    return

def download_from_csd(refcode):
    '''
    Function that downloads a crystal structure from 
    CSD using the refcode
    '''
    
    tempdir = tempfile.mkdtemp()
    crystal_reader = io.CrystalReader('CSD')

    read_crystal = crystal_reader.crystal(refcode)

    crystal_reader.close()
    return read_crystal

def main_downloader(refcodes, format='cif'):
    '''
    The main function to download the crystals from the csd.
     Parameters
    ----------
    refcodes: list of refcodes either read from a text file or pandas dataframe
    formats: One of the file formats. cif, csdsql, identifiers, mol, mol2, pdb, res, sdf
             The default format is cif
    '''
    for ref in refcodes:
        try:
            mofs = download_from_csd(ref)
            write_crystal(mofs, ref, format)
        except:
            pass 
    return