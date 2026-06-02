import sys
from pathlib import Path
root = Path(r'D:\LM_IA_LAB\04_PROJECTS\abp_cienciadatos')
sys.path.append(str(root / 'F2' / 'src'))
from preprocessing import run_pipeline
clean, transformed, validation = run_pipeline(root / 'F2' / 'data' / 'raw' / 'dataset_base.csv', root / 'F2' / 'data' / 'processed' / 'dataset_procesado.csv')
print(validation)
assert validation['sin_nulos']
assert validation['sin_duplicados']