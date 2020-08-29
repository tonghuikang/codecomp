### Facebook Hackercup

Hackercup allows (or rather require) offline computation, and we can get a little bit creative of how we compute. This may also be useful for FBHack if I manage to participate this year.

[TOC]

### Setup

You need to request increase in quota for CPUS.

| Name             | Region          | Requested Limit |
| ---------------- | --------------- | --------------- |
| CPUS             | asia-southeast1 | 96              |
| CPUS_ALL_REGIONS | GLOBAL          | 96              |

You will need to wait some time for this.



##### Create a new notebook instance

- https://console.cloud.google.com/ai-platform/notebooks/
- New Instance
- Python 2/3
- Region `asia-southeast1` (or otherwise as requested for quota)
- Customise
  - Machine Type - `n1-standard-96`
    - **US$2,332.96** ($3.196 hourly)
- When loaded, you can open Jupyterlab

The URL will be something like https://some_base_16-dot-asia-southeast1.notebooks.googleusercontent.com/lab



##### Installation

Clone this repository

```bash
git clone https://github.com/tonghuikang/codecomp
git checkout fb-2020-2
```



##### Install prerequisites

```
pip install ray
```



##### Run samples

```bash
python3 hackercup-sample-1.py < hackercup-sample-1.txt
python3 hackercup-sample-2.py < hackercup-sample-2.txt
```

- Sample 1 is from HackerCup Qualification Round - [Question D2](https://www.facebook.com/codingcompetitions/hacker-cup/2020/qualification-round/problems/D2)
- Sample 2 is from HackerCup Round 1 - [Question A2](https://www.facebook.com/codingcompetitions/hacker-cup/2020/round-1/problems/A2)

You have to download the tests from the website.




##### Networking

For the IP address of your new notebook, go to https://console.cloud.google.com/compute/instances

Copy your `/Users/${USER}/.ssh/id_rsa.pub` on your local computer to `/home/jupyter/.ssh/authorized_keys`



To view ray online

```bash
ssh -N -L localhost:8265:localhost:8265 jupyter@34.126.127.214
```

To sync files

```bash
# rsync to update remote repository
export REPO_DIR_LOCAL=/Users/${USER}/Desktop/codecomp/
export REPO_DIR_REMOTE=jupyter@34.126.127.214:/home/jupyter/codecomp/
alias uphacker="rsync -avz --exclude=.git/ --exclude='*.pyc' $REPO_DIR_LOCAL $REPO_DIR_REMOTE"

# to execute
uphacker
```



Try running the samples on remote to ensure that they work. You can view the progress on `localhost:8265`



##### Operation procedure on testing

Start the ray stream to remote. This will occupy one terminal

```bash
ssh -N -L localhost:8265:localhost:8265 jupyter@34.126.127.214
```



The testing file will be downloaded in the downloads folder. Please ensure that you are in the correct environment

```bash
export REPO_DIR_LOCAL=/Users/${USER}/Desktop/codecomp/

# move and rename file
cd ~/Downloads
mv .txt $REPO_DIR_LOCAL/template/b.val.txt
```



Compute on local

```bash
# run a copy offline, run in the template folder
python b.py < b.val.txt > b.val.out 

# upload file
uphacker
```



Compute on remote

```bash
# make sure you are already in the template folder
python b.py < b.val.txt > b.val.out
```



Download the output with UI and submit.



##### Closing

Please remember to delete the instance, or you will be billed hundreds, if not thousands.





### Planet-scale

I can scale this to 96 CPUs, but I hope to scale to 1 million CPUs with little latency. I still have not idea on how to do that latter.