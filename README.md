# power-grid-model-workshop

The steps for workshop are to follow `Power Flow Example.ipynb` and `Power Flow Assignment.ipynb` simultaneously.
To complete the workshop on your own, go through `Power Flow Example` notebook while completing the respective assignment from at each checkpoint.


# Pre-knowledge

Participants are expected to have knowledge of 
[Juypter Notebook](https://jupyter.org/) and
[numpy](https://numpy.org/).

It is recommended to read the numpy structured array 
[documentation](https://numpy.org/doc/stable/user/basics.rec.html).

# Preparation for Windows (beginners guide)

1. [Download](https://github.com/alliander-opensource/power-grid-model-workshop/archive/refs/heads/master.zip) (or 
   checkout) this workshop/repository and remember the destination location. For example: 
   `C:\Users\YourUserName\Downloads\power-grid-model-workshop`.

1. Install the latest [Python](https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe) version.
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
    > pip install power-grid-model jupyter pandas
    ```
1. Now run jupyter notebook. It will probably (depending on your system) automatically open a browser at
   http://localhost:8888. If not, the console output will tell you where to find the jupyter notebook server.
    ```shell
    > jupyter notebook
    ```
1. Try any of the `.ipynb` files, for example
   [`Power Flow Example.ipynb`](http://localhost:8888/notebooks/Power%20Flow%20Example.ipynb) and press the `>>` 
   button to run the entire file. Note that the last section in the Power Flow Example is about error handling, so 
   don't get scared if you see some error messages there.


# Next time, pick up where you left off
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

    
# Preparation for WSL2 or Linux (for advanced users)

If you know WSL2/Linux you should be able to configure environment yourself.

```shell
> pip install power-grid-model jupyter pandas
> jupyter notebook
```
Open the jupyter notebook [`Power Flow Example.ipynb`](http://localhost:8888/notebooks/Power%20Flow%20Example.ipynb), try to run it. 

# Support

Please create the relevant environment before the workshop. If you encounter problems, please contact
[Tony Xiang](https://github.com/TonyXiang8787),
[Peter Salemink](https://github.com/petersalemink95), or
[Bram Stoeller](https://github.com/bramstoeller).
