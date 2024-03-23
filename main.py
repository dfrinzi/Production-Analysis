import pandas as pd
from monthly_production_reader import MonthlyProductionReader
from summarize_production_by_workcenter import SummarizeProductionByWorkcenter

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 400)

PART_DATA_CSV = "test_data/base_data/manifold_base_data_2_2024.csv"
WORKCENTER_LOOKUP = "test_data/workcenter_name_lookup.csv"
MONTHLY_PRODUCTION_CSV_FILES = {
    "Jan": "test_data/prod_summaries_by_part/prod_jan24.csv",
    "Feb": "test_data/prod_summaries_by_part/prod_feb24.csv",
    "Mar": "",
    "Apr": "",
}

part_data_df = pd.DataFrame(pd.read_csv(PART_DATA_CSV).to_dict())
contract_parts = part_data_df.loc[part_data_df["hf_contract_2024"].notna()]

monthly_production_reader = MonthlyProductionReader(WORKCENTER_LOOKUP)
summarize_production_by_workcenter = SummarizeProductionByWorkcenter(part_data_df)



# print(contract_parts)
# print(part_df.loc[part_df["hf_contract_2024"].notna(), ["part", "hf_contract_2024"]])

jan_production_df = monthly_production_reader.read_monthly_production(MONTHLY_PRODUCTION_CSV_FILES["Jan"])
# feb_production_df = monthly_production_reader.read_monthly_production(MONTHLY_PRODUCTION_CSV_FILES["Feb"])

# print(f"January: {jan_production_df}")
# print(f"February: {feb_production_df}")

jan_workcenter_summary = summarize_production_by_workcenter.summarize(jan_production_df)

# print(jan_workcenter_summary)
