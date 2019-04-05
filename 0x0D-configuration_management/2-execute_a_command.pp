# a Puppet manifest that uses the exec resource to pkill a process killmenow
exec { 'pkill -f killmenow':
  command => 'pkill -f killmenow',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
