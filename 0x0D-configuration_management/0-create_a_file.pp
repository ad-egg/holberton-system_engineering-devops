# creates a file called holberton in /tmp directory
file { '/tmp/holberton':
  path    => '/tmp/holberton',
  ensure  => file,
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
