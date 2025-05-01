import os
from aws.Layers.common_aws_utils import S3Handler
import pandas as pd

def lambda_handler(event, context):
    try:
        s3_handler = S3Handler()
        # Read the CSV file from S3
        bucket = event["bucket"]
        key = event["lambda1_file"]
        lambda2_df = s3_handler.read_csv_from_s3(bucket, key)

        # Perform some data processing
        lambda2_df['Lambda2_Column'] = lambda2_df['Lambda1_Column'] * 3

        # Write the processed data back to S3
        output_filename = 'lambda2-processed-data.csv'
        file_key= os.path.join('lambda2', output_filename).replace('\\', '/')
        s3_handler.write_df_to_s3(lambda2_df, bucket, file_key)

        return {
            'statusCode': 200,
            'lambda2_file': file_key,
            'body': 'Lambda2 Data processing complete'
        }
    except Exception as e:
        raise e
    
    