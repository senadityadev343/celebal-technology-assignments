## Customer Data Pipeline Project

This repository implements a set of data pipelines designed to extract, transform, and load customer and product data from various sources based on specific conditions. The logic uses a Python notebook to run all steps interactively.

### 1. Threshold-Based Conditional Copy

* **Objective**: Read a threshold value from a JSON configuration file (`threshold.json`) and compare it to the number of records in the `Customer` table.
* **Action**: If the record count exceeds the threshold, extract all records from the `Customer` table and write them as JSON files.
* **Output Location**:

  ```
  output/Customer/YYYY/MM/DD/customer_<timestamp>.json
  ```

### 2. Overwriting with Partitioning

* **Objective**: Prevent data loss by partitioning output folders by execution date.
* **Action**: Each run writes to `output/Customer/YYYY/MM/DD/`, and filenames include timestamps to avoid collisions.

### 3. Unified Copy for Multiple Conditions (`Foreach_Example2`)

* **Objective**: Extract filtered data from multiple tables using one loop.
* **Included Filters**:

  * `Product` table: rows where `productid > 100`
  * `Customer` table: rows where `CustomerID > 100 AND CustomerID < 1000`
* **Action**: Iterate through each table and condition, applying the same extraction logic and saving to JSON in the date-partitioned `output` folders.

### 4. Join and Parquet Export

* **Objective**: Combine `Customer` data (from the database) with `Customer_Address` data (from CSV), filter, sort, and export as Parquet.
* **Process**:

  1. Load `Customer` table from the database.
  2. Load `Customer_Address` from CSV.
  3. Join on `CustomerID`.
  4. Filter for `1000 < CustomerID < 2000`.
  5. Sort in ascending order.
  6. Save to:

     ```
     output/joined/YYYY/MM/DD/joined_<timestamp>.parquet
     ```

---

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/senadityadev343/celebal-technology-assignments.git
   cd celebal-technology-assignments/final_project
   ```

2. **Open and run the notebook:**

   * Upload `celeb​al_technologies_project.ipynb` to Google Colab or open locally in Jupyter.
   * Ensure any required libraries (e.g., `pandas`, `pyarrow`, `sqlite3`) are available (these are included by default in most environments).
   * Run all cells in order.

3. **Verify outputs:**

   * Inspect the `output/` folder for JSON and Parquet files.
   * Check the `report/` folder for logs and summaries.

---

## Notes

* Uses SQLite for lightweight, local database simulation.
* Modify `threshold.json` to test different threshold scenarios.
* Folder and file names include timestamps to ensure uniqueness and partitioning.
