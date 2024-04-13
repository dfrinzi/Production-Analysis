import pandas
import pandas as pd
import settings as s


class SummarizeProduction:

    def __init__(self, part_data_df):
        self.part_data_df = part_data_df

    def summarize(self, monthly_production_df):
        # totals
        total_hours = monthly_production_df[s.col_total_hours_produced].sum()
        total_production = monthly_production_df[s.col_total_dollars_produced].sum()
        total_margin = monthly_production_df[s.col_total_margin_dollars].sum()
        margin_percent = (monthly_production_df[s.col_total_margin_dollars].sum() /
                          monthly_production_df[s.col_total_dollars_produced].sum()) * 100

        df = pandas.DataFrame({s.summary_col_total_hours: [total_hours]})
        df[s.summary_col_total_production] = total_production
        df[s.summary_col_total_margin] = total_margin
        df[s.summary_col_total_margin_percent] = margin_percent
        df[s.summary_col_blank] = ""

        # contract hours
        hours_df = monthly_production_df[monthly_production_df[s.col_hyfo_contract].notna()]
        contract_hours = hours_df[s.col_total_hours_produced].sum()
        percent = contract_hours / total_hours * 100
        # df[s.summary_col_contract_hours] = contract_hours
        df[s.summary_col_contract_percent_total] = percent

        # hf hours
        hours_df = monthly_production_df[monthly_production_df[s.col_customer] == s.hyfo]
        hours = hours_df[s.col_total_hours_produced].sum()
        percent = hours / total_hours * 100
        contract_percent = contract_hours / hours * 100
        # df[s.summary_col_hyfo_hours] = hours
        df[s.summary_col_hyfo_percent] = percent
        df[s.summary_col_contract_percent] = contract_percent

        # hy hours
        hours_df = monthly_production_df[monthly_production_df[s.col_customer] == s.hyda]
        hours = hours_df[s.col_total_hours_produced].sum()
        percent = hours / total_hours * 100
        # df[s.summary_col_hyda_hours] = hours
        df[s.summary_col_hyda_percent] = percent

        # daman hours
        hours_df = monthly_production_df[monthly_production_df[s.col_customer] == s.daman]
        hours = hours_df[s.col_total_hours_produced].sum()
        percent = hours / total_hours * 100
        # df[s.summary_col_daman_hours] = hours
        df[s.summary_col_daman_percent] = percent



        df = df.transpose()
        print(df)

