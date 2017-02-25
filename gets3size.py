__author = "Abhinav Grover"

import boto3
import sys
import logging
import argparse
import math


global LOGGER


def get_bucket_size(s3client, bucketname):

    total_bytes = 0
    n = 0

    response = s3client.list_objects(Bucket=bucketname)

    if 'Contents' in response:
        print "Yes"
        for key in s3client.list_objects(Bucket=bucketname)['Contents']:
            total_bytes += key['Size']
            n += 1
            if n % 2000 == 0:
                print n
    else:
        print "No"
        total_bytes = 0

    return total_bytes

def main():
    global LOGGER

    FORMAT = '%(levelname)s: %(asctime)-15s: %(filename)s: %(funcName)s: %(module)s: %(message)s'
    logging.basicConfig(filename="/var/log/gets3size.log", level=logging.DEBUG, format=FORMAT)
    LOGGER = logging.getLogger("S3Size")

    """ Define Argument Parsing """
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket', help='Bucket Name', required=True)

    args = parser.parse_args()

    """ Get Dynamic dictionary values """
    bucketname = "%s" % args.bucket

    s3client = boto3.client('s3', region_name='ap-south-1')

    try:
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")

        total_size = get_bucket_size(s3client, bucketname)

        if (total_size == 0):
            print 'Total Size is 0 Bytes'
        else:
            i = int(math.floor(math.log(total_size, 1024)))
            p = math.pow(1024, i)
            total_gigs = round(total_size / p, 2)

            print 'Total Size is %s %s' % (total_gigs, size_name[i])

    except Exception as e:
        LOGGER.error(e)

if __name__ == '__main__':
    main()