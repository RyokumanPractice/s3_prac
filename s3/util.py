import boto3
import time
from io import BytesIO
from s3_prac.settings import S3_ACCESS_KEY, S3_SECRET_KEY


def image_upload_s3(uploaded_image, user_name):
    s3_client = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY)
    key = user_name + str(int(time.time()))
    s3_client.upload_fileobj(uploaded_image, 'ryokumantest', key)
    image_url = "https://ryokumantest.s3.ap-northeast-2.amazonaws.com/" + key
    return image_url
