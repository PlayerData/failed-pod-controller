from os import environ
from kubernetes import client, config, watch


def handle_pod_event(client: client.CoreV1Api, event, dry_run):
    pod = event["object"]

    if pod.status.phase != "Failed":
        return

    if pod.status.reason != "Terminated":
        return

    print(
        'Removing pod %s in namespace %s. Message was "%s"'
        % (pod.metadata.name, pod.metadata.namespace, pod.status.message)
    )

    if dry_run:
        print("Dry run set - not continuing.")
        return

    client.delete_namespaced_pod(
        name=pod.metadata.name, namespace=pod.metadata.namespace
    )


def main():
    dry_run = environ.get("CONTROLLER_DRY_RUN")

    config.load_kube_config()

    v1 = client.CoreV1Api()

    w = watch.Watch()

    for event in w.stream(v1.list_pod_for_all_namespaces):
        handle_pod_event(v1, event, dry_run)


if __name__ == "__main__":
    main()
