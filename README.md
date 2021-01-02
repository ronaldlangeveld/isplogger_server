ISP LOGGER

Hello. 

Thank you for your interest in ISP Logger.

The project is still heavily work in progress, but a basic version is working.

What you need:

1) Create an account over at https://isplogger.herokuapp.com/
2) Create a network and obtain your Device ID. It's a UUID string.


For simplicity, run this project on Docker, but you're also free to run natively.

It's been tested on MacOS. It should work similarly on Linux. 

I'd love it if Windows users can help me out. Just contribute. 

3) Clone the Repository on the device you'll be using as a test server. If possible install on a device that's always on. Perhaps, even better if you have a home server, raspberry pi or similar.

Docker Instruction:

Locate the cloned repository in your terminal. 
build the container by writing: `$ docker build -t isp-logger-tester .`

If this is successful, time to run the container,

    $ docker run -it -d -e NETWORK_ID="<the device id you obtained from the website" isp-logger-tester

A speed test will now perform once, and then again every 60 minutes. 

You can see the results on your account at ISP Logger.


