def append_to_excel(fpath, df, sheet_name):
    with pd.ExcelWriter(fpath, mode="a") as f:
        df.to_excel(f, sheet_name=sheet_name)

import pandas as pd
CDR = "CDR.csv"
VARS = []
EXTS = [306, 318, 322, 382, 438, 488, 547, 573, 588, 722, 751, 775, 812, 816, 2239, 2254, 2255, 2256, 2259,2260, 2261, 2401, 2575]
df = pd.read_csv(CDR, usecols={'globalCallID_callId','dateTimeOrigination','callingPartyNumber','origCause_location','origCause_value','origPrecedenceLevel','destLegIdentifier','destNodeId','destSpan','originalCalledPartyNumber','finalCalledPartyNumber','destCause_location','destCause_value','dateTimeConnect','dateTimeDisconnect','lastRedirectDn','origDeviceName','destDeviceName','origCallTerminationOnBehalfOf','destCallTerminationOnBehalfOf','origCalledPartyRedirectOnBehalfOf','lastRedirectRedirectOnBehalfOf','originalCalledPartyPattern','finalCalledPartyPattern','lastRedirectingPartyPattern','huntPilotPattern','duration'})
output_file = "CDR.xlsx"
i = 0
for ext in EXTS:
    dn = str(ext)
    ext_df = df.loc[(df['originalCalledPartyNumber'] == dn)]
    ext_df = ext_df.loc[(ext_df['duration'] == 0)]
    append_to_excel(output_file,ext_df,dn)
