import pandas as pd

PART_DATA_DF_WORKCENTER = "Workcenter"
PART_DATA_DF_PART = "Part"
SUMMARY_DF_WORKCENTER = "Workcenter"
SUMMARY_DF_PARTS = "Parts"
SUMMARY_DF_PART_COUNT = "Part Count"
SUMMARY_DF_RUNTIME = "Run Time"


class SummarizeProductionByWorkcenter:

    def __init__(self, part_data_df):
        self.part_data_df = part_data_df
        self.summary_df = pd.DataFrame()
        self.summary_df[f"{SUMMARY_DF_WORKCENTER}"] = str
        self.summary_df[f"{SUMMARY_DF_PARTS}"] = object
        self.summary_df[f"{SUMMARY_DF_PART_COUNT}"] = int

    def summarize(self, monthly_production_df):
        self.summarize_parts_by_workcenter(monthly_production_df)

        print(self.summary_df)
        return self.summary_df

    def summarize_parts_by_workcenter(self, monthly_production_df):
        last_workcenter = ""
        # test = pd.DataFrame(monthly_production_df.query("Workcenter=='FMS 1'")["Part"]).reset_index(drop=True)
        # print(test)

        for i in range(len(monthly_production_df)):
            current_workcenter = monthly_production_df[f"{PART_DATA_DF_WORKCENTER}"][i]
            if last_workcenter != current_workcenter:
                last_workcenter = current_workcenter
                parts_list_df = (pd.DataFrame(monthly_production_df.query
                                              (f"{PART_DATA_DF_WORKCENTER}=="
                                               f"'{last_workcenter}'")[f"{PART_DATA_DF_PART}"])
                                 .reset_index(drop=True))

                self.summary_df.at[i, f'{SUMMARY_DF_WORKCENTER}'] = last_workcenter
                parts_list = []
                count = 0

                for j in range(len(parts_list_df)):
                    parts_list.append(parts_list_df[f"{PART_DATA_DF_PART}"][j])

                self.summary_df.at[i, f'{SUMMARY_DF_PARTS}'] = parts_list
                self.summary_df.at[i, f'{SUMMARY_DF_PART_COUNT}'] = len(parts_list_df)
                self.summary_df.reset_index(drop=True, inplace=True)

                # print(parts_list)







