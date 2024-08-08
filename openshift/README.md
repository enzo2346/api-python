## OpenShift

flask-chart/ contains the helm chart to setup the app in openshift

manifests/ contains the generated files with this helm chart

## Cluster setup

To fix network issue if cluster created in ubuntu 22.04 instead of in Red Hat:

```bash
systemctl disable systemd-resolved.service
rm /etc/resolv.conf
systemctl restart NetworkManager
```

Solution link:
https://labs.consol.de/devops/linux/2019/11/29/codeready-containers-on-ubuntu.html

## Backlog

- fix warnings in tests connection
- optimize deployment process to make it faster
- replace the route to make it work on a classic k8s cluster