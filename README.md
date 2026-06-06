# pipeline-kfp

## Disclaimer
This project or the binary files available in the `Releases` area are `NOT` delivered and/or released by Red Hat. This is an independent project to help with the understanding of pipeline KFP.

---

## Let's check two very basic Pipelines

### basic.py

This is a very simple workflow, just for demo/study purposes.


### basic_using_parallelfor.py

This is a very simple workflow, just for demo/study purposes. In this case, we are using `ParallelFor`, which will allow you to `iterate`


## How to Use it?

- Create a virtual environment
```
$ python -m venv ~/.venv/pipeline
$ source ~/.venv/pipeline/bin/activate
(pipeline) $
```

- Install kpf module
```
(pipeline) $ pip install kfp
```

- To generate the output from the examples above
```
(pipeline) $ python basic.py
(pipeline) $ ls basic.yaml
basic.yaml
```

```
(pipeline) $ python basic_using_parallelfor.py
(pipeline) $ ls basic_using_parallelfor.yaml
basic_using_parallelfor.yaml
```

From this point, you should be good to go, access your `RHOAI` webUI, Click on your `DataScience` Project, `Pipelines`, and import the `YAML` file generated above.

In case you need to update the file/logic. `DON'T` change your `YAML`, instead, update your `.py` code, rerun the step above, which will create a new `YAML` file, then you can update it via `RHOAI` webUI.

## What are in this folder?

```
basic_using_parallelfor.py   <-- The code using ParallelFor
basic_using_parallelfor.yaml <-- The output generated when executing "python basic_using_parallelfor.py"

basic.py   <-- Simple code
basic.yaml <-- The output generated when executing "python basic.py"
```



Thank you!<br>
Waldirio