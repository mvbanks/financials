import os

# Compute financial data
DATA_DIR='data'
PAYMENTS_RECONCILIATION_PATH='PaymentsReconciliation.xlsm'

import pandas as pd
xl = pd.ExcelFile(os.path.join(DATA_DIR,PAYMENTS_RECONCILIATION_PATH))
print(xl.sheet_names)
