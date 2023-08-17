# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
user { 'holberton':
  ensure => present,
}

file { '/home/holberton/.bashrc':
  ensure  => file,
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0644',
  content => "ulimit -n 4096\n",
  require => User['holberton'],
}

file { '/etc/security/limits.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "*               soft    nofile          4096\n
              *               hard    nofile          8192\n
              root            soft    nofile          4096\n
              root            hard    nofile          8192\n",
}

exec { 'restart-user-session':
  command     => '/bin/su - holberton -c "exit"',
  refreshonly => true,
  require     => [File['/home/holberton/.bashrc'], File['/etc/security/limits.conf']],
}
