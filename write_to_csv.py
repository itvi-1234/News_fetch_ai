import os
import csv
from text_regenerator import write_regenerated_csv
def write_to_csv(leads , filename):

    """Writes the leads to the csv file
        
        Args:
            leads (list): List of leads to write to the csv file
            filename (str): Name of the csv file to write to

        Returns:
            None

        functionality: Reads the existing csv file, checks for duplicates, and writes the new leads to the csv file
    """

    if not leads:
        print("No leads to save")
        return
    
    # Read existing venue keys (name + phone) to avoid duplicates
    existing_leads = set()
    if os.path.exists(filename):
        with open(filename , 'r' , encoding = 'utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    existing_leads.add((row.get('headline','N/A').strip() , row.get('summary', 'N/A'.strip()),row.get('Area' , 'N/A').strip()))

    #lets find new unique venues

    new_unique_leads = []

    for lead in leads:
            unique_key = (lead.get('headline' , 'N/A').strip() , lead.get('summary' , 'N/A').strip(),lead.get('Area' , 'N/A').strip())
            if unique_key not in existing_leads:
                new_unique_leads.append(lead)
                existing_leads.add(unique_key)

    if not new_unique_leads:
        print("ℹ️ No new unique leads to add.")
        return
    

    all_keys = set()

    for key in new_unique_leads:
        all_keys.update(key.keys())
    fieldnames = sorted(list(all_keys))

    file_exists = os.path.isfile(filename)

    with open(filename , 'a' , newline = '' , encoding = 'utf-8') as f:
        writer = csv.DictWriter(f , fieldnames = fieldnames)

        if not file_exists:
            writer.writeheader()

        for lead in new_unique_leads:
            row = {key : lead.get(key , 'N/A') for key in fieldnames}

            writer.writerow(row)

    print(f"Appended {len(new_unique_leads)} new unique leads to '{filename}'")

    print("Regerating the file")

    write_regenerated_csv(filename , fieldnames)