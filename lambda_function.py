import boto3
from datetime import datetime, timezone, timedelta
import logging

# Setup structured logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    bucket_name = 's3-auto-cleanup-bucket'  # ✅ Use your actual bucket name
    days_threshold = 0  # You can set to 0 temporarily for testing

    s3 = boto3.client('s3')
    deleted_files = []
    threshold_date = datetime.now(timezone.utc) - timedelta(days=days_threshold)

    logger.info(f"🔍 Starting cleanup for bucket: {bucket_name}")
    logger.info(f"🕒 Deleting files older than: {threshold_date}")

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            logger.info("📂 No files found in the bucket.")
            return {
                'statusCode': 200,
                'body': {
                    'message': 'No files to delete',
                    'deleted_files': []
                }
            }

        for obj in response['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']

            logger.info(f"🗂 Checking file: {key} | Last Modified: {last_modified}")

            if last_modified < threshold_date:
                try:
                    s3.delete_object(Bucket=bucket_name, Key=key)
                    deleted_files.append(key)
                    logger.info(f"✅ Deleted file: {key}")
                except Exception as delete_err:
                    logger.error(f"❌ Error deleting {key}: {str(delete_err)}")

    except Exception as e:
        logger.error(f"❌ Error listing objects: {str(e)}")
        return {
            'statusCode': 500,
            'body': {
                'message': 'Failed to list or delete objects',
                'error': str(e)
            }
        }

    logger.info(f"🧹 Cleanup completed. Total files deleted: {len(deleted_files)}")

    return {
        'statusCode': 200,
        'body': {
            'message': 'S3 cleanup completed',
            'deleted_files': deleted_files
        }
    }
