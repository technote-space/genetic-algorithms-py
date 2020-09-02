## Genetic Algorithms for Python

Genetic Algorithms for Python.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Details</summary>

- [Setup](#setup)
- [Run](#run)
- [Play](#play)
  - [Task](#task)
- [Linter](#linter)
- [Docker](#docker)
  - [Build Docker Image](#build-docker-image)
  - [Run](#run-1)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Setup
```shell script
curl -L 'https://raw.githubusercontent.com/technote-space/python-setup/master/bin/setup.sh' | bash -s -- 3.7.7 ga
pipenv install -d
```

## Run
```shell script
python src/app.py [task]
```

## Play
```shell script
python src/app.py -p [task]
```

### Task
#### Santa Fe Trail
`santa-fe-trail`

![Santa Fe Trail](https://raw.githubusercontent.com/technote-space/genetic-algorithms-py/images/santa-fe-trail.png)

#### Cart Pole
`cart-pole`

![Cart Pole](https://raw.githubusercontent.com/technote-space/genetic-algorithms-py/images/cart-pole.gif)

#### Mountain Car
`mountain-car`

![Mountain Car](https://raw.githubusercontent.com/technote-space/genetic-algorithms-py/images/mountain-car.gif)


## Linter
lint
```shell script
pipenv run lint
```

format
```shell script
pipenv run format
```

## Docker
### Build Docker Image
```shell script
docker build -t ga:latest .
```

### Run
```shell script
docker run ga:latest [task]
```
