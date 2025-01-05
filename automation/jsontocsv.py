import json
import csv
import os

def flatten_prescription(prescription, meta):
    """Flatten a prescription object into a list of rows"""
    rows = []
    
    for p in prescription['prescriptions']:
        # Join multiple items with semicolon
        items = '; '.join(p['items'])
        
        row = {
            'file': prescription['file'],
            'title': prescription['title'],
            'issued_by': prescription['issued_by'],
            'sample_date': prescription['sample_date'],
            'prescription_name': p['name'],
            'type': p['type'],
            'items': items,
            'start_date': p['start_date'],
            'dosage_frequency': p['dosage_frequency']
        }
        rows.append(row)
    
    return rows

def main():
    _thisdir = os.path.dirname(os.path.abspath(__file__))
    hash = os.getenv("HASH")
    jsondir = f"{_thisdir}/../{hash}/jsonout"
    csvdir = f"{_thisdir}/../{hash}/csvout"
    
    # Create csvout directory if it doesn't exist
    os.makedirs(csvdir, exist_ok=True)
    
    # Read JSON file
    with open(f"{jsondir}/prescription.json", 'r') as f:
        prescriptions = json.load(f)
    
    # Flatten all prescriptions
    rows = []
    for prescription in prescriptions:
        rows.extend(flatten_prescription(prescription, prescription.get('meta')))
    
    # Write CSV file
    fieldnames = ['file', 'title', 'issued_by', 'sample_date', 
                 'prescription_name', 'type', 'items', 
                 'start_date', 'dosage_frequency']
    
    with open(f"{csvdir}/prescriptions.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
