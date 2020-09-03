# Genetic Algorithms

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

[Wikipedia](https://en.wikipedia.org/wiki/Santa_Fe_Trail_problem)

![Santa Fe Trail](https://raw.githubusercontent.com/technote-space/genetic-algorithms-py/images/santa-fe-trail.gif)

#### Cart Pole
`cart-pole`

[Environment](https://github.com/openai/gym/wiki/CartPole-v0)

![Cart Pole](https://raw.githubusercontent.com/technote-space/genetic-algorithms-py/images/cart-pole.gif)

* [Generated Source Code](./samples/cart-pole)
* [Generated Algorithm](./samples/cart-pole/packages/algorithm.py)

#### Mountain Car
`mountain-car`

[Environment](https://github.com/openai/gym/wiki/MountainCar-v0)

![Mountain Car](https://raw.githubusercontent.com/technote-space/genetic-algorithms-py/images/mountain-car.gif)

* [Generated Source Code](./samples/mountain-car)
* [Generated Algorithm](./samples/mountain-car/packages/algorithm.py)

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
