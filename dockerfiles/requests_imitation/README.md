# Requests imitation

Container used for running requests_imitation script. It needs to load predict_service

#### Container Parameters

By default 'developer' branch used for build.

```shell
docker build -t predict_service .
```

You can change branch by adding BRANCH argument. Use --no-cache argument if you need to

```shell
docker build --build-arg BRANCH=fastapi_temp --no-cache -t predict_service .
```

It's necessary to mount folder with images from train dataset

```shell
docker run -d --rm --name requests_imitation -v /home/annual-main-project/datasets/images/train/:/home/annual-main-project/datasets/images/train/ requests_imitation
```

#### Environment Variables

* `BRANCH` - Git repo branch name we want to use

#### Useful File Locations

* `/home/annual-main-project` - WORKDIR. Script is launched from this directory
  
* `/home/annual-main-project/datasets/images/train/` - Images directory

## Built With

* requirements.txt - list of python packages necessary for application working
