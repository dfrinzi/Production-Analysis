import pandas as pd
import settings as s


# add stats to the monthly dataframes from the part data dataframe for use later


class MonthlyProductionExpander:

    def __init__(self):
        pass

    def expand(self, monthly_prod_df, part_data_df):
        monthly_prod_df = pd.merge(monthly_prod_df, part_data_df[[
            s.part_data_dfch_part,
            s.part_data_dfch_customer,
            s.part_data_dfch_material,
            s.part_data_dfch_cycle,
            s.part_data_dfch_hfcontract,
        ]], on=s.monthly_prod_dfch_part, how='left')

        monthly_prod_df[s.monthly_prod_df_hours] = (monthly_prod_df[s.monthly_prod_df_qty_prod] *
                                                    monthly_prod_df[s.part_data_dfch_cycle] / 60)

        return monthly_prod_df
