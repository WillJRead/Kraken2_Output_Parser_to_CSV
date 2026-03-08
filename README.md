# Kraken2 Output to CSV Parser

This Python script contains a function `kraken_output_to_csv` that parses Kraken2 classification output files and converts them into a structured CSV format for easy analysis.  

Created during a project where I was frequently using Kraken2 and needed to merge the results with other dataframes. This project also helped me learn a lot about Regex, which I had not encountered before.  

> **IMPORTANT NOTE:**  
> The Kraken2 output files used when writing the Regex pattern were from files that only included the flag `'C'` for classified reads. The function **skips unclassified (`'U'`) lines automatically**, but if your Kraken2 output contains unclassified reads, you may want to pre-filter with:  
> 
> ```bash
> awk '$1 == "C"' kraken2.output > kraken2_filtered.output
> ```

---

### Kraken2 Command Used for Classification

```bash
kraken2 \
  --db "$DB" \
  --paired \
  --threads 16 \
  --use-names \
  --report "${OUTDIR}/${BASENAME}_report.txt" \
  --output "${OUTDIR}/${BASENAME}_output.txt" \
  "$R1" "$R2"

  Note: Changing Kraken2 parameters may affect the ability of the regex pattern to correctly split the output.

## Function ##
```
kraken_output_to_csv(file_path, output_path)
```

**Description:**  
Parses a Kraken2 output file line by line, extracts key fields, and writes them to a CSV file. Lines flagged as `U` (unclassified) are skipped automatically.

**Parameters:**  

| Parameter     | Type   | Description |
|---------------|--------|-------------|
| `file_path`   | `str`  | Path to the Kraken2 output text file. |
| `output_path` | `str`  | Path to save the parsed CSV file. |

**Output:**  

- A CSV file with the following columns:

| Column    | Description |
|-----------|-------------|
| `Flag`    | Classification flag (`C` = classified, `U` = skipped) |
| `ReadID`  | Sequence identifier from the original FASTQ input |
| `Taxonomy`| Taxonomic name (supports multi-word names) |
| `TaxID`  | Taxonomic ID in the format `(taxid XXX)` |
| `Length`  | Paired read length (e.g., `137|137`) |
| `Mapping` | Mapping details including `|:|` sections |

## Example Usage

```python
from kraken_parser import kraken_output_to_csv

input_file = r"C:\path\to\239_output.txt"
output_file = r"C:\path\to\parsed_output.csv"

kraken_output_to_csv(input_file, output_file)
```
Any suggestions for improvements or collaboration ideas are welcome!