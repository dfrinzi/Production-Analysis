

# data frame column headers
# base data
col_part_number = "part"
col_cycle_minutes = "cycle_minutes"
col_hyfo_contract = "hf_contract_2024"
col_material = "material"
col_customer = "customer"
col_machine_planned = "machine_plan_2024_1"

# monthly data
col_workcenter = "workcenter"
col_qty_produced = "qty"
col_part_revision = "rev"
col_total_hours_produced = "total_hours"
col_total_hours_percent = "hours/total %"
col_total_dollars_produced = "total_production"
col_total_dollars_percent = "production/total %"
col_margin_dollars = "gross_margin"
col_total_margin_dollars = "total_margin_dollars"
col_total_margin_dollars_percent = "margin/total %"

# gross margin report
col_invoice_number = "invoice #"
col_gross_margin_percent = "gm %"
col_sale_price = "sale_price"

# summary report
summary_col_blank = " "
summary_col_workcenter = "Workcenter"
summary_col_parts = "Part List"
summary_col_part_number_count = "Part Num Count"
summary_col_part_count = "Part Count"
summary_col_runtime = "Run Time"
summary_col_machine_hours = "Machine Hours"

summary_col_total_hours = "Total Hours"
summary_col_total_production = "Total Production $"
summary_col_total_margin = "Total Margin $"
summary_col_total_margin_percent = "Plex Gross Margin %"

summary_col_contract_hours = "Hyfo Contract Hours"
summary_col_hyda_hours = "Hyda Hours"
summary_col_hyfo_hours = "Hyfo Hours"
summary_col_daman_hours = "Daman/Sun/Fast Hours"
summary_col_contract_percent_total = "Contract Hrs % of Total"
summary_col_contract_percent = "Contract Hrs % of Hyfo"
summary_col_hyda_percent = "Hyda Hrs % of Total"
summary_col_hyfo_percent = "Hyfo Hrs % of Total"
summary_col_daman_percent = "Daman Hrs % of Total"
summary_col_total_dollars = "Sales Value of Production"



# filepaths
monthly_production_df_csv_output_folder = "test_data/output/"
monthly_summary_df_csv_output_path = "test_data/output/monthly summary.csv"
part_data_csv_path = "test_data/base_data/manifold_base_data_2_2024.csv"
workcenter_lookup_csv_path = "test_data/workcenter_name_lookup.csv"
gross_margin_csv_path = "test_data/base_data/Gross_Margin_Download_2024_03_27.csv"
master_price_csv_path = "test_data/base_data/Master_Price_List_Export_2024_03_27.csv"

monthly_production_csv_folder = "test_data/prod_summaries_by_part/"
monthly_production_csv_file_paths = {
    "Jan": "01-2024.csv",
    "Feb": "02-2024.csv",
    "Mar": "03-2024.csv",
    "Apr": "",
}

# customer codes
hyfo = "HYFO"
hyda = "HYDA"
daman = "Daman"


