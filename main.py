import os
import pandas as pd
import settings as s
from monthly_production_reader import MonthlyProductionReader
from monthly_production_expander import MonthlyProductionExpander
from summarize_production import SummarizeProduction
from summarize_production_by_workcenter import SummarizeProductionByWorkcenter
import gross_margin_reader
from temp_scripts import temp

# temp()
# exit()

# pandas settings
pd.set_option('display.max_columns', 18)
pd.set_option('display.width', 400)

# loading data csvs
part_data_df = pd.DataFrame(pd.read_csv(s.part_data_csv_path))
contract_parts_df = part_data_df.loc[part_data_df[s.col_hyfo_contract].notna()]
gross_margin_df = pd.DataFrame(pd.read_csv(s.gross_margin_csv_path))

# initialize objects
monthly_production_reader = MonthlyProductionReader(s.workcenter_lookup_csv_path)
monthly_production_expander = MonthlyProductionExpander()
summarize_production = SummarizeProduction(part_data_df)
summarize_production_by_workcenter = SummarizeProductionByWorkcenter(part_data_df)

# process data csvs
gross_margin_df = gross_margin_reader.read_gross_margin(gross_margin_df)

# monthly reports
monthly_file_list = os.listdir(s.monthly_production_csv_folder)

monthly_summary_df = pd.DataFrame()

for file in monthly_file_list:
    file_no_ext = os.path.splitext(file)[0]

    monthly_production_df = monthly_production_reader.read_monthly_production(s.monthly_production_csv_folder + file)
    monthly_production_df = monthly_production_expander.expand(monthly_production_df, part_data_df, gross_margin_df)
    monthly_production_df.to_csv(s.monthly_production_df_csv_output_folder + file)

    summary = summarize_production.summarize(monthly_production_df)
    summary.rename(index={0: file_no_ext}, inplace=True)
    monthly_summary_df = pd.concat([monthly_summary_df, summary])

monthly_summary_df = monthly_summary_df.transpose()
print(monthly_summary_df)

monthly_summary_df.to_csv(s.monthly_summary_df_csv_output_path)

