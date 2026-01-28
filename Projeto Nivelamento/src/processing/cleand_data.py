
def replace_abbreviations(df):

    df.rename(columns={
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }, inplace=True)

    return df
