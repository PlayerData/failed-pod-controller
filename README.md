# Failed Pod Controller

Kubernetes controller which watches for pods which have certain failure states
and removes them.

## Why?

https://github.com/kubernetes/kubernetes/issues/99986

Since the introduction of [Graceful node shutdown](https://kubernetes.io/docs/concepts/architecture/nodes/#graceful-node-shutdown),
pods which were running a node which was shutdown are left in the cluster with
a state of `Terminated`.

This leads to issues such as https://github.com/prometheus/prometheus/issues/10257,
and can lead to alerts firing unnecessarily.

## Configuration

Available Env Vars:

| Name                 | Description                               |
| -------------------- | ----------------------------------------- |
| `CONTROLLER_DRY_RUN` | If truthy, won't actually delete any pods |
