import pandas as pd
import settings as s


# returns a df with only the most recent (highest invoice #) gross margin data for each part
def read_gross_margin(df, dict):
    df.rename(columns={'Part No': s.col_part_number,
                       'Revenue': s.col_revenue,
                       'Invoice No': s.col_invoice_number,
                       'Unit Price': s.col_sale_price,
                       'Sales Qty': s.col_sales_qty,
                       'Tooling Tooling': s.col_tooling_cost,
                       'Material Material': s.col_material_cost,
                       'Labor Part Production': s.col_labor_cost,
                       'Overhead Overhead Fixed': s.col_fixed_cost,
                       'Overhead Overhead Variable': s.col_variable_cost,
                       'Gross Margin': s.col_gross_margin}, inplace=True)

    df[s.col_gross_margin_percent] = df[s.col_gross_margin] / df[s.col_revenue] * 100

    # convert costs and revenue to per pc
    df[s.col_tooling_cost] = df[s.col_tooling_cost] / df[s.col_sales_qty]
    df[s.col_material_cost] = df[s.col_material_cost] / df[s.col_sales_qty]
    df[s.col_labor_cost] = df[s.col_labor_cost] / df[s.col_sales_qty]
    df[s.col_fixed_cost] = df[s.col_fixed_cost] / df[s.col_sales_qty]
    df[s.col_variable_cost] = df[s.col_variable_cost] / df[s.col_sales_qty]
    df[s.col_gross_margin] = df[s.col_gross_margin] / df[s.col_sales_qty]

    df[s.col_total_cost] = df[s.col_sale_price] - df[s.col_gross_margin]

    df = df[[s.col_part_number,
             s.col_invoice_number,
             s.col_sale_price,
             s.col_gross_margin_percent,
             s.col_tooling_cost,
             s.col_material_cost,
             s.col_labor_cost,
             s.col_fixed_cost,
             s.col_variable_cost,
             s.col_gross_margin,
             s.col_total_cost]]

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

    # fix part numbers that don't match between production and financial
    for key in dict:
        value = dict[key]
        gm_latest_invoice_rows_df[s.col_part_number] = (
            gm_latest_invoice_rows_df[s.col_part_number].replace({key: value}))

    # print(gm_latest_invoice_rows_df)
    # print(gm_latest_invoice_rows_df.loc[gm_latest_invoice_rows_df[s.column_part_number] == '7620320'])
    return gm_latest_invoice_rows_df

