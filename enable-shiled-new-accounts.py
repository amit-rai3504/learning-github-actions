import json

def get_account_detils(event):
    account_details = {}

    if "detail" in event and "eventName" in event["detail"] and event["detail"]["eventName"] == "CreateManagedAccount":
        account_details["accountId"] = event["detail"]["serviceEventDetails"]["createManagedAccountStatus"]["account"]["accountId"]
        account_details["accountName"] = event["detail"]["serviceEventDetails"]["createManagedAccountStatus"]["account"]["accountName"]
    
    else:
        account_details["accountId"] = event["detail"]["serviceEventDetails"]["createAccountStatus"]["accountId"]
        account_details["accountName"] = event["detail"]["serviceEventDetails"]["createAccountStatus"]["accountName"]

    return account_details



def lambda_handler(event, context):
    account_details = get_account_detils(event)
    account_id = account_details["accountId"]
    account_name = account_details["accountName"]
    print(f"New AWS Account Created  account_name : {account_name} and account_id : {account_id}  Event")


event = {
    "version": "0",
    "id": "999cccaa-eaaa-0000-1111-123456789012",
    "detail-type": "AWS Service Event via CloudTrail",
    "source": "aws.organizations",
    "account": "123456789012",
    "time": "2018-08-30T21:42:18Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
      "eventVersion": "1.05",
      "userIdentity": {
        "accountId": "123456789012",
        "invokedBy": "AWS Internal"
      },
      "eventTime": "2018-08-30T21:42:18Z",
      "eventSource": "organizations.amazonaws.com",
      "eventName": "CreateAccountResult",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "AWS Internal",
      "userAgent": "AWS Internal",
      "eventID": "0000000-0000-0000-1111-123456789012",
      "eventType": "AwsServiceEvent",
      "serviceEventDetails": {
        "createAccountStatus": {
          "id": "car-000000000000000000000000000000",
          "state": "SUCCEEDED",
          "accountName": "****",
          "accountId": "123456789012",
          "requestedTimestamp": "Aug 30, 2018 9:42:14 PM",
          "completedTimestamp": "Aug 30, 2018 9:42:18 PM"
        }
      }
    }
  }

lambda_handler(event,"xyz")
