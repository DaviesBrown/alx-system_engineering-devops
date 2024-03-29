# This Puppet script enhances the Nginx server's capacity to manage higher traffic loads.

# Adjust the ULIMIT in the default configuration file
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/bin/'
}

# Restart the Nginx service
exec { 'restart-nginx':
  command => '/usr/sbin/service nginx restart'
}
