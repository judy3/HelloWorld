should configure SMTP for gitlab service.
The docker command is:
sudo docker run --detach \
    --hostname judy-gitlab \
    --publish 8929:80 --publish 2289:22 \
    --name gitlab \
    --restart always \
    --env GITLAB_OMNIBUS_CONFIG="external_url 'http://boostgitlab'; gitlab_rails['gitlab_shell_ssh_port'] = 22;" \
    --volume /srv/gitlab/config:/etc/gitlab \
    --volume /srv/gitlab/logs:/var/log/gitlab \
    --volume /srv/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest
