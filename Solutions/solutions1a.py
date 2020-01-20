# register all descriptors
calc = Calculator(descriptors, ignore_3D=True)

for mol in suppl:
    if mol is None: continue
    print(mol.GetProp('_Name'), 'has', mol.GetNumBonds(), 'bonds')
    
descriptor_list = {'MW', 'nHBDon','nRing','nHBAcc',
                   'nRot','SLogP','TopoPSA'}
    
IPythonConsole.molSize = (450,200)

# mols = [Chem.MolFromSmiles(smi) for smi in suppl]
# as pandas
df = calc.pandas(mols)
df.to_csv(r'KRAS-desc.csv')

df