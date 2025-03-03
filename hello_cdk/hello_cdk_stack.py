from aws_cdk import (
    Stack,
    aws_lambda as _lambda,  # Import the Lambda module
)
from constructs import Construct


class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function resource
        my_function = _lambda.Function(
            self,
            id="HelloWorldFunction",  # ID within the CDK app
            # function_name="HelloWorldFunction",  # The actual name of the function (optional)
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="index.handler",
            # memory_size=512,  # MB
            code=_lambda.Code.from_inline(
                """
def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello World!'
    }
                """
            ),
        )
