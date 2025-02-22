import boto3
import pandas as pd
import io
class S3Handler:
    def __init__(self):
        pass

    def read_csv_from_s3(self, bucket, key):
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(obj['Body'])
        return df
    
    def write_df_to_s3(self, df, bucket, key):
        s3 = boto3.client('s3')
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        s3.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())
        return True