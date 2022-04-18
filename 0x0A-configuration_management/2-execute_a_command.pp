# Creates a file in /tmp.
exec { 'puppet-lint':
command    => 'pkill killmenow',
path       => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
}
