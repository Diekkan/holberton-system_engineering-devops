# Creates a file in /tmp.
file { '/etc/ssh/ssh_config':
ensure  => 'present',
owner   => 'root',
group   => 'root',
mode    => '0644',
content => "Host *\n   PasswordAuthentication no\n   IdentityFile ~/.ssh/school",
}
