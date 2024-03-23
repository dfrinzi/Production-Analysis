import pandas as pd

# column headers
PART_DATA_DF_PART = "part"
PART_DATA_DF_CYCLE = "cycle_minutes"

MONTHLY_PROD_DF_WORKCENTER = "Workcenter"
MONTHLY_PROD_DF_PART = "Part"

SUMMARY_DF_WORKCENTER = "Workcenter"
SUMMARY_DF_PARTS = "Part List"
SUMMARY_DF_PART_NUMBER_COUNT = "Part Num Count"
SUMMARY_DF_PART_COUNT = "Part Count"
SUMMARY_DF_RUNTIME = "Run Time"
SUMMARY_DF_MACHINE_HOURS = "Machine Hours"


class SummarizeProductionByWorkcenter:

    def __init__(self, part_data_df):
        self.part_data_df = part_data_df
        self.summary_df = pd.DataFrame()
        self.summary_df[f"{SUMMARY_DF_WORKCENTER}"] = str
        self.summary_df[f"{SUMMARY_DF_PARTS}"] = object
        self.summary_df[f"{SUMMARY_DF_PART_NUMBER_COUNT}"] = int
        self.summary_df[f"{SUMMARY_DF_PART_COUNT}"] = int
        # self.summary_df[f"{SUMMARY_DF_MACHINE_HOURS}"] = int

    def summarize(self, monthly_production_df):
        self.summarize_parts_by_workcenter(monthly_production_df)
        self.summarize_hours_by_workcenter(monthly_production_df)

        # print(self.summary_df)
        return self.summary_df

    def summarize_hours_by_workcenter(self, monthly_production_df):
        for i in range(len(monthly_production_df)):
            workcenter_hours = 0
            workcenter = monthly_production_df[f"{MONTHLY_PROD_DF_WORKCENTER}"][i]
            # print(workcenter)

    def summarize_parts_by_workcenter(self, monthly_production_df):
        last_workcenter = ""
        # test = pd.DataFrame(monthly_production_df.query("Workcenter=='FMS 1'")["Part"]).reset_index(drop=True)
        # print(test)

        for i in range(len(monthly_production_df)):
            current_workcenter = monthly_production_df[f"{MONTHLY_PROD_DF_WORKCENTER}"][i]

            if last_workcenter != current_workcenter:
                last_workcenter = current_workcenter
                parts_list_df_current_workcenter = (pd.DataFrame(monthly_production_df.query
                                                                 (f"{MONTHLY_PROD_DF_WORKCENTER}=="
                                                                  f"'{current_workcenter}'")[f"{MONTHLY_PROD_DF_PART}"])
                                                    .reset_index(drop=True))

                self.summary_df.at[i, f'{SUMMARY_DF_WORKCENTER}'] = current_workcenter
                parts_list = []
                total_wc_part_count = 0
                total_wc_hours = 0

                for j in range(len(parts_list_df_current_workcenter)):
                    current_part = parts_list_df_current_workcenter[f"{MONTHLY_PROD_DF_PART}"][j]
                    parts_list.append(current_part)

                    # total part count per workcenter
                    df = monthly_production_df
                    total_wc_part_count += df[(df['Part'] == current_part) &
                                              (df['Workcenter'] == current_workcenter)]['Qty Prod'].values

                    # total hours per workcenter
                    df = self.part_data_df
                    cycle = df[df[PART_DATA_DF_PART] == current_part][PART_DATA_DF_CYCLE].values
                    print(current_part)
                    print(cycle)

                self.summary_df.at[i, f'{SUMMARY_DF_PARTS}'] = parts_list
                self.summary_df.at[i, f'{SUMMARY_DF_PART_NUMBER_COUNT}'] = len(parts_list_df_current_workcenter)
                self.summary_df.at[i, f'{SUMMARY_DF_PART_COUNT}'] = total_wc_part_count
                self.summary_df.reset_index(drop=True, inplace=True)

                # print(parts_list)
