# check-s3-server-side-encryption

Simple script written in Python 3 that will check a given AWS account for the status of the default server-side encryption for all the S3 buckets and enable default server-side encryption with AES256 for S3 buckets with no current server-side encryption configuration.

## Prerequisites

Following Python 3 libraries are required.
```
boto3
botocore
```

AWS named profile and credentials should be configured - [Read more](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

## Installation

* Clone the git repository
```
git clone git@github.com:thilinajayanath/check-s3-server-side-encryption.git
```

It is recommended to use a Python 3 virtual environment to install external libraries [Read more](https://docs.python.org/3/library/venv.html)
Required libraries can be installed with the requirements.txt file to the virtual environment[Read more](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

```
python3 -m venv /path/to/new/virtual/environment
/path/to/new/virtual/environment/bin/pip install -r requirements.txt
```

## Run the application

```
cd s3-server-side-encryption-checker
chmod u+x enable-s3-encryption.py
/path/to/new/virtual/environment/bin/python enable-s3-encryption.py <AWS-PROFILE-NAME>
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
