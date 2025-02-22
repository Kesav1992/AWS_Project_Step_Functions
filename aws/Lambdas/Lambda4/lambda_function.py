from aws.Layers.common_aws_utils import S3Handler
import pandas as pd

def lambda_handler(event, context):
    s3_handler = S3Handler()
    # Read the CSV file from S3
    bucket = 'k7-bucket-main1'
    key = 'lambda3-processed-data.csv'
    lambda3_df = s3_handler.read_csv_from_s3(bucket, key)
    
    # Perform some data processing
    lambda3_df['Lambda3_Column'] = lambda3_df['Lambda1_Column'] * 5
    
    # Write the processed data back to S3
    output_key = 'lambda3-processed-data.csv'
    s3_handler.write_df_to_s3(lambda3_df, bucket, output_key)
    
    return {
        'statusCode': 200,
        'body': 'Lambda4 Data processing complete'
    }