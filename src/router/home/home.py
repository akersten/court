# ######################################################################################################################
# Home routes handle the overall status/dashboard functionality.
# ######################################################################################################################
from flask import render_template

from ..generic import generic_path_render

from src.vm.home.HomeVM import HomeVM


def home():
    # What should happen for endpoints is checking login, gathering data, creating the viewmodel.. for now just
    # do things here but we should really have an infrastructure.
    viewmodel = HomeVM(2)
    return render_template("home/home.html", vm=viewmodel)
