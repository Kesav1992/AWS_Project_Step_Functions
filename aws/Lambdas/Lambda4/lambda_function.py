import os
from aws.Layers.common_aws_utils import S3Handler
import pandas as pd

def lambda_handler(event, context):
    try:
        s3_handler = S3Handler()
        # Read the CSV file from S3
        bucket = event["bucket"]
        key = event["lambda3_file"]
        lambda3_df = s3_handler.read_csv_from_s3(bucket, key)

        # Perform some data processing
        lambda3_df['Lambda3_Column'] = lambda3_df['Lambda1_Column'] * 5

        # Write the processed data back to S3
        output_filename = 'lambda4-processed-data.csv'
        file_key= os.path.join('lambda4', output_filename).replace('\\', '/')
        s3_handler.write_df_to_s3(lambda3_df, bucket, output_filename)

        return {
            'statusCode': 200,
            'body': 'Lambda4 Data processing complete'
        }
    except Exception as e:
        raise e