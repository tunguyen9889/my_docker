Deployment using rancher-compose

```
rancher-compose --project-name wordpress -e wp.env --url <http://rancher.local/v1/projects/project_id> --access-key <API-accesskey> --secret-key <API-secretkey> --verbose up -d --upgrade --confirm-upgrade --pull
```

