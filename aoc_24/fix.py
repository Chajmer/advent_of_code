import os
import re

# Prejdi všetky súbory v aktuálnom adresári a podadresároch
for root, dirs, files in os.walk("."):
    for file in files:
        # Skontroluj, či názov súboru zodpovedá požiadavke
        match = re.match(r"aoc_24_(\d)_(\d+)\.py", file)
        if match:
            # Vytvor nový názov so správnym formátom
            new_filename = f"aoc_24_0{match.group(1)}_{match.group(2)}.py"
            
            # Získaj úplnú cestu k pôvodnému a novému súboru
            old_file = os.path.join(root, file)
            new_file = os.path.join(root, new_filename)
            
            # Premenuj súbor
            os.rename(old_file, new_file)
            print(f"Renamed: {file} -> {new_filename}")
