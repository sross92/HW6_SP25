#Built off Dr.Smay's criteria and Stem Files
#Used ChatGPT for debugging assistance on py.test

from Rankine import rankine
from Steam import steam


def test_cycle_efficiency():
    # Test Cycle 1: Saturated vapor at turbine inlet
    cycle1 = rankine(p_low=8, p_high=8000, t_high=None, name='Saturated Vapor Cycle')
    eff1 = cycle1.calc_efficiency()
    # Assert that the efficiency is within a reasonable range
    assert 0 < eff1 < 100


def main():
    # Cycle 1: Saturated vapor at turbine inlet (x1 = 1)
    cycle1 = rankine(p_low=8, p_high=8000, t_high=None, name='Saturated Vapor Cycle')
    eff1 = cycle1.calc_efficiency()
    print("Cycle 1 Efficiency: {:.3f}%".format(eff1))
    cycle1.print_summary()

    # Cycle 2: Superheated steam into turbine: T1 = 1.7 * Tsat at p_high
    # Create a temporary steam object at p_high with x = 1 (saturated vapor) to obtain T_sat.
    temp_steam = steam(8000, x=1, name='Temp Steam')
    Tsat = temp_steam.T  # Saturation temperature at 8000 kPa
    T_super = 1.7 * Tsat
    cycle2 = rankine(p_low=8, p_high=8000, t_high=T_super, name='Superheated Cycle')
    eff2 = cycle2.calc_efficiency()
    print("Cycle 2 Efficiency: {:.3f}%".format(eff2))
    cycle2.print_summary()


if __name__ == "__main__":
    main()
