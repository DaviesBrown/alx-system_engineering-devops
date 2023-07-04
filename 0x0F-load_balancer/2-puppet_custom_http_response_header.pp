# Add a custom HTTP header with Puppet
exec { 'update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  before  => Package['nginx'],
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update'],
}

file_line { 'http_header':
  path    => '/etc/nginx/nginx.conf',
  line    => 'add_header X-Served-By $hostname;',
  match   => '^http\s*{',
  notify  => Exec['restart_nginx'],
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  path        => '/usr/bin',
  refreshonly => true,
}
