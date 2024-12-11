def create_codon_dict(file_path):
    file = open(path)
    rows = file.readlines()
    file.close()

    milon = {}
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      amino_acids = cells[2]
      milon[codon] = amino_acids

    return milon
