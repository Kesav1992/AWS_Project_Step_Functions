import pandas as pd
from aws.Layers.common_aws_utils import S3Handler

def lambda_handler(event, context):
    s3_handler = S3Handler()
    # Read the CSV file from S3
    bucket = 'k7-bucket-main1'
    key = 'base_file.csv'
    raw_df = s3_handler.read_csv_from_s3(bucket, key)
    
    # Perform some data processing
    raw_df['Lambda1_Column'] = raw_df['Base_Column'] * 2
    
    # Write the processed data back to S3
    output_key = 'lambda1-processed-data.csv'
    raw_df.to_csv(f's3://{bucket}/{output_key}', index=False)
    
    return {
        'statusCode': 200,
        'body': 'Lambda1 Data processing complete'
    }