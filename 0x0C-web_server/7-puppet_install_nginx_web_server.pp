# install nginx web server
class nginx_config {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure => present,
    content => "
      server {
        listen 80;
        root /var/www/html;
        index index.html;
        
        location / {
          try_files $uri $uri/ =404;
        }
        
        location /redirect_me {
          return 301 http://example.com/new_page;
        }
      }
    ",
    notify => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    hasstatus => true,
    hasrestart => true,
  }
}

include nginx_config
