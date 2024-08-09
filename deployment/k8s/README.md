## OpenShift

flask-chart/ contains the helm chart to setup the app in k8s

The app have been deployed on a Docker-Desktop k8s and have been exposed using a NodePort service. This is not a productive solution where we should use ClusterIp, loadbalancers or Ingress.

## Specific setup

In Windows, to allow docker-desktop to use more ram to run the k8s cluster, we need to create `$HOME/.wslconfig` and paste the following content:

```shell
[wsl2]
memory=8GB
````