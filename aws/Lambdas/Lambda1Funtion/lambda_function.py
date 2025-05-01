import pandas as pd
import os
from aws.Layers.common_aws_utils import S3Handler

def lambda_handler(event, context):
    try:
        s3_handler = S3Handler()
        # Read the CSV file from S3
        bucket = event['bucket']
        key = 'base_file.csv'
        raw_df = s3_handler.read_csv_from_s3(bucket, key)

        # Perform some data processing
        raw_df['Lambda1_Column'] = raw_df['Base_Column'] * 2

        # Write the processed data back to S3
        output_filename = 'lambda1-processed-data.csv'
        file_key= os.path.join('lambda1', output_filename).replace('\\', '/')
        s3_handler.write_df_to_s3(raw_df, bucket, file_key)

        return {
            'statusCode': 200,
            'lambda1_file': file_key,
            'body': 'Lambda1 Data processing complete'
        }
    except Exception as e:
        raise e