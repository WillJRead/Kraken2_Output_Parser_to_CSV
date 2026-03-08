import re
import csv

def kraken_output_to_csv(file_path, output_path):

    parsed_lines = []

    with open(file_path) as f:
        while True:
            line = f.readline()
            if not line:  
                break
            line = line.strip()
            if not line:
                continue

            # Step 1: Extract flag
            flag_match = re.match(r'^[CU]\b', line)
            if flag_match:
                flag = flag_match.group()
                line = line[flag_match.end():].lstrip()
            else:
                flag = None
        
            # Skip line if flag is U
            if flag == 'U':
                continue
        
            # Step 2: Extract sequence (read ID)
            seq_match = re.match(r'^\S+', line)
            sequence = seq_match.group()
            line = line[seq_match.end():].lstrip()  

            # Step 3: Extract taxonomy and taxid
            tax_match = re.match(r'^(.*?)\s+(\(taxid \d+\))', line)
            taxonomy = tax_match.group(1)
            taxid_block = tax_match.group(2)
            line = line[tax_match.end():].lstrip()

            # Step 4: Extract score (read length)
            length_match = re.match(r'^(\d+\|\d+)', line)
            length = length_match.group()
            line = line[length_match.end():].lstrip()

            # Step 5: Rest is mapping
            mapping = line

            parsed_lines.append([flag, sequence, taxonomy, taxid_block, length, mapping])

    # Step 6: Write all parsed lines to CSV **once**
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Flag','ReadID','Taxonomy','TaxID','Score','Mapping'])
        writer.writerows(parsed_lines)

kraken_output_to_csv(r"C:\Users\willi\OneDrive\Documents\University\Studies\Coding Repo\Projects for Practice\Personal\239_output.txt",r"C:\Users\willi\OneDrive\Documents\University\Studies\Coding Repo\Projects for Practice\Personal\kraken_simplified.csv")