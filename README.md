# ISP Logger

Thank you for your interest in ISP Logger.

The project is still heavily work in progress, but a basic version is working.

# What you need

## Prerequisites

1. Create an account over at https://isplogger.com/

2. Create a network and obtain your Device ID. It's a UUID string.

3. Install Docker, or clone the project repo, then install Python 3.9+ and the project's dependencies.

For simplicity, run this project on Docker, but you're also free to run the python code directly.

It's been tested on MacOS and Linux.

I'd love it if Windows users can help me out. It should work fine on Docker, but let me know if you have trouble.

I highly recommend running this on a home server or computer that never sleeps / gets switched off.
I'm using an old-ish computer, running Ubuntu Server.

Something like a Raspberry Pi will work just fine as well. As long as it can run Docker, you can run it.

## Run in the background

Pull the project from the Docker Hub (recommended):

`$ docker pull ronaldl93/isp-logger`

If this is successful, time to run the container:

`$ docker run -it -d --restart always -e NETWORK_ID="<the device id you obtained from the website>" ronaldl93/isp-logger`

A speed test will now perform once, and then again every 60 minutes. With
Docker's `--restart always` flag, ISP Logger will automatically start on boot.

## Run a one-off test

ISP Logger can run a one-off speed test if e.g., you want to check changes you made to your network.

You can `docker exec` into your existing Docker container and
run the test there, or you can run the Python script natively on your host if
you've installed the dependencies.

```shell
$ docker ps --format "{{.Image}} {{.Names}}"
ronaldl93/isp-logger pensive_napier

$ docker exec -it pensive_napier sh
\ # python script.py --one-shot
```

# Viewing your results

You can see the results in your account on ISP Logger's website, https://isplogger.com/.
