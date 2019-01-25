import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_supervisord_running_and_enabled(host):
    haproxy_exporter = host.service('supervisord')
    assert haproxy_exporter.is_enabled


def test_haproxy_exporter_running(host):
    ansible_vars = \
        host.ansible("include_vars",
                     "file=../../defaults/main.yml")["ansible_facts"]
    haproxy_exporter_port = ansible_vars["haproxy_exporter_port"]
    haproxy_exporter_ip = ansible_vars["haproxy_exporter_ip"]
    socket = host.socket('tcp://%s:%s' % (haproxy_exporter_ip,
                                          haproxy_exporter_port))
    assert socket.is_listening
