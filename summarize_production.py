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

        # margins
        hyfo_combined_margin_df = monthly_production_df[monthly_production_df[s.col_customer] == s.hyfo]
        hyfo_combined_margin_sum = hyfo_combined_margin_df[s.col_total_margin_dollars].sum()
        hyfo_combined_production_sum = hyfo_combined_margin_df[s.col_total_dollars_produced].sum()
        df[s.summary_col_hyfo_combined_margin] = 100 * hyfo_combined_margin_sum / hyfo_combined_production_sum
        # todo: change to use loc to preserve index
        hyfo_contract_margin_df = hyfo_combined_margin_df[monthly_production_df[s.col_hyfo_contract].notna()]
        hyfo_contract_margin_sum = hyfo_contract_margin_df[s.col_total_margin_dollars].sum()
        hyfo_contract_production_sum = hyfo_contract_margin_df[s.col_total_dollars_produced].sum()
        df[s.summary_col_hyfo_contract_margin] = 100 * hyfo_contract_margin_sum / hyfo_contract_production_sum

        hyfo_noncontract_margin_df = hyfo_combined_margin_df[monthly_production_df[s.col_hyfo_contract].isna()]
        hyfo_noncontract_margin_sum = hyfo_noncontract_margin_df[s.col_total_margin_dollars].sum()
        hyfo_noncontract_production_sum = hyfo_noncontract_margin_df[s.col_total_dollars_produced].sum()
        df[s.summary_col_hyfo_noncontract_margin] = 100 * hyfo_noncontract_margin_sum / hyfo_noncontract_production_sum

        hyda_combined_margin_df = monthly_production_df[monthly_production_df[s.col_customer] == s.hyda]
        hyda_combined_margin_sum = hyda_combined_margin_df[s.col_total_margin_dollars].sum()
        hyda_combined_production_sum = hyda_combined_margin_df[s.col_total_dollars_produced].sum()
        df[s.summary_col_hyda_margin] = 100 * hyda_combined_margin_sum / hyda_combined_production_sum

        daman_combined_margin_df = monthly_production_df[monthly_production_df[s.col_customer] == s.daman]
        daman_combined_margin_sum = daman_combined_margin_df[s.col_total_margin_dollars].sum()
        daman_combined_production_sum = daman_combined_margin_df[s.col_total_dollars_produced].sum()
        df[s.summary_col_daman_margin] = 100 * daman_combined_margin_sum / daman_combined_production_sum

        # hf hours
        df[s.summary_col_blank] = ""
        hyfo_hours_df = monthly_production_df[monthly_production_df[s.col_customer] == s.hyfo]
        hyfo_hours = hyfo_hours_df[s.col_total_hours_produced].sum()
        hyfo_percent = hyfo_hours / total_hours * 100
        # df[s.summary_col_hyfo_hours] = hours
        df[s.summary_col_hyfo_percent] = hyfo_percent

        # contract hours
        contract_df = hyfo_hours_df[monthly_production_df[s.col_hyfo_contract].notna()]
        contract_hours = contract_df[s.col_total_hours_produced].sum()
        contract_percent_total = contract_hours / total_hours * 100
        contract_percent_hyfo = contract_hours / hyfo_hours * 100
        # df[s.summary_col_contract_hours] = contract_hours
        df[s.summary_col_contract_percent_total] = contract_percent_total
        df[s.summary_col_contract_percent] = contract_percent_hyfo

        # hy hours
        hyda_hours_df = monthly_production_df[monthly_production_df[s.col_customer] == s.hyda]
        hyda_hours = hyda_hours_df[s.col_total_hours_produced].sum()
        hyda_percent = hyda_hours / total_hours * 100
        # df[s.summary_col_hyda_hours] = hours
        df[s.summary_col_hyda_percent] = hyda_percent

        # daman hours
        daman_hours_df = monthly_production_df[monthly_production_df[s.col_customer] == s.daman]
        daman_hours = daman_hours_df[s.col_total_hours_produced].sum()
        daman_percent = daman_hours / total_hours * 100
        # df[s.summary_col_daman_hours] = hours
        df[s.summary_col_daman_percent] = daman_percent

        # df = df.transpose()
        # print(df)
        return df

