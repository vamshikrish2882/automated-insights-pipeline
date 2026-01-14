"""
run_pipeline.py

Orchestrates the full automated insights pipeline:
1. Generate synthetic raw data
2. Load into SQLite database
3. Run SQL transformations to build analytical tables
4. Compute weekly KPIs
5. Detect anomalous weeks
"""

from __future__ import annotations

from . import generate_data, extract_load, transform, kpis, anomalies


def run_all() -> None:
    """
    Run the entire pipeline end-to-end.
    """
    print("=== STEP 1: Generate synthetic raw data ===")
    generate_data.main()

    print("\n=== STEP 2: Extract & Load into SQLite ===")
    extract_load.main()

    print("\n=== STEP 3: Run SQL Transformations ===")
    transform.main()

    print("\n=== STEP 4: Compute Weekly KPIs ===")
    kpis.main()

    print("\n=== STEP 5: Detect Anomalies ===")
    anomalies.main()

    print("\nPipeline completed successfully.")


def main() -> None:
    run_all()


if __name__ == "__main__":
    main()
