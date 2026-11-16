# ISM2411 Lab 12 — Read a Sales CSV, Write a Cleaned Report

Asher Gottlieb

Run from this repository's top-level folder:

```bash
python csv_practice.py
```

The script completes Exercises 1–8 using Python's standard library. It reads
`data/sales.csv`, regenerates `data/cleaned.csv`, and appends one timestamped
revenue entry to `data/run_log.txt` each time it runs.

The supplied data contains 12 orders. The script checks that `csv.reader` and
`csv.DictReader` produce the same revenue total and prints a sorted summary
that combines repeated products.
