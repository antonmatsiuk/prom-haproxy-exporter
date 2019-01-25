Ansible: HAProxy Prometheus Exporter
=========

Ansible role to install HAProxy prometheus exporter on Linux

Requirements
------------

haproxy is installed on the target host. 

Role Variables
--------------
Available variables with default values (see defaults/main.yml):

Variable defines whether to install golang runtime or not, set to false if already installed:
    
    golang_install: true
    
Variable defines whether to install supervisord or not, set to false if already installed:

    supervisor_install: true    
    
Location for GOPATH environment variable:

    golang_gopath_home: "/root/go"


Installation directory for haproxy_exporter 

    haproxy_exporter_home: "{{ golang_gopath_home }}/bin"
       

IP and Port on which haproxy exporter listens on the host. Change IP to a desirable value e.g. `{{ ansible_eth0.ipv4.address }}` 
to listen on a specific interface:

    haproxy_exporter_port: 9104
    haproxy_exporter_ip: "0.0.0.0"
    

Dependencies
------------

To install haproxy use e.g.: geerlingguy.haproxy
The role also imports `geerlingguy.supervisor` to install supervisord


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: antonmatsiuk.prom_haproxy_exporter }

License
-------

MIT / BSD

Author Information
------------------

DevOps / SRE / Cloud Engineer [Anton Matsiuk](https://github.com/antonmatsiuk)