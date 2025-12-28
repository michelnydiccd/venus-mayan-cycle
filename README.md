# venus-mayan-cycle
Modeling the astronomical relationship between Earth's year, Venus's synodic cycle, and the Mayan Haab' calendar.

## Purpose
This project models the relationship where 5 synodic cycles of Venus approximately equal 8 Haab' years (5 × ~584 days ≈ 8 × 365 days). The connection to Fibonacci numbers (5 and 8) and the golden ratio is explored.

## Initial Flawed Model
The initial version uses a Venus synodic period of 583.9 days (an intentional inaccuracy). Running `venus_model.py` yields:

```
Our model shows that in 8 Haab' years, there are 4.9999 Venus cycles.
```

This result is slightly off from the expected 5 cycles, highlighting the need for a more precise synodic period value.

## How to Run
```bash
python venus_model.py
```