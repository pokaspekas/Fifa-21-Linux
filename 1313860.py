""" Game fix for Fifa 21
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ 
    """

    # Replace launcher with game exe in proton arguments
    util.protontricks('vcrun2012')
    util.protontricks('vcrun2013')
    util.protontricks('vcrun2019_ge')
    util.protontricks('allfonts')
    util.protontricks('dotnet462')
    util.protontricks('d3dcompiler_47')
    util.protontricks('d3dcompiler_43')
    util.protontricks('win7')
    util.use_seccomp()
