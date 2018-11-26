## Amazon Web Services EC2 Usage

**Overview:**

This document explains how to access AWS EC2 and how it was used to run the program in the cloud server.

**Setup**

Go to https://aws.amazon.com/. Click on "Sign In to the Console". If you do not already have an account set up, create an account. In the "AWS services" search bar, search "EC2" and click on the EC2 option. Under "Create Instance" click "Launch Instance". Click the "Select" button next to "Amazon Linux 2 AMI (HVM), SSD Volume Type". Click on "Review and Launch" then "Launch". In the drop-down menu select "Create a new key pair", type in a key pair name, click "Download Key Pair", select the check box below, and click "Launch Instance". In the green box at the top of the screen click on Instance ID link, this will open the instance.

**Accessing the instance**

Open command prompt, if using Windows, or Terminal, if using Mac. Type in "ssh  -i ~/*key-pair-location*   ec2-user@*IPv4 Public IP*". This will connect you into the EC2 instance.

**Uploading files into the instance**

Download Cyberduck 2. Open the application. In the dropdown menu, select "SFTP (SSH File Transfer Protocol)". In the Server field, enter the Public DNS. In the Username field enter "ec2-user" [@fa18-423-03-cyberduck-ec2]. In the SSH Private Key field select "Choose" from the dropdown menu and select your .pem key pair file. Click on "Connect". Once connected through Cyberduck, you can simply drag and drop files into the instance.

**Disclaimer**
Our .xml files were greater than 1 GB in size. AWS EC2's free tier only offers up to 1 GB memory therefore we would receive memory errors when running our python files on the server.
