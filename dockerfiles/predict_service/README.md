# Predict service

Container with prediction fastapi application

#### Container Parameters

By default 'developer' branch used for build.

```shell
docker build -t predict_service .
```

You can change branch by adding BRANCH argument. Use --no-cache argument if you need to

```shell
docker build --build-arg BRANCH=fastapi_temp --no-cache -t predict_service .
```

Then we can start container 

```shell
docker run -d --rm --name predict_service -p 8000:80 predict_service
```

#### Environment Variables

* `BRANCH` - Git repo branch name we want to use

#### Useful File Locations

* `/home/annual-main-project` - WORKDIR. App launches from this directory
  
* `/home/annual-main-project/databases` - Here we put dwh creds - dwh_def_user.pickle

## Built With

* requirements.txt - list of python packages necessary for application working
* dwh_def_user.pickle - pickle with dwh credentials
