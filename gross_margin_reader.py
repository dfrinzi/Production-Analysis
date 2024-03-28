import pandas as pd
import settings as s


def read_gross_margin(df):
    df.rename(columns={'Part No': s.column_part_number,
                       'Invoice No': s.column_invoice_num,
                       'Unit Price': s.column_gross_margin_price}, inplace=True)

    df[s.column_gross_margin_percent] = df['Gross Margin'] / df['Revenue'] * 100
    df = df[[s.column_part_number, s.column_invoice_num, s.column_gross_margin_price, s.column_gross_margin_percent]]

    df.loc[:, s.column_invoice_num] = pd.to_numeric(df.loc[:, s.column_invoice_num], errors="coerce")
    df = df[df[s.column_invoice_num].notna()]

    df = df.groupby(s.column_part_number)

    # df = df.drop_duplicates(s.column_part_number, keep=s.column_invoice_num.max())

    # df.reset_index(drop=True, inplace=True)
    print(df)
