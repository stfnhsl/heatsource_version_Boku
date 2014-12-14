__author__ = 'steha'
import heatsource900.BigRedButton
from os.path import dirname, exists, join, realpath


def getscriptpath():
    """Gets the path to the directory where the script is being executed from."""
    return dirname(realpath(__file__))


inputdir = getscriptpath() + '/'
control_file = 'HeatSource_Control.csv'

if not exists(join(inputdir, control_file)):
    raise Exception(
        "HeatSource_Control.csv not found. Move the executable or place the control file in this directory: %s." % inputdir)

heatsource900.BigRedButton.RunHS(inputdir, control_file)
