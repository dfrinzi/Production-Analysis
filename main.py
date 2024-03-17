import pandas
import pandas as pd
from prod_reader import ProdReader

PART_DATA_CSV = "test_data/base_data/manifold_base_data_2_2024.csv"
WORKCENTER_LOOKUP = "test_data/workcenter_name_lookup.csv"
JAN_PROD = "test_data/prod_summaries_by_part/prod_jan24.csv"


part_df = pandas.DataFrame(pd.read_csv(PART_DATA_CSV).to_dict())
contract_parts = part_df.loc[part_df["hf_contract_2024"].notna()]

# print(contract_parts)
# print(part_df.loc[part_df["hf_contract_2024"].notna(), ["part", "hf_contract_2024"]])

jan_prod = ProdReader(JAN_PROD, WORKCENTER_LOOKUP)
print(jan_prod.prod_df)

