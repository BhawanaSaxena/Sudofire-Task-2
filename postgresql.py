import psycopg2
import subprocess

#Database connection parameters
DB_HOST = "localhost"
DB_NAME = "test1"
DB_USER = "test1"
DB_PASSWORD = "test"


#Back up the file name and path:

BACKUP_FILE = "C:\Users\bhawansa\OneDrive - AMDOCS\Backup Folders\Desktop\Visual Studio code\myproject\db.sqlite3"

#Connect to the database:

conn = psycopg2.connect(host = DB_HOST,
                        dbname = DB_NAME,
                        user = DB_USER,
                        password = DB_PASSWORD)

#Creating a backup using the pg_dump command:

import boto3

#s3 bucket details

S3_BUCKET_NAME = "mybucket"
S3_OBJECT_KEY = "backup.sql"

#AWS credentials

AWS_ACCESS_KEY_ID = "AKIAVIKWOIGC5KBT72NR"
AWS_SECRET_ACCESS_KEY = "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"

#Uploadin the backup file to S3

s3 = boto3.client("s3",
                  aws_access_key_id = AWS_ACCESS_KEY_ID,
                  aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

with open(BACKUP_FILE,"rb") as f:
    s3.upload_fileobj(f,S3_BUCKET_NAME,S3_OBJECT_KEY)

subprocess.run(["pg_dump","-Fc","-f",BACKUP_FILE,"-d",DB_NAME])

#Close the database connection

conn.close()
