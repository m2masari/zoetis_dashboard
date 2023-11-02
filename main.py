from gaextract import Report
from daterange import daterange
from connect import connection
import pandas as pd
import os
import ast
import glob

report = Report()
date = daterange()
date_list = date.datelist()
con = connection()
data = con.getprop()


#viewid=['164566332','164541222']
# Index=[1,2]

for i in range(1,8):
    report.dimensions = ast.literal_eval(data.loc[data['Index'] == i, 'Dimensions'].iloc[0])
    report.metrics = ast.literal_eval(data.loc[data['Index'] == i, 'Metrics'].iloc[0])
    table = data.loc[data['Index'] == i, 'TableName'].iloc[0]
    Ind = data.loc[data['Index'] == i, 'Index'].iloc[0]
    viewid=ast.literal_eval(data.loc[data['Index'] == i, 'ViewId'].iloc[0])
    df1 = []
    for report.viewid in viewid:
           try:
               for date_item in date_list:

                   date_range = date_item[0]
                   report.date_range = {'startDate': date_range['startDate'], 'endDate': date_range['endDate']}
                   df = report.next_records()
                   df['view_id'] = report.viewid
                   df1.append(df)
               df = pd.concat(df1).reset_index(drop=True)
           except:
              df=[]
              df=pd.DataFrame(df)
    if not df.empty:
       start_date = date_list[0][0]['startDate']
       len1 = str(len(df.index))
       df.to_csv(os.path.join(r'C:\Users\melik.masarifoglu\PycharmProjects\zoetis_dashboard\export',
       table+'_'+'_'+start_date + "_" + date_range['endDate'] + "_" + len1 + ".csv"), index=False,header=True)





