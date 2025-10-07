import json, os, boto3, datetime, io

s3 = boto3.client("s3")
BUCKET = os.environ.get("PM_PACK_BUCKET", "your-bucket-name")

def handler(event, context):
    # Expect payload matching schemas/generate_pm_pack_payload.schema.json
    body = event.get("body")
    if isinstance(body, str):
        body = json.loads(body)
    artifacts = body.get("artifacts", {})
    project = body.get("projectName", "ATLAS_Project")
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    key = f"pm-pack/{project}-{ts}.json"
    s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(body, indent=2).encode("utf-8"), ContentType="application/json")
    url = f"s3://{BUCKET}/{key}"
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"file_url": url, "message": "Saved PM Pack JSON (replace with PDF render)."})
    }
