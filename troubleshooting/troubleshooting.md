# Troubleshooting
I've seen two big issues pop up: database errors and port 80 errors.

---
## Fixing Database Issues
If the $coursename container doesn't start, make sure to check the logs. If you see "Waiting for the db", it's a simple fix. Stop the $coursename and db containers. 

![db_error.png](/assets/db_error.png)

Delete the contents of /var/lib/docker/volumes/classes/$coursename/db/mysql
```
sudo rm -rf /var/lib/docker/volumes/classes/$coursename/db/mysql
``` 
And then recreate the folder:
```
sudo mkdir /var/lib/docker/volumes/classes/$coursename/db/mysql
```
After that, restart the db container and then the $coursename container. 

---

## Fixing the Port Errors
Sometimes when trying to start SWAG, you'll be told that port ## is in use. First, identify what is using that port.
```
sudo netstat -tulpn | grep LISTEN
```
![port_error.png](/assets/port_error.png)

And then kill that service. It's likely just nginx or apache that, for some reason, are pre-installed on your server. You may have to google the exact syntax, but it'll be something like:
```
sudo service apache2 stop
```
or
```
sudo systemctl stop nginx
```