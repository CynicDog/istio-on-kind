# istio-on-kind

## `kind` cluster with Calico CNI and MetalLB 

#### 1. Create a `kind` cluster with custom configurations with the default CNI disabled  
```bash 
kind create cluster --config kind-cluster-config.yml --name kind 
```
#### 2. Install Calico CNI 
```bash
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml
```
#### 3. Install MetalLB 
```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.10/config/manifests/metallb-native.yaml
```

#### 4. Configure MetalLB IP address pool 
```bash
kubectl apply -f metallb-config.yaml
```

<details><summary><code>metallb-config.yaml</code></summary>

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: lb-pool
  namespace: metallb-system
spec:
  addresses:
    - 172.18.255.200-172.18.255.240
    # Adjust this to match Docker's network: docker network inspect kind | jq '.[0].IPAM.Config[].Subnet'
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2adv
  namespace: metallb-system
```

</details>

#### 5. Create `LoadBalancer` type service and its nginx deployment 

```bash
kubectl apply f nginx-lb.yml 
```

<details><summary><code>nginx-lb.yml</code></summary>

```yaml
# nginx-lb.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
```

</details>

#### Port forward (if `kind` cluster is on Window/MacOS host machine)
```bash
kubectl port-forward svc/nginx-lb 8080:80
```

