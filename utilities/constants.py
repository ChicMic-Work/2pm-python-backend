import pytz, os
from dotenv import load_dotenv

from datetime import datetime, timedelta
from sqlalchemy import func

load_dotenv()
SECRET_KEY  = os.getenv("SECRET_KEY")
ALGORITHM   = os.getenv("ALGORITHM")

EMAIL_HOST          = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER     = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT          = os.getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL  = os.getenv("DEFAULT_FROM_EMAIL")

APPLE_TOKEN_ISS     = os.getenv("APPLE_TOKEN_ISS")
APPLE_TOKEN_AUD     = os.getenv("APPLE_TOKEN_AUD")
APPLE_AUTH_KEY_URL  = os.getenv("APPLE_AUTH_KEY_URL")
GOOGLE_TOKEN_AUD    = os.getenv("GOOGLE_TOKEN_AUD")
GOOGLE_AUTH_KEY_URL = os.getenv("GOOGLE_AUTH_KEY_URL")

#S3
UPLOAD_TO_S3    = os.getenv("UPLOAD_TO_S3")
S3_BUCKET_NAME  = os.getenv("S3_BUCKET_NAME")
CLOUDFRONT_URL  = os.getenv("CLOUDFRONT_URL")
S3_REGION       = os.getenv("S3_REGION")
S3_ACCESS_KEY_ID        = os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY    = os.getenv("S3_SECRET_ACCESS_KEY")

#Redis
REDIS_DB        = int(os.getenv("REDIS_DB"))

access_token_expire = timedelta(days=30)

AuthTokenHeaderKey = "Auth-Token"
protected_endpoints = [
    '/profile/create/', '/profile/alias', '/profile/image/', '/profile/user',
    '/posts/create/', '/profile/choices/', '/auth/logout/'
]


class AddType:

    Insert = 'I'
    Update = 'U'


class ContentType:
    
    daily_club_ans  = "A"
    post            = "P"
    comment         = "C"
    homepage        = "H"

class TableCharLimit:
    post_title  = 70
    post_detail = 5000
    alias       = 20
    bio         = 150
    comment     = 300
    tag         = 25
    feedback    = 1000
    
    _255        = 255
    _330        = 330


class SocialType:
    Google = 0
    Apple = 1

    _0 = "Google"
    _1 = "Apple"
    
    
class ChoicesType:
    Interest_Area = 0
    Language = 1
    
    
class PromoType:
    T = "Free Trial"
    S = "Fee Waiver"
    M = "Manual"
    

class PostType:
    B = "Blog"
    Q = "Question"
    A = "Answer" 
    P = "Poll"
    
    types_list = ['B', 'Q', 'A', 'P']
    
ALIAS_VALID     = "Valid"
ALIAS_INVALID   = "Invalid"
ALIAS_EXISTS    = "Nickname is already in use"
ALIAS_CURRENT   = "Current"
ALIAS_INVALID_CHARACTER = "Your input contains an invalid character"
ALIAS_ATLEAST = "Nickname must contain at least one letter"
ALIAS_STARTS = "Nickname must start with a letter"
ALIAS_ATMOST = "Nickname must not exceed 20 characters"
BIO_ATMOST = "Bio must not exceed 150 characters"
IMAGE_FAIL = "Failed to save image"

"""
TIMEZONE = 'Asia/Kolkata' pytz.timezone(TIMEZONE)
"""