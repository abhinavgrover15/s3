# s3

This file calculates the size of your S3 bucket.

1. It takes AWS credentials from /etc/boto.cfg. You can configure credentials as you want
2. AWS region is hard-coded in Line 53. You can change region in respect to your S3 bucket.
3. pip_requirements is shipped with this. Please ensure to install modules before running.
4. It takes bucketname as a parameter.
 
    Example Run -:
    python gets3size.py -b "YourS3bucketname"
    
5. Error and Success Logs are stored in '/var/log/gets3size.log'



In case of any queries, please drop an email to "infoabhi88@gmail.com"