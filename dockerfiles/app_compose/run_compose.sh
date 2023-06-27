#!/bin/bash
nobuild=false

# Getting command line args
while getopts n: flag
do
    case "${flag}" in
        n) nobuild=${OPTARG};;
    esac
done

# Building images if necessary
if [ $nobuild == false ]
then
    
    echo 'Building images'
    cd ../..

    # Building pred_service
    cp dockerfiles/predict_service/Dockerfile dockerfiles/predict_service/requirements.txt .
    docker build -t predict_service .

    # Building req_imitation
    cp dockerfiles/requests_imitation/Dockerfile dockerfiles/requests_imitation/requirements.txt .
    docker build -t requests_imitation .

    rm Dockerfile requirements.txt
    cd dockerfiles/app_compose

fi

# Running compose
docker compose down
docker compose up -d