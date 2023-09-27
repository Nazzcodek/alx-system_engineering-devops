# manifest to configure a nginx server

# install nginx
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server block for the root URL
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80;
    server_name _;

    location / {
      root   /var/www/html;
      index  index.html;
    }

    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
  }",
  require => Package['nginx'],
}

# Create "Hello World!" HTML page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}


# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [File['/etc/nginx/sites-available/default'], File['/var/www/html/index.html']],
}
