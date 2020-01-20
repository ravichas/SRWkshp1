# Step 1 
# Identify the list of compounds via PubChem (Ex. CDK inhibitors)
# 132145288  132145444  134325670 134326383 134325731 138911339 137278711 132145654 134817260 137796984 134817259
# Step 2
# use PubChem to convert the list into SMILES strings
# Step 3
# save the list of SMILES strings and compound IDs in a file  
# Step 4
# load and the list and the Napthelene core 
# highlight the core in the molecule list
 

suppl = Chem.SmilesMolSupplier('Data/RAS-Inhibitors-CIDtoSMILES.txt',delimiter='\t',titleLine=True, smilesColumn=1)
# show the molecules 
Draw.MolsToGridImage(suppl, subImgSize=(400, 300), molsPerRow = 3)

IPythonConsole.molSize = (450,400)
Draw.MolsToGridImage(suppl, molsPerRow = 3, subImgSize=(450, 200))
core = Chem.MolFromSmiles('C1=CC=CC2=C1C=CC=C2')
mols = [x for x in suppl]

# highlightAtomLists is list of atom list that you want to highlight.
Draw.MolsToGridImage( mols, molsPerRow=4, subImgSize=(550, 300), highlightAtomLists=[mol.GetSubstructMatch(core) for mol in mols] )
