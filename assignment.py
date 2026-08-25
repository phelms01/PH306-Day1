"""Starter file for the PH 306 warm-up assignment.

Complete the TODOs in this file. The public tests and CodeGrade checks
import these functions directly from ``assignment.py``.
"""

# Numerical Imports
import numpy as np
from astropy import units as u
from astropy.units import Quantity as Q


# --- Constants --- #
EARTH_GRAVITY = u.Quantity(9.81, u.m / u.s**2)  # Earth's gravitational acceleration


# --- Functions to Implement --- #
@u.quantity_input(v0="speed", a="acceleration", t="time")
def distance_traveled(v0: Q[u.m/u.s], a: Q[u.m/u.s**2], t: Q[u.s]) -> Q[u.m]:
    """Return the displacement for constant acceleration.

    Parameters
    ----------
    v0 : Quantity['speed']
        Initial velocity of the object.
    a : Quantity['acceleration']
        Constant acceleration of the object.
    t : Quantity['time']
        Elapsed time over which the object moves.

    Returns
    -------
    Quantity['length']
        Displacement computed from $v_0 t + \frac{1}{2} a t^2$.
    """    
    return v0*t + 0.5*a*t**2.0


def kinetic_energy(m: Q[u.kg], v: Q[u.m/u.s]) -> Q[u.J]:
    """Returns the kinetic energy of a kinematic object.

    Parameters
    ----------
    m : Q[u.kg]
        Mass in kilograms (kg).
    v : Q[u.m/u.s]
        Velocity in m/s.

    Returns
    -------
    Q[u.J]
        Kinetic energy (J).

    Examples
    --------
    FIXME: Add docs.

    """
    
    return 0.5*m*v**2.0


def free_fall_height(
    y0: Q[u.m],
    t: Q[u.s],
    v0: Q[u.m/u.s] = u.Quantity(0.0, u.m / u.s),
    g: Q[u.m/u.s**2] = EARTH_GRAVITY,
) -> Q[u.m]:
    """Returns the height of an object in free fall at a point in time.

    Parameters
    ----------
    y0 : Q[u.m]
        Initial height (m).
    t : Q[u.s]
        Time (s).
    v0 : Q[u.m/u.s]
        Initial velocity (m/s).
    g : Q[u.m/u.s**2]
        Gravitational constant (m/s^2).

    Returns
    -------
    Q[u.m]
        Height (m).

    Examples
    --------
    FIXME: Add docs.

    """

    return y0 - v0*t - 0.5*g*t**2.0



def projectile_range(v0: Q[u.m/u.s], th0: Q[u.deg], g : Q[u.m/u.s**2] = EARTH_GRAVITY) -> Q[u.m]:    
    """Return the horizontal range of an object following a ballistic trajectory, assuming the start and end heights are equal.

    Parameters
    ----------
    v0 : Quantity['velocity']
        Initial velocity of object.
    th0 : Quantity['angle']
        Initial angle of trajectory relative to the horizon.
    g : Quantity['acceleration']
        Gravitational acceleration constant.

    Returns
    -------
    Quantity[u.m]
        Horizontal range in meters.

    Examples
    --------
    FIXME: Add docs.

    """
    return (v0**2.0*np.sin(2.0*th0))/g    


def quadratic_solver(a: float, b: float, c: float) -> tuple[float, float]:    
    """Solves the quadratic equation and returns both roots in a tuple using the plus-minus convention.
    $ ax^2+bx+c=0 $

    Parameters
    ----------
    a : float
        A coefficient of quadratic equation.
    b : float
        B coefficient of quadratic equation.
    c : float
        C coefficient of quadratic equation.

    Returns
    -------
    tuple[float, float]
        Roots of quadratic equation.

    Examples
    --------
    FIXME: Add docs.

    """
    return ((-b + np.sqrt(b**2.0 - 4.0*a*c))/(2.0*a), (-b - np.sqrt(b**2.0 - 4.0*a*c))/(2.0*a))
