# About this Repo

This is the Git repo of my own Docker container which run crond jobs.

### Usage
- Put the scripts (with the *shebang* in the beginning of script) into the `tasks/{15min,daily,hourly,monthly,weekly}` directories. See this [note](http://archive.oreilly.com/pub/post/runparts_scripts_a_note_about.html) about naming convention for running scripts in `run-parts`.
- Modified `crontime` file as you wanted.

### Build the image
```
$ docker build --rm -t vitamingaugau/alpine:crond .
```

### Run the container
```
$ docker run -d -it --name my-cron-container -e PACKTEMAIL=<packtpub_email> -e PACKTPASSWD=<packtpub_password> -e SLACKHOOK=<Slack_webhook_URL> --restart=always vitamingaugau/alpine:crond
```

### Test your crond
```
$ docker exec -it my-cron-container run-parts --test /etc/periodic/daily
```
