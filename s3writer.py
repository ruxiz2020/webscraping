import json
import boto3


def s3writer(json_data, s3filename, bucket='breakingpet1.s3.us-west-1.aws.com'):

    s3 = boto3.resource('s3')
    s3object = s3.Object(bucket, s3filename)

    s3object.put(
        Body=(bytes(json.dumps(json_data).encode('UTF-8')))
    )
