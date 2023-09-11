apiVersion: v1
kind: Pod
metadata:
  name: nginxwebserver
spec:
  containers:
    - name: demo
      image: bitnami/nginx:latest
