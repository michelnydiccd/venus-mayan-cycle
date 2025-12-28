"""
Modeling the relationship between Earth's year, Venus's synodic cycle, and the Mayan Haab' calendar.
Corrected with precise Venus synodic period.
"""

VENUS_SYNODIC_PERIOD = 583.921356  # days (precise value)
HAAB_YEAR = 365  # days

def calculate_venus_cycles(earth_days):
    """Return number of Venus synodic cycles in given Earth days."""
    return earth_days / VENUS_SYNODIC_PERIOD

def calculate_haab_years(earth_days):
    """Return number of Haab' years in given Earth days."""
    return earth_days / HAAB_YEAR

def calculate_cycle_ratio():
    """
    Calculate the ratio of (8 Haab' years) / (5 Venus cycles).
    Should be close to 1, demonstrating the alignment.
    """
    eight_haab_years_days = 8 * HAAB_YEAR
    five_venus_cycles_days = 5 * VENUS_SYNODIC_PERIOD
    return eight_haab_years_days / five_venus_cycles_days

def main():
    # 8 Haab' years in Earth days
    eight_haab_years_days = 8 * HAAB_YEAR
    venus_cycles = calculate_venus_cycles(eight_haab_years_days)
    print(f"Our model shows that in 8 Haab' years, there are {venus_cycles:.6f} Venus cycles.")
    # Print ratio
    ratio = calculate_cycle_ratio()
    print(f"Ratio of (8 Haab' years) / (5 Venus cycles) = {ratio:.8f}")
    print(f"This demonstrates the close alignment (expected ~1).")

if __name__ == "__main__":
    main()