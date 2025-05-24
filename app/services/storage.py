import json
from minio import Minio
from minio.error import S3Error
from io import BytesIO
from app.core.config import settings
from typing import Dict, List, Optional


class MinioController(Minio):
    def __init__(self, endpoint: str, bucket_name: str, access_key: str, secret_key: str, secure: bool = True):
        self.client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )
        self.bucket_name = bucket_name
        self.ensure_bucket(self.bucket_name)

    def ensure_bucket(self, bucket_name: str) -> bool:
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
            return True
        except S3Error as err:
            print(f"Error checking/creating bucket: {err}")
            return False

    def get_users(self) -> Dict:
        obj = self.client.get_object(bucket_name=self.bucket_name, object_name="users.json")
        content = json.load(BytesIO(obj.read()))
        return content

minio_ctrl = MinioController(
    endpoint=settings.minio_host,
    bucket_name=settings.minio_bucket,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=settings.minio_secure
)