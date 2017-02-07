Deployment using rancher-compose

```
rancher-compose --project-name wordpress -f docker-compose-rancher.yml -e wp.env --url <http://rancher.local/v1/projects/project_id> --access-key <API-accesskey> --secret-key <API-secretkey> --verbose up -d --upgrade --confirm-upgrade --pull
```

Deployment using compose version 3 with Docker Swarm

```
docker stack deploy --compose-file docker-compose.yml wordpress
```

