## OpenShift

flask-chart/ contains the helm chart to setup the app in openshift

The app have been deployed on a local OpenShift cluster with Ubuntu22.04 and have been exposed using a service ClusterIp and an openshift route.

## Specific setup

To fix cluster network issue because of the network differences between ubuntu 22.04 and Red Hat:

```bash
systemctl disable systemd-resolved.service
rm /etc/resolv.conf
systemctl restart NetworkManager
```

Solution link:
https://labs.consol.de/devops/linux/2019/11/29/codeready-containers-on-ubuntu.html
