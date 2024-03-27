import pandas as pd
import settings as s
from monthly_production_reader import MonthlyProductionReader
from monthly_production_expander import MonthlyProductionExpander
from summarize_production import SummarizeProduction
from summarize_production_by_workcenter import SummarizeProductionByWorkcenter


# pandas settings
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 400)

# loading part data csvs
part_data_df = pd.DataFrame(pd.read_csv(s.part_data_csv_path))
contract_parts_df = part_data_df.loc[part_data_df[s.part_data_col_hfcontract].notna()]

# initialize objects
monthly_production_reader = MonthlyProductionReader(s.workcenter_lookup_csv_path)
monthly_production_expander = MonthlyProductionExpander()
summarize_production = SummarizeProduction(part_data_df)
summarize_production_by_workcenter = SummarizeProductionByWorkcenter(part_data_df)

# print(contract_parts_df)

jan_production_df = monthly_production_reader.read_monthly_production(s.monthly_production_csv_file_paths["Jan"])
jan_production_df = monthly_production_expander.expand(jan_production_df, part_data_df)

print(jan_production_df)
# print(f"February: {feb_production_df}")

summary = summarize_production.summarize(jan_production_df)
# jan_workcenter_summary = summarize_production_by_workcenter.summarize(jan_production_df)

# print(jan_workcenter_summary)
