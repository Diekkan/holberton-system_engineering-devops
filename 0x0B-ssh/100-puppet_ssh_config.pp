# Creates a file in /tmp.
file { '/etc/ssh/sshd_config':
ensure => 'present',
owner  => 'root',
group  => 'root',
mode   => '0600',
source => '/home/holberton-system_engineering-devops/0x0B-ssh/2-ssh_config',
}
