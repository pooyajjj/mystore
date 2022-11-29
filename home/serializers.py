from rest_framework import serializers


class UserDetailSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.IntegerField()


# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2OTg0ODMzMiwiaWF0IjoxNjY5NzYxOTMyLCJqdGkiOiI0NTY0ZTUxNzgwZTY0NThhYmE2NWRmYWM3Y2EyZWRjOSIsInVzZXJfaWQiOjR9.zj7jdvTRpKT4S3deFD_Dj5yS3dodnwj33DA1do539-k",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMTkzOTMyLCJpYXQiOjE2Njk3NjE5MzIsImp0aSI6IjJhMThiODU0YzYzNDQxYmQ4OTFiMzA2NTRlZWE1Zjk0IiwidXNlcl9pZCI6NH0.0X2alYblK0tKsUgvgziKog-EPvfn-aYQRz1YTAUeKGU"
# }