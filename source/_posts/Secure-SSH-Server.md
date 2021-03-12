---
title: 4 Ways to Secure your Server
tags:
  - SSH
  - Server
  - Security
categories:
  - Tutorials
date: 2021-03-12 15:45:53
---

Requirements:

1. Texteditor e.g. nano
2. SSH server
3. sudo installed and configured
(4. Ubuntu Server 20.04)

## 1. 4 Ways to Secure your Server

1. <a href="#1-Public-Key-Authentication">Public Key Authentication (SSH Keys)</a>
2. <a href="#2-Fail2Ban">Fail2Ban</a>
3. <a href="#3-Custom-SSH-Settings">Custom SSH Settings</a>
4. <a href="#4-Firewall">Firewall</a>

## 1. Public Key Authentication

### 1.1 Different Methods

#### 1.1.1 Using OpenSSh

Open CMD and enter: `ssh-keygen`
Enter a Path where to save to: Press Enter
Enter passphrase: you can leave this empty or set one.
**IMPORTANT: DON'T FORGET YOUR PASSPHRASE IF YOU SET ONE**

Press "WIN" + "R" and enter `%userprofile%\.ssh\`. There is your SSH Key located.

#### 1.1.2 Using PuTTY

[Install Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

Open "PuTTYgen"
Press on "Generate" and move your mouse around.

If you want to use a Passphrase enter it in "Key passphrase" and "Confirm passphrase"
**IMPORTANT: DON'T FORGET YOUR PASSPHRASE IF YOU SET ONE**

Press on "Save private key" and choose and remember where to put it

Copy the Public Key from the Field. This is what we upload into our server
**IMPORTANT: KEEP YOUR PRIVATE KEY SECURE! DON'T SHARE IT**

### 1.2 Upload Public SSH Keys

SSH into your server.
With OpenSSH or PuTTY doesn't matter

Now Copy the Following Commands:

```bash
cd ~
mkdir ~/.ssh # make ssh directory
chmod 700 ~/.ssh # correct permissions
touch ~/.ssh/authorized_keys # create file for keys
chmod 600 ~/.ssh/authorized_keys # correct permissions
```

Now open `~/.ssh/authorized_keys` with your favourite text editor. I use `nano`

```bash
nano ~/.ssh/authorized_keys
```

Insert the Public Key.
From Putty it was the one inside the Box
From OpenSSH Default Location: `%userprofile%\.ssh\id_rsa.pub`

Copy the whole key into the file with `Right-Click` or "Ctrl" + "V"

To save press
"Ctrl" + "X" -> "y" -> "Enter"

Now restart your OpenSSH Daemon to affect changes

```bash
sudo systemctl restart sshd
```

### 1.3 Login with SSH keys

If you use OpenSSH login with

```bash
ssh <username>@<ip> -p <port> -i <location of private key>
```

## 2. Fail2Ban

Update Packages and install fail2ban

```bash
sudo apt update
sudo apt install fail2ban -y
```

Copy Config file and restart fail2ban

```bash
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
systemctl restart fail2ban
```

Check if fail2ban is running

```bash
sudo systemctl status fail2ban
```

It should look something like this:

```bash
● fail2ban.service - Fail2Ban Service
     Loaded: loaded (/lib/systemd/system/fail2ban.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2020-08-19 06:16:29 UTC; 27s ago
       Docs: man:fail2ban(1)
   Main PID: 1251 (f2b/server)
      Tasks: 5 (limit: 1079)
     Memory: 13.8M
     CGroup: /system.slice/fail2ban.service
             └─1251 /usr/bin/python3 /usr/bin/fail2ban-server -xf start

```

Edit the fail2ban config file

```bash
sudo nano /etc/fail2ban/jail.local
```

Replace
`#bantime.increment = true` with `bantime.increment = true`
The more fails the longer ban
`bantime  = 10m` with `bantime  = 1h`
Longer bantime

See all Jails

```bash
JAILS=`sudo fail2ban-client status | grep "Jail list" | sed -E 's/^[^:]+:[ \t]+//' | sed 's/,//g'`
  for JAIL in $JAILS
  do
    sudo fail2ban-client status $JAIL
  done
```

You should see:

```bash
Status for the jail: sshd
|- Filter
|  |- Currently failed: 0
|  |- Total failed:     0
|  `- File list:        /var/log/auth.log
`- Actions
   |- Currently banned: 0
   |- Total banned:     0
   `- Banned IP list:
```

Restart fail2ban

```bash
sudo systemctl restart fail2ban
```

## 3. Custom SSH Settings

Open SSHd Config

If you don't have all options are others are from default on the right thing it is fine

```bash
sudo nano /etc/ssh/sshd_config
```

Replace
`#Port 22` with `Port <any number from 1024 to 65353>`
Port SSH is listening on. Protects against automated bots but not against humans
My Config: `Port 1024`

Replace
`PermitEmptyPasswords yes` with `PermitEmptyPasswords no`
Don't allow empty passwords

Replace
`X11Forwarding yes` with `X11Forwarding no`
Don't allow Graphic Forwarding

**Only if you have Public Key Authentication enabled and working. Otherwise you cant SSH into your server anymore**
Replace
`#PasswordAuthentication yes` with `PasswordAuthentication no`
Don't allow Password Authentication

**Only if you have another user than root with sudo rights**
Replace
`#PermitRootLogin yes` with `PermitRootLogin no`
Don't allow Password Authentication

Restart sshd to affect changes

```bash
sudo service sshd restart
```

My Config:

```ssh_config
Include /etc/ssh/sshd_config.d/*.conf

Port 1024

# Authentication:

LoginGraceTime 1m
PermitRootLogin no
#StrictModes yes
MaxAuthTries 3

PubkeyAuthentication yes


# To disable tunneled clear text passwords, change to no here!
PasswordAuthentication no
PermitEmptyPasswords no

# Change to yes to enable challenge-response passwords (beware issues with
# some PAM modules and threads)
ChallengeResponseAuthentication no

UsePAM yes

X11Forwarding no

# Allow client to pass locale environment variables
AcceptEnv LANG LC_*

# override default of no subsystems
Subsystem       sftp    /usr/lib/openssh/sftp-server
```

Edit fail2ban config because you changed the ssh port

Search in `/etc/fail2ban/jail.local`

```ini
[ssh]
enabled  = true
port     = ssh
```

And set `port = <ssh port>`
In my case: `port = 1024`

### 3.1 Login with Custom Port

If you use OpenSSH login with

```bash
ssh <username>@<ip> -p <port> -i <location of private key>
```

## 4. Firewall

Install UFW

```bash
sudo apt update
sudo apt install ufw
```

Enable Ports

```bash
sudo ufw allow <port>/<protocol>
```

### 4.1 Allow Ports

To enable SSH Port 1024 on TCP

```bash
sudo ufw allow 1024/tcp
```

To enable HTTP and HTTPS

```bash
sudo ufw allow http
sudo ufw allow https
```

To enable Imap and Smtp

```bash
sudo ufw allow imap
sudo ufw allow https
```

### 4.2 Remove Rules

To remove HTTP and HTTPS

```bash
sudo ufw delete allow http
sudo ufw delete allow https
```

To remove Port 88 on TCP

```bash
sudo ufw delete allow 88/tcp
```

To remove specific rule

```bash
sudo ufw status numbered
sudo ufw delete <number>
```
