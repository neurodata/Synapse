# Neurodata's Opensource Method for Autonomous Detection of Synapses (NOMADS)
![Build Status](https://travis-ci.org/neurodata/nomads_deploy.svg?branch=master)

### 0) Run the setup script found [here](https://cdn.rawgit.com/neurodata/nomads_deploy/master/setup.sh)

### 1) Upon running the setup script, you will see this screen:

![tut_1](https://github.com/neurodata/nomads_deploy/blob/master/README_assets/tut_1.png)

### 2) Click on the Upload File Button to select your data
  - The pipeline expects that your data is formatted in the following way:
    - 2 by Z by Y by X TIFF image
    - Channel 0 corresponds to the PRESYNAPTIC biomarker
    - Channel 1 corresponds to the POSTSYNAPTIC biomarker

![tut_2](https://github.com/neurodata/nomads_deploy/blob/master/README_assets/tut_2.png)

### 3) Click on the Launch NOMADS button to launch the pipeline.
  - You will see a loading symbol by the tab in your browser. This means the pipeline is running.

![tut_3](https://github.com/neurodata/nomads_deploy/blob/master/README_assets/tut_3.png)

### 4) Get your Results!
  - Nomads will ouput a file named results.tiff for you to download with your results  

![tut_4](https://github.com/neurodata/nomads_deploy/blob/master/README_assets/tut_4.png)
