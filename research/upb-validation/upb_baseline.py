"""Transparent closed-system U-Pb concordia reference, not a data fit.

Time is years. Daughter ratios are radiogenic daughter / present parent.
No common Pb, disequilibrium, transport, or measurement covariance is modeled.
"""
import math
import csv
from pathlib import Path

HALF_LIFE_238_Y = 4.4683e9  # Jaffey 1971, central value
HALF_LIFE_235_Y = 7.0381e8  # Jaffey 1971, central value
L238 = math.log(2) / HALF_LIFE_238_Y
L235 = math.log(2) / HALF_LIFE_235_Y

def conventional(t_years):
    return (math.expm1(L238 * t_years), math.expm1(L235 * t_years))

def initialized(t_years, initial_206_238, initial_207_235):
    return (initial_206_238 * math.exp(L238 * t_years) + math.expm1(L238 * t_years),
            initial_207_235 * math.exp(L235 * t_years) + math.expm1(L235 * t_years))

def conventional_inverse(r206_238, r207_235):
    if min(r206_238, r207_235) < 0:
        raise ValueError('negative radiogenic daughter ratio')
    return (math.log1p(r206_238) / L238, math.log1p(r207_235) / L235)

def main():
    out = Path(__file__).with_name('synthetic_concordia_reference.csv')
    with out.open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['synthetic_t_Ma', '206Pb_star_238U', '207Pb_star_235U', 'inverse_t206_Ma', 'inverse_t207_Ma'])
        for ma in [0, 1, 10, 100, 500, 1000, 2500, 4500]:
            a, b = conventional(ma * 1e6)
            t1, t2 = conventional_inverse(a, b)
            assert abs(t1 - ma * 1e6) < 1e-5
            assert abs(t2 - ma * 1e6) < 1e-5
            assert initialized(ma * 1e6, 0, 0) == (a, b)
            w.writerow([ma, f'{a:.12g}', f'{b:.12g}', f'{t1/1e6:.9g}', f'{t2/1e6:.9g}'])
    print('PASS: 8 synthetic conventional forward/inverse benchmarks; zero-initialization limit; output:', out)

if __name__ == '__main__':
    main()
