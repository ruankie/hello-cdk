#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import aws_cdk as cdk
from hello_cdk.hello_cdk_stack import HelloCdkStack

# Config
load_dotenv()
AWS_ACCOUNT_ID = os.environ.get("AWS_ACCOUNT")
AWS_REGION = os.environ.get("AWS_REGION")


app = cdk.App()
HelloCdkStack(
    app,
    "HelloCdkStack",
    env=cdk.Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION),
)

app.synth()
