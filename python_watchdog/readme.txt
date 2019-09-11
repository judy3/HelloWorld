Before using watchdog, you need to install it.
ref: https://github.com/gorakhargosh/watchdog/

If you'd like to cotinueously monitor, you can make the script auto start when restart the server. 
I've configured a systemd job.

1)cd /etc/systemd/system
2)vim monitorsftp.service
[Unit]
Description=Monitor SFTP
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python /root/scripts/monitor_files.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target

3)systemctl daemon-reload
4)systemctl start monitorsftp.service
5)systemctl status monitorsftp.service
