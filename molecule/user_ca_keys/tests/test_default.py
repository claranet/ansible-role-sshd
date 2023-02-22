#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def get_server_ip(host):
    return host.addr(str(testinfra_hosts[0])).ipv4_addresses[0]


def test_ssh_certificat(host):
    assert host.file("/etc/ssh/trusted-claranet-ca.pub").exists
    assert host.run_test(
        f'ssh -i ~/.ssh/claranet/user_key admin@{get_server_ip(host)} -o CertificateFile=~/.ssh/claranet/user_key-cert.pub -o "StrictHostKeyChecking=no" cat /etc/passwd'
    ).rc == 0


def test_ssh_AuthorizedPrincipalsFile(host):
    principal_config = host.file(f"/etc/ssh/auth_principals/admin")
    assert principal_config.exists
    assert principal_config.contains("admin")


def test_config_file(host):
    assert host.run_test("sshd -t").rc == 0


def test_listen_ssh(host):
    assert host.socket("tcp://22").is_listening
