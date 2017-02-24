
"""
Python model models/SIR_Simple.py
Translated using PySD version 0.7.2
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'cumulative cases': 'cumulative_cases',
    'report case': 'report_case',
    'infect': 'infect',
    'contact infectivity': 'contact_infectivity',
    'recovery period': 'recovery_period',
    'infectious': 'infectious',
    'recovered': 'recovered',
    'recover': 'recover',
    'susceptible': 'susceptible',
    'total population': 'total_population',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'}


@cache('step')
def cumulative_cases():
    """
    cumulative cases
    ----------------
    (cumulative_cases)


    """
    return integ_cumulative_cases()


@cache('step')
def report_case():
    """
    report case
    -----------
    (report_case)


    """
    return infect()


@cache('step')
def infect():
    """
    infect
    ------
    (infect)
    Persons/Day

    """
    return susceptible() * (infectious() / total_population()) * contact_infectivity()


@cache('run')
def contact_infectivity():
    """
    contact infectivity
    -------------------
    (contact_infectivity)
    Persons/Persons/Day
    A joint parameter listing both how many people you contact, and how likely
                you are to give them the disease.
    """
    return 0.7


@cache('run')
def recovery_period():
    """
    recovery period
    ---------------
    (recovery_period)
    Days
    How long are you infectious for?
    """
    return 5


@cache('step')
def infectious():
    """
    infectious
    ----------
    (infectious)
    Persons
    The population with the disease, manifesting symptoms, and able to
                transmit it to other people.
    """
    return integ_infectious()


@cache('step')
def recovered():
    """
    recovered
    ---------
    (recovered)
    Persons
    These people have recovered from the disease. Yay! Nobody dies in this
                model.
    """
    return integ_recovered()


@cache('step')
def recover():
    """
    recover
    -------
    (recover)
    Persons/Day

    """
    return infectious() / recovery_period()


@cache('step')
def susceptible():
    """
    susceptible
    -----------
    (susceptible)
    Persons
    The population that has not yet been infected.
    """
    return integ_susceptible()


@cache('run')
def total_population():
    """
    total population
    ----------------
    (total_population)
    Persons
    This is just a simplification to make it easer to track how many folks
                there are without having to sum up all the stocks.
    """
    return 1000


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Day
    The final time for the simulation.
    """
    return 100


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Day
    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Day [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Day [0,?]
    The time step for the simulation.
    """
    return 0.5


integ_cumulative_cases = functions.Integ(lambda: report_case(), lambda: 0)


integ_infectious = functions.Integ(lambda: infect() - recover(), lambda: 5)


integ_recovered = functions.Integ(lambda: recover(), lambda: 0)


integ_susceptible = functions.Integ(lambda: -infect(), lambda: total_population())


@cache('step')
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


def time():
    return _t
functions.time = time
functions._stage = lambda: _stage
