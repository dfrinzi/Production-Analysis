

# data frame column headers
part_data_col_part = "part"
part_data_col_cycle = "cycle_minutes"
part_data_col_hfcontract = "hf_contract_2024"
part_data_col_material = "material"
part_data_col_customer = "customer"
part_data_col_machine_plan = "machine_plan_2024_1"

monthly_prod_col_workcenter = "workcenter"
monthly_prod_col_part = "part"
monthly_prod_col_qty_prod = "qty"
monthly_prod_col_rev = "rev"
monthly_prod_col_df_hours = "hours"

summary_col_workcenter = "Workcenter"
summary_col_parts = "Part List"
summary_col_part_number_count = "Part Num Count"
summary_col_part_count = "Part Count"
summary_col_runtime = "Run Time"
summary_col_machine_hours = "Machine Hours"

summary_col_total_hours = "Total Hours"
summary_col_contract_hours = "Hyfo Contract Hours"
summary_col_hyda_hours = "Hyda Hours"
summary_col_hyfo_hours = "Hyfo Hours"
summary_col_daman_hours = "Daman/Sun/Fast Hours"
summary_col_contract_percent = "Hyfo Contract Percent"
summary_col_hyda_percent = "Hyda Percent"
summary_col_hyfo_percent = "Hyfo Percent"
summary_col_daman_percent = "Daman Percent"

# filepaths
monthly_production_df_csv_output = "test_data/output/monthly_production_df.csv"
part_data_csv_path = "test_data/base_data/manifold_base_data_2_2024.csv"
workcenter_lookup_csv_path = "test_data/workcenter_name_lookup.csv"
monthly_production_csv_file_paths = {
    "Jan": "test_data/prod_summaries_by_part/prod_jan24.csv",
    "Feb": "test_data/prod_summaries_by_part/prod_feb24.csv",
    "Mar": "",
    "Apr": "",
}

# customer codes
hyfo = "HYFO"
hyda = "HYDA"
daman = "Daman"
