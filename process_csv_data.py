import csv
import json
import os

def read_csv_file(filename):
    """Membaca file CSV dan mengembalikan data sebagai list of lists"""
    data = []
    try:
        # Coba berbagai encoding
        encodings = ['utf-8', 'utf-8-sig', 'latin1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding, newline='') as file:
                    reader = csv.reader(file)
                    data = [row for row in reader]
                    break
            except (UnicodeDecodeError, UnicodeError):
                continue
                
        if not data:
            print(f"Tidak bisa membaca {filename} dengan encoding apapun")
            
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
    except Exception as e:
        print(f"Error membaca {filename}: {e}")
    
    return data

def convert_to_js_format(csv_data_dict):
    """Konversi data CSV ke format JavaScript"""
    js_code = "const csvData = {\n"
    
    for gerai_name, data in csv_data_dict.items():
        js_code += f'    "{gerai_name}": [\n'
        for row in data:
            # Escape quotes dan special characters
            escaped_row = []
            for cell in row:
                cell_str = str(cell).replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r')
                escaped_row.append(f'"{cell_str}"')
            js_code += f'        [{", ".join(escaped_row)}],\n'
        js_code += '    ],\n'
    
    js_code += '};\n'
    return js_code

def main():
    # Mapping nama file ke nama gerai yang bersih
    file_mappings = {
        'Guest Comment - Ahmad Yani.csv': 'Ahmad Yani',
        'Guest Comment - Dalung (2).csv': 'Dalung', 
        'Guest Comment - Mengwi (2).csv': 'Mengwi',
        'Guest Comment - Panjer (1).csv': 'Panjer',
        'Guest Comment - Pemogan (2).csv': 'Pemogan',
        'Guest Comment - TP (1).csv': 'TP'
    }
    
    csv_data = {}
    
    # Baca semua file CSV
    for filename, gerai_name in file_mappings.items():
        if os.path.exists(filename):
            data = read_csv_file(filename)
            if data:
                csv_data[gerai_name] = data
                print(f"✓ Berhasil membaca {filename}: {len(data)} baris")
            else:
                print(f"✗ Gagal membaca {filename}")
        else:
            print(f"✗ File {filename} tidak ditemukan")
    
    # Konversi ke format JavaScript
    if csv_data:
        js_data = convert_to_js_format(csv_data)
        
        # Simpan ke file terpisah untuk debugging
        with open('csv_data.js', 'w', encoding='utf-8') as f:
            f.write(js_data)
        
        print(f"\n✓ Data berhasil dikonversi ke JavaScript")
        print(f"✓ Total gerai: {len(csv_data)}")
        
        # Tampilkan statistik singkat
        for gerai_name, data in csv_data.items():
            print(f"  - {gerai_name}: {len(data)-1} review (excluding header)")
    
    return csv_data, js_data if csv_data else None

if __name__ == "__main__":
    csv_data, js_data = main()
