from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import pandas as pd

KEY_FILE_LOCATION = "client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def initialize_analyticsreporting():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
    analytics = build("analyticsreporting", "v4", credentials=credentials)

    return analytics


Analytics = initialize_analyticsreporting()


class Report:
    def __init__(self):
        self.date_range = []
        self.dimensions = []
        self.metrics = []
        self.segments = []
        self.dimension_filters = []
        self.viewid=[]

    def debug(self):
        # TODO: Create a debug export file / log for each run contains a list of reports...
        print(self.date_range,
              self.dimensions,
              self.metrics,
              self.segments,
              self.dimension_filters,
              self.metric_filters,
              )

    def request(self, pageToken='None'):
        response = Analytics.reports().batchGet(
            # TODO: Validate values and prevent false query
            body={
                "reportRequests": [
                    {
                        "viewId": self.viewid,
                        "dateRanges": self.date_range,
                        "metrics": [{'expression': expression} for expression in self.metrics],
                        "dimensions": [{'name': name} for name in self.dimensions],
                        "pageSize": 100000,
                        "pageToken": pageToken
                    }]
            }
        ).execute()
        return response

    def next_records(self):
        from manipulate import manipulate
        records = []
        response = self.request()
        nextPageToken = response.get("reports")[0].get('nextPageToken', None)
        df = manipulate(response)
        records.append(df)
        while nextPageToken != None:
            response = self.request(nextPageToken)
            df = manipulate(response)
            records.append(df)
            nextPageToken = response.get("reports")[0].get('nextPageToken', None)
        df = pd.concat(records).reset_index(drop=True)
        df.columns = df.columns.str.replace(r'ga:', '')
        return df


