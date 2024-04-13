import pandas as pd
import settings as s


# returns a df with only the most recent (highest invoice #) gross margin data for each part
def read_gross_margin(df):
    df.rename(columns={'Part No': s.col_part_number,
                       'Invoice No': s.col_invoice_number,
                       'Unit Price': s.col_sale_price}, inplace=True)

    df[s.col_gross_margin_percent] = df['Gross Margin'] / df['Revenue'] * 100
    df = df[[s.col_part_number, s.col_invoice_number, s.col_sale_price, s.col_gross_margin_percent]]

    df.loc[:, s.col_invoice_number] = pd.to_numeric(df.loc[:, s.col_invoice_number], errors="coerce")
    df = df[df[s.col_invoice_number].notna()]
    unique_parts = df[s.col_part_number].unique()
    # print(unique_parts)

    latest_invoice_rows = []

    for part in unique_parts:
        part_df = df.loc[df[s.col_part_number] == part]
        row_num = part_df[s.col_invoice_number].idxmax(skipna=True)
        single_row_df = part_df.loc[[row_num], :]
        latest_invoice_rows.append(single_row_df)

    gm_latest_invoice_rows_df = pd.concat(latest_invoice_rows, axis=0, ignore_index=True)

    # print(gm_latest_invoice_rows_df)
    # print(gm_latest_invoice_rows_df.loc[gm_latest_invoice_rows_df[s.column_part_number] == '7620320'])
    return gm_latest_invoice_rows_df

