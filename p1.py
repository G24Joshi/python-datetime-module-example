from datetime import datetime
dt=datetime.now()
print(dt)
x=dt.strftime("%d-%m-%Y-%H:%M:%S")
file=f"filename_{x}.txt"
print(file)
#==========================================
class profile::base {
  include xscorp_base
  include xscorp_cisobase
  include xscorp_linux_ad_auth
  include xscorp_hardening
  include xscorp_dmcrypt
  class{'xscorp_zabbix': role => lookup('xscorp::zabbix::role', undef, undef, 'agent')}
  Class['::xscorp_cisobase'] -> Class['::xscorp_linux_ad_auth']
}

class profile::bind {
  include xscorp_bind
  include xscorp_dns_monitor
  include xscorp_frrouting
  Class[xscorp_bind] -> Class[xscorp_dns_monitor]
  Class[xscorp_frrouting] -> Class[xscorp_dns_monitor]
}

class role::bind {
  include profile::base
  include profile::bind
  include xscorp_packetbeat
  include xscorp_elastic_agent
  include xscorp_crowdstrike
}

node /^[a-z]{3}dns0(1|2).corp.sita.aero/ {
  include role::bind
}

node /^[a-z]{3}t[0-9]{3}-dns0(1|2).corp.sita.aero/ {
  include role::bind
}