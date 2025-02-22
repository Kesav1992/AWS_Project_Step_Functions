from aws.Layers.common_aws_utils import S3Handler
import pandas as pd

def lambda_handler(event, context):
    s3_handler = S3Handler()
    # Read the CSV file from S3
    bucket = 'k7-bucket-main1'
    key = 'lambda1-processed-data.csv'
    lambda2_df = s3_handler.read_csv_from_s3(bucket, key)
    
    # Perform some data processing
    lambda2_df['Lambda2_Column'] = lambda2_df['Lambda1_Column'] * 3
    
    # Write the processed data back to S3
    output_key = 'lambda2-processed-data.csv'
    s3_handler.write_df_to_s3(lambda2_df, bucket, output_key)
    
    return {
        'statusCode': 200,
        'body': 'Lambda2 Data processing complete'
    }
    
    