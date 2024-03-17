import pandas as pd


class ProdReader:
    def __init__(self, prod_file, wc_file):
        self.prod_df = pd.DataFrame(pd.read_csv(prod_file).to_dict())
        self.wc_df = pd.DataFrame(pd.read_csv(wc_file).to_dict())
        self.fix()
        self.fill_wc()
        self.split_part_rev()

    def fix(self):
        # remove un-needed rows/columns

        self.prod_df.drop(index=[0], inplace=True)
        self.prod_df = self.prod_df[["Workcenter", "Part", "Qty Prod"]]
        # print(self.df)

    def fill_wc(self):
        # fill workcenter lines that output blanks from the erp
        # rename workcenters to more readable format
        # test = "FMS1"
        # print(self.wc_df.query(f"Plex=='{test}'")["Sheet"].values[0])
        last_wc = ""
        for i in self.prod_df.index:
            current_wc = self.prod_df["Workcenter"][i]

            if type(current_wc) is str:
                last_wc = current_wc
                # print(self.wc_df.query(f"Plex=='{last_wc}'")["Sheet"])
                readable_wc = self.wc_df.query(f"Plex=='{last_wc}'")["Sheet"].item()
                self.prod_df.at[i, 'Workcenter'] = readable_wc

            if type(current_wc) is float:
                readable_wc = self.wc_df.query(f"Plex=='{last_wc}'")["Sheet"].item()
                self.prod_df.at[i, 'Workcenter'] = readable_wc

    def split_part_rev(self):
        self.prod_df.rename(columns={'Part': 'partrev'}, inplace=True)
        self.prod_df["Part"] = (self.prod_df["partrev"])
        self.prod_df["Rev"] = (self.prod_df["partrev"])
        for i in self.prod_df.index:
            partrev = self.prod_df["partrev"][i]
            if type(partrev) is str:
                # separate part number
                self.prod_df.at[i, 'Part'] = partrev[:partrev.find('rv')]

        for i in self.prod_df.index:
            partrev = self.prod_df["partrev"][i]
            if type(partrev) is str:
                # separate rev number
                self.prod_df.at[i, 'Rev'] = partrev[partrev.find('rv') + 3:]

        self.prod_df.drop(columns='partrev', inplace=True)

        # print(self.prod_df)

