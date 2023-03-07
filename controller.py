from os import environ

from kubernetes import client
import kopf


@kopf.on.field("Pod", field="status.phase")
def handle_phase_change(name, namespace, status, **_):
    api = client.CoreV1Api()

    if status["phase"] != "Failed":
        return

    if status["reason"] != "Terminated":
        return

    print(
        'Removing pod %s in namespace %s. Message was "%s"'
        % (name, namespace, status["message"])
    )

    api.delete_namespaced_pod(name=name, namespace=namespace)
