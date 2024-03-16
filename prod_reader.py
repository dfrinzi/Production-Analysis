import pandas as pd


class ProdReader:
    def __init__(self, file):
        self.file = file
        self.df = pd.DataFrame(pd.read_csv(self.file).to_dict())
        self.fix()
        self.fill_wc()
        self.split_part_rev()

    def fix(self):
        # remove un-needed rows/columns

        self.df.drop(index=[0], inplace=True)
        self.df = self.df[["Workcenter", "Part", "Qty Prod"]]
        # print(self.df)

    def fill_wc(self):
        # fill workcenter lines that output blanks from the erp

        last_wc = ""
        for i in self.df.index:
            current_wc = self.df["Workcenter"][i]
            if type(current_wc) is str:
                last_wc = current_wc
            if type(current_wc) is float:
                self.df.at[i, 'Workcenter'] = last_wc

    def split_part_rev(self):
        self.df.rename(columns={'Part': 'partrev'}, inplace=True)
        self.df["Part"] = (self.df["partrev"])
        self.df["Rev"] = (self.df["partrev"])
        for i in self.df.index:
            partrev = self.df["partrev"][i]
            if type(partrev) is str:
                # separate part number
                self.df.at[i, 'Part'] = partrev[:partrev.find('rv')]

        for i in self.df.index:
            partrev = self.df["partrev"][i]
            if type(partrev) is str:
                # separate rev number
                self.df.at[i, 'Rev'] = partrev[partrev.find('rv')+3:]

        self.df.drop(columns='partrev', inplace=True)

        print(self.df)




