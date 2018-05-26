import botocore
class S3MediaStorage:
  
  def __init__(self, s3, bucket_name):
    self.s3 = s3
    self.bucket_name = bucket_name
 
  def save(self, path, file_to_be_uploaded):
    bucket = self.s3.Bucket(self.bucket_name)
    bucket.put_object(Key=path, Body=file_to_be_uploaded)
  
  def contains(self, path):
    try:
      self.s3.Object(self.bucket_name, path).load()
      return True
    except botocore.exceptions.ClientError as e:
      return False
