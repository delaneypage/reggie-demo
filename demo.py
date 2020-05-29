
try:
    import pandas as pd
    import sys
    import csv
    sys.path.append('/Users/dp/projects/reggie-demo/reggie/')
    from reggie import convert_voter_file
except:
    print("Failed to import.")

# wa_dataframe, metadata = convert_voter_file(state='washington',
#                                             local_file='vrdb-current.zip',
#                                             date='2020-05-16'
#                                             )

(pd.read_csv('vrdb-current/201901_VRDB_Extract.txt', sep='\t', encoding='latin-1', error_bad_lines=False).head(30)).to_csv('wa_vf.csv')

#ga_dataframe = ga_dataframe.applymap(lambda x: x.replace('"', '') if (isinstance(x, str)) else x)


# df_voters = pd.read_csv("Georgia_Daily_VoterBase_16.txt", sep=",", dtype=str,
#                         error_bad_lines=False)
#
# print(df_voters)

# print(ga_dataframe.loc[pd.isna(ga_dataframe["all_history"]),
# ["Registration_Number", "Residence_zipcode", "Last_name", "Registration_date", "all_history"]])

# tbl = pd.read_csv("Georgia_Daily_VoterBase_16.txt", dtype="string", error_bad_lines=False)
# tbl = tbl.applymap(lambda x: str(x).strip('"')).replace({"<NA>":""})
# tbl.to_csv("Georgia_Daily_VoterBase_16_1.txt", index=False)
