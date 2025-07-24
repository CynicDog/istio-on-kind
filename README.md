# istio-on-kind

## With `docker-desktop` Kubernetes cluster distribution 

#### 1. Set Kubernetes context as `docker-desktop`  
```bash
kubectl config set-context docker-desktop  
```

#### 2. Install istio resources on the cluster 
```bash
istioctl install --set profile=demo -y  
```

#### 3. Intall add-ons on the cluster 
```bash
kubectl apply -f .\istio-1.26.2\samples\addons
```

> [!NOTE]
> To access Istio add-on UIs (like Kiali, Grafana, and Prometheus), you must port-forward the services from the istio-system namespace.
>
> Run the following commands each in a separate terminal, or use background processes/scripts to run them in parallel:
> ```bash
> istioctl dashboard jaeger
> istioctl dashboard kiali 
> istioctl dashboard grafana
> istioctl dashboard prometheus
> ```
