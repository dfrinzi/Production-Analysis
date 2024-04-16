import pandas as pd
import settings as s


# add stats to the monthly dataframes from the part data dataframe for use later


class MonthlyProductionExpander:

    def __init__(self):
        pass

    def expand(self, monthly_prod_df, part_data_df, gross_margin_df):
        monthly_prod_df = pd.merge(monthly_prod_df, part_data_df[[
            s.col_part_number,
            s.col_customer,
            s.col_material,
            s.col_cycle_minutes,
            s.col_hyfo_contract,
        ]], on=s.col_part_number, how='left')

        # todo: need better warning or report of parts without cycles in part data
        # todo: need method to update part data when missing cycles or erros are found
        zero_cycle_parts_df = monthly_prod_df.loc[monthly_prod_df[s.col_cycle_minutes] == 0]
        print("Parts Missing Cycle Times:")
        print(zero_cycle_parts_df)

        monthly_prod_df = pd.merge(monthly_prod_df, gross_margin_df[[
            s.col_part_number,
            s.col_sale_price,
            s.col_gross_margin_percent
        ]], on=s.col_part_number, how='left')

        monthly_prod_df[s.col_margin_dollars] = (monthly_prod_df[s.col_sale_price] *
                                                 monthly_prod_df[s.col_gross_margin_percent] / 100)

        monthly_prod_df[s.col_total_hours_produced] = (monthly_prod_df[s.col_qty_produced] *
                                                       monthly_prod_df[s.col_cycle_minutes] / 60)

        monthly_prod_df[s.col_total_dollars_produced] = (monthly_prod_df[s.col_qty_produced] *
                                                         monthly_prod_df[s.col_sale_price])

        monthly_prod_df[s.col_total_margin_dollars] = (monthly_prod_df[s.col_qty_produced] *
                                                       monthly_prod_df[s.col_margin_dollars])

        monthly_prod_df[s.col_total_hours_percent] = (monthly_prod_df[s.col_total_hours_produced] /
                                                      monthly_prod_df[s.col_total_hours_produced].sum() * 100)

        monthly_prod_df[s.col_total_dollars_percent] = (monthly_prod_df[s.col_total_dollars_produced] /
                                                        monthly_prod_df[s.col_total_dollars_produced].sum() * 100)

        monthly_prod_df[s.col_total_margin_dollars_percent] = (monthly_prod_df[s.col_total_margin_dollars] /
                                                               monthly_prod_df[s.col_total_margin_dollars].sum() * 100)

        # print(monthly_prod_df[s.monthly_prod_col_qty_prod].sum())
        # print(monthly_prod_df[s.col_total_dollars_produced].sum())
        # print(monthly_prod_df[s.col_total_margin_dollars].sum())
        # print(monthly_prod_df[s.col_total_dollars_percent].sum())
        # print(monthly_prod_df[s.col_total_margin_dollars_percent].sum())

        return monthly_prod_df
