# AirDrop
Send or recieve files not so quickly...

----

This is a simple Python program that allows you to transfer files from one device to another over a network using sockets.

## Usage

To use the program, you will need to have Python 3 installed on both the sender and receiver devices.

### Sender

1. Open a terminal window and navigate to the directory where the `sender.py` script is located.

2. Run the script with the following command:

```
python sender.py <filename> <receiver_ip> <port_number>
```

where `<filename>` is the name of the file you want to send, `<receiver_ip>` is the IP address or hostname of the device you want to send the file to, and `<port_number>` is the port number you want to use for the transfer.

For example, if you want to send a file named `my_file.txt` to a device with IP address `192.168.1.100` using port `8000`, you would run the following command:

```
python sender.py my_file.txt 192.168.1.100 8000
```


### Receiver

1. Open a terminal window and navigate to the directory where the `receive_file.py` script is located.

2. Run the script with the following command:

```
python reciever.py <filename> <port_number>
```


where `<filename>` is the name you want to save the received file as, and `<port_number>` is the same port number that was used by the sender.

For example, if you want to save the received file as `received_file.txt` and the sender used port `8000`, you would run the following command:

```
python reciever.py received_file.txt 8000
```



## Parameters

- `<filename>`: The name of the file you want to send or save.

- `<receiver_ip>`: The IP address or hostname of the device you want to send the file to.

- `<port_number>`: The port number you want to use for the transfer. This should be the same on both the sender and receiver devices.
