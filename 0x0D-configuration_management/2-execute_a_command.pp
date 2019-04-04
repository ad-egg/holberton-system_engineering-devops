# a Puppet manifest that uses the exec resource to pkill a process killmenow
exec { 'pkill killmenow':
  command => 'pkill killmenow'
}
