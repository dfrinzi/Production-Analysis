import pandas as pd
import settings as s


class SummarizeProductionByWorkcenter:

    def __init__(self, part_data_df):
        self.part_data_df = part_data_df
        self.summary_df = pd.DataFrame()
        self.summary_df[f"{s.summary_col_workcenter}"] = str
        self.summary_df[f"{s.summary_col_parts}"] = object
        self.summary_df[f"{s.summary_col_part_number_count}"] = int
        self.summary_df[f"{s.summary_col_part_count}"] = int
        self.summary_df[f"{s.summary_col_machine_hours}"] = int

    def summarize(self, monthly_production_df):
        self.summarize_parts_by_workcenter(monthly_production_df)

        # print(self.summary_df)
        return self.summary_df

    def summarize_parts_by_workcenter(self, monthly_production_df):
        last_workcenter = ""
        # test = pd.DataFrame(monthly_production_df.query("Workcenter=='FMS 1'")["Part"]).reset_index(drop=True)
        # print(test)

        for i in range(len(monthly_production_df)):
            current_workcenter = monthly_production_df[f"{s.monthly_prod_col_workcenter}"][i]

            if last_workcenter != current_workcenter:
                last_workcenter = current_workcenter
                parts_list_df_current_workcenter = (pd.DataFrame(monthly_production_df.query
                                                                 (f"{s.monthly_prod_col_workcenter}=="
                                                                  f"'{current_workcenter}'")[
                                                                     f"{s.column_part_number}"])
                                                    .reset_index(drop=True))

                self.summary_df.at[i, f'{s.summary_col_workcenter}'] = current_workcenter
                parts_list = []
                total_wc_part_count = 0
                total_wc_hours = 0

                for j in range(len(parts_list_df_current_workcenter)):
                    current_part = parts_list_df_current_workcenter[f"{s.column_part_number}"][j]

                    parts_list.append(current_part)

                    # total part count per workcenter
                    df = monthly_production_df
                    current_part_qty_prod = df[(df['Part'] == current_part) &
                                               (df['Workcenter'] == current_workcenter)]['Qty Prod'].values
                    total_wc_part_count += current_part_qty_prod

                    # total hours per workcenter
                    df = self.part_data_df
                    cycle = 1/60 * df[df[s.column_part_number] == current_part][s.part_data_col_cycle].values
                    current_part_prod_hours = cycle * current_part_qty_prod
                    total_wc_hours += current_part_prod_hours
                    # print(current_part)
                    # print(cycle)
                    # print(current_part_qty_prod)
                    # print(current_part_prod_hours)

                self.summary_df.at[i, f'{s.summary_col_parts}'] = parts_list
                self.summary_df.at[i, f'{s.summary_col_part_number_count}'] = len(parts_list_df_current_workcenter)
                self.summary_df.at[i, f'{s.summary_col_part_count}'] = total_wc_part_count
                self.summary_df.reset_index(drop=True, inplace=True)

                # print(parts_list)
