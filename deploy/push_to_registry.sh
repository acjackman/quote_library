#! /bin/bash

APP_NAME='quote_library'
SHA1=$1
TAG=$2
REPOSITORY='054430852345.dkr.ecr.us-west-2.amazonaws.com'

# Login to AWS
eval "$(aws ecr get-login --region us-west-2)"

# Tag and push to correct repository
docker tag $APP_NAME:$SHA1 $REPOSITORY/$APP_NAME:$TAG
docker push $REPOSITORY/$APP_NAME:$TAG
