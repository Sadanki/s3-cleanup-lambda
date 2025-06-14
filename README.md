# 🧹 AWS Lambda: Automated S3 Bucket Cleanup

## 📌 Objective
Automatically delete files older than 30 days from a specific S3 bucket using AWS Lambda and Boto3.

---

## 🛠️ Technologies Used
- AWS Lambda
- Amazon S3
- IAM Role
- Python (Boto3)

---

## 🧪 Steps Performed

### ✅ 1. Created S3 Bucket
- Uploaded multiple files (some simulated as older than 30 days)

### ✅ 2. Created IAM Role for Lambda
- Attached `AmazonS3FullAccess` (for demo purpose)

### ✅ 3. Created Lambda Function
- Runtime: Python 3.12
- Assigned IAM role
- Used Boto3 to delete files older than 30 days

### ✅ 4. Tested Lambda
- Manual test via AWS Console
- Verified S3 to confirm deletion

---

## 💡 Why Use This?

- Automates file cleanup
- Saves cost by deleting unused objects
- Helps with data retention compliance
- Useful for logs, backups, reports, temp data

---

## ⚠️ Limitations

- Uses `LastModified` (upload time, not original file time)
- Needs careful testing to avoid accidental deletion
- Might time out on very large buckets

---

## 📄 License
MIT License
