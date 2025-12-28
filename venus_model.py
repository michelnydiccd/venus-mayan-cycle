"""
Modeling the relationship between Earth's year, Venus's synodic cycle, and the Mayan Haab' calendar.
Intentional flaw: using 583.9 days for Venus synodic period.
"""

VENUS_SYNODIC_PERIOD = 583.9  # days (intentional flawed value)
HAAB_YEAR = 365  # days

def calculate_venus_cycles(earth_days):
    """Return number of Venus synodic cycles in given Earth days."""
    return earth_days / VENUS_SYNODIC_PERIOD

def calculate_haab_years(earth_days):
    """Return number of Haab' years in given Earth days."""
    return earth_days / HAAB_YEAR

def main():
    # 8 Haab' years in Earth days
    eight_haab_years_days = 8 * HAAB_YEAR
    venus_cycles = calculate_venus_cycles(eight_haab_years_days)
    print(f"Our model shows that in 8 Haab' years, there are {venus_cycles:.4f} Venus cycles.")
    # For demonstration, also print raw value
    print(f"({eight_haab_years_days} Earth days / {VENUS_SYNODIC_PERIOD} days per Venus cycle = {venus_cycles})")

if __name__ == "__main__":
    main()