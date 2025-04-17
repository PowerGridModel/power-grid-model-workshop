<!--
SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>

SPDX-License-Identifier: MPL-2.0
-->

# Power Grid Model Workshop

The steps for the workshop are to follow `Power Flow Example.ipynb` and `Power Flow Assignment.ipynb` simultaneously.
To complete the workshop on your own, go through `Power Flow Example` notebook while completing the respective assignment from at each checkpoint.
If you like to be guided through the workshop, please visit our [Power Grid Model Workshop](https://www.youtube.com/watch?v=Y8ejfZnnfPM) recording.

## Pre-knowledge

Participants are expected to have knowledge of 
[Juypter Notebook](https://jupyter.org/) and
[numpy](https://numpy.org/).

It is recommended to read the numpy structured array 
[documentation](https://numpy.org/doc/stable/user/basics.rec.html).

## Preparation

Please create the relevant environment before the workshop. If you encounter problems, please raise a question in the [discussion board](https://github.com/orgs/PowerGridModel/discussions)

### Preparation with uv (Windows/Mac/Linux)
1. Open a terminal
   - Windows: Press `Windows-Key + R`, type `cmd`, press **OK**
   - Mac/Linux: Open a terminal
1. Download or clone this workshop/repository
   - if you download the repository, remember the destination location. For example:
     - Windows:`C:\Users\YourUserName\Downloads\power-grid-model-workshop`
     - Mac/Linux: `~/Downloads/power-grid-model-workshop`
1. Install the `uv` package manager [link](https://docs.astral.sh/uv/getting-started/installation)
for your operating system (Windows/Mac/Linux)
1. Navigate to the repository folder
    - Windows: `cd Downloads\power-grid-model-workshop`
    - Mac/Linux: `cd ~/Downloads/power-grid-model-workshop`
1. Setup python environment and install dependencies using `uv`:
    ```shell
    uv sync
    ```
1. Start jupyter notebook. It will probably (depending on your system) automatically open a browser at
   http://localhost:8888. If not, the console output will tell you where to find the jupyter notebook server.
    ```shell
    uv run jupyter notebook
    ```
1. Try any of the `.ipynb` files, for example
   [`Power Flow Example.ipynb`](http://localhost:8888/notebooks/examples/Power%20Flow%20Example.ipynb) and press the `>>` 
   button to run the entire file. Note that the last section in the Power Flow Example is about error handling, so 
   don't get scared if you see some error messages there.

### Next time, pick up where you left off

1. Again, open a terminal
   - Windows: Press `Windows-Key + R`, type `cmd`, press **OK**
   - Mac/Linux: Open a terminal
1. Navigate to the repository folder
   - Example:
     - Windows: `cd Downloads\power-grid-model-workshop`
     - Mac/Linux: `cd ~/Downloads/power-grid-model-workshop`

1. Start jupyter notebook. It will probably (depending on your system) automatically open a browser at
   http://localhost:8888. If not, the console output will tell you where to find the jupyter notebook server.
    ```shell
    uv run jupyter notebook

## License

This project is licensed under the Mozilla Public License, version 2.0 - see [LICENSE](LICENSE) for details.

## Contributing

Please read [CODE_OF_CONDUCT](https://github.com/PowerGridModel/.github/blob/main/CODE_OF_CONDUCT.md) and [CONTRIBUTING](https://github.com/PowerGridModel/.github/blob/main/CONTRIBUTING.md) for details on the process 
for submitting pull requests to us.

Visit [Contribute](https://github.com/PowerGridModel/power-grid-model-workshop/contribute) for a list of good first issues in this repo.

## Contact

Please read [SUPPORT](https://github.com/PowerGridModel/.github/blob/main/SUPPORT.md) for how to connect and get into contact with the Power Grid Model project.
