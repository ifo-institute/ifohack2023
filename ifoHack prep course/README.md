## ifoHack 2023 Preparation Course
# by [at]

This repository contains programming tasks for a "Data Science and Engineering Basics for Economics" workshop/training for the ifo Institute.
The tasks are independent projects with data and three notebooks for demos, tasks and solutions.

## Tool Installation

We require the following tools during this workshop.
Please install them in advance.

### Git

Please install the version control system git.
You can check the current version of your git by running `git version` in the terminal (command is unknown, if git is not installed).

- **Windows:** use the [git-for-windows installer](https://gitforwindows.org/)
- **Mac:** use your favorite package manager (e.g., brew via `brew install git`)
- **Linux:** use your favorite package manager (e.g., apt via `sudo apt-get install git-all`)

Note: package managers like brew and apt are useful tools that manage (i.e., install, update and remove) packages and their dependencies for you.

### Conda

Please install the package manager Conda (miniconda might be sufficient).
It simplifies the installation of all required Python packages.
You can check the current version of your Conda by running `conda --version` in the terminal (command is unknown, if Conda is not installed).

- [Windows Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- [Mac Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
- [Linux Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

### Docker

Please install the containerization tool Docker.
The installations below include the Docker Engine and the orchestration tool Docker Compose.
You can check the current version of your Docker by running `docker version` in the terminal (command is unknown, if Docker is not installed or running).

- [Windows Installation](https://docs.docker.com/desktop/install/windows-install/), requires a [WSL 2 backend](https://docs.docker.com/desktop/install/windows-install/#wsl-2-backend)
- [Mac Installation](https://docs.docker.com/desktop/install/mac-install/)
- [Linux Installation](https://docs.docker.com/desktop/install/linux-install/)

### IDE

We recommend to use an Integrated Development Environment (IDE) like [VS Code](https://code.visualstudio.com/) to solve our tasks.
It comes with a lot of useful tools and simpliefies many tasks, e.g., testing, refactoring and exploring.
You should install the [Python extension](https://code.visualstudio.com/docs/languages/python).

## Project Setup

Please setup a conda environment with all required Python packages via `conda env create -f ifo_tasks_environment.yml` from the project's root directory (i.e., the directory where this README is located).
Activate it with `conda activate ifo_tasks`.
We use it for all tasks.