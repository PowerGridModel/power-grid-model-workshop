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

### Preparation for Windows (beginners guide)

1. [Download](https://github.com/PowerGridModel/power-grid-model-workshop/archive/refs/heads/main.zip) (or 
   checkout) this workshop/repository and remember the destination location. For example: 
   `C:\Users\YourUserName\Downloads\power-grid-model-workshop`.

1. Install the latest [Python](https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe) version.
   You probably want the **Windows installer (64-bit)** under **Stable Release**.

1. Now open a terminal (Windows-Key + R, type `cmd`, press **OK**) and use the `cd` (change dir) command to navigate
   to the folder where you downloaded the workshop. For example:
   ```shell
   C:\Users\YourUserName> cd Downloads\power-grid-model-workshop
   C:\Users\YourUserName\Downloads\power-grid-model-workshop>_
   ```
1. Optional: Create and activate a virtual environment. You can skip this step, but it helps you to keep your system
   clean, as we will be installing about 70 Python packages in the next step.
   ```shell
   > python -m venv venv
   > venv\Scripts\activate
   ```
1. install Power Grid Model and some other packages we'll use for this workshop:
    ```shell
    > pip install power-grid-model jupyter pandas matplotlib
    ```
1. Now run jupyter notebook. It will probably (depending on your system) automatically open a browser at
   http://localhost:8888. If not, the console output will tell you where to find the jupyter notebook server.
    ```shell
    > jupyter notebook
    ```
1. Try any of the `.ipynb` files, for example
   [`Power Flow Example.ipynb`](http://localhost:8888/notebooks/examples/Power%20Flow%20Example.ipynb) and press the `>>` 
   button to run the entire file. Note that the last section in the Power Flow Example is about error handling, so 
   don't get scared if you see some error messages there.


### Next time, pick up where you left off

1. Open a terminal (Windows-Key + R, type `cmd`, press **OK**) and use the `cd` (change dir) command to navigate
   to the folder where you downloaded the workshop. For example:
   ```shell
   C:\Users\YourUserName> cd Downloads\power-grid-model-workshop
   C:\Users\YourUserName\Downloads\power-grid-model-workshop>_
   ```
2. Optional: Activate the virtual environment (if you created one initially).
   ```shell
   > venv\Scripts\activate
   ```
3. Run jupyter notebook. It will probably (depending on your system) automatically open a browser at
   http://localhost:8888. If not, the console output will tell you where to find the jupyter notebook server.
    ```shell
    > jupyter notebook
    ```
    
### Preparation for WSL2 or Linux (for advanced users)

If you know WSL2/Linux you should be able to configure environment yourself.

```shell
> pip install power-grid-model jupyter pandas
> jupyter notebook
```

Open the jupyter notebook [`Power Flow Example.ipynb`](http://localhost:8888/Power%20Flow%20Example.ipynb), try to run it. 

## License

This project is licensed under the Mozilla Public License, version 2.0 - see [LICENSE](LICENSE) for details.

## Contributing

Please read [CODE_OF_CONDUCT](https://github.com/PowerGridModel/.github/blob/main/CODE_OF_CONDUCT.md) and [CONTRIBUTING](https://github.com/PowerGridModel/.github/blob/main/CONTRIBUTING.md) for details on the process 
for submitting pull requests to us.

Visit [Contribute](https://github.com/PowerGridModel/power-grid-model-workshop/contribute) for a list of good first issues in this repo.

## Contact

Please read [SUPPORT](https://github.com/PowerGridModel/.github/blob/main/SUPPORT.md) for how to connect and get into contact with the Power Grid Model project.
