---
title: "Setting Up AWS Access Keys"
date: 2017-07-26T09:39:41-07:00
draft: false
tags: ["aws", "amazon web services", "security", "access keys", "biohub", "czbiohub"]
categories: ['aws']
---

Amazon web services are a really powerful ecosystem of storage and compute
infrastructure and are new to me coming from the academic world where I had
access to the university's compute cluster. I've only used AWS a little bit to
host some files but haven't done much.

As part of the Chan Zuckerberg Biohub, I was an "identity access management"
(IAM) user as part of the CZ Biohub organization and I found that figuring out
how to set up my access keys was not straightforward, so here are my
screenshots of figuring it out.

## Step 0

Log in to the [AWS Console](aws.amazon.com).

## Step 1

After you log in to the console, click your name and then "My Security Credentials"

![](/img/aws_step1_from_console.png)

## Step 2
Click "Dashboard"
![](/img/aws_step2_from_security.png)

## Step 3

Click "Rotate your access keys"
![](/img/aws_step3_from_identity_management.png)

## Step 4

In the exposed menu, click "Manage User Access Keys"
![](/img/aws_step4_manage_access_keys.png)

## Step 5

Click "Security Credentials"
![](/img/aws_step5_from_users.png)

## Step 6

Click "Create access key"
![](/img/aws_step6_from_credentials.png)

That will prompt you to download `accessKeys.csv`.

## Step 7: Install AWS CLI

Install the [AWS command line interface](https://github.com/aws/aws-cli)

```
$ pip install awscli
```

## Step 8: Configure AWS CLI to use your access keys
I saved `accessKeys.csv` to my home directory and then `cat`'d it so I could
have it ready to copy/paste and answer the questions asked by `aws configure`:

```
$ aws configure
AWS Access Key ID [****************N4FQ]: 
AWS Secret Access Key [****************mAog]: 
Default region name [us-east-2]: 
Default output format [None]: 
```