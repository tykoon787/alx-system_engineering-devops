# Setups an nginx server

# Variables
$doc_root = '/var/www/html'
$server_ip = '52.87.215.121'
# Install the server
## Update
exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

## Install the package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

file { $doc_root:
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0644'
}

file { "${doc_root}/index.html":
  ensure  => 'present',
  content => '<html><body><h1>Hello World!</h1></body></html>'
}

nginx::resource::server {'web-01':
  listen_port => '80',
  server_name => '$server_ip',

  location    => {
    '/'            => {
      content => '<html><body><h1>Hello World!</h1></body></html>'

    },
    '/redirect_me' => {
      return => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4'
    },
  },
}

file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  notify  => Service['nginx'],
  require => Package['nginx']
}

service { 'nginx':
  ensure=> running,
}

