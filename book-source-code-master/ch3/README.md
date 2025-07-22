# Envoy & xDS APIs in Istio (Quick Overview)

## 🧭 What is Envoy?
[Envoy](https://www.envoyproxy.io/) is a high-performance, cloud-native proxy used for managing network traffic. It's commonly used as a **sidecar proxy** in service meshes like **Istio** to handle routing, load balancing, telemetry, and security.


## 📡 Dynamic Configuration with xDS APIs

Instead of loading all settings from static YAML files, **Envoy supports dynamic configuration** through a set of APIs known collectively as **xDS**:

- **LDS** (Listener Discovery Service): What ports Envoy listens on
- **RDS** (Route Discovery Service): How traffic is routed (paths, headers, etc.)
- **CDS** (Cluster Discovery Service): What services Envoy can talk to
- **EDS** (Endpoint Discovery Service): Actual IPs for services (like Pods)
- **SDS** (Secret Discovery Service): TLS certificates
- **ADS** (Aggregate Discovery Service): A single gRPC stream combining all of the above, to ensure ordering and consistency

> 💡 These APIs let Envoy update its config **at runtime** with **no restarts**.

## 🧠 How Istio Uses xDS

In Istio, the control plane component called **Pilot** generates the configurations (LDS, RDS, CDS, etc.) for all Envoy proxies.

### ✅ How it works:
1. Each Envoy sidecar starts up with a minimal **bootstrap config**
2. It connects to **Pilot** over gRPC at port `15010`
3. Envoy receives its full dynamic config using **ADS**
4. Config updates (e.g., new services, routes, certs) are pushed automatically

## 🔧 Example: Bootstrap Config in Istio

```yaml
dynamicResources:
  ldsConfig:
    ads: {}
  cdsConfig:
    ads: {}
  adsConfig:
    apiType: GRPC
    grpcServices:
    - envoyGrpc:
        clusterName: xds-grpc

staticResources:
  clusters:
  - name: xds-grpc
    type: STRICT_DNS
    connectTimeout: 10.000s
    hosts:
    - socketAddress:
        address: istio-pilot.istio-system
        portValue: 15010
````

> This tells Envoy to connect to Pilot (`istio-pilot.istio-system:15010`) and fetch all config via **ADS**.

## 🧪 Why this is powerful

* Centralized config management
* Live updates without restarting services
* Scalable to thousands of proxies
* Secure communication with automatic cert rotation (via SDS)

## 🔗 Related Links

* [Envoy xDS API Overview](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)
* [Istio Architecture](https://istio.io/latest/docs/architecture/)

# Envoy in Action

## Pull required images

```bash
docker pull envoyproxy/envoy:v1.19.0
docker pull curlimages/curl
docker pull citizenstig/httpbin
```

## Start the upstream service

```bash
docker run -d --name httpbin citizenstig/httpbin
```

This starts a simple HTTP server (`httpbin`) that echoes request data (headers, method, IPs, etc.).

```bash
docker run -it --rm --link httpbin curlimages/curl \
  curl -X GET http://httpbin:8000/headers
```

> `--link httpbin` enables the `curl` container to resolve `httpbin` as a hostname via Docker's legacy linking mechanism.

## Start the Envoy proxy

```bash
docker run --name proxy --link httpbin envoyproxy/envoy:v1.19.0 \
  --config-yaml "$(cat ./simple.yaml)"
```

This runs Envoy with a config (`simple.yaml`) that:

* Listens on port `15001`
* Routes all requests to a **cluster** named `httpbin_service`
* That cluster is defined to resolve to the container named `httpbin` on port `8000`

## Now test traffic through Envoy

```bash
docker run -it --rm --link proxy curlimages/curl \
   curl -X GET http://proxy:15001/headers
```

### How did it work?

* The `curl` request is sent to the **Envoy proxy** on port `15001`
* Envoy listens on that port, and matches the request using a listener and route defined in `simple.yaml`
* The route points to a **cluster** called `httpbin_service`
* In Envoy, a **cluster** is just a group of upstream endpoints (in this case, the single `httpbin` container at port `8000`)
* Because `--link httpbin` is used, Envoy can resolve the hostname `httpbin` to the right container IP
* Envoy forwards the request, receives the response from `httpbin`, and sends it back to `curl`
