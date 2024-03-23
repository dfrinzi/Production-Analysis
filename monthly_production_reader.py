import pandas as pd

MONTHLY_PRODUCTION_DF_CSV_OUT = "test_data/output/monthly_production_df.csv"

class MonthlyProductionReader:
    def __init__(self, workcenter_lookup_csv):
        self.workcenter_df = pd.DataFrame(pd.read_csv(workcenter_lookup_csv).to_dict())
        self.monthly_production_df = pd.DataFrame

    def read_monthly_production(self, monthly_production_csv):
        self.monthly_production_df = pd.DataFrame(pd.read_csv(monthly_production_csv).to_dict())
        self.drop_unneeded_rows_columns()
        self.fill_workcenter_labels()
        self.split_part_number_and_revision()
        self.drop_zero_quantity_rows()
        self.monthly_production_df.to_csv(MONTHLY_PRODUCTION_DF_CSV_OUT)
        return self.monthly_production_df

    def drop_unneeded_rows_columns(self):
        # remove un-needed rows/columns from standard csv

        self.monthly_production_df.drop(index=[0], inplace=True)
        self.monthly_production_df = self.monthly_production_df[["Workcenter", "Part", "Qty Prod"]]
        # print(self.df)

    def fill_workcenter_labels(self):
        # fill workcenter lines that output blanks from the erp
        # rename workcenters to more readable format
        last_wc = ""
        for i in self.monthly_production_df.index:
            current_wc = self.monthly_production_df["Workcenter"][i]

            if type(current_wc) is str:
                last_wc = current_wc
                # print(self.wc_df.query(f"Plex=='{last_wc}'")["Sheet"])
                readable_wc = self.workcenter_df.query(f"Plex=='{last_wc}'")["Sheet"].item()
                self.monthly_production_df.at[i, 'Workcenter'] = readable_wc

            if type(current_wc) is float:
                readable_wc = self.workcenter_df.query(f"Plex=='{last_wc}'")["Sheet"].item()
                self.monthly_production_df.at[i, 'Workcenter'] = readable_wc

    def split_part_number_and_revision(self):
        self.monthly_production_df.rename(columns={'Part': 'partrev'}, inplace=True)
        self.monthly_production_df["Part"] = (self.monthly_production_df["partrev"])
        self.monthly_production_df["Rev"] = (self.monthly_production_df["partrev"])

        for i in self.monthly_production_df.index:
            partrev = self.monthly_production_df["partrev"][i]
            if type(partrev) is str:
                # separate part number
                self.monthly_production_df.at[i, 'Part'] = partrev[:partrev.find('rv')]

        for i in self.monthly_production_df.index:
            partrev = self.monthly_production_df["partrev"][i]
            if type(partrev) is str:
                # separate rev number
                self.monthly_production_df.at[i, 'Rev'] = partrev[partrev.find('rv') + 3:]

        self.monthly_production_df.drop(columns='partrev', inplace=True)

        # print(self.prod_df)

    def drop_zero_quantity_rows(self):
        self.monthly_production_df = self.monthly_production_df[self.monthly_production_df['Qty Prod'] != 0.0]
        self.monthly_production_df.reset_index(drop=True, inplace=True)
