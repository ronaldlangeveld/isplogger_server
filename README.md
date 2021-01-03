
ISP LOGGER

Thank you for your interest in ISP Logger.
  
The project is still heavily work in progress, but a basic version is working.

What you need:
 

1) Create an account over at https://isplogger.herokuapp.com/

2) Create a network and obtain your Device ID. It's a UUID string.

For simplicity, run this project on Docker, but you're also free to run the python code directly.

It's been tested on MacOS and Linux. 
I'd love it if Windows users can help me out. It should work fine on Docker, but let me know if you have trouble.


3) Pull the project from the Docker Hub Hub (Recommended): `$ docker pull ronaldl93/isp-logger `.

If this is successful, time to run the container,

`$ docker run -it -d -e NETWORK_ID="<the device id you obtained from the website>" ronaldl93/isp-logger`

 
A speed test will now perform once, and then again every 60 minutes.


You can see the results on your account at ISP Logger.

I highly recommend running this on a home server or computer that never sleeps / gets switched off.
I'm using an old-ish computer, running Ubuntu Server.

Something like a Raspberry Pi will work just fine as well. As long as it can run docker, you can run it on any device.