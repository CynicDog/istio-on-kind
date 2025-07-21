# istio-on-kind

## Create a `kind` cluster with custom configurations 

```bash 
kind create cluster --config kind-config.yml
```

## Install `istio` release on your host machine 

```bash
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.22.0 sh -
cd istio-1.22.0
export PATH=$PWD/bin:$PATH
```

